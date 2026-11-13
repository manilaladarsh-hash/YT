import json, hashlib

u = "https://www.liverpool.ac.uk/study/postgraduate-research/courses/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
print("Text:")
print(d.get("text", ""))
print("\nLinks:")
for link in d.get("links", []):
    print(link)
