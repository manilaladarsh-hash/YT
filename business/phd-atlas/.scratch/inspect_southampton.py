import glob, json, csv

recs = glob.glob("data/programs/southampton--*.json")
print(f"Total southampton programs: {len(recs)}")
for p in sorted(recs):
    d = json.load(open(p, encoding="utf-8"))
    print(f"{p}: dept='{d.get('department')}' | page='{d.get('program_page')}'")

with open("handoff/audit_2026-10-31.csv", encoding="utf-8") as f:
    defects = [row for row in csv.DictReader(f) if "southampton" in row.get("file", "")]
    print(f"Total defects for southampton: {len(defects)}")
    for row in defects:
        print(f" - {row['check']} | {row['file']} | {row['field']} | {row['url']}")
