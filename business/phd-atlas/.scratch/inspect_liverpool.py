import csv, json
from pathlib import Path

recs = list(Path("data/programs").glob("liverpool--*.json"))
print(f"Total liverpool programs: {len(recs)}")

for p in sorted(recs):
    d = json.load(open(p, encoding="utf-8"))
    print(f"{p.name}: dept='{d.get('department')}' | page='{d.get('program_page')}'")

with open("handoff/audit_2026-10-31.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    defects = [row for row in r if "liverpool" in row.get("file", "")]
    print(f"Total defects for liverpool: {len(defects)}")
    for row in defects:
        print(f" - {row['check']} | {row['file']} | {row['field']} | {row['url']}")
