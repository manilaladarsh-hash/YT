import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "unimelb.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "unimelb.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_urls = {
    "bme": "https://biomedical.eng.unimelb.edu.au/",
    "chemeng": "https://chemical.eng.unimelb.edu.au/",
    "civil": "https://infrastructure.eng.unimelb.edu.au/",
    "cs": "https://cis.unimelb.edu.au/",
    "ece": "https://electrical.eng.unimelb.edu.au/",
    "mech": "https://mechanical.eng.unimelb.edu.au/"
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, url in prog_urls.items():
    p_path = ROOT / "data" / "programs" / f"unimelb--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = url
    p_data["checked"] = "2026-10-31"
    
    out_path = staged_prog_dir / f"unimelb--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged unimelb--{field}.json -> {url}")

print("Staging unimelb complete.")
