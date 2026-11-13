import json, hashlib

u = "https://www.liverpool.ac.uk/study/postgraduate-research/how-to-apply/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]
print("Text len:", len(t))

import re
matches = re.findall(r"[^\n.]{0,100}(?:deadline|apply|funding|intake|start)[^\n.]{0,100}", t, re.I)
for m in matches[:15]:
    print(" -", m.strip())
