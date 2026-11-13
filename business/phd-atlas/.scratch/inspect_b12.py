import hashlib
import json
import pathlib
import re

URLS = [
    ("umontreal", "https://admission.umontreal.ca/admission/preparation-de-la-demande/prevoir-les-entrevues-et-les-tests/"),
    ("unibe", "https://www.physik.unibe.ch/studies/international_students/index_eng.html"),
    ("unlv", "https://www.unlv.edu/admissions/international/graduate/english-proficiency"),
    ("unt_pdf", "https://catalog.unt.edu/mime/media/view/36/4024/2025-26_UNT_graduate_catalog.pdf"),
    ("uppsala", "https://www.uu.se/en/research/phd-studies"),
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
    if name == "unlv":
        for i, ln in enumerate(lines):
            if re.search(r"4\.0 \(Scale|TOEFL", ln, re.I):
                print(f"  L{i}: {ln}")
    elif name == "unt_pdf":
        for i, ln in enumerate(lines):
            if "Anguilla" in ln or "exempt" in ln.lower():
                for j in range(max(0, i - 5), min(len(lines), i + 3)):
                    print(f"  L{j}: {lines[j]}")
                print("  ---")
    elif name == "uppsala":
        for i, ln in enumerate(lines):
            if re.search(r"free of charge|fee|cost|apply|application", ln, re.I):
                print(f"  L{i}: {ln}")

print("\n=== SCAN unibe.ch GRE / uu.se fee ===")
for p in pathlib.Path(".cache/pages").glob("*.json"):
    c = json.loads(p.read_text(encoding="utf-8"))
    u = c.get("url", "")
    if "unibe.ch" in u:
        hits = [ln for ln in c.get("text", "").splitlines() if re.search(r"\bGRE\b|Graduate Record", ln, re.I)]
        if hits:
            print("UNIBE GRE:", u, hits)
    if "uu.se" in u:
        hits = [ln for ln in c.get("text", "").splitlines() if re.search(r"application fee|free of charge|tuition fee", ln, re.I)]
        if hits:
            print("UU FEE:", u, hits)
