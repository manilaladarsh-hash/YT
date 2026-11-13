import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
PROGS = ROOT / "data" / "programs"
STAGING = ROOT / "data" / "staging" / "programs"
STAGING.mkdir(parents=True, exist_ok=True)

FILES = [
    "leeds--chemeng.json",
    "leeds--chemistry.json",
    "leeds--civil.json",
    "leeds--cs.json",
    "leeds--earth.json",
    "leeds--ece.json",
    "leeds--environment.json",
    "leeds--math.json",
    "leeds--mech.json",
    "leeds--neuro.json",
]

for fname in FILES:
    d = json.loads((PROGS / fname).read_text(encoding="utf-8"))
    d["fields"]["deadline"]["quote"] = (
        "Deadlines We advise you to apply at least four months before your proposed start date. "
        "This is to allow sufficient time to review your application and undertake any additional checks."
    )
    d["fields"]["deadline"]["also"] = [
        {
            "quote": "Our entry points are 1 September, 1 October, 1 February and 1 April, though some areas may offer only one or two start dates per year.",
            "url": "https://www.leeds.ac.uk/research-applying/doc/start-dates-application-deadlines",
        }
    ]
    (STAGING / fname).write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Staged {len(FILES)} files for Batch 34.")
