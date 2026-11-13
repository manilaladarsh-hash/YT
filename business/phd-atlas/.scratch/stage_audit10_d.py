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

# 1 & 2. floridatech
r = load("floridatech")
r["checked"] = TODAY
r["fields"]["toefl_min"]["quote"] = (
    "an Internet-based TOEFL (standard, home-based, or paper-based) with a minimum score of 80 "
    "for test-takers prior to January 1, 2026. Test-takers on or after January 1, 2026, must earn a "
    "minimum score of 4.0"
)
r["fields"]["english_waiver"]["quote"] = (
    "Students whose first language is not English are considered to have demonstrated English language "
    "proficiency if they have accomplished any of the following: | "
    "4. Studied at an institution in the United States, United Kingdom, Ireland, Australia, Anglophone "
    "Canada, Anglophone Caribbean, Anglophone Africa, or a secondary school overseas where English is "
    "the primary language of instruction as deemed at the discretion of the Office of Admission, | "
    "earning a bachelor’s or higher degree from an accredited university or college."
)
save("floridatech", r)

# 3 & 4. freiburg
r = load("freiburg")
r["fields"]["gre_general"] = not_stated(r["fields"]["gre_general"]["url"])
save("freiburg", r)

# 5 & 6. fuberlin
r = load("fuberlin")
r["checked"] = TODAY
r["fields"]["gre_general"] = not_stated(r["fields"]["gre_general"]["url"])
save("fuberlin", r)

# 7. georgetown
r = load("georgetown")
r["checked"] = TODAY
r["fields"]["fee_waiver"]["quote"] = (
    "Populations eligible for an application fee waiver: | "
    "US citizens with demonstrated financial need who meet one of the following categories:"
)
save("georgetown", r)

print("Staged 4 universities for CARD 3 batch 4.")
