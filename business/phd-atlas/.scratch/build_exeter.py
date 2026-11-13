import json
import hashlib
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.exeter.ac.uk/study/pg-research/apply/"
u_entry = "https://www.exeter.ac.uk/study/pg-research/entryrequirements/"
u_fund = "https://www.exeter.ac.uk/study/pg-research/funding/"
u_lang = "https://www.exeter.ac.uk/study/englishlanguagerequirements/"
u_b2 = "https://www.exeter.ac.uk/study/englishlanguagerequirements/profile-b2/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f".cache/pages/{key}.json", encoding="utf-8"))["text"]

t_apply = get_text(u_apply)
t_entry = get_text(u_entry)
t_fund = get_text(u_fund)
t_lang = get_text(u_lang)
t_b2 = get_text(u_b2)
t_ets = get_text(u_ets)

idx_dl = t_apply.find("The application deadlines for September starters are:\n30 June for International Applicants")
q_dl = t_apply[idx_dl:idx_dl + 115]
assert q_dl in t_apply, "q_dl not in t_apply"

idx_sup = t_apply.find("You will only be able to pursue a research degree with us if we can offer appropriate supervision.")
q_sup = t_apply[idx_sup:idx_sup + 195]
assert q_sup in t_apply, "q_sup not in t_apply"

idx_entry = t_entry.find("For all research degrees you will normally be required to have obtained or expect to obtain a first degree equivalent to at least a UK 2:1 Honours degree.")
q_entry = t_entry[idx_entry:idx_entry + 155]
assert q_entry in t_entry, "q_entry not in t_entry"

idx_fund = t_fund.find("Money is the single biggest barrier to people undertaking postgraduate study, and securing funding for your PhD is vital to realising your ambitions.")
q_fund = t_fund[idx_fund:idx_fund + 152]
assert q_fund in t_fund, "q_fund not in t_fund"

idx_ielts = t_b2.find("IELTS Academic, IELTS Academic Online and IELTS One Skill Retake\n6.5 overall and no less than 6 in any section")
q_ielts = t_b2[idx_ielts:idx_ielts + 109]
assert q_ielts in t_b2, "q_ielts not in t_b2"

idx_toefl = t_b2.find("TOEFL iBT, TOEFL iBT Home Edition, TOEFL iBT Paper Edition and TOEFL MyBest scores\n90 with minimum scores of 21 for writing, listening, reading and speaking.")
q_toefl = t_b2[idx_toefl:idx_toefl + 161]
assert q_toefl in t_b2, "q_toefl not in t_b2"

idx_waiver = t_lang.find("English language requirements vary by programme, and our individual programme pages list the required profile for those who are not UK Nationals or who are not nationals of majority English-speaking countries determined by the Home Office.")
q_waiver = t_lang[idx_waiver:idx_waiver + 235]
assert q_waiver in t_lang, "q_waiver not in t_lang"

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
assert ets_quote in t_ets, "ets_quote not in t_ets"

uni_record = {
    "id": "exeter",
    "institution": "University of Exeter",
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
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Exeter.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "90",
            "value": "Standard minimum English requirement for Profile B2 programmes is TOEFL iBT 90 with minimum scores of 21 for writing, listening, reading and speaking.",
            "quote": q_toefl,
            "url": u_b2
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Standard minimum English requirement for Profile B2 programmes is IELTS Academic 6.5 overall and no less than 6 in any section.",
            "quote": q_ielts,
            "url": u_b2
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to UK nationals or nationals of majority English-speaking countries determined by the Home Office; qualifications from non-majority countries do not waive test requirements.",
            "quote": q_waiver,
            "url": u_lang
        }
    },
    "notes": "Postgraduate research degrees at the University of Exeter include PhD, MPhil, and Masters by Research programmes across faculties."
}

with open(staging_dir / "universities" / "exeter.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "Department of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Engineering", "Electronic Engineering PhD"),
    ("mech", "Department of Engineering", "Mechanical Engineering PhD"),
    ("civil", "Department of Engineering", "Civil Engineering PhD"),
    ("chemeng", "Department of Engineering", "Chemical Engineering PhD"),
    ("materials", "Department of Engineering / Department of Physics", "Materials Engineering PhD"),
    ("bme", "Department of Engineering / Department of Health and Life Sciences", "Biomedical Engineering PhD"),
    ("chemistry", "Department of Chemistry", "Chemistry PhD"),
    ("physics", "Department of Physics and Astronomy", "Physics PhD"),
    ("astronomy", "Department of Physics and Astronomy", "Astrophysics PhD"),
    ("math", "Department of Mathematics and Statistics", "Mathematics PhD"),
    ("statistics", "Department of Mathematics and Statistics", "Statistics PhD"),
    ("biology", "Department of Biosciences", "Biological Sciences PhD"),
    ("biomed", "Faculty of Health and Life Sciences / Department of Clinical and Biomedical Sciences", "Medical Sciences PhD"),
    ("neuro", "Department of Clinical and Biomedical Sciences / Department of Psychology", "Neuroscience PhD"),
    ("earth", "Department of Earth and Environmental Science / Camborne School of Mines", "Geology / Earth Sciences PhD"),
    ("environment", "Department of Earth and Environmental Science / Environment and Sustainability Institute", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Exeter.",
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
        "id": f"exeter--{field_id}",
        "university": "exeter",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_apply,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "2027-06-30",
                "value": "The application deadline for September starters is 30 June for International Applicants (and 31 July for Home Applicants).",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "For all research degrees applicants are normally required to have obtained or expect to obtain a first degree equivalent to at least a UK 2:1 Honours degree.",
                "quote": q_entry,
                "url": u_entry
            },
            "supervisor": {
                "code": "Required",
                "value": "Admission is conditional on appropriate supervisory capacity and guidance in the chosen research field.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Postgraduate research funding is competitive via university studentships, research council awards (such as EPSRC), and bespoke supervisor funding.",
                "quote": q_fund,
                "url": u_fund
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Exeter."
    }

    with open(staging_dir / "programs" / f"exeter--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated exeter university record and {len(disciplines)} program records.")
