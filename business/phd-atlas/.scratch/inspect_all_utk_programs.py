import json
import glob
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

progs = [
    ("cs", "36749"),
    ("ece", "36786"),
    ("bme", "36726"),
    ("chemeng", "36734"),
    ("civil", "36740"),
    ("materials", "36829"),
    ("mech", "36835"),
    ("datasci", "36923"),
    ("physics", "36859"),
    ("chemistry", "36736"),
    ("math", "36832"),
    ("earth", "36808"),
    ("biology", "36724"),
]

cache = {}
for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        url = d.get("url", "")
        for name, poid in progs:
            if f"poid={poid}" in url:
                cache[name] = (url, d.get("text", ""))
    except Exception:
        pass

for name, poid in progs:
    print(f"================ {name.upper()} (poid={poid}) ================")
    if name not in cache:
        print("NOT FOUND IN CACHE")
        continue
    url, text = cache[name]
    # Look for admissions section or print first 1500 chars
    idx = text.find("Admission")
    if idx != -1:
        print(text[idx:idx+1200].replace("\n", " "))
    else:
        print(text[:1200].replace("\n", " "))
    print()
