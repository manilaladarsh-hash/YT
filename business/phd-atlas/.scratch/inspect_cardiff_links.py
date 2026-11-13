import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
for link in d.get("links", []):
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if any(w in txt.lower() or w in href.lower() for w in ["admissions", "criteria", "entry", "apply", "requirement"]):
        print(txt, "->", href)
