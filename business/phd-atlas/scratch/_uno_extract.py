import pathlib, hashlib, json

cache = pathlib.Path(".cache/pages")
urls = [
    "https://www.unomaha.edu/office-of-graduate-studies/admissions/index.php",
    "https://www.unomaha.edu/office-of-graduate-studies/prospective-students/index.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/index.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/index.php",
    "https://www.unomaha.edu/college-of-education-health-and-human-sciences/biomechanics-core-facility/academic-programs/graduate-programs.php",
]
out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16] + ".json"
    p = cache / h
    if not p.exists():
        out.append("MISSING: " + u)
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append("=== " + u + " (chars=" + str(len(d["text"])) + ") ===")
    out.append("LINKS: " + str(d.get("links", [])))
    out.append(d["text"])
pathlib.Path("scratch/_uno_more.txt").write_text("\n".join(out), encoding="utf-8")

for p in pathlib.Path("data/universities").glob("*.json"):
    t = p.read_text(encoding="utf-8")
    if "new scale" in t:
        d = json.loads(t)
        print(p.stem, repr(d["fields"].get("toefl_min", {}).get("code")), repr(d["fields"].get("toefl_min", {}).get("value")))
