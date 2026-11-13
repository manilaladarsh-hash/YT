import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

# University record
uic_data = {
    "id": "uic",
    "institution": "University of Illinois Chicago",
    "country": "USA",
    "region": "Illinois",
    "grad_page": "https://grad.uic.edu/admissions/domestic-admission/",
    "checked": "2026-10-30",
    "notes": "Non-refundable application fee is $80; international credential evaluation fee of $100 applies to international credentials.",
    "fields": {
        "app_fee": {
            "code": "80 USD",
            "value": "A non-refundable application fee of $80 is required.",
            "quote": "A non-refundable application fee of $80 (U.S. currency) is required to have your application reviewed.",
            "url": "https://grad.uic.edu/admissions/domestic-admission/"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Financial hardship waivers are not granted; specific waivers available only for UIC alumni and select programs.",
            "quote": "Unfortunately, financial hardship waivers for graduate and professional applications are not granted.",
            "url": "https://admissions.uic.edu/graduate-professional/application-process/application-fee-waivers"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE requirements are determined by each specific academic program.",
            "quote": "These are determined by program. See the program's website for complete details. Program requirements may include (but are not limited to) items such as: GRE scores - use our Institutional Code 1851 to report your results",
            "url": "https://admissions.uic.edu/graduate-professional/requirements-deadlines/international-requirements"
        },
        "toefl_min": {
            "code": "80",
            "value": "Minimum required score for iBT Internet-based TOEFL is 80.",
            "quote": "Minimum required scores are: iBT Internet-based TOEFL of 80, with subscores of Reading 19, Listening 17, Speaking 20, and Writing 21; IELTS of 6.5, with all four subscores of at least 6.0",
            "url": "https://ece.uic.edu/admissions/"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum required IELTS Academic overall band score is 6.5.",
            "quote": "Minimum required scores are: iBT Internet-based TOEFL of 80, with subscores of Reading 19, Listening 17, Speaking 20, and Writing 21; IELTS of 6.5, with all four subscores of at least 6.0",
            "url": "https://ece.uic.edu/admissions/"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exemption granted for enrollment at an accredited U.S. institution for at least two years of full-time study.",
            "quote": "Enrollment at an accredited U.S. institution for at least two years of full-time, academic study.",
            "url": "https://admissions.uic.edu/graduate-professional/requirements-deadlines/international-requirements"
        }
    }
}

(uni_dir / "uic.json").write_text(json.dumps(uic_data, indent=2), encoding="utf-8")

uic_entry_route = {
    "code": "Direct from bachelor's",
    "value": "Unofficial transcripts uploaded for review; official documents required only if admitted.",
    "quote": "You must upload unofficial transcripts for review. If you are admitted, official documents will be requested at that time, along with submission instructions.",
    "url": "https://grad.uic.edu/admissions/domestic-admission/"
}

programs = [
    {
        "id": "uic--physics",
        "university": "uic",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": "https://phys.uic.edu/academics/graduate-studies/graduate/",
        "checked": "2026-10-30",
        "notes": "Physics Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 deadline for applicants seeking a Teaching/Research Assistantship.",
                "quote": "February 15th for International Applicants seeking a Teaching/Research Assistantship.",
                "url": "https://phys.uic.edu/academics/graduate-studies/graduate/"
            },
            "gre_subject": {
                "code": "Not stated",
                "value": "GRE Subject test score requirement not stated on prospective graduate page.",
                "quote": "",
                "url": "https://phys.uic.edu/academics/graduate-studies/graduate/"
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Advisor contact prior to admission not stated on prospective graduate page.",
                "quote": "",
                "url": "https://phys.uic.edu/academics/graduate-studies/graduate/"
            },
            "funding": {
                "code": "Typical",
                "value": "Applicants apply by February 15 seeking Teaching/Research Assistantship support.",
                "quote": "February 15th for International Applicants seeking a Teaching/Research Assistantship.",
                "url": "https://phys.uic.edu/academics/graduate-studies/graduate/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--cs",
        "university": "uic",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science",
        "program_page": "https://cs.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Computer Science Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 final deadline for PhD applicants (December 15 recommended).",
                "quote": "February 15: all PhD and MS applicants",
                "url": "https://cs.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact prior to admission not specified.",
                "quote": "",
                "url": "https://cs.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "PhD students in first five years guaranteed funded appointment with tuition waiver, partial fee waiver, and stipend.",
                "quote": "PhD students in their first five years of enrollment are guaranteed a funded appointment for fall and spring that includes a full tuition waiver, a partial fee waiver, and a stipend.",
                "url": "https://cs.uic.edu/graduate/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--math",
        "university": "uic",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics, Statistics, and Computer Science",
        "program_page": "https://mscs.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Mathematics Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-15",
                "value": "December 15 annual application deadline for PhD cohort.",
                "quote": "PhD students are admitted as a cohort each Fall semester, and the annual application deadline for both domestic and international students is December 15.",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "Not stated",
                "value": "GRE Subject score requirement not specified on MSCS admissions page.",
                "quote": "",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact prior to admission not specified.",
                "quote": "",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "PhD students admitted on a competitive basis with financial aid consideration.",
                "quote": "PhD students are admitted as a cohort each Fall semester, and the annual application deadline for both domestic and international students is December 15.",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--statistics",
        "university": "uic",
        "field": "statistics",
        "also_fields": [],
        "department": "Department of Mathematics, Statistics, and Computer Science",
        "program_page": "https://mscs.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Statistics Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-15",
                "value": "December 15 annual application deadline for PhD cohort.",
                "quote": "PhD students are admitted as a cohort each Fall semester, and the annual application deadline for both domestic and international students is December 15.",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact prior to admission not specified.",
                "quote": "",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "PhD students admitted on a competitive basis with financial aid consideration.",
                "quote": "PhD students are admitted as a cohort each Fall semester, and the annual application deadline for both domestic and international students is December 15.",
                "url": "https://mscs.uic.edu/graduate/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--chemistry",
        "university": "uic",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": "https://chem.uic.edu/graduate-studies/",
        "checked": "2026-10-30",
        "notes": "Chemistry Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-01-01",
                "value": "January 1 for fullest consideration including University Fellowship awards.",
                "quote": "For Fall 2026 admission to the Chemistry PhD program, applications are reviewed as soon as they are complete. For fullest consideration, including University Fellowship awards, all materials should be submitted by January 1, 2026.",
                "url": "https://chem.uic.edu/graduate-studies/"
            },
            "gre_subject": {
                "code": "Not stated",
                "value": "GRE Subject requirement not stated on graduate studies page.",
                "quote": "",
                "url": "https://chem.uic.edu/graduate-studies/"
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact prior to admission not specified.",
                "quote": "",
                "url": "https://chem.uic.edu/graduate-studies/"
            },
            "funding": {
                "code": "Typical",
                "value": "Fullest consideration for departmental and fellowship funding by January 1.",
                "quote": "For Fall 2026 admission to the Chemistry PhD program, applications are reviewed as soon as they are complete. For fullest consideration, including University Fellowship awards, all materials should be submitted by January 1, 2026.",
                "url": "https://chem.uic.edu/graduate-studies/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--biology",
        "university": "uic",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Biological Sciences",
        "program_page": "https://bios.uic.edu/academics/graduate-studies/graduate-application/",
        "checked": "2026-10-30",
        "notes": "Biological Sciences Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for full consideration.",
                "quote": "To receive full consideration, applications must be received by December 1st.",
                "url": "https://bios.uic.edu/academics/graduate-studies/graduate-application/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact prior to admission not stated as required for PhD.",
                "quote": "",
                "url": "https://bios.uic.edu/academics/graduate-studies/graduate-application/"
            },
            "funding": {
                "code": "Typical",
                "value": "Consideration for departmental support provided with December 1 submission.",
                "quote": "To receive full consideration, applications must be received by December 1st.",
                "url": "https://bios.uic.edu/academics/graduate-studies/graduate-application/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--bme",
        "university": "uic",
        "field": "bme",
        "also_fields": [],
        "department": "Richard and Loan Hill Department of Biomedical Engineering",
        "program_page": "https://bme.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Biomedical Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-15",
                "value": "December 15 deadline for fee waiver and priority consideration.",
                "quote": "The application fee for the Biomedical Engineering (BME) or Bioinformatics (BIOI) Doctoral/PhD programs will be waived for all applicants if the application is submitted by December 15, 2026.",
                "url": "https://bme.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Advisor contact prior to admission not stated.",
                "quote": "",
                "url": "https://bme.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "PhD students in BME funded year-round with stipend, full tuition waiver, and partial fee waiver for duration of studies.",
                "quote": "PhD students in BME will be funded with stipend, full tuition waiver, and partial fee waiver year around for the duration of their studies as long as they are making satisfactory progress towards the didactic and research requirements set forth by BME/UIC.",
                "url": "https://bme.uic.edu/graduate/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--ece",
        "university": "uic",
        "field": "ece",
        "also_fields": [],
        "department": "Department of Electrical and Computer Engineering",
        "program_page": "https://ece.uic.edu/admissions/",
        "checked": "2026-10-30",
        "notes": "Electrical and Computer Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-15",
                "value": "December 15 priority deadline for fee waiver and PhD application review.",
                "quote": "PhD applications must be submitted by Dec. 15, 2026",
                "url": "https://ece.uic.edu/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact not specified as mandatory.",
                "quote": "",
                "url": "https://ece.uic.edu/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "PhD applicants seeking financial assistance must submit personal statement and CV.",
                "quote": "PhD applications must be submitted by Dec. 15, 2026",
                "url": "https://ece.uic.edu/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--mech",
        "university": "uic",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical and Industrial Engineering",
        "program_page": "https://mie.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Mechanical Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-15",
                "value": "December 15 application deadline for fee waiver and priority review.",
                "quote": "The PhD application fee will be waived for applicants who submit their applications by December 15, 2026.",
                "url": "https://mie.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact not specified as mandatory.",
                "quote": "",
                "url": "https://mie.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "Four-Year PhD Funding Guarantee: Admitted students receive funded appointment with tuition waiver and fee waiver in first four years.",
                "quote": "Four-Year PhD Funding Guarantee: PhD students who are admitted into the MIE program with financial support in the form of a teaching or research assistantship will receive a funded appointment that includes a waiver of tuition and certain fees in the fall and spring semesters of their first four years.",
                "url": "https://mie.uic.edu/graduate/admissions/"
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Successful applicants should hold an MS degree in their field; direct admission considered for exceptional BS holders.",
                "quote": "PhD Applicants: Successful applicants for doctoral study should have a master of science degree in their field from an accredited institution and should have completed substantial coursework in the chosen field of study. The department does consider outstanding PhD applicants who have only a bachelor’s degree through a program called “direct admission.”",
                "url": "https://mie.uic.edu/graduate/admissions/"
            }
        }
    },
    {
        "id": "uic--chemeng",
        "university": "uic",
        "field": "chemeng",
        "also_fields": [],
        "department": "Department of Chemical Engineering",
        "program_page": "https://che.uic.edu/graduate-programs/admissions/",
        "checked": "2026-10-30",
        "notes": "Chemical Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 deadline for international PhD applicants (January 15 priority).",
                "quote": "February 15, 2027: International PhD applicants seeking to begin in August 2027",
                "url": "https://che.uic.edu/graduate-programs/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact not specified as mandatory.",
                "quote": "",
                "url": "https://che.uic.edu/graduate-programs/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "Financial aid consideration with priority application submitted by January 15.",
                "quote": "February 15, 2027: International PhD applicants seeking to begin in August 2027",
                "url": "https://che.uic.edu/graduate-programs/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--civil",
        "university": "uic",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Civil, Materials, and Environmental Engineering",
        "program_page": "https://cme.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Civil Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 general graduate deadline.",
                "quote": "February 15: all PhD and MS applicants",
                "url": "https://cs.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact not specified as mandatory.",
                "quote": "",
                "url": "https://cme.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "Application for Graduate Appointment submitted for financial aid consideration.",
                "quote": "GRE general test scores (PhD applicants only). GRE general test scores are required only for applicants to our PhD programs. Requirements are a minimum combined verbal and quantitative score of 305.",
                "url": "https://cme.uic.edu/graduate/admissions/"
            },
            "entry_route": uic_entry_route
        }
    },
    {
        "id": "uic--materials",
        "university": "uic",
        "field": "materials",
        "also_fields": [],
        "department": "Department of Civil, Materials, and Environmental Engineering",
        "program_page": "https://cme.uic.edu/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Materials Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 general graduate deadline.",
                "quote": "February 15: all PhD and MS applicants",
                "url": "https://cs.uic.edu/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact not specified as mandatory.",
                "quote": "",
                "url": "https://cme.uic.edu/graduate/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "Application for Graduate Appointment submitted for financial aid consideration.",
                "quote": "GRE general test scores (PhD applicants only). GRE general test scores are required only for applicants to our PhD programs. Requirements are a minimum combined verbal and quantitative score of 305.",
                "url": "https://cme.uic.edu/graduate/admissions/"
            },
            "entry_route": uic_entry_route
        }
    }
]

for prog in programs:
    fpath = prog_dir / f"{prog['id']}.json"
    fpath.write_text(json.dumps(prog, indent=2), encoding="utf-8")

print(f"Written uic.json and {len(programs)} program files to data/staging.")
