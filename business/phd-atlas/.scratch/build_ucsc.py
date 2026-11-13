import json
from pathlib import Path

staging_dir = Path("data/staging")
uni_dir = staging_dir / "universities"
prog_dir = staging_dir / "programs"

uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

# 1. UCSC University Record
help_url = "https://graduateadmissions.ucsc.edu/help-for-applicants/"
test_url = "https://graduateadmissions.ucsc.edu/test-score-requirements/"
deadlines_url = "https://graduateadmissions.ucsc.edu/application-deadlines/"
fin_url = "https://graduateadmissions.ucsc.edu/financial-support/"

ets_subject_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_subject_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

ucsc_uni = {
    "id": "ucsc",
    "institution": "University of California, Santa Cruz",
    "country": "USA",
    "region": "California",
    "grad_page": help_url,
    "checked": "2026-10-30",
    "notes": "Quarter system. Domestic application fee is $135; international application fee is $155.",
    "fields": {
        "app_fee": {
            "code": "135 USD",
            "value": "Application fee is $135.00 for domestic applicants and $155.00 for international applicants.",
            "quote": "The application fee is $135.00 for domestic applicants and $155.00 for international applicants. Electronic payment options are available through our application system; a small fee (approximately $4) will also be charged for credit card processing.",
            "url": help_url
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Fee waivers are available for US Citizens, AB 540, or Permanent Residents with financial hardship, but are extremely limited.",
            "quote": "If you are a US Citizen, AB 540, or Permanent Resident of the United States, you may request an application fee waiver if you believe you are eligible. Please be aware that fee waivers are extremely limited.",
            "url": help_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE requirements vary by program; applicants should check specific program requirements.",
            "quote": "GRE requirements vary by program; applicants whose native language is not English may be required to take the TOEFL iBT (including the Home Edition) or IELTS Academic exam.",
            "url": help_url
        },
        "toefl_min": {
            "code": "83",
            "value": "Minimum TOEFL iBT score is 83 for general programs, though select STEM programs require 89.",
            "quote": "83 for all other programs.",
            "url": test_url
        },
        "ielts_min": {
            "code": "7.0",
            "value": "A minimum overall band score of 7 from the IELTS test is required for admission.",
            "quote": "For those choosing to take the IELTS Academic (in-person and online versions), a minimum overall score of 7 from the IELTS test is required for admission.",
            "url": test_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Waivers for admission purposes may be requested by applicants who completed a 4-year bachelor's degree at an English-speaking institution.",
            "quote": "TOEFL/IELTS waivers for admission purposes may be requested by applicants who do not have English as their first language and who have completed a four-year bachelor’s degree at an English-speaking institution.",
            "url": help_url
        }
    }
}

with open(uni_dir / "ucsc.json", "w", encoding="utf-8") as f:
    json.dump(ucsc_uni, f, indent=2)
print("Wrote ucsc.json")

# 2. STEM PhD Programs
# Let's define the STEM PhD programs mapped from the UCSC deadline table and catalog
programs_data = [
    {
        "field": "physics",
        "department": "Department of Physics",
        "also_fields": [],
        "has_subject_test": True,
        "deadline_code": "2026-12-14",
        "deadline_quote": "December 14",
        "notes": "Physics M.S./Ph.D. program."
    },
    {
        "field": "astronomy",
        "department": "Department of Astronomy & Astrophysics",
        "also_fields": ["physics"],
        "has_subject_test": True,
        "deadline_code": "2026-12-10",
        "deadline_quote": "December 10",
        "notes": "Astronomy & Astrophysics Ph.D."
    },
    {
        "field": "chemistry",
        "department": "Department of Chemistry & Biochemistry",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2026-12-01",
        "deadline_quote": "December 1",
        "notes": "Chemistry Ph.D."
    },
    {
        "field": "materials",
        "department": "Materials Science & Engineering Program",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2027-01-07",
        "deadline_quote": "January 7",
        "notes": "Materials Science & Engineering Ph.D."
    },
    {
        "field": "math",
        "department": "Department of Mathematics",
        "also_fields": [],
        "has_subject_test": True,
        "deadline_code": "2027-01-04",
        "deadline_quote": "January 4",
        "notes": "Mathematics M.A./Ph.D."
    },
    {
        "field": "statistics",
        "department": "Department of Statistics",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2026-12-14",
        "deadline_quote": "December 14",
        "notes": "Statistical Science M.S./Ph.D."
    },
    {
        "field": "cs",
        "department": "Department of Computer Science & Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2027-01-05",
        "deadline_quote": "January 5",
        "notes": "Computer Science & Engineering Ph.D."
    },
    {
        "field": "ece",
        "department": "Department of Electrical & Computer Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2027-01-07",
        "deadline_quote": "January 7",
        "notes": "Electrical & Computer Engineering Ph.D."
    },
    {
        "field": "earth",
        "department": "Department of Earth & Planetary Sciences",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2027-01-07",
        "deadline_quote": "January 7",
        "notes": "Earth & Planetary Sciences M.S./Ph.D."
    },
    {
        "field": "environment",
        "department": "Environmental Studies Department",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2026-12-10",
        "deadline_quote": "December 10",
        "notes": "Environmental Studies Ph.D."
    },
    {
        "field": "biology",
        "department": "Department of Ecology & Evolutionary Biology",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2026-12-10",
        "deadline_quote": "December 10",
        "notes": "Ecology & Evolutionary Biology M.A./Ph.D."
    },
    {
        "field": "biomed",
        "department": "Program in Biomedical Sciences and Engineering (PBSE)",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2026-12-01",
        "deadline_quote": "December 1",
        "notes": "PBSE: Chemical Biology, Biochemistry & Biophysics / METX Ph.D."
    },
    {
        "field": "bme",
        "department": "Department of Biomolecular Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "deadline_code": "2026-12-01",
        "deadline_quote": "December 1",
        "notes": "Biomolecular Engineering & Bioinformatics Ph.D."
    }
]

entry_quote = "Awarding of a bachelor’s degree or its equivalent from an accredited university prior to the quarter for which admission is sought"
funding_quote = "Read about the 5/2 Year Graduate Student Funding Packages – offered to MFA and PhD admits."

for prog in programs_data:
    fid = prog["field"]
    pid = f"ucsc--{fid}"
    
    if prog["has_subject_test"]:
        gre_subj = {
            "code": "Not stated",
            "value": "Subject test requirement is program-dependent and not stated on central test scores page.",
            "quote": "GRE requirements vary by program; applicants whose native language is not English may be required to take the TOEFL iBT (including the Home Edition) or IELTS Academic exam.",
            "url": help_url
        }
    else:
        gre_subj = {
            "code": "No subject test",
            "value": "ETS offers no subject test in this discipline.",
            "quote": ets_subject_quote,
            "url": ets_subject_url
        }

    record = {
        "id": pid,
        "university": "ucsc",
        "field": fid,
        "also_fields": prog["also_fields"],
        "department": prog["department"],
        "program_page": deadlines_url,
        "checked": "2026-10-30",
        "notes": prog["notes"],
        "fields": {
            "deadline": {
                "code": prog["deadline_code"],
                "value": f"{prog['deadline_quote']} deadline for Ph.D. application.",
                "quote": prog["deadline_quote"],
                "url": deadlines_url
            },
            "gre_subject": gre_subj,
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact is not stated as required.",
                "quote": "",
                "url": help_url
            },
            "funding": {
                "code": "Guaranteed",
                "value": "UCSC offers 5-year funding packages to incoming PhD admits.",
                "quote": funding_quote,
                "url": fin_url
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Awarding of a bachelor's degree or equivalent prior to enrollment.",
                "quote": entry_quote,
                "url": help_url
            }
        }
    }
    
    with open(prog_dir / f"{pid}.json", "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)

print(f"Wrote {len(programs_data)} program records for UCSC.")
