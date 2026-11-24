import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
UNI_DIR = STAGING / "universities"
PROG_DIR = STAGING / "programs"
UNI_DIR.mkdir(parents=True, exist_ok=True)
PROG_DIR.mkdir(parents=True, exist_ok=True)

GRAD_URL = "https://www.unf.edu/graduateschool/"
FAQ_URL = "https://www.unf.edu/graduateschool/admissions/faqs.html"
PROC_URL = "https://www.unf.edu/catalog/admissions/graduate/Admission-Procedures.html"
REQ_URL = "https://www.unf.edu/catalog/admissions/graduate/Admission-Requirements.html"
INTL_URL = "https://www.unf.edu/catalog/admissions/graduate/International-Students.html"
DEADLINES_URL = "https://www.unf.edu/graduateschool/academics/program-contacts-deadlines.html"
ASSIST_URL = "https://www.unf.edu/graduateschool/assistants-awards/assistantships.html"
FELLOW_URL = "https://www.unf.edu/graduateschool/assistants-awards/fellowships.html"
PHD_URL = "https://www.unf.edu/ccec/computing/graduate/PhD-Computing.html"
ETS_ABOUT = "https://www.ets.org/gre/score-users/about/subject-tests.html"

CHECKED = "2026-11-15"

unf_uni = {
    "id": "unf",
    "institution": "University of North Florida",
    "country": "USA",
    "region": "Florida",
    "grad_page": GRAD_URL,
    "checked": CHECKED,
    "fields": {
        "app_fee": {
            "code": "30 USD",
            "value": "Non-refundable graduate application fee is $30 per program application (must be in U.S. currency drawn from a U.S. bank if paid by check/money order).",
            "quote": "All graduate applicants must complete and submit an online application and pay the non-refundable application fee of $30 by the deadline posted for the applicable term.",
            "url": PROC_URL,
            "also": [
                {
                    "quote": "Application Fee: The application fee is $30.00. The application fee must be in U.S. currency only (check or money order) drawn from a U.S. bank.",
                    "url": INTL_URL,
                }
            ],
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "No financial-need or general application fee waivers are offered; a waiver is available only by student request to the Graduate School when reapplying or switching programs within three consecutive terms of a previously paid fee.",
            "quote": "Please note, we do not offer application fee waivers unless the applicant has previously paid and qualifies for a waiver as discussed in the What should I know about the application fee? question above. | The graduate application fee may be good for three consecutive terms. Contact us if you previously paid an application fee within three consecutive terms of a current application and would like to know if you are eligible to an application fee waiver.",
            "url": FAQ_URL,
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Graduate Admissions Policy leaves standardized test (GRE) requirements to each individual department and program (Computing Ph.D. requires GRE Verbal >= 150 and Quantitative >= 155).",
            "quote": "",
            "url": REQ_URL,
        },
        "toefl_min": {
            "code": "79",
            "value": "Minimum Graduate School TOEFL iBT score is 79 (UNF Regulation 2.0385R states a general university floor of 63 iBT / 500 PBT while authorizing UNF to set higher graduate minimums).",
            "quote": "Minimum ELP test scores: | TOEFL 79 | IELTS 6.5 | DuoLingo 110 | PTE 53",
            "url": FAQ_URL,
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum Graduate School IELTS Academic overall score is 6.5 (also accepts Duolingo 110 or PTE 53).",
            "quote": "Minimum ELP test scores: | TOEFL 79 | IELTS 6.5 | DuoLingo 110 | PTE 53",
            "url": FAQ_URL,
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "English Language Proficiency cannot be waived as a university requirement, but applicants who graduated from a college taught in English (documented via school website, transcript, or Medium of Instruction certificate) or scored GRE Verbal >= 152 satisfy ELP if their Graduate Program Director emails approval and documentation to the Graduate School.",
            "quote": "Graduate applicants who meet one of the non-test score indicators for ELP should email their Graduate Program Director with official proof to request consideration. The Graduate Program Director must email The Graduate School stating their approval and the documentation if they would like to accept the indicator as demonstration of English Language Proficiency. | Non-test score English Language Proficiency Indicators: | Student graduated from a college taught in English (documented on the school website, transcript, or Medium of Instruction (MOI) certificate).",
            "url": FAQ_URL,
        },
    },
    "notes": (
        "Carnegie R2 institution in Jacksonville, Florida. Currently offers one active STEM research Ph.D. (Doctor of Philosophy in Computing, with Cybersecurity and Intelligent Systems concentrations; "
        "Note: the School of Computing webpage states F-1 visa international admission to the Computing Ph.D. is currently closed pending SEVP approval). "
        "All other active UNF doctoral degrees are non-STEM/clinical practice doctorates (Ed.D. in Curriculum & Instruction and Educational Leadership; D.C.N., D.H.A., D.N.P., D.P.T.). "
        "Engineering, Biology, Chemistry, Physics, and Math/Stats offer Master's degrees only."
    ),
}

unf_cs = {
    "id": "unf--cs",
    "university": "unf",
    "field": "cs",
    "also_fields": ["datasci"],
    "name": "Computing, Ph.D.",
    "department": "College of Computing, Engineering and Construction — School of Computing",
    "program_page": PHD_URL,
    "checked": CHECKED,
    "fields": {
        "deadline": {
            "code": "2027-06-01",
            "value": "June 1 is the recommended international Fall application deadline in the UNF Graduate Catalog (August 1 general Fall deadline on the Graduate School deadlines page, which defers to international deadlines). Important: the Computing Ph.D. webpage currently notes admission of international students on F-1 visas (or seeking F-1 status) is closed pending SEVP approval.",
            "quote": "The recommended deadline for international students for most programs are: | Fall - June 1 | Spring - October 1 | For programs with fall deadlines earlier than June 1 and spring deadlines earlier than October 1, the international deadlines are the same as the program deadlines.",
            "url": INTL_URL,
            "inferred": "year",
            "also": [
                {
                    "quote": "Computing (PhD) | Deadlines | Fall | August 1 | Spring | December 1 | Summer | April 15 | *International Applicants: Please see the program webpage for international application deadlines.",
                    "url": DEADLINES_URL,
                },
                {
                    "quote": "Admission of international students on F-1 visa (or seeking such status) is currently closed pending SEVP approval.",
                    "url": PHD_URL,
                },
            ],
        },
        "gre_general": {
            "code": "Required",
            "value": "GRE Verbal (>= 150) and GRE Quantitative (>= 155) scores are required for admission to the Computing Ph.D.",
            "quote": "Application Requirements | In addition to the general Graduate School application requirements, the application materials for the Computing PhD program must include the following: | GRE verbal and quantitative scores | A minimum score of 150 in the GRE verbal section | A minimum score of 155 in the GRE quantitative section",
            "url": PHD_URL,
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "No ETS GRE Subject Test exists for this field (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            "url": ETS_ABOUT,
        },
        "supervisor": {
            "code": "Not required",
            "value": "Pre-application supervisor commitment is not required; students identify a dissertation supervisor and form a 4-member dissertation committee by completion of 30 post-bachelor credits.",
            "quote": "The student must form a dissertation committee and identify a dissertation supervisor, who is a Graduate Faculty member and will chair this committee, by the completion of 30 credits in the program (post Bachelor).",
            "url": PHD_URL,
        },
        "funding": {
            "code": "Competitive",
            "value": "Competitive departmental graduate assistantships ($2,500/semester for 10 hrs/wk or $5,000/semester for 20 hrs/wk, plus prorated tuition waiver and out-of-state fee waiver for >=10 hr/wk appointments; renewal not guaranteed; international students eligible) and university fellowships (Key Bradbury STEM Fellowship $10,000/yr up to 2 years; Milligan Presidential Fellowship $5,000/yr).",
            "quote": "Graduate assistants receive a stipend based on their appointment: | $2,500 per semester (fall and spring) for 10 hours per week (minimum) | $5,000 per semester (fall and spring) for 20 hours per week (minimum) | Tuition waivers are prorated based on your appointment hours. | Availability depends on departmental needs and funding, so it’s important to connect with your program directly to learn about current opportunities. | Some assistantships may be renewed, but renewal is not guaranteed.",
            "url": ASSIST_URL,
            "also": [
                {
                    "quote": "The Key Bradbury STEM Fellowship is awarded to outstanding University of North Florida graduate students. This fellowship provides one student in a field related to science, technology, engineering or math (STEM) $10,000 per academic year ($5,000 per semester; fall/spring) for up to two years as long as the student remains eligible.",
                    "url": FELLOW_URL,
                }
            ],
        },
        "entry_route": {
            "code": "Either",
            "value": "72-credit post-baccalaureate Ph.D. admitting applicants with a four-year bachelor's degree (GPA >= 3.0 in last 60 credits) and allowing up to 30 relevant graduate transfer credits or graduate GPA consideration for prior graduate degree holders.",
            "quote": "A four-year baccalaureate degree from a regionally accredited U.S. institution, or its equivalent from a foreign institution, with a GPA of 3.0 or higher in all work attempted in the last 60 credit hours of undergraduate study. | If the applicant has a graduate degree in a Computing field, graduate courses may be considered if the undergraduate GPA is less than 3.0 | A minimum of 72 credits beyond the baccalaureate degree | Student may transfer a maximum of 30 relevant graduate credits toward the coursework requirement.",
            "url": PHD_URL,
        },
    },
    "notes": (
        "Offers two concentrations: Cybersecurity and Intelligent Systems (AI, Machine Learning, Data Analytics, Data Mining, Text Mining; cross-listed under datasci). "
        "F-1 VISA RESTRICTION: Program page states 'Admission of international students on F-1 visa (or seeking such status) is currently closed pending SEVP approval.' "
        "Applicants without a prior Computing degree must complete undergraduate prerequisite coursework (Programming, Data Structures, Applied Discrete Math, Databases, Computer Networks). "
        "Requires 3 letters of recommendation, resume, and <=500-word statement of purpose."
    ),
}

(UNI_DIR / "unf.json").write_text(json.dumps(unf_uni, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
(PROG_DIR / "unf--cs.json").write_text(json.dumps(unf_cs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Wrote unf.json and unf--cs.json to data/staging/")
