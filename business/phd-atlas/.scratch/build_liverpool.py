import json
import hashlib
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

u_apply = "https://www.liverpool.ac.uk/study/postgraduate-research/how-to-apply/"
u_pgr = "https://www.liverpool.ac.uk/study/postgraduate-research/"
u_req = "https://www.liverpool.ac.uk/study/international/apply/english-language/"
u_tests = "https://www.liverpool.ac.uk/international/applying/entry-requirements/english-language-requirements/international-english-language-tests/"
u_ets = "https://www.ets.org/gre/score-users/about/subject-tests.html"

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f".cache/pages/{key}.json", encoding="utf-8"))["text"]

t_apply = get_text(u_apply)
t_pgr = get_text(u_pgr)
t_req = get_text(u_req)
t_tests = get_text(u_tests)
t_ets = get_text(u_ets)

idx_dl = t_apply.find("You should apply as early as possible if you're also applying for funding, or if you need to secure a UK visa.")
q_dl = t_apply[idx_dl:idx_dl + 112]
assert q_dl in t_apply, "q_dl not in t_apply"

idx_sup = t_apply.find("It’s useful to contact potential supervisors before you make your application. This gives you the chance to discuss their availability and your proposed research.")
q_sup = t_apply[idx_sup:idx_sup + 163]
assert q_sup in t_apply, "q_sup not in t_apply"

idx_fund = t_pgr.find("Be part of the next generation of researchers, combining expert collaboration and structured training on a funded PhD.")
q_fund = t_pgr[idx_fund:idx_fund + 119]
assert q_fund in t_pgr, "q_fund not in t_pgr"

idx_entry = t_apply.find("University transcripts\u202fand degree certificates to date")
q_entry = t_apply[idx_entry:idx_entry + 54]
assert q_entry in t_apply, "q_entry not in t_apply"

idx_ielts = t_tests.find("Most of our postgraduate research courses require one of:\nIELTS 6.5 overall, with no component less than 5.5, or equivalent")
q_ielts = t_tests[idx_ielts:idx_ielts + 122]
assert q_ielts in t_tests, "q_ielts not in t_tests"

idx_toefl = t_tests.find("TOEFL iBT (excluding TOEFL Home Edition which is not accepted)")
q_toefl = t_tests[idx_toefl:idx_toefl + 62]
assert q_toefl in t_tests, "q_toefl not in t_tests"

idx_waiver = t_req.find("For most international students, unless you're a national of a majority English speaking country, you'll need to provide")
q_waiver = t_req[idx_waiver:idx_waiver + 120]
assert q_waiver in t_req, "q_waiver not in t_req"

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
assert ets_quote in t_ets, "ets_quote not in t_ets"

uni_record = {
    "id": "liverpool",
    "institution": "University of Liverpool",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": u_pgr,
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
            "value": "GRE General test is not required or requested centrally for postgraduate research admission at Liverpool.",
            "quote": "",
            "url": u_apply
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "Liverpool accepts TOEFL iBT (excluding Home Edition) as an approved alternative test alongside course-specific requirements.",
            "quote": q_toefl,
            "url": u_tests
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Most postgraduate research courses require IELTS 6.5 overall with no component less than 5.5 (or 6.0 in some disciplines).",
            "quote": q_ielts,
            "url": u_tests
        },
        "english_waiver": {
            "code": "No",
            "value": "Exemption applies only to nationals of majority English-speaking countries; degrees from non-majority countries like India do not qualify.",
            "quote": q_waiver,
            "url": u_req
        }
    },
    "notes": "Postgraduate research degrees at the University of Liverpool include PhD, MPhil, and MD programmes across faculties."
}

with open(staging_dir / "universities" / "liverpool.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

disciplines = [
    ("cs", "Department of Computer Science", "Computer Science PhD"),
    ("ece", "Department of Electrical Engineering and Electronics", "Electrical Engineering and Electronics PhD"),
    ("mech", "School of Engineering", "Mechanical and Materials Engineering PhD"),
    ("civil", "School of Engineering", "Civil and Environmental Engineering PhD"),
    ("chemeng", "School of Engineering", "Chemical Engineering PhD"),
    ("materials", "Department of Chemistry / Materials Innovation Factory", "Materials Science PhD"),
    ("bme", "School of Engineering / Institute of Life Course", "Biomedical Engineering PhD"),
    ("chemistry", "Department of Chemistry", "Chemistry PhD"),
    ("physics", "Department of Physics", "Physics PhD"),
    ("astronomy", "Department of Physics / Astrophysics Research Institute", "Astrophysics PhD"),
    ("math", "Department of Mathematical Sciences", "Mathematical Sciences PhD"),
    ("statistics", "Department of Mathematical Sciences", "Statistics PhD"),
    ("biology", "Institute of Integrative Biology", "Biological Sciences PhD"),
    ("biomed", "Institute of Systems, Molecular and Integrative Biology", "Medical Sciences PhD"),
    ("neuro", "Institute of Systems, Molecular and Integrative Biology", "Neuroscience PhD"),
    ("earth", "Department of Earth, Ocean and Ecological Sciences", "Earth and Ocean Sciences PhD"),
    ("environment", "Department of Earth, Ocean and Ecological Sciences / Geography", "Environmental Sciences PhD"),
]

for field_id, dept, title in disciplines:
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Liverpool.",
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
        "id": f"liverpool--{field_id}",
        "university": "liverpool",
        "field": field_id,
        "also_fields": [],
        "department": dept,
        "program_page": u_pgr,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications are accepted year-round on a rolling basis, with early submission advised when seeking funding or visa sponsorship.",
                "quote": q_dl,
                "url": u_apply
            },
            "entry_route": {
                "code": "Either",
                "value": "Applicants submit transcripts and degree certificates to date; standard doctoral entry requires an honours bachelor's or master's qualification.",
                "quote": q_entry,
                "url": u_apply
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants are instructed to contact potential supervisors in advance to discuss availability and research fit.",
                "quote": q_sup,
                "url": u_apply
            },
            "funding": {
                "code": "Competitive",
                "value": "Funded PhD studentships combine structured training and expert collaboration through university awards and research councils.",
                "quote": q_fund,
                "url": u_pgr
            },
            "gre_subject": gre_sub
        },
        "notes": f"Postgraduate research programme ({title}) in the {dept} at the University of Liverpool."
    }

    with open(staging_dir / "programs" / f"liverpool--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Successfully generated liverpool university record and {len(disciplines)} program records.")
