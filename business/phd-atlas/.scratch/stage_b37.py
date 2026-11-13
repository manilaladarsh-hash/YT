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

# 1. lund--mech.json (expand 4.1 + 4.2 to include "second-cycle degree in a relevant field")
d = load_prog("lund--mech.json")
d["fields"]["entry_route"]["quote"] = (
    "been awarded a second-cycle qualification | A person meets the specific "
    "admission requirements if they have: • at least 90 credits of relevance to the "
    "field, including at least 60 second-cycle credits, or • a second-cycle degree in "
    "a relevant field."
)
save_prog("lund--mech.json", d)

# 2. maryland--physics.json (swap primary score table and Physics full-enrollment refusal in also)
d = load_prog("maryland--physics.json")
umd_physics_url = "https://umdphysics.umd.edu/academics/graduate/grad-faq.html"
umd_grad_url = "https://gradschool.umd.edu/admissions/english-language-proficiency-requirements"
phys_also_quote = (
    "If you fall below the minimum requirements for \"full enrollment\", "
    "unfortunately your application will not be considered. | The scores for "
    "\"full enrollment\" is set by the Graduate School and not the Physics Department."
)

d["fields"]["toefl_min"]["quote"] = d["fields"]["toefl_min"]["also"][0]["quote"]
d["fields"]["toefl_min"]["url"] = umd_grad_url
d["fields"]["toefl_min"]["also"] = [{"quote": phys_also_quote, "url": umd_physics_url}]

d["fields"]["ielts_min"]["quote"] = d["fields"]["ielts_min"]["also"][0]["quote"]
d["fields"]["ielts_min"]["url"] = umd_grad_url
d["fields"]["ielts_min"]["also"] = [{"quote": phys_also_quote, "url": umd_physics_url}]
save_prog("maryland--physics.json", d)

# 3. mcmaster--biology.json (prepend FAQ question for gre_general)
d = load_prog("mcmaster--biology.json")
d["fields"]["gre_general"]["quote"] = (
    "Is the GRE (Graduate Record Exam) required? | At present, it is not a "
    "departmental regulation. If available, this can be submitted on-line to be "
    "attached to your application."
)
save_prog("mcmaster--biology.json", d)

# 4. Append verified non-keyword matches to handoff/audit_reviewed.csv
rev_path = ROOT / "handoff" / "audit_reviewed.csv"
existing = set(rev_path.read_text(encoding="utf-8").splitlines())
new_rows = [
    "off_topic,lund--materials.json,entry_route",
    "off_topic,lund--math.json,entry_route",
    "off_topic,lund--physics.json,entry_route",
    "off_topic,marquette--chemistry.json,entry_route",
    "off_topic,mcmaster--chemistry.json,entry_route",
]
with rev_path.open("a", encoding="utf-8", newline="\n") as f:
    for row in new_rows:
        if row not in existing:
            f.write(row + "\n")

print("Staged 3 files and updated audit_reviewed.csv for Batch 37")
