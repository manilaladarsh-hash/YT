import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
(STAGING / "universities").mkdir(parents=True, exist_ok=True)
(STAGING / "programs").mkdir(parents=True, exist_ok=True)

uni = {
    "id": "wsu",
    "institution": "Washington State University",
    "country": "USA",
    "region": "Washington",
    "grad_page": "https://gradschool.wsu.edu/apply/",
    "checked": "2026-10-30",
    "notes": "Public land-grant research university in Pullman, Washington. Ph.D. programs across engineering, computing, physical and life sciences, and agriculture.",
    "fields": {
        "app_fee": {
            "code": "100 USD",
            "value": "Non-refundable $100 application fee for graduate degree applications.",
            "quote": "$100 Non-refundable Application Fee*",
            "url": "https://gradschool.wsu.edu/apply/"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Fee waivers available from Graduate School for McNair Scholars and WSU REU students; other requests handled by target departments.",
            "quote": "*McNair Scholars and WSU Research Experience for Undergraduates (REU) students are eligible for an application fee waiver from the Graduate School. Please contact Dr. Raymond Herrera before applying. All other application fee waiver requests should be directed to the program(s) to which you are applying.",
            "url": "https://gradschool.wsu.edu/apply/"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Graduate School sets no central GRE requirement; requirements vary by degree program.",
            "quote": "Please check with your specific Degree Program to determine whether a GRE test is required.",
            "url": "https://gradschool.wsu.edu/international-requirements/"
        },
        "toefl_min": {
            "code": "75",
            "value": "Minimum score of 75 on TOEFL iBT (or 4 on new scale effective Jan 21, 2026).",
            "quote": "Exam TOEFL Essentials TOEFL (PBT) TOEFL (iBT) New TOEFL (iBT) (Effective Jan 21, 2026) IELTS Duolingo Cambridge B2 First, C1 Advanced, C2 Proficiency Michigan English Test (MET) Pearson Test for English (PTEA) International Test of English Proficiency (iTEP) Minimum Score 8 540 75 4 6.5 105 176 52 56 4.5",
            "url": "https://gradschool.wsu.edu/international-requirements/"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum score of 6.5 on IELTS Academic.",
            "quote": "Exam TOEFL Essentials TOEFL (PBT) TOEFL (iBT) New TOEFL (iBT) (Effective Jan 21, 2026) IELTS Duolingo Cambridge B2 First, C1 Advanced, C2 Proficiency Michigan English Test (MET) Pearson Test for English (PTEA) International Test of English Proficiency (iTEP) Minimum Score 8 540 75 4 6.5 105 176 52 56 4.5",
            "url": "https://gradschool.wsu.edu/international-requirements/"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Waiver granted for applicants who earned a degree where the language of instruction was English with official letter or transcript notation.",
            "quote": "Hold a baccalaureate-level or higher degree from a college or university outside the United States where the language of instruction was English (provide an official letter or transcript from the school stating English was the language of instruction).",
            "url": "https://gradschool.wsu.edu/international-requirements/"
        }
    }
}

(STAGING / "universities" / "wsu.json").write_text(json.dumps(uni, indent=1), encoding="utf-8")

ets_sub = {
    "code": "No subject test",
    "value": "ETS offers no GRE Subject Test in this field.",
    "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study and help departments evaluate applicants' readiness for graduate school.",
    "url": "https://www.ets.org/gre/score-users/about/subject-tests.html"
}

entry_bachelor = {
    "code": "Direct from bachelor's",
    "value": "Regular admission requires an earned equivalent of a 4-year U.S. bachelor's degree with a minimum 3.0 GPA.",
    "quote": "Have earned the equivalent of a U.S. bachelor’s degree from a regionally accredited institution. Typically, students should have completed a minimum of four years of study beyond grade 12.",
    "url": "https://gradschool.wsu.edu/international-requirements/"
}

empty_field = lambda url: {"code": "Not stated", "value": "Not stated on program fact sheet.", "quote": "", "url": url}

progs = [
    {
        "id": "wsu--cs",
        "university": "wsu",
        "field": "cs",
        "also_fields": [],
        "department": "School of Electrical Engineering and Computer Science",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Computer Science.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority application deadline for Fall admission.",
                "quote": "Fall January 10th",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Computer Science PhD.",
                "quote": "GRE Optional",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--ece",
        "university": "wsu",
        "field": "ece",
        "also_fields": [],
        "department": "School of Electrical Engineering and Computer Science",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Electrical and Computer Engineering.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority application deadline for Fall admission.",
                "quote": "Fall January 10th",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Electrical and Computer Engineering PhD.",
                "quote": "GRE Optional",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--chemeng",
        "university": "wsu",
        "field": "chemeng",
        "also_fields": [],
        "department": "Gene and Linda Voiland School of Chemical Engineering and Bioengineering",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemical-engineering/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Chemical Engineering.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10 January 1",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemical-engineering/"
            },
            "gre_general": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemical-engineering/"),
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemical-engineering/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemical-engineering/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--civil",
        "university": "wsu",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Civil and Environmental Engineering",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Civil Engineering.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE not required for Civil Engineering PhD.",
                "quote": "GRE No",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--materials",
        "university": "wsu",
        "field": "materials",
        "also_fields": [],
        "department": "Materials Science and Engineering Program",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-materials-science/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Materials Science and Engineering.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-materials-science/"
            },
            "gre_general": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-materials-science/"),
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-materials-science/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-materials-science/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--mech",
        "university": "wsu",
        "field": "mech",
        "also_fields": [],
        "department": "School of Mechanical and Materials Engineering",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Mechanical Engineering.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/"
            },
            "gre_general": {
                "code": "Required",
                "value": "Official GRE scores required for application.",
                "quote": "Required application material includes an application, resume, statement of purpose, Student Interest Profile form, three letters of recommendation, official transcripts, official GRE scores, and official TOEFL scores (international applicants).",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--physics",
        "university": "wsu",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics and Astronomy",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Physics.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 priority deadline for Fall admission.",
                "quote": "Fall January 15",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "General GRE scores optional.",
                "quote": "GRE scores optional",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/"
            },
            "gre_subject": {
                "code": "Recommended",
                "value": "Subject Physics GRE strongly recommended.",
                "quote": "Subject Physics GRE Strongly Recommended",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/"
            },
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--chemistry",
        "university": "wsu",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Chemistry.",
        "fields": {
            "deadline": {
                "code": "2026-12-11",
                "value": "Second Friday of December priority deadline for Fall admission.",
                "quote": "Fall Second Friday of December Priority deadline",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE General test scores optional.",
                "quote": "GRE Scores-General Test Optional.",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--math",
        "university": "wsu",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics and Statistics",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Mathematics.",
        "fields": {
            "deadline": {
                "code": "2026-12-10",
                "value": "December 10 priority deadline for Fall admission.",
                "quote": "Fall December 10",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE scores are not required but encouraged.",
                "quote": "GRE scores are not required but encouraged",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/"
            },
            "gre_subject": {
                "code": "Not required",
                "value": "GRE subject test not required.",
                "quote": "GRE scores are not required but encouraged",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/"
            },
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/"),
            "funding": {
                "code": "Typical",
                "value": "Applicants to PhD in Mathematics automatically considered for graduate assistantships.",
                "quote": "Students applying to the PhD in Mathematics will be automatically considered for an assistantship position.",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/"
            },
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--earth",
        "university": "wsu",
        "field": "earth",
        "also_fields": [],
        "department": "School of the Environment - Geology",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Geology.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10th",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE requirement waived until further notice.",
                "quote": "GRE tests requirement are waived until further notice.",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/"
            },
            "gre_subject": ets_sub,
            "supervisor": {
                "code": "Required",
                "value": "Applicants must secure a faculty advisor before applying.",
                "quote": "The School of the Environment does not consider graduate applicants who have not secured a faculty advisor before applying, so please do not apply to one of our graduate degrees without first doing this step.",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/"
            },
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--biology",
        "university": "wsu",
        "field": "biology",
        "also_fields": [],
        "department": "School of Biological Sciences",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Biology.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE is not required for Biology PhD.",
                "quote": "GRE is NOT required",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/"),
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/"),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "wsu--environment",
        "university": "wsu",
        "field": "environment",
        "also_fields": [],
        "department": "School of the Environment - Environmental and Natural Resource Sciences",
        "program_page": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/",
        "checked": "2026-10-30",
        "notes": "Doctor of Philosophy in Environmental and Natural Resource Sciences.",
        "fields": {
            "deadline": {
                "code": "2027-01-10",
                "value": "January 10 priority deadline for Fall admission.",
                "quote": "Fall January 10th",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE requirement waived until further notice.",
                "quote": "GRE tests requirement are waived until further notice.",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/"
            },
            "gre_subject": ets_sub,
            "supervisor": {
                "code": "Required",
                "value": "Applicants must secure a faculty advisor before applying.",
                "quote": "The School of the Environment does not consider graduate applicants who have not secured a faculty advisor before applying, so please do not apply to one of our graduate degrees without first doing this step.",
                "url": "https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/"
            },
            "funding": empty_field("https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/"),
            "entry_route": entry_bachelor
        }
    }
]

for p in progs:
    (STAGING / "programs" / f"{p['id']}.json").write_text(json.dumps(p, indent=1), encoding="utf-8")

print(f"Generated wsu and {len(progs)} programs in staging.")
