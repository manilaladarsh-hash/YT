import json
from pathlib import Path

# 1. Update nyu--math.json
nyu_math_path = Path("data/programs/nyu--math.json")
nyu_math = json.load(open(nyu_math_path, encoding="utf-8"))
nyu_math["fields"]["deadline"] = {
    "code": "2027-01-04",
    "value": "January 4 for Ph.D. program admission (year inferred for Fall 2027 entry).",
    "quote": "Admission to the Ph.D. program - January 4",
    "url": "https://math.nyu.edu/dynamic/graduate/phd-mathematics/admission-policies/",
    "inferred": "year"
}
nyu_math["fields"]["supervisor"] = {
    "code": "Not required",
    "value": "Admission decisions are based on committee review of academic record, recommendation letters, and credentials; no prior supervisor required before applying.",
    "quote": "Admission decisions are based on a careful review of the applicant's previous academic record, letters of recommendation, TOEFL (if applicable) and GRE scores, as well as other credentials, such as work experience or previous research projects.",
    "url": "https://math.nyu.edu/dynamic/graduate/phd-mathematics/admission-policies/"
}
with open(nyu_math_path, "w", encoding="utf-8") as f:
    json.dump(nyu_math, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 2. Update brown--physics.json
brown_phys_path = Path("data/programs/brown--physics.json")
brown_phys = json.load(open(brown_phys_path, encoding="utf-8"))
brown_phys["fields"]["supervisor"] = {
    "code": "Recommended",
    "value": "Prospective students are encouraged to contact specific faculty members to determine whether their research aligns more closely with the Physics or Astrophysics track.",
    "quote": "Prospective students are also encouraged to contact specific faculty members to determine whether their current research projects align more closely with the Physics or Astrophysics tracks.",
    "url": "https://physics.brown.edu/academics/graduate/how-apply"
}
with open(brown_phys_path, "w", encoding="utf-8") as f:
    json.dump(brown_phys, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 3. Update clarkson--physics.json
clarkson_phys_path = Path("data/programs/clarkson--physics.json")
clarkson_phys = json.load(open(clarkson_phys_path, encoding="utf-8"))
clarkson_phys["fields"]["supervisor"] = {
    "code": "Not required",
    "value": "Students select a thesis topic and are assigned a research advisor no later than the second semester of graduate study.",
    "quote": "Students must select a thesis topic and be assigned to a research advisor no later than the second semester of graduate study.",
    "url": "https://www.clarkson.edu/academics/majors-minors/physics-phd"
}
with open(clarkson_phys_path, "w", encoding="utf-8") as f:
    json.dump(clarkson_phys, f, indent=2, ensure_ascii=False)
    f.write("\n")

# 4. Update buffalo--physics.json
buffalo_phys_path = Path("data/programs/buffalo--physics.json")
buffalo_phys = json.load(open(buffalo_phys_path, encoding="utf-8"))
buffalo_phys["fields"]["gre_general"] = {
    "code": "Optional",
    "value": "Both GRE General and GRE Physics Test scores are optional.",
    "quote": "Both GRE General and GRE Physics Test scores are oprtional.",
    "url": "https://arts-sciences.buffalo.edu/physics/graduate/admissions.html"
}
with open(buffalo_phys_path, "w", encoding="utf-8") as f:
    json.dump(buffalo_phys, f, indent=2, ensure_ascii=False)
    f.write("\n")

print("Batch C program updates written successfully!")
