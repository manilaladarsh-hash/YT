import json
import pathlib

SRC = pathlib.Path("data/programs")
DST = pathlib.Path("data/staging/programs")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1. akron--materials: entry_route
d = load("akron--materials")
d["checked"] = "2026-11-12"
d["fields"]["entry_route"]["quote"] = (
    d["fields"]["entry_route"]["quote"]
    + " | There is a university minimum residence time requiring one year, although graduate students starting with a B.S. or B.A. typically spend four years in residence."
)
save("akron--materials", d)

# 2-3. alabamahuntsville--astronomy: gre_general -> Recommended
d = load("alabamahuntsville--astronomy")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Recommended"
d["fields"]["gre_general"]["value"] = "GRE score is not required but strongly encouraged for the Space Science PhD."
d["fields"]["gre_general"]["quote"] = "Space Science | Doctor of Philosophy | GRE score not required but strongly encouraged"
save("alabamahuntsville--astronomy", d)

# 4-5. alabamahuntsville--chemistry: gre_general -> Not required with GRE header + row
d = load("alabamahuntsville--chemistry")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "Here you can view which programs will require a GRE or GMAT test score for graduate admissions consideration. | "
    "Chemistry | Doctor of Philosophy | Not required"
)
save("alabamahuntsville--chemistry", d)

# 6-7. alabamahuntsville--civil: gre_general -> Required
d = load("alabamahuntsville--civil")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Required"
d["fields"]["gre_general"]["value"] = (
    "GRE is required for the Civil Engineering PhD (minimum 300 combined verbal and quantitative and 3.0 analytical writing)."
)
d["fields"]["gre_general"]["quote"] = "Civil Engineering | Doctor of Philosophy | GRE score required"
d["fields"]["gre_general"]["also"] = [
    {
        "quote": "All applicants must have a Graduate Record Examination combined score of 300 on the verbal and quantitative and a 3.0 on the analytical, and a grade point average of 3.0 or higher on a 4.0 scale.",
        "url": "https://www.uah.edu/eng/departments/cee/graduate-program/cee-phd-requirements",
    }
]
save("alabamahuntsville--civil", d)

# 8-9. alabamahuntsville--cs: gre_general -> Recommended
d = load("alabamahuntsville--cs")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Recommended"
d["fields"]["gre_general"]["value"] = (
    "GRE is not required but highly recommended for the Computer Science PhD to increase chances of receiving a graduate assistantship."
)
d["fields"]["gre_general"]["quote"] = (
    "Computer Science | Doctor of Philosophy | Not required but highly recommended. "
    "Providing GRE scores will greatly increase student's chance in receiving a graduate assistantship"
)
save("alabamahuntsville--cs", d)

# 10. alabamahuntsville--ece: gre_general -> Not required with GRE header + row
d = load("alabamahuntsville--ece")
d["checked"] = "2026-11-12"
d["notes"] = "Both Electrical Engineering PhD and Computer Engineering PhD state GRE is not required on the test score requirements page."
d["fields"]["gre_general"]["value"] = "GRE is not required for Electrical Engineering PhD or Computer Engineering PhD."
d["fields"]["gre_general"]["quote"] = (
    "Here you can view which programs will require a GRE or GMAT test score for graduate admissions consideration. | "
    "Electrical Engineering | Doctor of Philosophy | Not required"
)
save("alabamahuntsville--ece", d)

print("Staged 6 files for Batch 16")
