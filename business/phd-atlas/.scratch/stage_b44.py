import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

def load_prog(name):
    return json.loads((ROOT / "data" / "programs" / name).read_text(encoding="utf-8"))

def save_prog(name, data):
    (STAGING_PROGS / name).write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

# 1. nmsu--ece.json (entry_route)
d = load_prog("nmsu--ece.json")
d["fields"]["entry_route"] = {
    "code": "Either",
    "value": "Direct entry with a BSEE (no MS) or entry with a completed MS degree.",
    "quote": (
        "Coursework Requirements | Option 1 – Ph.D. with completed MS degree | "
        "Complete undergraduate deficiency coursework , if the student admitted has both "
        "master’s and bachelor’s degrees in fields other than electrical engineering. | "
        "Option 2 – Direct Ph.D. with BSEE or equivalent, but no MS degree"
    ),
    "url": "https://ece.nmsu.edu/grad-study/phd-requirements.html",
}
save_prog("nmsu--ece.json", d)

# 2 & 3. northwestern--biomed.json (gre_general, gre_subject)
d = load_prog("northwestern--biomed.json")
full_gre_quote = (
    "Test Scores | The DGP no longer requires the submission of GRE general or subject tests. "
    "DGP will accept GRE scores if you believe they will help your application. "
    "We would like to stress that submission of scores is truly optional."
)
d["fields"]["gre_general"] = {
    "code": "Optional",
    "value": "The DGP no longer requires GRE scores, and submitting them is optional.",
    "quote": full_gre_quote,
    "url": "https://www.feinberg.northwestern.edu/sites/dgp/prospective-students/admissions-and-application/index.html",
}
d["fields"]["gre_subject"] = {
    "code": "Optional",
    "value": "Subject GRE scores are optional.",
    "quote": full_gre_quote,
    "url": "https://www.feinberg.northwestern.edu/sites/dgp/prospective-students/admissions-and-application/index.html",
}
save_prog("northwestern--biomed.json", d)

# 4. northwestern--civil.json (ielts_min)
d = load_prog("northwestern--civil.json")
d["fields"]["ielts_min"]["quote"] = (
    "5. The IELTS exam: To meet the admission requirement, PhD applicants should score 7 or higher."
)
save_prog("northwestern--civil.json", d)

# 5. northwestern--materials.json (english_waiver)
d = load_prog("northwestern--materials.json")
d["fields"]["english_waiver"]["quote"] = (
    "Applicants who will have earned a Bachelor's or Master's degree from a university where "
    "the language of instruction is English by the quarter of matriculation will receive a TOEFL waiver. "
    "No special action is needed; we will grant the waiver based on the transcripts submitted with the application. "
    "This includes universities in the United States, United Kingdom, Canada, Australia, or New Zealand, "
    "and many (although not all) universities in India, Singapore, and Nigeria."
)
save_prog("northwestern--materials.json", d)

# 6. nyu--math.json (supervisor -> Not stated)
d = load_prog("nyu--math.json")
d["fields"]["supervisor"] = {
    "code": "Not stated",
    "value": "Not stated on the page checked",
    "quote": "",
    "url": d["fields"]["supervisor"]["url"],
}
save_prog("nyu--math.json", d)

# 8, 9, 10. odu--biology.json & odu--environment.json (gre_general -> Not stated)
for name in ("odu--biology.json", "odu--environment.json"):
    d = load_prog(name)
    d["fields"]["gre_general"] = {
        "code": "Not stated",
        "value": "Not stated on the page checked",
        "quote": "",
        "url": d["fields"]["gre_general"]["url"],
    }
    save_prog(name, d)

# 7. Mark verified BS/MS entry_route row for nyu--mech.json
rev_path = ROOT / "handoff" / "audit_reviewed.csv"
existing = set(rev_path.read_text(encoding="utf-8").splitlines())
row = "off_topic,nyu--mech.json,entry_route"
if row not in existing:
    with rev_path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(row + "\n")

print("Staged 7 files and marked 1 reviewed row for Batch 44")
