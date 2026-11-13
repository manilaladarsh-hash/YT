import json
import shutil
from pathlib import Path

ROOT = Path("C:/Users/manil/YT/business/phd-atlas")
STAGE = ROOT / "data" / "staging"
DATA = ROOT / "data"

(STAGE / "programs").mkdir(parents=True, exist_ok=True)
(STAGE / "universities").mkdir(parents=True, exist_ok=True)

# 1. Copy university record to staging
shutil.copy(str(DATA / "universities" / "sheffield.json"), str(STAGE / "universities" / "sheffield.json"))
print("Copied sheffield.json to staging/universities/")

# 2. Build 17 program records
u_apply = "https://www.sheffield.ac.uk/postgraduate/phd/apply"
u_scholarships = "https://sheffield.ac.uk/postgraduate/phd/scholarships"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

q_dl = "Although we advise students to start in September/October, it's often possible to start postgraduate research at any point in the year. You can state your preferred start date in your application, although this will need to be confirmed by the academic school."
q_entry = "Information about academic entry requirements is available from the school in which your research is based. Entry requirements vary depending on what you study – some subjects require a masters degree, others ask for a good undergraduate degree (a 2:1 or a First)."
q_sup = "If you want to research your own idea, you should contact the relevant academic school before you submit a formal application, to check that they have an appropriately-qualified supervisor in the area you'd like to study."
q_fund = "Schools and supervisors may have funding for specific projects throughout the year."
q_ets = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

programs = [
    {
        "field": "cs",
        "dept": "Department of Computer Science",
        "title": "Computer Science PhD",
        "page": "https://sheffield.ac.uk/cs/phd-study",
        "notes": "Postgraduate research programme (Computer Science PhD) in the Department of Computer Science at the University of Sheffield."
    },
    {
        "field": "chemistry",
        "dept": "School of Mathematical and Physical Sciences",
        "title": "Chemistry PhD",
        "page": "https://sheffield.ac.uk/mps/research/chemistry",
        "notes": "Postgraduate research programme (Chemistry PhD) in the School of Mathematical and Physical Sciences at the University of Sheffield."
    },
    {
        "field": "math",
        "dept": "School of Mathematical and Physical Sciences",
        "title": "Mathematics PhD",
        "page": "https://sheffield.ac.uk/mps/research/maths",
        "notes": "Postgraduate research programme (Mathematics PhD) in the School of Mathematical and Physical Sciences at the University of Sheffield."
    },
    {
        "field": "statistics",
        "dept": "School of Mathematical and Physical Sciences",
        "title": "Statistics PhD",
        "page": "https://sheffield.ac.uk/mps/research/maths",
        "notes": "Postgraduate research programme (Statistics PhD) in the School of Mathematical and Physical Sciences at the University of Sheffield."
    },
    {
        "field": "physics",
        "dept": "School of Mathematical and Physical Sciences",
        "title": "Physics PhD",
        "page": "https://sheffield.ac.uk/mps/research/physics",
        "notes": "Postgraduate research programme (Physics PhD) in the School of Mathematical and Physical Sciences at the University of Sheffield."
    },
    {
        "field": "astronomy",
        "dept": "School of Mathematical and Physical Sciences",
        "title": "Astrophysics PhD",
        "page": "https://sheffield.ac.uk/mps/research/physics",
        "notes": "Postgraduate research programme (Astrophysics PhD) in the School of Mathematical and Physical Sciences at the University of Sheffield."
    },
    {
        "field": "mech",
        "dept": "School of Mechanical, Aerospace and Civil Engineering",
        "title": "Mechanical Engineering PhD",
        "page": "https://sheffield.ac.uk/mac/phd",
        "notes": "Postgraduate research programme (Mechanical Engineering PhD) in the School of Mechanical, Aerospace and Civil Engineering at the University of Sheffield."
    },
    {
        "field": "civil",
        "dept": "School of Mechanical, Aerospace and Civil Engineering",
        "title": "Civil Engineering PhD",
        "page": "https://sheffield.ac.uk/mac/phd",
        "notes": "Postgraduate research programme (Civil Engineering PhD) in the School of Mechanical, Aerospace and Civil Engineering at the University of Sheffield."
    },
    {
        "field": "chemeng",
        "dept": "School of Chemical, Materials and Biological Engineering",
        "title": "Chemical Engineering PhD",
        "page": "https://sheffield.ac.uk/cmbe/phd",
        "notes": "Postgraduate research programme (Chemical Engineering PhD) in the School of Chemical, Materials and Biological Engineering at the University of Sheffield."
    },
    {
        "field": "materials",
        "dept": "School of Chemical, Materials and Biological Engineering",
        "title": "Materials Science and Engineering PhD",
        "page": "https://sheffield.ac.uk/cmbe/phd",
        "notes": "Postgraduate research programme (Materials Science and Engineering PhD) in the School of Chemical, Materials and Biological Engineering at the University of Sheffield."
    },
    {
        "field": "bme",
        "dept": "School of Chemical, Materials and Biological Engineering",
        "title": "Bioengineering / Biomedical Engineering PhD",
        "page": "https://sheffield.ac.uk/cmbe/phd",
        "notes": "Postgraduate research programme (Bioengineering / Biomedical Engineering PhD) in the School of Chemical, Materials and Biological Engineering at the University of Sheffield."
    },
    {
        "field": "ece",
        "dept": "School of Electrical and Electronic Engineering",
        "title": "Electronic and Electrical Engineering PhD",
        "page": "https://sheffield.ac.uk/eee/phd",
        "notes": "Postgraduate research programme (Electronic and Electrical Engineering PhD) in the School of Electrical and Electronic Engineering at the University of Sheffield."
    },
    {
        "field": "biology",
        "dept": "School of Biosciences",
        "title": "Biosciences PhD",
        "page": "https://sheffield.ac.uk/biosciences/postgraduate/phd",
        "notes": "Postgraduate research programme (Biosciences PhD) in the School of Biosciences at the University of Sheffield."
    },
    {
        "field": "biomed",
        "dept": "School of Biosciences",
        "title": "Biomedical Science PhD",
        "page": "https://sheffield.ac.uk/biosciences/postgraduate/phd",
        "notes": "Postgraduate research programme (Biomedical Science PhD) in the School of Biosciences at the University of Sheffield."
    },
    {
        "field": "earth",
        "dept": "School of Geography and Planning",
        "title": "Geography / Earth Systems PhD",
        "page": "https://sheffield.ac.uk/geography-planning/phd",
        "notes": "Postgraduate research programme (Geography / Earth Systems PhD) in the School of Geography and Planning at the University of Sheffield."
    },
    {
        "field": "environment",
        "dept": "School of Geography and Planning",
        "title": "Environmental Science PhD",
        "page": "https://sheffield.ac.uk/geography-planning/phd",
        "notes": "Postgraduate research programme (Environmental Science PhD) in the School of Geography and Planning at the University of Sheffield."
    },
    {
        "field": "neuro",
        "dept": "School of Psychology",
        "title": "Psychology / Cognitive Neuroscience PhD",
        "page": "https://sheffield.ac.uk/psychology/postgraduate/phd",
        "notes": "Postgraduate research programme (Psychology / Cognitive Neuroscience PhD) in the School of Psychology at the University of Sheffield."
    }
]

for p in programs:
    fid = p["field"]
    if fid in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {p['title']} at Sheffield.",
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
        "id": f"sheffield--{fid}",
        "university": "sheffield",
        "field": fid,
        "also_fields": [],
        "department": p["dept"],
        "program_page": p["page"],
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Students are advised to start in September/October; postgraduate research applications are accepted on a rolling basis throughout the year.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Academic entry requirements vary by academic school; some subjects require a master's degree, while others accept a good undergraduate degree (2:1 or First).",
                "quote": q_entry,
                "url": u_apply
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants wishing to research their own project idea must contact the academic school before submitting a formal application to ensure an appropriately-qualified supervisor is available.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Funding is competitive through university scholarships, research councils, and school or project-specific studentships.",
                "quote": q_fund,
                "url": u_scholarships
            },
            "gre_subject": gre_sub
        },
        "notes": p["notes"]
    }

    dst = STAGE / "programs" / f"sheffield--{fid}.json"
    dst.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Generated and staged {len(programs)} program files for Sheffield.")
