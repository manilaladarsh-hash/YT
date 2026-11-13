import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d.get("text", "")
print("Total length:", len(t))
for line in t.splitlines():
    if any(k in line.lower() for k in ["bachelor", "master", "honours", "2:1", "first class", "upper second", "degree"]):
        print("LINE:", line)
