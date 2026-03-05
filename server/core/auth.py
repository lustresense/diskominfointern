import hmac
import json
import os
import secrets
import sqlite3
from datetime import datetime, timedelta, timezone
from hashlib import pbkdf2_hmac

from server.config import PBKDF2_ITERATIONS, SESSION_TTL_HOURS
from server.database import execute


def utc_now_iso() -> str:
  return datetime.now(timezone.utc).isoformat()


def hash_password(password: str) -> str:
  salt = os.urandom(16)
  digest = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS)
  return f"{salt.hex()}:{digest.hex()}"


def verify_password(password: str, encoded: str) -> bool:
  try:
    salt_hex, digest_hex = encoded.split(":", 1)
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(digest_hex)
  except Exception:
    return False
  got = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS)
  return hmac.compare_digest(got, expected)


def create_session(conn: sqlite3.Connection, user_id: str) -> str:
  token = secrets.token_urlsafe(48)
  now = utc_now_iso()
  expires = (datetime.now(timezone.utc) + timedelta(hours=SESSION_TTL_HOURS)).isoformat()
  execute(
    conn,
    "INSERT INTO sessions(token, user_id, expires_at, created_at) VALUES(?, ?, ?, ?)",
    (token, user_id, expires, now),
  )
  return token


def user_from_token(conn: sqlite3.Connection, auth_header: str | None):
  if not auth_header or not auth_header.startswith("Bearer "):
    return None
  token = auth_header.split(" ", 1)[1].strip()
  return conn.execute(
    """
    SELECT users.*
    FROM sessions
    JOIN users ON users.id = sessions.user_id
    WHERE sessions.token = ? AND sessions.expires_at > ?
    """,
    (token, utc_now_iso()),
  ).fetchone()


def get_user_payload(conn: sqlite3.Connection, user_row: sqlite3.Row) -> dict:
  kel = None
  kampung = None
  if user_row["kelurahan_id"]:
    kel = conn.execute(
      """
      SELECT kelurahan.id AS id, kelurahan.name AS kel_name, kecamatan.name AS kec_name
      FROM kelurahan JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
      WHERE kelurahan.id = ?
      """,
      (user_row["kelurahan_id"],),
    ).fetchone()
    total = conn.execute("SELECT total_xp FROM xp_kelurahan WHERE kelurahan_id = ?", (kel["id"],)).fetchone()
    volunteers = conn.execute(
      "SELECT COUNT(*) AS c FROM users WHERE kelurahan_id = ? AND role_code IN ('user','ksh')",
      (kel["id"],),
    ).fetchone()["c"]
    kampung = {
      "id": kel["id"],
      "name": kel["kel_name"],
      "kecamatan": kel["kec_name"],
      "xp": int(total["total_xp"]) if total else 0,
      "volunteers": int(volunteers),
    }

  pending = conn.execute(
    """
    SELECT COUNT(*) AS c
    FROM event_participation ep
    JOIN events e ON e.id = ep.event_id
    WHERE ep.user_id = ? AND ep.status = 'attended' AND ep.checklist_done = 0 AND e.status = 'completed'
    """,
    (user_row["id"],),
  ).fetchone()["c"]

  return {
    "id": user_row["id"],
    "name": user_row["name"],
    "email": user_row["email"],
    "role": "admin" if user_row["role_code"] == "admin" else ("moderator" if str(user_row["role_code"]).startswith("moderator_t") else "user"),
    "roleCode": user_row["role_code"],
    "isKsh": bool(user_row["is_ksh"]),
    "moderatorTier": user_row["moderator_tier"],
    "tier2Badge": user_row["tier2_badge"],
    "kelurahan": kel["kel_name"] if kel else None,
    "kecamatan": kel["kec_name"] if kel else None,
    "kampungId": kel["id"] if kel else None,
    "kampung": kampung,
    "points": int(user_row["points"]),
    "badges": json.loads(user_row["badges_json"] or "[]"),
    "hasPendingReport": bool(pending),
    "developerNote": "Definition of Kampung may shift in future (RW vs Kelurahan). Logic must stay flexible.",
  }


def can_create_event(user: sqlite3.Row) -> bool:
  return user["role_code"] in ("moderator_t1", "admin")


def can_approve_event(user: sqlite3.Row) -> bool:
  return user["role_code"] in ("moderator_t2", "admin")


def can_verify_report(user: sqlite3.Row) -> bool:
  return user["role_code"] in ("moderator_t2", "admin")
