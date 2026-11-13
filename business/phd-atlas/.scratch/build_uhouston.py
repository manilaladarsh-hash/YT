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
uhouston_data = {
    "id": "uhouston",
    "institution": "University of Houston",
    "country": "USA",
    "region": "Texas",
    "grad_page": "https://www.uh.edu/graduate-school/admissions/how-to-apply/",
    "checked": "2026-10-30",
    "notes": "Domestic application fee is $50; international application fee is $80.",
    "fields": {
        "app_fee": {
            "code": "50 USD",
            "value": "Application fees are $50 for domestic applicants, $80 for international applicants.",
            "quote": "Application fees are $50 for domestic applicants, $80 for international applicants and $25 for non-degree (Certificate based programs). Limited application fee waivers are available. Please check with program regarding eligibility for application fee waivers.",
            "url": "https://www.uh.edu/graduate-school/admissions/how-to-apply/"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Limited application fee waivers are available depending on program eligibility.",
            "quote": "Limited application fee waivers are available. Please check with program regarding eligibility for application fee waivers.",
            "url": "https://www.uh.edu/graduate-school/admissions/how-to-apply/"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Test score requirements vary by program; refer to program website.",
            "quote": "Test Scores (GRE, GMAT, etc.) should be sent by the testing agency. Refer to the program's website for test score requirements. Use school code 6870 when reporting test scores to University of Houston.",
            "url": "https://www.uh.edu/graduate-school/admissions/how-to-apply/"
        },
        "toefl_min": {
            "code": "79",
            "value": "Minimum score required by UH for internet-based TOEFL is 79 overall.",
            "quote": "Minimum score required by UH for internet-based = 79 (120 scale) overall or 4 (6-point scale) overall internet-based test",
            "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum score required by UH is 6.5 overall.",
            "quote": "Minimum score required by UH = 6.5 overall",
            "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Waiver granted for baccalaureate degree earned from an accredited US institution or institution in an English-medium country.",
            "quote": "Baccalaureate degree (or higher) earned from a regionally accredited U.S. institution or at an institution at which English is the medium of instruction in the countries listed here.",
            "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
        }
    }
}

(uni_dir / "uhouston.json").write_text(json.dumps(uhouston_data, indent=2), encoding="utf-8")

# Common entry_route for graduate school
uh_entry_route = {
    "code": "Direct from bachelor's",
    "value": "Requires undergraduate degree conferral prior to enrollment.",
    "quote": "Please follow these instructions to properly scan and upload your transcript. If admitted, however, you will not be able to enroll without the official transcript(s) showing undergraduate degree conferral on file.",
    "url": "https://www.uh.edu/graduate-school/admissions/how-to-apply/"
}

programs = [
    {
        "id": "uhouston--physics",
        "university": "uhouston",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": "https://www.uh.edu/nsm/physics/graduate/faq/",
        "checked": "2026-10-30",
        "notes": "Physics Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 priority application deadline to guarantee consideration.",
                "quote": "In order to guarantee consideration please apply by January 15. However late applications",
                "url": "https://www.uh.edu/nsm/physics/graduate/faq/"
            },
            "gre_subject": {
                "code": "Not stated",
                "value": "GRE Subject score requirement not stated in application checklist.",
                "quote": "",
                "url": "https://www.uh.edu/nsm/physics/graduate/faq/"
            },
            "supervisor": {
                "code": "Not required",
                "value": "Students are required to identify research advisors by middle of spring semester after admission.",
                "quote": "Students are required to identify their research advisors by the middle of the spring",
                "url": "https://www.uh.edu/nsm/physics/graduate/faq/"
            },
            "funding": {
                "code": "Typical",
                "value": "Typically accepts 20-25 new graduate students and grants 15-20 teaching assistantships per year.",
                "quote": "We typically accept 20-25 new graduate students and grant 15-20 teaching assistantships",
                "url": "https://www.uh.edu/nsm/physics/graduate/faq/"
            },
            "entry_route": uh_entry_route
        }
    },
    {
        "id": "uhouston--cs",
        "university": "uhouston",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science",
        "program_page": "https://www.uh.edu/nsm/computer-science/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Computer Science Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 application deadline for international applicants.",
                "quote": "January 15 (PhD and MS program) International applicants",
                "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not required",
                "value": "Helpful, but not required to contact faculty of interest before or at application.",
                "quote": "It is helpful, but not required to contact faculty of interest before or at the time of application.",
                "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
            },
            "funding": {
                "code": "Not stated",
                "value": "Funding details not stated on admissions page.",
                "quote": "",
                "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "BS degree in Computer Science or related field.",
                "quote": "BS degree in Computer Science or related field (e.g. Engineering, Mathematics, Statistics)",
                "url": "https://www.uh.edu/nsm/computer-science/graduate/admissions/"
            }
        }
    },
    {
        "id": "uhouston--math",
        "university": "uhouston",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": "https://www.uh.edu/nsm/math/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Mathematics Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 recommended for priority consideration for Fall admission.",
                "quote": "materials be submitted before January 15. The regular deadline is April 1, but by",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "gre_subject": {
                "code": "Not required",
                "value": "GRE is waived for all graduate applications within Department of Mathematics.",
                "quote": "The Graduate Record Examination (GRE) is waived for all graduate applications within the Department of Mathematics.",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Advisor contact requirements prior to admission not stated.",
                "quote": "",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "Each fall semester approximately 15-20 funded positions are available.",
                "quote": "materials be submitted before January 15. The regular deadline is April 1, but by",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Undergraduate degree and demonstrated competence in mathematics required.",
                "quote": "To be admitted to any of the graduate programs in mathematics, a student must have an undergraduate degree and demonstrate competence in mathematics.",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            }
        }
    },
    {
        "id": "uhouston--statistics",
        "university": "uhouston",
        "field": "statistics",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": "https://www.uh.edu/nsm/math/graduate/admissions/",
        "checked": "2026-10-30",
        "notes": "Statistics and Data Science Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 recommended for priority consideration for Fall admission.",
                "quote": "materials be submitted before January 15. The regular deadline is April 1, but by",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Advisor contact requirements prior to admission not stated.",
                "quote": "",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "funding": {
                "code": "Typical",
                "value": "Each fall semester approximately 15-20 funded positions are available.",
                "quote": "materials be submitted before January 15. The regular deadline is April 1, but by",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Undergraduate degree and demonstrated competence in mathematics required.",
                "quote": "To be admitted to any of the graduate programs in mathematics, a student must have an undergraduate degree and demonstrate competence in mathematics.",
                "url": "https://www.uh.edu/nsm/math/graduate/admissions/"
            }
        }
    },
    {
        "id": "uhouston--chemistry",
        "university": "uhouston",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": "https://www.uh.edu/nsm/chemistry/graduate/",
        "checked": "2026-10-30",
        "notes": "Chemistry Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-01-31",
                "value": "January 31 application deadline for full consideration.",
                "quote": "The application deadline for International (all visa types) is January 31.",
                "url": "https://www.uh.edu/nsm/chemistry/graduate/"
            },
            "gre_subject": {
                "code": "Optional",
                "value": "GRE Chemistry test is optional but encouraged for fellowship consideration.",
                "quote": "Request Educational Testing Service (ETS) to send GRE Chemistry or Physics Test scores to the University of Houston Main Campus (ETS code 6870). These tests are optional but encouraged for consideration of fellowship awards.",
                "url": "https://www.uh.edu/nsm/chemistry/graduate/admissions/"
            },
            "supervisor": {
                "code": "Not required",
                "value": "Admitted students have until end of January of their second semester to choose a research advisor.",
                "quote": "If you are admitted, you have until the beginning of your second semester (end of January) to choose a research advisor.",
                "url": "https://www.uh.edu/nsm/chemistry/graduate/faq/"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "All Ph.D. students admitted are automatically given a Teaching Assistantship for the first year.",
                "quote": "All Ph.D. students admitted into the Graduate Program in the Department of Chemistry are automatically given a Teaching Assistantship for the first year. The monthly stipend for this assistantship is approximately $2,325. After the first year, students who",
                "url": "https://www.uh.edu/nsm/chemistry/graduate/faq/"
            },
            "entry_route": uh_entry_route
        }
    },
    {
        "id": "uhouston--biology",
        "university": "uhouston",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Biology & Biochemistry",
        "program_page": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/",
        "checked": "2026-10-30",
        "notes": "Biology Ph.D. (Cell & Molecular Biology / Ecology & Evolution)",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for fall Ph.D. admission.",
                "quote": "Deadline: December 1",
                "url": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact requirements not stated on program page.",
                "quote": "",
                "url": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "All admitted students receive $2,386/month stipend and Graduate Tuition Fellowship covering tuition and fees.",
                "quote": "You will receive a monthly stipend of $2,386/month (U. S. $28,632 per year) through either a Teaching Assistantship (TA) or Research Assistantship (RA). In addition, tuition and mandatory fees will be covered by the Graduate Tuition Fellowship (GTF).",
                "url": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/"
            },
            "entry_route": uh_entry_route
        }
    },
    {
        "id": "uhouston--biomed",
        "university": "uhouston",
        "field": "biomed",
        "also_fields": [],
        "department": "Department of Biology & Biochemistry",
        "program_page": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/",
        "checked": "2026-10-30",
        "notes": "Biochemistry Ph.D.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for fall Ph.D. admission.",
                "quote": "Deadline: December 1",
                "url": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Supervisor contact requirements not stated on program page.",
                "quote": "",
                "url": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "All admitted students receive $2,386/month stipend and Graduate Tuition Fellowship covering tuition and fees.",
                "quote": "You will receive a monthly stipend of $2,386/month (U. S. $28,632 per year) through either a Teaching Assistantship (TA) or Research Assistantship (RA). In addition, tuition and mandatory fees will be covered by the Graduate Tuition Fellowship (GTF).",
                "url": "https://www.uh.edu/nsm/biology-biochemistry/graduate/prospective-students/phd-programs/"
            },
            "entry_route": uh_entry_route
        }
    },
    {
        "id": "uhouston--bme",
        "university": "uhouston",
        "field": "bme",
        "also_fields": [],
        "department": "Department of Biomedical Engineering",
        "program_page": "https://www.bme.uh.edu/graduate/admissions",
        "checked": "2026-10-30",
        "notes": "Biomedical Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 priority deadline for Fall admission.",
                "quote": "Feb 15(*priority)",
                "url": "https://www.bme.uh.edu/graduate/admissions"
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
                "url": "https://www.bme.uh.edu/graduate/admissions"
            },
            "funding": {
                "code": "Not stated",
                "value": "Funding details not stated on program admissions page.",
                "quote": "",
                "url": "https://www.bme.uh.edu/graduate/admissions"
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "BS or MS degree in Biomedical Engineering or closely related field.",
                "quote": "(MS) 3.00/4.00 on last 60 hours (Ph.D.) 3.30/4.00 on last 60 hours or Graduate hours if hold MS degree",
                "url": "https://www.bme.uh.edu/graduate/admissions"
            }
        }
    },
    {
        "id": "uhouston--chemeng",
        "university": "uhouston",
        "field": "chemeng",
        "also_fields": [],
        "department": "Department of Chemical and Biomolecular Engineering",
        "program_page": "https://www.chee.uh.edu/graduate/admissions",
        "checked": "2026-10-30",
        "notes": "Chemical Engineering Ph.D.",
        "fields": {
            "deadline": {
                "code": "2027-02-15",
                "value": "February 15 application deadline for upcoming Fall term.",
                "quote": "The deadline to submit your Online Application is February 15 of each year for the upcoming Fall Term. Be advised that all required documents must be uploaded by this date.",
                "url": "https://www.chee.uh.edu/graduate/admissions"
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "ETS offers no subject test in this discipline.",
                "quote": ets_quote,
                "url": ets_url
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor contact not stated as mandatory.",
                "quote": "",
                "url": "https://www.chee.uh.edu/graduate/admissions"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "All qualified candidates accepted into PhD program receive full financial assistance ($34,200/year).",
                "quote": "At this time, the current stipend is $34,200 per year. All qualified candidates accepted into our PhD program receive full financial assistance. No separate application is necessary.",
                "url": "https://www.chee.uh.edu/graduate/admissions"
            },
            "entry_route": uh_entry_route
        }
    }
]

for prog in programs:
    fpath = prog_dir / f"{prog['id']}.json"
    fpath.write_text(json.dumps(prog, indent=2), encoding="utf-8")

print(f"Written uhouston.json and {len(programs)} program files to data/staging.")
