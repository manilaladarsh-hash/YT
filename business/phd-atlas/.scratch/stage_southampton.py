import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 15 programs mapping
PROGRAM_PAGES = {
    "cs": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-electronics-and-computer-science",
        "dept": "School of Electronics and Computer Science",
        "title": "Computer Science PhD",
        "note": "Postgraduate research programme (Computer Science PhD) in the School of Electronics and Computer Science at the University of Southampton."
    },
    "ece": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-electronics-and-computer-science",
        "dept": "School of Electronics and Computer Science",
        "title": "Electronic and Electrical Engineering PhD",
        "note": "Postgraduate research programme (Electronic and Electrical Engineering PhD) in the School of Electronics and Computer Science at the University of Southampton."
    },
    "chemistry": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-chemistry-and-chemical-engineering",
        "dept": "School of Chemistry and Chemical Engineering",
        "title": "Chemistry PhD",
        "note": "Postgraduate research programme (Chemistry PhD) in the School of Chemistry and Chemical Engineering at the University of Southampton."
    },
    "chemeng": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-chemistry-and-chemical-engineering",
        "dept": "School of Chemistry and Chemical Engineering",
        "title": "Chemical Engineering PhD",
        "note": "Postgraduate research programme (Chemical Engineering PhD) in the School of Chemistry and Chemical Engineering at the University of Southampton."
    },
    "physics": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-physics-and-astronomy",
        "dept": "School of Physics and Astronomy",
        "title": "Physics PhD",
        "note": "Postgraduate research programme (Physics PhD) in the School of Physics and Astronomy at the University of Southampton."
    },
    "astronomy": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-physics-and-astronomy",
        "dept": "School of Physics and Astronomy",
        "title": "Astronomy PhD",
        "note": "Postgraduate research programme (Astronomy PhD) in the School of Physics and Astronomy at the University of Southampton."
    },
    "biology": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-biological-sciences",
        "dept": "School of Biological Sciences",
        "title": "Biological Sciences PhD",
        "note": "Postgraduate research programme (Biological Sciences PhD) in the School of Biological Sciences at the University of Southampton."
    },
    "neuro": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-biological-sciences",
        "dept": "School of Biological Sciences / Faculty of Medicine",
        "title": "Neuroscience PhD",
        "note": "Postgraduate research programme (Neuroscience PhD) in the School of Biological Sciences and Faculty of Medicine at the University of Southampton."
    },
    "math": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-mathematical-sciences",
        "dept": "School of Mathematical Sciences",
        "title": "Mathematical Sciences PhD",
        "note": "Postgraduate research programme (Mathematical Sciences PhD) in the School of Mathematical Sciences at the University of Southampton."
    },
    "statistics": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-mathematical-sciences",
        "dept": "School of Mathematical Sciences",
        "title": "Statistics PhD",
        "note": "Postgraduate research in Statistics is delivered within the School of Mathematical Sciences at the University of Southampton."
    },
    "mech": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-engineering/department-of-mechanical-engineering",
        "dept": "Department of Mechanical Engineering",
        "title": "Mechanical Engineering PhD",
        "note": "Postgraduate research programme (Mechanical Engineering PhD) in the Department of Mechanical Engineering (School of Engineering) at the University of Southampton. Doctoral research in biomedical engineering and materials is delivered within this department.",
        "also_fields": ["bme", "materials"]
    },
    "civil": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/department-of-civil-maritime-environmental-engineering",
        "dept": "Department of Civil, Maritime and Environmental Engineering",
        "title": "Civil Engineering PhD",
        "note": "Postgraduate research programme (Civil Engineering PhD) in the Department of Civil, Maritime and Environmental Engineering at the University of Southampton."
    },
    "earth": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-ocean-and-earth-science",
        "dept": "School of Ocean and Earth Science",
        "title": "Ocean and Earth Science PhD",
        "note": "Postgraduate research programme (Ocean and Earth Science PhD) in the School of Ocean and Earth Science at the University of Southampton."
    },
    "environment": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/school-of-geography-and-environmental-science",
        "dept": "School of Geography and Environmental Science",
        "title": "Environmental Sciences PhD",
        "note": "Postgraduate research programme (Environmental Sciences PhD) in the School of Geography and Environmental Science at the University of Southampton."
    },
    "biomed": {
        "url": "https://www.southampton.ac.uk/about/faculties-schools-departments/faculty-of-medicine",
        "dept": "Faculty of Medicine",
        "title": "Medical Sciences PhD",
        "note": "Postgraduate research programme (Medical Sciences PhD) in the Faculty of Medicine at the University of Southampton."
    }
}

staging_progs = ROOT / "data" / "staging" / "programs"
staging_unis = ROOT / "data" / "staging" / "universities"
staging_removed = ROOT / "data" / "staging" / "_removed"
staging_progs.mkdir(parents=True, exist_ok=True)
staging_unis.mkdir(parents=True, exist_ok=True)
staging_removed.mkdir(parents=True, exist_ok=True)

# Copy university record to staging
shutil.copy(ROOT / "data" / "universities" / "southampton.json", staging_unis / "southampton.json")

# Stage 15 programs
for fld, info in PROGRAM_PAGES.items():
    orig_path = ROOT / "data" / "programs" / f"southampton--{fld}.json"
    data = json.loads(orig_path.read_text(encoding="utf-8"))
    
    data["program_page"] = info["url"]
    data["department"] = info["dept"]
    data["notes"] = info["note"]
    if "also_fields" in info:
        data["also_fields"] = info["also_fields"]
    else:
        data["also_fields"] = []
    
    # Write to staging
    out_file = staging_progs / f"southampton--{fld}.json"
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {out_file.name}")

# Move southampton--bme and southampton--materials to _removed if present
for rem in ["bme", "materials"]:
    p_orig = ROOT / "data" / "programs" / f"southampton--{rem}.json"
    p_staged = staging_removed / f"southampton--{rem}.json"
    if p_orig.exists():
        shutil.copy(p_orig, p_staged)
        print(f"Copied {p_orig.name} to {p_staged}")
