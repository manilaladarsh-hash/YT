import json, hashlib

urls = [
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-electronics-and-computer-science",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-chemistry-and-chemical-engineering",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-physics-and-astronomy",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-biological-sciences",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-engineering/department-of-mechanical-engineering",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/department-of-civil-maritime-environmental-engineering",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-mathematical-sciences",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-ocean-and-earth-science",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-geography-and-environmental-science",
    "https://www.southampton.ac.uk/about/faculties-schools-departments/faculty-of-medicine",
]

for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = f".cache/pages/{h}.json"
    try:
        d = json.load(open(p, encoding="utf-8"))
        print(f"OK ({d.get('status')}): {u} (len={len(d.get('text', ''))})")
    except Exception as e:
        print(f"MISSING: {u} ({e})")
