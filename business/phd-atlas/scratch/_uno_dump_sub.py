import pathlib, hashlib, json

cache = pathlib.Path(".cache/pages")
urls = [
    "https://www.unomaha.edu/office-of-graduate-studies/prospective-students/affording-your-education.php",
    "https://catalog.unomaha.edu/graduate/admission/",
    "https://www.unomaha.edu/college-of-information-science-and-technology/academics/graduate-programs-in-ist.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/admissions/scholarships.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/school-of-interdisciplinary-informatics/index.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/index.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/about-us/forms-resources/index.php",
    "https://www.unomaha.edu/college-of-education-health-and-human-sciences/biomechanics-core-facility/involvement-opportunities/graduate-assistantships.php",
    "https://www.unomaha.edu/college-of-education-health-and-human-sciences/biomechanics-core-facility/academic-programs/awards-scholarships-biomechanics.php",
]
out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16] + ".json"
    p = cache / h
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append(f"=== {u} -> {d.get('final_url')} (chars={len(d['text'])}) ===")
    links = [l for l in d.get("links", []) if len(l) == 2 and ("phd" in l[1].lower() or "psych" in l[1].lower() or "ist" in l[1].lower() or "bmi" in l[1].lower() or "cis" in l[1].lower() or "grad" in l[1].lower() or "assist" in l[1].lower() or "fund" in l[1].lower() or "afford" in l[1].lower() or "scholar" in l[1].lower() or "neuro" in l[1].lower() or "kines" in l[1].lower())]
    out.append("RELEVANT_LINKS: " + str(links))
    out.append(d["text"])
pathlib.Path("scratch/_uno_subpages.txt").write_text("\n".join(out), encoding="utf-8")
print("WROTE", len(out))
