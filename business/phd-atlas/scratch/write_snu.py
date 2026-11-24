import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING = ROOT / "data" / "staging"
UNI_DIR = STAGING / "universities"
PROG_DIR = STAGING / "programs"
UNI_DIR.mkdir(parents=True, exist_ok=True)
PROG_DIR.mkdir(parents=True, exist_ok=True)

PDF_URL = "https://en.snu.ac.kr/webdata/uploads/eng/file/2026/06/2027Spring_graduate_eng.pdf"
APP_URL = "https://en.snu.ac.kr/admission/graduate/application"
FAQ_URL = "https://en.snu.ac.kr/admission/overview/faq/admission"
SCHOL_URL = "https://en.snu.ac.kr/admission/graduate/scholarships/before_application"
ETS_ABOUT = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_SCORES = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"

CHECKED = "2026-11-15"

snu_uni = {
    "id": "snu",
    "institution": "Seoul National University",
    "country": "South Korea",
    "region": "Seoul",
    "grad_page": APP_URL,
    "checked": CHECKED,
    "fields": {
        "app_fee": {
            "code": "90000 KRW",
            "value": "Graduate international application fee is KRW 90,000 paid online (wire transfer of USD 85 is permitted only for documented disaster/communication-disruption postal submissions).",
            "quote": "Upon payment of the application fee (KRW 90,000), an application number will be | assigned and the online application will be considered complete.",
            "url": PDF_URL,
            "also": [
                {
                    "quote": "The application fee is KRW 70,000 for Undergraduate, KRW 90,000 for Graduate program.",
                    "url": FAQ_URL,
                }
            ],
        },
        "fee_waiver": {
            "code": "None",
            "value": "Application fee is non-refundable and cannot be waived under Article 42-3 (Admission Fees) of the Enforcement Decree of the Higher Education Act.",
            "quote": "The application fee is non-refundable and cannot be waived (Article 42-3 (Admission Fees) of the Enforcement Decree of the Higher Education Act).",
            "url": PDF_URL,
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Central SNU Graduate Admissions Guide does not state a GRE General requirement or exemption policy; Form 1 includes an optional 'Other (GRE, Etc.)' blank and the central FAQ treats standardized test score reports as optional supplementary material (SNU ETS institution code 7972).",
            "quote": "",
            "url": PDF_URL,
        },
        "toefl_min": {
            "code": "4.0 (new scale)",
            "value": "Minimum English criterion is TOEFL iBT 4.0 for tests taken on or after January 21, 2026 (or 80 on the prior 0-120 scale; MyBest Scores and Home Edition accepted, ITP not accepted) or TEPS 269. Centrally, Korean TOPIK Level 3 (or Korean university language center Level 4) also satisfies the language requirement unless a department requires English.",
            "quote": "[English] TOEFL iBT 80 (a score of 4.0 for tests taken on or after January 21, 2026) | OR IELTS Academic Band Score 6.0 OR TEPS 269 | ※ TOEFL: MyBestScores(see page 20) and iBT Home Edition scores are accepted; | TOEFL ITP scores are NOT accepted.",
            "url": PDF_URL,
        },
        "ielts_min": {
            "code": "6.0",
            "value": "Minimum IELTS Academic Band Score is 6.0 (One Skill Retake and IELTS Online accepted; IELTS Indicator not accepted), or Korean TOPIK Level 3 centrally unless a department requires English.",
            "quote": "[English] TOEFL iBT 80 (a score of 4.0 for tests taken on or after January 21, 2026) | OR IELTS Academic Band Score 6.0 OR TEPS 269 | ※ IELTS: One Skill Retake(see page 20) and IELTS Online scores are accepted; | IELTS Indicator scores are NOT accepted.",
            "url": PDF_URL,
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exempt from submitting TOEFL/IELTS scores if the applicant submits official documents or school profiles verifying that their entire bachelor's or master's curriculum was conducted in English (or Korean), or if presenting TOPIK Level 3 centrally (overridden by departments such as Chemistry that require English scores).",
            "quote": "Documents proving proficiency in Korean or English, including one or more of the following: | 2) Official documents or school profiles verifying that all courses were conducted | in Korean or English (Applicable only if the entire bachelor’s or master’s curriculum was completed in Korean or English)",
            "url": PDF_URL,
        },
    },
    "notes": (
        "QS WUR 2027 #38. Covers all 18 STEM PhD fields through central and professional graduate schools in Seoul "
        "(Gwanak, Yeongeon medical, Pyeongchang, and Siheung campuses). Fall 2027 international admissions guide is not yet published "
        "(Spring 2027 international online application ran July 6-9, 2026, prior to the Fall 2027 window; deadlines set to Not stated). "
        "Applicants may apply to only one program per admissions cycle. International scholarships include SNU President Fellowship (SPF: full tuition up to 6 semesters + KRW 1.5M-2.0M/mo for developing-country university faculty without a PhD), "
        "Graduate Scholarship for Excellent Foreign Students (GSFS: full tuition up to 4 semesters + >= KRW 500,000/mo), Global Korea Scholarship (GKS: full tuition + KRW 1.4M/mo), and SNU Global EDGE Fellowship (KRW 1.8M/mo + full tuition for BK21 Four PhD students)."
    ),
}

(UNI_DIR / "snu.json").write_text(json.dumps(snu_uni, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

NO_SUBJ_STD = {
    "code": "No subject test",
    "value": "No ETS GRE Subject Test exists for this field (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
    "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
    "url": ETS_ABOUT,
}

NO_SUBJ_CHEM = {
    "code": "No subject test",
    "value": "No GRE Subject Test exists for Chemistry (ETS discontinued the GRE Chemistry Test in May 2023).",
    "quote": "The GRE Chemistry Test was discontinued in May 2023.",
    "url": ETS_SCORES,
}

COMPETITIVE_CENTRAL = {
    "code": "Competitive",
    "value": "Competitive funding via university-wide international fellowships (GSFS: full tuition up to 4 semesters + >= KRW 500,000/mo; SPF for developing-country university faculty: full tuition up to 6 semesters + KRW 1.5M-2.0M/mo; GKS: full tuition + KRW 1.4M/mo) as well as BK21 Four Global EDGE Fellowship (KRW 1.8M/mo + full tuition) and faculty-grant RA/TA support.",
    "quote": "SNU President Fellowship Program (SPF) | Tuition fee: full tuition exemption for a maximum of 6 semesters | Living expenses: 1, 500,000 KRW ~ 2,000,000 KRW per month for 3~4 years | Graduate Scholarship for Excellent Foreign Students (GSFS) | Tuition fee: full tuition exemption for a maximum of 4 semesters | Living expenses: minimum of 500,000 KRW per month (different according to recipients’ majors)",
    "url": SCHOL_URL,
}

ENTRY_ELIG_EITHER_PREFIX = (
    "1) Master’s / Combined Master’s & Doctoral Programs: a bachelor’s degree or higher | "
    "Combined Master’s and Doctoral Course is available to applicants who wish to obtain a Ph.D. degree without a master’s degree. Applicants must have a bachelor’s degree or higher and should apply for the Combined Master’s and Doctoral Course."
)

ENTRY_ELIG_MASTERS_PREFIX = (
    "1) Master’s / Combined Master’s & Doctoral Programs: a bachelor’s degree or higher | "
    "2) Doctoral Programs: a master’s degree or higher"
)

programs = [
    {
        "id": "snu--math",
        "field": "math",
        "also_fields": [],
        "name": "Mathematical Sciences, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Natural Sciences — Department of Mathematical Sciences",
        "program_page": "https://www.math.snu.ac.kr/eng",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | College of Mathematical Sciences ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": "Not stated",
        "notes": "Research groups cover Algebra, Analysis, Topology, Geometry, and Applied Mathematics alongside the Research Institute of Mathematics. Note College of Education also offers a separate Mathematics Education (M/D) program.",
    },
    {
        "id": "snu--statistics",
        "field": "statistics",
        "also_fields": [],
        "name": "Statistics, Ph.D.",
        "department": "College of Natural Sciences — Department of Statistics",
        "program_page": "https://stat.snu.ac.kr/en/admission/graduate/",
        "entry_route": {
            "code": "Master's usually required",
            "value": "Offers Master's and Doctoral programs only (no Combined Master's & Doctoral track in the central programs table); Doctoral entry requires a master's degree or equivalent.",
            "quote": f"{ENTRY_ELIG_MASTERS_PREFIX} | Statistics ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Department graduate courses span Probability Theory, Theory of Statistics, Statistical Consulting, and Big Data / High-Dimensional Statistics; see Graduate School of Data Science (snu--datasci) for direct combined Ph.D. entry in data science.",
    },
    {
        "id": "snu--physics",
        "field": "physics",
        "also_fields": [],
        "name": "Physics, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Natural Sciences — Department of Physics and Astronomy (Physics Major)",
        "program_page": "https://physics.snu.ac.kr/en/academics/graduate/curriculum",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Physics and Astronomy Physics Major ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": "Not stated",
        "notes": "Note: TOEFL iBT 86 / New TEPS 327 listed on the Physics graduate curriculum page is the post-entry Qualifying Examination for Dissertation Submission requirement, not an admission minimum; centralized international admission criterion (TOEFL iBT 4.0 / 80) applies at admission.",
    },
    {
        "id": "snu--astronomy",
        "field": "astronomy",
        "also_fields": [],
        "name": "Astronomy, Ph.D.",
        "department": "College of Natural Sciences — Department of Physics and Astronomy (Astronomy Major)",
        "program_page": "https://astron.snu.ac.kr/en",
        "entry_route": {
            "code": "Master's usually required",
            "value": "Offers Master's and Doctoral programs only (no Combined Master's & Doctoral track in the central programs table); Doctoral entry requires a master's degree or equivalent.",
            "quote": f"{ENTRY_ELIG_MASTERS_PREFIX} | Astronomy Major ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": "Not stated",
        "notes": "Research facilities include SNU Astronomical Observatory (SAO), Seoul Radio Astronomical Observatory, Lee Sang Gak Telescope (LSGT), KVN/Pyeongchang Optical Observatory, and Event Horizon Telescope collaboration.",
    },
    {
        "id": "snu--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "name": "Chemistry, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Natural Sciences — Department of Chemistry",
        "program_page": "https://chem.snu.ac.kr/en/admission/faq",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Chemistry ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_CHEM,
        "toefl_min": {
            "code": "86",
            "value": "Department FAQ states all applicants must meet minimum Chemistry English proficiency score of TOEFL iBT 86 or higher (TEPS 327 or higher on the old/new scale listed).",
            "quote": "All applicants for the graduate school must submit the English proficiency test score such as TOEFL, IELTS, and TEPS. For successful admission to Chemistry, the test score should meet the minimum requirements. Currently, the minimum requirements are 86 or higher for TOEFL (IBT) and 327 or higher for TEPS.",
            "url": "https://chem.snu.ac.kr/en/admission/faq",
        },
        "english_waiver": {
            "code": "No",
            "value": "Chemistry FAQ explicitly states all applicants must submit an English proficiency test score (TOEFL, IELTS, or TEPS), stricter than SNU's central medium-of-instruction exemption.",
            "quote": "All applicants for the graduate school must submit the English proficiency test score such as TOEFL, IELTS, and TEPS.",
            "url": "https://chem.snu.ac.kr/en/admission/faq",
        },
        "supervisor": {
            "code": "Not required",
            "value": "Department FAQ explicitly states pre-admission faculty contact is only informational and not required for admission; admitted students select a supervisor after matriculation interviews.",
            "quote": "We remind any interested student that the pre-admission contact is only to provide information. The pre-admission contact will not be considered as a necessary step for admission. | After admission, students can choose their supervisors after interview with faculty members.",
            "url": "https://chem.snu.ac.kr/en/admission/faq",
        },
        "funding": {
            "code": "Guaranteed",
            "value": "Department guarantees full financial support for graduate students covering tuition, fees, housing, and living expenses (all graduate students complete one chemistry lab TAship and one regular class TAship).",
            "quote": "The school of chemistry guarantees full financial support for graduate students. The support includes tuitions and fees, housing, and living expenses.",
            "url": "https://chem.snu.ac.kr/en/admission/faq",
        },
        "notes": "Department FAQ contains a minor typo printing tuition as '38 M KRW (~ 3500 USD) per semester' (central Appendix 2 lists KRW 3,971,000 per semester for Natural Sciences excluding Mathematical Sciences). Note Interdisciplinary Program in Biophysics and Chemical Biology and WCU/CALS Applied Life Chemistry also offer related tracks.",
    },
    {
        "id": "snu--biology",
        "field": "biology",
        "also_fields": [],
        "name": "Biological Sciences, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Natural Sciences — School of Biological Sciences",
        "program_page": "https://biosci.snu.ac.kr/en/academics/curriculum/graduate",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Biological Sciences ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Tracks include Molecular & Cellular Biology (MCB), Integrative Organismic Biology (IOB), and Systematics & Ecology (SE). Also related interdisciplinary M/C/D Ph.D. programs in Genetic Engineering, Bioinformatics, Agricultural Biotechnology (CALS), and Applied Bioengineering (GSCST).",
    },
    {
        "id": "snu--earth",
        "field": "earth",
        "also_fields": ["environment"],
        "name": "Earth and Environmental Sciences, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Natural Sciences — School of Earth and Environmental Sciences",
        "program_page": "https://sees.snu.ac.kr/en/academics/graduate/courses",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Earth and Environmental Sciences ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Cross-listed under environment because SEES spans Atmospheric Sciences, Earth System Science (geology/geophysics/geochemistry), and Oceanography.",
    },
    {
        "id": "snu--environment",
        "field": "environment",
        "also_fields": [],
        "name": "Environmental Management, Ph.D.",
        "department": "Graduate School of Environmental Studies — Department of Environmental Management",
        "program_page": "https://gses.snu.ac.kr/en/academics/doctoral-courses",
        "entry_route": {
            "code": "Master's usually required",
            "value": "Offers Master's and Doctoral programs only (no Combined Master's & Doctoral track in GSES); Doctoral entry requires a master's degree or equivalent.",
            "quote": f"{ENTRY_ELIG_MASTERS_PREFIX} | Environmental Management ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "funding": {
            "code": "Competitive",
            "value": "Competitive internal GSES Research Assistant (RA) scholarships (full tuition waiver + stipend for one student per semester per professor), Development Fund tuition waivers, alumni/overseas student scholarships, plus central GSFS/SPF fellowships.",
            "quote": "Research Assistant(RA) Scholarship | Full waiver of tuition and scholarship for one student per semester per professor | Development Fund Special Scholarship | Full tuition waiver scholarship from Seoul National University Development Fund (one student per semester)",
            "url": "https://gses.snu.ac.kr/en/information/scholarship",
            "also": [
                {
                    "quote": "SNU President Fellowship Program (SPF) | Tuition fee: full tuition exemption for a maximum of 6 semesters | Graduate Scholarship for Excellent Foreign Students (GSFS) | Tuition fee: full tuition exemption for a maximum of 4 semesters",
                    "url": SCHOL_URL,
                }
            ],
        },
        "notes": "Department of Environmental Management (newly separated from Environmental Planning in 2025) focuses on climate change and carbon neutrality. Additional environmental Ph.D. tracks exist at Graduate School of Public Health (Environmental Health Sciences, M/D) and CALS (Forest Environmental Science, M/D; Agricultural & Forest Meteorology, M/D).",
    },
    {
        "id": "snu--neuro",
        "field": "neuro",
        "also_fields": [],
        "name": "Neuroscience (Interdisciplinary Program), Ph.D. / Combined Master's & Doctoral",
        "department": "College of Natural Sciences — Interdisciplinary Program in Neuroscience",
        "program_page": "https://science.snu.ac.kr/en/edu/programs",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Neuroscience Major ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": "Not stated",
        "notes": "SNU also offers Ph.D. programs in Department of Brain and Cognitive Sciences (bcs.snu.ac.kr, which notes higher domestic TEPS 327 in general admissions) and Program in Neuroscience at the School of Dentistry (M/D).",
    },
    {
        "id": "snu--biomed",
        "field": "biomed",
        "also_fields": [],
        "name": "Biomedical Sciences, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Medicine — Department of Biomedical Sciences",
        "program_page": "https://biomed.snu.ac.kr/en",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Biomedical Sciences ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "supervisor": {
            "code": "Not required",
            "value": "Department FAQ (Korean) explicitly states whether an applicant contacted/interviewed a prospective advisor beforehand does not affect admissions exam acceptance; incoming students have the department chair as temporary advisor and select an advisor after matriculation (with 2-3 lab rotations for combined MS-PhD students).",
            "quote": "물론 사전면접 여부는 입학시험의 합격 여부에는 영향을 주지 않습니다.",
            "url": "https://biomed.snu.ac.kr/admission/faq",
            "also": [
                {
                    "quote": "지도교수가 결정되기 전까지 신입생의 학사지도는 임시 지도교수의 자격으로 의과학과 학과장이 담당한다.",
                    "url": "https://biomed.snu.ac.kr/academics/info/advisor",
                }
            ],
        },
        "notes": "Housed at SNU Yeongeon medical campus. Related Ph.D. programs exist across College of Medicine (Anatomy & Cell Biology, Cancer Biology, Medical Informatics, Translational Medicine, Human Systems Medicine) and Graduate School of Convergence Science and Technology (Molecular Medicine and Biopharmaceutical Sciences).",
    },
    {
        "id": "snu--bme",
        "field": "bme",
        "also_fields": [],
        "name": "Bioengineering (Interdisciplinary Program), Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Interdisciplinary Program in Bioengineering",
        "program_page": "https://eng.snu.ac.kr/en/academics/graduate-programs/interdisciplinary-program-in-bioengineering",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Bioengineering Major ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Focuses on medical informatics, molecular diagnostics, biomedical materials, rehabilitation equipment, and bionic signal processing. SNU also offers Biosystems Engineering (CALS), Biomedical Engineering (College of Medicine, M/D), and Applied Bioengineering (GSCST).",
    },
    {
        "id": "snu--materials",
        "field": "materials",
        "also_fields": [],
        "name": "Materials Science and Engineering, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Department of Materials Science and Engineering",
        "program_page": "https://eng.snu.ac.kr/en/academics/graduate-programs/materials-science-and-engineering",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Materials Science and Engineering ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Covers Metallurgy, Ceramics, Electronic & Photonic Materials, and Polymers; also includes the WCU Hybrid Materials Major (M/C/D).",
    },
    {
        "id": "snu--mech",
        "field": "mech",
        "also_fields": [],
        "name": "Mechanical Engineering, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Department of Mechanical Engineering",
        "program_page": "https://eng.snu.ac.kr/en/academics/graduate-programs/mechanical-engineering",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Mechanical Engineering ◯ ◯ ◯",
            "url": PDF_URL,
            "also": [
                {
                    "quote": "Admissions are processed for the following academic programs; Master’s, combined Master’s/Doctoral, and Doctoral programs.",
                    "url": "https://eng.snu.ac.kr/en/academics/graduate-programs/mechanical-engineering",
                }
            ],
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Covers mechanics, thermal engineering, dynamics & control, fluid engineering, design & manufacturing, and nano/bio engineering; also WCU Multiscale Mechanical Design Major, Aerospace Engineering, and Naval Architecture & Ocean Engineering (all M/C/D).",
    },
    {
        "id": "snu--civil",
        "field": "civil",
        "also_fields": [],
        "name": "Civil, Urban and Environmental Engineering, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Department of Civil, Urban and Environmental Engineering",
        "program_page": "https://eng.snu.ac.kr/en/academics/graduate-programs/civil-urban-and-environmental-engineering",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | (Civil and Environmental Engineering ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Covers structural, geotechnical, hydro, transportation, environmental, spatial informatics, construction management, and smart city engineering tracks.",
    },
    {
        "id": "snu--chemeng",
        "field": "chemeng",
        "also_fields": [],
        "name": "Chemical and Biological Engineering, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Department of Chemical and Biological Engineering",
        "program_page": "https://eng.snu.ac.kr/en/academics/graduate-programs/chemical-and-biological-engineering",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Chemical and Biological ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Also offers WCU Chemical Convergence for Energy and Environment Major (M/D).",
    },
    {
        "id": "snu--ece",
        "field": "ece",
        "also_fields": [],
        "name": "Electrical and Computer Engineering, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Department of Electrical and Computer Engineering",
        "program_page": "https://ece.snu.ac.kr/en/academics/graduate/curriculum",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Electrical and Computer Engineering ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "funding": {
            "code": "Competitive",
            "value": "Competitive funding via BK21 Four SNU Global EDGE Fellowship for incoming international PhD students (full tuition + KRW 1,800,000/month), ECE TA/RA and Tuition Exemption Scholarships, plus university-wide GSFS/SPF fellowships.",
            "quote": "We are pleased to announce that applications for the SNU Global EDGE Fellowship Program for Fall 2026 are now open. | 3. Scholarship Benefits | - Full tuition coverage | - Monthly stipend of KRW 1,800,000",
            "url": "https://ece.snu.ac.kr/en/community/notice?md=v&bbsidx=58088",
            "also": [
                {
                    "quote": "Various scholarship and student loan programs are available for both domestic and international students with outstanding academic standing or financial need. | - Tuition and Admission Fee Exemption Scholarship | - Teaching, Research Assistant Scholarship",
                    "url": "https://ece.snu.ac.kr/en/academics/resources/scholarship",
                }
            ],
        },
        "notes": "96 of 135 ECE graduate courses provide online lecture notes; research groups span semiconductors, photonics, communications, power systems, control/robotics, and computer systems.",
    },
    {
        "id": "snu--cs",
        "field": "cs",
        "also_fields": [],
        "name": "Computer Science and Engineering, Ph.D. / Combined Master's & Doctoral",
        "department": "College of Engineering — Department of Computer Science and Engineering",
        "program_page": "https://eng.snu.ac.kr/en/academics/graduate-programs/computer-science-and-engineering",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Computer Science and Engineering ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "BK21 FOUR Intelligence Computing; related graduate tracks include Interdisciplinary Program in Artificial Intelligence and GSCST Department of Intelligence and Information (M/C/D).",
    },
    {
        "id": "snu--datasci",
        "field": "datasci",
        "also_fields": [],
        "name": "Data Science, Ph.D. / Combined Master's & Doctoral",
        "department": "Graduate School of Data Science",
        "program_page": "https://gsds.snu.ac.kr/",
        "entry_route": {
            "code": "Either",
            "value": "Accepts both bachelor's holders (Combined Master's & Doctoral course) and master's holders (Doctoral program).",
            "quote": f"{ENTRY_ELIG_EITHER_PREFIX} | Graduate School Data Science ◯ ◯ ◯",
            "url": PDF_URL,
        },
        "gre_subject": NO_SUBJ_STD,
        "notes": "Professional graduate school established in 2020 offering M.S., Combined M.S./Ph.D., and Ph.D. degrees in Data Science; also coordinates an Interdisciplinary Major in Applied Data Science.",
    },
]

for p in programs:
    rec = {
        "id": p["id"],
        "university": "snu",
        "field": p["field"],
        "also_fields": p["also_fields"],
        "name": p["name"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "Not stated",
                "value": "Fall 2027 International Admissions Guide has not yet been published by SNU Office of Admissions (Spring 2027 international online application ran July 6-9, 2026).",
                "quote": "",
                "url": APP_URL,
            },
            "gre_subject": (
                {
                    "code": "Not stated",
                    "value": "Central SNU Graduate Admissions Guide does not specify whether GRE Subject scores are expected or accepted for this program.",
                    "quote": "",
                    "url": PDF_URL,
                }
                if p["gre_subject"] == "Not stated"
                else p["gre_subject"]
            ),
            "supervisor": p.get(
                "supervisor",
                {
                    "code": "Not stated",
                    "value": "Central SNU Graduate Admissions Guide and the department's English pages do not state whether pre-application supervisor contact is required.",
                    "quote": "",
                    "url": p["program_page"],
                },
            ),
            "funding": p.get("funding", COMPETITIVE_CENTRAL),
            "entry_route": p["entry_route"],
        },
        "notes": p["notes"],
    }
    if "toefl_min" in p:
        rec["fields"]["toefl_min"] = p["toefl_min"]
    if "english_waiver" in p:
        rec["fields"]["english_waiver"] = p["english_waiver"]

    (PROG_DIR / f"{p['id']}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Wrote snu.json and {len(programs)} program files to data/staging/")
