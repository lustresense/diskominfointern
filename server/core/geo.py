import re

from server.config import GEO_PATH


def parse_geo_data() -> list[dict]:
  content = GEO_PATH.read_text(encoding="utf-8")
  rows: list[dict] = []
  current = None
  in_kelurahan_block = False

  kec_code_pattern = re.compile(r"kode:\s*'(\d{7})'")
  kec_name_pattern = re.compile(r"nama:\s*'([^']+)'")
  kel_pattern = re.compile(
    r"\{\s*kode:\s*'(\d{10})'\s*,\s*nama:\s*'([^']+)'\s*,\s*kodepos:\s*\[([^\]]*)\]"
  )
  code_pattern = re.compile(r"'(\d{5})'")

  for raw_line in content.splitlines():
    line = raw_line.strip()
    if not line or line.startswith("//"):
      continue

    if current is None:
      code_match = kec_code_pattern.search(line)
      if code_match:
        current = {"kode": code_match.group(1), "nama": "", "kelurahan": []}
      continue

    if "kelurahan:" in line and "[" in line:
      in_kelurahan_block = True
      continue

    if in_kelurahan_block:
      if line.startswith("]"):
        in_kelurahan_block = False
        continue
      kel_match = kel_pattern.search(line)
      if kel_match:
        kel_code, kel_name, code_block = kel_match.groups()
        current["kelurahan"].append(
          {"kode": kel_code, "nama": kel_name, "kodepos": code_pattern.findall(code_block)}
        )
      continue

    if not current["nama"]:
      name_match = kec_name_pattern.search(line)
      if name_match:
        current["nama"] = name_match.group(1)
      continue

    if line.startswith("},") or line.startswith("}"):
      if current["kode"] and current["nama"]:
        rows.append(current)
      current = None
      in_kelurahan_block = False

  if current and current["kode"] and current["nama"]:
    rows.append(current)
  return rows


def get_geo_stats() -> dict[str, int]:
  parsed = parse_geo_data()
  kecamatan_total = len(parsed)
  kelurahan_total = sum(len(kec.get("kelurahan", [])) for kec in parsed)
  postal_codes = {
    code
    for kec in parsed
    for kel in kec.get("kelurahan", [])
    for code in kel.get("kodepos", [])
    if isinstance(code, str) and len(code) == 5
  }
  return {
    "kecamatan": kecamatan_total,
    "kelurahan": kelurahan_total,
    "kodepos": len(postal_codes),
  }
