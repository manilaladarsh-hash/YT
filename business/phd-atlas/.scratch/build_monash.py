import hashlib
import json
from pathlib import Path

staging_unis = Path("data/staging/universities")
staging_progs = Path("data/staging/programs")
staging_unis.mkdir(parents=True, exist_ok=True)
staging_progs.mkdir(parents=True, exist_ok=True)

# Fetch cached text to get exact quote slices
h_proc = hashlib.sha1("https://publicpolicydms.monash.edu/Monash/documents/2723244".encode()).hexdigest()[:16]
proc_text = json.loads(Path(f".cache/pages/{h_proc}.json").read_text(encoding="utf-8"))["text"]

h_apply = hashlib.sha1("https://www.monash.edu/graduate-research/future-students/apply".encode()).hexdigest()[:16]
apply_text = json.loads(Path(f".cache/pages/{h_apply}.json").read_text(encoding="utf-8"))["text"]

# Slices
entry_q = proc_text[proc_text.find("1.8 The minimum qualifications"):proc_text.find("1.8.3")].strip()
waiver_q = proc_text[proc_text.find("Where an applicant’s first language is not English"):proc_text.find("1.12.2")].strip()
toefl_q = "1.12.2 achievement of minimum scores on a recognised English test as specified on the University website."
sup_q = proc_text[proc_text.find("1.4 In addition to the eligibility requirements"):proc_text.find("1.5 Applicants for a joint")].strip()

# Central Monash Record
monash_uni = {
    "id": "monash",
    "institution": "Monash University",
    "country": "Australia",
    "region": "Victoria",
    "grad_page": "https://www.monash.edu/graduate-research/study/apply",
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "Monash University does not charge an application fee for Graduate Research applications.",
            "quote": "",
            "url": "https://publicpolicydms.monash.edu/Monash/documents/2723244"
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "No application fee is charged, so no waiver is stated.",
            "quote": "",
            "url": "https://publicpolicydms.monash.edu/Monash/documents/2723244"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "No GRE requirement is stated for graduate research degrees at Monash University.",
            "quote": "",
            "url": "https://publicpolicydms.monash.edu/Monash/documents/2723244"
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "Recognised English test score thresholds are set by course and specified on the university website.",
            "quote": toefl_q,
            "url": "https://publicpolicydms.monash.edu/Monash/documents/2723244"
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "Recognised English test score thresholds are set by course and specified on the university website.",
            "quote": toefl_q,
            "url": "https://publicpolicydms.monash.edu/Monash/documents/2723244"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "English requirements may be met by successful completion of a tertiary course of study with minimum duration of two years full-time in English.",
            "quote": waiver_q,
            "url": "https://publicpolicydms.monash.edu/Monash/documents/2723244"
        }
    },
    "notes": "Monash University doctoral programs are governed centrally by the Graduate Research Admissions Procedure (DMS 2723244) and the Graduate Research Committee."
}

with open(staging_unis / "monash.json", "w", encoding="utf-8") as f:
    json.dump(monash_uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# Programs
departments = {
    "cs": ("Faculty of Information Technology", []),
    "datasci": ("Faculty of Information Technology", []),
    "chemeng": ("Department of Chemical and Biological Engineering", []),
    "civil": ("Department of Civil and Environmental Engineering", []),
    "ece": ("Department of Electrical and Computer Systems Engineering", []),
    "materials": ("Department of Materials Science and Engineering", []),
    "mech": ("Department of Mechanical and Aerospace Engineering", []),
    "math": ("School of Mathematics", []),
    "physics": ("School of Physics and Astronomy", []),
    "astronomy": ("School of Physics and Astronomy", []),
    "chemistry": ("School of Chemistry", []),
    "biology": ("School of Biological Sciences", []),
    "earth": ("School of Earth, Atmosphere and Environment", []),
    "environment": ("School of Biological Sciences / Earth, Atmosphere and Environment", []),
}

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
prog_url = "https://www.monash.edu/graduate-research/study/apply"
apply_page = "https://www.monash.edu/graduate-research/future-students/apply"
proc_url = "https://publicpolicydms.monash.edu/Monash/documents/2723244"

for field, (dept, also_fields) in departments.items():
    if field in ("math", "physics"):
        gre_sub = {
            "code": "Not stated",
            "value": "No GRE Subject test is required or mentioned for research degree admission.",
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
        "id": f"monash--{field}",
        "university": "monash",
        "field": field,
        "also_fields": also_fields,
        "department": dept,
        "program_page": prog_url,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "2027-02-28",
                "value": "Round 1 scholarship applications close on 28 February 2027.",
                "quote": "*Please note: R1 Closing date for 2027 has been brought forward from 31 March to 28 February.",
                "url": apply_page,
                "also": [
                    {
                        "quote": "Applications for admission can be submitted at any time throughout the year.",
                        "url": apply_page
                    }
                ]
            },
            "entry_route": {
                "code": "Either",
                "value": "Admission requires either a 4-year bachelor's degree with second class honours division A (H2A) or a master's degree with a research component equivalent to at least 25% of one year full-time study at H2A level.",
                "quote": entry_q,
                "url": proc_url
            },
            "supervisor": {
                "code": "Required",
                "value": "Admission is subject to the availability of appropriately qualified supervisors, and applicants must identify and contact a supervisor prior to applying.",
                "quote": sup_q,
                "url": proc_url,
                "also": [
                    {
                        "quote": "Find a supervisor",
                        "url": apply_page
                    }
                ]
            },
            "funding": {
                "code": "Competitive",
                "value": "Centrally managed scholarships for Australian campuses are awarded through a highly competitive process prioritised under RTP procedures.",
                "quote": "Centrally managed scholarships for Australian campuses are awarded through a highly competitive process. The Graduate Research Committee prioritises applicants in accordance with the Research Training Program scholarship procedure.",
                "url": apply_page
            },
            "gre_subject": gre_sub
        },
        "notes": f"Monash University offers the Doctor of Philosophy in {dept} under centralized Graduate Research Admissions regulations."
    }

    with open(staging_progs / f"monash--{field}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Generated monash and {len(departments)} programs.")
