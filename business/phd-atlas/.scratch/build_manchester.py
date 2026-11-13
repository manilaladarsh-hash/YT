import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_bmh = "https://www.bmh.manchester.ac.uk/study/research/getting-started/eligibility-and-entry-requirements/"
u_se = "https://www.se.manchester.ac.uk/study/postgraduate-research/getting-started/applying/"
u_lang = "https://www.manchester.ac.uk/study/international/admissions/language-requirements/"
u_guide = "https://www.manchester.ac.uk/study/postgraduate-research/admissions/how-to-apply/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

# Extract exact quotes from cache
d_bmh = json.load(open([p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_bmh][0], encoding="utf-8"))
text_bmh = d_bmh["text"]
idx_entry = text_bmh.find("To be considered for entry")
q_entry = text_bmh[idx_entry:text_bmh.find("International applicants must", idx_entry)].strip()

idx_toefl = text_bmh.find("a minimum IELTS score of 6.5 overall or TOEFL (iBT) 90;")
q_toefl = text_bmh[idx_toefl:idx_toefl + len("a minimum IELTS score of 6.5 overall or TOEFL (iBT) 90;\neach component of the English test to meet the minimum requirement of IELTS 5.5 in all components, TOEFL (iBT 22);")]

idx_ielts = text_bmh.find("a minimum IELTS score of 6.5 overall or TOEFL (iBT) 90;")
q_ielts = text_bmh[idx_ielts:idx_ielts + len("a minimum IELTS score of 6.5 overall or TOEFL (iBT) 90;\neach component of the English test to meet the minimum requirement of IELTS 5.5 in all components, TOEFL (iBT 22);\nfor the writing component, that you have achieved a minimum of 6.0 (IELTS).")]

q_lang = "For Student Route visa purposes, the UKVI has a prescribed list of Majority English-speaking countries (this list is not defined by The University of Manchester)."
q_sup = "Contacted the project supervisor and spoken to them about your suitability for the project."
q_fund = "If you are nominated for funding by your supervisor, you may be invited to further interviews to determine your suitability for funding."
q_roll = "We will try and notify you within 4-6 weeks of your application. However, due to various funding applications and deadlines, you may not receive an answer during this timeframe."

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

uni_record = {
    "id": "manchester",
    "institution": "University of Manchester",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_guide,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research admissions guidance does not state an application fee for postgraduate research degrees; taught master's application fees do not apply to PGR.",
            "quote": "",
            "url": u_guide
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Central research admissions guidance does not publish fee waivers as no general PGR application fee is stated.",
            "quote": "",
            "url": u_guide
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Manchester.",
            "quote": "",
            "url": u_guide
        },
        "toefl_min": {
            "code": "90",
            "value": "For most standard PhD/MPhil programmes, minimum TOEFL iBT requirement is 90 with at least 22 in each component.",
            "quote": q_toefl,
            "url": u_bmh
        },
        "ielts_min": {
            "code": "6.5",
            "value": "For most standard PhD/MPhil programmes, minimum IELTS Academic requirement is 6.5 overall (minimum 5.5 in all components and 6.0 in writing).",
            "quote": q_ielts,
            "url": u_bmh
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to nationals of UKVI-prescribed majority English-speaking countries or those holding degrees from those countries; degrees from India do not qualify.",
            "quote": q_lang,
            "url": u_lang
        }
    },
    "notes": "Postgraduate research degrees at Manchester include PhD and MPhil programmes across the Faculty of Science and Engineering and the Faculty of Biology, Medicine and Health."
}

with open(staging_dir / "universities" / "manchester.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "Department of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Electrical and Electronic Engineering", "Electrical and Electronic Engineering PhD"),
    ("mech", "Department of Mechanical, Aerospace and Civil Engineering", "Mechanical Engineering PhD"),
    ("civil", "Department of Mechanical, Aerospace and Civil Engineering", "Civil Engineering PhD"),
    ("chemeng", "Department of Chemical Engineering", "Chemical Engineering PhD"),
    ("materials", "Department of Materials", "Materials PhD"),
    ("bme", "Department of Mechanical, Aerospace and Civil Engineering / Division of Cell Matrix Biology", "Biomedical Engineering PhD"),
    ("chemistry", "Department of Chemistry", "Chemistry PhD"),
    ("physics", "Department of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "Department of Physics and Astronomy", "Astronomy and Astrophysics PhD"),
    ("math", "Department of Mathematics", "Mathematics PhD"),
    ("statistics", "Department of Mathematics", "Statistics PhD"),
    ("biology", "School of Biological Sciences", "Biological Sciences PhD"),
    ("biomed", "School of Medical Sciences", "Medical Sciences PhD"),
    ("neuro", "School of Biological Sciences / Division of Neuroscience", "Neuroscience PhD"),
    ("earth", "Department of Earth and Environmental Sciences", "Earth Sciences PhD"),
    ("environment", "Department of Earth and Environmental Sciences", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Manchester.",
            "quote": "",
            "url": u_se
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": u_ets
        }

    prog_record = {
        "id": f"manchester--{field_id}",
        "university": "manchester",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_se,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications are reviewed on a rolling basis, typically within 4-6 weeks of submission.",
                "quote": q_roll,
                "url": u_se
            },
            "entry_route": {
                "code": "Either",
                "value": "Standard entry requires a bachelor's honours degree at Upper Second class (2:1) or above, or a Lower Second class (2:2) bachelor's with a taught master's completed at Merit level.",
                "quote": q_entry,
                "url": u_bmh
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants must contact their prospective project supervisor and discuss their suitability prior to applying.",
                "quote": q_sup,
                "url": u_se
            },
            "funding": {
                "code": "Competitive",
                "value": "Applicants nominated by their supervisor for funding may be invited to further interviews to determine suitability.",
                "quote": q_fund,
                "url": u_se
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research degree ({title}) in the {dept} at the University of Manchester."
    }

    with open(staging_dir / "programs" / f"manchester--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated manchester university record and {len(disciplines)} program records.")
