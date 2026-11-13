import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

(STAGE / "universities").mkdir(parents=True, exist_ok=True)
(STAGE / "programs").mkdir(parents=True, exist_ok=True)

shutil.copy2(DATA / "universities" / "usyd.json", STAGE / "universities" / "usyd.json")

mapping = {
    "bme": (
        "School of Biomedical Engineering",
        "https://www.sydney.edu.au/engineering/schools/school-of-biomedical-engineering.html",
    ),
    "chemeng": (
        "School of Chemical and Biomolecular Engineering",
        "https://www.sydney.edu.au/engineering/schools/school-of-chemical-and-biomolecular-engineering.html",
    ),
    "civil": (
        "School of Civil Engineering",
        "https://www.sydney.edu.au/engineering/schools/school-of-civil-engineering.html",
    ),
    "cs": (
        "School of Computer Science",
        "https://www.sydney.edu.au/engineering/schools/school-of-computer-science.html",
    ),
    "ece": (
        "School of Electrical and Computer Engineering",
        "https://www.sydney.edu.au/engineering/schools/school-of-electrical-and-computer-engineering.html",
    ),
    "mech": (
        "School of Aerospace, Mechanical and Mechatronic Engineering",
        "https://www.sydney.edu.au/engineering/schools/school-of-aerospace-mechanical-and-mechatronic-engineering.html",
    ),
}

for field, (dept, url) in mapping.items():
    src_file = DATA / "programs" / f"usyd--{field}.json"
    rec = json.loads(src_file.read_text(encoding="utf-8"))
    rec["department"] = dept
    rec["program_page"] = url

    out_file = STAGE / "programs" / f"usyd--{field}.json"
    out_file.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"Staged usyd--{field}.json -> {dept} | {url}")

print("Done staging USYD!")
