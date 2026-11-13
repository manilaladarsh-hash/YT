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

# 1 & 2. heidelberg
r = load("heidelberg")
r["checked"] = TODAY
r["fields"]["gre_general"] = not_stated(r["fields"]["gre_general"]["url"])
save("heidelberg", r)

# 3 & 4. imperial
r = load("imperial")
r["checked"] = TODAY
r["fields"]["fee_waiver"]["quote"] = (
    "You do not need to pay an application fee for: | "
    "Postgraduate Doctoral degrees (e.g. PhD, EngD) | "
    "Combined MRes + PhD (1+3) Centre for Doctoral Training programmes"
)
save("imperial", r)

# 5-10. ipparis
r = load("ipparis")
for fld in ("app_fee", "fee_waiver", "gre_general"):
    r["fields"][fld] = not_stated(r["fields"][fld]["url"])
save("ipparis", r)

print("Staged 3 universities for CARD 3 batch 5.")
