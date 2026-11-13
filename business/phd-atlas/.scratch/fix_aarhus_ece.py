import json
import pathlib

src = pathlib.Path("data/programs/aarhus--ece.json")
dst_dir = pathlib.Path("data/staging/programs")
dst_dir.mkdir(parents=True, exist_ok=True)
d = json.loads(src.read_text(encoding="utf-8"))
d["checked"] = "2026-11-12"
d["fields"]["deadline"]["value"] = "Listed deadlines are per position; for example the Physical AI position closes 4 Jan 2027 (23:59 CET)."
d["fields"]["deadline"]["quote"] = "2027/01/04 23:59 CET | PhD in Physical AI for Adaptive Robot Manipulation"
(dst_dir / "aarhus--ece.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Staged aarhus--ece.json")
