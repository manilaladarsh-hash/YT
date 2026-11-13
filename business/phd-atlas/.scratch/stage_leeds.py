import json
import shutil
from pathlib import Path

ROOT = Path("C:/Users/manil/YT/business/phd-atlas")
STAGE = ROOT / "data" / "staging"
DATA = ROOT / "data"
REMOVED = STAGE / "_removed"

REMOVED.mkdir(parents=True, exist_ok=True)
(STAGE / "programs").mkdir(parents=True, exist_ok=True)
(STAGE / "universities").mkdir(parents=True, exist_ok=True)

# 1. Move unverified standalone programs bme & materials to data/staging/_removed/
for field in ["bme", "materials"]:
    src = DATA / "programs" / f"leeds--{field}.json"
    if src.exists():
        dst = REMOVED / f"leeds--{field}.json"
        shutil.move(str(src), str(dst))
        print(f"Moved leeds--{field}.json to data/staging/_removed/")

# 2. Copy university record to staging
shutil.copy(str(DATA / "universities" / "leeds.json"), str(STAGE / "universities" / "leeds.json"))
print("Copied leeds.json to staging/universities/")

# 3. Build 15 program records
u_apply = "https://www.leeds.ac.uk/research-applying/doc/applying-research-degrees"
u_entry = "https://environment.leeds.ac.uk/see-research-degrees/doc/entry-requirements"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

q_dl = "We advise you to apply at least four months before your proposed start date. This is to allow sufficient time to review your application and undertake any additional checks."
q_entry = "The minimum entry requirements for PhD study is a 2.1 honours degree, or equivalent, in a subject relating to your proposed area of research, or a good performance in a Masters level course in a relevant subject."
q_sup = "You need to identify the supervisors available to work with you. They must be experts in the topic you are interested in to ensure that your research is accurate and adding to current knowledge."
q_fund = "UK research councils: competition for these scholarships is high but the majority of your fees will be funded so it is well worth applying."
q_ets = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

programs = [
    {
        "field": "cs",
        "also_fields": [],
        "dept": "School of Computing",
        "title": "Computing PhD",
        "page": "https://eps.leeds.ac.uk/computing-research-degrees",
        "notes": "Postgraduate research programme (Computing PhD) in the School of Computing at the University of Leeds."
    },
    {
        "field": "physics",
        "also_fields": [],
        "dept": "School of Physics and Astronomy",
        "title": "Physics PhD",
        "page": "https://eps.leeds.ac.uk/physics-research-degrees",
        "notes": "Postgraduate research programme (Physics PhD) in the School of Physics and Astronomy at the University of Leeds."
    },
    {
        "field": "astronomy",
        "also_fields": [],
        "dept": "School of Physics and Astronomy",
        "title": "Astrophysics PhD",
        "page": "https://eps.leeds.ac.uk/physics-research-degrees",
        "notes": "Postgraduate research programme (Astrophysics PhD) in the School of Physics and Astronomy at the University of Leeds."
    },
    {
        "field": "chemistry",
        "also_fields": [],
        "dept": "School of Chemistry",
        "title": "Chemistry PhD",
        "page": "https://eps.leeds.ac.uk/chemistry-research-degrees",
        "notes": "Postgraduate research programme (Chemistry PhD) in the School of Chemistry at the University of Leeds."
    },
    {
        "field": "chemeng",
        "also_fields": ["materials"],
        "dept": "School of Chemical and Process Engineering",
        "title": "Chemical and Process Engineering PhD",
        "page": "https://eps.leeds.ac.uk/chemical-engineering-research-degrees",
        "notes": "Postgraduate research programme (Chemical and Process Engineering PhD) in the School of Chemical and Process Engineering at the University of Leeds; covers materials science and engineering."
    },
    {
        "field": "civil",
        "also_fields": [],
        "dept": "School of Civil Engineering",
        "title": "Civil Engineering PhD",
        "page": "https://eps.leeds.ac.uk/civil-engineering-research-degrees",
        "notes": "Postgraduate research programme (Civil Engineering PhD) in the School of Civil Engineering at the University of Leeds."
    },
    {
        "field": "ece",
        "also_fields": [],
        "dept": "School of Electronic and Electrical Engineering",
        "title": "Electronic and Electrical Engineering PhD",
        "page": "https://eps.leeds.ac.uk/electronic-engineering-research-degrees",
        "notes": "Postgraduate research programme (Electronic and Electrical Engineering PhD) in the School of Electronic and Electrical Engineering at the University of Leeds."
    },
    {
        "field": "mech",
        "also_fields": ["bme"],
        "dept": "School of Mechanical Engineering",
        "title": "Mechanical Engineering PhD",
        "page": "https://eps.leeds.ac.uk/mechanical-engineering-research-degrees",
        "notes": "Postgraduate research programme (Mechanical Engineering PhD) in the School of Mechanical Engineering at the University of Leeds; covers medical and biological engineering."
    },
    {
        "field": "math",
        "also_fields": [],
        "dept": "School of Mathematics",
        "title": "Mathematics PhD",
        "page": "https://eps.leeds.ac.uk/maths-research-degrees",
        "notes": "Postgraduate research programme (Mathematics PhD) in the School of Mathematics at the University of Leeds."
    },
    {
        "field": "statistics",
        "also_fields": [],
        "dept": "School of Mathematics",
        "title": "Statistics PhD",
        "page": "https://eps.leeds.ac.uk/maths-research-degrees",
        "notes": "Postgraduate research programme (Statistics PhD) in the Department of Statistics / School of Mathematics at the University of Leeds."
    },
    {
        "field": "biology",
        "also_fields": [],
        "dept": "Faculty of Biological Sciences",
        "title": "Biological Sciences PhD",
        "page": "https://biologicalsciences.leeds.ac.uk/research-degrees",
        "notes": "Postgraduate research programme (Biological Sciences PhD) in the Faculty of Biological Sciences at the University of Leeds."
    },
    {
        "field": "biomed",
        "also_fields": [],
        "dept": "School of Biomedical Sciences",
        "title": "Biomedical Sciences PhD",
        "page": "https://biologicalsciences.leeds.ac.uk/research-degrees",
        "notes": "Postgraduate research programme (Biomedical Sciences PhD) in the School of Biomedical Sciences / Faculty of Biological Sciences at the University of Leeds."
    },
    {
        "field": "earth",
        "also_fields": [],
        "dept": "School of Earth and Environment",
        "title": "Earth Sciences PhD",
        "page": "https://environment.leeds.ac.uk/see-research-degrees",
        "notes": "Postgraduate research programme (Earth Sciences PhD) in the School of Earth and Environment at the University of Leeds."
    },
    {
        "field": "environment",
        "also_fields": [],
        "dept": "School of Earth and Environment",
        "title": "Environmental Science PhD",
        "page": "https://environment.leeds.ac.uk/see-research-degrees",
        "notes": "Postgraduate research programme (Environmental Science PhD) in the School of Earth and Environment at the University of Leeds."
    },
    {
        "field": "neuro",
        "also_fields": [],
        "dept": "School of Psychology",
        "title": "Psychology / Cognitive Neuroscience PhD",
        "page": "https://medicinehealth.leeds.ac.uk/psychology-research-degrees",
        "notes": "Postgraduate research programme (Psychology / Cognitive Neuroscience PhD) in the School of Psychology at the University of Leeds."
    }
]

for p in programs:
    fid = p["field"]
    if fid in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {p['title']} at Leeds.",
            "quote": "",
            "url": u_apply
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": q_ets,
            "url": u_ets
        }

    rec = {
        "id": f"leeds--{fid}",
        "university": "leeds",
        "field": fid,
        "also_fields": p["also_fields"],
        "department": p["dept"],
        "program_page": p["page"],
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applicants are advised to apply at least four months before their proposed start date; admissions operate on a rolling basis across multiple start dates.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Minimum entry requirements are a 2.1 honours degree or good performance in a Master's level course in a relevant subject.",
                "quote": q_entry,
                "url": u_entry
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants need to identify and contact available academic supervisors who are experts in their research topic prior to applying.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Competition for research council scholarships and faculty awards is high and funding is competitive.",
                "quote": q_fund,
                "url": u_apply
            },
            "gre_subject": gre_sub
        },
        "notes": p["notes"]
    }

    dst = STAGE / "programs" / f"leeds--{fid}.json"
    dst.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Generated and staged 15 program files for Leeds.")
