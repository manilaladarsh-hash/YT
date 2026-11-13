import json
from pathlib import Path

urls = [
    "https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/computer-science-phd",
    "https://grad.admissions.uiowa.edu/academics/chemistry-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/integrated-biology-phd",
    "https://grad.admissions.uiowa.edu/academics/biomedical-science-phd",
    "https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/chemical-and-biochemical-engineering-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/civil-environmental-engineering-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/electrical-computer-engineering-ms-or-phd",
    "https://grad.admissions.uiowa.edu/academics/mechanical-engineering-ms-or-phd",
]

cache = Path(".cache/pages")
cache_map = {}
for p in cache.glob("*.json"):
    try:
        rec = json.loads(p.read_text(encoding="utf-8"))
        cache_map[rec.get("url")] = rec.get("text", "")
    except Exception:
        pass

for u in urls:
    text = cache_map.get(u, "")
    print(f"=== {u.split('/')[-1]} ===")
    lines = text.splitlines()
    in_dl = False
    for i, line in enumerate(lines):
        if "Application Deadline" in line or "Deadlines" in line:
            in_dl = True
        if in_dl:
            print("  ", line[:100].encode("ascii", errors="replace").decode("ascii"))
            if "Application Instructions" in line or "Estimated Cost" in line:
                in_dl = False
                print("---")
