import glob, json

urls = [
    "https://www.rit.edu/study/computing-and-information-sciences-phd",
    "https://www.rit.edu/study/electrical-and-computer-engineering-phd",
    "https://www.rit.edu/study/mechanical-and-industrial-engineering-phd",
    "https://www.rit.edu/study/biomedical-and-chemical-engineering-phd",
    "https://www.rit.edu/study/microsystems-engineering-phd",
    "https://www.rit.edu/study/sustainability-phd",
    "https://www.rit.edu/study/cognitive-science-phd",
    "https://www.rit.edu/study/imaging-science-phd",
    "https://www.rit.edu/study/color-science-phd",
    "https://www.rit.edu/study/physics-phd",
    "https://www.rit.edu/study/mathematical-modeling-phd",
    "https://www.rit.edu/study/astrophysical-sciences-and-technology-phd"
]

cache = {}
for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, 'r', encoding='utf-8'))
        u = d.get('url', '')
        if u in urls:
            cache[u] = d
    except Exception:
        pass

for u in urls:
    d = cache.get(u)
    if not d:
        print("MISSING:", u)
        continue
    text = d.get('text', '')
    print("="*60)
    print("URL:", u)
    for line in text.splitlines():
        if any(w in line for w in ['GRE', 'standard deadline', 'stipend', 'baccalaureate', 'Entrance exam']):
            clean = line.encode('ascii', errors='replace').decode('ascii')
            print("  ", clean)
