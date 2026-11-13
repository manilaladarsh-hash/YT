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

# 1. Move 4 unverified programs to data/staging/_removed/
for field in ["chemistry", "chemeng", "bme", "materials"]:
    src = DATA / "programs" / f"exeter--{field}.json"
    if src.exists():
        dst = REMOVED / f"exeter--{field}.json"
        shutil.move(str(src), str(dst))
        print(f"Moved exeter--{field}.json to data/staging/_removed/")

# 2. Copy university record to staging
shutil.copy(str(DATA / "universities" / "exeter.json"), str(STAGE / "universities" / "exeter.json"))
print("Copied exeter.json to staging/universities/")

# 3. Build 13 verified programs
u_apply = "https://www.exeter.ac.uk/study/pg-research/apply/"
u_entry = "https://www.exeter.ac.uk/study/pg-research/entryrequirements/"
u_fund = "https://www.exeter.ac.uk/study/pg-research/funding/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

q_dl = "The application deadlines for September starters are:\n30 June for International Applicants"
q_entry = "For all research degrees you will normally be required to have obtained or expect to obtain a first degree equivalent to at least a UK 2:1 Honours degree."
q_sup = "You will only be able to pursue a research degree with us if we can offer appropriate supervision."
q_fund = "Money is the single biggest barrier to people undertaking postgraduate study, and securing funding for your PhD is vital to realising your ambitions."
q_ets = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

programs = [
    {
        "field": "cs",
        "also_fields": [],
        "dept": "Department of Computer Science",
        "title": "Computer Science PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/computerscience/",
        "notes": "Postgraduate research programme (MPhil/PhD Computer Science) in the Department of Computer Science at the University of Exeter."
    },
    {
        "field": "ece",
        "also_fields": [],
        "dept": "Department of Engineering",
        "title": "Electronic Engineering PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/engineering/",
        "notes": "Postgraduate research programme (MPhil/PhD Engineering / Electronic Engineering) in the Department of Engineering at the University of Exeter."
    },
    {
        "field": "mech",
        "also_fields": ["bme", "materials"],
        "dept": "Department of Engineering",
        "title": "Mechanical Engineering PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/engineering/",
        "notes": "Postgraduate research programme (MPhil/PhD Engineering / Mechanical Engineering) in the Department of Engineering at the University of Exeter; covers materials and biomedical engineering research."
    },
    {
        "field": "civil",
        "also_fields": [],
        "dept": "Department of Engineering",
        "title": "Civil Engineering PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/engineering/",
        "notes": "Postgraduate research programme (MPhil/PhD Engineering / Civil and Structures) in the Department of Engineering at the University of Exeter."
    },
    {
        "field": "math",
        "also_fields": [],
        "dept": "Department of Mathematics and Statistics",
        "title": "Mathematics PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/mathematics/",
        "notes": "Postgraduate research programme (MPhil/PhD Mathematics) in the Department of Mathematics and Statistics at the University of Exeter."
    },
    {
        "field": "statistics",
        "also_fields": [],
        "dept": "Department of Mathematics and Statistics",
        "title": "Statistics PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/mathematics/",
        "notes": "Postgraduate research programme (MPhil/PhD Mathematics / Statistics research group) in the Department of Mathematics and Statistics at the University of Exeter."
    },
    {
        "field": "physics",
        "also_fields": [],
        "dept": "Department of Physics and Astronomy",
        "title": "Physics PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/physics/",
        "notes": "Postgraduate research programme (MPhil/PhD Physics) in the Department of Physics and Astronomy at the University of Exeter."
    },
    {
        "field": "astronomy",
        "also_fields": [],
        "dept": "Department of Physics and Astronomy",
        "title": "Astrophysics PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/physics/",
        "notes": "Postgraduate research programme (MPhil/PhD Physics / Astrophysics research group) in the Department of Physics and Astronomy at the University of Exeter."
    },
    {
        "field": "biology",
        "also_fields": [],
        "dept": "Department of Biosciences",
        "title": "Biological Sciences PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/biosciences/",
        "notes": "Postgraduate research programme (MPhil/PhD Biological Sciences) in the Department of Biosciences at the University of Exeter."
    },
    {
        "field": "biomed",
        "also_fields": [],
        "dept": "Department of Clinical and Biomedical Sciences",
        "title": "Clinical and Biomedical Sciences PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/medicine/clinicalandbiomedicalsciences/",
        "notes": "Postgraduate research programme (MPhil/PhD Clinical and Biomedical Sciences) in the Faculty of Health and Life Sciences at the University of Exeter."
    },
    {
        "field": "neuro",
        "also_fields": [],
        "dept": "Faculty of Health and Life Sciences",
        "title": "Neuroscience PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/medicine/neuroscience/",
        "notes": "Postgraduate research programme (MPhil/PhD Neuroscience) in the Faculty of Health and Life Sciences at the University of Exeter."
    },
    {
        "field": "earth",
        "also_fields": [],
        "dept": "Camborne School of Mines / Department of Earth and Environmental Science",
        "title": "Geology / Earth Sciences PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/geology/",
        "notes": "Postgraduate research programme (MPhil/PhD Geology) in the Camborne School of Mines at the University of Exeter."
    },
    {
        "field": "environment",
        "also_fields": [],
        "dept": "Department of Earth and Environmental Science",
        "title": "Climate Change and Environment PhD",
        "page": "https://www.exeter.ac.uk/study/pg-research/degrees/climatechange/",
        "notes": "Postgraduate research programme (MPhil/PhD Environmental Intelligence / Climate Change) at the University of Exeter."
    }
]

for p in programs:
    fid = p["field"]
    if fid in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {p['title']} at Exeter.",
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
        "id": f"exeter--{fid}",
        "university": "exeter",
        "field": fid,
        "also_fields": p["also_fields"],
        "department": p["dept"],
        "program_page": p["page"],
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "2027-06-30",
                "value": "The application deadline for September starters is 30 June for International Applicants (and 31 July for Home Applicants).",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "For all research degrees applicants are normally required to have obtained or expect to obtain a first degree equivalent to at least a UK 2:1 Honours degree.",
                "quote": q_entry,
                "url": u_entry
            },
            "supervisor": {
                "code": "Required",
                "value": "Admission is conditional on appropriate supervisory capacity and guidance in the chosen research field.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Postgraduate research funding is competitive via university studentships, research council awards (such as EPSRC), and bespoke supervisor funding.",
                "quote": q_fund,
                "url": u_fund
            },
            "gre_subject": gre_sub
        },
        "notes": p["notes"]
    }

    dst = STAGE / "programs" / f"exeter--{fid}.json"
    dst.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Generated and staged {len(programs)} program files for Exeter.")
