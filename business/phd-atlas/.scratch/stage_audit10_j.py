import json
import pathlib

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1-2. tuberlin: gre_general -> Not stated
d = load("tuberlin")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Not stated"
d["fields"]["gre_general"]["value"] = "Not stated on the page checked"
d["fields"]["gre_general"]["quote"] = ""
save("tuberlin", d)

# 3-4. tudresden: gre_general -> Not stated
d = load("tudresden")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Not stated"
d["fields"]["gre_general"]["value"] = "Not stated on the page checked"
d["fields"]["gre_general"]["quote"] = ""
save("tudresden", d)

# 5. twente: toefl_min -> add TOEFL iBT heading
d = load("twente")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL iBT (internet-based) certificate | (after January 2026) | "
    "Not older than two years, with an overall score of 5, and a minimum score of 5 on reading, listening and writing."
)
save("twente", d)

# 6. ua: fee_waiver -> add Fee Exemptions heading
d = load("ua")
d["checked"] = "2026-11-12"
d["fields"]["fee_waiver"]["quote"] = (
    "Fee Exemptions | Veterans and current members of the U.S. military. | "
    "Applicants previously enrolled in Graduate School at The University of Alabama. | "
    "UA undergraduates applying to the same program at the graduate level."
)
save("ua", d)

# 7. uab: english_waiver -> add English Proficiency Exam Waiver heading
d = load("uab")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "English Proficiency Exam Waiver | We may waive the requirement according to the guidelines below: | "
    + d["fields"]["english_waiver"]["quote"]
)
save("uab", d)

print("Staged 5 files for Batch 10")
