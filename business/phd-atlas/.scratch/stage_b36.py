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

# 1. loyolachicago--cs.json
d = load_prog("loyolachicago--cs.json")
d["fields"]["supervisor"]["value"] = (
    "Admission is decided on the applicant's portfolio rather than a pre-arranged "
    "advisor; new PhD students match with a research advisor after starting the program."
)
d["fields"]["supervisor"]["quote"] = (
    "Admission will be based on strength of applicant, evidenced in a portfolio "
    "comprising an essay in context with Loyola’s values and mission, samples of work "
    "in the field, recommendation letters, and academic performance in prior degree "
    "programs | Typically, new PhD students start their studies serving as teaching "
    "assistants for a few semesters, during which time they take graduate courses and "
    "match with a research advisor."
)
save_prog("loyolachicago--cs.json", d)

# 2. lsu--math.json
d = load_prog("lsu--math.json")
d["fields"]["entry_route"]["quote"] = (
    "A bachelor’s degree from an accredited U.S. institution or the equivalent from a "
    "foreign institution. (Note that an MS is not required for application to the PhD "
    "program in Mathematics.)"
)
save_prog("lsu--math.json", d)

# 3. lund--chemeng.json
d = load_prog("lund--chemeng.json")
d["fields"]["entry_route"]["quote"] = (
    "A person meets the general admission requirements for third-cycle courses and "
    "study programmes if he or she • has been awarded a second-cycle qualification • "
    "has satisfied the requirements for courses comprising at least 240 credits of which "
    "at least 60 credits were awarded in the second cycle | A person meets the specific "
    "admission requirements if he or she has: • a specialised project of at least 30 "
    "second-cycle credits in the subject."
)
save_prog("lund--chemeng.json", d)

# 4. lund--chemistry.json
d = load_prog("lund--chemistry.json")
d["fields"]["entry_route"]["quote"] = (
    "A person meets the general admission requirements for third-cycle courses and "
    "study programmes if he or she: • has been awarded a second-cycle qualification • "
    "has satisfied the requirements for courses comprising at least 240 credits of which "
    "at least 60 credits were awarded in the second cycle | The specific entry requirement "
    "of 120 credits (courses, or a combination of courses and degree project) is defined "
    "by the research orientation of the project."
)
save_prog("lund--chemistry.json", d)

# 5. lund--civil.json
d = load_prog("lund--civil.json")
d["fields"]["entry_route"]["quote"] = (
    "has been awarded a second-cycle qualification | A person meets the specific "
    "admission requirements if he or she has • at least 90 credits in subjects of "
    "relevance to the field including at least 60 second-cycle credits and a second-cycle "
    "degree project of at least 30 credits in the field, or • a second-cycle degree in "
    "a relevant field."
)
save_prog("lund--civil.json", d)

# 6. Append verified non-keyword matches to handoff/audit_reviewed.csv
rev_path = ROOT / "handoff" / "audit_reviewed.csv"
existing = set(rev_path.read_text(encoding="utf-8").splitlines())
new_rows = [
    "off_topic,lund--biomed.json,deadline",
    "off_topic,lund--bme.json,entry_route",
    "off_topic,lund--chemeng.json,entry_route",
    "off_topic,lund--cs.json,entry_route",
    "off_topic,lund--earth.json,entry_route",
    "off_topic,lund--ece.json,entry_route",
]
with rev_path.open("a", encoding="utf-8", newline="\n") as f:
    for row in new_rows:
        if row not in existing:
            f.write(row + "\n")

print("Staged 5 files and updated audit_reviewed.csv")
