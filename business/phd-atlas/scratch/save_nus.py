import os
import sys

os.environ["ATLAS_OUT"] = "data/staging"
sys.path.insert(0, "scripts")
from rec import save_university, save_program

TODAY = "2026-11-14"
ETS_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

STAT_PROSP = "https://www.stat.nus.edu.sg/education/graduate/phd-in-statistics-and-data-science/prospective-students/"
CS_MAIN = "https://www.comp.nus.edu.sg/programmes/pg/phdcs/"
CS_ADM = "https://www.comp.nus.edu.sg/programmes/pg/phdcs/admissions/"
CS_APP = "https://www.comp.nus.edu.sg/programmes/pg/phdcs/application/"
CS_SCHOL = "https://www.comp.nus.edu.sg/programmes/pg/phdcs/scholarships/"
CS_GRAD = "https://www.comp.nus.edu.sg/graduate/"
CHEM_PHD = "https://chemistry.nus.edu.sg/education/graduate/phd-programme/"
MATH_MAIN = "https://www.math.nus.edu.sg/pg/phd/"
MATH_PROSP = "https://www.math.nus.edu.sg/pg/phd/phd-prospective/"
DBS_PHD = "https://www.dbs.nus.edu.sg/education/graduates/doctor-of-philosophy/"

save_university(
    "nus",
    "National University of Singapore",
    "Singapore",
    "Singapore",
    "https://nusgs.nus.edu.sg/admissions/",
    {
        "app_fee": (
            "Not stated",
            "Central NUS Graduate School (nusgs.nus.edu.sg) and Faculty of Science pages are blocked by Imperva/Incapsula WAF; individual schools/departments state fees (e.g., S$50 in School of Computing).",
            "",
            CS_APP,
        ),
        "fee_waiver": (
            "Not stated",
            "Accessible NUS doctoral admissions pages do not state an international application fee waiver policy (nusgs.nus.edu.sg blocked by Imperva/Incapsula).",
            "",
            CS_APP,
        ),
        "gre_general": (
            "Not stated",
            "GRE requirements are set by each faculty and department (optional in School of Computing and Statistics; strongly encouraged in Chemistry and Mathematics).",
            "",
            CS_ADM,
        ),
        "toefl_min": (
            "85",
            "University-wide baseline minimum for NUS is TOEFL iBT 85 (several faculties set higher requirements, such as 90 in Computing and 95 / 5 on the new scale in Chemistry).",
            "the minimum TOEFL score ranges for NUS: | Internet-Based (iBT): 85",
            STAT_PROSP,
        ),
        "ielts_min": (
            "6",
            "University-wide baseline minimum for NUS is IELTS 6.0 (some departments set higher requirements, such as 7.0 in Chemistry).",
            "the minimum TOEFL score ranges for NUS: | For IELTS, the score should be 6 and above.",
            STAT_PROSP,
        ),
        "english_waiver": (
            "Conditional",
            "Applicants whose medium of undergraduate instruction was English may be exempt from TOEFL/IELTS depending on faculty verification; otherwise an approved test score is required.",
            "* The following guidelines are provided for applicants whose native language or medium of undergraduate instruction is not English",
            STAT_PROSP,
            {
                "also": [
                    {
                        "quote": "*International applicants who graduated from universities where English is not the main medium of communication must submit TOEFL (http://www.ets.org/) or IELTS (International English Language Testing System) (http://www.ielts.org) scores.",
                        "url": CS_ADM,
                    },
                    {
                        "quote": "a candidate whose medium of undergraduate instruction is not English is required to submit TOEFL (with the minimum score 95 (old scale) or 5 (new scale) for the internet-based test) or IELTS (with the minimum score 7.0) scores.",
                        "url": CHEM_PHD,
                    },
                ]
            },
        ),
    },
    notes="Five Faculty of Science / School of Computing PhD programmes verified from accessible official NUS department pages (cs, chemistry, statistics [+datasci], math, biology). Imperva/Incapsula WAF blocked automated fetching of nusgs.nus.edu.sg, science.nus.edu.sg, cde.nus.edu.sg (engineering PhDs: bme, chemeng, civil, ece, materials, mech), medicine.nus.edu.sg (biomed, neuro), fass.nus.edu.sg/geog/ (earth, environment), and collapsed accordions on physics.nus.edu.sg.",
    checked=TODAY,
)

save_program(
    "nus",
    "cs",
    "School of Computing — Department of Computer Science",
    CS_MAIN,
    {
        "deadline": (
            "2026-12-15",
            "August 2027 intake deadline is December 15, 2026 (January intake deadline is June 15 of the previous calendar year).",
            "August Intake: 15 December | January Intake: 15 June (of previous calendar year)",
            CS_APP,
            {
                "also": [
                    {
                        "quote": "PhD Intake: | Now – 15 December 2026",
                        "url": CS_GRAD,
                    }
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for computer science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Not stated",
            "School of Computing PhD admissions and application pages do not state whether pre-admission supervisor commitment is required.",
            "",
            CS_ADM,
        ),
        "funding": (
            "Competitive",
            "NUS Research Scholarships (monthly emoluments plus full tuition fee subsidy, plus an additional S$500/month for two years after passing the PhD Qualifying Examination) and President's Graduate Fellowships are awarded competitively for up to 4 years.",
            "Financial Assistance in the form of Research Scholarship is available, on a competitive-basis to all full-time students who meet the minimum criteria. The Research Scholarship will carry monthly emoluments, plus full tuition fee subsidy.",
            CS_SCHOL,
        ),
        "entry_route": (
            "Either",
            "Admits candidates with a good relevant bachelor's degree (at least 2nd Class Upper Honours or equivalent for Research Scholarships) or master's degree in computing or a related discipline.",
            "The normal minimum entry qualifications for admission to the programme by research are a good relevant bachelor’s degree/master’s degree. Candidates applying for Research Scholarships must have obtained a bachelor’s degree with at least a 2nd Class Upper Honours, or its equivalent in Computing or related discipline.",
            CS_ADM,
        ),
        "app_fee": (
            "50 SGD",
            "School of Computing charges a S$50 non-refundable online application fee (inclusive of GST) per PhD application.",
            "A S$50 non-refundable application fee (per online application & inclusive of prevailing GST) is payable for our PhD programme.",
            CS_APP,
        ),
        "gre_general": (
            "Optional",
            "GRE is not required, though applicants are encouraged to submit scores (Indian university graduates may submit GATE scores instead).",
            "GRE is not required, but applicants are encouraged to submit their GRE scores. Candidates who have graduated from Indian universities may submit GATE scores instead.",
            CS_ADM,
        ),
        "toefl_min": (
            "90",
            "School of Computing requires a minimum TOEFL iBT score of 90 (or IELTS 6.0) when English proficiency testing is required.",
            "The minimum TOEFL scores for Internet Based Test (IBT) is 90; or IELTS score of 6.0.",
            CS_ADM,
        ),
        "ielts_min": (
            "6.0",
            "School of Computing requires a minimum IELTS score of 6.0 (or TOEFL iBT 90) when English proficiency testing is required.",
            "The minimum TOEFL scores for Internet Based Test (IBT) is 90; or IELTS score of 6.0.",
            CS_ADM,
        ),
        "english_waiver": (
            "Conditional",
            "International applicants who graduated from universities where English was the main medium of communication are exempt from submitting TOEFL/IELTS scores.",
            "*International applicants who graduated from universities where English is not the main medium of communication must submit TOEFL (http://www.ets.org/) or IELTS (International English Language Testing System) (http://www.ielts.org) scores.",
            CS_ADM,
        ),
    },
    notes="School of Computing also offers a separate PhD in Information Systems (https://www.comp.nus.edu.sg/programmes/pg/phdis/) with the same admissions, TOEFL/IELTS, and GRE/GATE rules.",
    checked=TODAY,
)

save_program(
    "nus",
    "chemistry",
    "Faculty of Science — Department of Chemistry",
    CHEM_PHD,
    {
        "deadline": (
            "2026-11-15",
            "August intake application window runs from May 16 to November 15 of the previous year (January intake closes May 15 of the previous year).",
            "For August intake: 16 May to 15 November (of the previous year)",
            CHEM_PHD,
            {"inferred": "year"},
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for chemistry (ETS discontinued the Chemistry Subject Test in May 2023).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Recommended",
            "Applicants choose up to 3 proposed PhD supervisors from the Chemistry Faculty / Jointly Appointed Faculty list (and contact proposed supervisors for grant-funded scholarships).",
            "Please choose up to 3 proposed PhD supervisors from the “Faculty” and “Jointly Appointed Faculty” sections only",
            CHEM_PHD,
            {
                "also": [
                    {
                        "quote": "PhD Scholarship under research grant (contact the proposed supervisor)",
                        "url": CHEM_PHD,
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            "Competitive scholarships include NUS Research Scholarship, President's Graduate Fellowship, and the Faculty of Science Dean Graduate Fellowship (top 20% of scholarship holders, adding S$600/month to stipends of S$2,800/month for international students).",
            "PhD Scholarships in Department of Chemistry | NUS Research Scholarship | President’s Graduate Fellowship (PGF) | Dean Graduate Fellowship (DGF) | Selected from those with RSB, SINGA, IRP in admission per AY (top 20%) | Stipends in years 1-4, increase by 600 S$ per month | SC: S$3,400 +CPF 578; SPR: S$3,000; IS: S$2,800",
            CHEM_PHD,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Requires a 4-year bachelor's or Honours degree (at least 2nd Class Upper Honours or equivalent for Research Scholarship applicants).",
            "A Bachelor’s (Honours) degree or a 4-year Bachelor’s degree | Candidates applying for Research Scholarships must have obtained a bachelor’s degree with at least a 2nd Class Upper Honours, or its equivalent.",
            CHEM_PHD,
        ),
        "gre_general": (
            "Recommended",
            "Chemistry strongly encourages all PhD candidates to submit GRE scores (minimum 320 Verbal + Quantitative and 3.5 Analytical Writing).",
            "For all PhD programmes, candidates are strongly encouraged to submit GRE (minimum score of 320 [Verbal+ Quantitative] and 3.5 [Analytical Writing]).",
            CHEM_PHD,
        ),
        "toefl_min": (
            "5 (new scale)",
            "Chemistry requires TOEFL iBT 5 on the new scale (95 on the old scale) or IELTS 7.0 if undergraduate instruction was not in English.",
            "a candidate whose medium of undergraduate instruction is not English is required to submit TOEFL (with the minimum score 95 (old scale) or 5 (new scale) for the internet-based test) or IELTS (with the minimum score 7.0) scores.",
            CHEM_PHD,
        ),
        "ielts_min": (
            "7.0",
            "Chemistry requires IELTS 7.0 overall (or TOEFL iBT 95 old / 5 new scale) if undergraduate instruction was not in English.",
            "a candidate whose medium of undergraduate instruction is not English is required to submit TOEFL (with the minimum score 95 (old scale) or 5 (new scale) for the internet-based test) or IELTS (with the minimum score 7.0) scores.",
            CHEM_PHD,
        ),
    },
    notes="Department-specific higher English thresholds (TOEFL 95 old / 5 new, IELTS 7.0) and GRE recommendation override NUS baseline.",
    checked=TODAY,
)

save_program(
    "nus",
    "statistics",
    "Faculty of Science — Department of Statistics and Data Science",
    STAT_PROSP,
    {
        "deadline": (
            "2026-11-15",
            "Semester 1 (August) intake deadline is November 15 of the previous year (Semester 2 January intake deadline is May 15 of the previous year).",
            "Semester 1 (August) | 15 November of the previous year",
            STAT_PROSP,
            {"inferred": "year"},
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists specifically for statistics/data science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Not stated",
            "The PhD in Statistics and Data Science prospective students page does not state whether pre-admission supervisor confirmation is required.",
            "",
            STAT_PROSP,
        ),
        "funding": (
            "Competitive",
            "Priority for the NUS Research Scholarship (including full tuition fee subsidy and monthly stipend, plus departmental top-ups) is given to PhD applicants.",
            "Priority for NUS Research Scholarship will be given to PhD applicants. | The scholarship includes a full tuition fee subsidy, which is in the form of credit towards student’s fee bill when the fee is due. | In addition, our department provides additional top-ups to the scholars.",
            STAT_PROSP,
        ),
        "entry_route": (
            "Either",
            "Requires a good GPA in a relevant bachelor's or master's degree (upper second class Honours or higher in Mathematics/Statistics or equivalent).",
            "A good GPA in a relevant bachelor’s or master’s degree. (Applicants should have an upper second class Honours degree or higher in Mathematics /Statistics or equivalent qualifications and the ability to pursue research in Statistics/Probability.)",
            STAT_PROSP,
        ),
        "gre_general": (
            "Optional",
            "GRE scores are optional, though strong GRE scores (minimum 320 V+Q and 3.5 AW guideline) significantly strengthen the application.",
            "Standardized test scores such as the GRE. | Items (5) to (7) are optional; however, do note that evidence of strong quantitative, verbal, and analytical skills through GRE scores, as well as indicators of research skills and experience will significantly strengthen your application.",
            STAT_PROSP,
        ),
    },
    also_fields=["datasci"],
    notes="Covers PhD in Statistics and Data Science (covers both statistics and data science).",
    checked=TODAY,
)

save_program(
    "nus",
    "math",
    "Faculty of Science — Department of Mathematics",
    MATH_PROSP,
    {
        "deadline": (
            "Not stated",
            "Application deadlines are not exposed on the accessible Mathematics page (science.nus.edu.sg FAQ blocked by Imperva/Incapsula and accordion sections collapsed).",
            "",
            MATH_PROSP,
        ),
        "gre_subject": (
            "Not stated",
            "Mathematics encourages GRE scores generally without specifying whether the GRE Mathematics Subject Test is required.",
            "",
            MATH_PROSP,
        ),
        "supervisor": (
            "Not stated",
            "The prospective PhD in Mathematics page does not state whether pre-admission supervisor agreement is required.",
            "",
            MATH_PROSP,
        ),
        "funding": (
            "Typical",
            "Admission is competitive with scholarship eligibility; the majority of current full-time graduate students receive some form of financial support.",
            "Admission is on a competitive basis and eligible applicants may apply for Scholarship or other forms of financial assistance when applying for admission. Majority of the Department’s current full-time graduate students are given some form of financial support.",
            MATH_MAIN,
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Applicants must hold at least an Honours degree or equivalent from a reputable university.",
            "Applicants must have at least an Honours degree or its equivalent from a reputable university.",
            MATH_PROSP,
        ),
        "gre_general": (
            "Recommended",
            "Standardised GRE scores are strongly encouraged and will significantly strengthen the application.",
            "Standardised scores of TOEFL/IELTS & GRE will significantly strengthen the application to the university and strongly encouraged.",
            MATH_PROSP,
        ),
    },
    notes="Department page has collapsed accordions for Fees & Scholarships and Application Procedure; FAQ link points to science.nus.edu.sg (WAF-blocked).",
    checked=TODAY,
)

save_program(
    "nus",
    "biology",
    "Faculty of Science — Department of Biological Sciences",
    DBS_PHD,
    {
        "deadline": (
            "Rolling",
            "Department of Biological Sciences PhD admissions are open year-round.",
            "Application for admissions are open all year round so come be a part of our community today!",
            DBS_PHD,
        ),
        "gre_subject": (
            "No subject test",
            "No ETS GRE Subject Test exists for biology (ETS discontinued the Biology Subject Test in May 2021).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Not stated",
            "The Department of Biological Sciences PhD page lists a Laboratory Rotation Programme accordion whose details were collapsed in automated rendering, and science.nus.edu.sg FAQ is WAF-blocked.",
            "",
            DBS_PHD,
        ),
        "funding": (
            "Not stated",
            "Scholarship and stipend details on the Biological Sciences PhD page were collapsed in automated rendering and nusgs.nus.edu.sg/scholarships/ is WAF-blocked.",
            "",
            DBS_PHD,
        ),
        "entry_route": (
            "Not stated",
            "Admission criteria on the Biological Sciences PhD page were collapsed in automated rendering and science.nus.edu.sg is WAF-blocked.",
            "",
            DBS_PHD,
        ),
    },
    notes="Page accordions for Admission Criteria, Scholarships, and Laboratory Rotation Programme did not expand under headless Chromium.",
    checked=TODAY,
)

print("Saved nus and 5 programs to data/staging/")
