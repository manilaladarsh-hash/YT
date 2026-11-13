import json
from pathlib import Path

data = json.load(open("data/universities.json", "r", encoding="utf-8"))
unis = data.get("universities", [])
existing = {f.stem for f in Path("data/universities").glob("*.json")}
missing = [u for u in unis if u["id"] not in existing]
print(f"Total in plan: {len(unis)}")
print(f"Existing: {len(existing)}")
print(f"Missing ({len(missing)}):")
by_country = {}
for m in missing:
    by_country.setdefault(m.get("country", "Unknown"), []).append(m)

for c, lst in by_country.items():
    print(f"=== {c} ({len(lst)}) ===")
    for u in lst:
        print(f"  {u['id']}: {u.get('name', '')}")
