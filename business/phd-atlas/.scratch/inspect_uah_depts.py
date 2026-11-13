import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

urls = [
    "https://www.uah.edu/eng/departments/cme",
    "https://www.uah.edu/science/departments/biotechnology",
    "https://www.uah.edu/eng/departments/ece",
    "https://www.uah.edu/eng/departments/mae",
    "https://www.uah.edu/eng/departments/cee",
    "https://www.uah.edu/science/departments/computer-science",
    "https://www.uah.edu/science/departments/math",
    "https://www.uah.edu/science/departments/physics",
    "https://www.uah.edu/science/departments/atmospheric-earth-science",
    "https://www.uah.edu/science/departments/space-science"
]

for u in urls:
    d = json.load(open(cache_paths(u), "r", encoding="utf-8"))
    print("="*40)
    print("URL:", u)
    lines = [l.strip() for l in d.get("text", "").splitlines() if l.strip()]
    for l in lines:
        if any(w in l.lower() for w in ["ph.d", "doctor", "degree", "program", "admission", "deadline", "gre"]):
            print("  ", l[:120])
