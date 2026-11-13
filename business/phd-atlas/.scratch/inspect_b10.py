import hashlib
import json
import pathlib
import re

URLS = [
    ("tuberlin", "https://www.tu.berlin/en/studierendensekretariat/applying-enrolling-for-doctoral-studies"),
    ("tudresden", "https://tu-dresden.de/studium/vor-dem-studium/bewerbung/studienvoraussetzungen/voraussetzungen-fuer-ein-promotionsstudium?set_language=en"),
    ("twente", "https://www.utwente.nl/en/education/master/admission-requirements/language-requirement/"),
    ("ua", "https://graduate.ua.edu/applicants/requirements/"),
    ("uab", "https://www.uab.edu/gradadmissions/apply/international-applicants"),
    ("uark", "https://catalog.uark.edu/graduatecatalog/admissions/"),
]

recs = [p for d in ("universities", "programs") for p in pathlib.Path("data", d).glob("*.json")]

for name, u in URLS:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    c = json.loads(pathlib.Path(".cache/pages", f"{h}.json").read_text(encoding="utf-8"))
    refs = [p.name for p in recs if u in p.read_text(encoding="utf-8")]
    txt = c.get("text", "")
    print(f"\n=== {name} ({h}) method={c.get('method')} via={c.get('via')} status={c.get('status')} chars={len(txt)} ===")
    print("refs:", refs)
    if name in ("tuberlin", "tudresden"):
        hits = [ln for ln in txt.splitlines() if re.search(r"\bGRE\b|Graduate Record", ln, re.I)]
        print("GRE hits:", hits)
    elif name == "twente":
        lines = txt.splitlines()
        for i, ln in enumerate(lines):
            if "TOEFL" in ln or "overall score of 5" in ln:
                print(f"L{i}: {ln}")
    elif name == "ua":
        lines = txt.splitlines()
        for i, ln in enumerate(lines):
            if re.search(r"waiv|fee|Veterans", ln, re.I):
                print(f"L{i}: {ln}")
    elif name == "uab":
        lines = txt.splitlines()
        for i, ln in enumerate(lines):
            if re.search(r"exempt|waiv|english|GPA of 3\.00|citizen of one", ln, re.I):
                print(f"L{i}: {ln}")
