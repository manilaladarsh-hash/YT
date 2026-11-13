import json
import glob
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        if d.get("url") == "https://catalog.vt.edu/graduate/degree-programs/":
            print("Found degree-programs page in cache:")
            print("Links count:", len(d.get("links", [])))
            for text, href in d.get("links", []):
                if any(k in text.lower() for k in ["computer", "engineering", "physics", "chemistry", "mathematics", "biology", "geosciences", "materials"]):
                    print(f"{text} -> {href}")
            break
    except Exception as e:
        print("Error:", e)
