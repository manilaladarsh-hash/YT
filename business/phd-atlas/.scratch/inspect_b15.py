import json, pathlib, re

cache_dir = pathlib.Path(".cache/pages")
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    t = d.get("text", "")
    if "grad.uwo.ca/admissions/apply-for-admission/index.cfm" in u:
        print(f"=== {u} ===")
        print(t)
        print()
    elif "uwo.ca" in u:
        hits = [m.group(0) for m in re.finditer(r"\b(?:gre|waiv\w*|application fee)\b", t, re.I)]
        if hits:
            print(f"UWO HIT {u}: {hits[:10]}")
    elif "phd.tech.au.dk/for-applicants/apply-here" in u:
        print(f"=== {u} ===")
        print(t)
        print()
