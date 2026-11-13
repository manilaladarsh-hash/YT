import json
import pathlib

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. uci: ielts_min
d = load("uci")
d["checked"] = "2026-11-12"
d["fields"]["ielts_min"]["quote"] = (
    "IELTS Score Requirements for Admission Consideration: | "
    "An overall minimum score of 7 for admission, with no less than 6 on any individual module."
)
save("uci", d)

# 2. ucr: ielts_min
d = load("ucr")
d["checked"] = "2026-11-12"
d["fields"]["ielts_min"]["quote"] = (
    "The International English Language Testing System (IELTS) Academic must be taken within two years "
    "of the time you intend to enroll at UCR. The minimum acceptable overall score is: | "
    "- 7, with no score less than 6 on any individual component"
)
save("ucr", d)

# 3-4. uga-fr: gre_general -> Not stated
d = load("uga-fr")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Not stated"
d["fields"]["gre_general"]["value"] = "Not stated on the page checked"
d["fields"]["gre_general"]["quote"] = ""
save("uga-fr", d)

# 5-8. ugent: app_fee & fee_waiver -> Not stated
d = load("ugent")
d["checked"] = "2026-11-12"
d["fields"]["app_fee"]["code"] = "Not stated"
d["fields"]["app_fee"]["value"] = "Not stated on the page checked"
d["fields"]["app_fee"]["quote"] = ""
d["fields"]["fee_waiver"]["code"] = "Not stated"
d["fields"]["fee_waiver"]["value"] = "Not stated on the page checked"
d["fields"]["fee_waiver"]["quote"] = ""
save("ugent", d)

# 9. uic: english_waiver
d = load("uic")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "The English proficiency test requirement may be waived under the following circumstances, "
    "if the conditions have occurred within the last five years: | "
    "Enrollment at an accredited U.S. institution for at least two years of full-time, academic study. | "
    "English proficiency requirements are not waived based upon the medium of instruction at a previously attended institution."
)
save("uic", d)

# 10. uiowa: ielts_min
d = load("uiowa")
d["checked"] = "2026-11-12"
d["fields"]["ielts_min"]["quote"] = (
    "International applicants who do not meet the requirements for a waiver are required to submit "
    "English proficiency scores. | IELTS | Overall score of 7 with no subscore less than 6"
)
save("uiowa", d)

print("Staged 6 files for Batch 11")
