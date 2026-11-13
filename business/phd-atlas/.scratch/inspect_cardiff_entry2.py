import json, hashlib

urls = [
    ("cs", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"),
    ("chemistry", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/chemistry"),
    ("engineering", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/engineering")
]

for name, u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    t = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))["text"]
    print(f"=== {name} ===")
    idx = t.find("Entry requirements")
    if idx != -1:
        print(t[idx:idx+800])
    else:
        print("Not found")
