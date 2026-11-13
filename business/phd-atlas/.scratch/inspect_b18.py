import json, pathlib, re

cache_dir = pathlib.Path(".cache/pages")

def norm(s):
    return re.sub(r"\s+", " ", s)

for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    t = d.get("text", "")
    nt = norm(t)
    if "chemistry.berkeley.edu/grad/cbe/phd/admission" in u:
        idx = nt.find("consider it for admission")
        print("=== BERKELEY CBE ===")
        print(nt[max(0, idx - 350): idx + 250])
        print()
    elif "bristol.ac.uk" in u and any(x in u for x in ("phd-civil-engineering.pdf", "phd-electrical-and-electronic-engineering.pdf", "phd-mechanical-engineering.pdf")):
        idx = nt.find("received a completed copy of this document")
        print(f"=== {u} (idx={idx}) ===")
        print(nt[max(0, idx - 500): idx + 250])
        print()
    elif "brandeis.edu" in u:
        has_mcb = "MCB admissions committee" in nt
        has_rot = "rotation" in nt.lower()
        print(f"BRANDEIS: {p.name} | {u} -> {d.get('final_url')} | mcb={has_mcb} rot={has_rot}")
