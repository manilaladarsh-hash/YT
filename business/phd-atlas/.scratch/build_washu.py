import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
(STAGING / "universities").mkdir(parents=True, exist_ok=True)
(STAGING / "programs").mkdir(parents=True, exist_ok=True)

uni = {
    "id": "washu",
    "institution": "Washington University in St. Louis",
    "country": "USA",
    "region": "Missouri",
    "grad_page": "https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/",
    "checked": "2026-10-30",
    "notes": "Private research university in St. Louis, Missouri. Ph.D. programs across Arts & Sciences, McKelvey Engineering, and Division of Biology & Biomedical Sciences (DBBS).",
    "fields": {
        "app_fee": {
            "code": "45 USD",
            "value": "Non-refundable $45 application fee for graduate programs in Arts & Sciences (engineering programs are $75).",
            "quote": "The application fee for graduate programs in Arts & Sciences is $45.",
            "url": "https://gradstudies.artsci.washu.edu/admissions-faqs"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Fee waivers available for prospective applicants who attend an eligible graduate admissions information session or qualify through partner pipeline programs.",
            "quote": "Graduate applicants: Attend an info session and skip the application fee",
            "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
        },
        "gre_general": {
            "code": "Optional",
            "value": "GRE General Test is optional for doctoral programs across engineering and arts and sciences.",
            "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
            "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
        },
        "toefl_min": {
            "code": "90",
            "value": "Minimum score of 90 on old scale or 5.0 on new scale for TOEFL iBT.",
            "quote": "Test of English as a Foreign Language (TOEFL) iBT – 5.0 overall (new scale) OR 4.5 ≥ 90 overall (old scale)",
            "url": "https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum composite score of 6.5 on IELTS Academic.",
            "quote": "International English Language Testing System (IELTS) Academic – 6.5 minimum composite score",
            "url": "https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/"
        },
        "english_waiver": {
            "code": "Yes",
            "value": "Exemption from English proficiency testing granted for citizens of listed English-medium countries including India.",
            "quote": "Citizenship from one of the following countries: Australia, Bermuda, Cameroon, Canada, Caribbean Commonwealth countries and British Caribbean territories (Anguilla, Antigua and Barbuda, The Bahamas, Barbados, Belize, British Virgin Islands, Cayman Islands, Dominica, Grenada, Guyana, Jamaica, Montserrat, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Trinidad and Tobago, Turks and Caicos Islands), Ghana, Gibraltar, Hong Kong, India, Ireland, Kenya, Liberia, New Zealand, Nigeria, Sierra Leone, Singapore, South Africa, Uganda, United Kingdom, United States, Zambia, Zimbabwe.",
            "url": "https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/"
        }
    }
}

(STAGING / "universities" / "washu.json").write_text(json.dumps(uni, indent=1), encoding="utf-8")

ets_sub = {
    "code": "No subject test",
    "value": "ETS offers no GRE Subject Test in this field.",
    "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study and help departments evaluate applicants' readiness for graduate school.",
    "url": "https://www.ets.org/gre/score-users/about/subject-tests.html"
}

eng_entry = {
    "code": "Direct from bachelor's",
    "value": "Eligible applicants must have earned or will have earned an undergraduate degree by the start of their graduate program.",
    "quote": "All eligible applicants must have earned or will have earned an undergraduate degree by the start of their graduate program.",
    "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
}

artsci_entry = {
    "code": "Direct from bachelor's",
    "value": "Applicants may apply directly to a PhD program with an earned bachelor's degree.",
    "quote": "Applicants may apply to a PhD program so long as the equivalent of a bachelor's degree is earned prior to the application semester.",
    "url": "https://gradstudies.artsci.washu.edu/admissions-faqs"
}

eng_funding = {
    "code": "Guaranteed",
    "value": "PhD students at WashU receive full tuition remission and a monthly stipend for living expenses for the duration of their program.",
    "quote": "PhD students at WashU receive full tuition remission and a monthly stipend for living expenses for the duration of their program length.",
    "url": "https://gradstudies.artsci.washu.edu/admissions-faqs"
}

empty_field = lambda url: {"code": "Not stated", "value": "Not stated on program admission pages.", "quote": "", "url": url}

progs = [
    {
        "id": "washu--cs",
        "university": "washu",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science & Engineering",
        "program_page": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html",
        "checked": "2026-10-30",
        "notes": "PhD in Computer Science.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall PhD admission.",
                "quote": "December 1",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional for PhD applicants.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"),
            "funding": eng_funding,
            "entry_route": eng_entry
        }
    },
    {
        "id": "washu--ece",
        "university": "washu",
        "field": "ece",
        "also_fields": [],
        "department": "Preston M. Green Department of Electrical & Systems Engineering",
        "program_page": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html",
        "checked": "2026-10-30",
        "notes": "PhD in Electrical Engineering.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall PhD admission.",
                "quote": "December 1",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional for PhD applicants.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"),
            "funding": eng_funding,
            "entry_route": eng_entry
        }
    },
    {
        "id": "washu--bme",
        "university": "washu",
        "field": "bme",
        "also_fields": [],
        "department": "Department of Biomedical Engineering",
        "program_page": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html",
        "checked": "2026-10-30",
        "notes": "PhD in Biomedical Engineering.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall PhD admission.",
                "quote": "December 1",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional for PhD applicants.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"),
            "funding": eng_funding,
            "entry_route": eng_entry
        }
    },
    {
        "id": "washu--chemeng",
        "university": "washu",
        "field": "chemeng",
        "also_fields": [],
        "department": "Department of Energy, Environmental & Chemical Engineering",
        "program_page": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html",
        "checked": "2026-10-30",
        "notes": "PhD in Energy, Environmental & Chemical Engineering.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall PhD admission.",
                "quote": "December 1",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional for PhD applicants.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"),
            "funding": eng_funding,
            "entry_route": eng_entry
        }
    },
    {
        "id": "washu--materials",
        "university": "washu",
        "field": "materials",
        "also_fields": [],
        "department": "Institute of Materials Science & Engineering",
        "program_page": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html",
        "checked": "2026-10-30",
        "notes": "PhD in Materials Science & Engineering.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall PhD admission.",
                "quote": "December 1",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional for PhD applicants.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"),
            "funding": eng_funding,
            "entry_route": eng_entry
        }
    },
    {
        "id": "washu--mech",
        "university": "washu",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical Engineering & Materials Science",
        "program_page": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html",
        "checked": "2026-10-30",
        "notes": "PhD in Mechanical Engineering.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall PhD admission.",
                "quote": "December 1",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional for PhD applicants.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://engineering.washu.edu/academics/graduate-admissions/deadlines.html"),
            "funding": eng_funding,
            "entry_route": eng_entry
        }
    },
    {
        "id": "washu--physics",
        "university": "washu",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": "https://physics.washu.edu/graduate-program",
        "checked": "2026-10-30",
        "notes": "PhD in Physics.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for PhD admission.",
                "quote": "PhD - December 1, 2026 at 11:59 PM Eastern Standard Time",
                "url": "https://gradstudies.artsci.washu.edu/physics"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE General test scores are optional.",
                "quote": "The GRE General and Subject test scores are optional.",
                "url": "https://physics.washu.edu/graduate"
            },
            "gre_subject": {
                "code": "Optional",
                "value": "GRE Physics Subject test scores are optional.",
                "quote": "The GRE General and Subject test scores are optional.",
                "url": "https://physics.washu.edu/graduate"
            },
            "supervisor": empty_field("https://physics.washu.edu/graduate-program"),
            "funding": {
                "code": "Guaranteed",
                "value": "Financial support guaranteed for the first five years with full tuition and stipend/salary.",
                "quote": "Students who are admitted to the PhD program in Physics receive a complete financial support package including full tuition and a stipend/salary for the academic year. Financial support is guaranteed by the department for the first five years for students who are making satisfactory progress towards their PhD.",
                "url": "https://physics.washu.edu/graduate"
            },
            "entry_route": artsci_entry
        }
    },
    {
        "id": "washu--chemistry",
        "university": "washu",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": "https://chemistry.washu.edu/graduate-program",
        "checked": "2026-10-30",
        "notes": "PhD in Chemistry.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1, 2026 application deadline for Fall admission.",
                "quote": "Application deadline: December 1, 2026 at 11:59 PM Eastern Standard Time",
                "url": "https://gradstudies.artsci.washu.edu/chemistry"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://chemistry.washu.edu/graduate-program"),
            "funding": {
                "code": "Guaranteed",
                "value": "All Chemistry PhD students receive generous stipend and tuition fellowship for duration of program.",
                "quote": "All Chemistry PhD students receive a generous stipend ($36,050 for the '24-25 twelve-month academic year) and a tuition fellowship for the duration of the program.",
                "url": "https://chemistry.washu.edu/graduate"
            },
            "entry_route": artsci_entry
        }
    },
    {
        "id": "washu--math",
        "university": "washu",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": "https://math.washu.edu/graduate-program",
        "checked": "2026-10-30",
        "notes": "PhD in Mathematics.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1, 2026 application deadline for Mathematics PhD.",
                "quote": "PhD - December 1, 2026 at 11:59 PM Eastern Standard Time",
                "url": "https://gradstudies.artsci.washu.edu/mathematics"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE general test is optional.",
                "quote": "While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.",
                "url": "https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html"
            },
            "gre_subject": empty_field("https://math.washu.edu/graduate-program"),
            "supervisor": empty_field("https://math.washu.edu/graduate-program"),
            "funding": {
                "code": "Guaranteed",
                "value": "Virtually all doctoral students receive full financial support (stipends and tuition waiver).",
                "quote": "The completion of the doctoral degree requires about five years of full-time study, and virtually all students receive full financial support (stipends and tuition waiver) during their study.",
                "url": "https://math.washu.edu/graduate"
            },
            "entry_route": artsci_entry
        }
    },
    {
        "id": "washu--earth",
        "university": "washu",
        "field": "earth",
        "also_fields": [],
        "department": "Department of Earth, Environmental, and Planetary Sciences",
        "program_page": "https://eeps.washu.edu/graduate-program",
        "checked": "2026-10-30",
        "notes": "PhD in Earth, Environmental & Planetary Sciences.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1, 2026 application deadline for Fall admission.",
                "quote": "Application deadline: December 1, 2026 at 11:59 PM Eastern Standard Time",
                "url": "https://gradstudies.artsci.washu.edu/earth-environmental-and-planetary-sciences"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE scores are optional for Earth, Environmental & Planetary Sciences PhD.",
                "quote": "For those choosing to submit GRE scores, please use WashU's school code 6929 and the department code 0806. However, please note that GRE scores are optional.",
                "url": "https://eeps.washu.edu/graduate"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://eeps.washu.edu/graduate-program"),
            "funding": eng_funding,
            "entry_route": artsci_entry
        }
    },
    {
        "id": "washu--biology",
        "university": "washu",
        "field": "biology",
        "also_fields": [],
        "department": "Roy and Diana Vagelos Division of Biology & Biomedical Sciences",
        "program_page": "https://dbbs.wustl.edu/admissions/",
        "checked": "2026-10-30",
        "notes": "PhD programs in Division of Biology & Biomedical Sciences (DBBS).",
        "fields": {
            "deadline": {
                "code": "2026-11-15",
                "value": "November 15 application deadline at 11:59 PM EST.",
                "quote": "APPLICATION DATES: September 1 – November 15 at 11:59 PM EST",
                "url": "https://dbbs.wustl.edu/admissions/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE scores are not required nor accepted for DBBS admissions.",
                "quote": "GRE NOT REQUIRED NOR ACCEPTED",
                "url": "https://dbbs.wustl.edu/admissions/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://dbbs.wustl.edu/admissions/"),
            "funding": {
                "code": "Guaranteed",
                "value": "Full tuition and yearly stipend are guaranteed to all accepted students.",
                "quote": "full tuition and yearly stipend are guaranteed to all accepted students.",
                "url": "https://dbbs.wustl.edu/admissions/"
            },
            "entry_route": artsci_entry
        }
    },
    {
        "id": "washu--neuro",
        "university": "washu",
        "field": "neuro",
        "also_fields": [],
        "department": "Roy and Diana Vagelos Division of Biology & Biomedical Sciences - Neurosciences",
        "program_page": "https://dbbs.wustl.edu/admissions/",
        "checked": "2026-10-30",
        "notes": "PhD in Neurosciences (DBBS).",
        "fields": {
            "deadline": {
                "code": "2026-11-15",
                "value": "November 15 application deadline at 11:59 PM EST.",
                "quote": "APPLICATION DATES: September 1 – November 15 at 11:59 PM EST",
                "url": "https://dbbs.wustl.edu/admissions/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE scores are not required nor accepted for DBBS admissions.",
                "quote": "GRE NOT REQUIRED NOR ACCEPTED",
                "url": "https://dbbs.wustl.edu/admissions/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://dbbs.wustl.edu/admissions/"),
            "funding": {
                "code": "Guaranteed",
                "value": "Full tuition and yearly stipend are guaranteed to all accepted students.",
                "quote": "full tuition and yearly stipend are guaranteed to all accepted students.",
                "url": "https://dbbs.wustl.edu/admissions/"
            },
            "entry_route": artsci_entry
        }
    }
]

for p in progs:
    (STAGING / "programs" / f"{p['id']}.json").write_text(json.dumps(p, indent=1), encoding="utf-8")

print(f"Generated washu and {len(progs)} programs in staging.")
