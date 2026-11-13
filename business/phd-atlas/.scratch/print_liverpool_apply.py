import json, hashlib

u = "https://www.liverpool.ac.uk/study/postgraduate-research/how-to-apply/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]
idx = t.find("You should apply as early as possible")
print(repr(t[idx:idx+600]))
