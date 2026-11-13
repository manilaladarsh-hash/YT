import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

progs = [
    "atmospheric-sciences",
    "biochemistry-neuroscience",
    "biological-sciences",
    "earth-system-science",
    "engineering",
    "environmental-chemistry",
    "geophysics",
    "geoscience",
    "mathematics",
    "physics",
    "physics-space",
    "natural-resources-sustainability",
    "oceanography",
    "marine-biology"
]

for p in progs:
    u = f"https://catalog.uaf.edu/phd/{p}/"
    d = json.load(open(cache_paths(u), "r", encoding="utf-8"))
    text = d["text"]
    print("="*50)
    print("PROG:", p)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    for i, l in enumerate(lines):
        if any(k in l.lower() for k in ["admission requirements", "deadline", "official test results"]):
            print("  [L]", lines[max(0, i-1):min(len(lines), i+8)])
