import json, hashlib

u = "https://www.liverpool.ac.uk/study/postgraduate-research/degrees/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]

import re
matches = re.findall(r"[^\n.]{0,100}(?:apply by|year round|deadline|rolling)[^\n.]{0,100}", t, re.I)
print(f"Matches on degrees page ({len(matches)}):")
for m in matches[:10]:
    print(" -", m.strip())
