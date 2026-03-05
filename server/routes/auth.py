import hmac
import uuid

from fastapi import APIRouter, Depends, HTTPException, Request

from server.database import get_db, execute
from server.core.auth import hash_password, verify_password, create_session, user_from_token, get_user_payload, utc_now_iso
from server.core.security import rate_limited
from server.core.validators import bounded_text, valid_email, valid_password
from server.config import (
    ADMIN_LOGIN_PASSWORD,
    ADMIN_LOGIN_USERNAME,
    IS_PRODUCTION,
    RATE_LIMIT_AUTH_MAX,
    RATE_LIMIT_MUTATION_MAX,
    RATE_LIMIT_WINDOW_SECONDS,
)
from server.models.auth import SignupRequest, LoginRequest, AdminLoginRequest

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me")
def get_me(request: Request, db=Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    user = user_from_token(db, auth_header)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"user": get_user_payload(db, user)}

@router.post("/signup")
def signup(payload: SignupRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    try:
        rate_limited(request, "auth-signup", RATE_LIMIT_AUTH_MAX, RATE_LIMIT_WINDOW_SECONDS)
    except HTTPException:
        raise HTTPException(status_code=429, detail="Terlalu banyak percobaan signup, coba lagi nanti")

    if not payload.email or not payload.password or not payload.name:
        raise HTTPException(status_code=400, detail="Email, password, name wajib")

    email = str(payload.email).strip().lower()
    if not valid_email(email):
        raise HTTPException(status_code=400, detail="Format email tidak valid")
    if not valid_password(payload.password):
        raise HTTPException(status_code=400, detail="Password minimal 8 karakter dan kombinasi huruf-angka")

    name = bounded_text(payload.name, 120)
    nik = bounded_text(payload.nik or "", 32)
    rw = bounded_text(payload.rw or "", 16)
    kelurahan = bounded_text(payload.kelurahan, 120)

    if db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone():
        raise HTTPException(status_code=400, detail="Email sudah terdaftar")

    kel = db.execute(
        """
        SELECT kelurahan.id AS id, kecamatan.id AS kec_id
        FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        WHERE kelurahan.name = ? LIMIT 1
        """,
        (kelurahan,),
    ).fetchone()
    if not kel:
        raise HTTPException(status_code=400, detail="Kelurahan tidak ditemukan")

    user_id = str(uuid.uuid4())
    now = utc_now_iso()
    execute(
        db,
        """
        INSERT INTO users(
            id, name, email, password_hash, nik, rw, role_code, is_ksh, moderator_tier, email_verified,
            kelurahan_id, kecamatan_id, points, badges_json, created_at, updated_at
        )
        VALUES(?, ?, ?, ?, ?, ?, 'user', 0, NULL, 1, ?, ?, 0, '[]', ?, ?)
        """,
        (
            user_id,
            name,
            email,
            hash_password(payload.password),
            nik,
            rw,
            kel["id"],
            kel["kec_id"],
            now,
            now,
        ),
    )
    db.commit()
    user = db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    token = create_session(db, user_id)
    db.commit()
    return {"success": True, "token": token, "user": get_user_payload(db, user)}

@router.post("/login")
def login(payload: LoginRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    try:
        rate_limited(request, "auth-login", RATE_LIMIT_AUTH_MAX, RATE_LIMIT_WINDOW_SECONDS)
    except HTTPException:
        raise HTTPException(status_code=429, detail="Terlalu banyak percobaan login, coba lagi nanti")

    email = str(payload.email or "").strip().lower()
    if not valid_email(email):
        raise HTTPException(status_code=400, detail="Format email tidak valid")

    password = str(payload.password or "")
    user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if not user or not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Email/password salah")
    token = create_session(db, user["id"])
    db.commit()
    return {"success": True, "token": token, "user": get_user_payload(db, user)}

@router.post("/admin-login")
def admin_login(payload: AdminLoginRequest, request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    try:
        rate_limited(request, "auth-admin-login", RATE_LIMIT_AUTH_MAX, RATE_LIMIT_WINDOW_SECONDS)
    except HTTPException:
        raise HTTPException(status_code=429, detail="Terlalu banyak percobaan login admin, coba lagi nanti")

    if IS_PRODUCTION and (not ADMIN_LOGIN_USERNAME or not ADMIN_LOGIN_PASSWORD):
        raise HTTPException(status_code=403, detail="Admin login tidak dikonfigurasi untuk production")

    expected_username = ADMIN_LOGIN_USERNAME if ADMIN_LOGIN_USERNAME else "admin"
    expected_password = ADMIN_LOGIN_PASSWORD if ADMIN_LOGIN_PASSWORD else "admin"

    valid_user = hmac.compare_digest(payload.username, expected_username)
    valid_pass = hmac.compare_digest(payload.password, expected_password)

    if not valid_user or not valid_pass:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    admin = db.execute("SELECT * FROM users WHERE role_code = 'admin' LIMIT 1").fetchone()
    if not admin:
        raise HTTPException(status_code=500, detail="Akun admin tidak ditemukan")

    token = create_session(db, admin["id"])
    db.commit()
    return {"success": True, "token": token, "user": get_user_payload(db, admin)}

@router.post("/logout")
def logout(request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = auth_header.split(" ", 1)[1].strip()
    execute(db, "DELETE FROM sessions WHERE token = ?", (token,))
    db.commit()
    return {"success": True}


@router.delete("/logout")
def logout_delete_alias(request: Request, db=Depends(get_db)):
    rate_limited(request, "mutation", RATE_LIMIT_MUTATION_MAX, RATE_LIMIT_WINDOW_SECONDS)
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = auth_header.split(" ", 1)[1].strip()
    execute(db, "DELETE FROM sessions WHERE token = ?", (token,))
    db.commit()
    return {"success": True}
