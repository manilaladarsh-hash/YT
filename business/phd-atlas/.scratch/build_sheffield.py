import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.sheffield.ac.uk/postgraduate/phd/apply"
u_eng = "https://www.sheffield.ac.uk/postgraduate/english-language"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

# Load cached texts
p_apply = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_apply][0]
t_apply = json.load(open(p_apply, encoding="utf-8"))["text"]

p_eng = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_eng][0]
t_eng = json.load(open(p_eng, encoding="utf-8"))["text"]

# Slice exact quotes from cached text
idx_entry = t_apply.find("Information about academic entry requirements")
q_entry = t_apply[idx_entry:t_apply.find("Find A PhD page.", idx_entry) + len("Find A PhD page.")]

idx_sup = t_apply.find("If you want to research your own idea")
q_sup = t_apply[idx_sup:t_apply.find("like to study.", idx_sup) + len("like to study.")]

idx_dl = t_apply.find("Although we advise students to start")
q_dl = t_apply[idx_dl:t_apply.find("academic school.", idx_dl) + len("academic school.")]

idx_fund = t_apply.find("Search for PhD opportunities at Sheffield")
q_fund = t_apply[idx_fund:t_apply.find("Find a project or supervisor", idx_fund) + len("Find a project or supervisor")]

idx_waiver = t_eng.find("If you have recently been awarded a first degree or postgraduate diploma taught in English")
q_waiver = t_eng[idx_waiver:t_eng.find("start date of your Sheffield course.", idx_waiver) + len("start date of your Sheffield course.")]

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

assert q_entry in t_apply, "q_entry not in t_apply"
assert q_sup in t_apply, "q_sup not in t_apply"
assert q_dl in t_apply, "q_dl not in t_apply"
assert q_fund in t_apply, "q_fund not in t_apply"
assert q_waiver in t_eng, "q_waiver not in t_eng"

uni_record = {
    "id": "sheffield",
    "institution": "University of Sheffield",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_apply,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research guidance lists tuition fee lookup and scholarship funding with no general application fee stated for postgraduate research degrees.",
            "quote": "",
            "url": u_apply
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Central research guidance does not publish fee waiver procedures as no general PGR application fee is stated.",
            "quote": "",
            "url": u_apply
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Sheffield.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "English language requirements vary depending on what you study; requirements for research degrees are published on specific PhD course webpages.",
            "quote": "The IELTS requirements for research degrees are published on our PhD webpages.",
            "url": u_eng
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "English language requirements vary depending on what you study; requirements for research degrees are published on specific PhD course webpages.",
            "quote": "The IELTS requirements for research degrees are published on our PhD webpages.",
            "url": u_eng
        },
        "english_waiver": {
            "code": "No",
            "value": "Waivers apply to degrees taught in English in person in a majority native English speaking country; degrees from non-majority native English speaking countries require approved tests.",
            "quote": q_waiver,
            "url": u_eng
        }
    },
    "notes": "Postgraduate research degrees at the University of Sheffield include PhD, MPhil, and PhD with Integrated Masters programmes across faculties."
}

with open(staging_dir / "universities" / "sheffield.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "Department of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Electronic and Electrical Engineering", "Electronic and Electrical Engineering PhD"),
    ("mech", "Department of Mechanical Engineering", "Mechanical Engineering PhD"),
    ("civil", "Department of Civil and Structural Engineering", "Civil and Structural Engineering PhD"),
    ("chemeng", "Department of Chemical and Biological Engineering", "Chemical and Biological Engineering PhD"),
    ("materials", "Department of Materials Science and Engineering", "Materials Science and Engineering PhD"),
    ("bme", "Department of Chemical and Biological Engineering / School of Medicine", "Bioengineering PhD"),
    ("chemistry", "Department of Chemistry", "Chemistry PhD"),
    ("physics", "Department of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "Department of Physics and Astronomy", "Astrophysics PhD"),
    ("math", "School of Mathematics and Statistics", "Mathematics PhD"),
    ("statistics", "School of Mathematics and Statistics", "Statistics PhD"),
    ("biology", "School of Biosciences", "Biosciences PhD"),
    ("biomed", "School of Medicine and Population Health", "Biomedical Sciences PhD"),
    ("neuro", "Neuroscience Institute / School of Biosciences", "Neuroscience PhD"),
    ("earth", "School of Geography and Planning / Department of Multidisciplinary Engineering", "Earth Sciences PhD"),
    ("environment", "School of Geography and Planning / Energy Institute", "Environmental Science PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Sheffield.",
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
        "id": f"sheffield--{field_id}",
        "university": "sheffield",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_apply,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Students are advised to apply early; it is possible to start postgraduate research at any point in the year subject to school confirmation.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Entry requirements vary depending on what you study; some subjects require a master's degree, while others ask for a good undergraduate degree (2:1 or First).",
                "quote": q_entry,
                "url": u_apply
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants wishing to research their own idea must contact the relevant academic school before formal application to check supervisor availability.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "PhD opportunities and Centres for Doctoral Training offer competitive funding and research studentships.",
                "quote": q_fund,
                "url": u_apply
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Sheffield."
    }

    with open(staging_dir / "programs" / f"sheffield--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated sheffield university record and {len(disciplines)} program records.")
