"""One-off migration of the v1.2 physics records (schema 1.2) to schema 2.0.

Each old record data/programs/<id>.json becomes:
  data/universities/<uid>.json   university-wide fields, all 'Not stated' for now
                                 (the gap-fill research wave reads the graduate
                                 school pages and fills them)
  data/programs/<uid>--physics.json   the physics program, keeping every value it
                                 had. Old fee, waiver, GRE General, TOEFL and English
                                 values stay on the program as department-level
                                 statements, so nothing is lost or reassigned.
Run once: python3 scripts/migrate_v2.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UNI = json.loads((DATA / "universities.json").read_text())
REMAP = UNI["remap_v1"]
BY_ID = {u["id"]: u for u in UNI["universities"]}
UNI_FIELDS = ["app_fee", "fee_waiver", "gre_general", "toefl_min", "ielts_min", "english_waiver"]


def main():
    old_files = sorted(p for p in (DATA / "programs").glob("*.json") if "--" not in p.stem)
    (DATA / "universities").mkdir(exist_ok=True)
    for p in old_files:
        r = json.loads(p.read_text())
        uid = REMAP.get(r["id"], r["id"])
        u = BY_ID[uid]
        f = r["fields"]
        stub = {"code": "Not stated", "value": "Not stated on the pages checked so far", "quote": "", "url": r["program_page"]}
        uni = {
            "id": uid, "institution": u["name"], "country": r["country"], "region": r["region"],
            "grad_page": r["program_page"], "checked": r["checked"],
            "fields": {k: dict(stub) for k in UNI_FIELDS}, "notes": "",
        }
        (DATA / "universities" / f"{uid}.json").write_text(json.dumps(uni, indent=2, ensure_ascii=False) + "\n")
        fields = {
            "deadline": f["deadline"], "gre_subject": f["gre_physics"], "supervisor": f["supervisor"],
            "funding": f["funding"], "entry_route": f["entry_route"],
        }
        for k in ["app_fee", "fee_waiver", "gre_general", "toefl_min", "english_waiver"]:
            if f[k]["code"] != "Not stated":
                fields[k] = f[k]
        prog = {
            "id": f"{uid}--physics", "university": uid, "field": "physics", "also_fields": [],
            "department": r["department"], "program_page": r["program_page"], "checked": r["checked"],
            "fields": fields, "notes": r.get("notes", ""),
        }
        if u["kind"] == "school" or r["institution"] != u["name"]:
            prog["name"] = r["institution"] if u["kind"] == "school" else ""
            if not prog["name"]:
                del prog["name"]
        (DATA / "programs" / f"{uid}--physics.json").write_text(json.dumps(prog, indent=2, ensure_ascii=False) + "\n")
        p.unlink()
    print(f"migrated {len(old_files)} records")


if __name__ == "__main__":
    main()
