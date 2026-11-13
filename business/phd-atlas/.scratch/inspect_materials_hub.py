import json, hashlib

u = "https://www.materials.manchester.ac.uk/study/postgraduate-research/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
t = d.get("text", "")
print("Text:")
print(t[:1500])
print("\nLinks:")
for link in d.get("links", []):
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if any(k in txt.lower() or k in href.lower() for k in ["degree", "programme", "phd", "apply", "requirement"]):
        print(txt, "->", href)
