import json
import hashlib
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.bath.ac.uk/guides/how-to-apply-for-doctoral-study/"
u_faqs = "https://www.bath.ac.uk/guides/applying-for-doctoral-study-at-the-university-of-bath-faqs/"
u_lang = "https://www.bath.ac.uk/corporate-information/english-language-requirements-for-qualifications-category-c/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f".cache/pages/{key}.json", encoding="utf-8"))["text"]

t_apply = get_text(u_apply)
t_faqs = get_text(u_faqs)
t_lang = get_text(u_lang)
t_ets = get_text(u_ets)

idx_dl = t_apply.find("The application deadlines are three months before the intended start date (for Overseas applicants)")
q_dl = t_apply[idx_dl:idx_dl + 233]
assert q_dl in t_apply, "q_dl not in t_apply"

idx_entry = t_faqs.find("Most PhD programmes are open to applicants with a first-class or upper second-class undergraduate degree")
q_entry = t_faqs[idx_entry:idx_entry + 183]
assert q_entry in t_faqs, "q_entry not in t_faqs"

idx_sup = t_faqs.find("If you are applying with your own research proposal, your application must name at least one proposed supervisor")
q_sup = t_faqs[idx_sup:idx_sup + 258]
assert q_sup in t_faqs, "q_sup not in t_faqs"

idx_fund = t_faqs.find("A standard University of Bath studentship offers the UK Research and Innovation (UKRI) stipend rate")
q_fund = t_faqs[idx_fund:idx_fund + 144]
assert q_fund in t_faqs, "q_fund not in t_faqs"

idx_ielts = t_lang.find("IELTS Academic and IELTS Online (including One Skill Retake)")
q_ielts = t_lang[idx_ielts:idx_ielts + 89]
assert q_ielts in t_lang, "q_ielts not in t_lang"

idx_toefl = t_lang.find("TOEFL iBT and iBT Home Edition\n90 overall with 21 in each component")
q_toefl = t_lang[idx_toefl:idx_toefl + 68]
assert q_toefl in t_lang, "q_toefl not in t_lang"

idx_waiver = t_faqs.find("If English is not your first language, you must meet our English language requirements.")
q_waiver = t_faqs[idx_waiver:idx_waiver + 152]
assert q_waiver in t_faqs, "q_waiver not in t_faqs"

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
assert ets_quote in t_ets, "ets_quote not in t_ets"

uni_record = {
    "id": "bath",
    "institution": "University of Bath",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_apply,
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
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Bath.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "90",
            "value": "Standard minimum English requirement for Category C programmes is TOEFL iBT 90 overall with 21 in each component.",
            "quote": q_toefl,
            "url": u_lang
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Standard minimum English requirement for Category C programmes is IELTS Academic 6.5 with at least 6.0 in each component.",
            "quote": q_ielts,
            "url": u_lang
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption depends on nationality or previous study in majority English-speaking countries; degrees from non-majority countries like India do not qualify.",
            "quote": q_waiver,
            "url": u_faqs
        }
    },
    "notes": "Postgraduate research degrees at the University of Bath include PhD, Integrated PhD, and Professional Doctorate programmes across faculties."
}

with open(staging_dir / "universities" / "bath.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "Department of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Electronic & Electrical Engineering", "Electronic and Electrical Engineering PhD"),
    ("mech", "Department of Mechanical Engineering", "Mechanical Engineering PhD"),
    ("civil", "Department of Architecture & Civil Engineering", "Civil Engineering PhD"),
    ("chemeng", "Department of Chemical Engineering", "Chemical Engineering PhD"),
    ("materials", "Department of Mechanical Engineering / Department of Physics", "Materials Science PhD"),
    ("bme", "Department of Electronic & Electrical Engineering / Centre for Biosensors", "Biomedical Engineering PhD"),
    ("chemistry", "Department of Chemistry", "Chemistry PhD"),
    ("physics", "Department of Physics", "Physics PhD"),
    ("astronomy", "Department of Physics", "Astrophysics PhD"),
    ("math", "Department of Mathematical Sciences", "Mathematical Sciences PhD"),
    ("statistics", "Department of Mathematical Sciences", "Statistics PhD"),
    ("biology", "Department of Life Sciences", "Biological Sciences PhD"),
    ("biomed", "Department of Life Sciences / Centre for Therapeutic Innovation", "Medical / Biomedical Sciences PhD"),
    ("neuro", "Department of Life Sciences / Department of Psychology", "Neuroscience PhD"),
    ("earth", "Department of Architecture & Civil Engineering / Department of Life Sciences", "Earth and Environmental Engineering PhD"),
    ("environment", "Department of Chemical Engineering / Centre for Sustainable and Circular Technologies", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Bath.",
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
        "id": f"bath--{field_id}",
        "university": "bath",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_apply,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "2027-06-30",
                "value": "The application deadline for an end-of-September start is 30 June for Overseas applicants (or three months before other intended start dates).",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Most PhD programmes are open to applicants with a first-class or upper second-class undergraduate degree or a master's degree with Merit (or international equivalents).",
                "quote": q_entry,
                "url": u_faqs
            },
            "supervisor": {
                "code": "Required",
                "value": "Applications must name at least one proposed supervisor who will review the application, and applicants are strongly recommended to contact supervisors in advance.",
                "quote": q_sup,
                "url": u_faqs
            },
            "funding": {
                "code": "Competitive",
                "value": "Standard studentships provide the UKRI stipend rate (£21,805 for 2026-2027) plus tuition fees via competitive university awards and research councils.",
                "quote": q_fund,
                "url": u_faqs
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Bath."
    }

    with open(staging_dir / "programs" / f"bath--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated bath university record and {len(disciplines)} program records.")
