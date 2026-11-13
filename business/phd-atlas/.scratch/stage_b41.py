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

# 1-6. mtu--*.json (entry_route)
mtu_quote = (
    "Total Credit Requirements | Degrees | Credits | "
    "MS-PhD (minimum) 30 Credits | BS-PhD (minimum) 60 Credits"
)
for fn in (
    "mtu--ece.json",
    "mtu--materials.json",
    "mtu--math.json",
    "mtu--mech.json",
    "mtu--physics.json",
    "mtu--statistics.json",
):
    d = load_prog(fn)
    d["fields"]["entry_route"]["quote"] = mtu_quote
    save_prog(fn, d)

# 7. ncsu--chemeng.json (gre_general: expand to include PhD heading)
d = load_prog("ncsu--chemeng.json")
d["fields"]["gre_general"]["quote"] = (
    "Chemical Engineering (MR and PhD) | Delivery Method: On-Campus | Entrance Exam: None"
)
save_prog("ncsu--chemeng.json", d)

# 8. ncsu--chemistry.json (fee_waiver: prepend FAQ question + complete sentence)
d = load_prog("ncsu--chemistry.json")
d["fields"]["fee_waiver"]["quote"] = (
    "I am an international student. Can I apply for an application fee waiver? | "
    "Possibly, but that will require a review of your application materials first to see "
    "if you are competitive with the admission criteria of our admitted students."
)
save_prog("ncsu--chemistry.json", d)

# 9. Mark verified non-keyword matches in handoff/audit_reviewed.csv
rev_path = ROOT / "handoff" / "audit_reviewed.csv"
existing = set(rev_path.read_text(encoding="utf-8").splitlines())
new_rows = [
    "off_topic,nau--civil.json,entry_route",
    "off_topic,ncsu--chemeng.json,gre_general",
    "absence,ncsu--chemeng.json,gre_general",
]
with rev_path.open("a", encoding="utf-8", newline="\n") as f:
    for row in new_rows:
        if row not in existing:
            f.write(row + "\n")

print("Staged 8 files and updated audit_reviewed.csv for Batch 41")
