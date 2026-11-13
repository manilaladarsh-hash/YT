import json
import shutil
from pathlib import Path

ROOT = Path("C:/Users/manil/YT/business/phd-atlas")
STAGING_PROGS = ROOT / "data/staging/programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

# Clean any leftover staging files from earlier cards
for p in STAGING_PROGS.glob("*.json"):
    p.unlink()
staging_unis = ROOT / "data/staging/universities"
if staging_unis.exists():
    for p in staging_unis.glob("*.json"):
        p.unlink()

UPDATES = {
    "miami--bme.json": {
        "department": "Department of Biomedical Engineering",
        "program_page": "https://bulletin.miami.edu/graduate-academic-programs/engineering/biomedical-engineering/biomedical-engineering-phd/",
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "The Department admits students with BS or MS degrees in Biomedical Engineering or related science and engineering fields.",
            "quote": "In general, the Department admits students with BS or MS degrees in Biomedical Engineering or related science and engineering fields, or students with MD degrees with undergraduate degrees in sciences or engineering.",
            "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/biomedical-engineering/biomedical-engineering-phd/",
        },
    },
    "miami--chemeng.json": {
        "department": "Department of Chemical, Environmental, and Materials Engineering",
        "program_page": "https://bulletin.miami.edu/graduate-academic-programs/engineering/chemical-environmental-materials-engineering/chemical-environmental-materials-engineering/",
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "The bulletin lists a Direct B.S. to Ph.D. Pathway requiring at least 72 credits beyond a Bachelor's degree.",
            "quote": "Students in the PhD program are required to complete at least 72 credits beyond a Bachelors degree.",
            "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/chemical-environmental-materials-engineering/chemical-environmental-materials-engineering/",
            "also": [
                {
                    "quote": "Direct B.S. to Ph.D. Pathway - Fall Admission",
                    "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/chemical-environmental-materials-engineering/chemical-environmental-materials-engineering/",
                }
            ],
        },
    },
    "miami--civil.json": {
        "department": "Department of Civil and Architectural Engineering",
        "program_page": "https://bulletin.miami.edu/graduate-academic-programs/engineering/civil-architectural-environmental-engineering/civil-engineering-phd/",
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Students without a prior M.S. degree may enter directly and complete a minimum of 72 graduate-level credits beyond the B.S. degree.",
            "quote": "For students who do not have an earned M.S. (in either civil or architectural engineering, or a closely-related field), a minimum of 72 graduate-level credits (with an average of \"B\" or better and no grade below \"C\") are required beyond the B.S. degree.",
            "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/civil-architectural-environmental-engineering/civil-engineering-phd/",
        },
    },
    "miami--ece.json": {
        "department": "Department of Electrical and Computer Engineering",
        "program_page": "https://bulletin.miami.edu/graduate-academic-programs/engineering/electrical-computer-engineering/electrical-computer-engineering-phd/",
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "The bulletin lists a BS-to-PhD track for students entering with only a B.S. degree in Engineering.",
            "quote": "FOR STUDENTS WITH ONLY A B.S. DEGREE IN ENGINEERING",
            "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/electrical-computer-engineering/electrical-computer-engineering-phd/",
            "also": [
                {
                    "quote": "PhD in Electrical and Computer Engineering (BS-to-PhD)",
                    "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/electrical-computer-engineering/electrical-computer-engineering-phd/",
                }
            ],
        },
    },
    "miami--mech.json": {
        "department": "Department of Mechanical and Aerospace Engineering",
        "program_page": "https://bulletin.miami.edu/graduate-academic-programs/engineering/mechanical-aerospace-engineering/mechanical-engineering-phd/",
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Students may enter with only a B.S. degree in Engineering (as well as with a Master's degree in Engineering).",
            "quote": "Part 2 of the Qualifying Exam is to be taken within 2 years if the student has a Master\u2019s degree in Engineering and 2.5 years if the student has only a B.S. degree in Engineering.",
            "url": "https://bulletin.miami.edu/graduate-academic-programs/engineering/mechanical-aerospace-engineering/mechanical-engineering-phd/",
        },
    },
}

for fname, upd in UPDATES.items():
    src = ROOT / "data/programs" / fname
    dst = STAGING_PROGS / fname
    shutil.copy2(src, dst)
    data = json.loads(dst.read_text(encoding="utf-8"))
    data["department"] = upd["department"]
    data["program_page"] = upd["program_page"]
    data["checked"] = "2026-11-12"
    data["fields"]["entry_route"] = upd["entry_route"]
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {fname}")
