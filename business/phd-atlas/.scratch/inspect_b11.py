import hashlib
import json
import pathlib
import re

URLS = [
    ("uci", "https://grad.uci.edu/admissions/applying-to-uci/"),
    ("ucr", "https://graduate.ucr.edu/admission-requirements"),
    ("uga-fr", "https://doctorat.univ-grenoble-alpes.fr/preparing-a-phd/doctorate-enrolment/registration-at-doctoral-college-890540.kjsp"),
    ("ugent", "https://www.ugent.be/prospect/en/administration/application/requirement/phd.htm"),
    ("uic", "https://admissions.uic.edu/graduate-professional/requirements-deadlines/international-requirements"),
    ("uiowa", "https://grad.admissions.uiowa.edu/english-proficiency-requirements"),
]

recs = [p for d in ("universities", "programs") for p in pathlib.Path("data", d).glob("*.json")]

for name, u in URLS:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    c = json.loads(pathlib.Path(".cache/pages", f"{h}.json").read_text(encoding="utf-8"))
    refs = [p.name for p in recs if u in p.read_text(encoding="utf-8")]
    txt = c.get("text", "")
    lines = txt.splitlines()
    print(f"\n=== {name} ({h}) method={c.get('method')} status={c.get('status')} chars={len(txt)} ===")
    print("refs:", refs)
    if name in ("uci", "ucr", "uiowa"):
        for i, ln in enumerate(lines):
            if re.search(r"ielts|overall minimum score of 7|- 7, with no score|overall score of 7", ln, re.I):
                for j in range(max(0, i - 3), min(len(lines), i + 3)):
                    print(f"  L{j}: {lines[j]}")
                print("  ---")
    elif name == "uic":
        for i, ln in enumerate(lines):
            if re.search(r"english|waiv|exempt|two years of full-time", ln, re.I):
                print(f"  L{i}: {ln}")
    elif name == "uga-fr":
        hits = [ln for ln in lines if re.search(r"\bGRE\b|Graduate Record", ln, re.I)]
        print("GRE hits:", hits)
    elif name == "ugent":
        hits = [ln for ln in lines if re.search(r"fee|cost|free|charge|tuition", ln, re.I)]
        print("Fee hits:", hits)
