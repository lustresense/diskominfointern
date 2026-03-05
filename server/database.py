import sqlite3
from server.config import DB_PATH, IS_PRODUCTION

def open_sqlite(path):
    conn = sqlite3.connect(str(path), timeout=30)
    conn.row_factory = sqlite3.Row
    if IS_PRODUCTION:
        conn.execute("PRAGMA journal_mode = WAL")
        conn.execute("PRAGMA synchronous = NORMAL")
    else:
        conn.execute("PRAGMA journal_mode = MEMORY")
        conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA temp_store = MEMORY")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def connect_db():
    return open_sqlite(DB_PATH)

def execute(conn, sql, params=()):
    cur = conn.execute(sql, params)
    return cur

def get_db():
    conn = connect_db()
    try:
        yield conn
    finally:
        conn.close()