from server.database import execute
from server.core.auth import utc_now_iso

def apply_xp(conn, event_row, participants):
    kelurahan_id = event_row["kelurahan_id"]
    pillar = int(event_row["pillar"])
    base = 20 + (participants * 2)
    rows = conn.execute("SELECT pillar, xp FROM xp_pillar WHERE kelurahan_id = ?", (kelurahan_id,)).fetchall()
    pillar_map = {int(r["pillar"]): int(r["xp"]) for r in rows}
    total = sum(pillar_map.values())
    avg = total / 4 if total else 0
    p_value = pillar_map.get(pillar, 0)
    multiplier = 1.0
    if total > 0 and p_value > avg * 1.2:
        multiplier = 0.7
    elif total > 0 and p_value < avg * 0.8:
        multiplier = 1.3
    gained = int(round(base * multiplier))
    now = utc_now_iso()
    execute(
        conn,
        "UPDATE xp_pillar SET xp = xp + ?, updated_at = ? WHERE kelurahan_id = ? AND pillar = ?",
        (gained, now, kelurahan_id, pillar),
    )
    execute(
        conn,
        "UPDATE xp_kelurahan SET total_xp = total_xp + ?, updated_at = ? WHERE kelurahan_id = ?",
        (gained, now, kelurahan_id),
    )
    return gained

def cleanup_adjustments(conn):
    import json
    from datetime import datetime, timezone
    now = utc_now_iso()
    rows = conn.execute("SELECT * FROM temporary_adjustments WHERE expires_at <= ?", (now,)).fetchall()
    for row in rows:
        if row["adjustment_type"] == "points":
            value = json.loads(row["value_json"])
            execute(conn, "UPDATE users SET points = points - ? WHERE id = ?", (int(value.get("points", 0)), row["user_id"]))
        if row["adjustment_type"] == "badge":
            value = json.loads(row["value_json"])
            user = conn.execute("SELECT badges_json FROM users WHERE id = ?", (row["user_id"],)).fetchone()
            badges = json.loads(user["badges_json"] or "[]")
            badge_id = value.get("badgeId")
            badges = [item for item in badges if item.get("id") != badge_id]
            execute(conn, "UPDATE users SET badges_json = ? WHERE id = ?", (json.dumps(badges), row["user_id"]))
    execute(conn, "DELETE FROM temporary_adjustments WHERE expires_at <= ?", (now,))