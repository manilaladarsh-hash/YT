import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

ncl_deadline_quote = (
    "Closing Dates | There is no application closing date for this course, "
    "but specific deadlines for funding may apply."
)

updates = {
    "newcastle--cs.json": {
        "code": "Either",
        "value": (
            "A 2:1 honours degree and/or a merit master's degree (or international "
            "equivalent) in computer science or a related discipline."
        ),
        "quote": (
            "Typical entry requirements | A 2:1 Honours degree and/or a Master's degree at Merit level | "
            "Academic entry requirements | A 2:1 honours degree and/or a merit master's degree, "
            "or international equivalent, in computer science or a related discipline."
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8050f-23/",
    },
    "newcastle--earth.json": {
        "code": "Direct from bachelor's",
        "value": (
            "A 2:1 honours degree (or international equivalent) in an appropriate "
            "area relevant to the proposed topic of research."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | "
            "Academic entry requirements | A 2:1 honours degree, or international equivalent, "
            "in an appropriate area relevant to the proposed topic of research. "
            "Appropriate experience is desirable but not essential."
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8314f/",
    },
    "newcastle--ece.json": {
        "code": "Either",
        "value": (
            "A 2:1 honours degree (or international equivalent) in a relevant subject; "
            "combinations of undergraduate, master's, and relevant work experience are considered."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | "
            "Academic entry requirements | A 2:1 Honours degree, or international equivalent, "
            "in a relevant subject. However, combinations of the following can be taken into "
            "consideration: undergraduate qualifications masters qualifications relevant work experience"
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8060f-24/",
    },
    "newcastle--environment.json": {
        "code": "Either",
        "value": (
            "A 2:1 honours degree or master's degree in a related subject, "
            "or international equivalent."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree or a Master's degree | "
            "Academic entry requirements | A 2:1 honours degree or master's degree in a "
            "related subject, or international equivalent."
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8020f-2/",
    },
    "newcastle--materials.json": {
        "code": "Either",
        "value": (
            "A 2:1 honours degree (or international equivalent) in a relevant subject; "
            "combinations of undergraduate, master's, and relevant work experience are considered."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | "
            "Academic entry requirements | A 2:1 Honours degree, or international equivalent, "
            "in a relevant subject. However, combinations of the following can be taken into "
            "consideration: undergraduate qualifications masters qualifications relevant work experience"
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8030f-11/",
    },
    "newcastle--math.json": {
        "code": "Direct from bachelor's",
        "value": (
            "A 2:1 honours degree (or international equivalent) in computing science, "
            "mathematics, physics, statistics, or another strongly quantitative discipline; "
            "MMath/MMathStat and MPhys degrees are also accepted."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | "
            "Academic entry requirements | A 2:1 honours degree, or international equivalent in: "
            "computing science mathematics physics statistics another strongly quantitative discipline "
            "We also accept MMath/MMathStat and MPhys degrees."
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8080f-30/",
    },
    "newcastle--mech.json": {
        "code": "Either",
        "value": (
            "A 2:1 honours degree (or international equivalent) in a relevant subject; "
            "combinations of undergraduate, master's, and relevant work experience are considered."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | "
            "Academic entry requirements | A 2:1 Honours degree, or international equivalent, "
            "in a relevant subject. However, combinations of the following can be taken into "
            "consideration: undergraduate qualifications masters qualifications relevant work experience"
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8090f-32/",
    },
    "newcastle--neuro.json": {
        "code": "Either",
        "value": (
            "A 2:1 honours degree (or international equivalent); further research "
            "experience or a master's degree is preferred/advantageous."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree and preferably a Master's degree | "
            "PhD | A 2:1 honours degree, or international equivalent. Further research "
            "experience or a Master’s degree would be advantageous."
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8300f-75/",
    },
    "newcastle--physics.json": {
        "code": "Direct from bachelor's",
        "value": (
            "A 2:1 honours degree (or international equivalent) in physics, mathematics, "
            "electrical or electronic engineering, or a related subject."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | Academic entry requirements | "
            "A 2:1 honours degree, or international equivalent, in: physics mathematics "
            "electrical or electronic engineering a related subject such as mechanical "
            "engineering or computer science"
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8821f/",
    },
    "newcastle--statistics.json": {
        "code": "Direct from bachelor's",
        "value": (
            "A 2:1 honours degree (or international equivalent) in computing science, "
            "mathematics, physics, statistics, or another strongly quantitative discipline; "
            "MMath/MMathStat and MPhys degrees are also accepted."
        ),
        "quote": (
            "Typical entry requirements | 2:1 Honours degree | "
            "Academic entry requirements | A 2:1 honours degree, or international equivalent in: "
            "computing science mathematics physics statistics another strongly quantitative discipline "
            "We also accept MMath/MMathStat and MPhys degrees."
        ),
        "url": "https://www.ncl.ac.uk/postgraduate/degrees/8080f-29/",
    },
}

for name, entry in updates.items():
    d = json.loads((ROOT / "data" / "programs" / name).read_text(encoding="utf-8"))
    d["fields"]["deadline"]["quote"] = ncl_deadline_quote
    d["fields"]["entry_route"] = entry
    (STAGING_PROGS / name).write_text(
        json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

print(f"Staged {len(updates)} files for Batch 43")
