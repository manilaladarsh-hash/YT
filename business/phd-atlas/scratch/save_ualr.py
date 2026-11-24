import os
import sys
from pathlib import Path

os.environ["ATLAS_OUT"] = "data/staging"
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from rec import save_university, save_program

CHECKED = "2026-11-14"

# URLs
G_INTL = "https://ualr.edu/gradschool/international-prospects/"
G_GUIDE = "https://ualr.edu/gradschool/gradguide/"
G_ASST = "https://ualr.edu/gradschool/assistantship/"
G_INS = "https://ualr.edu/gradschool/current-students/health-insurance/"
G_NEWS = "https://ualr.edu/news/2026/06/18/ua-little-rock-increases-financial-support-for-graduate-assistantships/"
G_CAT = "https://catalog.ualr.edu/content.php?catoid=21&navoid=2484"
P_ADM = "https://ualr.edu/policy/home/student/graduate-school-admission/"
P_INTL = "https://ualr.edu/policy/home/student/graduate-school-international-student/"
ISS_ENG = "https://ualr.edu/international/english-requirements/"

ASCI_STEPS = "https://ualr.edu/appliedscience/steps-to-apply/"
ASCI_FUND = "https://ualr.edu/appliedscience/student-funding-options/"
ASCI_BIO = "https://ualr.edu/appliedscience/programs-facilities/applied-biosciences/"
ASCI_CHEM = "https://ualr.edu/appliedscience/programs-facilities/applied-chemistry/"
ASCI_PHYS = "https://ualr.edu/appliedscience/programs-facilities/applied-physics/"
ASCI_MATH = "https://ualr.edu/appliedscience/programs-facilities/applied-mathematics-and-statistics/"
CAT_BIO = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5494"
CAT_CHEM = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5495"
CAT_PHYS = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5496"
CAT_MATH = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5497"

BINF_PROGS = "https://ualr.edu/bioinformatics/programs/"
BINF_PHD = "https://ualr.edu/bioinformatics/programs/phd/"
BINF_FAQ = "https://ualr.edu/bioinformatics/faq/"
CAT_BINF = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5566"

CIS_CS = "https://ualr.edu/computerinformationsciences/cis-phd-computer-science/"
CIS_FUND = "https://ualr.edu/computerinformationsciences/financial-support-cis-phd/"
CAT_CIS = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5481"

ENG_PHD = "https://ualr.edu/engineering/engineering-phd/"
ENG_DL = "https://ualr.edu/engineering/admission-deadlines/"
CAT_ECE = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5574"
CAT_MECH = "https://catalog.ualr.edu/preview_program.php?catoid=21&poid=5576"

ETS_ABOUT = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_SCORES = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"

ETS_SUBJ_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ETS_DISC_QUOTE = "The GRE Chemistry Test was discontinued in May 2023. The GRE Biology Test and the GRE Literature in English Test were discontinued in May 2021."

save_university(
    "ualr",
    "University of Arkansas at Little Rock",
    "USA",
    "Arkansas",
    G_INTL,
    {
        "app_fee": (
            "40 USD",
            "Non-refundable $40 application fee required before processing (exempt for McNair Scholars, military members, and Indus Foundation applicants per catalog and Policy LR 509.3).",
            "All applicants must pay a non-refundable $40 application fee before their application can be processed.",
            G_INTL,
            {
                "also": [
                    {
                        "quote": "A non-refundable application fee of $40.00 is required of all applicants except for McNair Scholars and military members.",
                        "url": G_CAT,
                    },
                    {
                        "quote": "A non-refundable application fee is required for all applicants, except for McNair Scholars and applicants who apply through the Indus Foundation.",
                        "url": P_ADM,
                    },
                ]
            },
        ),
        "fee_waiver": (
            "Limited",
            "Application fee waivers are available only in rare extenuating circumstances on request, for McNair Scholars, military members, Indus Foundation applicants, or previously admitted students reapplying to defer.",
            "In rare circumstances, an application fee waiver may be requested.",
            G_GUIDE,
            {
                "also": [
                    {
                        "quote": "A non-refundable application fee of $40.00 is required of all applicants except for McNair Scholars and military members. | In these cases, the graduate application fee will be waived for students who need to reapply.",
                        "url": G_CAT,
                    },
                    {
                        "quote": "A non-refundable application fee is required for all applicants, except for McNair Scholars and applicants who apply through the Indus Foundation.",
                        "url": P_ADM,
                    },
                ]
            },
        ),
        "gre_general": (
            "Not stated",
            "Set by individual graduate programs rather than the Graduate School; all 8 STEM Ph.D. programs at UA Little Rock require GRE General scores (with program-specific GPA or institutional waivers; scores must be within 5 years). See each program record.",
            "",
            G_CAT,
        ),
        "toefl_min": (
            "79",
            "Doctoral applicants need at least 79 TOEFL iBT (550 PBT, 213 CBT); scores must be within 2 years. Note: the 'Minimum score of 4 on TOEFL iBT' on the International English Requirements page appears under Undergraduate Students; graduate doctoral admission still uses 79 iBT. Individual programs (e.g., CIS) may expect higher than 79.",
            "Doctoral applicants must achieve a score of 550 on the paper-based test, 213 on the computer-based version, or 79 on the Internet-based version.",
            G_INTL,
            {
                "also": [
                    {
                        "quote": "*TOEFL or IELTS scores must be from tests taken within the past 2 years.",
                        "url": ISS_ENG,
                    }
                ]
            },
        ),
        "ielts_min": (
            "6.5",
            "Minimum IELTS Academic overall score is 6.5 (scores must be from tests taken within the past 2 years).",
            "On the IELTS, all applicants must make at least a 6.5.",
            G_INTL,
            {
                "also": [
                    {
                        "quote": "*TOEFL or IELTS scores must be from tests taken within the past 2 years.",
                        "url": ISS_ENG,
                    }
                ]
            },
        ),
        "english_waiver": (
            "No",
            "An English-medium degree from India does not waive TOEFL/IELTS. Policy LR 509.9 (revised April 2026) and the Graduate Catalog exempt only applicants who studied full-time for 2+ years at an English-instruction institution located in a country where English is the native language (Canada except Quebec, Ireland, UK, Australia, New Zealand, or Commonwealth Caribbean) or hold a U.S. bachelor's degree.",
            "Only students who have studied full-time for two or more years at a college or university where English is the language of instruction located in a country where English is the native language are exempt from the TOEFL, the IELTS, or the PTE.",
            P_INTL,
            {
                "also": [
                    {
                        "quote": "Native English speakers with citizenship of an exempt country: Canada (except Quebec), Ireland, United Kingdom, Australia, New Zealand, or the Commonwealth Caribbean.",
                        "url": G_GUIDE,
                    }
                ]
            },
        ),
    },
    notes=(
        "All 10 Ph.D. programs in the 2026-2027 Graduate Catalog were reviewed; 2 are non-STEM (Criminal Justice Ph.D., Reading Ph.D.) "
        "and 8 STEM Ph.D. tracks are included across 12 fields. International transcripts from non-IAU-recognized institutions or for transfer credit require a NACES articulation (Policy LR 509.9 also states outside articulation for international academic records). "
        "Doctoral GA minimum 9-month stipend was increased from $13,000 to $15,000 starting Fall 2026, plus 9 credit hours tuition waiver and up to $400/semester health insurance reimbursement."
    ),
    checked=CHECKED,
)

# Common Applied Science data (Deadline, Supervisor, Funding, GRE General, Entry Route)
ASCI_DEADLINE = (
    "2027-06-01",
    "No separate Applied Science deadline is published; under Policy LR 509.9 (revised April 2026) and Graduate School International Prospects, all international application materials for Fall must be received by June 1 (June 1, 2027 inferred for Fall 2027; Spring Oct 1; Summer March 1). Note: the 2026-2027 catalog also prints legacy general international dates of July 1 and Feb 1.",
    "Application materials must be received no later than June 1 for fall semester, October 1 for spring semester, and March 1 for summer semester.",
    P_INTL,
    {
        "inferred": "year",
        "also": [
            {"quote": "Fall applications: June 1 | Spring applications: October 1 | Summer applications: March 1", "url": G_INTL},
            {"quote": "They must be received no later than July 1 for the fall semester and November 1 for the spring semester, and March 1 for the summer semester.", "url": G_CAT},
        ],
    },
)

ASCI_GRE_GEN = (
    "Required",
    "GRE General is required (min 155Q, 138V, 4.5 AW in the 2026-2027 catalog; the program Steps to Apply page states 300 combined and 4.5 AW), except applicants with a 3.5+ GPA on their last 60 credit hours may be exempted with graduate coordinator approval.",
    "Official GRE General Test from ETS (UA Little Rock’s institutional code is 6368) | Applicants with a 3.5 or greater GPA on their last 60 credit hours are not required to take the GRE.",
    ASCI_STEPS,
    {
        "also": [
            {
                "quote": "On the GRE, applicants must have a minimum quantitative score of 155, a verbal score of at least 138, and a writing assessment score of at least 4.5 | With the approval of the graduate coordinator, applicants with a 3.5 GPA or greater on their last 60 graduate and undergraduate credit hours, may not be required to take the GRE.",
                "url": CAT_BIO,
            }
        ]
    },
)

ASCI_SUPERVISOR = (
    "Not required",
    "Admission is made with the collective input of Applied Science Doctoral faculty (faculty mentor availability is considered), and entering students complete a mandatory first-semester Laboratory Rotation (ASCI 7450X) to select a dissertation advisor.",
    "Recommendations on a doctoral application for admission to the Applied Science program are made with the collective input of the Applied Science Doctoral faculty. | All Applied Science doctoral students must register for Introduction to Research in Applied Science (ASCI 7450X), also called “Laboratory Rotation,” in their first semester in the program",
    CAT_BIO,
)

ASCI_FUNDING = (
    "Competitive",
    "Funding is limited and not guaranteed with admission; admission and funding decisions are separate. Full-time doctoral GAs/TAs/RAs receive a minimum $15,000 9-month stipend (effective Fall 2026), 9 credits of tuition waiver per semester, and $400/semester health insurance reimbursement, renewable each semester with >=3.0 GPA.",
    "Admission decisions and funding decisions are considered separately, and the number of students admitted is usually much higher than the number of students who are funded. There are a limited number of funding opportunities and funding is not guaranteed to all students.",
    ASCI_FUND,
    {
        "also": [
            {
                "quote": "The full-time stipend for the academic year is a minimum of $15,000 for doctoral students and $10,000 for master’s students. | Full-time Graduate Assistants must be enrolled in at least 9 hours of credit courses that are covered by the tuition waiver.",
                "url": G_ASST,
            },
            {
                "quote": "The Doctoral Health Insurance Reimbursement provides $400 of insurance reimbursement for Fall and another $400 for Spring.",
                "url": G_INS,
            },
            {
                "quote": "Doctoral-level graduate assistants will see their minimum stipend increase from $13,000 to $15,000.",
                "url": G_NEWS,
            },
        ]
    },
)

ASCI_ENTRY = (
    "Direct from bachelor's",
    "Requires a baccalaureate degree in an appropriate scientific discipline with at least 3.0 overall GPA (catalog) or 3.3 on the last 60 credit hours (Steps to Apply page); 72 credit hours beyond the bachelor's degree.",
    "Applicants must possess a baccalaureate degree in an appropriate scientific discipline such as chemistry, physics, materials science, biology, mathematics, statistics, or earth science. | All emphases require a minimum of 72 credit hours beyond the baccalaureate degree.",
    CAT_BIO,
)

# 1. Applied Biosciences -> biology
save_program(
    "ualr",
    "biology",
    "Department of Applied Science (Applied Biosciences Emphasis)",
    ASCI_BIO,
    {
        "deadline": ASCI_DEADLINE,
        "gre_general": ASCI_GRE_GEN,
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Biology; ETS discontinued the GRE Biology Test in May 2021.",
            ETS_DISC_QUOTE,
            ETS_SCORES,
        ),
        "supervisor": ASCI_SUPERVISOR,
        "funding": ASCI_FUNDING,
        "entry_route": ASCI_ENTRY,
    },
    notes=(
        "Applied Science, Applied Biosciences Emphasis, Ph.D. (catalog poid=5494). Requires 3 LORs, statement of purpose, and prerequisites. "
        "Non-native English speakers qualifying for a TA must score 5.0 on TSE; international students must carry health insurance and submit TB/MMR documentation. "
        "Note discrepancy on GRE minimum between catalog (155Q/138V/4.5AW) and Steps to Apply page (300 combined, 4.5AW) and Fall international deadline (June 1 Policy LR 509.9 vs legacy July 1/Feb 1 in catalog)."
    ),
    checked=CHECKED,
    name="Applied Science, Applied Biosciences Emphasis, Ph.D.",
)

# 2. Applied Chemistry -> chemistry
save_program(
    "ualr",
    "chemistry",
    "Department of Applied Science (Applied Chemistry Emphasis)",
    ASCI_CHEM,
    {
        "deadline": ASCI_DEADLINE,
        "gre_general": ASCI_GRE_GEN,
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Chemistry; ETS discontinued the GRE Chemistry Test in May 2023.",
            ETS_DISC_QUOTE,
            ETS_SCORES,
        ),
        "supervisor": (
            "Not required",
            ASCI_SUPERVISOR[1],
            "Recommendations on a doctoral application for admission to the Applied Science program are made with the collective input of the Applied Science Doctoral faculty. | All Applied Science doctoral students must register for Introduction to Research in Applied Science (ASCI 7450X), also called “Laboratory Rotation,” in their first semester in the program",
            CAT_CHEM,
        ),
        "funding": (
            "Competitive",
            ASCI_FUNDING[1] + " Program page notes teaching as TAs (often in freshman labs) is required in Applied Chemistry.",
            ASCI_FUNDING[2],
            ASCI_FUND,
            {
                "also": ASCI_FUNDING[4]["also"] + [
                    {
                        "quote": "Teaching is also required in the program, and graduate students serve as TAs (teaching assistants), most often in freshman level laboratories.",
                        "url": ASCI_CHEM,
                    }
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            ASCI_ENTRY[1],
            ASCI_ENTRY[2],
            CAT_CHEM,
        ),
    },
    notes=(
        "Applied Science, Applied Chemistry Emphasis, Ph.D. (catalog poid=5495). Teaching as TAs is required. "
        "Non-native English speakers qualifying for a TA must score 5.0 on TSE. Catalog vs Steps to Apply GRE minimum and June 1 vs legacy July 1/Feb 1 deadline nuances match Applied Biosciences."
    ),
    checked=CHECKED,
    name="Applied Science, Applied Chemistry Emphasis, Ph.D.",
)

# 3. Applied Mathematics and Statistics -> math (also statistics)
save_program(
    "ualr",
    "math",
    "Department of Applied Science (Applied Mathematics and Statistics Emphasis)",
    ASCI_MATH,
    {
        "deadline": ASCI_DEADLINE,
        "gre_general": ASCI_GRE_GEN,
        "gre_subject": (
            "Not stated",
            "Neither the catalog nor the program page states whether the ETS GRE Mathematics Subject Test is required, optional, or not considered (only GRE General requirements are stated).",
            "",
            CAT_MATH,
        ),
        "supervisor": (
            "Not required",
            ASCI_SUPERVISOR[1],
            "Recommendations on a doctoral application for admission to the Applied Science program are made with the collective input of the Applied Science Doctoral faculty. | All Applied Science doctoral students must register for Introduction to Research in Applied Science (ASCI 7450X), also called “Laboratory Rotation,” in their first semester in the program",
            CAT_MATH,
        ),
        "funding": ASCI_FUNDING,
        "entry_route": (
            "Direct from bachelor's",
            ASCI_ENTRY[1] + " Requires prerequisite preparation in discrete math, single/multivariable calculus, linear algebra, differential equations, mathematical statistics, and programming through data structures.",
            ASCI_ENTRY[2],
            CAT_MATH,
        ),
    },
    also_fields=["statistics"],
    notes=(
        "Applied Science, Applied Mathematics and Statistics, Ph.D. (catalog poid=5497). Covers both Applied Mathematics and Applied Statistics candidacy/research areas (mapped to math + also_fields: statistics). "
        "Non-native English speakers qualifying for a TA must score 5.0 on TSE."
    ),
    checked=CHECKED,
    name="Applied Science, Applied Mathematics and Statistics, Ph.D.",
)

# 4. Applied Physics -> physics (also materials, earth, astronomy)
save_program(
    "ualr",
    "physics",
    "Department of Applied Science (Applied Physics Emphasis)",
    ASCI_PHYS,
    {
        "deadline": ASCI_DEADLINE,
        "gre_general": ASCI_GRE_GEN,
        "gre_subject": (
            "Not stated",
            "Neither the catalog nor the program page states whether the ETS GRE Physics Subject Test is required, optional, or not considered (only GRE General requirements are stated).",
            "",
            CAT_PHYS,
        ),
        "supervisor": (
            "Not required",
            ASCI_SUPERVISOR[1],
            "Recommendations on a doctoral application for admission to the Applied Science program are made with the collective input of the Applied Science Doctoral faculty. | All Applied Science doctoral students must register for Introduction to Research in Applied Science (ASCI 7450X), also called “Laboratory Rotation,” in their first semester in the program",
            CAT_PHYS,
        ),
        "funding": ASCI_FUNDING,
        "entry_route": (
            "Direct from bachelor's",
            ASCI_ENTRY[1],
            ASCI_ENTRY[2],
            CAT_PHYS,
        ),
    },
    also_fields=["materials", "earth", "astronomy"],
    notes=(
        "Applied Science, Applied Physics Emphasis, Ph.D. (catalog poid=5496). Explicitly encompasses research and doctoral training in Applied Physics, Materials Science & Nanotechnology, "
        "Applied Geophysics & Seismology (Earth Sciences), and Astronomy & Astrophysics (mapped to physics with also_fields: materials, earth, astronomy). "
        "Non-native English speakers qualifying for a TA must score 5.0 on TSE."
    ),
    checked=CHECKED,
    name="Applied Science, Applied Physics Emphasis, Ph.D.",
)

# 5. Bioinformatics -> biomed (also biology)
save_program(
    "ualr",
    "biomed",
    "UA Little Rock / UAMS Joint Graduate Program in Bioinformatics",
    BINF_PHD,
    {
        "deadline": (
            "2027-04-01",
            "Fall application deadline is April 1 with notification by May 1 (April 1, 2027 inferred for Fall 2027; Spring is October 15 with notification Nov 15). Applications may be considered at any time, but most are reviewed in these two cohorts.",
            "Fall April 1 May 1 | Spring Oct. 15 Nov. 15 | While admissions applications may be considered at any time, the majority of the applications will be considered as a group twice per year:",
            BINF_PROGS,
            {"inferred": "year"},
        ),
        "gre_general": (
            "Required",
            "GRE General Test is required unless a GRE Waiver Form is submitted; the admissions committee has no fixed minimum score, though most successful applicants score at or above the 60th percentile on Quantitative.",
            "GRE scores (general test only) or GRE Waiver Form",
            BINF_PROGS,
            {
                "also": [
                    {
                        "quote": "The Bioinformatics Graduate Program’s Student Admissions Committee had not established minimum GRE scores for admission to the program. | The GRE Quantitative Score is especially important; most successful applicants score in the 60th percentile or higher.",
                        "url": BINF_FAQ,
                    }
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "Only the GRE General Test is required; no ETS GRE Subject Test exists for Bioinformatics / Biomedical Sciences.",
            "Only the general GRE transcript is needed.",
            BINF_FAQ,
            {"also": [{"quote": ETS_SUBJ_QUOTE, "url": ETS_ABOUT}]},
        ),
        "supervisor": (
            "Not required",
            "Admission is decided by the Bioinformatics Student Admissions Committee (no pre-application CV/faculty match needed); students identify a research mentor during first-year lab rotations and form an advisory committee within 6 months.",
            "We make admission decisions based on all the materials requested as part of the application packet, so it is not necessary to send a CV prior to applying... only then will they forward it on the Admissions Committee.",
            BINF_FAQ,
            {
                "also": [
                    {
                        "quote": "Within the first six months of entering the Ph.D. program, students must have an approved advisory committee and defend their dissertation proposals.",
                        "url": CAT_BINF,
                    },
                    {
                        "quote": "By identifying a research topic and mentor during the first year’s research lab rotation",
                        "url": BINF_PHD,
                    },
                ]
            },
        ),
        "funding": (
            "Competitive",
            "Assistantships are highly competitive and not guaranteed; the program notes it admits many more students than it can fund. Ph.D. students receive priority, and funded GAs have UA Little Rock/UAMS tuition paid plus a stipend (university minimum $15,000/9-mo for full-time doctoral GAs from Fall 2026).",
            "Graduate assistantships that support research opportunities are available to qualified full-time students on a highly competitive basis. Tuition is paid, and a stipend is provided for living expenses.",
            CAT_BINF,
            {
                "also": [
                    {
                        "quote": "Ph.D. Students typically receive priority for any available assistantships. | Keep in mind that we admit many more students than we are able to supply financial assistance to.",
                        "url": BINF_FAQ,
                    },
                    {
                        "quote": "The full-time stipend for the academic year is a minimum of $15,000 for doctoral students and $10,000 for master’s students.",
                        "url": G_ASST,
                    },
                ]
            },
        ),
        "entry_route": (
            "Master's usually required",
            "Ph.D. admission requires completion of an M.S. degree in bioinformatics or a closely related field (with strong master's project/thesis performance); applicants entering with only a bachelor's apply to the M.S. track first.",
            "The Ph.D. program admission requires completion of the M.S. degree in bioinformatics or a closely related field. Students pursuing the Ph.D. need to demonstrate good research potential in their culminating master’s project or thesis.",
            CAT_BINF,
            {
                "also": [
                    {
                        "quote": "Only by completing the master’s degree, and excelling on the master’s capstone project and its defense, will students be admitted to the Ph.D. program.",
                        "url": BINF_PHD,
                    }
                ]
            },
        ),
    },
    also_fields=["biology"],
    notes=(
        "Joint Ph.D. offered by UA Little Rock and University of Arkansas for Medical Sciences (UAMS). "
        "UA Little Rock is the primary administrative home for admission; UAMS non-degree admission is completed after enrollment for taking UAMS courses or working with UAMS mentors. "
        "Note Bioinformatics FAQ refers to legacy 213 CBT TOEFL (equivalent to 79 iBT per Graduate School policy)."
    ),
    checked=CHECKED,
    name="Bioinformatics, Ph.D.",
)

# 6. Computer and Information Sciences, All Tracks -> cs
save_program(
    "ualr",
    "cs",
    "School of Computer and Information Sciences",
    CIS_CS,
    {
        "deadline": (
            "2027-06-01",
            "No separate CIS Ph.D. deadline is published; under Policy LR 509.9 (revised April 2026) and Graduate School International Prospects, all international application materials for Fall must be received by June 1 (June 1, 2027 inferred for Fall 2027; Spring Oct 1; Summer March 1). Note: the 2026-2027 catalog also prints legacy general international dates of July 1 and Feb 1.",
            ASCI_DEADLINE[2],
            ASCI_DEADLINE[3],
            ASCI_DEADLINE[4],
        ),
        "gre_general": (
            "Required",
            "GRE General Test (within 5 years) is required: desired combined V+Q >= 301, minimums 142V and 144Q, plus an additional minimum of 156 Quantitative for the Computer Science and Information Science tracks (Analytical Writing ~3.0+ or writing samples).",
            "GRE test scores are taken within five years of application. The desired combined quantitative and verbal score on the GRE is 301 or above (on a 336 scale), with minimum scores of 142 and 144 on the verbal and quantitative sections, respectively. Computer Science and Information Science tracks have an additional minimum score requirement of 156 for the quantitative section.",
            CIS_CS,
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Computer Science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_ABOUT,
        ),
        "supervisor": (
            "Not required",
            "The CIS Steering Committee evaluates admission and program fit; new students are initially advised by their track coordinator and formally declare a research adviser by the end of their 1st or 2nd semester.",
            "The CIS Steering Committee will evaluate the compatibility between the applicant’s background, research interests, and communication skills vis-a-vis the doctoral program when making admission decisions | New students will be advised initially by the program coordinator of the student’s chosen track area. | Students should formally declare a research adviser preferably at the end of the first semester but not later than the second semester.",
            CAT_CIS,
        ),
        "funding": (
            "Competitive",
            "Financial support is not guaranteed with admission. Competitive TA/RA/GA packages cover 9 credit hours of tuition per semester and a stipend (CIS lists $1,500/month; Graduate School raised the 9-month doctoral GA minimum to $15,000 in Fall 2026); faculty-nominated Fall international students may also receive an International Student Scholarship reducing tuition to in-state rates.",
            "Please be advised, financial support is not guaranteed with admission. However, some financial support is available for eligible students in the Ph.D. program. | Full-time assistantship pays for 9 hours of tuition per semester and a monthly stipend of $1,500.",
            CIS_FUND,
            {
                "also": [
                    {
                        "quote": "International Student Scholarships reduce tuition to in-state rates for international students as long as they remain in good standing in the program.",
                        "url": CIS_FUND,
                    },
                    {
                        "quote": "The full-time stipend for the academic year is a minimum of $15,000 for doctoral students and $10,000 for master’s students.",
                        "url": G_ASST,
                    },
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Requires a bachelor's degree or higher (75 credit hours beyond the baccalaureate) with >= 3.0 GPA on the last 60 credit hours; strongest preparation is an undergraduate or master's degree in CS, CE, engineering, or math.",
            "A bachelor’s degree or higher from an institutionally or regionally accredited institution. | The program requires a minimum of 75 hours beyond the baccalaureate degree.",
            CAT_CIS,
        ),
    },
    notes=(
        "Computer and Information Sciences, Ph.D. (catalog poid=5481) has 3 tracks: Computer Science (in-person), Information Science (in-person/online), and Information Quality (in-person/online). "
        "Note English/TA nuance in catalog poid=5481: TOEFL 'should exceed 550 (paper-based test), 213 (computer-based test), or 79 (internet-based test)' (provisional admission possible if close); TA requires AEOCPT >= 80% or TSE >= 5.0. "
        "Admission may be deferred/denied if a track is at full faculty/funding capacity. Policy LR 509.9 sets June 1 Fall international deadline (vs legacy July 1/Feb 1 in catalog)."
    ),
    checked=CHECKED,
    name="Computer and Information Sciences, Ph.D.",
)

# 7. Engineering, ECE Track -> ece
ENG_DEADLINE = (
    "2027-03-31",
    "Graduate engineering applications are rolling, but applicants should submit all required materials by the Fall priority deadline of March 31 (March 31, 2027 inferred for Fall 2027; Spring is September 30; Summer not offered).",
    "Graduate program applications are accepted on a rolling basis. However, for full consideration, applicants are strongly encouraged to submit all required materials by the priority deadlines below: – Fall Admission: March 31 – Spring Admission: September 30 Please note that summer admission is not offered.",
    ENG_DL,
    {
        "inferred": "year",
        "also": [
            {
                "quote": "Application Deadlines: March 31st for fall admission. September 30th for spring admissions. Summer admissions are not offered.",
                "url": CAT_ECE,
            }
        ],
    },
)

ENG_SUPERVISOR = (
    "Recommended",
    "Applicants are encouraged to contact engineering faculty for research supervision; advisor availability and willingness are considered in admission decisions (students formally declare an advisor by the end of the 2nd semester).",
    "Applicants are encouraged to contact engineering faculty for their research supervision. The availability and willingness of advisors will be considered in making admission decisions.",
    CAT_ECE,
)

ENG_FUNDING = (
    "Competitive",
    "A limited number of competitive TAs/RAs are available to qualified full-time students with regular admission, covering 9 credits of tuition per semester plus a living stipend (university minimum $15,000/9-mo from Fall 2026) and $400/semester health insurance reimbursement.",
    "A limited number of graduate assistantships that support teaching and research opportunities are available to qualified full-time students with regular admissions. Tuition is paid for nine credits per semester, and a stipend is provided for living expenses.",
    CAT_ECE,
    {
        "also": [
            {
                "quote": "The full-time stipend for the academic year is a minimum of $15,000 for doctoral students and $10,000 for master’s students.",
                "url": G_ASST,
            },
            {
                "quote": "The Doctoral Health Insurance Reimbursement provides $400 of insurance reimbursement for Fall and another $400 for Spring.",
                "url": G_INS,
            },
        ]
    },
)

ENG_ENTRY = (
    "Either",
    "Requires at least one degree (bachelor's or master's) in engineering: >=3.5 undergraduate GPA for bachelor's entry (72 credit hours) or >=3.3–3.5 master's GPA for master's entry (48 credit hours; department page states 3.3 while 2026-2027 catalog states 3.5).",
    "Applicants must have at least one degree (bachelor’s or master’s) in engineering. Applicants with only a bachelor’s degree in engineering must have an overall undergraduate GPA of 3.5 or better. Applicants with a master’s degree in engineering should have a master’s GPA of 3.5 or better. | 72 hours for students entering the PhD program with a Bachelor’s degree and 48 hours for students entering the Ph.D. program with a Master’s degree.",
    CAT_ECE,
    {
        "also": [
            {
                "quote": "Alternatively, applicants with a master’s degree in engineering should have a master’s GPA of 3.3 or better.",
                "url": ENG_PHD,
            }
        ]
    },
)

save_program(
    "ualr",
    "ece",
    "School of Engineering and Engineering Technology",
    ENG_PHD,
    {
        "deadline": ENG_DEADLINE,
        "gre_general": (
            "Required",
            "GRE General Test is required (315 V+Q combined and 3.5 AW expected); may be waived for UA Little Rock M.S. ECE (thesis option) graduates with >=3.5 GPA, in exceptional cases, or when GRE is not offered in the applicant's country.",
            "Applicants are required to submit GRE scores with the admission application. A combined total of 315 on the verbal and quantitative reasoning sections and a score of 3.5 on the analytical writing section will be expected. The GRE may be waived for applicants who graduate from UA Little Rock with a master’s degree in electrical and computer engineering (thesis option) and a 3.5 GPA or higher.",
            CAT_ECE,
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Electrical and Computer Engineering (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_ABOUT,
        ),
        "supervisor": ENG_SUPERVISOR,
        "funding": ENG_FUNDING,
        "entry_route": ENG_ENTRY,
    },
    notes=(
        "Engineering, Electrical and Computer Engineering Track, Ph.D. (catalog poid=5574). "
        "Note minor conflict on master's GPA requirement: department webpage (engineering-phd/) states 3.3 while catalog (poid=5574) states 3.5. "
        "Note priority vs rolling deadline: engineering/admission-deadlines/ lists March 31 as priority deadline with rolling applications thereafter, whereas catalog lists March 31."
    ),
    checked=CHECKED,
    name="Engineering, Electrical and Computer Engineering Track, Ph.D.",
)

# 8. Engineering, Mechanical Engineering Track -> mech
save_program(
    "ualr",
    "mech",
    "School of Engineering and Engineering Technology",
    ENG_PHD,
    {
        "deadline": (
            "2027-03-31",
            ENG_DEADLINE[1],
            ENG_DEADLINE[2],
            ENG_DL,
            {
                "inferred": "year",
                "also": [
                    {
                        "quote": "Application Deadlines: March 31st for fall admission. September 30th for spring admissions. Summer admissions are not offered.",
                        "url": CAT_MECH,
                    }
                ],
            },
        ),
        "gre_general": (
            "Required",
            "GRE General Test is required (315 V+Q combined and 3.5 AW expected); catalog text lists waivers for UA Little Rock M.S. ECE thesis graduates (>=3.5 GPA), exceptional cases, or where GRE is unavailable in the applicant's country.",
            "Applicants are required to submit GRE scores with the admission application. A combined total of 315 on the verbal and quantitative reasoning sections and a score of 3.5 on the analytical writing section will be expected. The GRE may be waived for applicants who graduate from UA Little Rock with a master’s degree in electrical and computer engineering (thesis option) and a 3.5 GPA or higher.",
            CAT_MECH,
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Mechanical Engineering (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_SUBJ_QUOTE,
            ETS_ABOUT,
        ),
        "supervisor": (
            "Recommended",
            ENG_SUPERVISOR[1],
            ENG_SUPERVISOR[2],
            CAT_MECH,
        ),
        "funding": (
            "Competitive",
            ENG_FUNDING[1],
            ENG_FUNDING[2],
            CAT_MECH,
            {"also": ENG_FUNDING[4]["also"]},
        ),
        "entry_route": (
            "Either",
            ENG_ENTRY[1],
            ENG_ENTRY[2],
            CAT_MECH,
            {"also": ENG_ENTRY[4]["also"]},
        ),
    },
    notes=(
        "Engineering, Mechanical Engineering Track, Ph.D. (catalog poid=5576). "
        "Note minor conflict on master's GPA requirement: department webpage states 3.3 while catalog (poid=5576) states 3.5 (and catalog GRE waiver text on poid=5576 appears copied from the ECE track). "
        "Note priority vs rolling deadline: engineering/admission-deadlines/ lists March 31 as priority deadline with rolling thereafter, whereas catalog lists March 31."
    ),
    checked=CHECKED,
    name="Engineering, Mechanical Engineering Track, Ph.D.",
)

print("Saved ualr university and 8 program records to data/staging/")
