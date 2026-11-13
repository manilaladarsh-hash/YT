import json
import pathlib
import shutil

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)

def load(name):
    dst = DST / name
    shutil.copy2(SRC / name, dst)
    return json.loads(dst.read_text(encoding="utf-8")), dst

def save(dst, data):
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 1. sorbonne.json: gre_general has no GRE mention on enrolment-procedures-and-tuition-fees -> Not stated
d, p = load("sorbonne.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": d["fields"]["gre_general"]["url"],
}
save(p, d)

# 2. stanford.json: include fee waivers sentence right before international sentence
d, p = load("stanford.json")
d["checked"] = "2026-11-12"
d["fields"]["fee_waiver"]["quote"] = (
    "Priority for fee waivers in the School of Humanities and Sciences is given to students who are applying to doctoral (PhD, DMA) and MFA programs, "
    "and who are U.S. citizens, permanent residents, or domestic undocumented or DACAmented students. "
    "International applicants are eligible to apply, but will be reviewed on a case-by-case basis."
)
save(p, d)

# 3. stockholm.json: app_fee and fee_waiver cite irrelevant Licentiate quote; no fee mention on page -> Not stated
d, p = load("stockholm.json")
d["checked"] = "2026-11-12"
for k in ("app_fee", "fee_waiver"):
    d["fields"][k] = {
        "code": "Not stated",
        "value": "Not stated on the page checked",
        "quote": "",
        "url": d["fields"][k]["url"],
    }
save(p, d)

# 4. stuttgart.json: gre_general cites English proficiency quote; no GRE mention on page -> Not stated
d, p = load("stuttgart.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": d["fields"]["gre_general"]["url"],
}
save(p, d)

# 5. syracuse.json: include GRE label sentence before optional sentence
d, p = load("syracuse.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "GRE Test Scores - Applicants are recommended to submit a GRE score. | "
    "This is optional for Spring 2027 and Fall 2027 applications."
)
save(p, d)

print("Staged 5 files for Batch 9")
