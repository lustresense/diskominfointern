import threading
import time
from fastapi import HTTPException, Request, Response, status
from server.config import IS_PRODUCTION, ALLOWED_ORIGINS, DEV_ALLOWED_ORIGINS

_rate_lock = threading.Lock()
_rate_hits = {}


def client_ip(request: Request):
  forwarded = request.headers.get("X-Forwarded-For", "")
  if forwarded:
    return forwarded.split(",")[0].strip()
  return request.client.host if request.client else "unknown"


def resolve_cors_origin(request: Request) -> str | None:
  origin = str(request.headers.get("Origin", "")).strip()
  if not origin:
    return None
  if origin in ALLOWED_ORIGINS:
    return origin
  if not IS_PRODUCTION and origin in DEV_ALLOWED_ORIGINS:
    return origin
  return None


def add_common_headers(response: Response, request: Request) -> None:
  response.headers["X-Content-Type-Options"] = "nosniff"
  response.headers["X-Frame-Options"] = "DENY"
  response.headers["Referrer-Policy"] = "no-referrer"
  response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
  response.headers["Cache-Control"] = "no-store"
  origin = resolve_cors_origin(request)
  if origin:
    response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Vary"] = "Origin"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"

  if IS_PRODUCTION:
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
    response.headers["Content-Security-Policy"] = (
      "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
      "font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'"
    )


def rate_limited(request: Request, bucket: str, limit: int, window_seconds: int):
  now = time.time()
  key = f"{bucket}:{client_ip(request)}"
  with _rate_lock:
    hits = _rate_hits.get(key, [])
    threshold = now - window_seconds
    hits = [item for item in hits if item >= threshold]
    if len(hits) >= limit:
      _rate_hits[key] = hits
      raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Terlalu banyak permintaan, coba lagi sebentar")
    hits.append(now)
    _rate_hits[key] = hits
