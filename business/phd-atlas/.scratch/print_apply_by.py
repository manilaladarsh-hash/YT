import json, hashlib

u = "https://www.liverpool.ac.uk/courses/computer-science-phd"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]

idx = t.find("Apply by")
print(repr(t[idx-200:idx+400]))
