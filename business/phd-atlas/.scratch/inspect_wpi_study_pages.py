import glob, json

urls = [
    "https://www.wpi.edu/academics/study/physics-phd",
    "https://www.wpi.edu/academics/study/mathematical-sciences-phd",
    "https://www.wpi.edu/academics/study/phd-statistics",
    "https://www.wpi.edu/academics/study/computer-science-phd",
    "https://www.wpi.edu/academics/study/data-science-phd",
    "https://www.wpi.edu/academics/study/electrical-computer-engineering-phd",
    "https://www.wpi.edu/academics/study/mechanical-engineering-phd",
    "https://www.wpi.edu/academics/study/chemical-engineering-phd",
    "https://www.wpi.edu/academics/study/civil-engineering-phd",
    "https://www.wpi.edu/academics/study/biomedical-engineering-phd",
    "https://www.wpi.edu/academics/study/materials-science-engineering-phd",
    "https://www.wpi.edu/academics/study/molecular-cellular-biology-phd",
    "https://www.wpi.edu/academics/study/chemistry-phd",
    "https://www.wpi.edu/academics/study/bioinformatics-computational-biology-phd",
    "https://www.wpi.edu/academics/study/robotics-engineering-phd",
    "https://www.wpi.edu/academics/study/aerospace-engineering-phd"
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
        print("Missing:", u)
        continue
    text = d.get('text', '')
    lines = text.splitlines()
    print("="*60)
    print("URL:", u)
    for i, line in enumerate(lines):
        if any(w in line.lower() for w in ['department', 'deadline', 'gre', 'funding', 'assistantship', 'stipend', 'admission requirements', 'application requirements', 'bachelor', 'master']):
            clean = line.encode('ascii', errors='replace').decode('ascii')
            print(f"  [{i}] {clean}")
