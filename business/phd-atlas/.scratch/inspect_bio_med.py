import json, hashlib

urls = [
    ("biosciences", "https://www.nottingham.ac.uk/biosciences/research/"),
    ("medicine", "https://www.nottingham.ac.uk/medicine/research/")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
    t = d["text"]
    print(f"=== {name} ===")
    print(t[:1500])
