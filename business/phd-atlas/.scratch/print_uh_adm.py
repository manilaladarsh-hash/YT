import json
from pathlib import Path

cache = Path(".cache/pages")
urls = [
    "https://www.uh.edu/graduate-school/academics/doctoral-programs/",
    "https://www.uh.edu/graduate-school/admissions/admission-requirements/",
    "https://www.uh.edu/graduate-school/admissions/how-to-apply/"
]

for p in cache.glob("*.json"):
    rec = json.loads(p.read_text(encoding="utf-8"))
    u = rec.get("url")
    if u in urls:
        print(f"=== {u} ===")
        print(rec.get("text", ""))
