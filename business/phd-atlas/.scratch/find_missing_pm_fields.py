import json
from pathlib import Path

PF = ["deadline", "gre_subject", "supervisor", "funding", "entry_route"]

missing_physics = []
missing_math = []

for p in sorted(Path("data/programs").glob("*--physics.json")):
    d = json.load(open(p, encoding="utf-8"))
    mf = [f for f in PF if d["fields"].get(f, {}).get("code") == "Not stated"]
    if mf:
        missing_physics.append((p.stem, d.get("program_page", ""), mf))

for p in sorted(Path("data/programs").glob("*--math.json")):
    d = json.load(open(p, encoding="utf-8"))
    mf = [f for f in PF if d["fields"].get(f, {}).get("code") == "Not stated"]
    if mf:
        missing_math.append((p.stem, d.get("program_page", ""), mf))

print(f"Physics programs with missing program fields ({len(missing_physics)}):")
for stem, url, mf in missing_physics[:25]:
    print(f"  {stem:<25}: {', '.join(mf)} | URL: {url[:70]}")

print(f"\nMath programs with missing program fields ({len(missing_math)}):")
for stem, url, mf in missing_math[:25]:
    print(f"  {stem:<25}: {', '.join(mf)} | URL: {url[:70]}")
