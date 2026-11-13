import json, pathlib

cache_dir = pathlib.Path(".cache/pages")
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "ucalgary.ca" in u:
        t = d.get("text", "")
        if any(x in u for x in ("biological-sciences-phd", "medical-science-phd", "biomedical-engineering-phd")):
            idx = t.find("Test scores")
            print(f"=== {u} (status={d.get('status')}) ===")
            print(t[max(0, idx - 300): idx + 300])
            print()
