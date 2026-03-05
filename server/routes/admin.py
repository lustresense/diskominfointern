import uuid
import json
from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, Request
from server.database import get_db, execute
from server.core.auth import user_from_token, utc_now_iso
from server.core.security import rate_limited
from server.core.validators import bounded_text
from server.config import RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS
from server.models.admin import AssignRoleRequest, RemoveRoleRequest, TempPointsRequest, TempBadgeRequest

router = APIRouter(prefix="/admin", tags=["admin"])

def get_admin_user(request: Request, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    user = user_from_token(db, auth_header)
    if not user or user["role_code"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return user

@router.get("/temporary-adjustments")
def get_adjustments(request: Request, db=Depends(get_db)):
    get_admin_user(request, db)
    rows = db.execute(
        """
        SELECT temporary_adjustments.*, users.name AS user_name
        FROM temporary_adjustments
        JOIN users ON users.id = temporary_adjustments.user_id
        ORDER BY temporary_adjustments.created_at DESC
        """
    ).fetchall()
    out = []
    for r in rows:
        value = json.loads(r["value_json"])
        out.append({
            "id": r["id"],
            "type": r["adjustment_type"],
            "value": value.get("points") if r["adjustment_type"] == "points" else value.get("badgeId", ""),
            "reason": r["reason"],
            "grantedAt": r["created_at"],
            "expiresAt": r["expires_at"],
            "targetUserName": r["user_name"],
        })
    return {"adjustments": out}

@router.post("/assign-role")
def assign_role(payload: AssignRoleRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    get_admin_user(request, db)
    badge = str(payload.tier2Badge).lower()
    if badge not in ("lurah", "camat"):
        badge = "lurah"
    execute(
        db,
        "UPDATE users SET role_code = 'moderator_t2', moderator_tier = 2, tier2_badge = ?, updated_at = ? WHERE id = ?",
        (badge, utc_now_iso(), payload.userId),
    )
    db.commit()
    return {"success": True}

@router.post("/remove-role")
def remove_role(payload: RemoveRoleRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    get_admin_user(request, db)
    execute(
        db,
        "UPDATE users SET role_code = 'user', moderator_tier = NULL, tier2_badge = NULL, updated_at = ? WHERE id = ?",
        (utc_now_iso(), payload.userId),
    )
    db.commit()
    return {"success": True}

@router.post("/add-temporary-points")
def add_temp_points(payload: TempPointsRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    get_admin_user(request, db)
    now = utc_now_iso()
    execute(db, "UPDATE users SET points = points + ?, updated_at = ? WHERE id = ?", (payload.points, now, payload.userId))
    execute(
        db,
        """
        INSERT INTO temporary_adjustments(id, user_id, adjustment_type, value_json, reason, expires_at, created_at)
        VALUES(?, ?, 'points', ?, ?, ?, ?)
        """,
        (
            str(uuid.uuid4()),
            payload.userId,
            json.dumps({"points": payload.points}),
            bounded_text(payload.reason, 300),
            (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat(),
            now,
        ),
    )
    db.commit()
    return {"success": True}

@router.post("/add-temporary-badge")
def add_temp_badge(payload: TempBadgeRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    get_admin_user(request, db)
    user = db.execute("SELECT badges_json FROM users WHERE id = ?", (payload.userId,)).fetchone()
    badges = json.loads(user["badges_json"] or "[]")
    badges.append({"id": payload.badgeId, "temporary": True})
    now = utc_now_iso()
    execute(db, "UPDATE users SET badges_json = ?, updated_at = ? WHERE id = ?", (json.dumps(badges), now, payload.userId))
    execute(
        db,
        """
        INSERT INTO temporary_adjustments(id, user_id, adjustment_type, value_json, reason, expires_at, created_at)
        VALUES(?, ?, 'badge', ?, ?, ?, ?)
        """,
        (
            str(uuid.uuid4()),
            payload.userId,
            json.dumps({"badgeId": payload.badgeId}),
            bounded_text(payload.reason, 300),
            (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat(),
            now,
        ),
    )
    db.commit()
    return {"success": True}
