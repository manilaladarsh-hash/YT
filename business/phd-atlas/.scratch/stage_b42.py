import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

def load_prog(name):
    return json.loads((ROOT / "data" / "programs" / name).read_text(encoding="utf-8"))

def save_prog(name, data):
    target = STAGING_PROGS / name
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if target.exists():
        with open(target, "r+", encoding="utf-8", newline="\n") as f:
            f.seek(0)
            f.write(text)
            f.truncate()
    else:
        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)

# 1. ncsu--earth.json (gre_general: expand with section heading)
d = load_prog("ncsu--earth.json")
d["fields"]["gre_general"]["quote"] = (
    "Applicant Information | Delivery Method: On-Campus | Entrance Exam: None"
)
save_prog("ncsu--earth.json", d)

# 2. ncsu--materials.json (gre_general: expand with section heading)
d = load_prog("ncsu--materials.json")
d["fields"]["gre_general"]["quote"] = (
    "Applicant Information | Delivery Method: On-Campus, Online, Hybrid | Entrance Exam: None"
)
save_prog("ncsu--materials.json", d)

ncl_deadline_quote = (
    "Closing Dates | There is no application closing date for this course, "
    "but specific deadlines for funding may apply."
)

# 3. newcastle--astronomy.json
d = load_prog("newcastle--astronomy.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
d["fields"]["entry_route"] = {
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
}
save_prog("newcastle--astronomy.json", d)

# 4. newcastle--biology.json
d = load_prog("newcastle--biology.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
d["fields"]["entry_route"] = {
    "code": "Either",
    "value": "A 2:1 honours degree or master's degree in a related subject, or international equivalent.",
    "quote": (
        "Typical entry requirements | 2:1 Honours degree or a Master's degree | "
        "Academic entry requirements | A 2:1 honours degree or master's degree in a "
        "related subject, or international equivalent."
    ),
    "url": "https://www.ncl.ac.uk/postgraduate/degrees/8020f-10/",
}
save_prog("newcastle--biology.json", d)

# 5. newcastle--biomed.json
d = load_prog("newcastle--biomed.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
d["fields"]["entry_route"] = {
    "code": "Either",
    "value": (
        "A 2:1 honours degree (or international equivalent); further research "
        "experience or a master's degree is preferred/advantageous."
    ),
    "quote": (
        "Typical entry requirements | 2:1 Honours degree and preferably a Master's degree | "
        "PhD | A 2:1 honours degree, or international equivalent. Further research "
        "experience or a master’s degree would be advantageous."
    ),
    "url": "https://www.ncl.ac.uk/postgraduate/degrees/8300f-74/",
}
save_prog("newcastle--biomed.json", d)

# 6. newcastle--chemeng.json
d = load_prog("newcastle--chemeng.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
d["fields"]["entry_route"] = {
    "code": "Either",
    "value": (
        "A 2:1 honours degree (or international equivalent) and preferably a master's "
        "degree; combinations of undergraduate, master's, and relevant work experience "
        "are considered."
    ),
    "quote": (
        "Typical entry requirements | 2:1 Honours degree and preferably a Master's degree | "
        "Academic entry requirements | A 2:1 Honours degree, or international equivalent, "
        "in a relevant subject. However, combinations of the following can be taken into "
        "consideration: undergraduate qualifications masters qualifications relevant work experience"
    ),
    "url": "https://www.ncl.ac.uk/postgraduate/degrees/8030f-12/",
}
save_prog("newcastle--chemeng.json", d)

# 7. newcastle--chemistry.json
d = load_prog("newcastle--chemistry.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
d["fields"]["entry_route"] = {
    "code": "Master's usually required",
    "value": (
        "Typical requirement is a 2:1 MChem honours degree (or international equivalent); "
        "BSc holders with additional relevant experience are considered individually."
    ),
    "quote": (
        "Typical entry requirements | 2:1 MChem Honours degree | PhD | A 2:1 MChem, "
        "or international equivalent, in chemistry or a related subject. We will also "
        "consider applicants on an individual basis with BSc qualifications if they have "
        "additional relevant experience."
    ),
    "url": "https://www.ncl.ac.uk/postgraduate/degrees/8100f-34/",
}
save_prog("newcastle--chemistry.json", d)

# 8. newcastle--civil.json
d = load_prog("newcastle--civil.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
d["fields"]["entry_route"] = {
    "code": "Either",
    "value": (
        "A 2:1 honours degree (or international equivalent) in a relevant subject; "
        "combinations of undergraduate, master's, and relevant work experience are considered."
    ),
    "quote": (
        "Typical entry requirements | 2:1 Honours degree | Academic entry requirements | "
        "A 2:1 Honours degree, or international equivalent, in a relevant subject. "
        "However, combinations of the following can be taken into consideration: "
        "undergraduate qualifications masters qualifications relevant work experience"
    ),
    "url": "https://www.ncl.ac.uk/postgraduate/degrees/8040f-17/",
}
save_prog("newcastle--civil.json", d)

# 9. newcastle--physics.json (shares 8821f/ deadline cache)
d = load_prog("newcastle--physics.json")
d["fields"]["deadline"]["quote"] = ncl_deadline_quote
save_prog("newcastle--physics.json", d)

# 10. Mark verified non-keyword Entrance Exam: None rows in handoff/audit_reviewed.csv
rev_path = ROOT / "handoff" / "audit_reviewed.csv"
existing = set(rev_path.read_text(encoding="utf-8").splitlines())
new_rows = [
    "off_topic,ncsu--earth.json,gre_general",
    "absence,ncsu--earth.json,gre_general",
    "off_topic,ncsu--materials.json,gre_general",
    "absence,ncsu--materials.json,gre_general",
]
with rev_path.open("a", encoding="utf-8", newline="\n") as f:
    for row in new_rows:
        if row not in existing:
            f.write(row + "\n")

print("Staged 9 files and updated audit_reviewed.csv for Batch 42")
