import json, hashlib, re

urls = [
    ("cs", "https://www.nottingham.ac.uk/pgstudy/course/research/computer-science-phd"),
    ("chemistry", "https://www.nottingham.ac.uk/pgstudy/course/research/chemistry-phd"),
    ("math", "https://www.nottingham.ac.uk/pgstudy/course/research/mathematics-phd"),
    ("physics", "https://www.nottingham.ac.uk/pgstudy/course/research/physics-phd"),
    ("civil", "https://www.nottingham.ac.uk/pgstudy/course/research/civil-engineering-phd"),
    ("chemeng", "https://www.nottingham.ac.uk/pgstudy/course/research/chemical-engineering-phd"),
    ("ece", "https://www.nottingham.ac.uk/pgstudy/course/research/electrical-and-electronic-engineering-phd"),
    ("mech", "https://www.nottingham.ac.uk/pgstudy/course/research/mechanical-engineering-phd"),
    ("materials", "https://www.nottingham.ac.uk/pgstudy/course/research/materials-engineering-and-materials-design-phd"),
    ("psychology", "https://www.nottingham.ac.uk/pgstudy/course/research/psychology-phd"),
    ("geography", "https://www.nottingham.ac.uk/pgstudy/course/research/geography-phd")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
    t = d["text"]
    m = re.findall(r"(?:2:1|honours|bachelor|master)[^\n.]{0,100}", t, re.I)
    print(f"\n=== {name} ===")
    for match in m[:3]:
        print("  -", match.strip())
