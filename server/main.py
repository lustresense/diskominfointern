from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.config import ALLOWED_ORIGINS, API_PREFIX, DEV_ALLOWED_ORIGINS, IS_PRODUCTION
from server.db.schema import init_schema
from server.database import connect_db
from server.core.xp import cleanup_adjustments
from server.core.security import add_common_headers
from server.routes import auth, events, reports, geo, collab, users, admin

app = FastAPI(title="SIMRP API", version="1.0.0")

origins = list(ALLOWED_ORIGINS)
if not IS_PRODUCTION:
    origins.extend(list(DEV_ALLOWED_ORIGINS))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=API_PREFIX)
app.include_router(events.router, prefix=API_PREFIX)
app.include_router(reports.router, prefix=API_PREFIX)
app.include_router(geo.router, prefix=API_PREFIX)
app.include_router(collab.router, prefix=API_PREFIX)
app.include_router(users.router, prefix=API_PREFIX)
app.include_router(admin.router, prefix=API_PREFIX)

@app.on_event("startup")
def on_startup():
    init_schema()

@app.middleware("http")
async def cleanup_middleware(request, call_next):
    try:
        conn = connect_db()
        cleanup_adjustments(conn)
        conn.commit()
        conn.close()
    except Exception:
        pass
    response = await call_next(request)
    add_common_headers(response, request)
    return response

@app.get(f"{API_PREFIX}/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
