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

# 1. portlandstate.json: include TOEFL header
d, p = load("portlandstate.json")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL: | For exams taken on or after January 21, 2026: | "
    "Minimum overall of 4.5 with minimum subscores of 4 in reading and writing."
)
save(p, d)

# 2. princeton.json: grad school says programs may require GRE and has no min score -> Not stated centrally
d, p = load("princeton.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": d["fields"]["gre_general"]["url"],
}
save(p, d)

# 3. rockefeller.json: IELTS is never mentioned on RURequirementsProcedures.pdf -> Not stated
d, p = load("rockefeller.json")
d["fields"]["ielts_min"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": d["fields"]["ielts_min"]["url"],
}
save(p, d)

# 4. sissa.json: include FAQ question naming TOEFL and IELTS
d, p = load("sissa.json")
faq_q = "Do I need to present a TOEFL, GRE, IELTS or other English proficiency certificates? | It is not mandatory but it will be very welcome."
d["fields"]["toefl_min"]["quote"] = faq_q
d["fields"]["ielts_min"]["quote"] = faq_q
save(p, d)

# 5. siucarbondale.json: include second sentence naming GRE
d, p = load("siucarbondale.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "The Graduate School does not require any graduate tests for admission. "
    "Individual programs may require, at their discretion, the GMAT, GRE, MAT, or other appropriate standardized tests for admission."
)
save(p, d)

# 6. sorbonne.json: enrolment-procedures-and-tuition-fees covers tuition (EUR 398), not application fee -> Not stated
d, p = load("sorbonne.json")
d["checked"] = "2026-11-12"
for k in ("app_fee", "fee_waiver"):
    d["fields"][k] = {
        "code": "Not stated",
        "value": "Not stated on the page checked",
        "quote": "",
        "url": d["fields"][k]["url"],
    }
save(p, d)

print("Staged 6 files for Batch 8")
