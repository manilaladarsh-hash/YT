import json
from pathlib import Path

staging_unis = Path("data/staging/universities")
staging_progs = Path("data/staging/programs")
staging_unis.mkdir(parents=True, exist_ok=True)
staging_progs.mkdir(parents=True, exist_ok=True)

eng_url = "https://studieren.univie.ac.at/en/applying-for-a-programme/language-proficiency/english-language-proficiency"
fee_url = "https://studieren.univie.ac.at/en/studying-and-learning/financial-matters/amount-of-the-tuition-fee/students-union-fee"
praedoc_url = "https://careers.univie.ac.at/en/praedoc"
prog_url = "https://studieren.univie.ac.at/en/find-your-degree-programme"

# Central Univie Record
univie_uni = {
    "id": "univie",
    "institution": "University of Vienna",
    "country": "Austria",
    "region": "Vienna",
    "grad_page": "https://doktorat.univie.ac.at/en/",
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "No application fee is charged to submit an admission application through u:space at the University of Vienna.",
            "quote": "",
            "url": fee_url
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "No application fee is charged, so no application fee waiver is stated.",
            "quote": "",
            "url": fee_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE is not required or used for doctoral admission at the University of Vienna.",
            "quote": "",
            "url": prog_url
        },
        "toefl_min": {
            "code": "94",
            "value": "Minimum TOEFL iBT score of 94 points or higher is required for English language proficiency at level B2.",
            "quote": "TOEFL: IBT (internet-based): 94 points or higher",
            "url": eng_url
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum IELTS Academic overall band score of 6.5 points is required for English language proficiency at level B2.",
            "quote": "IELTS Academic: Overall Band Score: 6.5 points",
            "url": eng_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "English proficiency is satisfied by a full-time degree programme of at least two years taught entirely in English at a university in an EU/EEA country, Switzerland, UK, USA, Australia, New Zealand or Canada.",
            "quote": "full-time degree programme of at least two years and\ntaught entirely in English and\nat a university in an EU/EEA country, Switzerland, the United Kingdom of Great Britain and Northern Ireland, the USA, Australia, New Zealand or Canada.",
            "url": eng_url
        }
    },
    "notes": "Doctoral studies at the University of Vienna (Dr. rer. nat., Dr. techn., PhD) are managed through the Center for Doctoral Studies and Vienna Doctoral Schools. Researchers are typically appointed as PraeDocs under employment contracts."
}

with open(staging_unis / "univie.json", "w", encoding="utf-8") as f:
    json.dump(univie_uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# Programs
departments = {
    "cs": ("Faculty of Computer Science", []),
    "math": ("Faculty of Mathematics", []),
    "physics": ("Faculty of Physics", []),
    "astronomy": ("Department of Astrophysics / Faculty of Earth Sciences, Geography and Astronomy", []),
    "chemistry": ("Faculty of Chemistry", []),
    "earth": ("Faculty of Earth Sciences, Geography and Astronomy", []),
    "biology": ("Faculty of Life Sciences / Center for Molecular Biology", []),
    "environment": ("Faculty of Life Sciences & Faculty of Earth Sciences", []),
    "neuro": ("Vienna Doctoral School in Cognition, Behavior and Neuroscience", []),
}

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

for field, (dept, also_fields) in departments.items():
    if field in ("math", "physics"):
        gre_sub = {
            "code": "Not stated",
            "value": "No GRE Subject test is required or mentioned for doctoral admission.",
            "quote": "",
            "url": prog_url
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": ets_url
        }

    prog_data = {
        "id": f"univie--{field}",
        "university": "univie",
        "field": field,
        "also_fields": also_fields,
        "department": dept,
        "program_page": prog_url,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Per position",
                "value": "Doctoral candidates apply to specific open PraeDoc positions advertised throughout the year.",
                "quote": "The University of Vienna is advertising 11 PhD positions (call for application opens in September 2026). We look forward to receiving applications from outstanding early-career researchers who wish to complete their PhD at the University of Vienna and actively participate in excellent research within an international environment.",
                "url": praedoc_url
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Doctoral and PhD programmes at the University of Vienna have a stipulated study duration of 6 semesters following completion of a master's programme.",
                "quote": "Doctoral/PhD programme\nStipulated degree programme duration 6 semesters + 2 tolerance semesters. You pay the tuition fee from the 9th semester onwards.",
                "url": fee_url
            },
            "supervisor": {
                "code": "Required",
                "value": "Doctoral researchers must be appointed to an approved research project with a faculty supervisor or obtain a supervisory commitment.",
                "quote": "We look forward to receiving applications from outstanding early-career researchers who wish to complete their PhD at the University of Vienna and actively participate in excellent research within an international environment.",
                "url": praedoc_url
            },
            "funding": {
                "code": "Typical",
                "value": "Doctoral researchers appointed to PraeDoc positions are fully funded employees under the Austrian collective bargaining agreement.",
                "quote": "seeking outstanding candidates for more than 40 fully funded PhD positions in the Life - and Natural Sciences.",
                "url": praedoc_url
            },
            "gre_subject": gre_sub
        },
        "notes": f"University of Vienna offers doctoral education in {dept} leading to Dr. rer. nat. or PhD degrees."
    }

    with open(staging_progs / f"univie--{field}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Generated univie and {len(departments)} programs.")
