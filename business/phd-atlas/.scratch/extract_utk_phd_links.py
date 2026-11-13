import json
import re
import sys
import glob

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cache = {}
for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        if "navoid=12418" in d.get("url", ""):
            # Let's see if html is present or links in text
            t = d.get("text", "")
            for line in t.split("\n"):
                if "PhD" in line or "Doctor of Philosophy" in line:
                    print(line.strip())
    except Exception:
        pass
