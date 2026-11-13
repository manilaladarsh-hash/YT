import json, hashlib

u = "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/basic/"
h = hashlib.sha1(u.encode()).hexdigest()[:16]
d = json.load(open(f".cache/pages/{h}.json", encoding="utf-8"))
links = d.get("links", [])

all_phds = {}
for link in links:
    txt = link[0] if isinstance(link, list) else str(link)
    href = link[1] if isinstance(link, list) and len(link) > 1 else ""
    if "programmes/list/" in href and "phd" in href.lower() and href != u:
        all_phds[txt] = href

print(f"Total PhD programmes found: {len(all_phds)}")

targets = [
    ("cs", ["computer science phd", "computer science"]),
    ("chemistry", ["chemistry phd", "inorganic chemistry", "organic chemistry"]),
    ("math", ["pure mathematics phd", "applied mathematics phd", "mathematics phd"]),
    ("statistics", ["probability and statistics phd", "statistics phd", "mathematics phd"]),
    ("physics", ["physics phd/mphil", "physics phd"]),
    ("astronomy", ["astronomy and astrophysics phd", "astrophysics phd"]),
    ("biology", ["biological sciences phd", "biochemistry phd", "molecular biology phd"]),
    ("biomed", ["medicine phd", "medical sciences phd", "biomedical"]),
    ("neuro", ["neuroscience phd/mphil", "neuroscience phd"]),
    ("earth", ["earth science phd/mphil", "earth and environmental sciences"]),
    ("environment", ["environmental science phd/mphil", "environmental engineering phd"]),
    ("mech", ["mechanical engineering phd", "mechanical, aerospace"]),
    ("civil", ["civil engineering phd"]),
    ("chemeng", ["chemical engineering phd"]),
    ("materials", ["materials phd", "materials science phd", "materials chemistry phd"]),
    ("ece", ["electrical and electronic engineering phd"]),
    ("bme", ["biomedical engineering phd", "bioengineering phd", "biomaterials phd"])
]

for field, patterns in targets:
    print(f"\nTarget field: {field}")
    found = False
    for title, url in all_phds.items():
        if any(p in title.lower() for p in patterns):
            print(f"  MATCH: {title} -> {url}")
            found = True
    if not found:
        print("  NO MATCH FOUND!")
