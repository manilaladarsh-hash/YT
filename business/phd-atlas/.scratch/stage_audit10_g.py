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

# 1. loyolachicago.json: include table column header with IELTS
d, p = load("loyolachicago.json")
d["fields"]["ielts_min"]["quote"] = "School TOEFL* IELTS PTE Duolingo | The Graduate School \u2020 4\u2002(79) 6 53 110"
save(p, d)

# 2. lsu.json: include the second sentence naming GRE
d, p = load("lsu.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "The Pinkie Gordon Lane Graduate School does not require the submission of standardized admission test scores. "
    "Your program of interest may require test scores, such as the GRE or GMAT."
)
save(p, d)

# 3. marquette.json: put waiver intro into quote itself
d, p = load("marquette.json")
d["checked"] = "2026-11-12"
d["fields"]["fee_waiver"]["quote"] = (
    "There are only a few circumstances in which the application fee may be waived: | "
    "Applicants who have previously attended Marquette University as a graduate student"
)
d["fields"]["fee_waiver"].pop("also", None)
save(p, d)

# 4. memphis.json: include TOEFL table label
d, p = load("memphis.json")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = "TOEFL | 4 on internet-based test taken January 2026 or later"
save(p, d)

# 5. mines.json: include TOEFL iBT (Tests taken after January 20, 2026) header
d, p = load("mines.json")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL iBT (Tests taken after January 20, 2026) | "
    "Reading 4 Listening 4.5 Writing 4 Speaking 4 Total 4"
)
save(p, d)

# 6. minnesota.json: include fee waiver eligibility header
d, p = load("minnesota.json")
d["checked"] = "2026-11-12"
d["fields"]["fee_waiver"]["quote"] = (
    "Applicants requesting a fee waiver from the University of Minnesota\u2019s Graduate School Diversity Office must meet the following criteria to receive consideration: | "
    "Be a U.S. citizen or permanent resident"
)
save(p, d)

# 7. mps-photonics.json: include GRE FAQ question
d, p = load("mps-photonics.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "Do I need proof of the GRE-test? | "
    "The test is not required and will not be evaluated by us if you upload it."
)
save(p, d)

# 8. ou.json: include TOEFL scale change sentence
d, p = load("ou.json")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "All TOEFL tests taken after January 21, 2026 will be scored with the new scoring system and must meet the new system minimums. | "
    "4.5 or higher (new scoring system)"
)
save(p, d)

# 9. portlandstate.json: update fee_waiver to PSU's dedicated waiver page + refresh app_fee quote on apply-to-grad-school
d, p = load("portlandstate.json")
d["checked"] = "2026-11-12"
d["fields"]["app_fee"]["quote"] = (
    "Submit Your Application and $65 Application Fee | "
    "Graduate applicants may be eligible for an application fee waiver of their $65 admission application fee (plus $2 processing fee)."
)
d["fields"]["fee_waiver"] = {
    "code": "Limited",
    "value": (
        "For international applicants, application fee waivers are only available if the program provides full funding packages "
        "(graduate assistantship) and the applicant attends a program information session; Fulbright and Gates Millennium Scholars also qualify."
    ),
    "quote": (
        "International student eligibility: Application fee waivers are only available to international applicants if the program provides full funding packages, "
        "i.e. a graduate assistantship, and the applicant attends an information session offered by the program to which they\u2019re applying."
    ),
    "url": "https://pdx.edu/admissions/graduate-admission-application-fee-waiver",
}
save(p, d)

print("Staged 9 files for Batch 7")
