import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 16 programs mapping
PROGRAM_PAGES = {
    "cs": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/computer-science-phd",
        "dept": "School of Computer Science",
        "entry_quote": "2:1 or masters in computer science or another relevant area",
        "entry_val": "Standard doctoral entry requires a 2:1 honours degree or a relevant Master's qualification in computer science or another relevant area.",
        "note": "Postgraduate research programme (Computer Science PhD) in the School of Computer Science at the University of Nottingham."
    },
    "chemistry": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/chemistry-phd",
        "dept": "School of Chemistry",
        "entry_quote": "Degree\n2:1 in an MSci/MChem or equivalent",
        "entry_val": "Standard doctoral entry requires a 2:1 in an MSci/MChem or equivalent qualification.",
        "note": "Postgraduate research programme (Chemistry PhD) in the School of Chemistry at the University of Nottingham."
    },
    "math": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/mathematics-phd",
        "dept": "School of Mathematical Sciences",
        "entry_quote": "Degree\n2:1 in mathematics or a closely related subject with substantial mathematical content.",
        "entry_val": "Standard doctoral entry requires a 2:1 honours degree in mathematics or a closely related subject with substantial mathematical content.",
        "note": "Postgraduate research programme (Mathematics PhD) in the School of Mathematical Sciences at the University of Nottingham."
    },
    "statistics": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/mathematics-phd",
        "dept": "School of Mathematical Sciences",
        "entry_quote": "Degree\n2:1 in mathematics or a closely related subject with substantial mathematical content.",
        "entry_val": "Doctoral research in statistics is delivered within the School of Mathematical Sciences; standard entry requires a 2:1 honours degree in mathematics or a closely related subject.",
        "note": "Postgraduate research in Statistics is delivered as part of the Mathematics PhD programme in the School of Mathematical Sciences at the University of Nottingham."
    },
    "physics": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/physics-phd",
        "dept": "School of Physics and Astronomy",
        "entry_quote": "2:1 or a masters in physics, mathematical physics or mathematics",
        "entry_val": "Standard doctoral entry requires a 2:1 honours degree or a master's in physics, mathematical physics or mathematics.",
        "note": "Postgraduate research programme (Physics PhD) in the School of Physics and Astronomy at the University of Nottingham."
    },
    "astronomy": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/physics-phd",
        "dept": "School of Physics and Astronomy",
        "entry_quote": "2:1 or a masters in physics, mathematical physics or mathematics",
        "entry_val": "Doctoral research in astronomy and astrophysics is delivered within the School of Physics and Astronomy; standard entry requires a 2:1 honours degree or a master's.",
        "note": "Postgraduate research in Astronomy is delivered within the School of Physics and Astronomy (Physics PhD) at the University of Nottingham."
    },
    "biology": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/biosciences-phd",
        "dept": "School of Biosciences",
        "entry_quote": "2:1 (or international equivalent) in a relevant subject or 2:2 (or international equivalent) in a relevant subject with a Merit at masters level; other qualifications may also be accepted.",
        "entry_val": "Standard doctoral entry requires a 2:1 honours degree in a relevant subject, or a 2:2 with a Merit at master's level.",
        "note": "Postgraduate research programme (Biosciences PhD) in the School of Biosciences at the University of Nottingham."
    },
    "biomed": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/medicineandhealth",
        "dept": "School of Medicine",
        "entry_quote": "2.1 (or equivalent) degree in a relevant subject and two references including at least one academic reference.",
        "entry_val": "Standard doctoral entry requires a 2:1 honours degree in a relevant subject and two references including at least one academic reference.",
        "note": "Postgraduate research programme (Medicine and Health PhD) in the School of Medicine at the University of Nottingham."
    },
    "neuro": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/neuroscience-neuropathology-phd",
        "dept": "School of Life Sciences / School of Medicine",
        "entry_quote": "British Honours degree at least 2:1 or equivalent.",
        "entry_val": "Standard doctoral entry requires a British Honours degree of at least 2:1 or equivalent.",
        "note": "Postgraduate research programme (Neuroscience and Neuropathology PhD) in the School of Life Sciences and School of Medicine at the University of Nottingham."
    },
    "earth": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/geography-phd",
        "dept": "School of Geography",
        "entry_quote": "Masters (or international equivalent) in a relevant discipline, with an average of 60% or above; applicants with a 2:1 (or international equivalent) or other suitable qualifications and/or at least two years of relevant professional experience also considered",
        "entry_val": "Standard doctoral entry requires a master's degree with merit (60%+), or a 2:1 honours degree with relevant research experience.",
        "note": "Postgraduate research programme (Geography PhD / Earth Sciences) in the School of Geography at the University of Nottingham."
    },
    "chemeng": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/chemical-engineering-phd",
        "dept": "Department of Chemical and Environmental Engineering",
        "entry_quote": "masters at merit level or above in a relevant subject",
        "entry_val": "Standard doctoral entry requires a master's degree at merit level or above in a relevant subject.",
        "note": "Postgraduate research programme (Chemical Engineering PhD) in the Department of Chemical and Environmental Engineering at the University of Nottingham."
    },
    "environment": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/chemical-engineering-phd",
        "dept": "Department of Chemical and Environmental Engineering",
        "entry_quote": "masters at merit level or above in a relevant subject",
        "entry_val": "Doctoral research in environmental engineering is delivered in the Department of Chemical and Environmental Engineering; standard entry requires a master's at merit level.",
        "note": "Postgraduate research in Environmental Engineering is delivered within the Department of Chemical and Environmental Engineering at the University of Nottingham."
    },
    "civil": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/civil-engineering-phd",
        "dept": "Department of Civil Engineering",
        "entry_quote": "masters at merit level or above in a relevant subject",
        "entry_val": "Standard doctoral entry requires a master's degree at merit level or above in a relevant subject.",
        "note": "Postgraduate research programme (Civil Engineering PhD) in the Department of Civil Engineering at the University of Nottingham."
    },
    "mech": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/mechanical-engineering-phd",
        "dept": "Department of Mechanical, Materials and Manufacturing Engineering",
        "entry_quote": "2:1 (or international equivalent) and / or a masters at merit level or above in a relevant subject",
        "entry_val": "Standard doctoral entry requires a 2:1 honours degree and/or a master's at merit level or above in a relevant subject.",
        "note": "Postgraduate research programme (Mechanical Engineering PhD) in the Department of Mechanical, Materials and Manufacturing Engineering at the University of Nottingham.",
        "also_fields": ["bme"]
    },
    "materials": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/materials-engineering-and-materials-design-phd",
        "dept": "Department of Mechanical, Materials and Manufacturing Engineering",
        "entry_quote": "masters at merit level or above in a relevant subject",
        "entry_val": "Standard doctoral entry requires a master's degree at merit level or above in a relevant subject.",
        "note": "Postgraduate research programme (Materials Engineering and Materials Design PhD) in the Department of Mechanical, Materials and Manufacturing Engineering at the University of Nottingham."
    },
    "ece": {
        "url": "https://www.nottingham.ac.uk/pgstudy/course/research/electrical-and-electronic-engineering-phd",
        "dept": "Department of Electrical and Electronic Engineering",
        "entry_quote": "masters at merit level or above in a relevant subject",
        "entry_val": "Standard doctoral entry requires a master's degree at merit level or above in a relevant subject.",
        "note": "Postgraduate research programme (Electrical and Electronic Engineering PhD) in the Department of Electrical and Electronic Engineering at the University of Nottingham."
    }
}

staging_progs = ROOT / "data" / "staging" / "programs"
staging_unis = ROOT / "data" / "staging" / "universities"
staging_removed = ROOT / "data" / "staging" / "_removed"
staging_progs.mkdir(parents=True, exist_ok=True)
staging_unis.mkdir(parents=True, exist_ok=True)
staging_removed.mkdir(parents=True, exist_ok=True)

# Copy university record to staging
shutil.copy(ROOT / "data" / "universities" / "nottingham.json", staging_unis / "nottingham.json")

# Stage 16 programs
for fld, info in PROGRAM_PAGES.items():
    orig_path = ROOT / "data" / "programs" / f"nottingham--{fld}.json"
    data = json.loads(orig_path.read_text(encoding="utf-8"))
    
    data["program_page"] = info["url"]
    data["department"] = info["dept"]
    data["notes"] = info["note"]
    if "also_fields" in info:
        data["also_fields"] = info["also_fields"]
    else:
        data["also_fields"] = []
    
    # Update entry_route to match exact program page quote
    data["fields"]["entry_route"]["quote"] = info["entry_quote"]
    data["fields"]["entry_route"]["value"] = info["entry_val"]
    data["fields"]["entry_route"]["url"] = info["url"]
    
    # Write to staging
    out_file = staging_progs / f"nottingham--{fld}.json"
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {out_file.name}")

# Move nottingham--bme to _removed if present
bme_orig = ROOT / "data" / "programs" / "nottingham--bme.json"
bme_staged = staging_removed / "nottingham--bme.json"
if bme_orig.exists():
    shutil.copy(bme_orig, bme_staged)
    print(f"Copied {bme_orig.name} to {bme_staged}")

