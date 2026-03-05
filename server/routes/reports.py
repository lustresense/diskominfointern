import uuid
import json
from fastapi import APIRouter, Depends, HTTPException, Request
from server.database import get_db, execute
from server.core.auth import user_from_token, can_verify_report, utc_now_iso
from server.core.security import rate_limited
from server.core.validators import bounded_text
from server.core.xp import apply_xp
from server.config import RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS
from server.models.report import ReportCreateRequest, ReportVerifyRequest

router = APIRouter(prefix="/reports", tags=["reports"])

def get_current_user(request: Request, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    user = user_from_token(db, auth_header)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user

@router.get("")
def get_reports(request: Request, status: str = None, userId: str = None, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    if not user_from_token(db, auth_header):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    sql = "SELECT * FROM event_reports WHERE 1=1"
    params = []
    if status:
        sql += " AND status = ?"
        params.append(status)
    if userId:
        sql += " AND user_id = ?"
        params.append(userId)
    sql += " ORDER BY created_at DESC"
    
    rows = db.execute(sql, tuple(params)).fetchall()
    out = []
    for r in rows:
        out.append({
            "id": r["id"],
            "eventId": r["event_id"],
            "userId": r["user_id"],
            "participants": int(r["participants"]),
            "outcomeTags": json.loads(r["outcome_tags_json"] or "[]"),
            "photoUrl": r["photo_url"],
            "status": r["status"],
            "points": int(r["points_awarded"]),
            "createdAt": r["created_at"],
        })
    return {"reports": out}

@router.post("")
def create_report(payload: ReportCreateRequest, request: Request, db=Depends(get_db), actor=Depends(get_current_user)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    if actor["role_code"] not in ("user", "ksh"):
        raise HTTPException(status_code=403, detail="Hanya relawan/KSH yang dapat lapor")
    
    event_id = payload.eventId
    if not event_id:
        raise HTTPException(status_code=400, detail="Event ID wajib diisi")

    event = db.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event or event["status"] != "completed":
        raise HTTPException(status_code=400, detail="Laporan hanya setelah event selesai")
    
    part = db.execute(
        "SELECT * FROM event_participation WHERE event_id = ? AND user_id = ?",
        (event_id, actor["id"]),
    ).fetchone()
    if not part:
        raise HTTPException(status_code=400, detail="Relawan belum terdaftar pada event ini")

    try:
        participants = int(payload.participants)
    except Exception:
        raise HTTPException(status_code=400, detail="Jumlah peserta harus angka")
    if participants < 1 or participants > 10000:
        raise HTTPException(status_code=400, detail="Jumlah peserta harus 1-10000")

    outcome_tags = payload.outcomeTags
    if not isinstance(outcome_tags, list):
        raise HTTPException(status_code=400, detail="Outcome tags harus berbentuk array")
    if len(outcome_tags) > 20:
        raise HTTPException(status_code=400, detail="Outcome tags maksimal 20 item")
    safe_tags = [bounded_text(tag, 60) for tag in outcome_tags]

    photo_url = bounded_text(payload.photoUrl, 2_000_000)
    
    report_id = f"report-{uuid.uuid4().hex[:12]}"
    now = utc_now_iso()
    execute(
        db,
        """
        INSERT INTO event_reports(
            id, event_id, user_id, participants, checklist_json, outcome_tags_json, photo_url,
            status, points_awarded, created_at, updated_at
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, 'pending', 0, ?, ?)
        """,
        (
            report_id, event_id, actor["id"], participants,
            json.dumps({"attendance": True, "post_event": True}),
            json.dumps(safe_tags),
            photo_url,
            now, now,
        ),
    )
    execute(
        db,
        "UPDATE event_participation SET status = 'reported', checklist_done = 1, updated_at = ? WHERE event_id = ? AND user_id = ?",
        (now, event_id, actor["id"]),
    )
    db.commit()
    return {"success": True, "report": {"id": report_id}}

@router.post("/{report_id}/verify")
def verify_report(report_id: str, payload: ReportVerifyRequest, request: Request, db=Depends(get_db), actor=Depends(get_current_user)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    if not can_verify_report(actor):
        raise HTTPException(status_code=403, detail="Hanya Moderator Tier 2/Admin yang boleh verifikasi")
    
    report = db.execute("SELECT * FROM event_reports WHERE id = ?", (report_id,)).fetchone()
    if not report:
        raise HTTPException(status_code=404, detail="Report tidak ditemukan")
    if report["status"] != "pending":
        raise HTTPException(status_code=400, detail="Report sudah diproses")
    
    now = utc_now_iso()
    if payload.approved:
        event = db.execute("SELECT * FROM events WHERE id = ?", (report["event_id"],)).fetchone()
        gained = apply_xp(db, event, int(report["participants"]))
        execute(
            db,
            "UPDATE event_reports SET status = 'verified', points_awarded = ?, verified_by_user_id = ?, verified_at = ?, updated_at = ? WHERE id = ?",
            (gained, actor["id"], now, now, report_id),
        )
        execute(db, "UPDATE users SET points = points + 5, updated_at = ? WHERE id = ?", (now, report["user_id"]))
    else:
        execute(
            db,
            "UPDATE event_reports SET status = 'rejected', verified_by_user_id = ?, verified_at = ?, updated_at = ? WHERE id = ?",
            (actor["id"], now, now, report_id),
        )
    db.commit()
    return {"success": True}
