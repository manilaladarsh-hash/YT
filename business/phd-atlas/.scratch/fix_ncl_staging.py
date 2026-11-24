import json
import os
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
ncl_deadline_quote = (
    "Closing Dates | There is no application closing date for this course, "
    "but specific deadlines for funding may apply."
)

for name in [
    "newcastle--astronomy.json",
    "newcastle--biology.json",
    "newcastle--biomed.json",
    "newcastle--chemeng.json",
    "newcastle--chemistry.json",
    "newcastle--civil.json",
]:
    target = STAGING_PROGS / name
    d = json.loads(target.read_text(encoding="utf-8"))
    d["fields"]["deadline"]["quote"] = ncl_deadline_quote
    tmp = ROOT / ".scratch" / f"_tmp_{name}"
    tmp.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(str(tmp), str(target))

# newcastle--physics.json from data/programs/newcastle--physics.json
d = json.loads((ROOT / "data" / "programs" / "newcastle--physics.json").read_text(encoding="utf-8"))
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
tmp = ROOT / ".scratch" / "_tmp_newcastle--physics.json"
tmp.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
os.replace(str(tmp), str(STAGING_PROGS / "newcastle--physics.json"))

print("Updated 7 newcastle staging files")
