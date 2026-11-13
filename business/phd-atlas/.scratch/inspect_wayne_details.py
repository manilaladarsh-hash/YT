import glob, json

urls = [
    "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/physics-astronomy/physics-phd/",
    "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/mathematics/mathematics-phd/",
    "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/chemistry/chemistry-phd/",
    "https://bulletins.wayne.edu/graduate/college-liberal-arts-sciences/biological-sciences/biological-sciences-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/computer-science/computer-science-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/electrical-computer-engineering/electrical-engineering-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/mechanical-engineering/mechanical-engineering-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/chemical-engineering-materials-science/chemical-engineering-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/chemical-engineering-materials-science/materials-science-engineering-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/civil-environmental-engineering/civil-engineering-phd/",
    "https://bulletins.wayne.edu/graduate/college-engineering/biomedical-engineering/biomedical-engineering-phd/",
    "https://bulletins.wayne.edu/graduate/school-medicine/programs/translational-neuroscience-phd/",
    "https://bulletins.wayne.edu/graduate/school-medicine/programs/oncology/cancer-biology-phd/",
    "https://bulletins.wayne.edu/graduate/school-medicine/programs/biochemistry-microbiology-immunology/biochemistry-molecular-biology-phd/"
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
    if not d: continue
    print("="*60)
    print("URL:", u)
    text = d.get('text', '')
    lines = text.splitlines()
    in_adm = False
    adm_lines = []
    for l in lines:
        if 'admission' in l.lower() or 'requirements' in l.lower():
            in_adm = True
        if in_adm:
            adm_lines.append(l)
            if len(adm_lines) > 25:
                break
    for l in adm_lines[:20]:
        clean = l.encode('ascii', errors='replace').decode('ascii')
        print("  ", clean)
