import json
import shutil
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)
removed_dir = staging_dir / "_removed"
removed_dir.mkdir(parents=True, exist_ok=True)

# Copy live university record
shutil.copy("data/universities/liverpool.json", staging_dir / "universities" / "liverpool.json")

# Verified program mapping
program_map = {
    "cs": {
        "title": "Computer Science PhD / MPhil",
        "dept": "Department of Computer Science",
        "url": "https://www.liverpool.ac.uk/courses/computer-science-phd",
        "also_fields": []
    },
    "chemistry": {
        "title": "Chemistry PhD",
        "dept": "Department of Chemistry",
        "url": "https://www.liverpool.ac.uk/courses/chemistry-phd",
        "also_fields": ["chemeng"]
    },
    "math": {
        "title": "Mathematical Sciences PhD",
        "dept": "Department of Mathematical Sciences",
        "url": "https://www.liverpool.ac.uk/courses/mathematical-sciences-phd",
        "also_fields": []
    },
    "statistics": {
        "title": "Biostatistics PhD",
        "dept": "Department of Mathematical Sciences / Institute of Population Health",
        "url": "https://www.liverpool.ac.uk/courses/biostatistics-phd",
        "also_fields": []
    },
    "physics": {
        "title": "Physics PhD",
        "dept": "Department of Physics",
        "url": "https://www.liverpool.ac.uk/courses/physics-phd",
        "also_fields": ["astronomy"]
    },
    "biology": {
        "title": "Biological Sciences PhD",
        "dept": "Institute of Integrative Biology / School of Life Sciences",
        "url": "https://www.liverpool.ac.uk/courses/biological-sciences-phd",
        "also_fields": []
    },
    "biomed": {
        "title": "Clinical Science PhD",
        "dept": "Institute of Systems, Molecular and Integrative Biology",
        "url": "https://www.liverpool.ac.uk/courses/clinical-science-phd",
        "also_fields": []
    },
    "neuro": {
        "title": "Neurological Science PhD",
        "dept": "Institute of Systems, Molecular and Integrative Biology",
        "url": "https://www.liverpool.ac.uk/courses/neurological-science-phd",
        "also_fields": []
    },
    "earth": {
        "title": "Earth Sciences PhD",
        "dept": "Department of Earth, Ocean and Ecological Sciences",
        "url": "https://www.liverpool.ac.uk/courses/earth-sciences-phd",
        "also_fields": []
    },
    "environment": {
        "title": "Environmental Science PhD",
        "dept": "Department of Earth, Ocean and Ecological Sciences",
        "url": "https://www.liverpool.ac.uk/courses/environmental-science-phd",
        "also_fields": []
    },
    "mech": {
        "title": "Mechanical and Aerospace Engineering Research",
        "dept": "Department of Mechanical and Aerospace Engineering",
        "url": "https://www.liverpool.ac.uk/engineering/research/",
        "also_fields": []
    },
    "civil": {
        "title": "Civil and Environmental Engineering Research",
        "dept": "Department of Civil and Environmental Engineering",
        "url": "https://www.liverpool.ac.uk/engineering/research/",
        "also_fields": []
    },
    "ece": {
        "title": "Electrical Engineering and Electronics PhD",
        "dept": "Department of Electrical Engineering and Electronics",
        "url": "https://www.liverpool.ac.uk/courses/electrical-engineering-and-electronics-phd",
        "also_fields": []
    },
    "materials": {
        "title": "Materials, Design and Manufacturing PhD",
        "dept": "Department of Materials, Design and Manufacturing Engineering",
        "url": "https://www.liverpool.ac.uk/courses/materials-design-and-manufacturing-phd",
        "also_fields": []
    },
    "bme": {
        "title": "Bioengineering PhD",
        "dept": "School of Engineering / Bioengineering",
        "url": "https://www.liverpool.ac.uk/courses/bioengineering-phd",
        "also_fields": []
    }
}

u_degrees = "https://www.liverpool.ac.uk/study/postgraduate-research/degrees/"

for field, info in program_map.items():
    p_path = Path(f"data/programs/liverpool--{field}.json")
    d = json.load(open(p_path, encoding="utf-8"))
    d["program_page"] = info["url"]
    d["department"] = info["dept"]
    d["also_fields"] = info["also_fields"]
    d["checked"] = "2026-10-31"
    d["notes"] = f"Postgraduate research programme ({info['title']}) in the {info['dept']} at the University of Liverpool."

    # Update deadline quote from course page or degrees directory
    if info["url"].startswith("https://www.liverpool.ac.uk/courses/"):
        d["fields"]["deadline"] = {
            "code": "Rolling",
            "value": "Doctoral applications are accepted year round on a rolling basis.",
            "quote": "Apply by\nYear round\nStart date\nYear round",
            "url": info["url"]
        }
    else:
        d["fields"]["deadline"] = {
            "code": "Rolling",
            "value": "Doctoral applications are accepted year round on a rolling basis.",
            "quote": "Apply by:\nYear round",
            "url": u_degrees
        }

    with open(staging_dir / "programs" / f"liverpool--{field}.json", "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")

# Move unverified standalone programs to _removed
for rem_field in ["chemeng", "astronomy"]:
    src = Path(f"data/programs/liverpool--{rem_field}.json")
    dst = removed_dir / f"liverpool--{rem_field}.json"
    shutil.copy(src, dst)
    print(f"Moved liverpool--{rem_field} to {dst}")

print(f"Staged {len(program_map)} verified liverpool programs.")
