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


# 1 & 2. leeds--physics, leeds--statistics (deadline)
for fname in ["leeds--physics.json", "leeds--statistics.json"]:
    d = load_prog(fname)
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
    save_staged(fname, d)

# 3. lehigh--biology.json (gre_general)
lb = load_prog("lehigh--biology.json")
lb["fields"]["gre_general"]["quote"] = (
    "Is the GRE required for admission? | "
    "For the 2027/2028 application cycle, the history PhD program requires the GRE. It is optional for all other programs."
)
save_staged("lehigh--biology.json", lb)

# 4. lmu--biomed.json (supervisor)
lbm = load_prog("lmu--biomed.json")
lbm["fields"]["supervisor"]["quote"] = (
    "In many programs, you must submit a project proposal developed together with your future 1st TAC member at the time of application. "
    "For the individual Ph.D. Medical Research program, the 1st TAC member must also be a member of the LMU Medical Faculty."
)
lbm["fields"]["supervisor"]["also"] = [
    {
        "quote": "A 3-member committee (TAC) accompanies your project and regularly documents the progress in TAC meetings.",
        "url": "https://www.med.lmu.de/en/doctorate/from-a-to-z-your-guide-to-your-degree/ph.d.-medical-research/",
    }
]
save_staged("lmu--biomed.json", lbm)

# 5. lmu--earth.json (supervisor)
le = load_prog("lmu--earth.json")
le["fields"]["supervisor"] = {
    "code": "Required",
    "value": "The application for admission as a doctoral candidate must include a confirmation of supervision signed by both supervisors.",
    "quote": (
        "Application for admission to doctoral studies (PDF, 289 KB), completed and signed by you, "
        "together with a completed confirmation of supervision (page 2 of the application) and signed by both supervisors"
    ),
    "url": "https://www.geo.lmu.de/en/doctorate-and-habilitation/doctoral-study.html",
}
save_staged("lmu--earth.json", le)

# 6 & 7. lmu--math.json (supervisor & entry_route)
lm = load_prog("lmu--math.json")
lm["fields"]["entry_route"]["quote"] = (
    "Abschlussdokumente (Diplom: Urkunde und Zeugnis; Bachelor und Master: Urkunde, Zeugnis und Transcript) "
    "(Originale oder beglaubigte Kopien) Ggf. Nachweis der bestandenen Promotionseignungsprüfung (Kopie)"
)
save_staged("lmu--math.json", lm)

# 8. lmu--physics.json (supervisor)
lp = load_prog("lmu--physics.json")
lp["fields"]["supervisor"] = {
    "code": "Required",
    "value": "You must contact a supervisor and submit their written Confirmation of Supervision before the faculty accepts your doctoral application.",
    "quote": (
        "Supervisor Search for and contact a university lecturer on your own. | "
        "Confirmation of Supervision (PDF, 82 KB)"
    ),
    "url": "https://www.physik.lmu.de/en/research/doctoral-study-and-habilitation/doctoral-study/",
}
save_staged("lmu--physics.json", lp)

# 9. louisville--math.json (gre_subject)
lom = load_prog("louisville--math.json")
lom["fields"]["gre_subject"]["quote"] = "Recent (within three years) GRE scores (only the general exam is required)"
save_staged("louisville--math.json", lom)

print("Staged 8 files for Batch 35.")
