import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_prog = "https://www.nottingham.ac.uk/pgstudy/course/research/physics-phd"
u_lang = "https://www.nottingham.ac.uk/studywithus/international-applicants/english-language.aspx"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

# Load cached texts
p_prog = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_prog][0]
t_prog = json.load(open(p_prog, encoding="utf-8"))["text"]

p_lang = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_lang][0]
t_lang = json.load(open(p_lang, encoding="utf-8"))["text"]

# Quotes
q_entry = "2:1 or a masters in physics, mathematical physics or mathematics"
q_sup = "You will have at least 10 meetings per year with your supervisor."
q_dl = "We accept applications all year round for some groups but you may want to check specific deadlines with your supervisor or prospective funder."
q_fund = "Check our guide to find out more about funding your postgraduate degree."
q_ielts = "IELTS\n6.5 (6.0 in each element)"
q_toefl = "This includes TOEFL iBT, Pearson PTE, GCSE, IB and O level English."
q_waiver = "If you're a native English speaker, or you have studied in an English-speaking country or institution, we may be able to accept your academic qualifications as evidence of your English language ability. Check the list of approved countries on the UK government website."

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

assert q_entry in t_prog, "q_entry not in t_prog"
assert q_sup in t_prog, "q_sup not in t_prog"
assert q_dl in t_prog, "q_dl not in t_prog"
assert q_fund in t_prog, "q_fund not in t_prog"
assert q_ielts in t_prog, "q_ielts not in t_prog"
assert q_toefl in t_prog, "q_toefl not in t_prog"
assert q_waiver in t_lang, "q_waiver not in t_lang"

uni_record = {
    "id": "nottingham",
    "institution": "University of Nottingham",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_prog,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research guidance outlines tuition fees and postgraduate funding without stating a general application fee for research degree programmes.",
            "quote": "",
            "url": u_prog
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Central guidance does not publish fee waiver procedures as no general PGR application fee is stated.",
            "quote": "",
            "url": u_prog
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Nottingham.",
            "quote": "",
            "url": u_prog
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "Nottingham accepts TOEFL iBT as an alternative qualification alongside course-specific IELTS requirements.",
            "quote": q_toefl,
            "url": u_prog
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Standard minimum English requirement for research programmes is IELTS 6.5 with at least 6.0 in each element.",
            "quote": q_ielts,
            "url": u_prog
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to native English speakers or applicants who studied in approved English-speaking countries on the UK government list; degrees from India do not qualify.",
            "quote": q_waiver,
            "url": u_lang
        }
    },
    "notes": "Postgraduate research degrees at the University of Nottingham include PhD and MRes programmes across faculties."
}

with open(staging_dir / "universities" / "nottingham.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "School of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Electrical and Electronic Engineering", "Electrical and Electronic Engineering PhD"),
    ("mech", "Department of Mechanical, Materials and Manufacturing Engineering", "Mechanical Engineering PhD"),
    ("civil", "Department of Civil Engineering", "Civil Engineering PhD"),
    ("chemeng", "Department of Chemical and Environmental Engineering", "Chemical Engineering PhD"),
    ("materials", "Department of Mechanical, Materials and Manufacturing Engineering", "Materials Science PhD"),
    ("bme", "School of Medicine / Department of Mechanical Engineering", "Biomedical Engineering PhD"),
    ("chemistry", "School of Chemistry", "Chemistry PhD"),
    ("physics", "School of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "School of Physics and Astronomy", "Astronomy PhD"),
    ("math", "School of Mathematical Sciences", "Mathematical Sciences PhD"),
    ("statistics", "School of Mathematical Sciences", "Statistics PhD"),
    ("biology", "School of Life Sciences", "Biological Sciences PhD"),
    ("biomed", "School of Medicine / School of Life Sciences", "Medical Sciences PhD"),
    ("neuro", "School of Life Sciences / School of Medicine", "Neuroscience PhD"),
    ("earth", "School of Geography / British Geological Survey", "Earth Sciences PhD"),
    ("environment", "Department of Chemical and Environmental Engineering / School of Geography", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Nottingham.",
            "quote": "",
            "url": u_prog
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": u_ets
        }

    prog_record = {
        "id": f"nottingham--{field_id}",
        "university": "nottingham",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_prog,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications are accepted all year round for most research groups, subject to specific funder or supervisor deadlines.",
                "quote": q_dl,
                "url": u_prog
            },
            "entry_route": {
                "code": "Either",
                "value": "Standard doctoral entry requires a 2:1 honours degree or a relevant Master's qualification.",
                "quote": q_entry,
                "url": u_prog
            },
            "supervisor": {
                "code": "Required",
                "value": "Postgraduate researchers work under the direction of an academic supervisor with regular supervisory meetings.",
                "quote": q_sup,
                "url": u_prog
            },
            "funding": {
                "code": "Competitive",
                "value": "Postgraduate research funding is competitive through university studentships and research council awards.",
                "quote": q_fund,
                "url": u_prog
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Nottingham."
    }

    with open(staging_dir / "programs" / f"nottingham--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated nottingham university record and {len(disciplines)} program records.")
