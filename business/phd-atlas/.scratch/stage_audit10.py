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

# 1. adelaide
r = load("adelaide")
r["checked"] = TODAY
r["fields"]["english_waiver"]["quote"] = (
    "You have attended and satisfactorily completed at least six years of primary and secondary# education "
    "taught and assessed solely in English in a recognised country**. | "
    "**Recognised countries: Antigua and Barbuda ... USA, and US Virgin Islands."
)
save("adelaide", r)

# 2 & 3. albany
r = load("albany")
r["checked"] = TODAY
r["fields"]["fee_waiver"]["quote"] = (
    "To request a waiver, submit a completed Graduate Fee Waiver Request Form and a certifying letter from "
    "your program director, attesting to your participation, with your admissions application. | "
    "International and SOPHAS applicants are not eligible."
)
r["fields"]["english_waiver"]["quote"] = (
    "Applicants can waive the English Language Proficiency requirement if they upload transcripts to the "
    "application portal showing they successfully completed at least four full-time semesters within a "
    "four-year time frame from time of application and maintained at least a B average at a college or "
    "university in the United States or a country from an approved list."
)
save("albany", r)

# 7. arizona
r = load("arizona")
r["checked"] = TODAY
r["fields"]["ielts_min"]["quote"] = (
    "International English Language Testing System (IELTS) - minimum composite score of 7, "
    "with no subject area below a 6 on IELTS or IELTS Online."
)
save("arizona", r)

# 8. auckland
r = load("auckland")
r["checked"] = TODAY
r["fields"]["app_fee"]["value"] = (
    "An application fee of 100 NZD applies when the highest qualification gained or attempted is from an "
    "overseas tertiary institution."
)
r["fields"]["app_fee"]["quote"] = (
    "International Applicants | "
    "Highest qualification gained or attempted is from an overseas tertiary institution. | $100"
)
save("auckland", r)

# 9. baylor
r = load("baylor")
r["checked"] = TODAY
r["fields"]["toefl_min"]["quote"] = "TOEFL | PhD Research Doctorates 4.5"
save("baylor", r)

# 10. bristol
r = load("bristol")
r["fields"]["fee_waiver"] = {
    "code": "No fee",
    "value": (
        "No application fee applies to the STEM research programmes checked, so no waiver is needed; "
        "the fee policy lists fees only for Business School and School of Economics taught programmes."
    ),
    "quote": "While there is no University-wide charge to applicants for consideration of their applications, individual schools may charge application fees.",
    "url": "https://www.bristol.ac.uk/media-library/sites/study/documents/policies/Admissions principles and procedures for postgraduate research programmes 2026.pdf",
    "also": [
        {
            "quote": "Applications for Postgraduate Taught programmes in the following Schools will require | an application fee of £60 per application.",
            "url": "https://www.bristol.ac.uk/media-library/sites/study/postgraduate/documents/2026_Application Fee Policy_2026_v2.pdf",
        }
    ],
}
save("bristol", r)

print("Staged 6 universities for CARD 3.")
