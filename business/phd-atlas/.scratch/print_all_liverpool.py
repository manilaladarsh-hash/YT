import json, hashlib

u = "https://www.liverpool.ac.uk/study/postgraduate-research/degrees/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
links = d.get("links", [])

phds = {}
for link in links:
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if href.endswith("-phd") and "/courses/" in href:
        phds[txt] = href

for t, h in sorted(phds.items()):
    print(f"{t}: {h}")
