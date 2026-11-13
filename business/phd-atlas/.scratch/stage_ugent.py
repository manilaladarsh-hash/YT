import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "ugent.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "ugent.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_urls = {
    "bme": "https://studiekiezer.ugent.be/2026/doctor-of-biomedical-engineering",
    "chemeng": "https://studiekiezer.ugent.be/2026/doctor-of-chemical-engineering",
    "civil": "https://studiekiezer.ugent.be/2026/doctor-of-civil-engineering",
    "cs": "https://studiekiezer.ugent.be/2026/doctor-of-computer-science-engineering",
    "ece": "https://studiekiezer.ugent.be/2026/doctor-of-electrical-engineering",
    "materials": "https://studiekiezer.ugent.be/2026/doctor-of-materials-engineering",
    "mech": "https://studiekiezer.ugent.be/2026/doctor-of-electromechanical-engineering"
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, url in prog_urls.items():
    p_path = ROOT / "data" / "programs" / f"ugent--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = url
    p_data["checked"] = "2026-10-31"
    
    out_path = staged_prog_dir / f"ugent--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged ugent--{field}.json -> {url}")

print("Staging ugent complete.")
