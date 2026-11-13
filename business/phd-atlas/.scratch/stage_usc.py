import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. University record
uni_path = ROOT / "data" / "universities" / "usc.json"
uni_data = json.loads(uni_path.read_text(encoding="utf-8"))
uni_data["checked"] = "2026-10-31"

staged_uni_dir = ROOT / "data" / "staging" / "universities"
staged_uni_dir.mkdir(parents=True, exist_ok=True)
(staged_uni_dir / "usc.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. Programs mapping
prog_urls = {
    "bme": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-biomedical-engineering/",
    "chemeng": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-chemical-engineering/",
    "civil": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-civil-engineering/",
    "cs": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-computer-science/",
    "ece": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-electrical-engineering/",
    "materials": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-materials-science/",
    "mech": "https://viterbigradadmission.usc.edu/doctoral/phddegrees/phd-mechanical-engineering/"
}

staged_prog_dir = ROOT / "data" / "staging" / "programs"
staged_prog_dir.mkdir(parents=True, exist_ok=True)

for field, url in prog_urls.items():
    p_path = ROOT / "data" / "programs" / f"usc--{field}.json"
    p_data = json.loads(p_path.read_text(encoding="utf-8"))
    p_data["program_page"] = url
    p_data["checked"] = "2026-10-31"
    
    out_path = staged_prog_dir / f"usc--{field}.json"
    out_path.write_text(json.dumps(p_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged usc--{field}.json -> {url}")

print("Staging usc complete.")
