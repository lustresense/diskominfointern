import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_DIR = ROOT_DIR / "database"
DB_PATH = Path(os.environ.get("SIMRP_DB_PATH", str(DB_DIR / "runtime" / "database.db")))
GEO_PATH = ROOT_DIR / "src" / "data" / "geographicData.ts"
API_PREFIX = "/make-server-32aa5c5c"

APP_ENV = str(os.environ.get("SIMRP_ENV", "development")).strip().lower()
IS_PRODUCTION = APP_ENV in ("prod", "production")
PBKDF2_ITERATIONS = int(os.environ.get("SIMRP_PBKDF2_ITERATIONS", "210000"))
MAX_BODY_BYTES = int(os.environ.get("SIMRP_MAX_BODY_BYTES", str(8 * 1024 * 1024)))
SESSION_TTL_HOURS = int(os.environ.get("SIMRP_SESSION_TTL_HOURS", "24" if IS_PRODUCTION else "168"))
RATE_LIMIT_WINDOW_SECONDS = int(os.environ.get("SIMRP_RATE_LIMIT_WINDOW_SECONDS", "60"))
RATE_LIMIT_AUTH_MAX = int(os.environ.get("SIMRP_RATE_LIMIT_AUTH_MAX", "10"))
RATE_LIMIT_MUTATION_MAX = int(os.environ.get("SIMRP_RATE_LIMIT_MUTATION_MAX", "120"))

DEV_ALLOWED_ORIGINS = {
    "http://localhost:5173",
    "http://127.0.0.1:5173",
}
raw_allowed_origins = str(os.environ.get("SIMRP_ALLOWED_ORIGINS", "")).strip()
ALLOWED_ORIGINS = {item.strip() for item in raw_allowed_origins.split(",") if item.strip()}

ADMIN_LOGIN_USERNAME = str(os.environ.get("SIMRP_ADMIN_LOGIN_USERNAME", "")).strip()
ADMIN_LOGIN_PASSWORD = str(os.environ.get("SIMRP_ADMIN_LOGIN_PASSWORD", "")).strip()