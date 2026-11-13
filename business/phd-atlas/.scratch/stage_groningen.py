import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "groningen.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "groningen.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_urls = {
    "astronomy": "https://www.rug.nl/research/kapteyn/",
    "biology": "https://www.rug.nl/research/gelifes/",
    "chemistry": "https://www.rug.nl/research/stratingh/",
    "cs": "https://www.rug.nl/research/bernoulli/education/phd-programme",
    "datasci": "https://www.rug.nl/research/bernoulli/groups/machine-learning/",
    "environment": "https://www.rug.nl/research/esrig/",
    "math": "https://www.rug.nl/research/bernoulli/groups/cmnm/",
    "physics": "https://www.rug.nl/research/zernike/"
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, url in prog_urls.items():
    p_path = ROOT / "data" / "programs" / f"groningen--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = url
    p_data["checked"] = "2026-10-31"
    
    out_path = staged_prog_dir / f"groningen--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged groningen--{field}.json -> {url}")

print("Staging groningen complete.")
