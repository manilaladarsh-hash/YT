import json
from pathlib import Path

# Update clemson.json
uni_path = Path("data/universities/clemson.json")
uni = json.load(open(uni_path, encoding="utf-8"))

elp_url = "https://www.clemson.edu/admissions/graduate-admissions/apply/international-applicants/elp-requirement.html"

uni["fields"]["toefl_min"] = {
    "code": "4.0 (new scale)",
    "value": "Clemson University minimum requirement is TOEFL iBT 4.0 on the 1-6 scale (MyBest scores allowed). Individual programs may set higher requirements.",
    "quote": "Minimum Score Requirements | TOEFL iBT (MyBest Scores allowed) | 4.0 | Please note, the minimum score requirements listed above are the minimum required by the University.",
    "url": elp_url
}

uni["fields"]["ielts_min"] = {
    "code": "6.5",
    "value": "Clemson University minimum requirement is IELTS 6.5 overall. Individual programs may set higher requirements.",
    "quote": "Minimum Score Requirements | IELTS | 6.5 | Please note, the minimum score requirements listed above are the minimum required by the University.",
    "url": elp_url
}

with open(uni_path, "w", encoding="utf-8") as f:
    json.dump(uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# Update clemson--math.json to remove Not stated overrides
math_path = Path("data/programs/clemson--math.json")
math_prog = json.load(open(math_path, encoding="utf-8"))
del math_prog["fields"]["toefl_min"]
del math_prog["fields"]["ielts_min"]

with open(math_path, "w", encoding="utf-8") as f:
    json.dump(math_prog, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Updated clemson.json and clemson--math.json successfully!")
