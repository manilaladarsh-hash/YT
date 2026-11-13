import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_fee = "https://www.ucl.ac.uk/study/prospective-students/graduate/how-apply/application-fees"
u_eng = "https://www.ucl.ac.uk/study/prospective-students/graduate/how-apply/english-language-requirements"
u_guide = "https://www.ucl.ac.uk/study/prospective-students/graduate/how-apply/applying-graduate-research-study-ucl"
u_entry = "https://www.ucl.ac.uk/study/prospective-students/graduate/how-apply/entry-requirements"

uni_record = {
    "id": "ucl",
    "institution": "University College London",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_guide,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "0 (no fee)",
            "value": "UCL Research Degree courses are exempt from the graduate application fee.",
            "quote": "Courses that are exempt from application fees\nUCL Research Degree courses",
            "url": u_fee
        },
        "fee_waiver": {
            "code": "No fee",
            "value": "Research degree courses do not charge an application fee.",
            "quote": "Courses that are exempt from application fees\nUCL Research Degree courses",
            "url": u_fee
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for graduate research admission at UCL.",
            "quote": "",
            "url": u_entry
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "UCL sets five levels of English language proficiency; each degree course page confirms which level applies.",
            "quote": "See each degree course page to confirm which UCL level of English proficiency you will need to meet.",
            "url": u_eng
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "UCL sets five levels of English language proficiency; each degree course page confirms which level applies.",
            "quote": "See each degree course page to confirm which UCL level of English proficiency you will need to meet.",
            "url": u_eng
        },
        "english_waiver": {
            "code": "No",
            "value": "UCL waives the English test only for degrees completed in an approved majority English-speaking country; degrees from India do not qualify.",
            "quote": "This must be in a country that UCL considers to be acceptable for this purpose and the medium of instruction must be English.",
            "url": u_eng
        }
    },
    "notes": "Graduate research degrees at UCL include MPhil/PhD programmes across faculties. Most research programmes have rolling admission and no application fee."
}

with open(staging_dir / "universities" / "ucl.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

disciplines = [
    ("cs", "Department of Computer Science", "Computer Science MPhil/PhD"),
    ("ece", "Department of Electronic and Electrical Engineering", "Electronic and Electrical Engineering MPhil/PhD"),
    ("mech", "Department of Mechanical Engineering", "Mechanical Engineering MPhil/PhD"),
    ("civil", "Department of Civil, Environmental and Geomatic Engineering", "Civil, Environmental and Geomatic Engineering MPhil/PhD"),
    ("chemeng", "Department of Chemical Engineering", "Chemical Engineering MPhil/PhD"),
    ("materials", "Department of Chemistry / Physics / IMD", "Materials Science MPhil/PhD"),
    ("bme", "Department of Medical Physics and Biomedical Engineering", "Medical Physics and Biomedical Engineering MPhil/PhD"),
    ("chemistry", "Department of Chemistry", "Chemistry MPhil/PhD"),
    ("physics", "Department of Physics and Astronomy", "Physics MPhil/PhD"),
    ("astronomy", "Department of Physics and Astronomy", "Astrophysics MPhil/PhD"),
    ("math", "Department of Mathematics", "Mathematics MPhil/PhD"),
    ("statistics", "Department of Statistical Science", "Statistical Science MPhil/PhD"),
    ("biology", "Division of Biosciences", "Biosciences MPhil/PhD"),
    ("earth", "Department of Earth Sciences", "Earth Sciences MPhil/PhD"),
    ("neuro", "Division of Biosciences / Queen Square Institute of Neurology", "Neuroscience MPhil/PhD"),
    ("biomed", "Division of Medicine / Faculty of Medical Sciences", "Medical Sciences MPhil/PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at UCL.",
            "quote": "",
            "url": u_entry
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": ets_url
        }

    prog_record = {
        "id": f"ucl--{field_id}",
        "university": "ucl",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_guide,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications for research degrees are accepted on a rolling basis; UCL recommends applying at least four months before the intended start date.",
                "quote": "If your course has no application deadline, we recommend you apply at least four months before your intended start date.",
                "url": u_guide
            },
            "entry_route": {
                "code": "Either",
                "value": "Research applicants are normally required to hold either a first or upper-second class bachelor's degree from a UK university or a recognised taught master's degree (or overseas equivalent).",
                "quote": "research applicants will normally be required to hold a first or upper-second class Bachelor...degree from a UK university...in an appropriate subject, or a recognised taught Master...degree. Overseas qualifications of an equivalent standard from a recognised higher education institution are also accepted.",
                "url": u_entry
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants must contact the academic department to discuss suitability and ensure a suitable supervisor is available before applying.",
                "quote": "Please note - Before you apply, contact the academic department to discuss your suitability and to ensure a suitable supervisor is available.",
                "url": u_guide
            },
            "funding": {
                "code": "Competitive",
                "value": "Academics can help identify funding sources and nominate qualified candidates for scholarships.",
                "quote": "They can also nominate you for scholarships.",
                "url": u_guide
            },
            "gre_subject": gre_sub
        },
        "notes": f"{title} at University College London."
    }

    with open(staging_dir / "programs" / f"ucl--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Staged ucl and {len(disciplines)} programs successfully.")
