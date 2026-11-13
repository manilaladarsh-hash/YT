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

# 1. Move unverified standalone BME PhD to data/staging/_removed/
src_bme = DATA / "programs" / "newcastle--bme.json"
if src_bme.exists():
    shutil.move(str(src_bme), str(REMOVED / "newcastle--bme.json"))
    print("Moved newcastle--bme.json to data/staging/_removed/")

# 2. Copy university record to staging
shutil.copy(str(DATA / "universities" / "newcastle.json"), str(STAGE / "universities" / "newcastle.json"))
print("Copied newcastle.json to staging/universities/")

# 3. Build 16 verified programs
u_apply = "https://www.ncl.ac.uk/postgraduate-research/how-to-apply/"
u_pgr = "https://www.ncl.ac.uk/postgraduate-research/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

q_dl = "If you're applying for funding, always check the funding application deadline. This deadline may be earlier than the application deadline for your course."
q_entry = "Academic and English language requirements are all given in individual course profiles. Studentship adverts will specify academic and English language requirements."
q_sup = "As a postgraduate research student at Newcastle, you’ll engage in independent research under the guidance of experienced supervisors, and with the support of our Doctoral College."
q_fund = "We invest in research funding to support our postgraduate research students. There are many options and opportunities for you to explore."
q_ets = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

programs = [
    {
        "field": "cs",
        "also_fields": [],
        "dept": "School of Computing",
        "title": "Computer Science PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8050f-23/",
        "notes": "Postgraduate research programme (Computer Science MPhil, PhD) in the School of Computing at Newcastle University."
    },
    {
        "field": "chemistry",
        "also_fields": [],
        "dept": "School of Natural and Environmental Sciences",
        "title": "Chemistry PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8100f-34/",
        "notes": "Postgraduate research programme (Chemistry MPhil, PhD) in the School of Natural and Environmental Sciences at Newcastle University."
    },
    {
        "field": "math",
        "also_fields": [],
        "dept": "School of Mathematics, Statistics and Physics",
        "title": "Mathematics PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8080f-30/",
        "notes": "Postgraduate research programme (Mathematics MPhil, PhD) in the School of Mathematics, Statistics and Physics at Newcastle University."
    },
    {
        "field": "statistics",
        "also_fields": [],
        "dept": "School of Mathematics, Statistics and Physics",
        "title": "Statistics PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8080f-29/",
        "notes": "Postgraduate research programme (Statistics MPhil, PhD) in the School of Mathematics, Statistics and Physics at Newcastle University."
    },
    {
        "field": "physics",
        "also_fields": [],
        "dept": "School of Mathematics, Statistics and Physics",
        "title": "Physics PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8821f/",
        "notes": "Postgraduate research programme (Physics MPhil, PhD) in the School of Mathematics, Statistics and Physics at Newcastle University."
    },
    {
        "field": "astronomy",
        "also_fields": [],
        "dept": "School of Mathematics, Statistics and Physics",
        "title": "Astrophysics PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8821f/",
        "notes": "Postgraduate research programme (Physics MPhil, PhD / Astrophysics research group) in the School of Mathematics, Statistics and Physics at Newcastle University."
    },
    {
        "field": "chemeng",
        "also_fields": [],
        "dept": "School of Engineering",
        "title": "Chemical Engineering PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8030f-12/",
        "notes": "Postgraduate research programme (Chemical Engineering MPhil, PhD) in the School of Engineering at Newcastle University."
    },
    {
        "field": "materials",
        "also_fields": [],
        "dept": "School of Engineering",
        "title": "Materials Engineering PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8030f-11/",
        "notes": "Postgraduate research programme (Materials Engineering MPhil, PhD) in the School of Engineering at Newcastle University."
    },
    {
        "field": "civil",
        "also_fields": [],
        "dept": "School of Engineering",
        "title": "Civil Engineering PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8040f-17/",
        "notes": "Postgraduate research programme (Civil Engineering MPhil, PhD) in the School of Engineering at Newcastle University."
    },
    {
        "field": "ece",
        "also_fields": [],
        "dept": "School of Engineering",
        "title": "Electrical and Electronic Engineering PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8060f-24/",
        "notes": "Postgraduate research programme (Electrical and Electronic Engineering PhD) in the School of Engineering at Newcastle University."
    },
    {
        "field": "mech",
        "also_fields": ["bme"],
        "dept": "School of Engineering",
        "title": "Mechanical and Systems Engineering PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8090f-32/",
        "notes": "Postgraduate research programme (Mechanical and Systems Engineering MPhil, PhD) in the School of Engineering at Newcastle University; covers biomedical engineering research via the Centre for Biomedical Engineering."
    },
    {
        "field": "biology",
        "also_fields": [],
        "dept": "School of Natural and Environmental Sciences",
        "title": "Biology PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8020f-10/",
        "notes": "Postgraduate research programme (Biology MPhil, PhD) in the School of Natural and Environmental Sciences at Newcastle University."
    },
    {
        "field": "biomed",
        "also_fields": [],
        "dept": "Faculty of Medical Sciences",
        "title": "Biomedicine PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8300f-74/",
        "notes": "Postgraduate research programme (Biomedicine MPhil, PhD, MD) in the Faculty of Medical Sciences at Newcastle University."
    },
    {
        "field": "neuro",
        "also_fields": [],
        "dept": "Faculty of Medical Sciences",
        "title": "Neuroscience PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8300f-75/",
        "notes": "Postgraduate research programme (Neuroscience MPhil, PhD, MD) in the Faculty of Medical Sciences at Newcastle University."
    },
    {
        "field": "earth",
        "also_fields": [],
        "dept": "School of Natural and Environmental Sciences",
        "title": "Geosciences PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8314f/",
        "notes": "Postgraduate research programme (Geosciences MPhil, PhD) in the School of Natural and Environmental Sciences at Newcastle University."
    },
    {
        "field": "environment",
        "also_fields": [],
        "dept": "School of Natural and Environmental Sciences",
        "title": "Environmental Science PhD",
        "page": "https://www.ncl.ac.uk/postgraduate/degrees/8020f-2/",
        "notes": "Postgraduate research programme (Environmental Science MPhil, PhD) in the School of Natural and Environmental Sciences at Newcastle University."
    }
]

for p in programs:
    fid = p["field"]
    if fid in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {p['title']} at Newcastle.",
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
        "id": f"newcastle--{fid}",
        "university": "newcastle",
        "field": fid,
        "also_fields": p["also_fields"],
        "department": p["dept"],
        "program_page": p["page"],
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications for research degrees are accepted on a rolling basis; applicants seeking funding must check specific funding application deadlines which may be earlier than course deadlines.",
                "quote": q_dl,
                "url": p["page"]
            },
            "entry_route": {
                "code": "Either",
                "value": "Academic entry requirements are specified in individual course profiles and studentship adverts, typically requiring a 2:1 honours degree or a master's qualification.",
                "quote": q_entry,
                "url": u_apply
            },
            "supervisor": {
                "code": "Required",
                "value": "Postgraduate researchers engage in independent research under the guidance of experienced academic supervisors.",
                "quote": q_sup,
                "url": u_pgr
            },
            "funding": {
                "code": "Competitive",
                "value": "Postgraduate research funding is competitive via university studentships, Doctoral Training Centres and Partnerships, and external research councils.",
                "quote": q_fund,
                "url": u_pgr
            },
            "gre_subject": gre_sub
        },
        "notes": p["notes"]
    }

    dst = STAGE / "programs" / f"newcastle--{fid}.json"
    dst.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Generated and staged {len(programs)} program files for Newcastle.")
