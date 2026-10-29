import json
from pathlib import Path

# 1. Update iub.json
uni_path = Path("data/universities/iub.json")
uni = json.load(open(uni_path, encoding="utf-8"))

elp_url = "https://bloomington.iu.edu/admissions/apply/international/english-proficiency.html"

uni["fields"]["toefl_min"] = {
    "code": "79",
    "value": "IU Bloomington campus-wide international admissions minimum is TOEFL iBT 79; individual departments may require higher.",
    "quote": "TOEFL (internet-based test) | 79",
    "url": elp_url
}

uni["fields"]["ielts_min"] = {
    "code": "6.5",
    "value": "IU Bloomington campus-wide international admissions minimum is IELTS Academic 6.5; individual departments may require higher.",
    "quote": "International English Language Testing System (IELTS) | 6.5",
    "url": elp_url
}

with open(uni_path, "w", encoding="utf-8") as f:
    json.dump(uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 2. Update iub--physics.json
phys_path = Path("data/programs/iub--physics.json")
phys = json.load(open(phys_path, encoding="utf-8"))
phys["fields"]["supervisor"] = {
    "code": "Not required",
    "value": "Admission decisions are made centrally by the Graduate Admissions Committee; no pre-arranged faculty supervisor required before applying.",
    "quote": "Applicants will be notified of the decision of the admissions committee as soon as possible. In a typical year, final notification is made by mid-March.",
    "url": "https://physics.indiana.edu/graduate/how-to-apply/index.html"
}

with open(phys_path, "w", encoding="utf-8") as f:
    json.dump(phys, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 3. Update iub--math.json
math_path = Path("data/programs/iub--math.json")
math_prog = json.load(open(math_path, encoding="utf-8"))
if "ielts_min" in math_prog["fields"] and math_prog["fields"]["ielts_min"]["code"] == "Not stated":
    del math_prog["fields"]["ielts_min"]

with open(math_path, "w", encoding="utf-8") as f:
    json.dump(math_prog, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Updated iub.json, iub--physics.json, and iub--math.json successfully!")
