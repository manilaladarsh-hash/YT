import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "univie.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"
uni_data["fields"]["gre_general"]["url"] = "https://doktorat.univie.ac.at/en/"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "univie.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Program records mapping
prog_urls = {
    "cs": "https://docs.univie.ac.at/",
    "chemistry": "https://doschem.univie.ac.at/",
    "biology": "https://vds-ecology-evolution.univie.ac.at/",
    "environment": "https://careers.univie.ac.at/en/praedoc/stem-call/microbiology-and-environmental-sciences",
    "math": "https://www.vsmath.at/",
    "physics": "https://careers.univie.ac.at/en/praedoc/stem-call/physics",
    "neuro": "https://vds-cobene.univie.ac.at/",
    "earth": "https://doktorat.univie.ac.at/en/vienna-doctoral-schools",
    "astronomy": "https://careers.univie.ac.at/en/praedoc/stem-call"
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, url in prog_urls.items():
    p_path = ROOT / "data" / "programs" / f"univie--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = url
    p_data["checked"] = "2026-10-31"
    
    # Check if gre_subject url was generic
    if "gre_subject" in p_data["fields"]:
        if p_data["fields"]["gre_subject"].get("code") == "Not stated":
            p_data["fields"]["gre_subject"]["url"] = url
            
    out_path = staged_prog_dir / f"univie--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged univie--{field}.json -> {url}")

print("Staging complete.")
