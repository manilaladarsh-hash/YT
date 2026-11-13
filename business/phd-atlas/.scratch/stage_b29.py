import json
from pathlib import Path

ROOT = Path(r"C:\Users\manil\YT\business\phd-atlas")
STAGING = ROOT / "data" / "staging" / "programs"
PROGS = ROOT / "data" / "programs"
STAGING.mkdir(parents=True, exist_ok=True)

FIT_PREFIX = "Please reference the \u201cProgram Specific Application requirements\u201d table below to verify GRE requirement for each graduate program. | "

for fname in [
    "floridatech--environment.json",
    "floridatech--math.json",
    "floridatech--mech.json",
    "floridatech--physics.json",
]:
    data = json.loads((PROGS / fname).read_text(encoding="utf-8"))
    f = data["fields"]["gre_general"]
    assert f["code"] == "Not required"
    if not f["quote"].startswith(FIT_PREFIX):
        f["quote"] = FIT_PREFIX + f["quote"]
    (STAGING / fname).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# fordham--biology.json
fordham = json.loads((PROGS / "fordham--biology.json").read_text(encoding="utf-8"))
fordham["fields"]["gre_subject"]["quote"] = (
    "Official GRE subject score Recommended not required. Please see the above statement on the GRE scores."
)
(STAGING / "fordham--biology.json").write_text(
    json.dumps(fordham, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

# fsu--biology.json
fsu = json.loads((PROGS / "fsu--biology.json").read_text(encoding="utf-8"))
fsu["fields"]["supervisor"] = {
    "code": "Recommended",
    "value": (
        "Applicants identify faculty of interest in the supplemental application. Reaching out to faculty is "
        "strongly encouraged in Cell & Molecular Biology (which uses three first-year lab rotations), while "
        "Ecology & Evolution requires a faculty sponsor to be admitted and Neuroscience asks applicants to list "
        "at least one contacted potential sponsor."
    ),
    "quote": "Applicants will identify their intended area and faculty members of interest within the Biological Science Supplemental Application under your Application Checklist.",
    "url": "https://www.bio.fsu.edu/grad/",
    "also": [
        {
            "quote": "First-year CMB students typically arrange for and participate in three lab rotations as a prerequisite for final selection of their lab and major professor. Even though prospective students do NOT need a prospective faculty mentor to sponsor their candidacy prior to application, we strongly encouraged you to reach out to faculty members whose research you are interested in as early as possible.",
            "url": "https://www.bio.fsu.edu/grad/cmbgrad/applicationTips.php",
        },
        {
            "quote": "While prospective students do NOT need a faculty sponsor prior to applying, each prospective student MUST have a faculty sponsor who is willing to serve as their formal mentor in order to be admitted.",
            "url": "https://www.bio.fsu.edu/grad/eegrad/appInstructions.php",
        },
        {
            "quote": "On this form you'll specify Neuroscience as your area of interest and list at least one faculty member with whom you have communicated and identified as a potential faculty sponsor.",
            "url": "https://www.bio.fsu.edu/grad/neuro/application.php",
        },
    ],
}
(STAGING / "fsu--biology.json").write_text(
    json.dumps(fsu, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print("Staged 6 files for Batch 29.")
