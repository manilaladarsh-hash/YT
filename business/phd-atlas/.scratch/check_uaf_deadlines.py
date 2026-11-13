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
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    matches = [l for l in lines if any(k in l.lower() for k in ["deadline", "january", "february", "march", "december", "fall semester"])]
    print(f"=== {p} ({len(matches)} matches) ===")
    for m in matches[:5]:
        print("  ", m[:120])
