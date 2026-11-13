import json, hashlib

urls = [
    ("mech", "https://www.liverpool.ac.uk/engineering/departments/mechanical-and-aerospace-engineering/"),
    ("civil", "https://www.liverpool.ac.uk/engineering/departments/civil-and-environmental-engineering/")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
    t = d["text"]
    print(f"=== {name} ===")
    print(t[:1200])
