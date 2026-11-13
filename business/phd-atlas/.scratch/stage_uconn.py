import json
from pathlib import Path

SRC = Path("data/programs")
DST = Path("data/staging/programs")
DST.mkdir(parents=True, exist_ok=True)

TODAY = "2026-11-12"

def load_src(field):
    return json.loads((SRC / f"uconn--{field}.json").read_text(encoding="utf-8"))

def save_dst(field, rec):
    (DST / f"uconn--{field}.json").write_text(
        json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

# 1. chemeng
r = load_src("chemeng")
url = "https://chemical-biomolecular.engineering.uconn.edu/graduate/how-to-apply/"
r["program_page"] = url
r["department"] = "Chemical & Biomolecular Engineering Department"
r["checked"] = TODAY
r["fields"]["deadline"] = {
    "code": "2027-01-01",
    "value": "January 1 recommended deadline for Fall admission (late applications reviewed on an ongoing basis).",
    "quote": "January 1 for both full-time M.S. and Ph.D. applications for Fall admission. Late applications will be reviewed on an ongoing basis until all openings are filled.",
    "url": url,
}
r["fields"]["funding"] = {
    "code": "Typical",
    "value": "Full-time Ph.D. students generally receive financial aid (assistantships or fellowships) throughout their tenure of study.",
    "quote": "Full-time Ph.D. graduate students generally receive financial aid throughout their tenure of study.",
    "url": url,
}
r["fields"]["entry_route"] = {
    "code": "Direct from bachelor's",
    "value": "Must hold a B.A./B.S. degree from an accredited college or university.",
    "quote": "Must hold a B.A./B.S. degree from an accredited college or university.",
    "url": url,
}
save_dst("chemeng", r)

# 2. ece
r = load_src("ece")
url = "https://electrical-computer.engineering.uconn.edu/graduate/ph-d-program/"
r["program_page"] = url
r["department"] = "Electrical and Computer Engineering Department"
r["checked"] = TODAY
r["fields"]["entry_route"] = {
    "code": "Direct from bachelor's",
    "value": "Minimum 33 credits beyond a B.S. degree or 18 credits beyond an M.S. degree.",
    "quote": "Students must take a minimum of 33 credits of content coursework beyond a B.S. degree or 18 credits of content coursework beyond an M.S. degree.",
    "url": url,
}
save_dst("ece", r)

# 3. civil
r = load_src("civil")
r["program_page"] = "https://grad.engineering.uconn.edu/current-students/degree-programs/degree-programs-ce/"
r["department"] = "School of Civil and Environmental Engineering"
r["checked"] = TODAY
save_dst("civil", r)

# 4. environment
r = load_src("environment")
r["program_page"] = "https://grad.engineering.uconn.edu/current-students/degree-programs/degree-programs-enve/"
r["department"] = "Environmental Engineering Program"
r["checked"] = TODAY
save_dst("environment", r)

# 5. materials
r = load_src("materials")
r["program_page"] = "https://grad.engineering.uconn.edu/current-students/degree-programs/degree-programs-mse/"
r["department"] = "Materials Science and Engineering department"
r["checked"] = TODAY
save_dst("materials", r)

print("Staged 5 uconn programs.")
