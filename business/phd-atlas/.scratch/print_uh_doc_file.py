import json
from pathlib import Path

cache = Path(".cache/pages")
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    u = rec.get("url", "")
    if u == "https://www.uh.edu/graduate-school/academics/doctoral-programs/":
        print(f"File: {p.name}")
        t = rec.get("text", "")
        for line in t.splitlines():
            if line.strip():
                print(line.strip()[:100])
