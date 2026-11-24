import hashlib, json, pathlib, requests, bs4, urllib.parse

urls = [
    "https://graduateschool.uccs.edu/academics",
    "https://graduateschool.uccs.edu/admissions",
    "https://graduateschool.uccs.edu/english-proficiency-requirements",
    "https://graduateschool.uccs.edu/prospective-students/entrance-exams",
    "https://graduateschool.uccs.edu/graduate_student_funding",
    "https://graduateschool.uccs.edu/graduate-assistantships",
    "https://graduateschool.uccs.edu/fellowships-scholarships",
    "https://graduateschool.uccs.edu/research-travel-awards",
    "https://www.uccs.edu/admissions-aid/application-details/international",
    "https://eas.uccs.edu/academics/programs/computer-science-phd",
    "https://eas.uccs.edu/academics/programs/engineering-concentration-in-electrical-engineering-phd",
    "https://eas.uccs.edu/graduate-programs/mechanical-engineering-phd",
    "https://eas.uccs.edu/academics/programs/security-phd",
    "https://math.uccs.edu/academics/phd",
    "https://physics.uccs.edu/academics/phd",
]

out = []
for u in urls:
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    p = pathlib.Path(".cache/pages") / f"{h}.json"
    if not p.exists():
        out.append(f"=== MISSING {u} ({h}) ===")
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    txt = d.get("text", "")
    out.append(f"\n============================================================")
    out.append(f"URL: {u}")
    out.append(f"FINAL: {d.get('url')} | STATUS: {d.get('status')} | CHARS: {len(txt)}")
    out.append(f"============================================================")
    out.append(txt[:18000])

pathlib.Path("scratch/uccs_dump1.txt").write_text("\n".join(out), encoding="utf-8")
print("WROTE", len(out))
