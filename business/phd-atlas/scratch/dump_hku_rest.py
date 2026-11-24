import hashlib
import json
import pathlib

urls = [
    "https://psychology.hku.hk/human-neuroscience-and-artificial-intelligence/",
    "https://ece.hku.hk/study/scholarships/",
    "https://chemistry.hku.hk/study/postgraduate_students/2/",
    "https://chemistry.hku.hk/study/postgraduate_students/13/",
    "https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/fellowships/",
    "https://engg.hku.hk/Teaching-Learning/PhD-MPhil/Fields-of-Study",
    "https://engg.hku.hk/Admissions/PhD-MPhil/Admission-Requirements",
    "https://www.scifac.hku.hk/rpg/programme-info/stipend-support",
    "https://hkumath.hku.hk/web/prospective/p-pg-program.php",
    "https://gradsch.hku.hk/prospective_students/research_areas",
]

out = []
for u in urls:
    p = pathlib.Path(".cache/pages") / (hashlib.sha1(u.encode()).hexdigest()[:16] + ".json")
    if p.exists():
        d = json.loads(p.read_text(encoding="utf-8"))
        out.append(f"=== {u} (status={d.get('status')}, method={d.get('method')}) ===\n" + d.get("text", ""))
    else:
        out.append(f"=== {u} === MISSING")

txt = "\n\n".join(out)
pathlib.Path("scratch/hku_extra2.txt").write_text(txt, encoding="utf-8")
print("lines=", len(txt.splitlines()))
