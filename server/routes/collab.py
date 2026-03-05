import uuid
from fastapi import APIRouter, Depends, HTTPException, Request
from server.database import get_db, execute
from server.core.auth import user_from_token, utc_now_iso
from server.core.security import rate_limited
from server.core.validators import bounded_text, valid_email
from server.config import RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS
from server.models.collab import CollabCreateRequest, CollabApprovalRequest

router = APIRouter(prefix="/collaboration-requests", tags=["collab"])

def get_current_user(request: Request, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    user = user_from_token(db, auth_header)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user

@router.get("")
def get_collab_requests(request: Request, status: str = None, db=Depends(get_db)):
    actor = get_current_user(request, db)
    if actor["role_code"] not in ("moderator_t2", "admin"):
        raise HTTPException(status_code=403, detail="Hanya Moderator Tier 2/Admin")
    
    sql = """
        SELECT
            collaboration_requests.*,
            users.name AS reviewer_name,
            kecamatan.name AS scope_kecamatan_name,
            kelurahan.name AS scope_kelurahan_name
        FROM collaboration_requests
        LEFT JOIN users ON users.id = collaboration_requests.reviewed_by_user_id
        LEFT JOIN kecamatan ON kecamatan.id = collaboration_requests.scope_kecamatan_id
        LEFT JOIN kelurahan ON kelurahan.id = collaboration_requests.scope_kelurahan_id
        WHERE 1=1
    """
    params = []
    if status in ("pending", "approved", "rejected"):
        sql += " AND collaboration_requests.status = ?"
        params.append(status)
    sql += " ORDER BY collaboration_requests.created_at DESC"
    
    rows = db.execute(sql, tuple(params)).fetchall()
    requests = []
    for row in rows:
        requests.append({
            "id": row["id"],
            "organizationName": row["organization_name"],
            "picName": row["pic_name"],
            "email": row["email"],
            "supportType": row["support_type"],
            "contributionScope": row["contribution_scope"] or "kota",
            "scopeKecamatanId": row["scope_kecamatan_id"],
            "scopeKelurahanId": row["scope_kelurahan_id"],
            "scopeKecamatanName": row["scope_kecamatan_name"],
            "scopeKelurahanName": row["scope_kelurahan_name"],
            "supportDescription": row["support_description"],
            "status": row["status"],
            "reviewedByName": row["reviewer_name"],
            "reviewedAt": row["reviewed_at"],
            "createdAt": row["created_at"],
        })
    return {"requests": requests}

@router.post("")
def create_collab_request(payload: CollabCreateRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)

    organization_name = bounded_text(payload.organizationName, 180)
    pic_name = bounded_text(payload.picName, 120)
    email = str(payload.email or "").strip().lower()
    support_type = str(payload.supportType or "").strip().lower()
    contribution_scope = str(payload.contributionScope or "kota").strip().lower()
    support_description = bounded_text(payload.supportDescription, 2000)

    if not organization_name or not pic_name or not email or not support_type or not support_description:
        raise HTTPException(status_code=400, detail="Semua field kolaborasi wajib diisi")
    if support_type not in ("dana", "konsumsi", "peralatan", "media_partner", "lainnya"):
        raise HTTPException(status_code=400, detail="Jenis dukungan tidak valid")
    if contribution_scope not in ("kota", "kecamatan", "kelurahan"):
        raise HTTPException(status_code=400, detail="Skala kontribusi tidak valid")
    if not valid_email(email):
        raise HTTPException(status_code=400, detail="Format email tidak valid")

    scope_kecamatan_id = None
    scope_kelurahan_id = None
    if contribution_scope in ("kecamatan", "kelurahan"):
        try:
            scope_kecamatan_id = int(payload.kecamatanId)
        except Exception:
            raise HTTPException(status_code=400, detail="Kecamatan wajib dipilih untuk skala ini")
        kec = db.execute("SELECT id FROM kecamatan WHERE id = ?", (scope_kecamatan_id,)).fetchone()
        if not kec:
            raise HTTPException(status_code=400, detail="Kecamatan tidak ditemukan")

    if contribution_scope == "kelurahan":
        try:
            scope_kelurahan_id = int(payload.kelurahanId)
        except Exception:
            raise HTTPException(status_code=400, detail="Kelurahan wajib dipilih untuk skala kelurahan")
        kel = db.execute(
            "SELECT id FROM kelurahan WHERE id = ? AND kecamatan_id = ?",
            (scope_kelurahan_id, scope_kecamatan_id),
        ).fetchone()
        if not kel:
            raise HTTPException(status_code=400, detail="Kelurahan tidak sesuai kecamatan pilihan")
            
    req_id = f"collab-{uuid.uuid4().hex[:10]}"
    now = utc_now_iso()
    execute(
        db,
        """
        INSERT INTO collaboration_requests(
            id, organization_name, pic_name, email, support_type, contribution_scope,
            scope_kecamatan_id, scope_kelurahan_id, support_description,
            status, reviewed_by_user_id, reviewed_at, created_at, updated_at
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, 'pending', NULL, NULL, ?, ?)
        """,
        (
            req_id, organization_name, pic_name, email, support_type,
            contribution_scope, scope_kecamatan_id, scope_kelurahan_id, support_description,
            now, now,
        ),
    )
    db.commit()
    return {"success": True, "request": {"id": req_id}}

@router.post("/{req_id}/approval")
def approve_collab_request(req_id: str, payload: CollabApprovalRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    actor = get_current_user(request, db)
    if actor["role_code"] not in ("moderator_t2", "admin"):
        raise HTTPException(status_code=403, detail="Hanya Moderator Tier 2/Admin yang boleh approve")
    
    row = db.execute("SELECT id, status FROM collaboration_requests WHERE id = ?", (req_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Permintaan tidak ditemukan")
    if row["status"] != "pending":
        raise HTTPException(status_code=400, detail="Permintaan sudah diproses")
    
    now = utc_now_iso()
    execute(
        db,
        """
        UPDATE collaboration_requests
        SET status = ?, reviewed_by_user_id = ?, reviewed_at = ?, updated_at = ?
        WHERE id = ?
        """,
        ("approved" if payload.approved else "rejected", actor["id"], now, now, req_id),
    )
    db.commit()
    return {"success": True}
