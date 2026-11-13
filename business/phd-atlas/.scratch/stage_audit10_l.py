import json
import pathlib

SRC = pathlib.Path("data/universities")
DST = pathlib.Path("data/staging/universities")
DST.mkdir(parents=True, exist_ok=True)


def load(name):
    return json.loads((SRC / f"{name}.json").read_text(encoding="utf-8"))


def save(name, d):
    (DST / f"{name}.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# 4-5. unibe: gre_general -> Not stated
d = load("unibe")
d["checked"] = "2026-11-12"
d["fields"]["gre_general"]["code"] = "Not stated"
d["fields"]["gre_general"]["value"] = "Not stated on the page checked"
d["fields"]["gre_general"]["quote"] = ""
save("unibe", d)

# 6. unlv: toefl_min -> add NEW TOEFL IBT Test header
d = load("unlv")
d["checked"] = "2026-11-12"
d["fields"]["toefl_min"]["quote"] = "NEW TOEFL IBT Test | " + d["fields"]["toefl_min"]["quote"]
save("unlv", d)

# 7. unt: english_waiver -> add UNT English proof intro
d = load("unt")
d["checked"] = "2026-11-12"
d["fields"]["english_waiver"]["quote"] = (
    "UNT accepts any 1 of the following 4 measures as proof of English | "
    "1. Citizenship of one of these approved English-speaking | "
    + d["fields"]["english_waiver"]["quote"]
)
save("unt", d)

# 8-10. uppsala: app_fee & fee_waiver -> add "Application and tuition fees for PhD students | "
d = load("uppsala")
d["checked"] = "2026-11-12"
q = "Application and tuition fees for PhD students | PhD programmes are free of charge in Sweden, regardless of citizenship."
d["fields"]["app_fee"]["quote"] = q
d["fields"]["fee_waiver"]["quote"] = q
save("uppsala", d)

print("Staged 4 files for Batch 12")
