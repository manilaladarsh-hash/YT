import json
import pathlib
import shutil

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)

def load(name):
    src = SRC / name
    dst = DST / name
    shutil.copy2(src, dst)
    return json.loads(dst.read_text(encoding="utf-8")), dst

def save(dst, data):
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 1. ku.json: include TOEFL (iBT) row header and Admission Proficiency tier in quote
d, p = load("ku.json")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL (iBT) (test center and online/at home)** | "
    "Admission Proficiency | "
    "For tests beginning Jan. 21, 2026: | "
    "Total score of 3.5 with no part score below 3.5"
)
d["fields"]["toefl_min"]["also"] = [
    {
        "quote": "Full Proficiency | For tests beginning Jan. 21, 2026: | Total score of 4.5 with no part score below 4.5",
        "url": "https://gradapply.ku.edu/english-requirements",
    }
]
save(p, d)

# 2. leiden.json: app_fee, fee_waiver, gre_general all had irrelevant language quote; none stated centrally -> Not stated
d, p = load("leiden.json")
for k in ("app_fee", "fee_waiver", "gre_general"):
    d["fields"][k] = {
        "code": "Not stated",
        "value": "Not stated on the page checked",
        "quote": "",
        "url": d["fields"][k]["url"],
    }
save(p, d)

# 3. lmu.json: gre_general had no GRE mention on page -> Not stated
d, p = load("lmu.json")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": d["fields"]["gre_general"]["url"],
}
save(p, d)

# 4. louisville.json: include full verbatim TOEFL Score Scale Change sentence
d, p = load("louisville.json")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL Score Scale Change: Effective January 21, 2026, TOEFL will implement a new 1.0\u20136.0 score scale. "
    "In response, the University of Louisville will require a minimum overall score of 4.0, with minimum sub-scores of 4.0 in each skill area."
)
save(p, d)

print("Staged ku, leiden, lmu, louisville")
