import json, pathlib

cache_dir = pathlib.Path(".cache/pages")
targets = {
    "https://www.uts.edu.au/for-students/admissions-entry/how-to-apply/masters-by-research-phd",
    "https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html",
}

for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if u in targets:
        print(f"=== {u} ({p.name}) ===")
        print(d.get("text", ""))
        print()
    elif "uva.nl" in u:
        t = d.get("text", "")
        hits = [w for w in ("fee", "gre", "cost", "free", "charge", "euro", "tuition") if w in t.lower()]
        print(f"UVA: {p.name} | {u} | hits={hits}")
