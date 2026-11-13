import json, hashlib

urls = [
    ("ecs", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-electronics-and-computer-science"),
    ("chem", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-chemistry-and-chemical-engineering"),
    ("phys", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-physics-and-astronomy"),
    ("bio", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-biological-sciences"),
    ("eng", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-engineering"),
    ("mech", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-engineering/department-of-mechanical-engineering"),
    ("civil", "https://www.southampton.ac.uk/about/faculties-schools-departments/department-of-civil-maritime-environmental-engineering"),
    ("math", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-mathematical-sciences"),
    ("earth", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-ocean-and-earth-science"),
    ("env", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-geography-and-environmental-science"),
    ("med", "https://www.southampton.ac.uk/about/faculties-schools-departments/faculty-of-medicine"),
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
    t = d["text"]
    print(f"\n=== {name} ===")
    for line in t.split("\n"):
        line = line.strip()
        if any(k in line.lower() for k in ["contribute to", "phd with us", "phd opportunities", "by completing a phd", "postgraduate research degree"]):
            print("  *", line[:120])
