import json
import os
from pathlib import Path

staging_dir = Path("data/staging")
uni_dir = staging_dir / "universities"
prog_dir = staging_dir / "programs"

uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

# 1. UCR University Record
ucr_uni = {
    "id": "ucr",
    "institution": "University of California, Riverside",
    "country": "USA",
    "region": "California",
    "grad_page": "https://graduate.ucr.edu/admission-requirements",
    "checked": "2026-10-30",
    "notes": "Quarter system. Domestic application fee is $135; international application fee is $155.",
    "fields": {
        "app_fee": {
            "code": "135 USD",
            "value": "Application fee is $135 for domestic applicants and $155 for international applicants.",
            "quote": "All programs except the MPAc, MFin, Business Analytics, and MBA: $135",
            "url": "https://graduate.ucr.edu/admission-requirements"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Financial hardship fee waivers are available to qualified domestic applicants only.",
            "quote": "A limited amount of Financial Hardship Fee Waivers are available to qualified domestic applicants only.",
            "url": "https://graduate.ucr.edu/admission-requirements"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Many graduate programs no longer require GRE; required status depends on specific program.",
            "quote": "Many graduate programs no longer require the GRE. However, if the graduate program you are applying to requires the GRE, this will be confirmed in the online application.",
            "url": "https://graduate.ucr.edu/admission-requirements"
        },
        "toefl_min": {
            "code": "80",
            "value": "Minimum acceptable score is 80 for the TOEFL iBT (prior to January 21, 2026).",
            "quote": "- 80 for the TOEFL iBT (prior to January 21, 2026)",
            "url": "https://graduate.ucr.edu/admission-requirements"
        },
        "ielts_min": {
            "code": "7.0",
            "value": "Minimum acceptable overall score is 7.0, with no score less than 6 on any individual component.",
            "quote": "- 7, with no score less than 6 on any individual component",
            "url": "https://graduate.ucr.edu/admission-requirements"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exemption granted if degree earned where English is the exclusive language of instruction, confirmed through WHED.",
            "quote": "You have earned or will earn an undergraduate or advanced degree at an institution outside of the U.S. where English is the exclusive language of instruction, confirmed through WHED. If English is not the only language listed or if no language is listed, additional documentation may be required.",
            "url": "https://graduate.ucr.edu/admission-requirements"
        }
    }
}

with open(uni_dir / "ucr.json", "w", encoding="utf-8") as f:
    json.dump(ucr_uni, f, indent=2)
print("Wrote ucr.json")

# 2. Programs
ets_subject_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_subject_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

programs_data = [
    {
        "field": "physics",
        "department": "Department of Physics and Astronomy",
        "also_fields": [],
        "has_subject_test": True,
        "notes": ""
    },
    {
        "field": "astronomy",
        "department": "Department of Physics and Astronomy",
        "also_fields": ["physics"],
        "has_subject_test": True,
        "notes": ""
    },
    {
        "field": "chemistry",
        "department": "Department of Chemistry",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "materials",
        "department": "Materials Science and Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "math",
        "department": "Department of Mathematics",
        "also_fields": [],
        "has_subject_test": True,
        "notes": ""
    },
    {
        "field": "statistics",
        "department": "Department of Statistics",
        "also_fields": [],
        "has_subject_test": False,
        "notes": "Applied Statistics Ph.D."
    },
    {
        "field": "cs",
        "department": "Department of Computer Science and Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "ece",
        "department": "Department of Electrical and Computer Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "mech",
        "department": "Department of Mechanical Engineering",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "chemeng",
        "department": "Department of Chemical and Environmental Engineering",
        "also_fields": ["environment"],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "environment",
        "department": "Department of Environmental Sciences",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "earth",
        "department": "Department of Earth and Planetary Sciences",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "biology",
        "department": "Department of Biology",
        "also_fields": [],
        "has_subject_test": False,
        "notes": "Evolution, Ecology, and Organismal Biology Ph.D."
    },
    {
        "field": "biomed",
        "department": "School of Medicine",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    },
    {
        "field": "neuro",
        "department": "Interdepartmental Graduate Program in Neuroscience",
        "also_fields": [],
        "has_subject_test": True,
        "notes": ""
    },
    {
        "field": "bme",
        "department": "Department of Bioengineering",
        "also_fields": [],
        "has_subject_test": False,
        "notes": ""
    }
]

for prog in programs_data:
    fid = prog["field"]
    pid = f"ucr--{fid}"
    
    if prog["has_subject_test"]:
        gre_subj = {
            "code": "Not stated",
            "value": "Subject GRE requirement is not stated on central Graduate Division admissions pages.",
            "quote": "Many graduate programs no longer require the GRE. However, if the graduate program you are applying to requires the GRE, this will be confirmed in the online application.",
            "url": "https://graduate.ucr.edu/admission-requirements"
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
        "university": "ucr",
        "field": fid,
        "also_fields": prog["also_fields"],
        "department": prog["department"],
        "program_page": "https://graduate.ucr.edu/programs",
        "checked": "2026-10-30",
        "notes": prog["notes"],
        "fields": {
            "deadline": {
                "code": "2027-01-05",
                "value": "January 5 priority fellowship consideration deadline for Fall admission (admission only deadline is June 1).",
                "quote": "Fall - January 5th (Fellowship Consideration) / June 1st (Admission Only)",
                "url": "https://graduate.ucr.edu/deadlines"
            },
            "gre_subject": gre_subj,
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor agreement is not stated as required.",
                "quote": "",
                "url": "https://graduate.ucr.edu/programs"
            },
            "funding": {
                "code": "Competitive",
                "value": "Applications received by January 5 are considered for fellowship and financial support based on funding availability.",
                "quote": "Applications received after January 5th will be considered for financial support based on funding availability and if the degree objective selected is eligible for fellowship funding.",
                "url": "https://graduate.ucr.edu/deadlines"
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Direct admission from a bachelor's degree or recognized international equivalent.",
                "quote": "A bachelor's degree from a regionally accredited institution, or a recognized international equivalent. The degree must represent the completion of a program equivalent in subject matter and scholarship to that offered by the University of California.",
                "url": "https://graduate.ucr.edu/admission-requirements"
            }
        }
    }
    
    with open(prog_dir / f"{pid}.json", "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)

print(f"Wrote {len(programs_data)} program records for UCR.")
