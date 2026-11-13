import json, hashlib

u = "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/basic/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
links = d.get("links", [])

for link in links:
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if any(k in txt.lower() for k in ["biological", "bioengineering", "biomedical", "materials", "bio"]):
        if "programmes/list/" in href:
            print(f"{txt} -> {href}")
