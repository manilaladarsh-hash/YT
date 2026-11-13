import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
PROGS = ["floridatech--bme.json", "floridatech--chemeng.json", "floridatech--chemistry.json", "floridatech--civil.json", "floridatech--ece.json"]
PREFIX = "Please reference the \u201cProgram Specific Application requirements\u201d table below to verify GRE requirement for each graduate program. | "

staging_dir = ROOT / "data" / "staging"
staging_dir.mkdir(parents=True, exist_ok=True)

for fname in PROGS:
    src = staging_dir / fname
    if not src.exists():
        src = ROOT / "data" / "programs" / fname
    data = json.loads(src.read_text(encoding="utf-8"))
    f = data["fields"]["gre_general"]
    assert f["code"] == "Not required", f"{fname}: unexpected code {f['code']}"
    if not f["quote"].startswith(PREFIX):
        f["quote"] = PREFIX + f["quote"]
    (staging_dir / fname).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {fname}: {f['quote']}")
