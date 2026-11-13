import json, hashlib

u = "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
html = d.get("html", "")
print("HTML len:", len(html))
idx = html.find("section-entry-requirements")
if idx != -1:
    print(html[idx:idx+1500])
else:
    print("section-entry-requirements not found in html")
