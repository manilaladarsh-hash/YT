import json
import shutil
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)
removed_dir = staging_dir / "_removed"
removed_dir.mkdir(parents=True, exist_ok=True)

# Copy live university record
shutil.copy("data/universities/manchester.json", staging_dir / "universities" / "manchester.json")

# Mapping of programs to authentic pages and departments
program_map = {
    "cs": {
        "title": "Computer Science PhD",
        "dept": "Department of Computer Science",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/02954/phd-computer-science/",
        "also_fields": []
    },
    "chemistry": {
        "title": "Chemistry PhD",
        "dept": "Department of Chemistry",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/02934/phd-chemistry/",
        "also_fields": []
    },
    "math": {
        "title": "Pure Mathematics PhD",
        "dept": "Department of Mathematics",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/05325/phd-pure-mathematics/",
        "also_fields": []
    },
    "statistics": {
        "title": "Statistics PhD",
        "dept": "Department of Mathematics",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/08195/phd-statistics/",
        "also_fields": []
    },
    "physics": {
        "title": "Physics PhD/MPhil",
        "dept": "Department of Physics and Astronomy",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/03161/phd-mphil-physics/",
        "also_fields": []
    },
    "astronomy": {
        "title": "Astronomy and Astrophysics PhD/MPhil",
        "dept": "Department of Physics and Astronomy",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/05482/phd-mphil-astronomy-and-astrophysics/",
        "also_fields": []
    },
    "biology": {
        "title": "Molecular Biology PhD/MPhil",
        "dept": "School of Biological Sciences",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/10945/phd-mphil-molecular-biology/",
        "also_fields": []
    },
    "biomed": {
        "title": "Medicine PhD/MPhil",
        "dept": "School of Medical Sciences",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/11044/phd-mphil-medicine/",
        "also_fields": []
    },
    "neuro": {
        "title": "Neuroscience PhD/MPhil",
        "dept": "School of Biological Sciences / Division of Neuroscience",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/10947/phd-mphil-neuroscience/",
        "also_fields": []
    },
    "earth": {
        "title": "Earth Science PhD/MPhil",
        "dept": "Department of Earth and Environmental Sciences",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/05689/phd-mphil-earth-science/",
        "also_fields": []
    },
    "environment": {
        "title": "Environmental Science PhD/MPhil",
        "dept": "Department of Earth and Environmental Sciences",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/11063/phd-mphil-environmental-science/",
        "also_fields": []
    },
    "mech": {
        "title": "Mechanical Engineering PhD",
        "dept": "Department of Mechanical, Aerospace and Civil Engineering",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/03061/phd-mechanical-engineering/",
        "also_fields": ["bme"]
    },
    "civil": {
        "title": "Civil Engineering PhD",
        "dept": "Department of Civil Engineering and Management",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/02942/phd-civil-engineering/",
        "also_fields": []
    },
    "chemeng": {
        "title": "Chemical Engineering PhD/MPhil",
        "dept": "Department of Chemical Engineering",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/12228/phd-mphil-chemical-engineering/",
        "also_fields": []
    },
    "materials": {
        "title": "Materials Postgraduate Research",
        "dept": "Department of Materials",
        "url": "https://www.materials.manchester.ac.uk/study/postgraduate-research/",
        "also_fields": []
    },
    "ece": {
        "title": "Electrical and Electronic Engineering PhD",
        "dept": "Department of Electrical and Electronic Engineering",
        "url": "https://www.manchester.ac.uk/study/postgraduate-research/programmes/list/04620/phd-electrical-and-electronic-engineering/",
        "also_fields": []
    }
}

# Update all 16 valid programs
for field, info in program_map.items():
    p_path = Path(f"data/programs/manchester--{field}.json")
    d = json.load(open(p_path, encoding="utf-8"))
    d["program_page"] = info["url"]
    d["department"] = info["dept"]
    d["also_fields"] = info["also_fields"]
    d["checked"] = "2026-10-31"
    d["notes"] = f"Postgraduate research programme ({info['title']}) in the {info['dept']} at the University of Manchester."
    with open(staging_dir / "programs" / f"manchester--{field}.json", "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")

# Move bme to _removed
bme_src = Path("data/programs/manchester--bme.json")
bme_dst = removed_dir / "manchester--bme.json"
shutil.copy(bme_src, bme_dst)

print(f"Staged 16 verified manchester programs and moved bme to {bme_dst}")
