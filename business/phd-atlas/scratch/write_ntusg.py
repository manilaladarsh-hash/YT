import os
import sys
from pathlib import Path

os.environ["ATLAS_OUT"] = "data/staging"
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import rec  # noqa: E402

CHECKED = "2026-11-14"
ETS_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

URL_GUIDE = "https://www.ntu.edu.sg/admissions/graduate/radmissionguide"
URL_FAQ = "https://www.ntu.edu.sg/admissions/graduate/frequently-asked-questions"
URL_SCHOL_FAQ = "https://www.ntu.edu.sg/admissions/graduate/financialmatters/scholarships/frequently-asked-questions"
URL_RSS = "https://www.ntu.edu.sg/admissions/graduate/financialmatters/scholarships/rss"
URL_NPGS = "https://www.ntu.edu.sg/admissions/graduate/financialmatters/scholarships/npgs"
URL_PGA = "https://www.ntu.edu.sg/admissions/graduate/financialmatters/scholarships/pga"

SUP_REC_QUOTE = (
    "It is highly recommended that you seek out a potential supervisor prior to submitting your application. "
    "Alternatively, if you have not identified one, the School will appoint a supervisor based on your research interests."
)

RSS_FUNDING_QUOTE = (
    "The NTU Research Scholarship is awarded to outstanding graduate students for research. | "
    "In addition to the monthly stipend, the award also covers the annual tuition fee."
)
RSS_FUNDING_VAL = (
    "Full-time PhD students are eligible on a competitive basis for the NTU Research Scholarship "
    "(S$3,000/month for international students, plus up to S$500/month after passing the Qualifying Examination, "
    "and annual tuition fee coverage for up to 4 years; S$3,400 PR / S$3,800 Singapore Citizen), "
    "as well as the Nanyang President's Graduate Scholarship and Provost Graduate Award (S$4,300/month international)."
)

DEADLINE_CENTRAL_QUOTE = "August (Semester 1) | 1 October | 31 January"

rec.save_university(
    uid="ntusg",
    institution="Nanyang Technological University, Singapore",
    country="Singapore",
    region="Singapore",
    grad_page=URL_GUIDE,
    checked=CHECKED,
    fields={
        "app_fee": (
            "50 SGD",
            "S$50 (nett) non-refundable application fee per research application (waived only for nationals who have resided since birth in Singapore or 55 listed developing countries; India is not on the list).",
            "An application fee of S$50 (Nett) will be charged for each Research application. Payment can be made online before submitting application by VISA/Mastercard.",
            URL_GUIDE,
        ),
        "fee_waiver": (
            "Limited",
            "Automatic application fee waiver applies only to nationals who have resided since birth in Singapore or 55 listed developing countries (India is not on the 56-country waiver list, so Indian applicants pay S$50).",
            "Wavier of Application fees will be extended to applicants from the countries listed below, if they are nationals of an eligible country and have resided there since birth.",
            URL_GUIDE,
        ),
        "gre_general": (
            "Optional",
            "GRE/GMAT/GATE scores are optional across NTU research programs (minimum 90th percentile GATE within 3 years accepted from Indian applicants to strengthen applications), except where specific schools/programs require or do not require them.",
            "GRE / GMAT / GATE are optional*. | Strong evidence of quantitative, verbal, and/or analytical skills through these tests will enhance your application.",
            URL_GUIDE,
        ),
        "toefl_min": (
            "Not stated",
            "Central graduate research guide requires a 'good TOEFL/IELTS score' without a university-wide numerical cutoff; individual schools set minimums (EEE 100, MSE 100, ASE 5.0 new scale, IGP Neuroscience 105).",
            "English Language Proficiency: A good TOEFL/IELTS score for applicants whose Bachelor’s degree is not conducted in English.",
            URL_GUIDE,
        ),
        "ielts_min": (
            "Not stated",
            "Central graduate research guide does not specify a university-wide IELTS band minimum; individual schools set minimums (EEE 6.5, MSE 6.5, ASE 6.5, IGP Neuroscience 7.0).",
            "English Language Proficiency: A good TOEFL/IELTS score for applicants whose Bachelor’s degree is not conducted in English.",
            URL_GUIDE,
        ),
        "english_waiver": (
            "Conditional",
            "Applicants whose tertiary studies were taught in English may request a TOEFL/IELTS waiver by submitting an official Medium of Instruction certification letter from their home university (case-by-case at the School's discretion).",
            "If the medium of instruction used in your studies is English, you may obtain a letter from your home University to certify the medium of instruction for waiver.",
            URL_SCHOL_FAQ,
            {
                "also": [
                    {
                        "quote": "Test score (TOEFL/IELTS, GRE) exemptions are granted on a case-by-case basis at the School's discretion. Contact the School directly for more information.",
                        "url": URL_FAQ,
                    }
                ]
            },
        ),
    },
    notes=(
        "Covers 17 of 18 Atlas STEM fields across 13 PhD programs (no standalone Astronomy PhD at NTU Singapore). "
        "Note two school-specific August 2027 intake deadlines differ from NTU's standard 2027-01-31 cutoff: "
        "LKCMedicine (biomed) closes 2026-12-31, and CEE (civil) closes 2027-02-28. "
        "International PhD Research Scholarship stipends were revised effective January 2026 to S$3,000/month "
        "(+ up to S$500/month post-QE) with full tuition coverage, and NPGS/PGA to S$4,300/month."
    ),
)

# 1. CS (+ datasci) - CCDS
rec.save_program(
    uid="ntusg",
    field="cs",
    also_fields=["datasci"],
    department="College of Computing and Data Science (CCDS)",
    page="https://www.ntu.edu.sg/education/graduate-programme/ccds-phd-computing-datascience",
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 (Semester 1) intake deadline is January 31, 2027 (application portal opens October 1; January intake deadline is July 31).",
            DEADLINE_CENTRAL_QUOTE,
            URL_GUIDE,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for computer science or data science.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor prior to applying; if none is identified, the School appoints one based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            RSS_FUNDING_QUOTE,
            URL_RSS,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD admission from a strong bachelor's degree with minimum Honours (Distinction) or equivalent.",
            "Bachelor’s Degree: A strong Bachelor’s degree with minimum Honours (Distinction) and its equivalent.",
            "https://www.ntu.edu.sg/education/graduate-programme/ccds-phd-computing-datascience",
        ),
    },
    notes=(
        "Covers Doctor of Philosophy in Computing and Data Science (Artificial Intelligence, Data Science, Computer Science). "
        "NTU's Interdisciplinary Graduate Programme (IGP) also offers an AI-X interdisciplinary PhD track supervised jointly by AI and domain faculty."
    ),
)

# 2. Chemistry - CCEB
URL_CHEM = "https://www.ntu.edu.sg/cceb/admissions/detail/doctor-of-philosophy-(phd)-in-chemistry"
rec.save_program(
    uid="ntusg",
    field="chemistry",
    department="School of Chemistry, Chemical Engineering and Biotechnology (CCEB) — Chemistry",
    page=URL_CHEM,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 (Semester 1) intake closes January 31, 2027 (portal opens October 1; January intake closes July 31).",
            DEADLINE_CENTRAL_QUOTE,
            URL_GUIDE,
            {"also": [{"quote": "August (Semester 1) | 1 October", "url": URL_CHEM}]},
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for chemistry (discontinued in May 2023).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor before applying; otherwise the School assigns a supervisor based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            RSS_FUNDING_QUOTE,
            URL_RSS,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a relevant bachelor's degree with minimum Honours (Distinction / Upper Second Class Honours); a master's degree is not mandatory.",
            "Applicants should possess a good relevant Bachelor’s degree with Honours, with a minimum of Distinction, Upper Second Class Honours or its equivalent. A Master’s degree is not mandatory.",
            URL_CHEM,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS may be waived if the applicant provides documentary proof (such as an official letter or certificate) that English was the medium of instruction during tertiary studies.",
            "This requirement may be waived if the applicant can provide documentary proof, normally in the form of a letter or certificate, that English was the medium of instruction during their tertiary studies.",
            URL_CHEM,
        ),
    },
    notes="CCEB PhD applicants must also submit a short video essay alongside two academic references and research proposal.",
)

# 3. Chemical & Biomedical Engineering (+ bme) - CCEB
URL_CHEMENG = "https://www.ntu.edu.sg/cceb/admissions/detail/cceb-doctor-of-philosophy-(phd)-(by-research)"
rec.save_program(
    uid="ntusg",
    field="chemeng",
    also_fields=["bme"],
    department="School of Chemistry, Chemical Engineering and Biotechnology (CCEB) — Chemical and Biomedical Engineering",
    page=URL_CHEMENG,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 (Semester 1) intake closes January 31, 2027 (portal opens October 1; January intake closes July 31).",
            DEADLINE_CENTRAL_QUOTE,
            URL_GUIDE,
            {"also": [{"quote": "August (Semester 1) | 1 October", "url": URL_CHEMENG}]},
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for chemical or biomedical engineering.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor before applying; otherwise the School assigns a supervisor based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            RSS_FUNDING_QUOTE,
            URL_RSS,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a relevant bachelor's degree with minimum Honours (Distinction / Upper Second Class Honours); a master's degree is not mandatory.",
            "Applicants should possess a good relevant Bachelor’s degree with Honours, with a minimum of Distinction, Upper Second Class Honours or its equivalent. A Master’s degree is not mandatory.",
            URL_CHEMENG,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS may be waived if the applicant provides documentary proof (letter or certificate) that English was the medium of instruction during tertiary studies.",
            "This requirement may be waived if the applicant can provide documentary proof, normally in the form of a letter or certificate, that English was the medium of instruction during their tertiary studies.",
            URL_CHEMENG,
        ),
    },
    notes="Covers NTU's PhD in Chemical and Biomedical Engineering (biotechnology, tissue engineering, chiral/pharmaceutical sciences, process systems); MAE also offers a Biomedical Engineering PhD research area.",
)

# 4. Civil & Environmental Engineering - CEE
URL_CIVIL = "https://www.ntu.edu.sg/cee/admissions/graduate/detail/cee-phd-programme-(by-research)"
rec.save_program(
    uid="ntusg",
    field="civil",
    department="School of Civil and Environmental Engineering (CEE)",
    page=URL_CIVIL,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-02-28",
            "School of CEE August 2027 intake application period runs 1 October to 28 February (later than NTU's central 31 January deadline; January intake closes 31 July).",
            "August | 1 October – 28 February",
            URL_CIVIL,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for civil or environmental engineering.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor before applying; otherwise the School assigns a supervisor based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            "Research Scholarships | Nanyang President's Graduate Scholarship | NTU Research Scholarship | Provost Graduate Award",
            URL_CIVIL,
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD admission from a good Honours bachelor's degree (preferably at least Second Class Upper / Honours Distinction).",
            "Applicants should possess a good Honours degree, preferably at least Second Class Honours (Upper Division) or Honours (Distinction), and demonstrate the ability to undertake research in their proposed field of study.",
            URL_CIVIL,
        ),
    },
    notes="CEE offers a school-specific August intake deadline of 28 February (vs 31 January centrally).",
)

# 5. Electrical and Electronic Engineering - EEE
URL_ECE = "https://www.ntu.edu.sg/engineering/coe-programmes/graduate/coe-programme-detail/eee-doctor-of-philosophy-(ph.d)-programme"
rec.save_program(
    uid="ntusg",
    field="ece",
    department="School of Electrical and Electronic Engineering (EEE)",
    page=URL_ECE,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 (Semester 1) intake closes January 31, 2027 (application portal opens October 1; January intake closes July 31).",
            DEADLINE_CENTRAL_QUOTE,
            URL_GUIDE,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for electrical or computer engineering.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor before applying; otherwise the School assigns a supervisor based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            "Research scholarships or financial top-ups (for selected industrial projects only) are available to outstanding candidates.",
            URL_ECE,
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a relevant bachelor's degree with at least 2nd class Honours upper or equivalent.",
            "Applicants from overseas universities must have a relevant Bachelor’s degree with at least 2nd class Honours upper or equivalent.",
            URL_ECE,
        ),
        "gre_general": (
            "Optional",
            "GRE is not mandatory for EEE PhD applicants, though satisfactory scores (V >= 149, Q >= 149, V+Q >= 319, AW >= 3.5; or GATE >= 90th percentile for applicants from India) strengthen admission chances.",
            "Graduate Record Examination (GRE) is not mandatory but having these satisfactory test scores will enhance the chances of admission. Applicants from India may use Graduate Aptitude Test in Engineering (GATE) in place of GRE.",
            URL_ECE,
        ),
        "toefl_min": (
            "100",
            "EEE requires a minimum TOEFL score of 100 iBT (250 CBT / 600 PBT) within 2 years for overseas applicants unless waived via English MOI documentation.",
            "Minimum TOEFL score must be at least: | 100 for internet-based test",
            URL_ECE,
        ),
        "ielts_min": (
            "6.5",
            "EEE requires a minimum IELTS score of 6.5 within 2 years for overseas applicants unless waived via English MOI documentation.",
            "Minimum IELTS score must be at least 6.5.",
            URL_ECE,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS may be waived for EEE applicants who submit documentary proof (letter or certificate) that English was the medium of instruction during tertiary studies.",
            "The TOEFL/IELTS requirement may be waived if the applicant can submit documentation that English was used as the medium of instruction during tertiary studies. The documentary proof is usually in a form of a letter or certificate.",
            URL_ECE,
        ),
    },
    notes="EEE explicitly specifies TOEFL >= 100 iBT / IELTS >= 6.5 and recommended GRE benchmarks (V+Q >= 319, AW >= 3.5, or GATE >= 90th percentile for India) for overseas graduates.",
)

# 6. Mechanical and Aerospace Engineering - MAE
URL_MECH = "https://www.ntu.edu.sg/engineering/coe-programmes/graduate/coe-programme-detail/mae-phd"
rec.save_program(
    uid="ntusg",
    field="mech",
    department="School of Mechanical and Aerospace Engineering (MAE)",
    page=URL_MECH,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 intake deadline is January 31, 2027 (application portal opens October 1; January intake deadline is July 31).",
            "August Semester | 1 October | 31 January",
            URL_MECH,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for mechanical or aerospace engineering.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "Applicants must list preferred supervisors on the application and are strongly encouraged to contact potential supervisors before submitting.",
            "Applicants are required to indicate their preferred supervisors in the application. Candidates are strongly encouraged to contact potential supervisors in advance before submitting their application.",
            URL_MECH,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            RSS_FUNDING_QUOTE,
            URL_RSS,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a strong bachelor's degree with minimum Honours (Distinction) or equivalent.",
            "1. Bachelor’s Degree: A strong Bachelor’s degree with minimum Honours (Distinction) and its equivalent.",
            URL_MECH,
        ),
    },
    notes="Covers Mechanical Engineering and Aerospace Engineering PhD research areas (also includes Robotics & Intelligent Systems and Biomedical Engineering tracks).",
)

# 7. Materials Science and Engineering - MSE
URL_MAT = "https://www.ntu.edu.sg/education/graduate-programme/mse-doctor-of-philosophy-(phd)"
URL_MAT_OVER = "https://www.ntu.edu.sg/mse/admissions/postgraduates/prospective-students/doctor-of-philosophy-master-of-engineering"
rec.save_program(
    uid="ntusg",
    field="materials",
    department="School of Materials Science and Engineering (MSE)",
    page=URL_MAT,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 intake deadline with supporting documents is January 31, 2027 (January intake: July 31).",
            "August Semester | 31 January",
            URL_MAT_OVER,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for materials science and engineering.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor before applying; otherwise the School assigns a supervisor based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            RSS_FUNDING_QUOTE,
            URL_RSS,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a relevant bachelor's degree with at least 2nd Upper Honours (1st Class Honours required for universities in India; 80+ average for China).",
            "Applicants from overseas universities must have a relevant Bachelor’s degree with at least 2nd Upper Honours or better. | Applicants from universities in India must have 1st Class Honours for the relevant Bachelor’s degree.",
            URL_MAT,
        ),
        "toefl_min": (
            "100",
            "MSE requires a minimum TOEFL score of 100 iBT (250 CBT / 600 PBT) within 2 years unless waived via English MOI documentation.",
            "Minimum TOEFL score must be equivalent to or more than: | 100 for internet-based test",
            URL_MAT,
        ),
        "ielts_min": (
            "6.5",
            "MSE requires a minimum IELTS score of 6.5 within 2 years unless waived via English MOI documentation.",
            "Minimum IELTS score must be equivalent to or more than 6.5.",
            URL_MAT,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS may be waived if the applicant provides documentary proof (letter or certificate) that English was the medium of instruction during tertiary studies.",
            "The TOEFL/IELTS requirements may be waived if the applicant can prove that English was used as the medium of instruction during tertiary studies. The documentary proof is usually in a form of a letter or certificate.",
            URL_MAT,
        ),
    },
    notes="MSE specifies 1st Class Honours for Indian bachelor's applicants, TOEFL >= 100 iBT / IELTS >= 6.5, and requires at least one accepted first-author/co-first-author publication before PhD thesis submission.",
)

# 8. Biological Sciences - SBS
URL_BIO = "https://www.ntu.edu.sg/sbs/admissions/graduate/research/application-for-admission/admission-criteria"
rec.save_program(
    uid="ntusg",
    field="biology",
    department="School of Biological Sciences (SBS)",
    page=URL_BIO,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 (Semester 1) intake closes January 31, 2027 (application window October 1 – January 31; January intake closes July 31).",
            "August Intake (Semester 1) | 1 October – 31 January | 31 January",
            URL_BIO,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for biology (ETS discontinued Biology and Biochemistry Subject Tests).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "NTU strongly recommends contacting a potential supervisor before applying; otherwise the School assigns a supervisor based on research interests.",
            SUP_REC_QUOTE,
            URL_SCHOL_FAQ,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            "NTU offers a wide range of scholarships for full-time Ph.D. studies to Singapore citizens, Singapore permanent residents and international applicants.",
            "https://www.ntu.edu.sg/sbs/admissions/graduate/research/application-for-admission/scholarship",
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a relevant bachelor's degree with at least 2nd Upper Honours or equivalent.",
            "Applicants from overseas universities must have a relevant Bachelor’s degree with at least 2nd Upper Honours or better, or the equivalent.",
            URL_BIO,
        ),
        "gre_general": (
            "Not required",
            "SBS explicitly states that GRE and GATE scores are optional and need not be provided for overseas applicants.",
            "Graduate Record Examination (GRE) and Graduate Aptitude Test in Engineering (GATE) scores are optional and need not be provided.",
            URL_BIO,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS may be waived if the applicant provides documentary proof that English was used as the medium of instruction during tertiary studies.",
            "TOEFL/IELTS scores are required if the Bachelor's degree was not conducted in English. These may be waived if the applicant can provide documentary proof that English was used as the medium of instruction during tertiary studies.",
            URL_BIO,
        ),
    },
    notes="SBS PhD applicants are required to submit a short video essay in addition to standard supporting documents.",
)

# 9. Mathematical Sciences (+ statistics) - SPMS
URL_MATH = "https://www.ntu.edu.sg/spms/about-us/mathematics/grad/phd"
URL_SPMS_FAQ = "https://www.ntu.edu.sg/spms/admissions/grad/grad-faqs"
URL_SPMS_SCHOL = "https://www.ntu.edu.sg/spms/admissions/grad/scholarships"
rec.save_program(
    uid="ntusg",
    field="math",
    also_fields=["statistics"],
    department="School of Physical and Mathematical Sciences (SPMS) — Division of Mathematical Sciences",
    page=URL_MATH,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 intake deadline is January 31, 2027 (application period October to January; January intake June to July / closes July 31).",
            DEADLINE_CENTRAL_QUOTE,
            URL_GUIDE,
            {
                "also": [
                    {
                        "quote": "There are two application periods each year: October to January (for admission in August), and June to July (for admission in January).",
                        "url": URL_MATH,
                    }
                ]
            },
        ),
        "gre_subject": (
            "Not required",
            "SPMS Mathematics PhD lists only general GRE/GATE (319 V+Q, 3.5 AW encouraged in FAQs) as optional and does not require the GRE Mathematics Subject Test.",
            "[Optional] GRE/GATE test scores - Demonstrating strong quantitative, verbal, or analytical skills through the submission of will enhance your application.",
            URL_MATH,
            {
                "also": [
                    {
                        "quote": "A Graduate Record Examinations (GRE) test score of 319 (Verbal and Quantitative Reasoning) + 3.5 (Analytical Writing) and above is strongly encouraged.",
                        "url": URL_SPMS_FAQ,
                    }
                ]
            },
        ),
        "supervisor": (
            "Recommended",
            "Unlike SPMS Physics, SPMS Mathematics does not require pre-admission supervisor sign-off, though SPMS FAQs advise contacting faculty before applying.",
            "For PhD and MSc by research, contact the faculty member(s) you are interested in working with, and ask if they are interested in supervising you.",
            URL_SPMS_FAQ,
            {"also": [{"quote": SUP_REC_QUOTE, "url": URL_SCHOL_FAQ}]},
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            "The NTU Research Scholarship is assigned by the School, and may be offered to applicants during the PhD programme application process (subject to limited availability).",
            URL_SPMS_SCHOL,
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a bachelor's degree in Mathematics or related discipline with minimum Honours (Distinction); an MSc is optional and not mandatory.",
            "For the PhD programme, applicants may optionally have a MSc degree in Mathematics or a related discipline, but this is not mandatory.",
            URL_MATH,
        ),
    },
    notes=(
        "Division of Mathematical Sciences research covers Pure Mathematics, Coding and Cryptography, Computational Mathematics, "
        "and Applied Mathematics and Statistics. Note SPMS Scholarships page shows outdated RSS figures vs central January 2026 rates (S$3,000/month international)."
    ),
)

# 10. Physics - SPMS
URL_PHYS = "https://www.ntu.edu.sg/spms/about-us/physics/grad/phd"
rec.save_program(
    uid="ntusg",
    field="physics",
    department="School of Physical and Mathematical Sciences (SPMS) — Division of Physics and Applied Physics",
    page=URL_PHYS,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 intake deadline is January 31, 2027 (application period October to January; January intake June to July).",
            DEADLINE_CENTRAL_QUOTE,
            URL_GUIDE,
            {
                "also": [
                    {
                        "quote": "There are two application periods each year: October to January (for admission in August), and June to July (for admission in January).",
                        "url": URL_PHYS,
                    }
                ]
            },
        ),
        "gre_subject": (
            "Not required",
            "SPMS Physics PhD lists only general GRE/GATE as optional and does not require the GRE Physics Subject Test.",
            "[Optional] GRE/GATE test scores - Demonstrating strong quantitative, verbal, or analytical skills through the submission of will enhance your application.",
            URL_PHYS,
            {
                "also": [
                    {
                        "quote": "A Graduate Record Examinations (GRE) test score of 319 (Verbal and Quantitative Reasoning) + 3.5 (Analytical Writing) and above is strongly encouraged.",
                        "url": URL_SPMS_FAQ,
                    }
                ]
            },
        ),
        "supervisor": (
            "Required",
            "Applicants are admitted to the Division of Physics and Applied Physics PhD only if a faculty member agrees to be their research supervisor before formal application.",
            "Graduate students are admitted into the Division of Physics and Applied Physics only if a faculty member agrees to be the research supervisor. | Once a faculty member has agreed to accept you as a graduate student, you may start the formal application process.",
            URL_PHYS,
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            "The NTU Research Scholarship is assigned by the School, and may be offered to applicants during the PhD programme application process (subject to limited availability).",
            URL_SPMS_SCHOL,
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a BSc in Physics or related discipline with minimum Honours (Distinction); an MSc is optional and not mandatory.",
            "Applicants may optionally have a MSc degree in physics or a related discipline, but this is not mandatory.",
            URL_PHYS,
        ),
    },
    notes="SPMS Physics strictly requires faculty supervisor agreement prior to starting the formal application, and requires at least one first-author paper publication for August 2024+ cohorts.",
)

# 11. Earth and Environmental Science (+ earth) - ASE
URL_ASE = "https://www.ntu.edu.sg/ase/admissions/graduate-programmes/phd"
URL_ASE_FAQ = "https://www.ntu.edu.sg/ase/admissions/graduate-programmes/faqs"
rec.save_program(
    uid="ntusg",
    field="environment",
    also_fields=["earth"],
    department="The Asian School of the Environment (ASE)",
    page=URL_ASE,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "August 2027 intake deadline is January 31, 2027 (January intake deadline is July 31).",
            "For August and January admissions, the deadlines for applications are 31st January and 31st July, respectively.",
            URL_ASE_FAQ,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for earth or environmental sciences.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "ASE strongly urges applicants to contact faculty members before applying to identify a supervisor and states applicants who do not contact faculty are unlikely to be admitted.",
            "Applicants are strongly encouraged to visit the projects site of the ASE and contact faculty to discuss possible PhD topics. Applicants who do not contact faculty before applying are unlikely to be admitted to the program.",
            URL_ASE_FAQ,
            {
                "also": [
                    {
                        "quote": "Before applying, please contact individual ASE faculty members to discuss potential PhD opportunities and identify a suitable faculty supervisor.",
                        "url": "https://www.ntu.edu.sg/education/graduate-programme/ase-doctor-of-philosophy-(phd)-(by-research)",
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            RSS_FUNDING_VAL,
            "Tuition fees will be in accordance with the fees set by the Ministry of Education and are subject to change. But, tuition fees should be covered under the scholarship schemes.",
            URL_ASE_FAQ,
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a bachelor's degree with minimum Honours (Distinction) or Second Class (Upper) Honours in a related science, engineering, or social science discipline.",
            "A bachelor’s degree with minimum Honours (Distinction) or Second Class (Upper) Honours in a related science, engineering, or social science programme.",
            URL_ASE,
        ),
        "toefl_min": (
            "5.0 (new scale)",
            "ASE requires TOEFL iBT 5.0+ (new 1-6 scale, Jan 2026+) or IELTS 6.5+ within 2 years unless waived via English-medium university instruction.",
            "A TOEFL (internet-based) score of 5.0 or more, or IELTS score of 6.5 or more, is required for international applicants for whom English is not their first language and/or graduates of universities in which English is not the medium of instruction.",
            URL_ASE,
        ),
        "ielts_min": (
            "6.5",
            "ASE requires IELTS 6.5+ (or TOEFL iBT 5.0+ on the new scale) within 2 years unless waived via English-medium university instruction.",
            "A TOEFL (internet-based) score of 5.0 or more, or IELTS score of 6.5 or more, is required for international applicants for whom English is not their first language and/or graduates of universities in which English is not the medium of instruction.",
            URL_ASE,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS is required only when English is not the applicant's first language and/or their university degree was not taught in English (university-level MOI letter accepted; NTU EPT may be arranged for selected applicants).",
            "A TOEFL (internet-based) score of 5.0 or more, or IELTS score of 6.5 or more, is required for international applicants for whom English is not their first language and/or graduates of universities in which English is not the medium of instruction.",
            URL_ASE,
            {"also": [{"quote": "If the medium of instruction used in your studies is English, you may obtain a letter from your home University to certify the medium of instruction for waiver.", "url": URL_SCHOL_FAQ}]},
        ),
    },
    notes="Covers ASE's PhD in Earth and Environmental Science (geosciences, climate, geohazards, ecology, human-environment systems) and notes collaboration with Earth Observatory of Singapore (IGP-EOS).",
)

# 12. Biomedical & Health Sciences - LKCMedicine
URL_MED_APP = "https://www.ntu.edu.sg/medicine/education/graduate-programmes/phd-by-research-programme/admissions-applications"
URL_MED_SCHOL = "https://www.ntu.edu.sg/medicine/education/graduate-programmes/phd-by-research-programme/scholarships---funding-opportunities"
URL_MED_PDF = "https://www.ntu.edu.sg/media/docs/librariesprovider77/graduate-studies/lkcmedicine-phd-application-checklist_2026.pdf?sfvrsn=db8a33b1_1"
rec.save_program(
    uid="ntusg",
    field="biomed",
    department="Lee Kong Chian School of Medicine (LKCMedicine)",
    page=URL_MED_APP,
    checked=CHECKED,
    fields={
        "deadline": (
            "2026-12-31",
            "LKCMedicine August 2027 intake application window closes December 31, 2026 (one month earlier than NTU's central Jan 31 deadline; January 2028 intake: June 1–30, 2027).",
            "August 2027 | 1 October 2026 – 31 December 2026",
            URL_MED_APP,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for biomedical sciences.",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Required",
            "All LKCMedicine PhD applicants must obtain agreement from at least one eligible PhD supervisor before applying and attach confirmation email correspondence.",
            "Please note that all applicants must obtain the agreement of at least one eligible PhD supervisor before submitting an application.",
            URL_MED_SCHOL,
            {
                "also": [
                    {
                        "quote": "5 Proof of Agreement for PhD Supervision | You are required to attach the email correspondence confirming the proposed supervisor’s agreement from at least 1 proposed supervisor.",
                        "url": URL_MED_PDF,
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            "Some PhD projects and central NTU scholarships (RSS/NPGS/PGA) provide competitive funding; self-financed applicants must submit bank statement proof of financial support.",
            "A range of research projects is available across LKCMedicine's research areas, with some projects may offer scholarship opportunities.",
            URL_MED_SCHOL,
            {
                "also": [
                    {
                        "quote": "11 Documentary Proof of Financial Support | Applicants who wish to opt for self-financed must submit documentary evidence of their ability to support their study in the form of bank statement.",
                        "url": URL_MED_PDF,
                    },
                    {"quote": RSS_FUNDING_QUOTE, "url": URL_RSS},
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a strong bachelor's degree with minimum Honours (Distinction) or equivalent (master's certificate/transcript submitted only if applicable).",
            "Bachelor’s Degree: A strong Bachelor’s degree with minimum Honours (Distinction) and its equivalent.",
            URL_GUIDE,
            {
                "also": [
                    {
                        "quote": "3 Bachelor’s degree certificate | Master’s degree certificate (if applicable)",
                        "url": URL_MED_PDF,
                    }
                ]
            },
        ),
        "gre_general": (
            "Recommended",
            "LKCMedicine checklist states a GRE scoresheet is highly recommended for applicants who are not graduates of autonomous universities in Singapore.",
            "7 GRE scoresheet | Highly recommended for applicants who are not graduates from autonomous universities in Singapore.",
            URL_MED_PDF,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS is compulsory unless the applicant's university medium of instruction was fully in English, verified by an official proof letter from the university.",
            "Compulsory for applicants whose medium of instruction is not English. | If your university's medium of instruction was fully in English, please contact your university to request a proof letter and us the letter confirming your medium of instruction.",
            URL_MED_PDF,
        ),
    },
    notes=(
        "LKCMedicine PhD minimum full-time candidature is 3 years (maximum 5 years), requires confirmed supervisor agreement email at application, "
        "and closes December 31, 2026 for August 2027 entry."
    ),
)

# 13. Neuroscience - Graduate College IGP Neuroscience Ph.D. Programme
URL_NEURO = "https://www.ntu.edu.sg/research/research-focus/research-cluster-3-BrainandLearning/programmes"
URL_IGP_REQ = "https://www.ntu.edu.sg/graduate-college/admissions/programme/interdisciplinary-graduate-programme/admission-requirement"
URL_IGP_APPLY = "https://www.ntu.edu.sg/graduate-college/admissions/programme/interdisciplinary-graduate-programme/how-to-apply"
rec.save_program(
    uid="ntusg",
    field="neuro",
    department="Graduate College — Interdisciplinary Graduate Programme (IGP) Neuroscience Ph.D. Programme",
    page=URL_NEURO,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-31",
            "IGP August semester deadline is January 31, 2027 (January semester: July 31).",
            "August Semester | ​31 January",
            URL_IGP_APPLY,
        ),
        "gre_subject": (
            "Not required",
            "IGP requires GRE General (V >= 153, Q >= 149, V+Q >= 319, AW >= 3.5; or GATE >= 97% for India) for overseas degree holders and does not require the GRE Psychology Subject Test.",
            "GRE | (With validity of 5 years from date of application) | Minimum Verbal Reasoning Measure (V) ≥ 153 | Minimum Quantitative Reasoning Measure (Q) ≥ 149 | Minimum Analytical Writing (AW) ≥ 3.5 | Total V+Q ≥ 319",
            URL_IGP_REQ,
        ),
        "supervisor": (
            "Not required",
            "Incoming Neuroscience PhD students can complete up to 3 optional ~2-month lab rotations in year 1 to select a mentor (initial guidance provided by the Programme Director if no mentor is chosen beforehand).",
            "Neuroscience Ph.D. students are encouraged to complete up to 3 laboratory rotations. The goals of these rotations are to provide exposure to different conceptual approaches and experimental techniques, as well as to expose students to several laboratories to help them identify their Ph.D. mentor and home laboratory.",
            URL_NEURO,
            {
                "also": [
                    {
                        "quote": "The Director of the Neuroscience Ph.D. Programme will provide initial guidance to students prior to selection of a faculty mentor and Thesis Advisory Committee.",
                        "url": URL_NEURO,
                    }
                ]
            },
        ),
        "funding": (
            "Typical",
            "Full-time Neuroscience PhD students are eligible for full tuition and living-stipend financial support (RSS S$3,000/mo, PGA/NPGS S$4,300/mo international) for up to 4 years.",
            "All students are eligible for full financial support, including payment of their tuition and a stipend to cover their living expenses.",
            URL_NEURO,
            {"also": [{"quote": RSS_FUNDING_QUOTE, "url": URL_RSS}]},
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Direct PhD entry from a relevant bachelor's degree with 1st Class Honours or equivalent (India: 1st Class Honours with Distinction; China: 85%+ average).",
            "For Applicants with Overseas Degree | Relevant Bachelor Degree with 1st Class Honours or equivalent | Relevant Bachelor Degree with 1st Class Honours (with Distinction)",
            URL_IGP_REQ,
        ),
        "gre_general": (
            "Required",
            "Required for overseas degree applicants: GRE V >= 153, Q >= 149, V+Q >= 319, AW >= 3.5 (within 5 years); Indian applicants may substitute GATE >= 97% (within 3 years).",
            "For Applicants with Overseas Degree | AND | GRE | Minimum Verbal Reasoning Measure (V) ≥ 153 | Minimum Quantitative Reasoning Measure (Q) ≥ 149 | Minimum Analytical Writing (AW) ≥ 3.5 | Total V+Q ≥ 319 | India - Can replace with GATE score | ≥ 97%",
            URL_IGP_REQ,
        ),
        "toefl_min": (
            "105",
            "IGP requires TOEFL iBT >= 105 (or IELTS >= 7.0) within 2 years unless waived via 3+ years of English-medium tertiary study.",
            "TOEFL | (With validity of 2 years from date of application) | Internet Based Test ≥ 105",
            URL_IGP_REQ,
        ),
        "ielts_min": (
            "7.0",
            "IGP requires IELTS >= 7.0 (or TOEFL iBT >= 105) within 2 years unless waived via 3+ years of English-medium tertiary study.",
            "IELTS | (With validity of 2 years from date of application) | Minimum Score ≥ 7.0",
            URL_IGP_REQ,
        ),
        "english_waiver": (
            "Conditional",
            "TOEFL/IELTS may be waived if the applicant's tertiary studies (minimum 3 years) were conducted in English and a certification letter from the institution is provided at application.",
            "TOEFL/IELTS Requirement may be waived if medium of instruction for applicant’s tertiary studies (minimum 3 years) was conducted in English | Certification letter for medium of instruction from applicant’s tertiary institution must be provided during application",
            URL_IGP_REQ,
        ),
    },
    notes=(
        "NTU's Interdisciplinary Graduate Programme (IGP) Neuroscience Ph.D. brings together >80 faculty across 10 schools (including LKCMedicine, SBS, CCDS, MAE, EEE, CCEB, MSE, SSS). "
        "Note LKCMedicine also admits direct-entry PhD students into its Neuroscience & Mental Health research programme."
    ),
)

print("Wrote ntusg staging files.")
