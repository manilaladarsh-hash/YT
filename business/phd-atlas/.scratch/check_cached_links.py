import json
import glob
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        if "navoid=12418" in d.get("url", ""):
            print(f"File: {f}")
            print(list(d.keys()))
            if "links" in d:
                for text, href in d["links"]:
                    if any(k in text for k in ["Computer Science", "Physics", "Chemistry", "Mathematics", "Geology", "Electrical Engineering"]):
                        print(f"{text} -> {href}")
            break
    except Exception as e:
        print("Error:", e)
