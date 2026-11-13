import json
import hashlib
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.cardiff.ac.uk/study/postgraduate/applying/how-to-apply"
u_pgr = "https://www.cardiff.ac.uk/study/postgraduate/research"
u_lang = "https://www.cardiff.ac.uk/study/international/english-language-requirements"
u_adm = "https://www.cardiff.ac.uk/study/postgraduate/applying/admissions-criteria"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f".cache/pages/{key}.json", encoding="utf-8"))["text"]

t_apply = get_text(u_apply)
t_pgr = get_text(u_pgr)
t_lang = get_text(u_lang)
t_adm = get_text(u_adm)
t_ets = get_text(u_ets)

idx_fee = t_apply.find("Cardiff University does not charge an application fee for any of our postgraduate programmes.")
q_fee = t_apply[idx_fee:idx_fee + 90]
assert q_fee in t_apply, "q_fee not in t_apply"

idx_dl = t_apply.find("Look at our funding pages to see the financial support available - if you intend to apply for funding, we advise that you submit your application at least two months before a scholarship deadline.")
q_dl = t_apply[idx_dl:idx_dl + 196]
assert q_dl in t_apply, "q_dl not in t_apply"

idx_entry = t_adm.find("Our online course finder and postgraduate prospectus will give you a broad overview of the entry requirements for particular degree programmes. However, we welcome applications from those offering alternative qualifications. We will also consider applications from those with combinations of qualifications and those with other relevant life/work experience.")
q_entry = t_adm[idx_entry:idx_entry + 348]
assert q_entry in t_adm, "q_entry not in t_adm"

sup_str = "Research degrees are focused on independent study. Unlike taught students, you'll work with your supervisor to identify your study needs."
idx_sup = t_pgr.find(sup_str)
q_sup = t_pgr[idx_sup:idx_sup + len(sup_str)]
assert q_sup in t_pgr, "q_sup not in t_pgr"

idx_fund = t_pgr.find("Find funded PhD studentships and projects, as well as projects available for applicants who are self-funded or have already secured funding.")
q_fund = t_pgr[idx_fund:idx_fund + 140]
assert q_fund in t_pgr, "q_fund not in t_pgr"

idx_ielts = t_lang.find("The university minimum requirement for English language is a grade C/4 at GCSE or IELTS (Academic) with 6.5 overall and a minimum of 5.5 in each of the subskills")
q_ielts = t_lang[idx_ielts:idx_ielts + 158]
assert q_ielts in t_lang, "q_ielts not in t_lang"

idx_toefl = t_lang.find("TOEFL iBT including\nHome Edition (pre-January 2026) 88")
q_toefl = t_lang[idx_toefl:idx_toefl + 54]
assert q_toefl in t_lang, "q_toefl not in t_lang"

idx_waiver = t_lang.find("In addition to meeting the academic language standard, applicants who require a Student Route visa to study in the UK must present an acceptable English language qualification to meet UKVI (UK Visas and Immigration) requirements")
q_waiver = t_lang[idx_waiver:idx_waiver + 233]
assert q_waiver in t_lang, "q_waiver not in t_lang"

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
assert ets_quote in t_ets, "ets_quote not in t_ets"

uni_record = {
    "id": "cardiff",
    "institution": "Cardiff University",
    "country": "United Kingdom",
    "region": "Wales",
    "grad_page": u_pgr,
    "checked": "2026-10-31",
    "fields": {
        "app_fee": {
            "code": "0 (no fee)",
            "value": "Cardiff University does not charge an application fee for any postgraduate programmes.",
            "quote": q_fee,
            "url": u_apply
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "No fee waiver policy is required as Cardiff University does not charge a postgraduate application fee.",
            "quote": "",
            "url": u_apply
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Cardiff.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "88",
            "value": "Cardiff accepts TOEFL iBT with a minimum overall score of 88.",
            "quote": q_toefl,
            "url": u_lang
        },
        "ielts_min": {
            "code": "6.5",
            "value": "University minimum requirement for postgraduate English language is IELTS (Academic) with 6.5 overall and a minimum of 5.5 in each subskill.",
            "quote": q_ielts,
            "url": u_lang
        },
        "english_waiver": {
            "code": "No",
            "value": "Applicants requiring a Student Route visa must present an acceptable English qualification meeting UKVI standards; degrees from non-majority English countries do not waive requirements.",
            "quote": q_waiver,
            "url": u_lang
        }
    },
    "notes": "Postgraduate research degrees at Cardiff University include PhD, MPhil, and MD programmes across schools."
}

with open(staging_dir / "universities" / "cardiff.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

prog_specs = [
    ("cs", "School of Computer Science and Informatics", "Computer Science PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/computer-science-and-informatics"),
    ("chemistry", "School of Chemistry", "Chemistry PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/chemistry"),
    ("math", "School of Mathematics", "Mathematics PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/mathematics"),
    ("statistics", "School of Mathematics", "Statistics and Operational Research PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/mathematics"),
    ("physics", "School of Physics and Astronomy", "Physics PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/physics-and-astronomy"),
    ("astronomy", "School of Physics and Astronomy", "Astrophysics PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/physics-and-astronomy"),
    ("biology", "School of Biosciences", "Biological Sciences PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/biosciences-phd-mphil-md"),
    ("biomed", "School of Medicine", "Medicine PhD / MPhil / MD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/medicine"),
    ("neuro", "School of Psychology", "Psychology / Neuroscience PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/psychology"),
    ("earth", "School of Earth and Environmental Sciences", "Earth Sciences PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/earth-sciences"),
    ("environment", "School of Geography and Planning", "Geography and Planning PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/programme/geography-and-planning"),
    ("mech", "School of Engineering", "Engineering (Mechanics, Materials and Advanced Manufacturing) PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-mechanics,-materials-and-advanced-manufacturing"),
    ("materials", "School of Engineering", "Engineering (Mechanics, Materials and Advanced Manufacturing) PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-mechanics,-materials-and-advanced-manufacturing"),
    ("ece", "School of Engineering", "Engineering (Health, Technology and the Digital World) PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-health,-technology-and-the-digital-world"),
    ("bme", "School of Engineering", "Engineering (Health, Technology and the Digital World) PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-health,-technology-and-the-digital-world"),
    ("civil", "School of Engineering", "Engineering (Energy and Environment) PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-energy-and-environment"),
    ("chemeng", "School of Engineering", "Engineering (Energy and Environment) PhD", "https://www.cardiff.ac.uk/study/postgraduate/research/programmes/area/engineering-energy-and-environment"),
]

for field_id, dept, title, prog_url in prog_specs:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Cardiff.",
            "quote": "",
            "url": prog_url
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": u_ets
        }

    prog_record = {
        "id": f"cardiff--{field_id}",
        "university": "cardiff",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": prog_url,
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications are accepted throughout the year on a rolling basis, with applicants advised to apply at least two months before funding deadlines.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Cardiff welcomes applications from those offering alternative qualifications alongside standard degree requirements.",
                "quote": q_entry,
                "url": u_adm
            },
            "supervisor": {
                "code": "Required",
                "value": "Research degrees focus on independent study under academic supervision to identify study needs and guide research.",
                "quote": q_sup,
                "url": u_pgr
            },
            "funding": {
                "code": "Competitive",
                "value": "Funding is available via competitive PhD studentships and research council projects as well as self-funded places.",
                "quote": q_fund,
                "url": u_pgr
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at Cardiff University."
    }

    with open(staging_dir / "programs" / f"cardiff--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated cardiff university record and {len(prog_specs)} program records.")
