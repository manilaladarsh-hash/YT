import json, hashlib

u = "https://www.liverpool.ac.uk/engineering/research/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]
print(t[2000:4000])
