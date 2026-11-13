import json
import pathlib

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. uq: english_waiver
d = load("uq")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "You can also meet our English language proficiency requirements if you can demonstrate one of the following: | "
    + d["fields"]["english_waiver"]["quote"]
)
save("uq", d)

# 2. uri: toefl_min
d = load("uri")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "Applicants whose native language is not English must submit an official test report from the Test of English as a Foreign Language (TOEFL) taken within the past two years. | "
    "Required scores on the Internet-based (iBT) test if taken AFTER January 21, 2026: | "
    + d["fields"]["toefl_min"]["quote"]
)
save("uri", d)

# 4-10. utrecht: app_fee, fee_waiver, gre_general, toefl_min -> Not stated
d = load("utrecht")
d["checked"] = "2026-11-12"
for k in ("app_fee", "fee_waiver", "gre_general", "toefl_min"):
    d["fields"][k]["code"] = "Not stated"
    d["fields"][k]["value"] = "Not stated on the page checked"
    d["fields"][k]["quote"] = ""
save("utrecht", d)

print("Staged 3 files for Batch 13")
