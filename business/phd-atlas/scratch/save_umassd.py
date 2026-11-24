import os
import sys
from pathlib import Path

os.environ["ATLAS_OUT"] = "data/staging"
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import rec

CHECKED = "2026-11-14"
UID = "umassd"

APPLY_URL = "https://www.umassd.edu/graduate/apply/"
DATES_URL = "https://www.umassd.edu/graduate/dates/"
FAQS_URL = "https://www.umassd.edu/graduate/faqs/"
LANG_URL = "https://www.umassd.edu/graduate/international-students/language-test-waiver/"
ASSIST_URL = "https://www.umassd.edu/graduate/assistantships/"
REQ_URL = "https://www.umassd.edu/graduate/apply/program-specific-requirements/"
ETS_SUBJ_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"

ETS_SUBJ_QUOTE = (
    "The GRE Subject Tests in Mathematics, Physics and Psychology measure "
    "undergraduate achievement in a particular field of study"
)

DEADLINE_QUOTE = (
    "For fall applicants, the date for priority consideration for university assistantships or fellowships is January 15. | "
    "Application closing dates: | "
    "International application: July 15 | "
    "Note: International students may only apply for fall or spring."
)

DEADLINE_FIELD = (
    "2027-07-15",
    "Fall 2027 international application closing date is July 15, 2027 (Spring 2027 international closing date: December 15; Summer not open to international students). Priority consideration for university assistantships or fellowships is January 15, 2027.",
    DEADLINE_QUOTE,
    DATES_URL,
    {"inferred": "year", "time_sensitive": "2027-01-15"},
)

rec.save_university(
    UID,
    "University of Massachusetts Dartmouth",
    "USA",
    "Massachusetts",
    APPLY_URL,
    {
        "app_fee": (
            "60 USD",
            "$60 non-refundable graduate application fee per program application.",
            "$60 application fee (non-refundable)",
            APPLY_URL,
        ),
        "fee_waiver": (
            "None",
            "UMass Dartmouth states that regardless of circumstances, the graduate application fee cannot be waived or deferred.",
            "Do you offer graduate application fee waivers or deferrals for prospective students with financial trouble? | No, regardless of the circumstances, the application fee cannot be waived or deferred.",
            FAQS_URL,
        ),
        "gre_general": (
            "Not required",
            "GRE General is not required for most graduate programs (institution code 3786), though Biomedical Engineering & Biotechnology and Electrical Engineering require it unless waived by program criteria and Marine Science & Technology lists it as optional.",
            "GRE/GMAT (not required for most programs, see program requirements for more information)",
            APPLY_URL,
            {
                "also": [
                    {
                        "quote": "Only a few programs require the GRE. For specific programs, please refer to the Graduate Application and Program-specific Requirements.",
                        "url": FAQS_URL,
                    }
                ]
            },
        ),
        "toefl_min": (
            "4 (new scale)",
            "University minimum is 4 on the post-1/21/2026 TOEFL iBT 1-6 scale (72 on the legacy 0-120 iBT scale) for general admission and 79 legacy / 4 new scale for teaching assistantship consideration; Duolingo 95 or PTE Academic 52 also accepted unless excluded by program. Note: Chemistry & Biochemistry and Electrical Engineering require 80 (4 new scale), and Engineering & Applied Science (EAS) requires 90 (4.5 new scale).",
            "We require an overall/total minimum score of 72 on the TOEFL iBT (New TOEFL 2026 score of 4) or BAND 6.0 on the IELTS Academic or a 52 on the Pearsons PTE Academic for entrance to any program and a minimum score of 79 on the TOEFL iBT (New TOEFL 2026 score of 4) or BAND 6.5 on the IELTS Academic for consideration for a teaching assistantship.",
            LANG_URL,
        ),
        "ielts_min": (
            "6.0",
            "University minimum IELTS Academic band is 6.0 for general admission and 6.5 for teaching assistantship consideration; Chemistry & Biochemistry, Electrical Engineering, and Engineering & Applied Science (EAS) require 6.5.",
            "We require an overall/total minimum score of 72 on the TOEFL iBT (New TOEFL 2026 score of 4) or BAND 6.0 on the IELTS Academic or a 52 on the Pearsons PTE Academic for entrance to any program and a minimum score of 79 on the TOEFL iBT (New TOEFL 2026 score of 4) or BAND 6.5 on the IELTS Academic for consideration for a teaching assistantship.",
            LANG_URL,
        ),
        "english_waiver": (
            "No",
            "An English-medium degree from India does not qualify for an English proficiency waiver because India is not on the exempt-countries list and UMass Dartmouth explicitly states Medium of Instruction (MOI) does not meet exemption requirements (waived only with a degree from the U.S. or a listed English-speaking country, 4 named American universities abroad, or >=2 semesters of full-time U.S. college study).",
            "This is required of any applicant who did not earn a bachelor’s degree or higher degree from an accredited academic institution in the U.S. or accepted English-speaking country (see below). | MOI (Medium of Instruction) does not meet our exemption requirements. | * Countries: Australia, Belize, Botswana, Canada (except Quebec), Caribbean English-speaking countries, Gambia, Ghana, Guyana, Ireland, Kenya, Lesotho, Liberia, Malawi, Namibia, New Zealand, Nigeria, Scotland, Sierra Leone, Singapore, South Africa, Swaziland, Tanzania, Uganda, United Kingdom, Zambia, Zimbabwe.",
            LANG_URL,
        ),
    },
    notes=(
        "10 STEM Ph.D. programs mapped: Biomedical Engineering & Biotechnology, Chemistry & Biochemistry, Electrical Engineering (including Computer Engineering option), Integrative Biology, Marine Science & Technology (SMAST), plus 5 Engineering & Applied Science (EAS) Ph.D. tracks (Computer Science & Information Science, Machine Learning & Data Science, Computational Science & Engineering, Applied Mechanics & Materials [plus Industrial & Systems Engineering note], and Infrastructure, Environmental, & Fluids Engineering). Excluded non-STEM/clinical/education doctorates: Educational Leadership & Policy Studies Ed.D., Law J.D., Luso-Afro-Brazilian Studies & Theory Ph.D., Nursing Ph.D. and DNP, and STEM Education Ph.D.; Physics, Civil & Environmental Engineering, and Psychology offer master's degrees only as standalone programs (physics/civil research options exist within EAS Ph.D.)."
    ),
    checked=CHECKED,
)

# 1. BME
BME_PAGE = "https://www.umassd.edu/programs/biomedical-engineering-biotechnology/"
BME_CAT = "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12705"
rec.save_program(
    UID,
    "bme",
    "Department of Bioengineering",
    BME_PAGE,
    {
        "deadline": (
            "2027-07-15",
            "Fall 2027 international application closing date is July 15, 2027 (Spring closing: December 15). University priority date for assistantships/fellowships is January 15, 2027; the BMEBT catalog additionally notes a March 15th deadline for teaching/research assistantship applications.",
            DEADLINE_QUOTE,
            DATES_URL,
            {
                "inferred": "year",
                "time_sensitive": "2027-01-15",
                "also": [
                    {
                        "quote": "Applicants desiring teaching or research assistantships should submit completed applications by March 15th.",
                        "url": BME_CAT,
                    }
                ],
            },
        ),
        "gre_general": (
            "Required",
            "GRE General is required (catalog notes a 300 minimum combined V+Q guideline), though the program page states GRE is waived (but strongly recommended) for applicants with cumulative baccalaureate GPA > 3.00 and the catalog notes waiver by petition for holders of an accredited U.S. graduate degree.",
            "GRE is required, but waived (but strongly recommended) for applicants with cumulative baccalaureate degree GPA > 3.00.",
            BME_PAGE,
            {
                "also": [
                    {
                        "quote": "Applicants accepted into the program should present a minimum Graduate Record Exam (GRE) combined verbal + quantitative score of 300. | The GRE can be waived by petition to the AACC for applicants with a prior graduate degree from an accredited US institution; an application without the GRE must demonstrate exceptional potential.",
                        "url": BME_CAT,
                    }
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Biomedical Engineering or Biotechnology (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_SUBJ_URL,
        ),
        "supervisor": (
            "Recommended",
            "Applicants are strongly encouraged to contact participating faculty before applying to explore specialization fit and report those contacts in their Statement of Purpose; admissions are decided by the campus AACC, and acceptance is subject to availability of appropriate advisors.",
            "Applicants are strongly encouraged to contact participating faculty to explore how they might fit into a specific specialization option before submitting their application and to report on the results of those contacts in their Statement of Purpose (see below). | Admissions decisions are made at the campus level, under the purview of each campus’s Admissions/Advising/Curriculum Committee (AACC). | Acceptance into the program is subject to the availability of appropriate advisors.",
            BME_CAT,
            {
                "also": [
                    {
                        "quote": "indicate your specific areas of interest within Biomedical Engineering and Biotechnology so that an appropriate fit in the program can be determined. If you have a specific interest in working with one or more of the program’s faculty, describe that specific interest and identify those faculty members.",
                        "url": BME_PAGE,
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            "A limited number of graduate assistantships (predominantly Research Assistantships) are available on a competitive basis; applicants are invited to contact faculty about RA opportunities and apply by January 15 (university priority) / March 15 (program assistantship deadline).",
            "A limited number of assistantships are available on a competitive basis. This award is subject to the work needs of the position and department, your satisfactory performance of duties, your academic record, and availability of funds, and may be subject to change.",
            BME_PAGE,
            {
                "also": [
                    {
                        "quote": "A limited number of assistantships are available on a competitive basis. Applicants desiring teaching or research assistantships should submit completed applications by March 15th. | Almost all assistantship support in this program comes in the form of Research Assistantships. Applicants are invited to contact faculty about opportunities for Research Assistantships.",
                        "url": BME_CAT,
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Accepts both bachelor's and master's holders in life sciences, physical sciences, or engineering (minimum 3.0 GPA and 2 semesters of calculus); MS entrants may receive Advanced Standing (>=44 credits minimum vs. 63 credits from BS).",
            "Individuals holding a bachelor’s or master’s degree in the life sciences or engineering/physical science fields (or the U.S. baccalaureate equivalents from a foreign institution) are encouraged to apply.",
            BME_PAGE,
            {
                "also": [
                    {
                        "quote": "Applications will be accepted from individuals holding appropriate bachelor’s degrees or master’s degrees (or the US baccalaureate equivalents from a foreign institution). | Students who join the program with an earned master’s degree may receive Advanced Standing in the doctoral program.",
                        "url": BME_CAT,
                    }
                ]
            },
        ),
    },
    notes="Intercampus UMass BMEBT program (Boston, Dartmouth, Lowell, UMass Chan Medical); applicants apply directly to their intended home campus.",
    checked=CHECKED,
    name="Biomedical Engineering and Biotechnology Ph.D.",
)

# 2. Chemistry
CHEM_PAGE = "https://www.umassd.edu/programs/chemistry-biochemistry-phd/"
CHEM_CAT = "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12724"
rec.save_program(
    UID,
    "chemistry",
    "Department of Chemistry & Biochemistry",
    CHEM_PAGE,
    {
        "deadline": DEADLINE_FIELD,
        "toefl_min": (
            "4 (new scale)",
            "Department requires TOEFL iBT 80 (4 on the post-1/21/2026 1-6 scale), Duolingo 110, or PTE Academic 58 — higher than the university general minimum of 72.",
            "International students should have a minimum English Proficiency score of TOEFL iBT 80 (New TOEFL 2026 score of 4), IELTS 6.5, Duolingo 110 or the Pearsons PTE Academic 58.",
            CHEM_PAGE,
        ),
        "ielts_min": (
            "6.5",
            "Department requires IELTS 6.5 minimum (higher than the university general minimum of 6.0).",
            "International students should have a minimum English Proficiency score of TOEFL iBT 80 (New TOEFL 2026 score of 4), IELTS 6.5, Duolingo 110 or the Pearsons PTE Academic 58.",
            CHEM_PAGE,
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Chemistry (ETS discontinued the Chemistry Subject Test in May 2023; offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_SUBJ_URL,
        ),
        "supervisor": (
            "Not stated",
            "Program and catalog pages do not state whether a supervisor must be secured before admission.",
            "",
            CHEM_PAGE,
        ),
        "funding": (
            "Competitive",
            "A limited number of graduate research and teaching assistantships are available on a competitive basis.",
            "You will be eligible for graduate assistantships for research and/or teaching activities. | A limited number of assistantships are available on a competitive basis. This award is subject to the work needs of the position and department, your satisfactory performance of duties, your academic record, and availability of funds, and may be subject to change.",
            CHEM_PAGE,
        ),
        "entry_route": (
            "Either",
            "Admits holders of a bachelor's degree (minimum 55 credits required beyond the BS) or an earned master's degree in chemistry or biochemistry (eligible for Advanced Standing with a minimum of 8 credits from formal courses).",
            "A minimum of 55 course credits is required beyond the BS, including at least 24 credits of formal courses, at least 27 credits of doctoral dissertation research, and 4 credits of Graduate Seminar. | If you enter the program with an earned master's degree in chemistry or biochemistry you may be eligible to receive Advanced Standing in the doctoral program. You will complete a minimum of 8 credits from formal courses.",
            CHEM_PAGE,
        ),
    },
    notes="2026-2027 catalog entry (poid=12724) confirms Advanced Standing for earned MS holders (minimum 8 formal course credits).",
    checked=CHECKED,
    name="Chemistry and Biochemistry Ph.D.",
)

# 3. ECE
ECE_PAGE = "https://www.umassd.edu/programs/electrical-engineering-phd/"
ECE_CAT = "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12719"
rec.save_program(
    UID,
    "ece",
    "Department of Electrical & Computer Engineering",
    ECE_PAGE,
    {
        "deadline": DEADLINE_FIELD,
        "gre_general": (
            "Required",
            "GRE General is required for international applicants; waived only for students with a bachelor's or graduate degree from an institution in the United States.",
            "GRE is required. The GRE is waived for students with a bachelor's or graduate degree from an institution in the United States.",
            ECE_PAGE,
        ),
        "toefl_min": (
            "4 (new scale)",
            "Department requires TOEFL iBT 80 (4 on the post-1/21/2026 1-6 scale), Duolingo 110, or PTE Academic 58.",
            "International students should have a minimum English Proficiency score of TOEFL iBT 80 (New TOEFL 2026 score of 4), IELTS 6.5, Duolingo 110 or the Pearsons PTE Academic 58.",
            ECE_PAGE,
        ),
        "ielts_min": (
            "6.5",
            "Department requires IELTS 6.5 minimum (higher than the university general minimum of 6.0).",
            "International students should have a minimum English Proficiency score of TOEFL iBT 80 (New TOEFL 2026 score of 4), IELTS 6.5, Duolingo 110 or the Pearsons PTE Academic 58.",
            ECE_PAGE,
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Electrical or Computer Engineering (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_SUBJ_URL,
        ),
        "supervisor": (
            "Not required",
            "Admissions are evaluated competitively and exceptions are approved by the ECE Graduate Committee rather than requiring an advisor pre-commitment (only BS/MS applicants are encouraged to include a faculty advisor letter).",
            "However, students who do not meet minimum requirements—but who otherwise show evidence of strong academic, professional, or research ability—may be accepted upon approval of the ECE Graduate Committee. | BS/MS applicants are encouraged to include a recommendation from a department faculty member willing to advise their graduate research.",
            ECE_PAGE,
        ),
        "funding": (
            "Competitive",
            "A limited number of graduate assistantships are available on a competitive basis.",
            "A limited number of assistantships are available on a competitive basis. This award is subject to the work needs of the position and department, your satisfactory performance of duties, your academic record, and availability of funds, and may be subject to change.",
            ECE_PAGE,
        ),
        "entry_route": (
            "Either",
            "Encourages both master's holders (min. 18 credits beyond MS) and direct bachelor's holders in EE, CompE, or a closely related discipline (min. 48 credits beyond BS, exclusive of dissertation research).",
            "Students possessing a master's degree and a strong academic background in electrical engineering, computer engineering, or similar disciplines are encouraged to apply. | While most students admitted to the doctoral program hold a master’s degree, applicants with a bachelor’s degree in electrical engineering, computer engineering, or a closely related discipline are also encouraged to apply for direct admission to the PhD program.",
            ECE_PAGE,
        ),
    },
    notes="Offers two formal Ph.D. options: Electrical Engineering and Computer Engineering (catalog poid=12719).",
    checked=CHECKED,
    name="Electrical Engineering Ph.D. (and Computer Engineering Option)",
)

# 4. Biology
BIO_PAGE = "https://www.umassd.edu/programs/integrative-biology-phd/"
BIO_CAT = "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12767"
rec.save_program(
    UID,
    "biology",
    "Department of Biology",
    BIO_PAGE,
    {
        "deadline": DEADLINE_FIELD,
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Biology (ETS discontinued Biochemistry, Cell & Molecular Biology in 2016 and Biology in 2021; offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_SUBJ_URL,
        ),
        "supervisor": (
            "Not stated",
            "Program and catalog pages do not state whether an advisor must be contacted or secured prior to admission (dissertation committee is formed after completing formal coursework).",
            "",
            BIO_PAGE,
        ),
        "funding": (
            "Competitive",
            "A limited number of graduate assistantships are available on a competitive basis.",
            "A limited number of assistantships are available on a competitive basis. This award is subject to the work needs of the position and department, your satisfactory performance of duties, your academic record, and availability of funds, and may be subject to change.",
            BIO_PAGE,
        ),
        "entry_route": (
            "Either",
            "University Graduate Admissions FAQs confirm that UMass Dartmouth doctoral programs consider applicants with either a bachelor's degree only or a bachelor's and master's degree (55 total credits required for Integrative Biology Ph.D.).",
            "Can I apply for a PhD program with only a bachelor's degree? | Yes. Our doctoral programs can consider applicants with a bachelor's only or a bachelor's and a master's.",
            FAQS_URL,
        ),
    },
    notes="Note: Language Proficiency page specifies that Biology/Marine Biology does not accept Duolingo (use TOEFL, IELTS, or PTE Academic). Graduate Admissions FAQs mention an outdated Subject GRE recommendation for Biology/Marine Biology and Research Psychology assistantships, though ETS discontinued the Biology Subject Test in 2021.",
    checked=CHECKED,
    name="Integrative Biology Ph.D.",
)

# 5. Marine Science (Environment)
ENV_PAGE = "https://www.umassd.edu/programs/marine-science-phd/"
SMAST_ADM = "https://www.umassd.edu/smast/admissions--aid/"
SMAST_FUND = "https://www.umassd.edu/smast/admissions--aid/assistantships-scholarships--fellowships/"
rec.save_program(
    UID,
    "environment",
    "School for Marine Science and Technology (SMAST)",
    ENV_PAGE,
    {
        "deadline": DEADLINE_FIELD,
        "gre_general": (
            "Optional",
            "GRE General is optional for Marine Science and Technology Ph.D. applicants.",
            "GRE is optional.",
            ENV_PAGE,
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Marine Science or Environmental/Ocean Science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_SUBJ_URL,
        ),
        "supervisor": (
            "Recommended",
            "SMAST advises applicants to take an active role in contacting potential faculty advisors and seeking funding before applying.",
            "Applicants should take an active role in contacting faculty member(s) who could potentially advise them, as well as make an effort to seek funding before applying.",
            ENV_PAGE,
            {
                "also": [
                    {
                        "quote": "Applicants should take an active role in contacting faculty member(s) who could potentially advise them, as well as make an effort to seek funding before applying.",
                        "url": SMAST_ADM,
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            "Limited teaching/research assistantships and competitive fellowships are available (including Graduate Research Assistantships with stipend + tuition waiver, First-Year Doctoral Fellows at $16,000 + full tuition/fee waiver, and Distinguished Doctoral Fellows at $24,000/yr + waivers for outstanding applicants).",
            "A limited number of assistantships are available on a competitive basis. This award is subject to the work needs of the position and department, your satisfactory performance of duties, your academic record, and availability of funds, and may be subject to change.",
            ENV_PAGE,
            {
                "also": [
                    {
                        "quote": "The Distinguished Doctoral Fellows annually receive a $24,000 stipend plus full tuition and Curriculum Support Fee waivers. | The First Year Doctoral Fellows receive one year of support that includes a stipend of $16,000 plus a full tuition and Curriculum Support Fee waiver. | The School for Marine Science & Technology also offers graduate research assistantships",
                        "url": SMAST_FUND,
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Admits candidates holding an undergraduate or graduate degree (minimum 3.00 GPA, strong natural sciences/engineering background, calculus encouraged); direct Ph.D. entry from a bachelor's expects exceptional credentials, and some bachelor's entrants may complete an M.S. first.",
            "Completion of an undergraduate or graduate degree with a GPA of 3.00 or higher.",
            ENV_PAGE,
            {
                "also": [
                    {
                        "quote": "Candidates may apply for admission at either the master's or PhD (doctoral) level. | Students admitted directly into the PhD (doctoral) program are expected to have exceptional academic credentials and/or work experience. | Students entering with a bachelor’s degree may be required to complete the requirements of a master's degree before admission to the doctoral program.",
                        "url": SMAST_ADM,
                    }
                ]
            },
        ),
    },
    notes="UMass systemwide Intercampus Marine Science (IMS) / SMAST Ph.D. program; also offers a University of Sao Paulo Dual Ph.D. option.",
    checked=CHECKED,
    name="Marine Science and Technology Ph.D.",
)

# 6-10. Five EAS PhD tracks (distinct catalog URLs as program_page, common EAS admissions rules)
EAS_PAGE = "https://www.umassd.edu/programs/engineering-applied-science-phd/"

def eas_common_fields(gre_subject_tuple):
    return {
        "deadline": DEADLINE_FIELD,
        "gre_general": (
            "Not required",
            "GRE General is waived for Engineering and Applied Science (EAS) Ph.D. applicants.",
            "GRE is waived.",
            EAS_PAGE,
        ),
        "toefl_min": (
            "4.5 (new scale)",
            "EAS Ph.D. requires TOEFL iBT 90 (4.5 on the post-1/21/2026 1-6 scale), Duolingo 120, or PTE 60 — higher than the university minimum of 72.",
            "International students should have a minimum English Proficiency score of TOEFL iBT 90 (New TOEFL 2026 score of 4.5), IELTS 6.5, Duolingo 120 or the Pearsons PTE 60.",
            EAS_PAGE,
        ),
        "ielts_min": (
            "6.5",
            "EAS Ph.D. requires IELTS 6.5 minimum (higher than the university general minimum of 6.0).",
            "International students should have a minimum English Proficiency score of TOEFL iBT 90 (New TOEFL 2026 score of 4.5), IELTS 6.5, Duolingo 120 or the Pearsons PTE 60.",
            EAS_PAGE,
        ),
        "gre_subject": gre_subject_tuple,
        "supervisor": (
            "Not required",
            "Applications indicating option preferences are made directly to the EAS Ph.D. program and reviewed by admissions committees in the selected options rather than requiring a pre-committed supervisor.",
            "Applications indicating option preferences will be made directly to the PhD program and reviewed by admissions committees in the selected options. Admission is made by the Associate Provost for Graduate Studies and the Dean of the College of Engineering upon the recommendation of the EAS Graduate Program Director and the admissions director of the major option.",
            EAS_PAGE,
        ),
        "funding": (
            "Competitive",
            "A limited number of graduate assistantships are available on a competitive basis.",
            "A limited number of assistantships are available on a competitive basis. This award is subject to the work needs of the position and department, your satisfactory performance of duties, your academic record, and availability of funds, and may be subject to change.",
            EAS_PAGE,
        ),
        "entry_route": (
            "Either",
            "Encourages applicants with either a bachelor's degree (min. 3.00 GPA) or a master's degree (min. 3.25 GPA); 66 semester credit hours minimum beyond the bachelor's degree.",
            "Students possessing a bachelor's or master's degree and a strong academic background in any of the four program tracks (Applied Mechanics and Materials, Computational Science and Engineering, Computer Science and Information Science, Industrial and Systems Engineering) or similar disciplines are encouraged to apply for admission to the EAS PhD program. | Generally, a minimum undergraduate GPA of 3.00 (on a scale of 4.00) is required or a minimum graduate GPA of 3.25. | EAS options require a minimum of 66 semester credit hours beyond the bachelor’s degree.",
            EAS_PAGE,
        ),
    }

NO_SUBJ_TUPLE = (
    "No subject test",
    "No GRE Subject Test exists for this field (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
    ETS_SUBJ_QUOTE,
    ETS_SUBJ_URL,
)

# 6. CS
rec.save_program(
    UID,
    "cs",
    "Department of Computer and Information Science (EAS Ph.D.)",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12775",
    eas_common_fields(NO_SUBJ_TUPLE),
    notes="Computer Science and Information Science option of the College of Engineering EAS Ph.D. program (66 credits; QE waived with core GPA >= 3.5). Shared EAS admissions rules (GRE waived; TOEFL 90 / 4.5 new scale, IELTS 6.5) appear on https://www.umassd.edu/programs/engineering-applied-science-phd/.",
    checked=CHECKED,
    name="Engineering and Applied Science Ph.D. — Computer Science and Information Science",
)

# 7. Data Science
rec.save_program(
    UID,
    "datasci",
    "College of Engineering — Machine Learning & Data Science (EAS Ph.D.)",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12777",
    eas_common_fields(NO_SUBJ_TUPLE),
    notes="Machine Learning and Data Science (MLDS) option of the College of Engineering EAS Ph.D. program (13 courses / 66 credits spanning MTH, CIS, and DSC coursework). Shared EAS admissions rules (GRE waived; TOEFL 90 / 4.5 new scale, IELTS 6.5) appear on https://www.umassd.edu/programs/engineering-applied-science-phd/.",
    checked=CHECKED,
    name="Engineering and Applied Science Ph.D. — Machine Learning and Data Science",
)

# 8. Math / Computational Science & Engineering
rec.save_program(
    UID,
    "math",
    "Department of Mathematics / College of Engineering (EAS Ph.D.)",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12774",
    eas_common_fields((
        "Not stated",
        "Neither the EAS Ph.D. admissions page nor the Computational Science & Engineering catalog page mentions a Mathematics GRE Subject Test requirement (GRE General itself is waived).",
        "",
        "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12774",
    )),
    notes="Computational Science and Engineering (CSE) option of the EAS Ph.D. co-directed with Mathematics faculty (66 credits; major electives drawn from MTH, PHY, and MAR). Physics has an M.S.-only standalone degree, so computational physics doctoral work runs through this option. Shared EAS admissions rules appear on https://www.umassd.edu/programs/engineering-applied-science-phd/.",
    checked=CHECKED,
    name="Engineering and Applied Science Ph.D. — Computational Science and Engineering",
)

# 9. Mechanical Engineering + Materials Science (+ ISE companion option noted)
rec.save_program(
    UID,
    "mech",
    "Department of Mechanical Engineering (EAS Ph.D.)",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12773",
    eas_common_fields(NO_SUBJ_TUPLE),
    also_fields=["materials"],
    notes="Applied Mechanics and Materials (AMM) option of the EAS Ph.D. (66 credits covering solid/fluid mechanics, dynamics, and atomic/molecular-scale materials science). Also covers the College of Engineering's Industrial and Systems Engineering - EAS Ph.D. option (https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12776), which shares the same 66-credit MNE/EAS core and EAS admissions rules (https://www.umassd.edu/programs/engineering-applied-science-phd/).",
    checked=CHECKED,
    name="Engineering and Applied Science Ph.D. — Applied Mechanics and Materials",
)

# 10. Civil & Environmental Engineering
rec.save_program(
    UID,
    "civil",
    "Department of Civil and Environmental Engineering (EAS Ph.D.)",
    "https://catalog.umassd.edu/preview_program.php?catoid=89&poid=12778",
    eas_common_fields(NO_SUBJ_TUPLE),
    notes="Infrastructure, Environmental, and Fluids Engineering (IEF) option of the EAS Ph.D. (66 credits covering Civil & Environmental Engineering [CEN], coastal infrastructure, geotechnical, and fluid/environmental engineering). Shared EAS admissions rules appear on https://www.umassd.edu/programs/engineering-applied-science-phd/.",
    checked=CHECKED,
    name="Engineering and Applied Science Ph.D. — Infrastructure, Environmental, and Fluids Engineering",
)

print("Staged UMass Dartmouth (umassd) successfully.")
