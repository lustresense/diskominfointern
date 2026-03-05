from fastapi import APIRouter, Depends, HTTPException, Request
from server.database import get_db
from server.core.auth import user_from_token
from server.core.geo import get_geo_stats

router = APIRouter(tags=["geo"])

@router.get("/kodepos/{code}")
def get_kodepos(code: str, db=Depends(get_db)):
    rows = db.execute(
        """
        SELECT postal_codes.code AS kodepos, kelurahan.name AS kelurahan, kecamatan.name AS kecamatan
        FROM postal_codes
        JOIN kampung_mapping ON kampung_mapping.postal_code_id = postal_codes.id
        JOIN kelurahan ON kelurahan.id = kampung_mapping.kelurahan_id
        JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        WHERE postal_codes.code = ?
        ORDER BY kelurahan.name
        """,
        (code,),
    ).fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="Kodepos tidak ditemukan")
    payload = [{"kelurahan": r["kelurahan"], "kecamatan": r["kecamatan"]} for r in rows]
    return {"kodepos": code, "kelurahan": payload}

@router.get("/geo/options")
def get_geo_options(db=Depends(get_db)):
    rows = db.execute(
        """
        SELECT
            kecamatan.id AS kec_id,
            kecamatan.name AS kec_name,
            kelurahan.id AS kel_id,
            kelurahan.name AS kel_name,
            postal_codes.code AS kodepos
        FROM kampung_mapping
        JOIN kelurahan ON kelurahan.id = kampung_mapping.kelurahan_id
        JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        JOIN postal_codes ON postal_codes.id = kampung_mapping.postal_code_id
        ORDER BY kecamatan.name ASC, kelurahan.name ASC, postal_codes.code ASC
        """
    ).fetchall()
    grouped = {}
    for row in rows:
        if row["kec_id"] not in grouped:
            grouped[row["kec_id"]] = {"id": row["kec_id"], "name": row["kec_name"], "kelurahan": [], "_kel_idx": {}}
        if row["kel_id"] is not None:
            key = row["kel_id"]
            if key not in grouped[row["kec_id"]]["_kel_idx"]:
                grouped[row["kec_id"]]["_kel_idx"][key] = len(grouped[row["kec_id"]]["kelurahan"])
                grouped[row["kec_id"]]["kelurahan"].append({"id": row["kel_id"], "name": row["kel_name"], "kodepos": []})
            kel_idx = grouped[row["kec_id"]]["_kel_idx"][key]
            if row["kodepos"] is not None and row["kodepos"] not in grouped[row["kec_id"]]["kelurahan"][kel_idx]["kodepos"]:
                grouped[row["kec_id"]]["kelurahan"][kel_idx]["kodepos"].append(row["kodepos"])
    result = []
    for kec in grouped.values():
        out = {"id": kec["id"], "name": kec["name"], "kelurahan": kec["kelurahan"]}
        result.append(out)
    return {"kecamatan": result}

@router.get("/geo/stats")
def geo_stats():
    stats = get_geo_stats()
    return {
        "stats": {
            "kecamatan": int(stats["kecamatan"]),
            "kelurahan": int(stats["kelurahan"]),
            "kodepos": int(stats["kodepos"]),
        }
    }

@router.get("/landing/leaderboard")
def landing_leaderboard(db=Depends(get_db)):
    rows = db.execute(
        """
        SELECT kelurahan.name AS kelurahan, kecamatan.name AS kecamatan, xp_kelurahan.total_xp AS xp
        FROM xp_kelurahan
        JOIN kelurahan ON kelurahan.id = xp_kelurahan.kelurahan_id
        JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        WHERE EXISTS (
            SELECT 1 FROM kampung_mapping WHERE kampung_mapping.kelurahan_id = kelurahan.id
        )
        ORDER BY xp_kelurahan.total_xp DESC, kelurahan.name ASC
        LIMIT 7
        """
    ).fetchall()
    entries = [
        {
            "rank": idx + 1,
            "kelurahan": row["kelurahan"],
            "kecamatan": row["kecamatan"],
            "xp": int(row["xp"]),
        }
        for idx, row in enumerate(rows)
    ]
    return {"leaderboard": entries}

@router.get("/kampung")
def get_kampung(request: Request, db=Depends(get_db)):
    actor = user_from_token(db, request.headers.get("Authorization"))
    if not actor:
        raise HTTPException(status_code=401, detail="Unauthorized")

    rows = db.execute(
        """
        SELECT kelurahan.id AS id, kelurahan.name AS name, kecamatan.name AS kecamatan, xp_kelurahan.total_xp AS xp
        FROM kelurahan
        JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        JOIN xp_kelurahan ON xp_kelurahan.kelurahan_id = kelurahan.id
        WHERE EXISTS (
            SELECT 1 FROM kampung_mapping WHERE kampung_mapping.kelurahan_id = kelurahan.id
        )
        ORDER BY xp_kelurahan.total_xp DESC, kelurahan.name ASC
        LIMIT 100
        """
    ).fetchall()
    data = [{"id": r["id"], "name": r["name"], "kecamatan": r["kecamatan"], "xp": int(r["xp"])} for r in rows]
    return {"kampung": data}


@router.get("/recommendations")
def recommendations_get():
    raise HTTPException(status_code=410, detail="ASN recommendation is off-system")


@router.post("/recommendations")
def recommendations_post():
    raise HTTPException(status_code=410, detail="ASN recommendation is off-system")
