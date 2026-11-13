import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_env = "https://environment.leeds.ac.uk/see-research-degrees/doc/entry-requirements"
u_apply = "https://www.leeds.ac.uk/research-applying/doc/applying-research-degrees"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

# Extract exact quotes from cache
d_env = json.load(open([p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_env][0], encoding="utf-8"))
t_env = d_env["text"]

idx_entry = t_env.find("minimum entry requirements for PhD study")
q_entry = t_env[idx_entry:t_env.find("English language requirements", idx_entry)].strip()

q_ielts = "IELTS: 6.0 overall with at least 5.5 in all components."
q_waiver = "a postgraduate degree from a majority English speaking country. The duration of the degree must be at least 12 months and awarded less than 2 years and 4 months from the proposed start date of the PhD"

q_dl = "We advise you to apply at least four months before your proposed start date. This is to allow sufficient time to review your application and undertake any additional checks."
q_sup = "You need to identify the supervisors available to work with you. They must be experts in the topic you are interested in to ensure that your research is accurate and adding to current knowledge."
q_fund = "UK research councils: competition for these scholarships is high but the majority of your fees will be funded so it is well worth applying."

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

uni_record = {
    "id": "leeds",
    "institution": "University of Leeds",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_apply,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research degree admissions guidance lists tuition fees and funding with no general application fee for postgraduate research degrees.",
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
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Leeds.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "Specific TOEFL minimums vary by faculty and school programme; applicants should confirm scores on their individual school course pages.",
            "quote": "",
            "url": u_env
        },
        "ielts_min": {
            "code": "6.0",
            "value": "Standard minimum English requirement for research degrees is IELTS 6.0 overall with at least 5.5 in all components.",
            "quote": q_ielts,
            "url": u_env
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to degrees completed in a recognised majority English-speaking country; degrees completed in English elsewhere do not qualify.",
            "quote": q_waiver,
            "url": u_env
        }
    },
    "notes": "Postgraduate research degrees at the University of Leeds include PhD, MPhil, and MSc by Research programmes across eight academic faculties."
}

with open(staging_dir / "universities" / "leeds.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "School of Computing", "Computing PhD"),
    ("ece", "School of Electronic and Electrical Engineering", "Electronic and Electrical Engineering PhD"),
    ("mech", "School of Mechanical Engineering", "Mechanical Engineering PhD"),
    ("civil", "School of Civil Engineering", "Civil Engineering PhD"),
    ("chemeng", "School of Chemical and Process Engineering", "Chemical and Process Engineering PhD"),
    ("materials", "School of Chemical and Process Engineering / School of Chemistry", "Materials Science PhD"),
    ("bme", "School of Mechanical Engineering / Institute of Medical and Biological Engineering", "Biomedical Engineering PhD"),
    ("chemistry", "School of Chemistry", "Chemistry PhD"),
    ("physics", "School of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "School of Physics and Astronomy", "Astrophysics PhD"),
    ("math", "School of Mathematics", "Mathematics PhD"),
    ("statistics", "School of Mathematics", "Statistics PhD"),
    ("biology", "School of Biology", "Biological Sciences PhD"),
    ("biomed", "School of Biomedical Sciences", "Biomedical Sciences PhD"),
    ("neuro", "School of Biomedical Sciences", "Neuroscience PhD"),
    ("earth", "School of Earth and Environment", "Earth Sciences PhD"),
    ("environment", "School of Earth and Environment", "Environmental Science PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Leeds.",
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
        "id": f"leeds--{field_id}",
        "university": "leeds",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_apply,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applicants are advised to apply at least four months before their proposed start date; admissions operate on a rolling basis across multiple start dates.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Minimum entry requirements are a 2.1 honours degree or good performance in a Master's level course in a relevant subject.",
                "quote": q_entry,
                "url": u_env
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants need to identify and contact available academic supervisors who are experts in their research topic prior to applying.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Competition for research council scholarships and faculty awards is high and funding is competitive.",
                "quote": q_fund,
                "url": u_apply
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Leeds."
    }

    with open(staging_dir / "programs" / f"leeds--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated leeds university record and {len(disciplines)} program records.")
