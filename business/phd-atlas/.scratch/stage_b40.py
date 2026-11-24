import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

def load_prog(name):
    return json.loads((ROOT / "data" / "programs" / name).read_text(encoding="utf-8"))

def save_prog(name, data):
    (STAGING_PROGS / name).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

# 1. msstate--math.json (funding)
d = load_prog("msstate--math.json")
d["fields"]["funding"]["quote"] = (
    "Graduate Teaching Assistantship (GTA): | GTA is available on a COMPETITIVE basis."
)
save_prog("msstate--math.json", d)

# 2. msu--statistics.json (gre_subject)
d = load_prog("msu--statistics.json")
d["fields"]["gre_subject"]["quote"] = (
    "GRE | The GRE test is required for PhD applicants. Sub tests are not required."
)
save_prog("msu--statistics.json", d)

# 3-9. mtu--*.json (entry_route: include Total Credit Requirements / Degrees table header)
mtu_quote = (
    "Total Credit Requirements | Degrees | Credits | "
    "MS-PhD (minimum) 30 Credits | BS-PhD (minimum) 60 Credits"
)
for fn in (
    "mtu--biology.json",
    "mtu--bme.json",
    "mtu--chemeng.json",
    "mtu--chemistry.json",
    "mtu--civil.json",
    "mtu--cs.json",
    "mtu--earth.json",
):
    d = load_prog(fn)
    d["fields"]["entry_route"]["quote"] = mtu_quote
    save_prog(fn, d)

print("Staged 9 files for Batch 40")
