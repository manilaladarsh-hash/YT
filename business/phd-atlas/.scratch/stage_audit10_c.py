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

def not_stated(url):
    return {
        "code": "Not stated",
        "value": "Not stated on the page checked",
        "quote": "",
        "url": url,
    }

# 1 & 2. dalhousie
r = load("dalhousie")
r["checked"] = TODAY
r["fields"]["gre_general"] = not_stated(r["fields"]["gre_general"]["url"])
save("dalhousie", r)

# 3. denver
r = load("denver")
r["checked"] = TODAY
r["fields"]["gre_general"] = not_stated(r["fields"]["gre_general"]["url"])
save("denver", r)

# 4-9. dtu
r = load("dtu")
r["checked"] = TODAY
for fld in ("app_fee", "fee_waiver", "gre_general"):
    r["fields"][fld] = not_stated(r["fields"][fld]["url"])
save("dtu", r)

# 10. ecu
r = load("ecu")
r["checked"] = TODAY
r["fields"]["english_waiver"] = {
    "code": "No",
    "value": (
        "An English-medium Indian degree does not waive the exam; exemption requires English as "
        "native language or at least 24 U.S. undergraduate or 9 U.S. graduate credit hours with a 3.0 GPA."
    ),
    "quote": (
        "Provide Evidence of English Proficiency: If English is not your native language and you have "
        "not completed at least 24 U.S. credit hours. at the undergraduate level with a minimum 3.0 GPA "
        "or completed 9 U.S. credit hours at the graduate level with a minimum GPA of 3.0, you are "
        "required to take a standardized English language exam."
    ),
    "url": "https://gradschool.ecu.edu/international-students/",
}
save("ecu", r)

print("Staged 4 universities for CARD 3 batch 3.")
