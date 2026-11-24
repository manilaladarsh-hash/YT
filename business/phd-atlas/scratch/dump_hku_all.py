import json
from pathlib import Path

CACHE = Path("C:/Users/manil/YT/business/phd-atlas/.cache/pages")
OUT = Path("C:/Users/manil/YT/business/phd-atlas/scratch/hku_cached_summary.txt")

targets = [
    "gradsch.hku.hk/prospective_students/application/faq_on_application",
    "gradsch.hku.hk/prospective_students/application/admission_requirement",
    "gradsch.hku.hk/prospective_students/application/application_period",
    "gradsch.hku.hk/prospective_students/fees",
    "gradsch.hku.hk/prospective_students/financial_support_and_awards/postgraduate_scholarships",
    "gradsch.hku.hk/prospective_students/financial_support_and_awards/hong_kong_phd_fellowship_scheme",
    "engg.hku.hk/Admissions/PhD-MPhil/Admission-Requirements",
    "engg.hku.hk/Admissions/PhD-MPhil/Scholarships-Financial-Assistance-and-Fees",
    "engg.hku.hk/About-Us/Departments",
    "scifac.hku.hk/rpg/apply",
    "scifac.hku.hk/rpg/programme-info/stipend-support",
    "scifac.hku.hk/rpg/programme-info/phd",
    "med.hku.hk/en/teaching-and-learning/postgraduate/rpg",
    "civil.hku.hk/h4_pros_pg_MPhil_PhD.html",
    "cds.hku.hk/prospective-students/postgraduate/",
    "ece.hku.hk/study/admissions/",
    "ece.hku.hk/study/scholarships/",
    "mse.hku.hk/",
    "sbme.hku.hk/",
    "saasweb.hku.hk/programme/rpg/mphil-phd",
    "biosch.hku.hk/teaching/research-postgraduate-programmes/",
    "chemistry.hku.hk/study/postgraduate_students/",
    "earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/",
    "geog.hku.hk/mphil-phd",
    "hkumath.hku.hk/web/prospective/p-pg-admission.php",
    "physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/",
    "physics.hku.hk/research/research_groups/",
    "sbms.hku.hk/",
    "psychology.hku.hk/research-degrees-mphil-phd/",
    "psychology.hku.hk/admission-research-postgraduate/",
    "psychology.hku.hk/human-neuroscience-and-artificial-intelligence/",
    "mech.hku.hk/research-postgraduate/",
]

recs = []
for p in sorted(CACHE.glob("*.json")):
    r = json.loads(p.read_text(encoding="utf-8"))
    u = r.get("url", "")
    if "hku.hk" in u:
        recs.append(r)

lines = []
for r in recs:
    u = r["url"]
    if any(t in u for t in targets):
        lines.append(f"\n{'='*80}\nURL: {u}\nFINAL: {r.get('final_url','')}\nSTATUS: {r.get('status')}\nTEXT:\n{r.get('text','')[:8000]}\n")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {len(lines)} HKU pages to {OUT}")
