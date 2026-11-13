import json
import shutil
from pathlib import Path

ROOT = Path("C:/Users/manil/YT/business/phd-atlas")
STAGING_PROGS = ROOT / "data/staging/programs"
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

for p in STAGING_PROGS.glob("*.json"):
    p.unlink()
staging_unis = ROOT / "data/staging/universities"
if staging_unis.exists():
    for p in staging_unis.glob("*.json"):
        p.unlink()

UPDATES = {
    "oxford--bme.json": {
        "program_page": "https://ibme.ox.ac.uk/training/",
        "supervisor": {
            "code": "Recommended",
            "value": "Applicants are encouraged to contact potential supervisors in their area(s) of interest before applying.",
            "quote": "Applicants are encouraged to contact potential supervisors in their area(s) of interest to identify research projects that are best suited to their skillset and aspirations.",
            "url": "https://ibme.ox.ac.uk/training/",
        },
        "funding": {
            "code": "Competitive",
            "value": "Several scholarships are available to cover post-graduate tuition fees and living expenses; applicants should apply to be considered for them.",
            "quote": "Several scholarships are available to cover post-graduate tuition fees and living expenses.",
            "url": "https://ibme.ox.ac.uk/training/",
        },
        "notes": "DPhil in Engineering Science (Biomedical Engineering) via the Institute of Biomedical Engineering (IBME), University of Oxford.",
    },
    "oxford--civil.json": {
        "program_page": "https://eng.ox.ac.uk/civil/graduate-study",
        "funding": {
            "code": "Competitive",
            "value": "A very limited number of University bursaries are available on a strongly competitive basis, alongside Oxford scholarships.",
            "quote": "The University administers a scheme whereby a very limited number of bursaries are available to support research students. There is very strong competition for these bursaries and you will need an excellent academic record to have a chance of success.",
            "url": "https://eng.ox.ac.uk/civil/graduate-study",
        },
        "notes": "DPhil in Engineering Science (Civil and Offshore Engineering Research Group) at the University of Oxford.",
    },
    "oxford--mech.json": {
        "program_page": "https://oti.eng.ox.ac.uk/the-institute/training/",
        "supervisor": {
            "code": "Recommended",
            "value": "Applicants are encouraged to contact potential supervisors in their area(s) of interest before applying.",
            "quote": "Applicants are encouraged to contact potential supervisors in their area(s) of interest to identify research projects that are best suited to their skillset and aspirations.",
            "url": "https://oti.eng.ox.ac.uk/the-institute/training/",
        },
        "funding": {
            "code": "Competitive",
            "value": "Several scholarships are available to cover post-graduate tuition fees and living expenses; applicants should apply to be considered for them.",
            "quote": "Several scholarships are available to cover post-graduate tuition fees and living expenses.",
            "url": "https://oti.eng.ox.ac.uk/the-institute/training/",
        },
        "notes": "DPhil in Engineering Science (Thermofluids and Aerospace Engineering via the Oxford Thermofluids Institute) at the University of Oxford.",
    },
}

for fname, upd in UPDATES.items():
    src = ROOT / "data/programs" / fname
    dst = STAGING_PROGS / fname
    shutil.copy2(src, dst)
    data = json.loads(dst.read_text(encoding="utf-8"))
    data["program_page"] = upd["program_page"]
    data["checked"] = "2026-11-12"
    if "supervisor" in upd:
        data["fields"]["supervisor"] = upd["supervisor"]
    if "funding" in upd:
        data["fields"]["funding"] = upd["funding"]
    if "notes" in upd:
        data["notes"] = upd["notes"]
    dst.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Staged {fname}")
