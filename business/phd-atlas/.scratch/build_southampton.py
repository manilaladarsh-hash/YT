import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.southampton.ac.uk/study/postgraduate-research/apply"
u_fund = "https://www.southampton.ac.uk/study/postgraduate-research/funding"
u_eng = "https://www.southampton.ac.uk/international/english-language-requirements"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

# Load cached texts
p_apply = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_apply][0]
t_apply = json.load(open(p_apply, encoding="utf-8"))["text"]

p_fund = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_fund][0]
t_fund = json.load(open(p_fund, encoding="utf-8"))["text"]

p_eng = [p for p in Path(".cache/pages").glob("*.json") if json.load(open(p, encoding="utf-8")).get("url") == u_eng][0]
t_eng = json.load(open(p_eng, encoding="utf-8"))["text"]

# Slices
idx_entry = t_apply.find("an academic transcript of your undergraduate degree")
q_entry = t_apply[idx_entry:t_apply.find("(if you have already graduated)", idx_entry) + len("(if you have already graduated)")]

idx_sup = t_apply.find("supervisor name (you should speak to the supervisor before applying)")
q_sup = t_apply[idx_sup:idx_sup + len("supervisor name (you should speak to the supervisor before applying)")]

idx_dl = t_apply.find("You should apply as early as possible if you need to secure a UK visa")
q_dl = t_apply[idx_dl:t_apply.find("in advance of the start date.", idx_dl) + len("in advance of the start date.")]

idx_fund = t_fund.find("For projects advertised as 'fully funded' or 'competition funded'")
q_fund = t_fund[idx_fund:t_fund.find("apply for additional funding.", idx_fund) + len("apply for additional funding.")]

q_waiver = "If you are from a majority English-speaking country you do not need to provide evidence of your English language proficiency."
q_band = "Each course has its own English language proficiency requirement, expressed as an English language band (A to I) and its International English Language Testing System (IELTS) equivalent. Your offer letter will tell you which band you need to meet."

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

assert q_entry in t_apply, "q_entry not in t_apply"
assert q_sup in t_apply, "q_sup not in t_apply"
assert q_dl in t_apply, "q_dl not in t_apply"
assert q_fund in t_fund, "q_fund not in t_fund"
assert q_waiver in t_eng, "q_waiver not in t_eng"
assert q_band in t_eng, "q_band not in t_eng"

uni_record = {
    "id": "southampton",
    "institution": "University of Southampton",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_apply,
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Central research degree application guidance publishes no application fee for postgraduate research degrees; applications are submitted online.",
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
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Southampton.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "English language requirements vary by programme band (Bands A to I); specific requirements are detailed on individual course and project pages.",
            "quote": q_band,
            "url": u_eng
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "English language requirements vary by programme band (Bands A to I); specific requirements are detailed on individual course and project pages.",
            "quote": q_band,
            "url": u_eng
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to applicants from a recognised majority English-speaking country; other international applicants must provide evidence of proficiency.",
            "quote": q_waiver,
            "url": u_eng
        }
    },
    "notes": "Postgraduate research degrees at the University of Southampton include PhD and Integrated PhD programmes across faculties."
}

with open(staging_dir / "universities" / "southampton.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "School of Electronics and Computer Science", "Computer Science PhD"),
    ("ece", "School of Electronics and Computer Science", "Electronic and Electrical Engineering PhD"),
    ("mech", "School of Engineering", "Mechanical Engineering PhD"),
    ("civil", "School of Engineering", "Civil Engineering PhD"),
    ("chemeng", "School of Engineering / School of Chemistry", "Chemical Engineering PhD"),
    ("materials", "School of Engineering", "Materials Science PhD"),
    ("bme", "School of Engineering / School of Biological Sciences", "Biomedical Engineering PhD"),
    ("chemistry", "School of Chemistry", "Chemistry PhD"),
    ("physics", "School of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "School of Physics and Astronomy", "Astronomy PhD"),
    ("math", "School of Mathematical Sciences", "Mathematical Sciences PhD"),
    ("statistics", "School of Mathematical Sciences", "Statistics PhD"),
    ("biology", "School of Biological Sciences", "Biological Sciences PhD"),
    ("biomed", "Faculty of Medicine", "Medical Sciences PhD"),
    ("neuro", "School of Biological Sciences / Faculty of Medicine", "Neuroscience PhD"),
    ("earth", "School of Ocean and Earth Science", "Ocean and Earth Science PhD"),
    ("environment", "School of Geography and Environmental Science", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Southampton.",
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
        "id": f"southampton--{field_id}",
        "university": "southampton",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_apply,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Research applications operate on a rolling basis; applicants should apply as early as possible (funding deadlines are usually at least 6 months prior to start).",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Applicants present undergraduate and (if graduated) Master's transcripts and degree certificates.",
                "quote": q_entry,
                "url": u_apply
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants are required to name their proposed supervisor and speak to them prior to submitting an application.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Funded and competition-funded research projects cover tuition fees and stipends through competitive review.",
                "quote": q_fund,
                "url": u_fund
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Southampton."
    }

    with open(staging_dir / "programs" / f"southampton--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated southampton university record and {len(disciplines)} program records.")
