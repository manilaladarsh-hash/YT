import json, hashlib, re

h = hashlib.sha1('https://www.gradoffice.caltech.edu/documents/35541/New_Updated_GRE2026.pdf'.encode()).hexdigest()[:16]
d = json.load(open(f'.cache/pages/{h}.json', encoding='utf-8'))
page = d['text'].lower()

header = "GRADUATE RECORD EXAM (GRE)"
test_cases = [
    ("cs", "Computer Science PhD R"),
    ("chemistry", "Chemistry PhD M"),
    ("math", "Mathematics PhD N"),
    ("physics", "Physics PhD R / (Physics subject test is required)"),
    ("astronomy", "Astrophysics PhD R / (Physics subject test required)"),
    ("biology", "Biology PhD R"),
    ("bme", "Bioengineering PhD R"),
    ("chemeng", "Chemical Engineering PhD R"),
    ("civil", "Civil Engineering PhD R"),
    ("ece", "Electrical Engineering MS - PhD R"),
    ("environment", "Environmental Science and Engineering PhD R"),
    ("earth", "Geology PhD M"),
    ("materials", "Materials Science PhD R"),
    ("mech", "Mechanical Engineering PhD R"),
    ("neuro", "Neurobiology PhD R")
]

kw_pat = r"gre|graduate record"

for name, row in test_cases:
    full_q = f"{header}... {row}"
    kw_match = bool(re.search(kw_pat, full_q, re.I))
    p1 = header.lower() in page
    p2 = row.lower() in page
    print(f"{name:<12}: kw={kw_match}, p1={p1}, p2={p2}")
