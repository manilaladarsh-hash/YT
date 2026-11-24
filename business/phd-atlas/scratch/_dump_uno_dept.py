import hashlib, json, pathlib

urls = [
    "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/prospective-students/index.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/prospective-students/deadlines-and-forms.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/prospective-students/frequently-asked-questions.php",
    "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/current-students/find-a-thesis-advisor.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/neuroscience/neuro-phd.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/neuroscience/neurorequire.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/io-psych/io-faq.php",
    "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/developmental/devcurriculum.php",
    "https://www.unomaha.edu/college-of-education-health-and-human-sciences/health-kinesiology/phd/index.php",
    "https://www.unomaha.edu/college-of-education-health-and-human-sciences/health-kinesiology/phd/doctoral-research-assistant.php",
]

out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path(f".cache/pages/{h}.json")
    if not p.exists():
        out.append(f"=== MISSING: {u}")
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append(f"=== {u} (final={d.get('final_url')}, chars={len(d.get('text',''))})")
    out.append(d.get("text", ""))
    raw_links = d.get("links", [])
    links = [l for l in raw_links if "catalog.unomaha.edu" in str(l) or "phd" in str(l).lower()]
    if links:
        out.append("LINKS: " + json.dumps(links[:25], ensure_ascii=False))
    out.append("")

pathlib.Path("scratch/_uno_dept.txt").write_text("\n".join(out), encoding="utf-8")
print("Wrote scratch/_uno_dept.txt", len(out))
