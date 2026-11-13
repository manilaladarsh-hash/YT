import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
(STAGING / "universities").mkdir(parents=True, exist_ok=True)
(STAGING / "programs").mkdir(parents=True, exist_ok=True)

uni = {
    "id": "virginiatech",
    "institution": "Virginia Tech",
    "country": "USA",
    "region": "Virginia",
    "grad_page": "https://graduateschool.vt.edu/admissions/how-to-apply.html",
    "checked": "2026-10-30",
    "notes": "Comprehensive research university in Blacksburg, Virginia. Ph.D. programs across engineering, science, computing, and life sciences.",
    "fields": {
        "app_fee": {
            "code": "75 USD",
            "value": "Non-refundable $75 application fee for degree-seeking students.",
            "quote": "Degree-seeking students must include a $75 fee with their application, though check to see if you qualify for a waiver or reduced fee. All application fees are non-refundable.",
            "url": "https://graduateschool.vt.edu/admissions/how-to-apply.html"
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Application fee waivers available based on qualifying events and pipeline programs.",
            "quote": "Applicants may be eligible for a Virginia Tech Graduate School application fee waivers based on the qualifying events below. Documentation as evidence of eligibility must be provided for review and approval under each category.",
            "url": "https://graduateschool.vt.edu/admissions/tuition-and-costs/Application_Fees.html"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Graduate School does not centrally require entrance tests; departments set entrance test requirements.",
            "quote": "The Graduate School does not require entrance tests, but check to see whether your department requires you to submit GRE, GMAT, or subject test scores with your application.",
            "url": "https://graduateschool.vt.edu/admissions/how-to-apply.html"
        },
        "toefl_min": {
            "code": "90",
            "value": "Minimum overall TOEFL score of 90 with 20 on each subsection (or 4.5 on scale after Jan 21, 2026).",
            "quote": "For TOEFL tests taken prior to January 21, 2026, a minimum overall score of 90 and 20 on each subsection score is required. Some departments may require higher minimum scores.",
            "url": "https://graduateschool.vt.edu/admissions/how-to-apply/testing-requirements.html"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum IELTS score of 6.5 required for admission.",
            "quote": "A minimum TOEFL score of 4.5 (IBT) or IELTS score of 6.5 is required for admission.",
            "url": "https://graduateschool.vt.edu/admissions/how-to-apply/testing-requirements.html"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Waiver granted for applicants who earned a bachelor's degree from an accredited university where English is the medium of instruction.",
            "quote": "English proficiency can also be demonstrated through a conferred bachelor’s degree from an accredited university where English is the medium of instruction. If this applies to you, we will code a waiver of the English proficiency requirement into your application once we receive and review your transcript showing degree conferral and medium of instruction as English.",
            "url": "https://graduateschool.vt.edu/admissions/how-to-apply/testing-requirements.html"
        }
    }
}

(STAGING / "universities" / "virginiatech.json").write_text(json.dumps(uni, indent=1), encoding="utf-8")

ets_sub = {
    "code": "No subject test",
    "value": "ETS offers no GRE Subject Test in this field.",
    "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study and help departments evaluate applicants' readiness for graduate school.",
    "url": "https://www.ets.org/gre/score-users/about/subject-tests.html"
}

entry_bachelor = {
    "code": "Direct from bachelor's",
    "value": "Regular admission requires an earned bachelor's degree with a minimum 3.0 GPA.",
    "quote": "Regular admission to a graduate degree is open to applicants whose grade point average (GPA) meets or exceeds the 3.00 required by the Graduate School for the last half of the credits earned for the undergraduate (bachelor’s) degree, and whose academic background meets the requirements of the admitting academic unit.",
    "url": "https://catalog.vt.edu/graduate/graduate-policies/"
}

empty_field = lambda: {"code": "Not stated", "value": "Not stated on program admission pages.", "quote": "", "url": "https://catalog.vt.edu/graduate/graduate-policies/"}

progs = [
    {
        "id": "virginiatech--cs",
        "university": "virginiatech",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/computer-science-applications/computer-science-applications-phd/",
        "checked": "2026-10-30",
        "notes": "Computer Science and Applications, PhD.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1, 2026 application deadline for full funding consideration.",
                "quote": "Dec. 1, 2026",
                "url": "https://website.cs.vt.edu/academic/graduate/future-grads/ApplicationDeadlines.html"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE not required for any degree programs in computer science.",
                "quote": "Graduate Record Examination (GRE): Not required for any degree programs.",
                "url": "https://website.cs.vt.edu/academic/graduate/future-grads/ApplicationDeadlines.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--ece",
        "university": "virginiatech",
        "field": "ece",
        "also_fields": [],
        "department": "Bradley Department of Electrical and Computer Engineering",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/electrical-engineering/electrical-engineering-phd/",
        "checked": "2026-10-30",
        "notes": "Electrical Engineering, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 priority deadline for fall admission with full funding consideration.",
                "quote": "Program-specific: To be fully considered for funding, Jan 15 for fall admission and Sep 1 for spring admission",
                "url": "https://catalog.vt.edu/graduate/degree-programs/electrical-engineering/electrical-engineering-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Electrical Engineering PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/electrical-engineering/electrical-engineering-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--bme",
        "university": "virginiatech",
        "field": "bme",
        "also_fields": [],
        "department": "Department of Biomedical Engineering and Mechanics",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/biomedical-engineering/biomedical-engineering-phd/",
        "checked": "2026-10-30",
        "notes": "Biomedical Engineering, PhD.",
        "fields": {
            "deadline": {
                "code": "2026-12-15",
                "value": "December 15 application deadline for Fall admission.",
                "quote": "Admission application deadlines: Dec 15 (or Friday before)",
                "url": "https://catalog.vt.edu/graduate/degree-programs/biomedical-engineering/biomedical-engineering-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Biomedical Engineering PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/biomedical-engineering/biomedical-engineering-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--chemeng",
        "university": "virginiatech",
        "field": "chemeng",
        "also_fields": [],
        "department": "Department of Chemical Engineering",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/chemical-engineering/chemical-engineering-phd/",
        "checked": "2026-10-30",
        "notes": "Chemical Engineering, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-06",
                "value": "January 6 application deadline for Fall admission.",
                "quote": "Admission application deadlines: Jan 6 for Fall; Sep 1 for Spring",
                "url": "https://catalog.vt.edu/graduate/degree-programs/chemical-engineering/chemical-engineering-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Chemical Engineering PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/chemical-engineering/chemical-engineering-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--civil",
        "university": "virginiatech",
        "field": "civil",
        "also_fields": [],
        "department": "The Charles E. Via, Jr. Department of Civil and Environmental Engineering",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/civil-engineering/civil-engineering-phd/",
        "checked": "2026-10-30",
        "notes": "Civil Engineering, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-08-01",
                "value": "Graduate School default deadline of August 1 for Fall admission.",
                "quote": "Admission application deadlines: Graduate School default of Aug 1 for Fall; Jan 5 for Spring",
                "url": "https://catalog.vt.edu/graduate/degree-programs/civil-engineering/civil-engineering-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Civil Engineering PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/civil-engineering/civil-engineering-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--materials",
        "university": "virginiatech",
        "field": "materials",
        "also_fields": [],
        "department": "Department of Materials Science and Engineering",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/materials-science-engineering/materials-science-engineering-phd/",
        "checked": "2026-10-30",
        "notes": "Materials Science and Engineering, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-15",
                "value": "January 15 application deadline for Fall admission.",
                "quote": "Admission application deadlines: Jan 15 for Fall; Sep 15 for Spring",
                "url": "https://catalog.vt.edu/graduate/degree-programs/materials-science-engineering/materials-science-engineering-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Materials Science and Engineering PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/materials-science-engineering/materials-science-engineering-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--mech",
        "university": "virginiatech",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical Engineering",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/mechanical-engineering/mechanical-engineering-phd/",
        "checked": "2026-10-30",
        "notes": "Mechanical Engineering, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-04",
                "value": "January 4, 2027 priority deadline for funding.",
                "quote": "January 4, 2027: priority deadline for funding",
                "url": "https://me.vt.edu/for-students/graduate/admissions-funding.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "The GRE is optional for all applicants in Mechanical Engineering.",
                "quote": "The GRE is optional for all applicants.",
                "url": "https://me.vt.edu/for-students/graduate/admissions-funding.html"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--physics",
        "university": "virginiatech",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/physics/physics-phd/",
        "checked": "2026-10-30",
        "notes": "Physics, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-05",
                "value": "For Fall admissions, the deadline is January 5th at 11:59 PM EST.",
                "quote": "For Fall admissions, the deadline is January 5th at 11:59 PM EST.",
                "url": "https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html"
            },
            "gre_general": {
                "code": "Optional",
                "value": "Submission of GRE general scores is optional.",
                "quote": "Submission of GRE general and subject tests is optional.",
                "url": "https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html"
            },
            "gre_subject": {
                "code": "Optional",
                "value": "Submission of GRE Physics subject test is optional.",
                "quote": "Submission of GRE general and subject tests is optional.",
                "url": "https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html"
            },
            "supervisor": empty_field(),
            "funding": {
                "code": "Guaranteed",
                "value": "All offers include at least five years of support with monthly stipend, tuition, and 88% health insurance subsidy.",
                "quote": "All of our offers include at least five years of support, typically starting with a teaching assistantship. All assistantships include a monthly stipend, full tuition, and a health insurance subsidy of 88% if you are enrolled in the university plan.",
                "url": "https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html"
            },
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--chemistry",
        "university": "virginiatech",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/chemistry/chemistry-phd/",
        "checked": "2026-10-30",
        "notes": "Chemistry, PhD.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall admission.",
                "quote": "Admission application deadlines: Dec 1",
                "url": "https://catalog.vt.edu/graduate/degree-programs/chemistry/chemistry-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Chemistry PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/chemistry/chemistry-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--math",
        "university": "virginiatech",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/mathematics/mathematics-phd/",
        "checked": "2026-10-30",
        "notes": "Mathematics, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-01",
                "value": "Apply by January 1st to receive full consideration for admission and graduate assistant support.",
                "quote": "To receive full consideration for admission and graduate assistant support beginning in the Fall term, please apply by January 1st.",
                "url": "https://www.math.vt.edu/grads-math/future-grads.html"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE general test scores not required.",
                "quote": "We don't require applicants to report GRE scores from the general test or subject test. Students who submit applications without GRE scores will be given equal consideration.",
                "url": "https://www.math.vt.edu/grads-math/future-grads.html"
            },
            "gre_subject": {
                "code": "Not required",
                "value": "GRE Mathematics subject test scores not required.",
                "quote": "We don't require applicants to report GRE scores from the general test or subject test. Students who submit applications without GRE scores will be given equal consideration.",
                "url": "https://www.math.vt.edu/grads-math/future-grads.html"
            },
            "supervisor": {
                "code": "Recommended",
                "value": "Prospective students encouraged to reach out to potential advisors via email.",
                "quote": "We emphasize that, to become a competitive applicant, you need to identify and begin forming a relationship with a potential advisor. We encourage prospective students to reach out to potential advisors, via email, to learn more about their work and how it might align with your research interests.",
                "url": "https://www.math.vt.edu/grads-math/future-grads.html"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "All admitted graduate students offered GTA or GRA support covering tuition and living stipend.",
                "quote": "Yes, all graduate students admitted into our graduate program are offered support through a graduate teaching assistnatship (GTA) or a graduate research assistantship (GRA). Assistantships cover the cost of tuition and provide a stipend to cover the cost of living in Blacksburg, VA.",
                "url": "https://www.math.vt.edu/grads-math/future-grads.html"
            },
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--earth",
        "university": "virginiatech",
        "field": "earth",
        "also_fields": [],
        "department": "Department of Geosciences",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/geosciences/geosciences-phd/",
        "checked": "2026-10-30",
        "notes": "Geosciences, PhD.",
        "fields": {
            "deadline": {
                "code": "2027-01-05",
                "value": "January 5 application deadline for Fall admission.",
                "quote": "Admission application deadlines: Jan 5 for Fall; Sep 1 for Spring",
                "url": "https://catalog.vt.edu/graduate/degree-programs/geosciences/geosciences-phd/"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE is not needed for Geosciences PhD.",
                "quote": "GRE: not needed",
                "url": "https://catalog.vt.edu/graduate/degree-programs/geosciences/geosciences-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--biology",
        "university": "virginiatech",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Biological Sciences",
        "program_page": "https://biol.vt.edu/Graduates/how_to_apply.html",
        "checked": "2026-10-30",
        "notes": "Biological Sciences, PhD.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "Fall admissions have a priority deadline of December 1.",
                "quote": "Fall admissions have a priority deadline of December 1. International applications will be reviewed on a rolling basis until March 31 and domestic applications will be reviewed until May 15.",
                "url": "https://biol.vt.edu/Graduates/how_to_apply.html"
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE neither required nor considered when making admissions decisions.",
                "quote": "■GRE: neither required nor considered when making admissions decisions",
                "url": "https://biol.vt.edu/Graduates/how_to_apply.html"
            },
            "gre_subject": ets_sub,
            "supervisor": {
                "code": "Recommended",
                "value": "Applicants strongly encouraged to contact faculty directly for more information about laboratories.",
                "quote": "Applicants are strongly encouraged to contact faculty directly for more information about individual laboratories. Faculty research areas may be viewed on the research webpage.",
                "url": "https://biol.vt.edu/Graduates/how_to_apply.html"
            },
            "funding": {
                "code": "Guaranteed",
                "value": "All graduate students receive competitive fellowships or 12 months of GTA or GRA support.",
                "quote": "All others receive 12 months of GTA or GRA support",
                "url": "https://biol.vt.edu/Graduates.html"
            },
            "entry_route": entry_bachelor
        }
    },
    {
        "id": "virginiatech--neuro",
        "university": "virginiatech",
        "field": "neuro",
        "also_fields": [],
        "department": "School of Neuroscience",
        "program_page": "https://catalog.vt.edu/graduate/degree-programs/neuroscience-phd/",
        "checked": "2026-10-30",
        "notes": "Neuroscience, PhD.",
        "fields": {
            "deadline": {
                "code": "2026-12-01",
                "value": "December 1 application deadline for Fall admission.",
                "quote": "Admission application deadlines: Dec 1",
                "url": "https://catalog.vt.edu/graduate/degree-programs/neuroscience-phd/"
            },
            "gre_general": {
                "code": "Optional",
                "value": "GRE is optional for Neuroscience PhD.",
                "quote": "GRE: optional",
                "url": "https://catalog.vt.edu/graduate/degree-programs/neuroscience-phd/"
            },
            "gre_subject": ets_sub,
            "supervisor": empty_field(),
            "funding": empty_field(),
            "entry_route": entry_bachelor
        }
    }
]

for p in progs:
    (STAGING / "programs" / f"{p['id']}.json").write_text(json.dumps(p, indent=1), encoding="utf-8")

print(f"Generated virginiatech and {len(progs)} programs in staging.")
