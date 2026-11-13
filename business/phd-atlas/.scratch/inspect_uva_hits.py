import json, pathlib, re

cache_dir = pathlib.Path(".cache/pages")
for p in cache_dir.glob("*.json"):
    d = json.loads(p.read_text(encoding="utf-8"))
    u = d.get("url", "")
    if "uva.nl" not in u:
        continue
    t = d.get("text", "")
    if "admission-to-a-doctoral-programme.html" in u:
        print(f"=== FULL {u} ===")
        print(t)
        print()
    for m in re.finditer(r"\b(?:fee|fees|gre|cost|tuition|application fee)\b", t, re.I):
        s = max(0, m.start() - 80)
        e = min(len(t), m.end() + 80)
        print(f"HIT [{u}]: ...{t[s:e].replace(chr(10), ' ')}...")
