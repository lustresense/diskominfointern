import uuid
from fastapi import APIRouter, Depends, HTTPException, Request
from server.database import get_db, execute
from server.core.auth import user_from_token, can_create_event, can_approve_event, utc_now_iso
from server.core.security import rate_limited
from server.core.validators import bounded_text
from server.config import RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS
from server.models.event import EventCreateRequest, EventApprovalRequest, EventCompleteRequest

router = APIRouter(prefix="/events", tags=["events"])

def get_current_user(request: Request, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    user = user_from_token(db, auth_header)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user

@router.get("")
def get_events(request: Request, status: str = None, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    actor = user_from_token(db, auth_header)
    if not actor:
        raise HTTPException(status_code=401, detail="Unauthorized")

    sql = """
        SELECT events.*, kelurahan.name AS kelurahan, kecamatan.name AS kecamatan
        FROM events
        LEFT JOIN kelurahan ON kelurahan.id = events.kelurahan_id
        LEFT JOIN kecamatan ON kecamatan.id = events.kecamatan_id
        WHERE 1=1
    """
    params = []
    if status:
        sql += " AND events.status = ?"
        params.append(status)
    if actor and actor["is_ksh"]:
        sql += " AND ((events.scope_type = 'kelurahan' AND events.kelurahan_id = ?) OR (events.scope_type = 'kecamatan' AND events.kecamatan_id = ?))"
        params.append(actor["kelurahan_id"])
        params.append(actor["kecamatan_id"])
    sql += " ORDER BY events.event_date ASC"
    
    rows = db.execute(sql, tuple(params)).fetchall()
    out = []
    for r in rows:
        participants = db.execute("SELECT user_id FROM event_participation WHERE event_id = ?", (r["id"],)).fetchall()
        out.append({
            "id": r["id"],
            "title": r["title"],
            "description": r["description"],
            "pillar": int(r["pillar"]),
            "date": r["event_date"],
            "time": r["event_time"],
            "location": r["location"],
            "quota": int(r["quota"]),
            "scopeType": r["scope_type"],
            "status": r["status"],
            "kelurahan": r["kelurahan"],
            "kecamatan": r["kecamatan"],
            "participants": [p["user_id"] for p in participants],
        })
    return {"events": out}

@router.post("")
def create_event(payload: EventCreateRequest, request: Request, db=Depends(get_db), actor=Depends(get_current_user)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    if not can_create_event(actor):
        raise HTTPException(status_code=403, detail="Hanya ASN Tier 1/Admin yang boleh input kegiatan")

    title = bounded_text(payload.title, 200)
    description = bounded_text(payload.description, 3000)
    time_text = bounded_text(payload.time, 16)
    location = bounded_text(payload.location, 220)
    date = str(payload.date or "").strip()
    scope_type = str(payload.scopeType or "kelurahan").strip().lower()
    if not title or not date:
        raise HTTPException(status_code=400, detail="Judul dan tanggal wajib diisi")
    if scope_type not in ("kelurahan", "kecamatan"):
        raise HTTPException(status_code=400, detail="Skala kegiatan harus kelurahan atau kecamatan")

    try:
        kecamatan_id = int(payload.kecamatanId)
    except Exception:
        raise HTTPException(status_code=400, detail="Kecamatan wajib dipilih")

    kelurahan_id = None
    if scope_type == "kelurahan":
        try:
            kelurahan_id = int(payload.kelurahanId)
        except Exception:
            raise HTTPException(status_code=400, detail="Untuk skala kelurahan, kelurahan wajib dipilih")

        check = db.execute(
            "SELECT id FROM kelurahan WHERE id = ? AND kecamatan_id = ?",
            (kelurahan_id, kecamatan_id),
        ).fetchone()
        if not check:
            raise HTTPException(status_code=400, detail="Kelurahan tidak cocok dengan kecamatan pilihan")
    else:
        kec_exists = db.execute("SELECT id FROM kecamatan WHERE id = ?", (kecamatan_id,)).fetchone()
        if not kec_exists:
            raise HTTPException(status_code=400, detail="Kecamatan tidak ditemukan")

    try:
        quota = int(payload.quota)
    except Exception:
        raise HTTPException(status_code=400, detail="Kuota harus angka")
    if quota < 0 or quota > 10000:
        raise HTTPException(status_code=400, detail="Kuota harus 0-10000")

    try:
        pillar = int(payload.pillar)
    except Exception:
        raise HTTPException(status_code=400, detail="Pilar harus angka")
    if pillar not in (1, 2, 3, 4):
        raise HTTPException(status_code=400, detail="Pilar harus 1-4")

    event_id = f"event-{uuid.uuid4().hex[:10]}"
    now = utc_now_iso()
    execute(
        db,
        """
        INSERT INTO events(
            id, title, description, pillar, event_date, event_time, location, quota,
            scope_type, kecamatan_id, kelurahan_id, created_by_user_id, status, created_at, updated_at
        )
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'draft', ?, ?)
        """,
        (
            event_id, title, description, pillar, date, time_text,
            location, quota, scope_type, kecamatan_id, kelurahan_id,
            actor["id"], now, now,
        ),
    )
    db.commit()
    return {"success": True, "event": {"id": event_id}}

@router.post("/{event_id}/approval")
def approve_event(event_id: str, payload: EventApprovalRequest, request: Request, db=Depends(get_db), actor=Depends(get_current_user)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    if not can_approve_event(actor):
        raise HTTPException(status_code=403, detail="Hanya Moderator Tier 2/Admin yang boleh approve")
    
    event = db.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    
    if actor["role_code"] == "moderator_t2":
        badge = (actor["tier2_badge"] or "").lower()
        if event["scope_type"] == "kelurahan":
            if badge != "lurah" or actor["kelurahan_id"] != event["kelurahan_id"]:
                raise HTTPException(status_code=403, detail="Draft skala kelurahan harus disetujui Lurah area terkait")
        elif event["scope_type"] == "kecamatan":
            if badge != "camat" or actor["kecamatan_id"] != event["kecamatan_id"]:
                raise HTTPException(status_code=403, detail="Draft skala kecamatan harus disetujui Camat area terkait")
    
    status_val = "published" if payload.approved else "draft"
    execute(
        db,
        "UPDATE events SET status = ?, published_at = ?, updated_at = ? WHERE id = ?",
        (status_val, utc_now_iso() if payload.approved else None, utc_now_iso(), event_id),
    )
    db.commit()
    return {"success": True}

@router.post("/{event_id}/join")
def join_event(event_id: str, request: Request, db=Depends(get_db), actor=Depends(get_current_user)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    if actor["role_code"] not in ("user", "ksh"):
        raise HTTPException(status_code=403, detail="Hanya relawan/KSH yang dapat mendaftar")
    
    pending = db.execute(
        """
        SELECT COUNT(*) AS c
        FROM event_participation ep
        JOIN events e ON e.id = ep.event_id
        WHERE ep.user_id = ? AND ep.status = 'attended' AND ep.checklist_done = 0 AND e.status = 'completed'
        """,
        (actor["id"],),
    ).fetchone()["c"]
    if pending > 0:
        raise HTTPException(status_code=400, detail="Laporan event sebelumnya belum lengkap")
    
    event = db.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event or event["status"] != "published":
        raise HTTPException(status_code=400, detail="Event belum dipublish")
    
    if int(event["quota"]) > 0:
        count = db.execute("SELECT COUNT(*) AS c FROM event_participation WHERE event_id = ?", (event_id,)).fetchone()["c"]
        if count >= int(event["quota"]):
            raise HTTPException(status_code=400, detail="Kuota penuh")
    
    execute(
        db,
        """
        INSERT OR IGNORE INTO event_participation(event_id, user_id, status, checklist_done, created_at, updated_at)
        VALUES(?, ?, 'registered', 0, ?, ?)
        """,
        (event_id, actor["id"], utc_now_iso(), utc_now_iso()),
    )
    db.commit()
    return {"success": True}

@router.post("/{event_id}/complete")
def complete_event(event_id: str, payload: EventCompleteRequest, request: Request, db=Depends(get_db), actor=Depends(get_current_user)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    if not actor["is_ksh"]:
        raise HTTPException(status_code=403, detail="Hanya KSH yang bisa menandai selesai")
    
    event = db.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
    if not event:
        raise HTTPException(status_code=404, detail="Event tidak ditemukan")
    
    if event["scope_type"] == "kelurahan" and event["kelurahan_id"] != actor["kelurahan_id"]:
        raise HTTPException(status_code=403, detail="Event di luar kelurahan KSH")
    if event["scope_type"] == "kecamatan" and event["kecamatan_id"] != actor["kecamatan_id"]:
        raise HTTPException(status_code=403, detail="Event di luar kecamatan KSH")
    if event["status"] != "published":
        raise HTTPException(status_code=400, detail="Event harus published sebelum completed")
    
    summary = str(payload.outputSummary or "").strip()
    if not summary:
        raise HTTPException(status_code=400, detail="Output summary wajib diisi")

    now = utc_now_iso()
    execute(
        db,
        """
        UPDATE events
        SET status = 'completed', output_summary = ?, completed_at = ?, completed_by_user_id = ?, updated_at = ?
        WHERE id = ?
        """,
        (summary, now, actor["id"], now, event_id),
    )
    execute(db, "UPDATE event_participation SET status = 'attended', updated_at = ? WHERE event_id = ?", (now, event_id))
    db.commit()
    return {"success": True}
