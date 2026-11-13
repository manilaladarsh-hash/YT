import json
import pathlib

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. utrecht: ielts_min -> Not stated
d = load("utrecht")
d["checked"] = "2026-11-12"
d["fields"]["ielts_min"]["code"] = "Not stated"
d["fields"]["ielts_min"]["value"] = "Not stated on the page checked"
d["fields"]["ielts_min"]["quote"] = ""
save("utrecht", d)

# 2. uts: english_waiver -> include full sentence naming IELTS/TOEFL requirement
d = load("uts")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "the Medium of Instruction (MoI) option is not accepted for qualifications from India, Bangladesh, Nepal, and Pakistan. "
    "Applicants with qualifications from these countries will need to provide a valid IELTS, TOEFL, PTE, or UTS College Academic English score."
)
save("uts", d)

# 3-8. uva: app_fee, fee_waiver, gre_general -> Not stated
d = load("uva")
d["checked"] = "2026-11-12"
for k in ("app_fee", "fee_waiver", "gre_general"):
    d["fields"][k]["code"] = "Not stated"
    d["fields"][k]["value"] = "Not stated on the page checked"
    d["fields"][k]["quote"] = ""
save("uva", d)

print("Staged 3 files for Batch 14")
