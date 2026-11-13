import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/applying/how-to-apply"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d.get("text", "")
print("Len:", len(t))
for line in t.splitlines():
    if any(k in line.lower() for k in ["bachelor", "master", "honours", "degree", "entry", "requirement", "qualif"]):
        print(line)
