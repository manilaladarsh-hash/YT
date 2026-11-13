import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "umich.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "umich.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_urls = {
    "bme": "https://bme.umich.edu/",
    "chemeng": "https://che.engin.umich.edu/",
    "civil": "https://cee.engin.umich.edu/",
    "ece": "https://ece.engin.umich.edu/",
    "materials": "https://mse.engin.umich.edu/",
    "mech": "https://me.engin.umich.edu/"
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, url in prog_urls.items():
    p_path = ROOT / "data" / "programs" / f"umich--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = url
    p_data["checked"] = "2026-10-31"
    
    # Update Not stated fields to point to department url
    for k in ["supervisor", "funding"]:
        if p_data["fields"].get(k, {}).get("code") == "Not stated":
            p_data["fields"][k]["url"] = url
            
    out_path = staged_prog_dir / f"umich--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged umich--{field}.json -> {url}")

print("Staging umich complete.")
