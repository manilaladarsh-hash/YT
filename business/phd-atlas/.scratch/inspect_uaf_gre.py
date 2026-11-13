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
    for l in text.splitlines():
        if "official test results:" in l.lower() or "gre" in l.lower():
            if len(l.strip()) < 200:
                print(f"{p}: {l.strip()}")
