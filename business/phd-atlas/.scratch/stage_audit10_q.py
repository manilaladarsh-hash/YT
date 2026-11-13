import json
import pathlib

SRC = pathlib.Path("data/programs")
DST = pathlib.Path("data/staging/programs")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 1-2. alabamahuntsville--materials: gre_general
d = load("alabamahuntsville--materials")
d["checked"] = "2026-11-12"
d["notes"] = "Both Materials Science Engineering Track and Science Track list GRE as Not required on the test score requirements page."
d["fields"]["gre_general"]["value"] = "GRE is not required for Materials Science - Engineering Track (nor Science Track)."
d["fields"]["gre_general"]["quote"] = (
    "Here you can view which programs will require a GRE or GMAT test score for graduate admissions consideration. | "
    "Materials Science - Engineering Track | Doctor of Philosophy | Not required"
)
save("alabamahuntsville--materials", d)

# 3-4. alabamahuntsville--mech: gre_general
d = load("alabamahuntsville--mech")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "Here you can view which programs will require a GRE or GMAT test score for graduate admissions consideration. | "
    "Mechanical Engineering | Doctor of Philosophy | Not required"
)
save("alabamahuntsville--mech", d)

# 5-6. alabamahuntsville--physics: gre_general
d = load("alabamahuntsville--physics")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["quote"] = (
    "Here you can view which programs will require a GRE or GMAT test score for graduate admissions consideration. | "
    "Physics | Doctor of Philosophy | Not required"
)
save("alabamahuntsville--physics", d)

# 7. baylor--chemistry: entry_route
d = load("baylor--chemistry")
d["checked"] = "2026-11-12"
d["fields"]["entry_route"]["quote"] = (
    "While we do offer a M.S. degree in Chemistry, all students are recruited directly into our Ph.D. program. "
    "Those that do not complete the Ph.D. program can receive a M.S. if the degree requirements are met."
)
save("baylor--chemistry", d)

# 8. baylor--earth: toefl_min
d = load("baylor--earth")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL, IELTS, and DUOLINGO: International applicants must provide a test score from one of the three tests. | "
    + d["fields"]["toefl_min"]["quote"]
)
save("baylor--earth", d)

# 10. baylor--statistics: supervisor -> Not stated
d = load("baylor--statistics")
d["checked"] = "2026-11-12"
d["fields"]["supervisor"]["code"] = "Not stated"
d["fields"]["supervisor"]["value"] = "Not stated on the page checked"
d["fields"]["supervisor"]["quote"] = ""
save("baylor--statistics", d)

print("Staged 6 files for Batch 17")
