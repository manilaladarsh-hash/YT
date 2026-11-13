import json, glob

found = []
for f in glob.glob(".cache/pages/*.json"):
    try:
        d = json.load(open(f, encoding="utf-8"))
        u = d.get("url", "")
        if "ucl.ac.uk" in u and d.get("status") == 200:
            found.append((u, len(d.get("text", ""))))
    except Exception:
        pass

print(f"Total 200 URLs for ucl.ac.uk: {len(found)}")
for u, length in sorted(found):
    print(f"  {u} (len={length})")
