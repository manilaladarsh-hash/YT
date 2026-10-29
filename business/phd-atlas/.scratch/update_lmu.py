import json
from pathlib import Path

# 1. Update lmu.json
uni_path = Path("data/universities/lmu.json")
uni = json.load(open(uni_path, encoding="utf-8"))

lsm_url = "https://www.bio.lmu.de/lsm/en/become-an-lsm-student/"
gc_url = "https://www.lmu.de/graduatecenter/en/prospective-doctoral-researchers/"

uni["fields"]["app_fee"] = {
    "code": "0 (no fee)",
    "value": "LMU charges no application or tuition fees for doctoral studies.",
    "quote": "There are no application or tuition fees.",
    "url": lsm_url
}

uni["fields"]["fee_waiver"] = {
    "code": "No fee",
    "value": "No application fee is charged, so no waiver is needed.",
    "quote": "There are no application or tuition fees.",
    "url": lsm_url
}

uni["fields"]["gre_general"] = {
    "code": "Not required",
    "value": "LMU has no central office that accepts applications or requires the GRE; individual doctoral regulations specify requirements.",
    "quote": "There is no central office at LMU that accepts applications for individual doctoral studies.",
    "url": gc_url
}

with open(uni_path, "w", encoding="utf-8") as f:
    json.dump(uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 2. Update lmu--physics.json
phys_path = Path("data/programs/lmu--physics.json")
phys = json.load(open(phys_path, encoding="utf-8"))
phys["fields"]["funding"] = {
    "code": "Competitive",
    "value": "Doctoral researchers secure funding through competitive scholarships, external research project positions, or employment contracts.",
    "quote": "Numerous foundations and funding agencies award doctoral scholarships through competitive selection processes.",
    "url": gc_url
}
with open(phys_path, "w", encoding="utf-8") as f:
    json.dump(phys, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 3. Update lmu--math.json
math_path = Path("data/programs/lmu--math.json")
math_prog = json.load(open(math_path, encoding="utf-8"))
math_prog["fields"]["funding"] = {
    "code": "Competitive",
    "value": "Doctoral researchers secure funding through competitive scholarships, external research project positions, or employment contracts.",
    "quote": "Numerous foundations and funding agencies award doctoral scholarships through competitive selection processes.",
    "url": gc_url
}
with open(math_path, "w", encoding="utf-8") as f:
    json.dump(math_prog, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Updated lmu.json, lmu--physics.json, and lmu--math.json successfully!")
