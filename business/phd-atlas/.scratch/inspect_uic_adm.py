import json
from pathlib import Path

cache = Path(".cache/pages")
for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    u = rec.get("url", "")
    if "international-requirements" in u or "application-fee-waivers" in u:
        print(f"=== URL: {u} ===")
        for line in rec.get("text", "").splitlines():
            s = line.strip()
            if any(k in s.lower() for k in ["toefl", "ielts", "exempt", "waiver", "minimum", "bachelor", "fee"]):
                if len(s) < 150:
                    print("  *", s)
