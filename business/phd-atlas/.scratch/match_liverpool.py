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

print(f"Total degree -phd programmes: {len(phds)}")

targets = [
    ("cs", ["computer science"]),
    ("chemistry", ["chemistry"]),
    ("math", ["mathematical sciences", "mathematics"]),
    ("statistics", ["statistics", "mathematical sciences"]),
    ("physics", ["physics"]),
    ("astronomy", ["astrophysics", "physics"]),
    ("biology", ["biological sciences"]),
    ("biomed", ["medicine", "biomedical"]),
    ("neuro", ["neuroscience"]),
    ("earth", ["earth sciences", "earth, ocean"]),
    ("environment", ["environmental sciences", "geography"]),
    ("mech", ["mechanical engineering", "aerospace engineering"]),
    ("civil", ["civil engineering"]),
    ("chemeng", ["chemical engineering", "chemistry"]),
    ("materials", ["materials", "materials science", "chemistry"]),
    ("ece", ["electrical engineering", "electronic"]),
    ("bme", ["bioengineering", "biomedical", "clinical engineering"])
]

for field, patterns in targets:
    print(f"\nTarget field: {field}")
    found = False
    for title, url in sorted(phds.items()):
        if any(p == title.lower() or f"{p}-phd" in url for p in patterns):
            print(f"  MATCH: {title} -> {url}")
            found = True
    if not found:
        print("  NO MATCH FOUND!")
