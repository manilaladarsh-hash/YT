import json, hashlib

urls = [
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/chemistry",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/mathematics",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/physics-and-astronomy",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/biosciences-phd-mphil-md",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/medicine",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/psychology",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/earth-sciences",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/geography-and-planning",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-mechanics,-materials-and-advanced-manufacturing",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-health,-technology-and-the-digital-world",
    "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-energy-and-environment"
]

for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = f".cache/pages/{h}.json"
    try:
        data = json.load(open(p, encoding="utf-8"))
        print(f"OK ({len(data.get('text', ''))} chars): {u}")
    except Exception as e:
        print(f"MISSING {p}: {u}")
