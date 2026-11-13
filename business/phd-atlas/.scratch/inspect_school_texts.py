import json, hashlib

urls = [
    ("ecs", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-electronics-and-computer-science"),
    ("chem", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-chemistry-and-chemical-engineering"),
    ("phys", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-physics-and-astronomy"),
    ("bio", "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-biological-sciences")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
    t = d["text"]
    print(f"\n=== {name} ({u}) ===")
    print("Length:", len(t))
    # Look for lines containing PhD or research degree
    for line in t.split("\n"):
        line = line.strip()
        if any(k in line.lower() for k in ["phd", "doctoral", "postgraduate research"]):
            print("  *", line[:120])
