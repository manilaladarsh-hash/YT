import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

(STAGE / "universities").mkdir(parents=True, exist_ok=True)
(STAGE / "programs").mkdir(parents=True, exist_ok=True)

# Copy university record
shutil.copy2(DATA / "universities" / "unsw.json", STAGE / "universities" / "unsw.json")

mapping = {
    "bme": ("School of Biomedical Engineering", "https://www.unsw.edu.au/engineering/study-with-us/study-areas/biomedical-engineering"),
    "chemeng": ("School of Chemical Engineering", "https://www.unsw.edu.au/engineering/study-with-us/study-areas/chemical-engineering"),
    "civil": ("School of Civil and Environmental Engineering", "https://www.unsw.edu.au/engineering/study-with-us/study-areas/water-geotechnical-and-transport"),
    "cs": ("School of Computer Science and Engineering", "https://www.unsw.edu.au/engineering/study-with-us/study-areas/Computer-science-and-software-engineering"),
    "ece": ("School of Electrical Engineering and Telecommunications", "https://www.unsw.edu.au/engineering/study-with-us/study-areas/telecommunications-engineering"),
    "mech": ("School of Mechanical and Manufacturing Engineering", "https://www.unsw.edu.au/engineering/study-with-us/study-areas/mechanical-and-advanced-manufacturing-engineering"),
}

for field, (dept, url) in mapping.items():
    src_file = DATA / "programs" / f"unsw--{field}.json"
    rec = json.loads(src_file.read_text(encoding="utf-8"))
    rec["department"] = dept
    rec["program_page"] = url
    
    out_file = STAGE / "programs" / f"unsw--{field}.json"
    out_file.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"Staged unsw--{field}.json with {url}")

print("Done staging UNSW!")
