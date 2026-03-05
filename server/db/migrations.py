from server.database import execute

def migrate_schema(conn):
    user_cols = {row["name"] for row in conn.execute("PRAGMA table_info(users)").fetchall()}
    if "tier2_badge" not in user_cols:
        execute(conn, "ALTER TABLE users ADD COLUMN tier2_badge TEXT")

    collab_cols = {row["name"] for row in conn.execute("PRAGMA table_info(collaboration_requests)").fetchall()}
    if "contribution_scope" not in collab_cols:
        execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN contribution_scope TEXT NOT NULL DEFAULT 'kota'")
    if "scope_kecamatan_id" not in collab_cols:
        execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN scope_kecamatan_id INTEGER")
    if "scope_kelurahan_id" not in collab_cols:
        execute(conn, "ALTER TABLE collaboration_requests ADD COLUMN scope_kelurahan_id INTEGER")

    event_cols = conn.execute("PRAGMA table_info(events)").fetchall()
    names = {row["name"] for row in event_cols}
    kel_notnull = 1
    for row in event_cols:
        if row["name"] == "kelurahan_id":
            kel_notnull = int(row["notnull"])
            break
    needs_event_migration = (
        "scope_type" not in names or
        "kecamatan_id" not in names or
        kel_notnull == 1
    )
    if not needs_event_migration:
        return

    execute(conn, "ALTER TABLE events RENAME TO events_legacy")
    execute(
        conn,
        """
        CREATE TABLE events (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            pillar INTEGER NOT NULL,
            event_date TEXT NOT NULL,
            event_time TEXT,
            location TEXT,
            quota INTEGER NOT NULL DEFAULT 0,
            scope_type TEXT NOT NULL CHECK(scope_type IN ('kelurahan','kecamatan')),
            kecamatan_id INTEGER NOT NULL,
            kelurahan_id INTEGER,
            created_by_user_id TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('draft','approved','published','completed')),
            output_summary TEXT,
            published_at TEXT,
            completed_at TEXT,
            completed_by_user_id TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            FOREIGN KEY (kecamatan_id) REFERENCES kecamatan(id),
            FOREIGN KEY (kelurahan_id) REFERENCES kelurahan(id),
            FOREIGN KEY (created_by_user_id) REFERENCES users(id)
        )
        """,
    )
    legacy_cols = {row["name"] for row in conn.execute("PRAGMA table_info(events_legacy)").fetchall()}
    if "kecamatan_id" in legacy_cols:
        kec_expr = "COALESCE(events_legacy.kecamatan_id, (SELECT kecamatan_id FROM kelurahan WHERE id = events_legacy.kelurahan_id))"
    else:
        kec_expr = "(SELECT kecamatan_id FROM kelurahan WHERE id = events_legacy.kelurahan_id)"
    execute(
        conn,
        f"""
        INSERT INTO events(
            id, title, description, pillar, event_date, event_time, location, quota,
            scope_type, kecamatan_id, kelurahan_id, created_by_user_id, status,
            output_summary, published_at, completed_at, completed_by_user_id, created_at, updated_at
        )
        SELECT
            events_legacy.id,
            events_legacy.title,
            events_legacy.description,
            events_legacy.pillar,
            events_legacy.event_date,
            events_legacy.event_time,
            events_legacy.location,
            events_legacy.quota,
            'kelurahan',
            {kec_expr},
            events_legacy.kelurahan_id,
            events_legacy.created_by_user_id,
            CASE WHEN events_legacy.status = 'rejected' THEN 'draft' ELSE events_legacy.status END,
            events_legacy.output_summary,
            events_legacy.published_at,
            events_legacy.completed_at,
            events_legacy.completed_by_user_id,
            events_legacy.created_at,
            events_legacy.updated_at
        FROM events_legacy
        """,
    )
    execute(conn, "DROP TABLE events_legacy")