import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

uni_record = {
    "id": "kuleuven",
    "institution": "KU Leuven",
    "country": "Belgium",
    "region": "Flemish Brabant",
    "grad_page": "https://www.kuleuven.be/english/phd",
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "0 (no fee)",
            "value": "Applicants for a doctoral or predoctoral programme are exempted from paying an application fee at KU Leuven.",
            "quote": "Who is exempted from paying the application fee?\nExemptions on paying the application fee are only granted to applicants:\nfor a (pre)doctoral programme",
            "url": "https://www.kuleuven.be/english/apply/requested-documents/application-fee"
        },
        "fee_waiver": {
            "code": "No fee",
            "value": "Doctoral applicants are exempt from the application fee, so no fee is charged.",
            "quote": "Who is exempted from paying the application fee?\nExemptions on paying the application fee are only granted to applicants:\nfor a (pre)doctoral programme",
            "url": "https://www.kuleuven.be/english/apply/requested-documents/application-fee"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or mentioned for doctoral admission at KU Leuven.",
            "quote": "",
            "url": "https://www.kuleuven.be/english/apply/application-instructions/instructions-doctoral"
        },
        "toefl_min": {
            "code": "79",
            "value": "KU Leuven requires a minimum TOEFL iBT overall score of 79 for English proficiency.",
            "quote": "The minimum overall score is 79.",
            "url": "https://www.kuleuven.be/english/apply/language-requirements/english-proficiency-tests"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "KU Leuven requires a minimum IELTS Academic overall band score of 6.5 for English proficiency.",
            "quote": "The minimum overall score is 6.5.",
            "url": "https://www.kuleuven.be/english/apply/language-requirements/english-proficiency-tests"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "English proficiency test is waived only for applicants who have obtained a previous diploma taught in English in Australia, English-speaking Canada, Ireland, New Zealand, the UK, or the USA.",
            "quote": "All applicants who have not obtained a previous diploma in a programme taught in English in Australia, English-speaking Canada, Ireland, New Zealand, the United Kingdom or the United States of America must submit one of the tests mentioned on this webpage, proving their proficiency in English.",
            "url": "https://www.kuleuven.be/english/apply/language-requirements/english-proficiency-tests"
        }
    },
    "notes": "Doctoral education at KU Leuven is organized through doctoral schools including the Arenberg Doctoral School (Science, Engineering & Technology) and Biomedical Sciences Doctoral School. Applicants must secure a supervisor before applying."
}

with open(staging_dir / "universities" / "kuleuven.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "Arenberg Doctoral School / Department of Computer Science", "Doctoral Programme in Engineering Science: Computer Science"),
    ("ece", "Arenberg Doctoral School / Department of Electrical Engineering (ESAT)", "Doctoral Programme in Engineering Science: Electrical Engineering"),
    ("mech", "Arenberg Doctoral School / Department of Mechanical Engineering", "Doctoral Programme in Engineering Science: Mechanical Engineering"),
    ("civil", "Arenberg Doctoral School / Department of Civil Engineering", "Doctoral Programme in Engineering Science: Civil Engineering"),
    ("chemeng", "Arenberg Doctoral School / Department of Chemical Engineering", "Doctoral Programme in Engineering Science: Chemical Engineering"),
    ("materials", "Arenberg Doctoral School / Department of Materials Engineering", "Doctoral Programme in Engineering Science: Materials Engineering"),
    ("bme", "Arenberg Doctoral School / Department of Mechanical Engineering / ESAT", "Doctoral Programme in Biomedical Engineering"),
    ("chemistry", "Arenberg Doctoral School / Department of Chemistry", "Doctoral Programme in Science: Chemistry"),
    ("physics", "Arenberg Doctoral School / Department of Physics and Astronomy", "Doctoral Programme in Science: Physics"),
    ("astronomy", "Arenberg Doctoral School / Institute of Astronomy", "Doctoral Programme in Science: Astronomy & Astrophysics"),
    ("math", "Arenberg Doctoral School / Department of Mathematics", "Doctoral Programme in Science: Mathematics"),
    ("statistics", "Arenberg Doctoral School / Leuven Statistics Research Centre", "Doctoral Programme in Science: Statistics"),
    ("biology", "Arenberg Doctoral School / Department of Biology", "Doctoral Programme in Science: Biology"),
    ("earth", "Arenberg Doctoral School / Department of Earth and Environmental Sciences", "Doctoral Programme in Science: Geology"),
    ("neuro", "Doctoral School of Biomedical Sciences / Department of Neurosciences", "Doctoral Programme in Biomedical Sciences: Neurosciences")
]

doc_url = "https://www.kuleuven.be/english/apply/application-instructions/instructions-doctoral"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

for field_id, dept, prog_title in disciplines:
    if field_id in ("math", "physics", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject test is not stated or required for doctoral admission in {prog_title} at KU Leuven.",
            "quote": "",
            "url": doc_url
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": ets_url
        }

    prog_record = {
        "id": f"kuleuven--{field_id}",
        "university": "kuleuven",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": "https://set.kuleuven.be/phd",
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Per position",
                "value": "KU Leuven doctoral admissions have no general deadline; individual supervisors or research projects have their own deadlines.",
                "quote": "This guide explains the different steps to apply for a doctoral programme at KU Leuven. There is no general application deadline. It is possible, however, that an individual supervisor or project does have deadlines.",
                "url": doc_url
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Applicants must hold a relevant master's degree with distinction, or an equivalent higher education degree from abroad, or pass a predoctoral exam.",
                "quote": "Every PhD candidate must meet the following requirements:\nEither you hold a Flemish Master’s degree relevant to the doctoral research or an equivalent higher education degree from abroad, obtained with at least the degree of distinction or have distinguished yourself with high-quality scientific publications or design-oriented achievements,\nOr you have passed the predoctoral exam with the degree of distinction.",
                "url": doc_url
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants cannot initiate the admission procedure directly; a KU Leuven supervisor must start the application on the candidate's behalf.",
                "quote": "You cannot initiate the application procedure yourself. Regardless of your starting point, your KU Leuven supervisor will start up the application procedure on your behalf.",
                "url": doc_url
            },
            "funding": {
                "code": "Typical",
                "value": "PhD positions advertised on the KU Leuven jobsite have financing already arranged by the supervisor.",
                "quote": "The PhD positions on the KU Leuven jobsite already have financing available (via the supervisor).",
                "url": doc_url
            },
            "gre_subject": gre_sub
        },
        "notes": f"{prog_title} at KU Leuven."
    }

    with open(staging_dir / "programs" / f"kuleuven--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Staged kuleuven university and {len(disciplines)} programs successfully.")
