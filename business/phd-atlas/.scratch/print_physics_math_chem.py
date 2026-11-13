import glob, json

urls = [
    ("physics", "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/physics-astronomy/physics-phd/"),
    ("math", "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/mathematics/mathematics-phd/"),
    ("chemistry", "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/chemistry/chemistry-phd/")
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
    lines = d.get('text', '').splitlines()
    for i in range(55, min(len(lines), 95)):
        clean = lines[i].encode('ascii', errors='replace').decode('ascii')
        print(f"  [{i}] {clean}")
