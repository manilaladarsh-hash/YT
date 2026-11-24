import os
import sys

os.environ["ATLAS_OUT"] = "data/staging"
sys.path.insert(0, "scripts")
from rec import save_university, save_program

UID = "uccs"
CHECKED = "2026-11-14"

GS_ADM = "https://graduateschool.uccs.edu/admissions"
GS_ENG = "https://graduateschool.uccs.edu/english-proficiency-requirements"
GS_ACAD = "https://graduateschool.uccs.edu/academics"
GS_FELL = "https://graduateschool.uccs.edu/fellowships-scholarships"
GS_POL = "https://graduateschool.uccs.edu/current-student-resources/policies-procedures"
UCCS_GRAD_DET = "https://www.uccs.edu/admissions-aid/application-details/graduate"
UCCS_INTL = "https://www.uccs.edu/admissions-aid/application-details/international"
ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"

CS_PAGE = "https://eas.uccs.edu/academics/programs/computer-science-phd"
CS_GRAD_REQ = "https://eas.uccs.edu/graduate-programs/computer-science-phd/graduation-requirements"
SEC_PAGE = "https://eas.uccs.edu/academics/programs/security-phd"
ECE_PAGE = "https://eas.uccs.edu/academics/programs/engineering-concentration-in-electrical-engineering-phd"
ECE_GRAD_REQ = "https://eas.uccs.edu/graduate-programs/electrical-engineering-phd/graduation-requirements"
MAE_APP = "https://eas.uccs.edu/mae/graduate/application"
MAE_PHD = "https://eas.uccs.edu/graduate-programs/mechanical-engineering-phd"
EAS_APPLY = "https://eas.uccs.edu/future-student-resources/how-to-apply"

MATH_PHD = "https://math.uccs.edu/academics/phd"
MATH_GRAD = "https://math.uccs.edu/academics/graduate"
MATH_FORMS = "https://math.uccs.edu/graduate-requirements/applications-forms"
MATH_GTF = "https://math.uccs.edu/graduate-requirements/graduate-teaching-fellowships"
MATH_ENG = "https://math.uccs.edu/graduate-requirements/english-proficiency-requirements"

PHYS_PHD = "https://physics.uccs.edu/academics/phd"
PHYS_HB = "https://physics.uccs.edu/sites/default/files/inline-files/UCCS_PhD_Physics_Handbook-August2023.pdf"

save_university(
    UID,
    "University of Colorado Colorado Springs",
    "USA",
    "Colorado",
    GS_ADM,
    {
        "app_fee": (
            "60 USD",
            "Non-refundable $60 application fee for both domestic and international graduate applicants (note: a legacy College of Engineering and Applied Science page still lists $100 for international applicants, though current university Admissions and Mathematics pages both state $60).",
            "A $60 non-refundable application fee for domestic students and $60 non-refundable application fee is required for international student applicants.",
            UCCS_GRAD_DET,
            {
                "also": [
                    {
                        "quote": "$60 application fee",
                        "url": GS_ADM,
                    },
                    {
                        "quote": "A $100, non-refundable application fee, paid online or check made payable to UCCS.",
                        "url": EAS_APPLY,
                    },
                ]
            },
        ),
        "fee_waiver": (
            "Limited",
            "UCCS offers fee waivers only via specific scholar programs (including Fulbright Scholar Program, GEM, McNair, MARC, RISE, Gates Millennium, TRIO SSS, U-STAR), financial-need criteria requiring a FAFSA or ETS GRE fee reduction voucher, or U.S. military/veteran status.",
            "UCCS offers three application fee waiver options. | If you were involved in one or more of the following scholar programs, you may be eligible for an application fee waiver: ... Fullbright Scholar Program | If you received a fee reduction voucher from ETS to take the GRE test, you qualify for an application fee waiver.",
            GS_ADM,
        ),
        "gre_general": (
            "Not stated",
            "Set by each graduate program rather than the Graduate School; UCCS institution code is 4874. Engineering (CS, ECE, MAE) and Mathematics Ph.D. programs require GRE General scores for international applicants, while Physics requires the Physics GRE instead. See each program record.",
            "",
            GS_ADM,
        ),
        "toefl_min": (
            "4.5 (new scale)",
            "Graduate School minimum for all covered STEM Ph.D. programs is 4.5 on the TOEFL iBT 1-6 scale effective January 21, 2026 (80 on the legacy 0-120 iBT scale prior to 1/21/2026; scores valid 2 years; Duolingo 115 also accepted). Note: Physics department pages still state 83 iBT (560 PBT).",
            "Tests must have been taken in the last two years. See the Summary of Program Requirements chart below. | Computer Science MS & PhD 80 4.5 6.5 115 | Electrical Engineering MSEE & PhD 80 4.5 6.5 115 | Mathematics: Applied Science PhD 80 4.5 6.5 115 | Mechanical & Aerospace Engineering PhD 80 4.5 6.5 115 | Physics: Applied Science PhD 80 4.5 6.5 115",
            GS_ENG,
        ),
        "ielts_min": (
            "6.5",
            "Graduate School minimum IELTS score for all covered STEM Ph.D. programs is 6.5 (scores must be taken within the last two years; institution code 4874).",
            "Tests must have been taken in the last two years. See the Summary of Program Requirements chart below. | Computer Science MS & PhD 80 4.5 6.5 115 | Physics: Applied Science PhD 80 4.5 6.5 115",
            GS_ENG,
        ),
        "english_waiver": (
            "Conditional",
            "An English-medium degree from India may qualify conditionally at the Graduate School level if the transcript or an official institutional letter states English was the medium of instruction, BUT each academic program chooses which methods to accept (Computer Science and Physics specify US-study waivers only — always confirm with the program; India is not on the citizenship exemption list).",
            "Academic programs use one or more of the following methods for determining English proficiency. **Please contact your program to verify which method(s) they allow.** | You have received or will receive a post-secondary degree where English is the language (medium) of instruction. If the language of instruction is English, but not noted on the transcript, students may be asked to submit an official letter from their post-secondary institution stating that the medium of instruction is English in order to meet the English Language Proficiency requirement.",
            GS_ENG,
            {
                "also": [
                    {
                        "quote": "Each program judges the qualifications of its students in the use of English. The following are options for determining English Proficiency. Departments must use at least one of these options: Postsecondary degree from a US accredited institution or in a program where English is the language of instruction.",
                        "url": GS_POL,
                    }
                ]
            },
        ),
    },
    notes="All UCCS graduate programs reviewed via Graduate School Academics directory: 5 STEM Ph.D. tracks mapped (CS plus companion Cybersecurity PhD, ECE, MAE, Applied Science: Mathematics, Applied Science: Physics). Excluded non-STEM/clinical doctorates: Psychology: Clinical (Geropsychology & Trauma, APA-accredited clinical Ph.D.s), Educational Leadership, Research & Policy Ph.D., Executive DBA, DNP, and DPT; Biology and Chemistry offer master's degrees only. International applicants with foreign post-secondary coursework must submit an official NACES or AICE course-by-course transcript evaluation (UCCS preferred partner IEE offers a $145 discounted 3-day rate). Graduate School funding includes competitive Graduate School PhD Grants (up to $26,000/yr, international eligible), Tuition Matching Grants (up to $8,000/yr with paid GTA/GRA/GPTI appointment), and First-Year Graduate Fellowships ($6,000, Feb 15 program nomination deadline).",
    checked=CHECKED,
)

# 1. Computer Science (+ Cybersecurity)
save_program(
    UID,
    "cs",
    "Department of Computer Science",
    CS_PAGE,
    {
        "deadline": (
            "2027-02-01",
            "Fall 2027 application deadline is February 1, 2027 (Spring 2027: October 1, 2026; Summer starts not accepted). Note: most scholarships and fellowships go to Fall applicants; Graduate School First-Year Fellowship nominations close February 15.",
            "Fall 2027: February 1, 2027 | This program admits students for the Fall and Spring terms. Summer starts are not accepted.",
            GS_ACAD,
            {
                "time_sensitive": "2027-02-15",
                "also": [
                    {
                        "quote": "International students applying for the program should have all application materials into the Admissions Office at UCCS by February 1 for Fall Semester and by October 1 for Spring Semester. | Most scholarships and fellowships are given to Fall applicants, not Spring applicants.",
                        "url": CS_PAGE,
                    }
                ],
            },
        ),
        "gre_general": (
            "Required",
            "All GRE General sections are required for international applicants with at least 148 Quantitative; waived only for U.S. ABET CS bachelor's graduates (>= 3.0 GPA) or U.S. R1/R2 master's graduates (>= 3.0 GPA).",
            "All sections of the Graduate Record Examination (GRE) are required, with at least 148 on the quantitative portion, unless one of the following conditions is satisfied: The applicant has a bachelor’s degree with a GPA of 3.0 or above from an ABET-accredited Computer Science or a closely related program from within the U.S. The applicant has a master’s degree in Computer Science or a closely related field with a GPA of 3.0 or above from an R1 or R2 institution from within the U.S.",
            CS_PAGE,
            {
                "also": [
                    {
                        "quote": "GRE: required, unless completed bachelor's degree with GPA of 3.0 or above from an ABET-accredited Comp Sci program or related program in the U.S. OR a master's degree with GPA of 3.0 or above from an R1 or R2 institution in the U.S.",
                        "url": GS_ACAD,
                    }
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Computer Science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            ETS_SUBJ,
        ),
        "english_waiver": (
            "No",
            "Computer Science specifies English proficiency waivers only for completing a degree in the U.S., so an English-medium degree from India requires TOEFL (80 / 4.5 new scale), IELTS (6.5), or Duolingo (115).",
            "A TOEFL score of 80 of higher, an ILETS of 6.5 or higher, or a Duolingo exam score of 115 will be required for proof of English Proficiency. If the student has completed a degree in the US, this requirement may be waived.",
            CS_PAGE,
        ),
        "supervisor": (
            "Not required",
            "Admission is decided by the PhD committee rather than an individual advisor's prior commitment, and students may begin qualifying exams before selecting an advisor; however, applicants must name 1-3 potential CS faculty advisors and justify fit in their goal/personal statement.",
            "The PhD committee will review all applicants for admission | Complete a personal statement and within that personal statement name a potential advisor and justify your choice.",
            CS_PAGE,
            {
                "also": [
                    {
                        "quote": "The examining committee will be organized by the advisor if identified by the student, or by the program director if the advisor has not been chosen by the student.",
                        "url": CS_GRAD_REQ,
                    },
                    {
                        "quote": "Also include in your goal statement the three faculty member's names that you selected on page 4 and describe why you feel they would be a good fit for you as your advisor.",
                        "url": GS_ACAD,
                    },
                ]
            },
        ),
        "funding": (
            "Competitive",
            "Funding is competitive rather than guaranteed: students can apply directly to the department for RA/TA positions, which can pair with Graduate School Tuition Matching Grants (up to $8,000/yr) or competitive Graduate School PhD Grants (up to $26,000/yr) and First-Year Fellowships ($6,000/yr, mainly Fall admits).",
            "For financial aid consideration, we encourage you to apply as soon as possible. Most scholarships and fellowships are given to Fall applicants, not Spring applicants.",
            CS_PAGE,
            {
                "also": [
                    {
                        "quote": "Research/Teaching Assistantships may be available, and are used for requesting financial assistance from the department - please contact the department directly for the RA/TA application.",
                        "url": EAS_APPLY,
                    },
                    {
                        "quote": "Awards in any amount of up to $26,000 per year, or $13,000 per semester, may be processed by the Office of Financial Aid. | Resident and nonresident graduate students, including international students, are eligible for this grant.",
                        "url": GS_FELL,
                    },
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Admits holders of a bachelor's or master's degree in CS or a closely related field with >= 3.3 GPA and prerequisite math/CS coursework; bachelor's entrants may earn an M.S. along the way to the 60-credit Ph.D.",
            "The student holds a bachelor's degree in computer science or a master's degree in computer science or closely related field from a college or university of recognized standing. A student who is admitted without a master's degree may earn that degree as a part of the Ph.D. studies.",
            CS_PAGE,
        ),
    },
    notes="Covers both Computer Science, Ph.D. and the Department of Computer Science's companion Cybersecurity, Ph.D. (Security, Ph.D.; https://eas.uccs.edu/academics/programs/security-phd), which shares the same February 1 Fall deadline, GRE General (>= 148Q, same U.S. waiver rules), TOEFL 80 / IELTS 6.5 / Duolingo 115 (US-degree waiver), >= 3.3 GPA, 60-credit structure, and BS-or-MS entry route (plus a 3-month operational security internship/publication/CISSP requirement). Graduate School table lists 4.5 on the post-1/21/2026 TOEFL 1-6 scale (80 prior).",
    name="Computer Science, Ph.D. (and Cybersecurity, Ph.D.)",
    checked=CHECKED,
)

# 2. Electrical and Computer Engineering
save_program(
    UID,
    "ece",
    "Department of Electrical and Computer Engineering",
    ECE_PAGE,
    {
        "deadline": (
            "2027-08-16",
            "Fall 2027 Graduate School deadline is August 16, 2027 (applications are reviewed continuously); however, ECE recommends international applicants apply at least 3 months before term start (~May 2027) for visa processing, and Graduate School First-Year Fellowship nominations close February 15, 2027.",
            "Fall 2027: August 16, 2027",
            GS_ACAD,
            {
                "time_sensitive": "2027-02-15",
                "also": [
                    {
                        "quote": "Applications are reviewed on a continual basis. Please visit the Graduate School’s page to review application deadlines by program. It is recommended that international students apply at least three months prior to the start of the semester to allow time to request a visa.",
                        "url": ECE_PAGE,
                    }
                ],
            },
        ),
        "gre_general": (
            "Required",
            "GRE General (Verbal and Quantitative) is required for applicants whose highest degree is from an international university or non-ABET program (may be waived only by special petition to the ECE Graduate Studies Committee).",
            "Graduate Record Examination (GRE): applicants whose highest degree is held from an international university or from a non-ABET-accredited undergraduate program are required to take the verbal-reasoning and quantitative-reasoning portions of the Graduate Records Examinations (GRE) | The GRE requirement may be waived by special petition to the Department Graduate Studies Committee.",
            ECE_PAGE,
            {
                "also": [
                    {
                        "quote": "GRE: required if domestic applicant GPA < 3.3; GRE is required for all students with international transcripts",
                        "url": GS_ACAD,
                    }
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Electrical and Computer Engineering (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            ETS_SUBJ,
        ),
        "supervisor": (
            "Not required",
            "Students select a Ph.D. advisor after admission and develop their Plan of Study with that advisor by the end of their second semester.",
            "Once accepted into the ECE PhD program the student must: Select a PhD advisor and complete a Plan of Study | Once accepted into the program, the student must select a PhD advisor. ... This must be accomplished by the end of the second semester of residence in the PhD program.",
            ECE_GRAD_REQ,
        ),
        "funding": (
            "Competitive",
            "Funding is competitive rather than guaranteed: students apply separately to the department for RA/TA positions, alongside competitive Graduate School PhD Grants (up to $26,000/yr), Tuition Matching Grants (up to $8,000/yr), and First-Year Fellowships ($6,000/yr).",
            "Research/Teaching Assistantships may be available, and are used for requesting financial assistance from the department - please contact the department directly for the RA/TA application.",
            EAS_APPLY,
            {
                "also": [
                    {
                        "quote": "Spring 2027: January 12, 2027 (assistantships: October 1, 2026)",
                        "url": GS_ACAD,
                    },
                    {
                        "quote": "The Graduate School Tuition Matching Grant provides funding, up to $8,000, with 50 – 100 awards made annually across all graduate programs at UCCS.",
                        "url": GS_FELL,
                    },
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Both bachelor's-entry (66 credit hours: 36 coursework + 30 dissertation) and master's-entry (60 credit hours: 12 coursework + up to 18 MS transfer credits + 30 dissertation) pathways exist, requiring a >= 3.3 GPA.",
            "Requirements for students entering with a master's degree (60 credits): ... Requirements for students entering without a master's degree (66 credits):",
            ECE_PAGE,
        ),
    },
    notes="ECE notes 'Applicants earning an undergraduate or graduate degrees from non-English institutions are required to show proof of English proficiency' without detailing an MOI waiver; under Graduate School policy, contact ECE directly to verify whether an English-medium degree from India qualifies (legacy EAS instructions cite only US-degree or UCCS ESL completion waivers). Minimum GPA 3.3 across previous undergraduate and graduate work; preliminary exam is offered annually in January.",
    name="Engineering, Ph.D. (Electrical Engineering Concentration)",
    checked=CHECKED,
)

# 3. Mechanical & Aerospace Engineering
save_program(
    UID,
    "mech",
    "Department of Mechanical and Aerospace Engineering",
    MAE_APP,
    {
        "deadline": (
            "2027-01-15",
            "Fall 2027 deadline for full TA/RA funding consideration is January 15, 2027; final Fall admission deadline is March 15, 2027 (Spring: August 15 TA/RA, October 15 final).",
            "Fall admission: January 15 for full consideration of TA and RA positions (Applications accepted until March 15)",
            MAE_APP,
            {
                "also": [
                    {
                        "quote": "Fall 2027: March 15, 2027 (TA and RA apps: January 15, 2027)",
                        "url": GS_ACAD,
                    }
                ]
            },
        ),
        "gre_general": (
            "Required",
            "GRE General is required for all international applicants and for graduates of foreign universities (waived only for domestic ABET ME/AE graduates meeting GPA criteria).",
            "GRE: Required for ALL international applicants. Required for domestic applicants if GPA < 3.3 OR if undergraduate degree is not in aerospace or mechanical engineering from an ABET-accredited program.",
            GS_ACAD,
            {
                "also": [
                    {
                        "quote": "Graduate Record Examination (GRE) scores are not required except in the following cases: Failure to meet the GPA requirement | Previous degree from a foreign university",
                        "url": MAE_APP,
                    }
                ]
            },
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Mechanical and Aerospace Engineering (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            ETS_SUBJ,
        ),
        "supervisor": (
            "Not required",
            "Students formally select their MAE dissertation advisor after passing the qualifying examination; however, applicants are asked in their goal statement to name a faculty member from the MAE directory and explain research fit.",
            "Once the qualifying exam has been successfully completed, the dissertation committee will be formed. The student will select a dissertation advisor from the MAE faculty.",
            MAE_PHD,
            {
                "also": [
                    {
                        "quote": "Also include in your goal statement the faculty member's name that you selected on the previous page and describe why you feel they would be a good fit for you as your advisor.",
                        "url": GS_ACAD,
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            "Teaching and research assistantships require applying by the January 15 priority deadline for full consideration (not guaranteed), alongside competitive Graduate School PhD Grants (up to $26,000/yr) and Tuition Matching Grants (up to $8,000/yr).",
            "Fall admission: January 15 for full consideration of TA and RA positions",
            MAE_APP,
            {
                "also": [
                    {
                        "quote": "Awards in any amount of up to $26,000 per year, or $13,000 per semester, may be processed by the Office of Financial Aid. | Resident and nonresident graduate students, including international students, are eligible for this grant.",
                        "url": GS_FELL,
                    }
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Admits students with either a Bachelor of Science or Master of Science in Mechanical Engineering, Aerospace Engineering, or a closely related field with >= 3.3 GPA (BS entrants must also satisfy MS admission prerequisites; up to 21 MS credits transferable, or 24 with waiver).",
            "Bachelor of Science or Master of Science in Mechanical Engineering, Aerospace Engineering, or closely related field with a GPA of 3.3/4.0 on all previous college work. BS students must also satisfy all admission requirements for the Master of Science.",
            MAE_APP,
        ),
    },
    notes="Graduate School table sets 4.5 TOEFL iBT on the post-1/21/2026 scale (legacy 80 iBT / IELTS 6.5 also shown on MAE application page). Program requires 30 coursework + 30 dissertation credits; qualifying exam covers Thermal and Fluid Systems, Solid Mechanics/Structures/Materials, or Dynamics and Controls after one academic semester.",
    name="Mechanical & Aerospace Engineering, Ph.D.",
    checked=CHECKED,
)

# 4. Mathematics (Applied Science: Mathematics)
save_program(
    UID,
    "math",
    "Department of Mathematics",
    MATH_PHD,
    {
        "deadline": (
            "2027-04-01",
            "Graduate Teaching Fellowship (GTF) funding applications for Fall are due April 1, 2027 (inferred from annual 'APRIL 1st'; Spring GTF: October 31). Admission itself is rolling until 1 week before Fall 2027 classes (August 16, 2027 on GS page; 60 days prior recommended for international/document processing); Graduate School First-Year Fellowship nominations close February 15.",
            "Applications for GTF positions are due APRIL 1st for the Fall semester and OCTOBER 31st for the Spring semester.",
            MATH_GTF,
            {
                "inferred": "year",
                "time_sensitive": "2027-02-15",
                "also": [
                    {
                        "quote": "Fall 2027: August 16, 2027",
                        "url": GS_ACAD,
                    },
                    {
                        "quote": "Completed applications (including all supporting documentation) should be submitted 60 days prior to the term for which admission is sought. However, applications are reviewed on a continuous basis, and will be considered if this deadline is not met.",
                        "url": MATH_FORMS,
                    },
                ],
            },
        ),
        "gre_general": (
            "Required",
            "GRE General Test taken within the last 2 years is required (for non-UCCS students), with >= 80th percentile Quantitative recommended.",
            "Submit GRE General Test scores, taken within the last 2 years, with a recommended percentile of 80 or higher on the Quantitative Reasoning section.",
            MATH_PHD,
            {
                "also": [
                    {
                        "quote": "Scores from the GRE General Test, taken within the last 2 years (for Spring 2022 or later admission)",
                        "url": MATH_FORMS,
                    }
                ]
            },
        ),
        "gre_subject": (
            "Not stated",
            "Department and Graduate School pages list only the GRE General Test and do not state any policy on the ETS Mathematics Subject Test.",
            "",
            MATH_PHD,
        ),
        "supervisor": (
            "Not required",
            "Admission decisions are made individually by the Mathematics Graduate Committee; prospective applicants are encouraged to review faculty research interests and contact faculty to discuss mentorship.",
            "decisions regarding admission are made on an individual basis by the Graduate Committee.",
            MATH_PHD,
            {
                "also": [
                    {
                        "quote": "For more information or to discuss mentorship, please see our research interests and contact faculty directly.",
                        "url": MATH_GRAD,
                    }
                ]
            },
        ),
        "funding": (
            "Competitive",
            "A limited number of competitive Graduate Teaching Fellowships (GTFs) provide a tuition grant and teaching pay (renewable annually based on performance; apply by April 1 for Fall), alongside competitive Graduate School PhD Grants (up to $26,000/yr) and Tuition Matching Grants (up to $8,000/yr).",
            "For students enrolled in the mathematics M.S. and Ph.D. programs, the department offers a limited number of Graduate Teaching Fellowships (GTF's). Each GTF receives a tuition grant and pay for teaching. | Applications for GTF positions are due APRIL 1st for the Fall semester",
            MATH_GTF,
            {
                "also": [
                    {
                        "quote": "A limited number of scholarships are available each year from the Department of Mathematics to provide financial support to students enrolled in the PhD program.",
                        "url": MATH_PHD,
                    }
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Requires a bachelor's degree in mathematics or a related field with significant math coursework (>= 3.0 overall and math GPA); up to 25% of the 60 required credits may be transferred from prior graduate or MS coursework.",
            "Holding a baccalaureate degree in mathematics or a related field with significant math coursework from an accredited college or university | The total hours of graduate coursework and dissertation work applied to the degree must be 60. This total may include coursework applied toward a Master's degree.",
            MATH_PHD,
        ),
    },
    notes="Official degree track is Applied Science: Mathematics, Ph.D., spanning probability and statistics, differential equations, applied analysis, algebra, and coding theory. Department English page confirms TOEFL 80 (legacy web scale) / IELTS 6.5 / Duolingo 105 (note GS updated chart lists 4.5 on the 1-6 scale effective 1/21/2026 and Duolingo 115) and defers exemptions to UCCS admissions policy. Conditional admission is NOT granted for applicants not meeting English proficiency requirements.",
    name="Applied Science: Mathematics, Ph.D.",
    checked=CHECKED,
)

# 5. Physics (Applied Science: Physics)
save_program(
    UID,
    "physics",
    "Department of Physics & Energy Science",
    PHYS_PHD,
    {
        "deadline": (
            "2027-08-16",
            "Fall 2027 Graduate School deadline is August 16, 2027 (Spring 2027: January 12, 2027; Summer 2027: June 7, 2027), with no separate departmental admission deadline posted. Apply before February 15, 2027 if seeking nomination for the Graduate School First-Year Graduate Fellowship ($6,000).",
            "Fall 2027: August 16, 2027",
            GS_ACAD,
            {
                "time_sensitive": "2027-02-15",
                "also": [
                    {
                        "quote": "Programs may nominate up to five eligible incoming (first year) graduate students by February 15th annually.",
                        "url": GS_FELL,
                    }
                ],
            },
        ),
        "gre_general": (
            "Not stated",
            "Neither the Physics Ph.D. webpage nor the Ph.D. handbook specifies a GRE General Test requirement (only the Physics GRE is specified for international transcripts).",
            "",
            PHYS_PHD,
        ),
        "gre_subject": (
            "Required",
            "Applicants with international transcripts must take the ETS Physics GRE Subject Test; minimum score for regular admission is 520-550.",
            "Students with international transcripts must take the Physics GRE exam. A minimum score for regular admission is in the range of 520-550.",
            PHYS_PHD,
            {
                "also": [
                    {
                        "quote": "students with international transcripts must take the Physics GRE exam. A minimum score for regular admission is in the range of 520-550.",
                        "url": PHYS_HB,
                    }
                ]
            },
        ),
        "toefl_min": (
            "83",
            "Physics department page and handbook specify a minimum TOEFL iBT of 83 (560 PBT), which is stricter than the Graduate School chart's legacy 80 iBT / 4.5 (1-6 scale effective 1/21/2026); an oral interview with Physics faculty may also be required.",
            "Applicants for whom English is a second language must complete the TOEFL exam with a minimum score of 560 (paper-based exam) or 83 (internet-based exam) or 220 (internet-based exam).",
            PHYS_PHD,
            {
                "also": [
                    {
                        "quote": "Physics: Applied Science PhD 80 4.5 6.5 115",
                        "url": GS_ENG,
                    }
                ]
            },
        ),
        "english_waiver": (
            "No",
            "Physics states the English test requirement can be waived only if the student has successfully completed one year of full-time academic study at a U.S. institution; an English-medium degree from India alone does not waive it, and an oral interview with Physics faculty may also be required.",
            "Applicants for whom English is a second language must complete the TOEFL exam with a minimum score of 560 (paper-based exam) or 83 (internet-based exam) or 220 (internet-based exam). A band score of 6.5 on the IELTS is also acceptable. If the student has successfully completed one year of full-time academic study at a U.S. institution, this requirement can be waived.",
            PHYS_PHD,
        ),
        "supervisor": (
            "Not required",
            "Bachelor's entrants are not required to have a pre-committed advisor at admission and must identify a willing dissertation adviser by the time coursework is completed; however, applicants who already hold a Physics Master's degree should contact a potential faculty research adviser in advance.",
            "By the time students have successfully completed the coursework requirements of the PhD program, they must identify a dissertation adviser who agrees to supervise their research work. | Applicants who already hold a Masters degree in Physics should discuss their application with a potential faculty research adviser in advance, and mention these discussions in their goal statement.",
            PHYS_PHD,
        ),
        "funding": (
            "Competitive",
            "Funding is explicitly NOT guaranteed with admission. Competitive support includes Teaching Assistant positions (~$2,000 per lab plus possible tuition support), hourly Research Assistant positions funded by faculty grants, and Graduate School PhD Grants (up to $26,000/yr) or Tuition Matching Grants (up to $8,000/yr).",
            "Students admitted to the PhD program are NOT guaranteed funding. However, various funding opportunities exist that students are encouraged to look into: 1. Teaching Assistant positions worth roughly $2,000 per lab, plus the possibility of some tuition support.",
            PHYS_HB,
            {
                "also": [
                    {
                        "quote": "Awards in any amount of up to $26,000 per year, or $13,000 per semester, may be processed by the Office of Financial Aid. | Resident and nonresident graduate students, including international students, are eligible for this grant.",
                        "url": GS_FELL,
                    }
                ]
            },
        ),
        "entry_route": (
            "Direct from bachelor's",
            "Requires a bachelor's degree in biological sciences, mathematics, physics, or equivalent with >= 3.0 undergraduate GPA and appropriate undergraduate physics coursework (66-credit program; master's transfer credits may reduce coursework at adviser's discretion).",
            "Hold a baccalaureate degree in biological sciences, mathematics, physics or equivalents from an accredited college or university and have an appropriate background of undergraduate physics courses",
            PHYS_PHD,
        ),
    },
    notes="Official degree track is Applied Science: Physics, Ph.D. Research areas span Solid State and Quantum Physics, Fundamental Magnetism/Spintronics, Nanotechnology & Plasmonics, Liquid Crystals, Bio-Physics, and Nonlinear Physics & Chaos. Department website (83 iBT / 560 PBT, US-study-only waiver) is stricter than Graduate School table (80 legacy / 4.5 effective 1/21/2026); the Physics webpage text '220 (internet-based exam)' reflects the legacy computer-based score typoed as iBT.",
    name="Applied Science: Physics, Ph.D.",
    checked=CHECKED,
)

print("Saved UCCS records to data/staging/")
