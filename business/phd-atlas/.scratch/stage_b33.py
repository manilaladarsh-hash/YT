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


# 1. kent--math.json (funding)
km = load_prog("kent--math.json")
km["fields"]["funding"]["quote"] = (
    "Mathematics Graduate Assistantship Available to both doctoral and master's students, "
    "and is normally the first appointment a new student will receive."
)
save_staged("kent--math.json", km)

# 2. kit--mech.json (supervisor)
kit = load_prog("kit--mech.json")
kit["fields"]["supervisor"]["quote"] = (
    "Acceptance as a doctoral candidate requires that you have found a scientific supervisor at KIT. | "
    "Application for acceptance as a doctoral candidate required: Doctoral agreement and registration with KHYS"
)
save_staged("kit--mech.json", kit)

# 3. ksu--civil.json (gre_general)
ksuc = load_prog("ksu--civil.json")
ksuc["fields"]["gre_general"]["quote"] = (
    "The score obtained in the Graduate Record Examination (GRE) should be reported officially to "
    "Kansas State University Civil Engineering Department. K-State CE’s minimum requirement for admission "
    "is 80th percentile rank on quantitative portion of the exam."
)
save_staged("ksu--civil.json", ksuc)

# 4. ku--cs.json (supervisor)
kucs = load_prog("ku--cs.json")
kucs["fields"]["supervisor"]["quote"] = (
    "Computer Science Ph.D. students are encouraged to choose a research cluster and dissertation topic "
    "as early in the graduate program as possible and identify a faculty adviser who is interested in supervising their work."
)
save_staged("ku--cs.json", kucs)

# 5. ku--ece.json (supervisor)
kuece = load_prog("ku--ece.json")
kuece["fields"]["supervisor"]["quote"] = (
    "Electrical Engineering students are encouraged to choose a reserach cluster and dissertation topic "
    "as early in the graduate program as possible and identify a faculty adviser who is interested in supervising their work."
)
save_staged("ku--ece.json", kuece)

# 6. ku--statistics.json (funding)
kust = load_prog("ku--statistics.json")
kust["fields"]["funding"]["quote"] = (
    "Graduate research assistantships and graduate teaching assistantships are available through the "
    "Department of Biostatistics & Data Science. GRA and GTA slots are limited and highly competitive."
)
save_staged("ku--statistics.json", kust)

# 7-9. leeds--astronomy, leeds--biology, leeds--biomed (deadline)
for fname in ["leeds--astronomy.json", "leeds--biology.json", "leeds--biomed.json"]:
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

print("Staged 9 files for Batch 33.")
