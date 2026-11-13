import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
STAGE = ROOT / "data" / "staging"

(STAGE / "universities").mkdir(parents=True, exist_ok=True)
(STAGE / "programs").mkdir(parents=True, exist_ok=True)

shutil.copy2(DATA / "universities" / "gwu.json", STAGE / "universities" / "gwu.json")

mapping = {
    "bme": (
        "Department of Biomedical Engineering",
        "https://graduate.engineering.gwu.edu/phd-biomedical-engineering",
        "Bachelor's or master's degree in a relevant field from an accredited institution. | For bachelor's-only applicants, a minimum of a 3.4 GPA (out of a 4.0 scale) must have been achieved.",
        "Direct-entry PhD with a bachelor's degree (minimum 3.4 GPA) or a master's degree in a relevant field.",
    ),
    "civil": (
        "Department of Civil and Environmental Engineering",
        "https://graduate.engineering.gwu.edu/phd-civil-and-environmental-engineering",
        "Bachelor's or master's degree in a relevant field from an accredited institution. | If the applicant has only obtained a bachelor’s degree, the minimum grade point average must be a 3.3 (on a scale of 4.0).",
        "Direct-entry PhD with a bachelor's degree (minimum 3.3 GPA) or a master's degree (minimum 3.4 GPA) in a relevant field.",
    ),
    "cs": (
        "Department of Computer Science",
        "https://graduate.engineering.gwu.edu/phd-computer-science",
        "Bachelor’s or master’s degree in a relevant area from an accredited institution. | If applicant has only obtained a bachelor’s degree, the minimum grade point average must be a 3.3 (on a scale of 4.0).",
        "Direct-entry PhD with a bachelor's degree (minimum 3.3 GPA) or a master's degree (minimum 3.5 GPA) in a relevant area.",
    ),
    "ece": (
        "Department of Electrical and Computer Engineering",
        "https://graduate.engineering.gwu.edu/phd-electrical-engineering",
        "Bachelor’s or master’s degree in an appropriate area from an accredited institution. | If applicant has only obtained a bachelor’s, the minimum grade point average must be a 3.3 (on a scale of 4.0).",
        "Direct-entry PhD with a bachelor's degree (minimum 3.3 GPA) or a master's degree (minimum 3.4 GPA) in an appropriate area.",
    ),
    "mech": (
        "Department of Mechanical and Aerospace Engineering",
        "https://graduate.engineering.gwu.edu/phd-mechanical-and-aerospace-engineering",
        "Bachelor’s or master’s degree in an appropriate area from an accredited institution. | If applicant has only obtained a bachelor’s degree, the minimum grade point average must be a 3.3 (on a scale of 4.0).",
        "Direct-entry PhD with a bachelor's degree (minimum 3.3 GPA) or a master's degree (minimum 3.4 GPA) in an appropriate area.",
    ),
}

for field, (dept, url, entry_quote, entry_val) in mapping.items():
    src_file = DATA / "programs" / f"gwu--{field}.json"
    rec = json.loads(src_file.read_text(encoding="utf-8"))
    rec["department"] = dept
    rec["program_page"] = url
    rec["fields"]["entry_route"] = {
        "code": "Direct from bachelor's",
        "value": entry_val,
        "quote": entry_quote,
        "url": url,
    }
    rec["notes"] = "SEAS doctoral program page checked; school-wide SEAS deadline, GRE, English, supervisor, and funding rules apply."

    out_file = STAGE / "programs" / f"gwu--{field}.json"
    out_file.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"Staged gwu--{field}.json -> {url}")

print("Done staging GWU!")
