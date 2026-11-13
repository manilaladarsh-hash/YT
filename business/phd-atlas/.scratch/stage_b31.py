import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
PROGS = ROOT / "data" / "programs"
STAGING = ROOT / "data" / "staging" / "programs"
STAGING.mkdir(parents=True, exist_ok=True)


def load_prog(name):
    return json.loads((PROGS / name).read_text(encoding="utf-8"))


def save_staged(name, data):
    (STAGING / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. hamburg--chemistry.json (supervisor)
hc = load_prog("hamburg--chemistry.json")
hc["fields"]["supervisor"] = {
    "code": "Required",
    "value": "Students in the MIN Faculty must first find a supervisor and identify a research topic; Chemistry requires naming two supervisors, at least one a full or habilitated professor in the department.",
    "quote": "Supervision: Students interested in completing a doctorate in the MIN Faculty will first need to find a supervisor and identify a suitable research topic",
    "url": "https://www.promovieren.uni-hamburg.de/en/min/promotion/voraussetzungen.html",
    "also": [
        {
            "quote": "zwei Betreuer angeben; mindestens einer aus der Gruppe der hauptamtlichen Hochschullehrer und habilitierten Mitglieder des Fachbereichs Chemie sein",
            "url": "https://www.chemie.uni-hamburg.de/studium/promotion/promotion-strukturiert.html",
        }
    ],
}
save_staged("hamburg--chemistry.json", hc)

# 2. hamburg--datasci.json (deadline)
hd = load_prog("hamburg--datasci.json")
hd["fields"]["deadline"]["quote"] = (
    "You can apply for up to two PhD research topics. To this end, you must submit two individual applications, one for each project."
)
save_staged("hamburg--datasci.json", hd)

# 3-8. illinoistech--*.json (gre_general)
iit_updates = {
    "illinoistech--bme.json": "Minimum GRE Scores 1800 (combined), 1200 (quantitative + verbal), 3.0 (analytical writing)",
    "illinoistech--chemeng.json": "Minimum GRE Scores | Ph.D.: 304 (quantitative + verbal), 3.0 (analytical writing)",
    "illinoistech--civil.json": "Minimum GRE Scores | Doctor of Philosophy (Ph.D.): 292 (quantitative + verbal), 2.5 (analytical writing)",
    "illinoistech--ece.json": "Minimum GRE Scores | Ph.D.: 304 (quantitative + verbal), 3.5 (analytical writing)",
    "illinoistech--materials.json": "Minimum GRE Scores 300 (quantitative + verbal), 3.0 (analytical writing)",
    "illinoistech--mech.json": "Minimum GRE Scores 300 (quantitative + verbal), 3.0 (analytical writing)",
}
for fname, quote in iit_updates.items():
    d = load_prog(fname)
    d["fields"]["gre_general"]["quote"] = quote
    save_staged(fname, d)

# 9. imperial--biology.json (funding)
ib = load_prog("imperial--biology.json")
ib["fields"]["funding"]["quote"] = (
    "Unfortunately, international students are not eligible for this call. Funding The studentships will cover UK "
    "tuition fees and will provide an annual tax-free maintenance stipend at the standard UKRI level, currently at "
    "£23,805 (rising annually by an amount linked to inflation), in 12 monthly instalments."
)
save_staged("imperial--biology.json", ib)

# 10. imperial--datasci.json (toefl_min)
ids = load_prog("imperial--datasci.json")
ids["fields"]["toefl_min"]["quote"] = (
    "The College’s postgraduate English language entry requirement page describes the exemptions and acceptable "
    "language tests: our programme requires that students have proficiency at Standard level."
)
save_staged("imperial--datasci.json", ids)

print("Staged 10 files for Batch 31.")
