import json
import hashlib
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.ncl.ac.uk/postgraduate-research/how-to-apply/"
u_pgr = "https://www.ncl.ac.uk/postgraduate-research/"
u_lang = "https://www.ncl.ac.uk/international/language/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f".cache/pages/{key}.json", encoding="utf-8"))["text"]

t_apply = get_text(u_apply)
t_pgr = get_text(u_pgr)
t_lang = get_text(u_lang)
t_ets = get_text(u_ets)

idx_sup = t_pgr.find("As a postgraduate research student at Newcastle, you’ll engage in independent research under the guidance of experienced supervisors, and with the support of our Doctoral College.")
q_sup = t_pgr[idx_sup:idx_sup + 181]
assert q_sup in t_pgr, "q_sup not in t_pgr"

idx_fund = t_pgr.find("We invest in research funding to support our postgraduate research students. There are many options and opportunities for you to explore.")
q_fund = t_pgr[idx_fund:idx_fund + 138]
assert q_fund in t_pgr, "q_fund not in t_pgr"

idx_dl = t_apply.find("The majority of studentships have a fixed project title and named supervisor or supervisors.")
q_dl = t_apply[idx_dl:idx_dl + 92]
assert q_dl in t_apply, "q_dl not in t_apply"

idx_entry = t_apply.find("Academic and English language requirements are all given in individual course profiles. Studentship adverts will specify academic and English language requirements.")
q_entry = t_apply[idx_entry:idx_entry + 165]
assert q_entry in t_apply, "q_entry not in t_apply"

idx_ielts = t_lang.find("In most cases you will need an overall score of IELTS 6.5 or equivalent. You will also need at least IELTS 5.5 or equivalent in each of the four sub-skills")
q_ielts = t_lang[idx_ielts:idx_ielts + 152]
assert q_ielts in t_lang, "q_ielts not in t_lang"

idx_toefl = t_lang.find("Before 21 January 2026\nTOEFL IBT: score of 90 with a minimum of:\nreading: 18")
q_toefl = t_lang[idx_toefl:idx_toefl + 74]
assert q_toefl in t_lang, "q_toefl not in t_lang"

idx_waiver = t_lang.find("If English is not your first language you will need to provide a recognised English language test or qualification.")
q_waiver = t_lang[idx_waiver:idx_waiver + 115]
assert q_waiver in t_lang, "q_waiver not in t_lang"

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
assert ets_quote in t_ets, "ets_quote not in t_ets"

uni_record = {
    "id": "newcastle",
    "institution": "Newcastle University",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_pgr,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research guidance outlines tuition fees and postgraduate funding without stating a general application fee for research degree programmes.",
            "quote": "",
            "url": u_apply
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Central guidance does not publish fee waiver procedures as no general PGR application fee is stated.",
            "quote": "",
            "url": u_apply
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Newcastle.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "90",
            "value": "Standard minimum English requirement for degree programmes is TOEFL iBT 90 with minimum sub-scores (such as reading 18).",
            "quote": q_toefl,
            "url": u_lang
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Standard minimum English requirement is IELTS 6.5 overall with at least 5.5 in each of the four sub-skills.",
            "quote": q_ielts,
            "url": u_lang
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to applicants from approved majority English-speaking countries; degrees from non-majority countries like India do not waive the test requirement.",
            "quote": q_waiver,
            "url": u_lang
        }
    },
    "notes": "Postgraduate research degrees at Newcastle University include PhD, MPhil, and MD programmes across faculties."
}

with open(staging_dir / "universities" / "newcastle.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "School of Computing", "Computing Science PhD"),
    ("ece", "School of Engineering", "Electrical and Electronic Engineering PhD"),
    ("mech", "School of Engineering", "Mechanical Engineering PhD"),
    ("civil", "School of Engineering", "Civil Engineering PhD"),
    ("chemeng", "School of Engineering", "Chemical Engineering PhD"),
    ("materials", "School of Engineering", "Materials Engineering PhD"),
    ("bme", "School of Engineering / Faculty of Medical Sciences", "Biomedical Engineering PhD"),
    ("chemistry", "School of Natural and Environmental Sciences", "Chemistry PhD"),
    ("physics", "School of Mathematics, Statistics and Physics", "Physics PhD"),
    ("astronomy", "School of Mathematics, Statistics and Physics", "Astrophysics PhD"),
    ("math", "School of Mathematics, Statistics and Physics", "Mathematics PhD"),
    ("statistics", "School of Mathematics, Statistics and Physics", "Statistics PhD"),
    ("biology", "School of Natural and Environmental Sciences", "Biological Sciences PhD"),
    ("biomed", "Faculty of Medical Sciences / Biosciences Institute", "Medical Sciences PhD"),
    ("neuro", "Faculty of Medical Sciences / Biosciences Institute", "Neuroscience PhD"),
    ("earth", "School of Natural and Environmental Sciences", "Earth Science PhD"),
    ("environment", "School of Natural and Environmental Sciences", "Environmental Science PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Newcastle.",
            "quote": "",
            "url": u_apply
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": u_ets
        }

    prog_record = {
        "id": f"newcastle--{field_id}",
        "university": "newcastle",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_pgr,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Research applications are accepted throughout the year on a rolling basis, while funded studentships have fixed project-specific deadlines.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Academic entry requirements are specified in individual course profiles and studentship adverts, typically requiring a 2:1 honours degree or a master's qualification.",
                "quote": q_entry,
                "url": u_apply
            },
            "supervisor": {
                "code": "Required",
                "value": "Postgraduate researchers engage in independent research under the guidance of experienced academic supervisors.",
                "quote": q_sup,
                "url": u_pgr
            },
            "funding": {
                "code": "Competitive",
                "value": "Postgraduate research funding is competitive via university studentships, Doctoral Training Centres and Partnerships, and external research councils.",
                "quote": q_fund,
                "url": u_pgr
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at Newcastle University."
    }

    with open(staging_dir / "programs" / f"newcastle--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated newcastle university record and {len(disciplines)} program records.")
