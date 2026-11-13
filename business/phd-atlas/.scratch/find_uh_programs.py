import json
from pathlib import Path

cache = Path(".cache/pages")
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    u = rec.get("url", "")
    t = rec.get("text", "")
    if "uh.edu" in u and ("Computer Science" in t or "Physics" in t or "Doctor of Philosophy" in t):
        print(f"URL: {u}")
        for line in t.splitlines():
            line_s = line.strip()
            if any(k in line_s for k in ["Ph.D.", "Doctor of Philosophy", "Doctoral"]):
                if len(line_s) < 120:
                    print("  *", line_s)
