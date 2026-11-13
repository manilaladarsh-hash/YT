import json, pathlib, re

cache_dir = pathlib.Path(".cache/pages")
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    t = d.get("text", "")
    if "phd.tech.au.dk/for-applicants/apply-here" in u:
        print(f"=== {u} ===")
        print(t)
        print()
    elif u in {
        "https://grad.uwo.ca/admissions/program.cfm?p=61",
        "https://grad.uwo.ca/admissions/program.cfm?p=67",
        "https://www.uwo.ca/stats/graduate/phd-program.html",
    }:
        for m in re.finditer(r"\b(?:gre|waiv\w*|application fee)\b", t, re.I):
            s = max(0, m.start() - 100)
            e = min(len(t), m.end() + 100)
            print(f"UWO [{u}]: ...{t[s:e].replace(chr(10), ' ')}...")
