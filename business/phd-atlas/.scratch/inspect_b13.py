import hashlib
import json
import pathlib
import re

URLS = [
    ("uq", "https://study.uq.edu.au/admissions/english-language-requirements"),
    ("uri", "https://web.uri.edu/graduate-school/admission/international/"),
    ("uta_pdf", "https://catalog.uta.edu/academicregulations/admissions/graduate/graduate.pdf"),
    ("utrecht_pdf", "https://www.uu.nl/sites/default/files/minimum_requirements_for_the_quality_assurance_system_for_doctoral_programmes.pdf"),
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
    if name == "uq":
        for i, ln in enumerate(lines):
            if "Successfully completed a bachelor's" in ln:
                for j in range(max(0, i - 4), min(len(lines), i + 3)):
                    print(f"  L{j}: {lines[j]}")
    elif name == "uri":
        for i, ln in enumerate(lines):
            if "4 or above" in ln or "TOEFL" in ln:
                for j in range(max(0, i - 3), min(len(lines), i + 2)):
                    print(f"  L{j}: {lines[j]}")
                print("  ---")
    elif name == "uta_pdf":
        for i, ln in enumerate(lines):
            if "application evaluation charge" in ln.lower() or "no exceptions to this policy" in ln.lower():
                for j in range(max(0, i - 3), min(len(lines), i + 3)):
                    print(f"  L{j}: {lines[j]}")
                print("  ---")

print("\n=== SCAN uu.nl ===")
for p in pathlib.Path(".cache/pages").glob("*.json"):
    c = json.loads(p.read_text(encoding="utf-8"))
    u = c.get("url", "")
    if "uu.nl" in u:
        hits = [ln for ln in c.get("text", "").splitlines() if re.search(r"application fee|\bGRE\b|TOEFL", ln, re.I)]
        if hits:
            print("UU HIT:", u, hits)
