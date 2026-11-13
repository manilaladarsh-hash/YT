import json, os

os.makedirs('data/staging/universities', exist_ok=True)
os.makedirs('data/staging/programs', exist_ok=True)

ets_subject_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_subject_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

rit_uni = {
    "id": "rit",
    "institution": "Rochester Institute of Technology",
    "country": "USA",
    "region": "New York",
    "grad_page": "https://www.rit.edu/admissions/graduate/apply",
    "checked": "2026-10-29",
    "notes": "",
    "fields": {
        "app_fee": {
            "code": "65 USD",
            "value": "$65 non-refundable application fee",
            "quote": "To be considered for graduate study, you are required to pay a non-refundable $65 application fee. Your application fee can be paid within your admissions portal after you submit your application.",
            "url": "https://www.rit.edu/admissions/graduate/application-instructions"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Waivers available for current RIT students and RIT alumni",
            "quote": "Current RIT students and RIT alumni are not required to pay the $65.00 application fee. The application fee will be waived within 24 hours of the submission of your application.",
            "url": "https://www.rit.edu/admissions/graduate/application-instructions"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Central graduate admissions does not set a campus-wide GRE requirement; requirements vary by academic degree program.",
            "quote": "Test Scores (GRE/GMAT) varies by program Test Score Requirements Only some degrees require a GMAT (Graduate Management Admissions Test) or GRE (Graduate Record Examination).",
            "url": "https://www.rit.edu/admissions/graduate/application-instructions"
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "Central graduate admissions does not set a single university-wide minimum TOEFL score; minimums are determined by each individual degree program in the deadlines and requirements table.",
            "quote": "View the overall minimum score requirement for your intended program in the graduate admission deadlines and requirements table.",
            "url": "https://www.rit.edu/admissions/graduate/application-instructions"
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "Central graduate admissions does not set a single university-wide minimum IELTS score; minimums are determined by each individual degree program in the deadlines and requirements table.",
            "quote": "View the overall minimum score requirement for your intended program in the graduate admission deadlines and requirements table.",
            "url": "https://www.rit.edu/admissions/graduate/application-instructions"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "International applicants may be considered for a waiver if they have worked or studied in the U.S. for the last two years.",
            "quote": "International Applicants may be considered for a waiver of an english language proficiency exam if:\nThey have worked or studied in the U.S. for the last two years",
            "url": "https://www.rit.edu/admissions/graduate/application-instructions"
        }
    }
}

with open('data/staging/universities/rit.json', 'w', encoding='utf-8') as f:
    json.dump(rit_uni, f, indent=2)

print("Saved rit.json")

funding_quote = "Ph.D. students typically receive full tuition and an RIT Graduate Assistantship that will consist of a research assistantship (stipend) or a teaching assistantship (salary)."

programs_def = [
    {
        "field": "physics",
        "also_fields": [],
        "department": "School of Physics and Astronomy",
        "program_page": "https://www.rit.edu/study/physics-phd",
        "deadline_code": "2026-12-31",
        "deadline_val": "December 31 standard deadline for fall admission",
        "deadline_quote": "December 31 standard deadline",
        "gre_code": "Optional",
        "gre_val": "GRE is optional",
        "gre_quote": "Entrance exam requirements:\nGRE optional",
        "gre_sub_code": "Not stated",
        "gre_sub_val": "GRE subject test requirement is not stated on physics PhD page.",
        "gre_sub_quote": "",
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty advisor agreement is not stated as required.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is standard.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college in physical sciences or engineering.",
        "toefl": "94",
        "toefl_quote": "TOEFL: 94/5",
        "ielts": "7.0",
        "ielts_quote": "IELTS: 7.0"
    },
    {
        "field": "astronomy",
        "also_fields": ["physics"],
        "department": "School of Physics and Astronomy",
        "program_page": "https://www.rit.edu/study/astrophysical-sciences-and-technology-phd",
        "deadline_code": "2027-01-15",
        "deadline_val": "January 15 standard deadline for fall admission",
        "deadline_quote": "January 15 standard deadline",
        "gre_code": "Not required",
        "gre_val": "Entrance exams are not required",
        "gre_quote": "Entrance exam requirements:",
        "gre_sub_code": "Not stated",
        "gre_sub_val": "GRE subject test requirement is not stated.",
        "gre_sub_quote": "",
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty advisor agreement is not stated as required.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "79",
        "toefl_quote": "TOEFL: 79/4.5",
        "ielts": "6.5",
        "ielts_quote": "IELTS: 6.5"
    },
    {
        "field": "math",
        "also_fields": ["statistics"],
        "department": "School of Mathematics and Statistics",
        "program_page": "https://www.rit.edu/study/mathematical-modeling-phd",
        "deadline_code": "2027-01-15",
        "deadline_val": "January 15 standard deadline for fall admission",
        "deadline_quote": "January 15 standard deadline",
        "gre_code": "Not required",
        "gre_val": "Entrance exams are not required",
        "gre_quote": "Entrance exam requirements:",
        "gre_sub_code": "Not stated",
        "gre_sub_val": "GRE subject test is not stated on program page.",
        "gre_sub_quote": "",
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty advisor agreement is not stated as required.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "100",
        "toefl_quote": "TOEFL: 100/5.5",
        "ielts": "7.5",
        "ielts_quote": "IELTS: 7.5"
    },
    {
        "field": "cs",
        "also_fields": ["datasci"],
        "department": "Golisano College of Computing and Information Sciences",
        "program_page": "https://www.rit.edu/study/computing-and-information-sciences-phd",
        "deadline_code": "2026-12-31",
        "deadline_val": "December 31 standard deadline for fall admission",
        "deadline_quote": "December 31 standard deadline",
        "gre_code": "Required",
        "gre_val": "GRE is required",
        "gre_quote": "GRE required",
        "gre_sub_code": "No subject test",
        "gre_sub_val": "ETS offers no Computer Science subject test.",
        "gre_sub_quote": ets_subject_quote,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "88",
        "toefl_quote": "TOEFL: 88/4.5",
        "ielts": "6.5",
        "ielts_quote": "IELTS: 6.5"
    },
    {
        "field": "ece",
        "also_fields": [],
        "department": "Kate Gleason College of Engineering",
        "program_page": "https://www.rit.edu/study/electrical-and-computer-engineering-phd",
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 standard deadline for fall admission",
        "deadline_quote": "December 15 standard deadline",
        "gre_code": "Optional",
        "gre_val": "GRE is optional but recommended",
        "gre_quote": "Entrance exam requirements:\nGRE optional but recommended",
        "gre_sub_code": "No subject test",
        "gre_sub_val": "ETS offers no Electrical/Computer Engineering subject test.",
        "gre_sub_quote": ets_subject_quote,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "94",
        "toefl_quote": "TOEFL: 94/5",
        "ielts": "7.0",
        "ielts_quote": "IELTS: 7.0"
    },
    {
        "field": "mech",
        "also_fields": [],
        "department": "Kate Gleason College of Engineering",
        "program_page": "https://www.rit.edu/study/mechanical-and-industrial-engineering-phd",
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 standard deadline for fall admission",
        "deadline_quote": "December 15 standard deadline",
        "gre_code": "Required",
        "gre_val": "GRE is required",
        "gre_quote": "Entrance exam requirements:\nGRE required",
        "gre_sub_code": "No subject test",
        "gre_sub_val": "ETS offers no Mechanical Engineering subject test.",
        "gre_sub_quote": ets_subject_quote,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "94",
        "toefl_quote": "TOEFL: 94/5",
        "ielts": "7.0",
        "ielts_quote": "IELTS: 7.0"
    },
    {
        "field": "bme",
        "also_fields": ["chemeng"],
        "department": "Kate Gleason College of Engineering",
        "program_page": "https://www.rit.edu/study/biomedical-and-chemical-engineering-phd",
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 standard deadline for fall admission",
        "deadline_quote": "December 15 standard deadline",
        "gre_code": "Optional",
        "gre_val": "GRE is optional but recommended",
        "gre_quote": "Entrance exam requirements:\nGRE optional but recommended",
        "gre_sub_code": "No subject test",
        "gre_sub_val": "ETS offers no Biomedical Engineering subject test.",
        "gre_sub_quote": ets_subject_quote,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "94",
        "toefl_quote": "TOEFL: 94/5",
        "ielts": "7.0",
        "ielts_quote": "IELTS: 7.0"
    },
    {
        "field": "materials",
        "also_fields": [],
        "department": "Kate Gleason College of Engineering",
        "program_page": "https://www.rit.edu/study/microsystems-engineering-phd",
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 standard deadline for fall admission",
        "deadline_quote": "December 15 standard deadline",
        "gre_code": "Optional",
        "gre_val": "GRE is optional but recommended",
        "gre_quote": "Entrance exam requirements:\nGRE optional but recommended",
        "gre_sub_code": "No subject test",
        "gre_sub_val": "ETS offers no Materials Engineering subject test.",
        "gre_sub_quote": ets_subject_quote,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college in the physical sciences or engineering.",
        "toefl": "94",
        "toefl_quote": "TOEFL: 94/5",
        "ielts": "7.0",
        "ielts_quote": "IELTS: 7.0"
    },
    {
        "field": "environment",
        "also_fields": [],
        "department": "Golisano Institute for Sustainability",
        "program_page": "https://www.rit.edu/study/sustainability-phd",
        "deadline_code": "2027-01-15",
        "deadline_val": "January 15 standard deadline for fall admission",
        "deadline_quote": "January 15 standard deadline",
        "gre_code": "Not required",
        "gre_val": "Entrance exams are not required",
        "gre_quote": "Entrance exam requirements:",
        "gre_sub_code": "No subject test",
        "gre_sub_val": "ETS offers no Environmental Science/Sustainability subject test.",
        "gre_sub_quote": ets_subject_quote,
        "supervisor_code": "Required",
        "supervisor_val": "Each faculty member in the Golisano Institute for Sustainability sponsors a select number of students for specific research projects; admission is tied to sponsored project acceptance.",
        "supervisor_quote": "Each faculty member in the Golisano Institute for Sustainability sponsors a select number of students for specific research projects, with the scope varying from fundamental science to applied engineering to corporate sustainability applications. On acceptance into a sponsored research project, you will receive a fully-funded education, a stipend to help with living expenses",
        "funding_code": "Guaranteed",
        "funding_val": "Fully-funded education with living stipend upon acceptance into sponsored research project.",
        "funding_quote": "On acceptance into a sponsored research project, you will receive a fully-funded education, a stipend to help with living expenses, your own office space",
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "100",
        "toefl_quote": "TOEFL: 100/5.5",
        "ielts": "7.5",
        "ielts_quote": "IELTS: 7.5"
    },
    {
        "field": "neuro",
        "also_fields": [],
        "department": "College of Liberal Arts",
        "program_page": "https://www.rit.edu/study/cognitive-science-phd",
        "deadline_code": "2027-01-15",
        "deadline_val": "January 15 standard deadline for fall admission",
        "deadline_quote": "January 15 standard deadline",
        "gre_code": "Not required",
        "gre_val": "Entrance exams are not required",
        "gre_quote": "Entrance exam requirements:",
        "gre_sub_code": "Not stated",
        "gre_sub_val": "GRE subject test requirement is not stated.",
        "gre_sub_quote": "",
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_quote": "",
        "funding_code": "Typical",
        "funding_val": "Doctoral students typically receive full tuition and an assistantship with stipend or salary.",
        "funding_quote": funding_quote,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from baccalaureate degree is accepted.",
        "entry_quote": "Hold a baccalaureate degree (or US equivalent) from an accredited university or college.",
        "toefl": "88",
        "toefl_quote": "TOEFL: 88/4.5",
        "ielts": "6.5",
        "ielts_quote": "IELTS: 6.5"
    }
]

for p in programs_def:
    prog_id = f"rit--{p['field']}"
    prog_data = {
        "id": prog_id,
        "university": "rit",
        "field": p["field"],
        "also_fields": p["also_fields"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": "2026-10-29",
        "notes": "",
        "fields": {
            "deadline": {
                "code": p["deadline_code"],
                "value": p["deadline_val"],
                "quote": p["deadline_quote"],
                "url": p["program_page"]
            },
            "gre_general": {
                "code": p["gre_code"],
                "value": p["gre_val"],
                "quote": p["gre_quote"],
                "url": p["program_page"]
            },
            "gre_subject": {
                "code": p["gre_sub_code"],
                "value": p["gre_sub_val"],
                "quote": p["gre_sub_quote"],
                "url": ets_subject_url if p["gre_sub_code"] == "No subject test" else p["program_page"]
            },
            "supervisor": {
                "code": p["supervisor_code"],
                "value": p["supervisor_val"],
                "quote": p["supervisor_quote"],
                "url": p["program_page"]
            },
            "funding": {
                "code": p["funding_code"],
                "value": p["funding_val"],
                "quote": p["funding_quote"],
                "url": p["program_page"]
            },
            "entry_route": {
                "code": p["entry_code"],
                "value": p["entry_val"],
                "quote": p["entry_quote"],
                "url": p["program_page"]
            },
            "toefl_min": {
                "code": p["toefl"],
                "value": f"Minimum overall TOEFL score is {p['toefl']}.",
                "quote": p["toefl_quote"],
                "url": p["program_page"]
            },
            "ielts_min": {
                "code": p["ielts"],
                "value": f"Minimum overall IELTS score is {p['ielts']}.",
                "quote": p["ielts_quote"],
                "url": p["program_page"]
            }
        }
    }
    with open(f"data/staging/programs/{prog_id}.json", 'w', encoding='utf-8') as f:
        json.dump(prog_data, f, indent=2)
    print(f"Saved {prog_id}.json")
