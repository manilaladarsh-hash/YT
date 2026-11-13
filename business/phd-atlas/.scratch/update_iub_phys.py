import json
from pathlib import Path

# Update iub--physics.json
phys_path = Path("data/programs/iub--physics.json")
phys = json.load(open(phys_path, encoding="utf-8"))
phys["fields"]["supervisor"] = {
    "code": "Not required",
    "value": "Admission decisions are made centrally by the Graduate Admissions Committee; no pre-arranged faculty supervisor required before applying.",
    "quote": "Applicants will be notified of the decision of the admissions committee as soon as possible. In a typical year, final notifications are sent out by late April.",
    "url": "https://physics.indiana.edu/graduate/how-to-apply/index.html"
}

with open(phys_path, "w", encoding="utf-8") as f:
    json.dump(phys, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Updated iub--physics.json quote successfully!")
