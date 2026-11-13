import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "adelaide.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "adelaide.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_updates = {
    "biomed": {
        "url": "https://adelaide.edu.au/about/school/pharmacy-and-biomedical-science/our-study-areas/",
        "dept": "School of Pharmacy and Biomedical Science"
    },
    "bme": {
        "url": "https://adelaide.edu.au/about/school/electrical-and-mechanical-engineering/our-study-areas/",
        "dept": "School of Electrical and Mechanical Engineering"
    },
    "chemeng": {
        "url": "https://adelaide.edu.au/about/school/chemical-engineering/our-study-areas/",
        "dept": "School of Chemical Engineering"
    },
    "civil": {
        "url": "https://adelaide.edu.au/about/school/civil-engineering-and-construction-management/our-study-areas/",
        "dept": "School of Civil Engineering and Construction Management"
    },
    "cs": {
        "url": "https://adelaide.edu.au/about/school/computer-science-information-technology/our-study-areas/",
        "dept": "School of Computer Science and Information Technology"
    },
    "ece": {
        "url": "https://adelaide.edu.au/about/school/electrical-and-mechanical-engineering/our-study-areas/",
        "dept": "School of Electrical and Mechanical Engineering"
    },
    "mech": {
        "url": "https://adelaide.edu.au/about/school/electrical-and-mechanical-engineering/our-study-areas/",
        "dept": "School of Electrical and Mechanical Engineering"
    }
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, info in prog_updates.items():
    p_path = ROOT / "data" / "programs" / f"adelaide--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = info["url"]
    p_data["department"] = info["dept"]
    p_data["checked"] = "2026-10-31"
    
    out_path = staged_prog_dir / f"adelaide--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged adelaide--{field}.json -> {info['url']}")

print("Staging adelaide complete.")
