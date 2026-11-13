import json, hashlib, re

u = "https://www.nottingham.ac.uk/pgstudy/course/research/computer-science-phd"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]

matches = re.findall(r"[^\n.]{0,100}(?:apply|application|deadline|supervisor)[^\n.]{0,100}", t, re.I)
for m in matches[:10]:
    print(" -", m.strip())
