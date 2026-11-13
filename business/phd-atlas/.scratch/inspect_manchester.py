import csv, json
from pathlib import Path

recs = list(Path("data/programs").glob("manchester--*.json"))
print(f"Total manchester programs: {len(recs)}")

for p in sorted(recs):
    d = json.load(open(p, encoding="utf-8"))
    print(f"{p.name}: dept='{d.get('department')}' | page='{d.get('program_page')}'")

with open("handoff/audit_2026-10-31.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    defects = [row for row in r if "manchester" in row.get("file", "")]
    print(f"Total defects for manchester: {len(defects)}")
    for row in defects[:10]:
        print(f" - {row['check']} | {row['file']} | {row['field']} | {row['url']}")
