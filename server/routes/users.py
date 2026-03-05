from fastapi import APIRouter, Depends, HTTPException, Request
from server.database import get_db, execute
from server.core.auth import user_from_token, get_user_payload, utc_now_iso
from server.core.security import rate_limited
from server.core.validators import bounded_text
from server.config import RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/users", tags=["users"])

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    rw: Optional[str] = None
    nik: Optional[str] = None

def get_current_user(request: Request, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    user = user_from_token(db, auth_header)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user

@router.get("")
def get_users(request: Request, role: str = None, kampungId: int = None, db=Depends(get_db)):
    get_current_user(request, db)
    
    sql = """
        SELECT users.*, kelurahan.name AS kel_name, kecamatan.name AS kec_name
        FROM users
        LEFT JOIN kelurahan ON kelurahan.id = users.kelurahan_id
        LEFT JOIN kecamatan ON kecamatan.id = users.kecamatan_id
        WHERE 1=1
    """
    params = []
    if role == "user":
        sql += " AND users.role_code IN ('user','ksh')"
    if kampungId:
        sql += " AND users.kelurahan_id = ?"
        params.append(int(kampungId))
    sql += " ORDER BY users.name ASC"
    
    rows = db.execute(sql, tuple(params)).fetchall()
    users = []
    for r in rows:
        users.append({
            "id": r["id"],
            "name": r["name"],
            "email": r["email"],
            "role": "admin" if r["role_code"] == "admin" else ("moderator" if str(r["role_code"]).startswith("moderator_t") else "user"),
            "roleCode": r["role_code"],
            "isKsh": bool(r["is_ksh"]),
            "moderatorTier": r["moderator_tier"],
            "tier2Badge": r["tier2_badge"],
            "kecamatan": r["kec_name"],
            "kelurahan": r["kel_name"],
            "kampungId": r["kelurahan_id"],
            "points": int(r["points"]),
        })
    return {"users": users}

@router.put("/{user_id}")
def update_user(user_id: str, payload: UserUpdateRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    actor = get_current_user(request, db)
    if actor["id"] != user_id and actor["role_code"] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    
    fields = []
    params = []
    if payload.name is not None:
        fields.append("name = ?")
        params.append(bounded_text(payload.name, 120))
    if payload.rw is not None:
        fields.append("rw = ?")
        params.append(bounded_text(payload.rw, 16))
    if payload.nik is not None:
        fields.append("nik = ?")
        params.append(bounded_text(payload.nik, 32))
        
    if not fields:
        raise HTTPException(status_code=400, detail="No fields")
        
    fields.append("updated_at = ?")
    params.append(utc_now_iso())
    params.append(user_id)
    
    execute(db, f"UPDATE users SET {', '.join(fields)} WHERE id = ?", tuple(params))
    db.commit()
    row = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return {"success": True, "user": get_user_payload(db, row)}
