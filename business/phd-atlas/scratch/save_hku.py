import os
import sys
from pathlib import Path

os.environ["ATLAS_OUT"] = "data/staging"
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import rec  # noqa: E402

CHECKED = "2026-11-14"

GRE_NOT_REQ = (
    "Not required",
    "Not required for STEM PhD programs (GRE Subject Test in Psychology >= 550 is required only for Department of Psychology applicants whose first degree is not in Psychology; GRE General/GMAT is required only for Business and Economics).",
    "Faculty of Business and Economics applicants are required to demonstrate their capability for graduate studies by obtaining satisfactory scores in the Graduate Management Admission Test (GMAT) or Graduate Record Examinations (GRE), taken within five years | Department of Psychology applicants whose first degree is not in Psychology are required to obtain a minimum score of 550 in the GRE’s Subject Test in Psychology taken within five years",
    "https://gradsch.hku.hk/prospective_students/application/admission_requirement",
)

NO_SUBJECT_TEST = lambda label: (
    "No subject test",
    f"No ETS GRE Subject Test exists for {label} (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
    "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
    "https://www.ets.org/gre/score-users/about/subject-tests.html",
)

CENTRAL_DEADLINE = (
    "2026-12-01",
    "Main Round and Hong Kong PhD Fellowship Scheme (HKPFS) deadline for 2027-28 entry is December 1, 2026 (1st Clearing Round: April 30, 2027; 2nd Clearing Round: August 31, 2027).",
    "1 September 2026 – 1 December 2026 (HKT 23:59, GMT+8)",
    "https://gradsch.hku.hk/prospective_students/application/application_period",
    {
        "time_sensitive": "2026-12-01",
        "also": [
            {
                "quote": "In view of the limited admission quota, applicants are strongly encouraged to apply in the Main Round. Applications will be considered in the clearing rounds only if there are vacancies after the Main Round.",
                "url": "https://gradsch.hku.hk/prospective_students/application/application_period",
            }
        ],
    },
)

ENGG_DEADLINE = (
    "2026-12-01",
    "Main Round and Hong Kong PhD Fellowship Scheme (HKPFS) deadline for 2027-28 entry is December 1, 2026 (1st Clearing Round: April 30, 2027; 2nd Clearing Round: August 31, 2027).",
    "September 1, 2026 - December 1, 2026 (HKT 23:59 or GMT +8 hours) | The submission deadline for HKPFS applications in 2027-28 is December 1, 2026.",
    "https://engg.hku.hk/Admissions/PhD-MPhil/Application-Procedures",
    {"time_sensitive": "2026-12-01"},
)

MED_DEADLINE = (
    "2026-12-01",
    "Main Round deadline is December 1, 2026 (HKPFS deadline is December 1, 2026 at noon HKT; 1st Clearing Round: April 30, 2027; 2nd Clearing Round: August 31, 2027).",
    "Hong Kong PhD Fellowship Scheme: 1 December 2026 (HKT noon, GMT+8) | Main Round: 1 December 2026 (HKT 23:59, GMT+8)",
    "https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/key-info",
    {"time_sensitive": "2026-12-01"},
)

SUPERVISOR_OPTIONAL = (
    "Not required",
    "HKU Graduate School treats contacting a potential supervisor before applying as optional.",
    "Contact potential supervisor (optional)",
    "https://gradsch.hku.hk/prospective_students/application/how_to_apply",
)

ENGG_SUPERVISOR = (
    "Recommended",
    "Faculty of Engineering instructs MPhil/PhD applicants to search for potential supervisors and discuss proposed research areas before submitting an application.",
    "Search for potential supervisor(s) (contact details and brief introduction of teaching staff are also available in the departmental websites). | Discuss the proposed research areas with the potential supervisor(s) before submitting application.",
    "https://engg.hku.hk/Admissions/PhD-MPhil/Application-Procedures",
)

CENTRAL_FUNDING = (
    "Typical",
    "Full-time PhD students holding a bachelor's degree with 2:1 honours (or equivalent) or above are normally eligible for Postgraduate Scholarships (HK$19,135/month initially and HK$19,655/month after probation confirmation, effective Sept 1, 2026), subject to funding availability; top applicants receive HKU-PS or HKPF (HK$28,700/month + tuition waiver).",
    "other full-time PhD and MPhil students who hold a first degree with second-class honours first division (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (PGS) during the normative study period, subject to availability of funding. | The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
    "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
)

ENGG_FUNDING = (
    "Typical",
    "Full-time PhD students with 2:1 honours (or equivalent) or above are normally eligible for Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after probation confirmation), subject to funding availability, plus HKU-PS/HKPF awards waiving HK$47,000-HK$49,500 composition fees.",
    "other full-time PhD and MPhil students who hold a first degree with second-class honours first division (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (PGS) during the normative study period, subject to availability of funding. | The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
    "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
    {
        "also": [
            {
                "quote": "Various scholarships and fellowships are available to our research students: | HKU Presidential PhD Scholar Programme (HKU-PS) | Hong Kong PhD Fellowship Scheme (HKPF) | Postgraduate Scholarships (PGS)",
                "url": "https://engg.hku.hk/Admissions/PhD-MPhil/Scholarships-Financial-Assistance-and-Fees",
            }
        ]
    },
)

SCIFAC_FUNDING = (
    "Typical",
    "Full-time PhD students with 2:1 honours (or equivalent) or above are normally eligible for Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026), subject to funding availability, while HKU-PS/HKPF awardees receive HK$28,700/month plus tuition waiver and cash awards.",
    "For non HKU-PS / non-HKPF Research Postgraduate (RPg) students | Postgraduate Scholarship (PGS) | Funding value: HK$19,135/month or HK$19,655/month# (wef 1/9/2026)",
    "https://www.scifac.hku.hk/rpg/programme-info/stipend-support",
    {
        "also": [
            {
                "quote": "other full-time PhD and MPhil students who hold a first degree with second-class honours first division (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (PGS) during the normative study period, subject to availability of funding.",
                "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
            }
        ]
    },
)

CENTRAL_ENTRY = (
    "Either",
    "Admits either honours bachelor's (or taught master's) holders to the 4-year PhD or research master's (MPhil) holders to the 3-year PhD.",
    "All candidates with an honours Bachelor’s degree are eligible for PhD and MPhil admission.",
    "https://gradsch.hku.hk/prospective_students/application/faq_on_application",
)

ENGG_ENTRY = (
    "Either",
    "Admits First Class Honours bachelor's holders or 2:1 honours + taught master's holders to the 4-year PhD, and 2:1 honours + research MPhil holders to the 3-year PhD.",
    "4-year Doctor of Philosophy (4-year PhD) | Bachelor’s degree with First Class Honours preferably with research experience; or | Bachelor’s degree with Second Class Honours Division I and a taught Master’s degree | 3-year Doctor of Philosophy (3-year PhD) | Bachelor’s degree with Second Class Honours Division I or above and a research Master’s degree (MPhil)",
    "https://engg.hku.hk/Admissions/PhD-MPhil/Admission-Requirements",
)

SCIFAC_ENTRY = (
    "Either",
    "Admits good honours bachelor's and/or taught master's holders to the 4-year PhD, and research master's (e.g., MPhil) holders to the 3-year PhD.",
    "The University offers 3-year and 4-year PhD programmes. Applicants who have a good Bachelor’s degree with honours and/or a taught Master’s degree will be considered for admission to a 4-year PhD programme, whereas those who already hold a research Master’s degree (e.g. MPhil) will only be considered for admission to a 3-year PhD programme.",
    "https://www.scifac.hku.hk/rpg/programme-info/phd",
)

rec.save_university(
    "hku",
    "The University of Hong Kong",
    "Hong Kong",
    "Hong Kong",
    "https://gradsch.hku.hk/prospective_students/application/admission_requirement",
    {
        "app_fee": (
            "780 HKD",
            "Non-refundable, non-transferable online application fee of HK$780 per application.",
            "Application fee for each application is HK$780.",
            "https://gradsch.hku.hk/prospective_students/application/faq_on_application",
        ),
        "fee_waiver": (
            "None",
            "HKU Graduate School states that application fee waivers will not be considered.",
            "Please note that a waiver of application fee will not be considered.",
            "https://gradsch.hku.hk/prospective_students/application/faq_on_application",
        ),
        "gre_general": (
            "Not required",
            "GRE General (or GMAT) is required only for Faculty of Business and Economics applicants, not for STEM PhD programs.",
            "Faculty of Business and Economics applicants are required to demonstrate their capability for graduate studies by obtaining satisfactory scores in the Graduate Management Admission Test (GMAT) or Graduate Record Examinations (GRE), taken within five years",
            "https://gradsch.hku.hk/prospective_students/application/admission_requirement",
        ),
        "toefl_min": (
            "4.5 (new scale)",
            "Minimum TOEFL iBT overall score is 4.5 (for tests taken from January 21, 2026 onwards) or 85 (for tests taken before January 21, 2026), taken in one single attempt within 2 years (Home Edition not accepted).",
            "TOEFL - Internet-based test (taken in one single attempt within 2 years) | An overall score of 85 or above (for tests taken before January 21, 2026) | An overall score of 4.5 or above (for tests taken from January 21, 2026 onwards)",
            "https://gradsch.hku.hk/prospective_students/application/admission_requirement",
        ),
        "ielts_min": (
            "6.5",
            "Minimum IELTS Academic overall band score is 6.5 with no sub-score lower than 6.0 (taken in one single attempt within 2 years; One Skill Retake not accepted).",
            "IELTS - Academic Module (taken in one single attempt within 2 years) | Other Faculties: Overall score – 6.5; All sub-score – not lower than 6",
            "https://gradsch.hku.hk/prospective_students/application/admission_requirement",
        ),
        "english_waiver": (
            "Conditional",
            "English proficiency tests are required only for qualifications obtained outside Hong Kong where the language of teaching and/or examination is not English; applicants whose prior university degree was taught and examined in English are exempt.",
            "An applicant who is seeking admission on the basis of a qualification from a university or comparable institution outside Hong Kong of which the language of teaching and/or examination is not English is required to obtain one of the followings:",
            "https://gradsch.hku.hk/prospective_students/application/admission_requirement",
            {
                "also": [
                    {
                        "quote": "A TOEFL/ IELTS score is not required if your first language is English or English was used as the medium of instruction in your undergraduate studies.",
                        "url": "https://www.cds.hku.hk/prospective-students/postgraduate/",
                    }
                ]
            },
        ),
    },
    notes="HKU offers PhD and MPhil degrees across 17 covered STEM fields in 2027-28; no Chemical Engineering PhD is offered (Faculty of Engineering and Graduate School list Civil Engineering, Computing and Data Science, Data and Systems Engineering, Electrical and Computer Engineering, Materials and Energy, Mechanical Engineering, Biomedical Engineering, and School of Innovation). Note Chemistry's department page (chemistry.hku.hk/study/postgraduate_students/2/) still lists a legacy HK$600 fee vs HKU Graduate School's HK$780 fee; and Department of IMSE (imse.hku.hk) was renamed Department of Data and Systems Engineering (dase.hku.hk) in September 2024.",
    checked=CHECKED,
)

# 1. CS
rec.save_program(
    "hku",
    "cs",
    "School of Computing and Data Science — Department of Computer Science",
    "https://www.cds.hku.hk/prospective-students/postgraduate/",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("computer science"),
        "supervisor": SUPERVISOR_OPTIONAL,
        "funding": (
            "Typical",
            "Full-time PhD students with 2:1 honours or above are normally eligible for Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026), subject to funding availability, plus HKU-PS/HKPF fellowships.",
            "other full-time PhD and MPhil students who hold a first degree with second-class honours first division (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (PGS) during the normative study period, subject to availability of funding. | The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
            "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
            {
                "also": [
                    {
                        "quote": "Various scholarships, fellowships, and conference/travel support are also available to enrich students’ learning experience and promote professional and personal development",
                        "url": "https://www.cds.hku.hk/prospective-students/postgraduate/",
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Offers 3-year (post-MPhil) and 4-year (post-bachelor's/taught master's) PhD programmes.",
            "The School of CDS offers the following research postgraduate programmes in both full-time and part-time modes: | Master of Philosophy (MPhil) | 3-year Doctor of Philosophy (PhD) | 4-year Doctor of Philosophy (PhD) | Computer Science – Doctor of Philosophy (PhD) and Master of Philosophy (MPhil)",
            "https://www.cds.hku.hk/prospective-students/postgraduate/",
            {
                "also": [
                    {
                        "quote": "All candidates with an honours Bachelor’s degree are eligible for PhD and MPhil admission.",
                        "url": "https://gradsch.hku.hk/prospective_students/application/faq_on_application",
                    }
                ]
            },
        ),
    },
    notes="HKU School of Computing and Data Science (CDS, formed July 2024) encompasses Computer Science and Statistics & Actuarial Science and also runs an early recruitment scheme (2026-08-31 for 2027-28 entry) alongside HKU Main Round (2026-12-01).",
    checked=CHECKED,
)

# 2. Statistics
rec.save_program(
    "hku",
    "statistics",
    "School of Computing and Data Science — Department of Statistics and Actuarial Science",
    "https://saasweb.hku.hk/programme/rpg/mphil-phd",
    {
        "deadline": (
            "2026-12-01",
            "Main Round deadline is December 1, 2026 (1st Clearing Round: April 30, 2027; 2nd Clearing Round: August 31, 2027).",
            "Main Round: 1 September 2026 – 1 December 2026 (HKT 23:59, GMT+8)",
            "https://saasweb.hku.hk/programme/rpg/mphil-phd",
            {"time_sensitive": "2026-12-01"},
        ),
        "gre_subject": GRE_NOT_REQ,
        "supervisor": (
            "Not required",
            "A tentative supervisor is appointed at commencement and pre-admission supervisor confirmation is optional.",
            "At the commencement, a tentative supervisor will be appointed, though changes in supervision may occur during the early coursework phase.",
            "https://saasweb.hku.hk/programme/rpg/mphil-phd",
            {
                "also": [
                    {
                        "quote": "Contact potential supervisor (optional)",
                        "url": "https://gradsch.hku.hk/prospective_students/application/how_to_apply",
                    }
                ]
            },
        ),
        "funding": (
            "Typical",
            "Full-time PhD students are eligible for Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026), subject to funding availability, plus HKU-PS/HKPF fellowships.",
            "Full-time students are eligible for financial support in the form of a Postgraduate Studentship (PGS) or part-time Demonstratorship, which carries with it some duties of conducting tutorials.",
            "https://saasweb.hku.hk/programme/rpg/mphil-phd",
            {
                "also": [
                    {
                        "quote": "The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
                        "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Direct PhD admission is considered for applicants with a First Class or 2A honours bachelor's degree in Statistics or Mathematics, or a relevant research master's degree.",
            "Direct entry to the PhD degree will normally be considered for students with (a) first class honours or 2A honours degree in Statistics or Mathematics from HKU or an equivalent institution, or (b) a research master's degree in Statistics, Probability and Actuarial Science.",
            "https://saasweb.hku.hk/programme/rpg/mphil-phd",
        ),
    },
    notes="Includes Statistics, Biostatistics, Probability, Machine Learning, and Actuarial Science; HKU CDS also ran an early recruitment scheme closing 2026-08-31 for 2027-28 entry.",
    checked=CHECKED,
)

# 3. Civil
rec.save_program(
    "hku",
    "civil",
    "Faculty of Engineering — Department of Civil Engineering",
    "https://www.civil.hku.hk/h4_pros_pg_MPhil_PhD.html",
    {
        "deadline": ENGG_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("civil engineering"),
        "supervisor": ENGG_SUPERVISOR,
        "funding": ENGG_FUNDING,
        "entry_route": ENGG_ENTRY,
    },
    notes="Research areas include Construction Engineering and Management, Geotechnical Engineering, Structural Engineering, Transportation Engineering, and Water and Environmental Engineering.",
    checked=CHECKED,
)

# 4. ECE
rec.save_program(
    "hku",
    "ece",
    "Faculty of Engineering — Department of Electrical and Computer Engineering",
    "https://ece.hku.hk/study/rpg/",
    {
        "deadline": ENGG_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("electrical and computer engineering"),
        "supervisor": ENGG_SUPERVISOR,
        "funding": ENGG_FUNDING,
        "entry_route": (
            "Either",
            "Honours bachelor's and/or taught master's holders are normally considered for the 4-year PhD; research master's holders enter the 3-year PhD.",
            "Students who hold a Bachelor’s degree with honours and/or a taught Master’s degree will normally be considered for admission to a 4-year PhD programme. Students who hold a research Master’s degree will be admitted to a 3-year PhD programme.",
            "https://ece.hku.hk/study/rpg/",
        ),
    },
    notes="Renamed from Department of Electrical and Electronic Engineering (EEE) to Department of Electrical and Computer Engineering (ECE) in February 2026; also offers departmental conference support grants and Clean Energy scholarships.",
    checked=CHECKED,
)

# 5. Mech
rec.save_program(
    "hku",
    "mech",
    "Faculty of Engineering — Department of Mechanical Engineering",
    "https://mech.hku.hk/research-postgraduate/",
    {
        "deadline": ENGG_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("mechanical engineering"),
        "supervisor": ENGG_SUPERVISOR,
        "funding": (
            "Typical",
            "Full-time PhD candidates may hold a University Postgraduate Scholarship (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026) or other fellowship (HKU-PS, HKPF), subject to funding availability.",
            "Full-time candidates may hold a University postgraduate studentship or another postgraduate studentship or scholarship which is intended to enable them to study on a full-time basis.",
            "https://mech.hku.hk/research-postgraduate/",
            {
                "also": [
                    {
                        "quote": "The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
                        "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Candidates without a research master's degree are considered for the 4-year PhD; those holding a research master's degree are considered for the 3-year PhD.",
            "Candidates without a research Master’s degree will be considered for admission to a 4-year PhD program, and those who hold research Master’s degrees will be considered for admission to a 3-year PhD program.",
            "https://mech.hku.hk/research-postgraduate/",
        ),
    },
    notes="Covers Design and Manufacture, Materials and Solids, Natural and Built Environment, Sound, Vibration and Control, Thermofluids, and Biomedical Engineering.",
    checked=CHECKED,
)

# 6. Data Science (DASE)
rec.save_program(
    "hku",
    "datasci",
    "Faculty of Engineering — Department of Data and Systems Engineering",
    "https://www.dase.hku.hk/teaching-and-learning/prospective-students/mphil-phd",
    {
        "deadline": ENGG_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("data science"),
        "supervisor": (
            "Recommended",
            "Prospective applicants are encouraged to contact supervisors regarding research topics before submitting an application.",
            "Potential applicants are encouraged to contact Supervisors on research topics.",
            "https://www.dase.hku.hk/teaching-and-learning/prospective-students/mphil-phd",
            {
                "also": [
                    {
                        "quote": "Discuss the proposed research areas with the potential supervisor(s) before submitting application.",
                        "url": "https://engg.hku.hk/Admissions/PhD-MPhil/Application-Procedures",
                    }
                ]
            },
        ),
        "funding": ENGG_FUNDING,
        "entry_route": ENGG_ENTRY,
    },
    notes="Formerly Department of Industrial and Manufacturing Systems Engineering (renamed DASE in September 2024; legacy imse.hku.hk fails SSL). School of Computing and Data Science (cds.hku.hk) also supervises AI and Data Science PhD research.",
    checked=CHECKED,
)

# 7. Materials (MSE)
rec.save_program(
    "hku",
    "materials",
    "Faculty of Engineering — Department of Materials and Energy",
    "https://mse.hku.hk/",
    {
        "deadline": ENGG_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("materials science"),
        "supervisor": ENGG_SUPERVISOR,
        "funding": ENGG_FUNDING,
        "entry_route": ENGG_ENTRY,
    },
    notes="Department of Materials and Energy (MSE) was established August 1, 2026 and is listed by HKU Graduate School as admitting MPhil/PhD students; mse.hku.hk/teaching-learning/rpg/ currently displays 'Coming soon...'.",
    checked=CHECKED,
)

# 8. BME (SBME)
rec.save_program(
    "hku",
    "bme",
    "School of Biomedical Engineering",
    "https://sbme.hku.hk/",
    {
        "deadline": ENGG_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("biomedical engineering"),
        "supervisor": ENGG_SUPERVISOR,
        "funding": ENGG_FUNDING,
        "entry_route": ENGG_ENTRY,
    },
    notes="School of Biomedical Engineering (SBME, established March 2025 across Dentistry, Engineering, Medicine, and Science) is listed by HKU Graduate School (gradsch.hku.hk/prospective_students/research_areas) as admitting MPhil/PhD students; ECE and Mechanical Engineering also list Biomedical Engineering PhD/MPhil fields of study (engg.hku.hk/Teaching-Learning/PhD-MPhil/Fields-of-Study).",
    checked=CHECKED,
)

# 9. Biology
rec.save_program(
    "hku",
    "biology",
    "Faculty of Science — School of Biological Sciences",
    "https://www.biosch.hku.hk/teaching/research-postgraduate-programmes/",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("biology"),
        "supervisor": (
            "Recommended",
            "School of Biological Sciences strongly recommends identifying and emailing a potential supervisor in Ecology & Biodiversity or Molecular & Cell Biology to check availability and develop a project before applying.",
            "Applicants are strongly recommended to browse the web pages of each Research Area: Area of Ecology & Biodiversity and Area of Molecular & Cell Biology to identify a staff member who is carrying out research closest to their interests. You should then contact them by email to ascertain whether the staff member intends to take on a new student this year, and whether you are suitable.",
            "https://www.biosch.hku.hk/teaching/research-postgraduate-programmes/",
        ),
        "funding": SCIFAC_FUNDING,
        "entry_route": SCIFAC_ENTRY,
    },
    notes="Covers Ecology & Biodiversity and Molecular & Cell Biology.",
    checked=CHECKED,
)

# 10. Chemistry
rec.save_program(
    "hku",
    "chemistry",
    "Faculty of Science — Department of Chemistry",
    "https://chemistry.hku.hk/study/postgraduate_students/1/",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("chemistry"),
        "supervisor": (
            "Recommended",
            "Chemistry strongly encourages prospective applicants to communicate with one or more potential supervisors before applying.",
            "Before application, you are strongly encouraged to explore the research interests of our Research Supervisors and to communicate with one or more potential supervisors, who will be able to discuss further details about their research programs and their projected number of RPg intakes in the upcoming academic year.",
            "https://chemistry.hku.hk/study/postgraduate_students/2/",
        ),
        "funding": SCIFAC_FUNDING,
        "entry_route": (
            "Either",
            "Admits First Class Honours bachelor's holders to the 4-year PhD, and research MPhil holders to the 3-year PhD (2A honours bachelor's holders enter via MPhil or 4-year PhD transfer).",
            "A B. Sc. degree with IIA honours or above from this University or an equivalent qualification from a comparable institution. | An M. Phil. (Research) degree from this University or an equivalent qualification from a comparable institution. | A B. Sc. degree with 1st Honours from this University or an equivalent qualification from a comparable institution.",
            "https://chemistry.hku.hk/study/postgraduate_students/1/",
        ),
    },
    notes="Department webpage (chemistry.hku.hk/study/postgraduate_students/2/) still mentions an outdated HK$600 application fee; central Graduate School FAQ states HK$780.",
    checked=CHECKED,
)

# 11. Earth
rec.save_program(
    "hku",
    "earth",
    "Faculty of Science — Department of Earth and Planetary Sciences",
    "https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/general_information/",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("earth and planetary sciences"),
        "supervisor": (
            "Required",
            "Department of Earth and Planetary Sciences states it is essential for prospective students to contact potential supervisors ahead of application submission to discuss project details and confirm availability.",
            "It is essential for prospective students to contact potential supervisor(s) ahead of application submission in order to determine if he/she/they are interested in admitting a new student and to discuss project details.",
            "https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/how_to_apply/",
        ),
        "funding": (
            "Guaranteed",
            "Department of Earth and Planetary Sciences guarantees full financial support during study for formally registered research students.",
            "A formally registered research student will have full financial support during his/her study at the University of Hong Kong.",
            "https://www.earthsciences.hku.hk/education/postgraduate_students/research_postgraduates/fellowships/",
        ),
        "entry_route": SCIFAC_ENTRY,
    },
    notes="Applications require a research proposal; full financial support guaranteed for registered research students.",
    checked=CHECKED,
)

# 12. Math
rec.save_program(
    "hku",
    "math",
    "Faculty of Science — Department of Mathematics",
    "https://hkumath.hku.hk/web/prospective/p-pg-admission.php",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": GRE_NOT_REQ,
        "supervisor": (
            "Recommended",
            "Department of Mathematics lists connecting with a potential supervisor under its application preparation steps.",
            "Tips for Application Preparation | Connect with a potential supervisor",
            "https://hkumath.hku.hk/web/prospective/p-pg-admission.php",
            {
                "also": [
                    {
                        "quote": "Contact potential supervisor (optional)",
                        "url": "https://gradsch.hku.hk/prospective_students/application/how_to_apply",
                    }
                ]
            },
        ),
        "funding": SCIFAC_FUNDING,
        "entry_route": SCIFAC_ENTRY,
    },
    notes="Department admission page (hkumath.hku.hk/web/prospective/p-pg-admission.php) still displays sample 2023-24 dates following the same December 1 Main Round schedule.",
    checked=CHECKED,
)

# 13. Physics
rec.save_program(
    "hku",
    "physics",
    "Faculty of Science — Department of Physics",
    "https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": GRE_NOT_REQ,
        "supervisor": (
            "Recommended",
            "Students are encouraged to contact prospective supervisors directly to obtain detailed project information.",
            "Students are encouraged to contact their prospective supervisors directly to obtain the further detailed information of the project.",
            "https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/",
        ),
        "funding": (
            "Typical",
            "Full-time PhD students with 2:1 honours (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026).",
            "Full-time MPhil and PhD students who hold a first degree with second-class honours first division (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (HK$19,135 per month) during the normative study period.",
            "https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/",
            {
                "also": [
                    {
                        "quote": "A PGS holder whose PhD probationary candidature has been confirmed will receive a higher PGS rate (HK$19,655, wef 1/9/2026)",
                        "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
                    }
                ]
            },
        ),
        "entry_route": SCIFAC_ENTRY,
    },
    checked=CHECKED,
)

# 14. Astronomy
rec.save_program(
    "hku",
    "astronomy",
    "Faculty of Science — Department of Physics (Astronomy and Astrophysics)",
    "https://www.physics.hku.hk/prospective-students/rpg-admission",
    {
        "deadline": CENTRAL_DEADLINE,
        "gre_subject": GRE_NOT_REQ,
        "supervisor": (
            "Recommended",
            "Students are encouraged to contact prospective supervisors directly to obtain detailed project information.",
            "Students are encouraged to contact their prospective supervisors directly to obtain the further detailed information of the project.",
            "https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/",
        ),
        "funding": (
            "Typical",
            "Full-time PhD students with 2:1 honours (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026).",
            "Full-time MPhil and PhD students who hold a first degree with second-class honours first division (or equivalent) or above are normally considered eligible to receive a Postgraduate Scholarship (HK$19,135 per month) during the normative study period.",
            "https://www.physics.hku.hk/graduate_studies/for_prospective_students/research_postgraduate_program/",
        ),
        "entry_route": SCIFAC_ENTRY,
    },
    notes="Astronomy and Astrophysics Group in the Department of Physics (and affiliated Hong Kong Institute for Astronomy and Astrophysics, HKIAA, and Laboratory for Space Research, LSR).",
    checked=CHECKED,
)

# 15. Environment (Geography)
rec.save_program(
    "hku",
    "environment",
    "Faculty of Social Sciences — Department of Geography",
    "https://www.geog.hku.hk/mphil-phd",
    {
        "deadline": (
            "2026-12-01",
            "Main Round application deadline is December 1, 2026 (HKT 23:59 GMT+8; HKPF deadline December 1, 2026 at noon HKT; clearing rounds April 30 and August 31, 2027).",
            "December 1, 2026 (Main Round Application, HKT 23:59 GMT+8)",
            "https://www.geog.hku.hk/mphil-phd",
            {"time_sensitive": "2026-12-01"},
        ),
        "gre_subject": NO_SUBJECT_TEST("environmental and geographical sciences"),
        "supervisor": (
            "Recommended",
            "Department of Geography advises applicants to contact prospective advisors at their earliest convenience before applying.",
            "*Please contact your prospective advisor at your earliest convenience",
            "https://www.geog.hku.hk/mphil-phd",
        ),
        "funding": (
            "Typical",
            "Registered MPhil and PhD students are eligible to receive Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026) and HKU-PS/HKPF fellowships, subject to funding availability.",
            "Students registering for MPhil and PhD degrees are eligible to be selected to receive the Postgraduate Scholarship.",
            "https://www.geog.hku.hk/mphil-phd",
            {
                "also": [
                    {
                        "quote": "The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
                        "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Offers 3-year (post-research master's) and 4-year (post-honours bachelor's) PhD programmes.",
            "the Department of Geography at The Universityt of Hong Kong offers research postgraduate programmes leading to Master of Philosophy (MPhil) (2-year) and Doctor of Philosophy (PhD) (3-year and 4-year) degrees",
            "https://www.geog.hku.hk/mphil-phd",
            {
                "also": [
                    {
                        "quote": "All candidates with an honours Bachelor’s degree are eligible for PhD and MPhil admission.",
                        "url": "https://gradsch.hku.hk/prospective_students/application/faq_on_application",
                    }
                ]
            },
        ),
    },
    notes="Covers physical geography, climate change, carbon sequestration, urban environment, and marine/remote sensing topics; Faculty of Science's Swire Institute of Marine Science (SWIMS) and Department of Earth and Planetary Sciences also offer environmental/marine PhD supervision.",
    checked=CHECKED,
)

# 16. Biomed (SBMS)
rec.save_program(
    "hku",
    "biomed",
    "LKS Faculty of Medicine — School of Biomedical Sciences",
    "https://www.sbms.hku.hk/study",
    {
        "deadline": MED_DEADLINE,
        "gre_subject": NO_SUBJECT_TEST("biomedical sciences"),
        "supervisor": SUPERVISOR_OPTIONAL,
        "funding": (
            "Typical",
            "Eligible full-time PhD students receive Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026), HKU-PS, or HKPF, plus HKUMed entrance scholarships and travel grants.",
            "Financial support is a key feature, with eligible students receiving prestigious scholarships such as the Hong Kong PhD Fellowship (HKPF) or HKU Presidential PhD Scholarship (HKU-PS), offering monthly stipends, cash awards, and tuition fee waivers. The Postgraduate Scholarship (PGS) provides additional financial assistance.",
            "https://www.sbms.hku.hk/study",
            {
                "also": [
                    {
                        "quote": "The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
                        "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Admits First Class Honours bachelor's holders or 2:1 honours + taught master's holders to the 4-year PhD, and 2:1 honours + research MPhil holders to the 3-year PhD.",
            "3-year PhD: | Bachelor's degree with Honours at Second Class Division I or above, AND a research Master's degree (MPhil). | 4-year PhD: | Bachelor's degree at First Class Honours (preferably with research experience); | Bachelor's degree with Honours at Second Class Division I, AND a taught Master's degree (preferably with Second Class Honours Division I).",
            "https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/key-info",
        ),
    },
    checked=CHECKED,
)

# 17. Neuro (SBMS Neuroscience)
rec.save_program(
    "hku",
    "neuro",
    "LKS Faculty of Medicine — School of Biomedical Sciences (Neuroscience)",
    "https://www.sbms.hku.hk/research",
    {
        "deadline": MED_DEADLINE,
        "gre_subject": GRE_NOT_REQ,
        "supervisor": SUPERVISOR_OPTIONAL,
        "funding": (
            "Typical",
            "Eligible full-time PhD students receive Postgraduate Scholarships (HK$19,135/month; HK$19,655/month after confirmation, wef 1/9/2026), HKU-PS, or HKPF, plus HKUMed entrance scholarships and travel grants.",
            "Financial support is a key feature, with eligible students receiving prestigious scholarships such as the Hong Kong PhD Fellowship (HKPF) or HKU Presidential PhD Scholarship (HKU-PS), offering monthly stipends, cash awards, and tuition fee waivers. The Postgraduate Scholarship (PGS) provides additional financial assistance.",
            "https://www.sbms.hku.hk/study",
            {
                "also": [
                    {
                        "quote": "The basic level of scholarship is HK$19,135 per month (wef 1/9/2026).",
                        "url": "https://gradsch.hku.hk/prospective_students/fees_scholarships_and_financial_support/postgraduate_scholarships",
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Admits First Class Honours bachelor's holders or 2:1 honours + taught master's holders to the 4-year PhD, and 2:1 honours + research MPhil holders to the 3-year PhD.",
            "3-year PhD: | Bachelor's degree with Honours at Second Class Division I or above, AND a research Master's degree (MPhil). | 4-year PhD: | Bachelor's degree at First Class Honours (preferably with research experience); | Bachelor's degree with Honours at Second Class Division I, AND a taught Master's degree (preferably with Second Class Honours Division I).",
            "https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/key-info",
        ),
    },
    notes="School of Biomedical Sciences conducts Neuroscience PhD research (neural circuits, neurodevelopment, neurodegeneration) under HKUMed without a GRE Subject Test. Separately, the Department of Psychology offers a PhD track in Human Neuroscience and Artificial Intelligence (https://psychology.hku.hk/research-degrees-mphil-phd/), for which applicants whose first degree is not in Psychology must submit a minimum score of 550 on the GRE Subject Test in Psychology.",
    checked=CHECKED,
)

print("Saved HKU + 17 programs to data/staging")
