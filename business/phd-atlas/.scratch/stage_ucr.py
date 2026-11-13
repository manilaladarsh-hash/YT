import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

UCR_PAGES = {
    "cs": {
        "url": "https://www1.cs.ucr.edu/",
        "dept": "Department of Computer Science and Engineering",
        "note": "PhD in Computer Science offered by the Department of Computer Science and Engineering at UC Riverside."
    },
    "ece": {
        "url": "https://www.ece.ucr.edu/",
        "dept": "Department of Electrical and Computer Engineering",
        "note": "PhD in Electrical Engineering offered by the Department of Electrical and Computer Engineering at UC Riverside."
    },
    "mech": {
        "url": "https://me.ucr.edu/",
        "dept": "Department of Mechanical Engineering",
        "note": "PhD in Mechanical Engineering offered by the Department of Mechanical Engineering at UC Riverside."
    },
    "bme": {
        "url": "https://bioeng.ucr.edu/",
        "dept": "Department of Bioengineering",
        "note": "PhD in Bioengineering offered by the Department of Bioengineering at UC Riverside."
    },
    "chemeng": {
        "url": "https://cee.ucr.edu/",
        "dept": "Department of Chemical and Environmental Engineering",
        "note": "PhD in Chemical and Environmental Engineering offered by the Department of Chemical and Environmental Engineering at UC Riverside."
    },
    "chemistry": {
        "url": "https://chem.ucr.edu/",
        "dept": "Department of Chemistry",
        "note": "PhD in Chemistry offered by the Department of Chemistry at UC Riverside."
    },
    "materials": {
        "url": "https://mse.ucr.edu/",
        "dept": "Materials Science and Engineering Program",
        "note": "PhD in Materials Science and Engineering offered by the intercollegiate Materials Science and Engineering Program at UC Riverside."
    },
    "math": {
        "url": "https://mathdept.ucr.edu/",
        "dept": "Department of Mathematics",
        "note": "PhD in Mathematics offered by the Department of Mathematics at UC Riverside."
    },
    "statistics": {
        "url": "https://statistics.ucr.edu/",
        "dept": "Department of Statistics",
        "note": "PhD in Applied Statistics offered by the Department of Statistics at UC Riverside."
    },
    "physics": {
        "url": "https://www.physics.ucr.edu/",
        "dept": "Department of Physics and Astronomy",
        "note": "PhD in Physics offered by the Department of Physics and Astronomy at UC Riverside."
    },
    "astronomy": {
        "url": "https://www.physics.ucr.edu/",
        "dept": "Department of Physics and Astronomy",
        "note": "PhD in Astronomy offered by the Department of Physics and Astronomy at UC Riverside."
    },
    "earth": {
        "url": "https://epsci.ucr.edu/",
        "dept": "Department of Earth and Planetary Sciences",
        "note": "PhD in Earth and Planetary Sciences offered by the Department of Earth and Planetary Sciences at UC Riverside."
    },
    "environment": {
        "url": "https://envisci.ucr.edu/",
        "dept": "Department of Environmental Sciences",
        "note": "PhD in Environmental Sciences offered by the Department of Environmental Sciences at UC Riverside."
    },
    "biology": {
        "url": "https://eeob.ucr.edu/",
        "dept": "Department of Evolution, Ecology, and Organismal Biology",
        "note": "PhD in Evolution, Ecology, and Organismal Biology offered by the Department of Biology / EEOB at UC Riverside."
    },
    "neuro": {
        "url": "https://neuro.ucr.edu/",
        "dept": "Interdepartmental Graduate Program in Neuroscience",
        "note": "PhD in Neuroscience offered by the Interdepartmental Graduate Program in Neuroscience at UC Riverside."
    },
    "biomed": {
        "url": "https://medschool.ucr.edu/",
        "dept": "Division of Biomedical Sciences / School of Medicine",
        "note": "PhD in Biomedical Sciences offered by the Division of Biomedical Sciences in the School of Medicine at UC Riverside."
    }
}

staging_progs = ROOT / "data" / "staging" / "programs"
staging_unis = ROOT / "data" / "staging" / "universities"
staging_progs.mkdir(parents=True, exist_ok=True)
staging_unis.mkdir(parents=True, exist_ok=True)

# Copy university record to staging
shutil.copy(ROOT / "data" / "universities" / "ucr.json", staging_unis / "ucr.json")

# Stage 16 programs
for fld, info in UCR_PAGES.items():
    orig_path = ROOT / "data" / "programs" / f"ucr--{fld}.json"
    data = json.loads(orig_path.read_text(encoding="utf-8"))
    
    data["program_page"] = info["url"]
    data["department"] = info["dept"]
    data["notes"] = info["note"]
    
    # Write to staging
    out_file = staging_progs / f"ucr--{fld}.json"
    out_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {out_file.name}")
