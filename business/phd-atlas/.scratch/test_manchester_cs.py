import json, hashlib

u_cs = "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/02954/phd-computer-science/"
h = hashlib.sha1(u_cs.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d["text"]

print("CS text len:", len(t))

# Check for supervisor, funding, entry, deadline keywords
import re
for kw in ["supervisor", "deadline", "funding", "entry", "bachelor", "master", "apply"]:
    matches = re.findall(rf"[^\n.]{{0,100}}{kw}[^\n.]{{0,100}}", t, re.I)
    print(f"\nKW: {kw} ({len(matches)} matches)")
    for m in matches[:3]:
        print("  -", m.strip())
