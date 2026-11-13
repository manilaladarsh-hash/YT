import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/applying/admissions-criteria"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d.get("text", "")
print(t)
