import json, hashlib, re

urls = [
    ("cs", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"),
    ("chemistry", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/chemistry"),
    ("math", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/mathematics"),
    ("physics", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/physics-and-astronomy"),
    ("biology", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/biosciences-phd-mphil-md"),
    ("biomed", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/medicine"),
    ("neuro", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/psychology"),
    ("earth", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/earth-sciences"),
    ("environment", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/geography-and-planning"),
    ("engineering", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/engineering"),
    ("eng_mech", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-mechanics,-materials-and-advanced-manufacturing"),
    ("eng_health", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-health,-technology-and-the-digital-world"),
    ("eng_energy", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-energy-and-environment")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    t = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]
    print(f"=== {name} ===")
    matches = re.findall(r"(?:entry requirements|bachelor|master|degree|honours|qualification)[^\n.]{0,200}", t, re.I)
    for m in matches[:3]:
        print(" -", m.strip())
