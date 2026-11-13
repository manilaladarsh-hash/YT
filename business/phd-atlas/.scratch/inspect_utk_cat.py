import json
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

url = "https://catalog.utk.edu/content.php?catoid=57&navoid=12403"
data = None
for f in json.load(open(".cache/pages/c62c9ac5f2576a49.json", encoding="utf-8")) if False else []:
    pass

import glob
for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        if d.get("url") == url:
            data = d
            break
    except Exception:
        pass

if not data:
    print("Catalog page not found in cache")
    sys.exit(1)

text = data.get("text", "")
print(f"Catalog length: {len(text)}")

for kw in ["Admissions Application Fee", "$60", "application fee", "Doctor of Philosophy", "bachelor", "fee waiver"]:
    print(f"=== KW: {kw} ===")
    for m in re.finditer(re.escape(kw), text, re.IGNORECASE):
        start = max(0, m.start() - 100)
        end = min(len(text), m.end() + 200)
        print("  " + text[start:end].replace("\n", " "))
        print()
