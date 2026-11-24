import hashlib
import json
import pathlib

urls = [
    "https://www.umassd.edu/graduate/apply/program-specific-requirements/",
    "https://www.umassd.edu/smast/admissions--aid/",
    "https://www.umassd.edu/smast/admissions--aid/assistantships-scholarships--fellowships/",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12705",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12724",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12719",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12767",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12726",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12773",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12774",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12775",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12776",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12777",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12778",
]

out = []
for u in urls:
    p = pathlib.Path(".cache/pages") / (hashlib.sha1(u.encode()).hexdigest()[:16] + ".json")
    d = json.loads(p.read_text(encoding="utf-8"))
    out.append(f"=== {u} (status={d.get('status')}, method={d.get('method')}) ===\n" + d.get("text", ""))

txt = "\n\n".join(out)
pathlib.Path("scratch/umassd_rest.txt").write_text(txt, encoding="utf-8")
print("lines=", len(txt.splitlines()))
