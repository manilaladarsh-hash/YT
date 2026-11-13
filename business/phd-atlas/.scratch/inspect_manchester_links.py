import json, hashlib

u = "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
links = d.get("links", [])
print(f"Total links: {len(links)}")
phd_links = []
for link in links:
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if "programmes/list" in href:
        phd_links.append((txt, href))

print(f"PGR links: {len(phd_links)}")
for txt, href in phd_links[:40]:
    print(f"{txt} -> {href}")
