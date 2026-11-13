import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

d = json.load(open(".cache/pages/977ee8d762408ab1.json", encoding="utf-8"))
for text, href in d.get("links", []):
    if "PhD" in text:
        print(f"{text} -> {href}")
