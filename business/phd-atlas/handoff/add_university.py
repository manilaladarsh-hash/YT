"""Add one university to data/universities.json safely.

Usage: python3 handoff/add_university.py <id> "<official name>" "<state or region>" [country]
Example: python3 handoff/add_university.py umassboston "University of Massachusetts Boston" "Massachusetts"
"""

import json
import re
import sys
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "universities.json"

if len(sys.argv) not in (4, 5):
    sys.exit(__doc__)
uid, name, region = sys.argv[1:4]
country = sys.argv[4] if len(sys.argv) == 5 else "USA"
if not re.fullmatch(r"[a-z][a-z0-9-]{1,30}", uid):
    sys.exit("id must be lowercase letters/digits, like umassboston")
d = json.loads(P.read_text(encoding="utf-8"))
if any(u["id"] == uid for u in d["universities"]):
    sys.exit(f"id {uid} already exists: pick another")
if any(u["name"].lower() == name.lower() for u in d["universities"]):
    sys.exit(f"{name} is already in the list")
regions = {u["region"] for u in d["universities"] if u["country"] == country}
if regions and region not in regions:
    print(f"note: region '{region}' is new for {country}. Existing examples: {sorted(regions)[:8]}")
d["universities"].append({"id": uid, "name": name, "country": country, "region": region, "kind": "university", "wave": 5})
P.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
print(f"added {uid}: {name} ({region}, {country})")
