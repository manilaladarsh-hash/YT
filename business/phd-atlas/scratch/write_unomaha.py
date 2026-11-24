import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
os.environ["ATLAS_OUT"] = "data/staging"

from rec import save_university, save_program

CHECKED = "2026-11-14"
ETS_SUBJECT_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_SUBJECT_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

GA_CAT_URL = "https://catalog.unomaha.edu/graduate/financing-education/graduate-assistantships/"
GA_WEB_URL = "https://www.unomaha.edu/office-of-graduate-studies/prospective-students/affording-your-education.php"

save_university(
    "unomaha",
    "University of Nebraska Omaha",
    "USA",
    "Nebraska",
    "https://www.unomaha.edu/office-of-graduate-studies/admissions/index.php",
    {
        "app_fee": (
            "50 USD",
            "$50.00 (USD) non-refundable online application fee for degree-seeking applicants ($25.00 for currently enrolled UNO students or non-degree/certificate applicants).",
            "Degree-seeking applications: $50.00 (USD)",
            "https://www.unomaha.edu/office-of-graduate-studies/admissions/how-to-apply.php",
        ),
        "fee_waiver": (
            "Limited",
            "Application fee is waived only for U.S. military active duty/guard/reserve/veterans and dependents, McNair scholarship recipients, undergraduate Pell Grant recipients with a current SAR, and AmeriCorps participants/alumni.",
            "The application fee is waived for the following groups: | All U.S. Military Active Duty, Guard, Reserve, Veterans, and dependents with proof of military status. | McNair scholarship recipients | Undergraduate Pell Grant recipients who provide their current Student Aid Report (SAR) | AmeriCorps with Certification of Service Letter",
            "https://www.unomaha.edu/office-of-graduate-studies/admissions/how-to-apply.php",
            {
                "also": [
                    {
                        "quote": "A non-refundable application fee is required for all applications. | The application fee will be waived for: | McNair Scholars who provide the McNair Certification of Participation form | Undergraduate Pell Grant recipients who provide their current Student Aid Report (SAR)",
                        "url": "https://catalog.unomaha.edu/graduate/admission/",
                    }
                ]
            },
        ),
        "gre_general": (
            "Not stated",
            "UNO Office of Graduate Studies states that some programs require aptitude or advanced knowledge tests (set per program: Required in Computing & Information Science and Biomedical Informatics, Optional in Psychology, and Not required in Biomechanics & Kinesiology).",
            "",
            "https://www.unomaha.edu/office-of-graduate-studies/admissions/entrance-exams.php",
        ),
        "toefl_min": (
            "4 (new scale)",
            "Graduate Council minimum is 80 iBT (total score of 4 on the updated TOEFL scoring scale effective January 21, 2026; institution code 6420; Computing & Information Science and Biomedical Informatics require 90 iBT).",
            "80 internet-based (iBT) TOEFL (total score of 4 on the updated scoring scale effective January 21, 2026)",
            "https://www.unomaha.edu/office-of-graduate-studies/admissions/entrance-exams.php",
        ),
        "ielts_min": (
            "6.5",
            "Graduate Council minimum is IELTS 6.5 (Computing & Information Science and Biomedical Informatics require IELTS 7.0; UNO also accepts Duolingo 110 or PTE 53 centrally).",
            "6.5 IELTS",
            "https://www.unomaha.edu/office-of-graduate-studies/admissions/entrance-exams.php",
        ),
        "english_waiver": (
            "No",
            "Required unless the applicant holds a baccalaureate or advanced degree from a U.S. institution or a country on UNO's predetermined waiver list (India is excluded; an English-medium Indian degree is not exempt).",
            "All graduate applicants whose language of nurture is not English must present an English language proficiency score | Automatic waivers from this policy are granted for individuals who have received a baccalaureate or other advanced degree from an institution in the United States OR for individuals who have received (or will be receiving) a baccalaureate or other advanced degree from a pre-determined country on the following list",
            "https://www.unomaha.edu/office-of-graduate-studies/admissions/entrance-exams.php",
            {
                "also": [
                    {
                        "quote": "All applicants to Graduate Studies at UNO whose language of nurture is not English must present a score on the Test of English as a Foreign Language (TOEFL), the International English Language Testing System (IELTS), the Pearson Test of English (PTE), or Duolingo.",
                        "url": "https://catalog.unomaha.edu/graduate/admission/",
                    }
                ]
            },
        ),
    },
    notes=(
        "University of Nebraska Omaha (UNO) offers 4 STEM Ph.D. programs across 5 Atlas fields: "
        "cs (Computing & Information Science Ph.D., also covering datasci via the Artificial Intelligence Concentration), "
        "biomed (Biomedical Informatics Ph.D., joint with UNMC), "
        "bme (Biomechanics & Kinesiology Ph.D., STEM-designated CIP), and "
        "neuro (Psychology Ph.D. — Neuroscience and Behavior Concentration). "
        "Excluded non-STEM Ph.D. programs: Criminology and Criminal Justice, Gerontology, Public Administration, and the Developmental and Industrial/Organizational concentrations of Psychology Ph.D."
    ),
    checked=CHECKED,
)

# 1. Computing & Information Science, Ph.D. (cs + datasci)
cs_url = "https://catalog.unomaha.edu/graduate/degree-programs-certificates-minors/information-technology/information-technology-phd/"
cs_web = "https://www.unomaha.edu/college-of-information-science-and-technology/academics/computing_and_information_science_phd.php"
save_program(
    "unomaha",
    "cs",
    "College of Information Science & Technology",
    cs_url,
    {
        "deadline": (
            "2027-02-01",
            "Fall 2027 priority deadline is February 1 for applicants seeking funding (April 1 for all other Fall applicants; Spring 2027 deadline September 15).",
            "Fall 2027: Applicants seeking funding February 1, all other applicants April 1",
            cs_url,
            {"time_sensitive": "2027-02-01"},
        ),
        "gre_general": (
            "Required",
            "GRE General is required for most applicants (typical competitive scores 150V / 160Q); automatically waived for a U.S. computing M.S. with GPA >= 3.3, and waiver petitions are accepted >= 1 month before deadline for U.S. computing B.S. >= 3.6 GPA, 5+ years U.S. IT experience, or peer-reviewed computing publications.",
            "Graduate Record Examination (GRE) scores are required for most applicants but are only one component of a holistic admission decision.",
            cs_url,
        ),
        "gre_subject": (
            "No subject test",
            "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (none in Computer Science or Data Science).",
            ETS_SUBJECT_QUOTE,
            ETS_SUBJECT_URL,
        ),
        "toefl_min": (
            "90",
            "Program requires internet-based TOEFL 90 (above Graduate Council's 80 / 4.0 new-scale minimum).",
            "Internet-based TOEFL: 90, IELTS: 7.0, PTE: 61, Duolingo: 120",
            cs_url,
        ),
        "ielts_min": (
            "7.0",
            "Program requires IELTS 7.0 (above Graduate Council's 6.5 minimum).",
            "Internet-based TOEFL: 90, IELTS: 7.0, PTE: 61, Duolingo: 120",
            cs_url,
        ),
        "supervisor": (
            "Recommended",
            "Applicants are advised to identify matching faculty in their statement of purpose and reach out via email to faculty prior to applying.",
            "identify specific research areas that interest you in your statement of purpose, and explicitly mention faculty names with whom you see a good match. Feel free to reach out via email to our faculty prior to submitting your application to discuss your interest.",
            cs_url,
        ),
        "funding": (
            "Competitive",
            "Competitive Graduate Assistantships (20 hrs/week, monthly salary, tuition waiver up to 12 credits/semester, subsidized health insurance, capped at 6 semesters beyond a master's) and doctoral fellowships (separate fellowship interest letter; Feb 1 funding deadline).",
            "If you are interested in applying for a doctoral fellowship, please submit a letter stating your interest in the fellowship | Fall 2027: Applicants seeking funding February 1",
            cs_url,
            {
                "also": [
                    {
                        "quote": "As a graduate assistant you will be considered a UNO employee with a tuition waiver, monthly salary, and subsidized health insurance. | doctoral students are limited to six (6) semesters beyond their master's degree.",
                        "url": GA_CAT_URL,
                    },
                    {
                        "quote": "Partner with faculty on funded research projects | Gain experience through research assistantships",
                        "url": cs_web,
                    },
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Applicants with an earned bachelor's or master's degree in a computing discipline may apply directly to the 90-credit Ph.D.; up to 24 foundation credits may transfer from a prior computing master's degree.",
            "Applicants with an earned undergraduate or graduate degree in a computing discipline (e.g., computer science, management information systems, bioinformatics, cybersecurity or a closely related discipline) can apply for admission to the PhD program. | Credit for graduate computing-related coursework in a prior degree may only be used to satisfy foundation course hours in the plan of study.",
            cs_url,
        ),
    },
    also_fields=["datasci"],
    name="Computing & Information Science, Ph.D.",
    notes=(
        "STEM-OPT eligible Ph.D. in Computing & Information Science covering core computer science, cybersecurity, data analytics, and the Artificial Intelligence Concentration (also mapped to datasci), plus Computing Systems, Human-Centered Computing, and IT Project Management concentrations. "
        "Requires 90 graduate credits, statement of purpose (max 2 pages), CV, 2 letters of recommendation (3rd optional), and GRE waiver requests at least 1 month before the deadline."
    ),
    checked=CHECKED,
)

# 2. Biomedical Informatics, Ph.D. (biomed)
bmi_url = "https://catalog.unomaha.edu/graduate/degree-programs-certificates-minors/biomedical-informatics/biomedical-informatics-phd/"
bmi_faq = "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/prospective-students/frequently-asked-questions.php"
bmi_adm = "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/prospective-students/index.php"
bmi_dl = "https://www.unomaha.edu/college-of-information-science-and-technology/phd-biomedical-informatics/prospective-students/deadlines-and-forms.php"
save_program(
    "unomaha",
    "biomed",
    "School of Interdisciplinary Informatics",
    bmi_url,
    {
        "deadline": (
            "2027-07-01",
            "Fall 2027 application deadline is July 1 (Spring 2027 December 1; Summer 2027 April 1).",
            "Fall 2027: July 1",
            bmi_url,
            {
                "time_sensitive": "2027-07-01",
                "also": [
                    {
                        "quote": "Fall Term – July 1",
                        "url": bmi_dl,
                    }
                ],
            },
        ),
        "gre_general": (
            "Required",
            "All Ph.D. applicants must submit a valid GRE (or GMAT) score regardless of assistantship interest (minimum target 310/336 GRE or >80th percentile GMAT, though Doctoral Program Committee may grant individual waivers).",
            "All applicants to the Ph.D. program are required to have a valid GRE/GMAT score, irrespective of whether they are applying for an assistantship or not.",
            bmi_faq,
            {
                "also": [
                    {
                        "quote": "Applicants must score 310 out of 336 on the Graduate Record Exam (GRE) or above the 80th percentile on the Graduate Management Admission Test (GMAT).",
                        "url": bmi_adm,
                    },
                    {
                        "quote": "GRE requirement may be waived for students on an individual basis based on a review by the Doctoral Program Committee.",
                        "url": bmi_url,
                    },
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (none in Biomedical Informatics).",
            ETS_SUBJECT_QUOTE,
            ETS_SUBJECT_URL,
        ),
        "toefl_min": (
            "90",
            "Program requires internet-based TOEFL 90 (above Graduate Council's 80 / 4.0 new-scale minimum).",
            "Internet-based TOEFL: 90, IELTS: 7.0, PTE: 64, Duolingo: 120",
            bmi_url,
        ),
        "ielts_min": (
            "7.0",
            "Program requires IELTS 7.0 (above Graduate Council's 6.5 minimum).",
            "Internet-based TOEFL: 90, IELTS: 7.0, PTE: 64, Duolingo: 120",
            bmi_url,
        ),
        "supervisor": (
            "Not stated",
            "Applications are evaluated by the Doctoral Program Committee with attention to research alignment with IS&T faculty; no pre-application advisor confirmation is stated.",
            "",
            bmi_url,
        ),
        "funding": (
            "Competitive",
            "Competitive UNO Graduate Assistantships (20 hrs/week, monthly salary, tuition remission up to 12 credits/semester, subsidized health insurance; limited to 6 semesters beyond a master's; selected individually by departments).",
            "As a graduate assistant you will be considered a UNO employee with a tuition waiver, monthly salary, and subsidized health insurance. | doctoral students are limited to six (6) semesters beyond their master's degree.",
            GA_CAT_URL,
            {
                "also": [
                    {
                        "quote": "GAs are selected by each department individually, so please contact your department's office to apply.",
                        "url": GA_WEB_URL,
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "Requires a baccalaureate degree (3.5+ GPA recommended) with preference given to applicants holding a related master's or doctoral degree; 90 credits beyond the bachelor's with up to 24 prior graduate credits transferable.",
            "successfully completed a baccalaureate degree from an accredited institution: preference will be given to students with a master's or doctoral degree from a related field. | A maximum of 24 credit hours of graduate coursework can be transferred from courses taken in a graduate program prior to admission into the PhD in BMI.",
            bmi_url,
        ),
    },
    name="Biomedical Informatics, Ph.D.",
    notes=(
        "Joint doctoral program offered by UNO and the University of Nebraska Medical Center (UNMC). Requires 3 letters of recommendation, CV, 2-page statement of purpose, and a writing sample/research portfolio; admission statement notes PTE 61 vs Catalog PTE 64 (Catalog used)."
    ),
    checked=CHECKED,
)

# 3. Biomechanics and Kinesiology, Ph.D. (bme)
bme_url = "https://catalog.unomaha.edu/graduate/degree-programs-certificates-minors/exercise-science/"
bme_web = "https://www.unomaha.edu/college-of-education-health-and-human-sciences/biomechanics-core-facility/academic-programs/graduate-programs.php"
bme_ra = "https://www.unomaha.edu/college-of-education-health-and-human-sciences/health-kinesiology/phd/doctoral-research-assistant.php"
save_program(
    "unomaha",
    "bme",
    "Department of Biomechanics / School of Health and Kinesiology",
    bme_url,
    {
        "deadline": (
            "Rolling",
            "Applications are accepted on a rolling basis for Spring, Summer, and Fall 2027; January 31 is the priority deadline for full departmental assistantship consideration.",
            "Spring 2027, Summer 2027, and Fall 2027: Applications for this program are accepted on a rolling basis. All materials must be submitted prior to the beginning of the semester in which the student has elected to begin coursework. To receive full consideration for departmental assistantships, applications must be received by January 31st.",
            bme_url,
            {"time_sensitive": "2027-01-31"},
        ),
        "gre_general": (
            "Not required",
            "The GRE is no longer required for admission to the Ph.D. in Biomechanics and Kinesiology.",
            "The GRE is no longer a requirement for admission.",
            bme_web,
        ),
        "gre_subject": (
            "No subject test",
            "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (none in Biomechanics or Biomedical Engineering).",
            ETS_SUBJECT_QUOTE,
            ETS_SUBJECT_URL,
        ),
        "supervisor": (
            "Required",
            "Applicants must contact a potential faculty advisor prior to applying and confirm mentorship and advisor willingness prior to admission.",
            "Preliminary contact is made with a potential advisor prior to applying to the program. Prior to being admitted, a student must confirm mentorship with an advisor based on mutual interests and willingness of the advisor to take on the student.",
            bme_url,
        ),
        "funding": (
            "Competitive",
            "Competitive doctoral research assistantships (paid at the typical NIH standard, dependent on available faculty/grant funding; UNO GAs provide tuition waiver and subsidized health insurance; January 31 priority deadline).",
            "The availability of doctoral research assistants is largely determined by available funding to support the position. | Research assistants are typically paid the National Institutes of Health standard.",
            bme_ra,
            {
                "also": [
                    {
                        "quote": "To receive full consideration for departmental assistantships, applications must be received by January 31st.",
                        "url": bme_url,
                    },
                    {
                        "quote": "As a graduate assistant you will be considered a UNO employee with a tuition waiver, monthly salary, and subsidized health insurance.",
                        "url": GA_CAT_URL,
                    },
                ]
            },
        ),
        "entry_route": (
            "Master's usually required",
            "Requires a master's degree or at least 30 graduate credit hours in a related field with a minimum 3.2 graduate GPA (60-credit post-master's Ph.D.).",
            "Master’s degree, or minimum of 30 graduate hours in a related field, e.g., health, physical therapy",
            bme_url,
        ),
    },
    name="Biomechanics and Kinesiology, Ph.D.",
    notes=(
        "Joint Ph.D. between the Department of Biomechanics and the School of Health and Kinesiology; holds a STEM-designated CIP code. "
        "Offers concentrations in Biomechanics (Movement Biomechanics and Cardiovascular Biomechanics), Physiology of Exercise, Motor Development and Control, and Physical Activity. Requires 3 letters of recommendation, 500-word statement of purpose, CV, and writing sample."
    ),
    checked=CHECKED,
)

# 4. Psychology, Ph.D. — Neuroscience and Behavior Concentration (neuro)
psy_url = "https://catalog.unomaha.edu/graduate/degree-programs-certificates-minors/psychology/psychology-phd/"
neuro_idx = "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/neuroscience/index.php"
neuro_req = "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/neuroscience/neurorequire.php"
neuro_phd = "https://www.unomaha.edu/college-of-arts-and-sciences/psychology/academics/graduate-programs/neuroscience/neuro-phd.php"
save_program(
    "unomaha",
    "neuro",
    "Department of Psychology",
    psy_url,
    {
        "deadline": (
            "2027-01-10",
            "Fall 2027 admission deadline is January 10.",
            "Fall 2027: January 10",
            psy_url,
            {
                "time_sensitive": "2027-01-10",
                "also": [
                    {
                        "quote": "Application Deadline: January 10th",
                        "url": neuro_idx,
                    }
                ],
            },
        ),
        "gre_general": (
            "Optional",
            "GRE General scores are optional; all applications are reviewed whether or not GRE scores are submitted.",
            "GRE scores are OPTIONAL for those applying to the PhD Program. All applications will be reviewed whether or not GRE scores are included.",
            psy_url,
            {
                "also": [
                    {
                        "quote": "the reporting of GRE scores is OPTIONAL for those applying to the program. All applications will be reviewed whether or not GRE scores are included.",
                        "url": neuro_req,
                    }
                ]
            },
        ),
        "gre_subject": (
            "Not required",
            "The GRE Psychology Subject Test is not required.",
            "The psychology subject test is not required.",
            neuro_req,
        ),
        "supervisor": (
            "Not stated",
            "Neither the Graduate Catalog nor the Neuroscience & Behavior application pages state whether pre-admission faculty supervisor contact or confirmation is required.",
            "",
            psy_url,
        ),
        "funding": (
            "Competitive",
            "Competitive UNO Graduate Assistantships (20 hrs/week, monthly salary, tuition waiver up to 12 credits/semester, subsidized health insurance; limited to 6 semesters beyond a master's).",
            "As a graduate assistant you will be considered a UNO employee with a tuition waiver, monthly salary, and subsidized health insurance. | doctoral students are limited to six (6) semesters beyond their master's degree.",
            GA_CAT_URL,
            {
                "also": [
                    {
                        "quote": "GAs are selected by each department individually, so please contact your department's office to apply.",
                        "url": GA_WEB_URL,
                    }
                ]
            },
        ),
        "entry_route": (
            "Either",
            "90-credit doctoral track accommodating applicants entering directly with a bachelor's degree (earning an M.A. en route at UNO before advancing to candidacy in Year 4–5) or entering with a prior master's degree (30–45 credits transferred).",
            "Credit from Masters (30-45 hrs); 4 field-related courses; 1 other (ROTT); Dissertations hours | Students earnings a MA at UNO, this would be the end of your 4th year or beginning of 5th; Students arriving with a master's earned elsewhere, this would be by the end of your 3rd year",
            neuro_phd,
            {
                "also": [
                    {
                        "quote": "Minimum GPA of at least 3.0 in undergraduate courses related to proposed major",
                        "url": neuro_req,
                    }
                ]
            },
        ),
    },
    name="Psychology, Ph.D. (Neuroscience and Behavior)",
    notes=(
        "Neuroscience and Behavior Concentration within UNO's 90-credit Psychology Ph.D. (in collaboration with UNMC, Boys Town National Research Hospital, and Henry Doorly Zoo). "
        "Requires 3 letters of recommendation, statement of purpose, writing sample (APA style preferred), and CV/resume. UNO Psychology Ph.D. also offers Developmental Psychology and Industrial/Organizational Psychology concentrations (excluded as non-STEM/applied)."
    ),
    checked=CHECKED,
)
print("Wrote unomaha staging records.")
