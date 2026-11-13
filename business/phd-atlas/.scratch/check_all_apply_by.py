import json, hashlib

urls = [
    ("cs", "https://www.liverpool.ac.uk/courses/computer-science-phd"),
    ("chemistry", "https://www.liverpool.ac.uk/courses/chemistry-phd"),
    ("math", "https://www.liverpool.ac.uk/courses/mathematical-sciences-phd"),
    ("physics", "https://www.liverpool.ac.uk/courses/physics-phd"),
    ("biology", "https://www.liverpool.ac.uk/courses/biological-sciences-phd"),
    ("biomed", "https://www.liverpool.ac.uk/courses/clinical-science-phd"),
    ("neuro", "https://www.liverpool.ac.uk/courses/neurological-science-phd"),
    ("earth", "https://www.liverpool.ac.uk/courses/earth-sciences-phd"),
    ("environment", "https://www.liverpool.ac.uk/courses/environmental-science-phd"),
    ("ece", "https://www.liverpool.ac.uk/courses/electrical-engineering-and-electronics-phd"),
    ("materials", "https://www.liverpool.ac.uk/courses/materials-design-and-manufacturing-phd"),
    ("bme", "https://www.liverpool.ac.uk/courses/bioengineering-phd"),
    ("statistics", "https://www.liverpool.ac.uk/courses/biostatistics-phd"),
    ("mech", "https://www.liverpool.ac.uk/engineering/departments/mechanical-and-aerospace-engineering/"),
    ("civil", "https://www.liverpool.ac.uk/engineering/departments/civil-and-environmental-engineering/")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
    t = d["text"]
    idx = t.find("Apply by")
    if idx != -1:
        print(f"{name}: FOUND 'Apply by' -> {repr(t[idx:idx+25])}")
    else:
        print(f"{name}: NOT FOUND")
