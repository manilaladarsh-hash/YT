import json
import glob
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        url = d.get("url", "")
        if "utk.edu" in url:
            text = d.get("text", "")
            for m in re.finditer(r"deadline", text, re.I):
                print(f"[{url}]")
                print("  " + text[max(0, m.start()-60):min(len(text), m.end()+140)].replace("\n", " "))
    except Exception:
        pass
