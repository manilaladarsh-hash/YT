import glob, json

urls = [
    ("physics", "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/physics-astronomy/physics-phd/"),
    ("math", "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/mathematics/mathematics-phd/"),
    ("chemistry", "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/chemistry/chemistry-phd/"),
    ("cs", "https://bulletins.wayne.edu/graduate/college-engineering/computer-science/computer-science-phd/"),
    ("ece", "https://bulletins.wayne.edu/graduate/college-engineering/electrical-computer-engineering/electrical-engineering-phd/"),
    ("civil", "https://bulletins.wayne.edu/graduate/college-engineering/civil-environmental-engineering/civil-engineering-phd/")
]

cache = {}
for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, 'r', encoding='utf-8'))
        u = d.get('url', '')
        cache[u] = d
    except: pass

for name, u in urls:
    d = cache.get(u)
    if not d: continue
    print("="*60)
    print("PROGRAM:", name, u)
    text = d.get('text', '')
    lines = text.splitlines()
    for i, l in enumerate(lines[:120]):
        clean = l.encode('ascii', errors='replace').decode('ascii')
        print(f"  [{i}] {clean}")
