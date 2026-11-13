import csv

with open("handoff/audit_2026-10-31.csv", encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        if "cardiff" in row.get("file", ""):
            print(f"{row['check']} | {row['file']} | {row['field']} | {row['url']}")
