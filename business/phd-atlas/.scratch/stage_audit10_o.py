import json
import pathlib

SRC_U = pathlib.Path("data/universities")
SRC_P = pathlib.Path("data/programs")
DST_U = pathlib.Path("data/staging/universities")
DST_P = pathlib.Path("data/staging/programs")
DST_U.mkdir(parents=True, exist_ok=True)
DST_P.mkdir(parents=True, exist_ok=True)


def load_u(name):
    return json.loads((SRC_U / f"{name}.json").read_text(encoding="utf-8"))


def save_u(name, d):
    (DST_U / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_p(name):
    return json.loads((SRC_P / f"{name}.json").read_text(encoding="utf-8"))


def save_p(name, d):
    (DST_P / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 2. vcu: english_waiver
d = load_u("vcu")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "Applicants may be exempted from an English proficiency test if they meet any of the following criteria. | "
    + d["fields"]["english_waiver"]["quote"]
)
save_u("vcu", d)

# 3. warwick: toefl_min
d = load_u("warwick")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "Test of English as a Foreign Language (TOEFL) (iBT) and TOEFL (iBT) Special Home Edition for tests taken on or after 21st January 2026 | Band A | "
    + d["fields"]["toefl_min"]["quote"]
)
save_u("warwick", d)

# 4. washu: english_waiver
d = load_u("washu")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "Exemptions from the English language proficiency test requirement may be granted for individuals who meet one or more of the following criteria: | "
    + d["fields"]["english_waiver"]["quote"]
)
save_u("washu", d)

# 5-7. western: fee_waiver, gre_general -> Not stated
d = load_u("western")
d["checked"] = "2026-11-12"
for k in ("fee_waiver", "gre_general"):
    d["fields"][k]["code"] = "Not stated"
    d["fields"][k]["value"] = "Not stated on the page checked"
    d["fields"][k]["quote"] = ""
save_u("western", d)

# 8. wrightstate: fee_waiver
d = load_u("wrightstate")
d["checked"] = "2026-11-12"
d["fields"]["fee_waiver"]["quote"] = (
    "International Student Application Fee: "
    + d["fields"]["fee_waiver"]["quote"]
)
save_u("wrightstate", d)

# 9. wur: toefl_min
d = load_u("wur")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = (
    "TOEFL iBT (TOEFL Home Edition and MyBest scores are not accepted) | "
    + d["fields"]["toefl_min"]["quote"]
)
save_u("wur", d)

# 10. aarhus--chemeng: deadline
d = load_p("aarhus--chemeng")
d["checked"] = "2026-11-12"
d["fields"]["deadline"]["quote"] = (
    "Apply for a PhD position here | "
    + d["fields"]["deadline"]["quote"]
    + " | Application deadline"
)
save_p("aarhus--chemeng", d)

print("Staged 7 files for Batch 15")
