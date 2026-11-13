import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

(STAGE / "universities").mkdir(parents=True, exist_ok=True)
(STAGE / "programs").mkdir(parents=True, exist_ok=True)

shutil.copy2(DATA / "universities" / "washu.json", STAGE / "universities" / "washu.json")

mapping = {
    "bme": (
        "Department of Biomedical Engineering",
        "https://bme.washu.edu/academics/graduate-programs/phd/index.html",
        "Our PhD students are fully funded, including full tuition support and health and dental insurance. As a doctoral candidate, you will also receive a generous stipend to cover living expenses. This support is guaranteed as you continue to make satisfactory progress towards your degree.",
        "PhD students are fully funded with full tuition support, health and dental insurance, and a stipend for living expenses, guaranteed with satisfactory progress.",
    ),
    "chemeng": (
        "Department of Energy, Environmental & Chemical Engineering",
        "https://eece.washu.edu/academics/graduate-programs/PhD-in-Energy-Environmental-Chemical-Engineering.html",
        "Our PhD students are fully funded, including full tuition support and health insurance. As a doctoral candidate, you will also receive a generous stipend to cover living expenses. This support is guaranteed as you continue to make satisfactory progress towards your degree.",
        "PhD students are fully funded with full tuition support, health insurance, and a stipend for living expenses, guaranteed with satisfactory progress.",
    ),
    "cs": (
        "Department of Computer Science & Engineering",
        "https://cse.washu.edu/academics/graduate/PhD-in-Computer-Science-or-Computer-Engineering.html",
        "Our PhD students are fully funded, including full tuition support and health insurance. | As a doctoral candidate, you will also receive a generous stipend to cover living expenses. This support is guaranteed as you continue to make satisfactory progress towards your degree.",
        "PhD students are fully funded with full tuition support, health insurance, and a stipend for living expenses, guaranteed with satisfactory progress.",
    ),
    "ece": (
        "Preston M. Green Department of Electrical & Systems Engineering",
        "https://ese.washu.edu/academics/graduate-programs/doctoral/PhD-in-Electrical-Engineering.html",
        "Our PhD students are fully funded, including full tuition support and health insurance. | As a doctoral candidate, you will also receive a generous stipend to cover living expenses. This support is guaranteed as you continue to make satisfactory progress towards your degree.",
        "PhD students are fully funded with full tuition support, health insurance, and a stipend for living expenses, guaranteed with satisfactory progress.",
    ),
    "materials": (
        "Institute of Materials Science & Engineering",
        "https://imse.washu.edu/graduate-program/index.html",
        "Our PhD students are fully funded, including full tuition support and health insurance. As a doctoral candidate, you will also receive a generous 12-month stipend to cover living expenses.",
        "PhD students are fully funded with full tuition support, health insurance, and a 12-month stipend for living expenses, contingent on satisfactory academic performance and acceptance into a research group.",
    ),
    "mech": (
        "Department of Mechanical Engineering & Materials Science",
        "https://mems.washu.edu/academics/graduate/PhD-in-Mechanical-Engineering.html",
        "Our PhD students are fully funded, including full tuition support and health insurance. As a doctoral candidate, you will also receive a generous stipend to cover living expenses. This support is guaranteed as you continue to make satisfactory progress towards your degree.",
        "PhD students are fully funded with full tuition support, health insurance, and a stipend for living expenses, guaranteed with satisfactory progress.",
    ),
}

for field, (dept, url, funding_quote, funding_val) in mapping.items():
    src_file = DATA / "programs" / f"washu--{field}.json"
    rec = json.loads(src_file.read_text(encoding="utf-8"))
    rec["department"] = dept
    rec["program_page"] = url
    rec["fields"]["funding"] = {
        "code": "Guaranteed",
        "value": funding_val,
        "quote": funding_quote,
        "url": url,
    }
    if rec["fields"]["supervisor"]["code"] == "Not stated" and not rec["fields"]["supervisor"].get("quote"):
        rec["fields"]["supervisor"]["url"] = url

    out_file = STAGE / "programs" / f"washu--{field}.json"
    out_file.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"Staged washu--{field}.json -> {url}")

print("Done staging WashU!")
