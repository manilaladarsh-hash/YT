import pathlib, hashlib, json

cache = pathlib.Path(".cache/pages")
urls = [
    "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/index.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/academics/computing_and_information_science_phd.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/neuroscience/index.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/io-psych/index.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/developmental/index.php",
    "https://catalog.unomaha.edu/graduate/financing-education/graduate-assistantships/",
    "https://catalog.unomaha.edu/graduate/financing-education/",
    "https://www.unomaha.edu/office-of-graduate-studies/admissions/how-to-apply-international.php",
    "https://www.unomaha.edu/college-of-education-health-and-human-sciences/health-kinesiology/index.php",
    "https://catalog.une.edu/graduate/programs/",
    "https://www.une.edu/academics/programs",
    "https://psl.eu/en/education/doctorate-psl",
    "https://psl.eu/en/education/psl-phd-tracks",
]
out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16] + ".json"
    p = cache / h
    if not p.exists():
        out.append("MISSING: " + u)
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append(f"=== {u} -> {d.get('final_url')} (chars={len(d['text'])}) ===")
    links = [l for l in d.get("links", []) if len(l) == 2]
    # Keep short summary of interesting links
    rel = [l for l in links if any(k in (l[0]+l[1]).lower() for k in ("phd", "doctor", "track", "fund", "assist", "stipend", "apply", "admiss", "faq", "handb", "neuro", "bio", "chem", "comp", "astro", "math", "phys", "ecole", "gsbse", "une.edu", "psl"))]
    out.append("LINKS: " + str(rel[:50]))
    out.append(d["text"])
pathlib.Path("scratch/_uno_une_psl.txt").write_text("\n".join(out), encoding="utf-8")
print("WROTE", len(out))
