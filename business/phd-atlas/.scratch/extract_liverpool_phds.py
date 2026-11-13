import json, hashlib

u = "https://www.liverpool.ac.uk/study/postgraduate-research/degrees/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
links = d.get("links", [])
print(f"Total links: {len(links)}")

phds = {}
for link in links:
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if "/courses/" in href:
        phds[txt] = href

print(f"Courses links: {len(phds)}")
for txt, href in sorted(phds.items())[:50]:
    print(f"{txt} -> {href}")
