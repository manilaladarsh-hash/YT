import json, hashlib

areas = [
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-mechanics,-materials-and-advanced-manufacturing",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-health,-technology-and-the-digital-world",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-energy-and-environment"
]

for a in areas:
    h = hashlib.sha1(a.encode()).hexdigest()[:16]
    t = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]
    print(f"=== {a} ===")
    print(t[:1200])
