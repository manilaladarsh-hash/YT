import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
print(d.get("text", ""))
