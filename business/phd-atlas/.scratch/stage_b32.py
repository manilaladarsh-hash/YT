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


# 1. imperial--ece.json (funding)
ie = load_prog("imperial--ece.json")
ie["fields"]["funding"]["quote"] = (
    "Our Awards Panel meets four times a year to consider funding nominations for PhD applicants. "
    "Candidates are nominated by their potential PhD supervisor only after receiving an offer of a PhD place. | "
    "Previous successful applicants have obtained 1st class equivalent degrees at Master's level"
)
save_staged("imperial--ece.json", ie)

# 2. imperial--materials.json (supervisor)
im = load_prog("imperial--materials.json")
im["fields"]["supervisor"]["quote"] = (
    "Find a Prospective Supervisor and submit a formal application: Regardless of your funding needs, "
    "you must identify and secure the interest of a department academic whose research aligns with your background."
)
save_staged("imperial--materials.json", im)

# 3. imperial--physics.json (fee_waiver)
ip = load_prog("imperial--physics.json")
ip["fields"]["fee_waiver"]["quote"] = (
    "Postgraduate courses without an application fee You do not need to pay an application fee for: | "
    "Postgraduate Doctoral degrees (e.g. PhD, EngD)"
)
save_staged("imperial--physics.json", ip)

# 4. imprs-cpqm--physics.json (supervisor)
ic = load_prog("imprs-cpqm--physics.json")
ic["fields"]["supervisor"]["quote"] = (
    "Please use our online form to submit your application. Applications received by email will not be taken into consideration. "
    "Also, please do not send your application to individual PIs."
)
save_staged("imprs-cpqm--physics.json", ic)

# 5. iub--cs.json (english_waiver)
iuc = load_prog("iub--cs.json")
iuc["fields"]["english_waiver"]["quote"] = (
    "Only non-native English speakers who earned an undergraduate degree in the US and are applying to a master’s program "
    "are exempt from submitting an English proficiency test score. Otherwise, all non-native English speakers must provide "
    "an English proficiency test score to complete their application. This includes ALL PhD applicants, regardless of location "
    "of their previous education."
)
save_staged("iub--cs.json", iuc)

# 6. iub--physics.json (entry_route)
iup = load_prog("iub--physics.json")
iup["fields"]["entry_route"]["quote"] = (
    "Your transcripts must show: Graduation from a recognized four-year college, university, or institute of technology."
)
save_staged("iub--physics.json", iup)

# 7. kcl--bme.json (deadline)
kcl = load_prog("kcl--bme.json")
kcl["fields"]["deadline"]["quote"] = (
    "Please note application instructions for individual programmes prior to applying: | "
    "We recruit excellent students for a wide range of studentships. Applications are invited for a range of "
    "individually funded PhD studentships offered by our interdisciplinary research groups and centres"
)
save_staged("kcl--bme.json", kcl)

# 8. kent--biomed.json (fee_waiver)
kb = load_prog("kent--biomed.json")
kb["fields"]["fee_waiver"]["also"] = [
    {
        "quote": "No, we do not grant fee waivers.",
        "url": "https://www.kent.edu/admissions/graduate-degree-student-requirements",
    }
]
save_staged("kent--biomed.json", kb)

print("Staged 8 files for Batch 32.")
