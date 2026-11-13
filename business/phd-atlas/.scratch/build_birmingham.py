import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_propose = "https://www.birmingham.ac.uk/study/postgraduate/research/how-to-apply/propose-research"
u_ad = "https://www.birmingham.ac.uk/study/postgraduate/research/how-to-apply/advertised-phd"
u_guide = "https://www.birmingham.ac.uk/study/postgraduate/research/how-to-apply"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

q_entry = "Once you have found your subject area you will need to check the entry requirements to see if you are eligible to undertake research with us. Typically you will need to have a good Honours degree and usually a Masters degree."
q_sup = "Once you've identified a subject area, you will need to find a supervisor for your project. All Doctoral Researchers are provided with a lead supervisor, who will act as the main source of academic supervisory support and research mentoring during your time as a Doctoral Researcher at the University."
q_fund = "To pay for your research, there’s a range of funding available from scholarships, charities, loans and self-finance."
q_waiver = "For those who have recently graduated from a University in the UK or majority English speaking country (e.g. USA, Australia, New Zealand or Canada) you may be exempt from taking English language test. Please note that if your degree was delivered in English but not at a recognised university in the UK or majority English speaking country, our Admissions Office will require you to demonstrate your level of English with IELTS/TOEFL/PTE or alternative qualifications."
q_dl = "Make sure you read all the detailed information about the research project including duration, funding level/type, entry requirements and application deadlines."
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

uni_record = {
    "id": "birmingham",
    "institution": "University of Birmingham",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_guide,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research admissions guidance outlines tuition and funding but states no general application fee for postgraduate research degrees.",
            "quote": "",
            "url": u_guide
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Central guidance does not publish fee waiver procedures as no general PGR application fee is stated.",
            "quote": "",
            "url": u_guide
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Birmingham.",
            "quote": "",
            "url": u_guide
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "English language requirements vary by academic subject band; applicants must consult individual course profiles for specific minimum scores.",
            "quote": "For the full list of suitable documents which you can use as your proof of English proficiency, you can visit our English language requirements page.",
            "url": u_ad
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "English language requirements vary by academic subject band; applicants must consult individual course profiles for specific minimum scores.",
            "quote": "For the full list of suitable documents which you can use as your proof of English proficiency, you can visit our English language requirements page.",
            "url": u_ad
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to recent graduates from a university in the UK or a recognised majority English-speaking country; degrees delivered in English elsewhere are not exempt.",
            "quote": q_waiver,
            "url": u_propose
        }
    },
    "notes": "Postgraduate research degrees at the University of Birmingham include PhD, MPhil, and Masters by Research programmes across all colleges and schools."
}

with open(staging_dir / "universities" / "birmingham.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "School of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Electronic, Electrical and Systems Engineering", "Electronic, Electrical and Systems Engineering PhD"),
    ("mech", "Department of Mechanical Engineering", "Mechanical Engineering PhD"),
    ("civil", "Department of Civil Engineering", "Civil Engineering PhD"),
    ("chemeng", "School of Chemical Engineering", "Chemical Engineering PhD"),
    ("materials", "School of Metallurgy and Materials", "Metallurgy and Materials PhD"),
    ("bme", "School of Chemical Engineering / Biomedical Engineering", "Biomedical Engineering PhD"),
    ("chemistry", "School of Chemistry", "Chemistry PhD"),
    ("physics", "School of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "School of Physics and Astronomy", "Astrophysics and Space Research PhD"),
    ("math", "School of Mathematics", "Mathematics PhD"),
    ("statistics", "School of Mathematics", "Statistics PhD"),
    ("biology", "School of Biosciences", "Biosciences PhD"),
    ("biomed", "College of Medical and Dental Sciences", "Medical and Dental Sciences PhD"),
    ("neuro", "School of Psychology / Centre for Human Brain Health", "Neuroscience PhD"),
    ("earth", "School of Geography, Earth and Environmental Sciences", "Earth Sciences PhD"),
    ("environment", "School of Geography, Earth and Environmental Sciences", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Birmingham.",
            "quote": "",
            "url": u_propose
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": u_ets
        }

    prog_record = {
        "id": f"birmingham--{field_id}",
        "university": "birmingham",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_propose,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "General self-proposed research applications are considered on a rolling basis; advertised projects carry specific project deadlines.",
                "quote": q_dl,
                "url": u_ad
            },
            "entry_route": {
                "code": "Either",
                "value": "Applicants typically require a good Honours degree and usually a Master's degree (or international equivalent).",
                "quote": q_entry,
                "url": u_propose
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants proposing research must identify and contact a potential academic supervisor prior to formal application.",
                "quote": q_sup,
                "url": u_propose
            },
            "funding": {
                "code": "Competitive",
                "value": "Funding is competitive and available via scholarships, research councils, charities, and loans.",
                "quote": q_fund,
                "url": u_propose
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Birmingham."
    }

    with open(staging_dir / "programs" / f"birmingham--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated birmingham university record and {len(disciplines)} program records.")
