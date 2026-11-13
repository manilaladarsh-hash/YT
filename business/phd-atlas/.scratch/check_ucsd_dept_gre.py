import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

progs = [
    ("math", "https://catalog.ucsd.edu/curric/MATH-gr.html"),
    ("cs", "https://catalog.ucsd.edu/curric/CSE-gr.html"),
    ("ece", "https://catalog.ucsd.edu/curric/ECE-gr.html"),
    ("chem", "https://catalog.ucsd.edu/curric/CHEM-gr.html"),
    ("bio", "https://catalog.ucsd.edu/curric/BIOL-gr.html"),
    ("bme", "https://catalog.ucsd.edu/curric/BENG-gr.html"),
    ("mech", "https://catalog.ucsd.edu/curric/MAE-gr.html"),
    ("civil", "https://catalog.ucsd.edu/curric/SE-gr.html"),
    ("earth", "https://catalog.ucsd.edu/curric/SIO-gr.html"),
    ("neuro", "https://catalog.ucsd.edu/curric/NEU.html"),
    ("materials", "https://catalog.ucsd.edu/curric/MATS.html"),
    ("datasci", "https://catalog.ucsd.edu/curric/DSC-gr.html"),
    ("physics", "https://catalog.ucsd.edu/curric/PHYS-gr.html"),
]

for name, u in progs:
    d = json.load(open(cache_paths(u), "r", encoding="utf-8"))
    text = d["text"]
    lines = [l.strip() for l in text.splitlines() if "gre" in l.lower()]
    print(f"{name}: {len(lines)} lines mentioning GRE")
    for l in lines[:3]:
        print("  ", l[:120])
