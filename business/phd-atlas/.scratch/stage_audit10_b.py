import json
from pathlib import Path

SRC = Path("data/universities")
DST = Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)

TODAY = "2026-11-12"

def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))

def save(name, rec):
    (DST / f"{name}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 1 & 2. byu
r = load("byu")
r["checked"] = TODAY
r["fields"]["toefl_min"]["quote"] = (
    "TOEFL iBT (internet-based test) | "
    "NEW SCORING as of January 21, 2026: Minimum sub-scores of at least 4.0 in Listening, Reading, "
    "Speaking, and Writing, comprising an overall score of at least 4.5."
)
r["fields"]["english_waiver"]["quote"] = (
    "Generally, all applicants are required to demonstrate an acceptable level of English language "
    "proficiency in order to satisfy the university requirements for graduate admission, unless an "
    "applicable exemption or waiver applies. | "
    "Only applicants who are citizens of the following countries (or those applicants who have received "
    "a residential bachelor's degree or higher from said countries, within the previous 24 months of the "
    "intended start date of their respective graduate program) are 'exempt' from this requirement."
)
save("byu", r)

# 3. canterbury-nz
r = load("canterbury-nz")
r["checked"] = TODAY
r["fields"]["toefl_min"]["quote"] = (
    "TOEFL iBT | Tests taken from 21 January 2026 onwards: | "
    "Overall: 4.5, Listening: 3.5, Reading: 3.5, Writing: 4.0, Speaking: 3.5"
)
save("canterbury-nz", r)

# 4. clemson
r = load("clemson")
r["checked"] = TODAY
r["fields"]["english_waiver"]["quote"] = (
    "Clemson University Graduate Admissions uses the IAU WHED World Higher Education Database when "
    "determining whether your institution qualifies for satisfaction of the English language proficiency "
    "requirement. | You may verify whether your institution meets this requirement by looking up your "
    "institution in the IAU WHED World Higher Education Database."
)
save("clemson", r)

# 5 & 6. clevelandstate
r = load("clevelandstate")
r["checked"] = TODAY
r["fields"]["gre_general"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": r["fields"]["gre_general"]["url"],
}
save("clevelandstate", r)

# 7, 8, 9. cmu
r = load("cmu")
r["checked"] = TODAY
for fld in ("fee_waiver", "gre_general"):
    r["fields"][fld] = {
        "code": "Not stated",
        "value": "Not stated on the page checked",
        "quote": "",
        "url": r["fields"][fld]["url"],
    }
save("cmu", r)

# 10. colostate
r = load("colostate")
r["fields"]["toefl_min"]["quote"] = (
    "TOEFL: (including the TOEFL My Best Score) Minimum | "
    "score of 550 (paper based), 80 (Internet based); Effective | "
    "January 2026: 4.5 (Internet based)"
)
save("colostate", r)

print("Staged 6 universities for CARD 3 batch 2.")
