import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "uga.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "uga.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_updates = {
    "bme": {
        "url": "https://engineering.uga.edu/degree/phd-biomedical-engineering/",
        "dept": "School of Chemical, Materials and Biomedical Engineering"
    },
    "chemeng": {
        "url": "https://engineering.uga.edu/degree/phd-biochemical-engineering/",
        "dept": "School of Chemical, Materials and Biomedical Engineering"
    },
    "civil": {
        "url": "https://engineering.uga.edu/degree/phd-civil-and-environmental-engineering/",
        "dept": "School of Environmental, Civil, Agricultural and Mechanical Engineering"
    },
    "ece": {
        "url": "https://engineering.uga.edu/degree/phd-engineering-electrical-computer-engineering-emphasis/",
        "dept": "School of Electrical and Computer Engineering"
    },
    "environment": {
        "url": "https://engineering.uga.edu/degree/phd-engineering-environment-water-emphasis/",
        "dept": "School of Environmental, Civil, Agricultural and Mechanical Engineering"
    },
    "mech": {
        "url": "https://engineering.uga.edu/degree/phd-mechanical-engineering/",
        "dept": "School of Environmental, Civil, Agricultural and Mechanical Engineering"
    }
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, info in prog_updates.items():
    p_path = ROOT / "data" / "programs" / f"uga--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = info["url"]
    p_data["department"] = info["dept"]
    p_data["checked"] = "2026-10-31"
    
    out_path = staged_prog_dir / f"uga--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged uga--{field}.json -> {info['url']}")

print("Staging uga complete.")
