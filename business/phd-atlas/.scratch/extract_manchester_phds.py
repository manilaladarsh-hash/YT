import json, hashlib

u = "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/basic/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
links = d.get("links", [])
print(f"Total links: {len(links)}")

stem_phds = {}
for link in links:
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if "programmes/list/" in href and href != u:
        for term in ["computer", "chem", "math", "phys", "astro", "bio", "neuro", "earth", "environ", "electr", "mechan", "civil", "mater", "biomed"]:
            if term in txt.lower():
                stem_phds[txt] = href

for txt, href in sorted(stem_phds.items()):
    print(f"{txt} -> {href}")
