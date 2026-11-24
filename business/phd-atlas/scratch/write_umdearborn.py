import os
import sys

os.environ["ATLAS_OUT"] = "data/staging"
sys.path.insert(0, "scripts")
import rec  # noqa: E402

ETS_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

CAT_ADM = "https://catalog.umd.umich.edu/graduate/graduate-admissions/"
CAT_PRE = "https://catalog.umd.umich.edu/graduate/graduate-admissions/prerequisites-by-college/college-engineering-and-computer-science/"
CECS_ADM = "https://umdearborn.edu/cecs/graduate-programs/admissions"
APPLY_URL = "https://umdearborn.edu/admissions-aid/graduate-applicants/apply-graduate-student"
WAIVER_URL = "https://umdearborn.edu/admissions-aid/graduate-applicants/planning-graduate-school/application-fee-waivers"

CHECKED = "2026-11-14"

rec.save_university(
    uid="umdearborn",
    institution="University of Michigan-Dearborn",
    country="USA",
    region="Michigan",
    grad_page=APPLY_URL,
    checked=CHECKED,
    fields={
        "app_fee": (
            "60 USD",
            "$60 non-refundable graduate application fee per program application.",
            "Submission requires a $60 application fee. UM-Dearborn offers limited application fee waivers on a first-come, first-serve basis. The fee is nonrefundable and cannot be applied toward tuition or other fees.",
            APPLY_URL,
        ),
        "fee_waiver": (
            "Limited",
            "Limited first-come, first-served waivers: international applicants qualify if they are current Fulbright Scholars, UM-Dearborn students/alumni/employees, citizens/residents of countries with SWIFT banking sanctions, or attendees who check in at an eligible recruitment event (financial need waivers are restricted to U.S. citizens/permanent residents).",
            "UM-Dearborn has a defined policy for granting application fee waivers, which are considered on a first-come, first-serve basis. | Current Fulbright or McNair Scholar with award letter | U.S. citizens or legal permanent residents demonstrating extreme financial need (financial need waivers are not available to international applicants) | Applicants from countries with SWIFT banking sanctions in place will be considered for a waiver | Attend an eligible recruitment event",
            WAIVER_URL,
        ),
        "gre_general": (
            "Not required",
            "GRE/GMAT is not required for UM-Dearborn graduate programs (optional; admissions committee may request scores during holistic review if needed to demonstrate readiness).",
            "Note: our graduate programs do not require the GRE or GMAT. If received, they will be linked to your application file and weighed at the discretion of the review committee during decision review.",
            CAT_ADM,
            {
                "also": [
                    {
                        "quote": "Our graduate programs do not require the GRE or GMAT. If you submit test scores, we will link them to your application file and the review committee may consider them during the admissions decision process.",
                        "url": APPLY_URL,
                    }
                ]
            },
        ),
        "toefl_min": (
            "84",
            "Minimum TOEFL iBT score of 84 overall is required for Ph.D. programs (higher than the 79 overall minimum for most master's programs; ETS code 1861; Duolingo 105 or MET 59 also accepted).",
            "Overall 79 for most programs; 84 overall for PhD, EdD, EdS, and Psychology (MS)",
            CAT_ADM,
        ),
        "ielts_min": (
            "6.5",
            "Minimum IELTS Academic score of 6.5 overall required for graduate admission.",
            "IELTS | Overall 6.5",
            CAT_ADM,
        ),
        "english_waiver": (
            "Conditional",
            "Applicants who have earned or will earn a bachelor's or master's degree from an institution where the language of instruction is exclusively English (including India) may be exempt from submitting an official English proficiency score; institutional verification may be required.",
            "Applicants who have earned or will earn a bachelor's or master's degree from an institution where the language of instruction is exclusively English may be exempt from submitting an Official English Proficiency Score. Verification from the school may be required.",
            CAT_ADM,
        ),
    },
    notes=(
        "UM-Dearborn's 4 research Ph.D. programs are Rackham Graduate School (University of Michigan-Ann Arbor) programs located, administered, and offered by UM-Dearborn within the College of Engineering and Computer Science (CECS). "
        "3 programs map to the 18 Atlas fields: cs (Computer and Information Science, also datasci), ece (Electrical, Electronics, and Computer Engineering), and mech (Mechanical Sciences and Engineering, also bme & materials). "
        "The 4th Ph.D. — Industrial and Systems Engineering (https://umdearborn.edu/academics/program/industrial-and-systems-engineering-phd; master's required GPA >= 3.5, Jan 15 Fall / Aug 1 Winter deadline, 5-year guaranteed GSI/GSRA funding, no GRE required) — has no standalone Industrial Engineering category in the 18 Atlas fields and is noted here. "
        "Excluded professional and non-STEM doctorates: Doctor of Engineering (D.Eng.) in Automotive Systems and Mobility and in Electrical and Computer Engineering (geared toward working professionals with >= 2 years industry experience), and Ed.D. in Education."
    ),
)

CIS_URL = "https://umdearborn.edu/academics/program/computer-and-information-science-phd"
CIS_CAT = "https://catalog.umd.umich.edu/graduate/college-engineering-computer-science/computer-information-science/"

rec.save_program(
    uid="umdearborn",
    field="cs",
    also_fields=["datasci"],
    department="Department of Computer and Information Science",
    name="Computer and Information Science, Ph.D.",
    page=CIS_URL,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-15",
            "Strict Fall 2027 deadline: January 15, 2027 (Winter term deadline: August 1).",
            "This program operates on a strict deadline. All application and materials must be submitted by January 15 for Fall consideration and August 1 for Winter consideration.",
            CIS_URL,
            {"inferred": "year"},
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Computer Science or Data Science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Not required",
            "Applications are reviewed by the department; admitted Ph.D. CIS students identify a faculty research advisor and topic as their first program milestone.",
            "Each student is guided by a research advisor and a dissertation committee and has to pass the following major milestones: | Identifying the faculty advisor and research topic",
            CIS_CAT,
            {
                "also": [
                    {
                        "quote": "The University of Michigan-Dearborn Office of Graduate Studies coordinates the application process for all programs in the College of Engineering and Computer Science. Individual CECS departments review all applications for program admission requirements and make decisions on each applicant.",
                        "url": CECS_ADM,
                    }
                ]
            },
        ),
        "funding": (
            "Guaranteed",
            "All Ph.D. CIS students receive full funding via GSI and/or GSRA appointments (monthly stipend, health insurance, and tuition waiver) guaranteed for up to 5 years with good standing.",
            "To lessen financial concerns, all Ph.D. students receive full funding in the form of appointments as a graduate student instructor, a research assistant, or both. The appointments provide a monthly stipend, health insurance, and a tuition waiver. Students are guaranteed full funding for up to five years provided they maintain good academic standing and adequate progress toward their degree.",
            CIS_URL,
        ),
        "entry_route": (
            "Either",
            "Admits students with a bachelor's degree (expected GPA >= 3.2; 36 coursework credits + 24 dissertation credits, optionally earning an M.S. in CIS or Data Science en route) or a master's degree (expected GPA >= 3.5) in engineering, applied mathematics, computer science, or a physical science.",
            "Computer and Information Science (PhD) | Previous Degrees Required | Bachelor or master's degree in engineering, applied mathematics, computer science, or a physical science | Bachelor's degree expected GPA of 3.2 or higher on a 4-point scale | Master's degree expected GPA of 3.5 or higher on a 4-point scale",
            CAT_PRE,
            {
                "also": [
                    {
                        "quote": "Students with just a B.S. in computer and information science or closely related area | Complete at least 36 credit hours of coursework, including 30 credit hours toward the completion of the MS degree, and at least 24 dissertation credits, and can earn an M.S. CIS, M.S. DS, M.S. SWE, M.S. CIA, or M.S. AI along the way to their Ph.D. CIS.",
                        "url": CIS_CAT,
                    }
                ]
            },
        ),
    },
    notes="Rackham Ph.D. offered at UM-Dearborn with four official concentration areas: Data Management, Data Science, Systems and Security, and Software Engineering (mapped to cs with also_fields=['datasci']). Requires 3 recommendations; direct B.S. admits complete 36 coursework + 24 dissertation credits (prior UM M.S.: 6+24; non-UM M.S.: 18+24).",
)

ECE_URL = "https://umdearborn.edu/academics/program/electrical-electronics-and-computer-engineering-phd"
ECE_CAT = "https://catalog.umd.umich.edu/graduate/college-engineering-computer-science/electrical-computer-engineering/"
ECE_DEPT = "https://umdearborn.edu/cecs/departments/electrical-and-computer-engineering/graduate-programs"

rec.save_program(
    uid="umdearborn",
    field="ece",
    department="Department of Electrical and Computer Engineering",
    name="Electrical, Electronics, and Computer Engineering, Ph.D.",
    page=ECE_URL,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-15",
            "Strict Fall 2027 deadline: January 15, 2027 (Winter term deadline: August 1).",
            "This program operates on a strict deadline. All application and materials must be submitted by January 15 for Fall consideration and August 1 for Winter consideration.",
            ECE_URL,
            {"inferred": "year"},
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Electrical and Computer Engineering (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Not required",
            "Applications are reviewed by the ECE department; enrolled Ph.D. students receive guidance from an assigned faculty advisor and mentor.",
            "Ph.D. students receive academic and research guidance from their assigned faculty advisor and mentor.",
            ECE_DEPT,
            {
                "also": [
                    {
                        "quote": "Individual CECS departments review all applications for program admission requirements and make decisions on each applicant.",
                        "url": CECS_ADM,
                    }
                ]
            },
        ),
        "funding": (
            "Guaranteed",
            "All Ph.D. EECE students receive full funding via GSI and/or GSRA appointments (monthly stipend, health insurance, and tuition waiver) guaranteed for up to 5 years with good standing.",
            "To lessen financial concerns, all PhD students receive full funding in the form of appointments as a graduate student instructor, a research assistant, or both. The appointments provide a monthly stipend, health insurance, and a tuition waiver. Students are guaranteed full funding for up to five years provided they maintain good academic standing and adequate progress toward their degree.",
            ECE_URL,
        ),
        "entry_route": (
            "Either",
            "Admits students with a bachelor's or master's degree in ECE/CS (expected GPA >= 3.2; 36 coursework + 24 dissertation credits for direct B.S. entrants, with optional embedded M.S. in EE or CE).",
            "Electrical, Electronics and Computer Engineering (PhD) | Previous Degrees Required | Bachelor or master's degree in electrical and/or computer engineering or computer science with an expected GPA of 3.2 or higher on a 4-point scale",
            CAT_PRE,
            {
                "also": [
                    {
                        "quote": "The EECE Ph.D. degree requirements include a minimum of 36 credits of coursework and a minimum of 24 credit hours of dissertation credits for Ph.D. students entering the program without a prior M.S. degree.",
                        "url": ECE_CAT,
                    }
                ]
            },
        ),
    },
    notes="Rackham Ph.D. in Electrical, Electronics, and Computer Engineering offered by UM-Dearborn ECE (core areas: Computer Systems & Networks; Control Systems & Signal Processing; Electronics, Optoelectronics, Power & Energy Systems; Intelligent Systems & Robotics). Separate part-time/working-professional D.Eng. in ECE is excluded.",
)

MECH_URL = "https://umdearborn.edu/academics/program/mechanical-sciences-and-engineering-phd"
MECH_CAT = "https://catalog.umd.umich.edu/graduate/college-engineering-computer-science/mechanical-sciences-engineering/"

rec.save_program(
    uid="umdearborn",
    field="mech",
    also_fields=["bme", "materials"],
    department="Department of Mechanical Engineering",
    name="Mechanical Sciences and Engineering, Ph.D.",
    page=MECH_URL,
    checked=CHECKED,
    fields={
        "deadline": (
            "2027-01-15",
            "Strict Fall 2027 deadline: January 15, 2027 (program page also lists August 1 for Winter, though the Graduate Catalog states Fall-only admission).",
            "This program operates on a strict deadline. All application and materials must be submitted by January 15 for Fall consideration and August 1 for Winter consideration.",
            MECH_URL,
            {"inferred": "year"},
        ),
        "gre_subject": (
            "No subject test",
            "No GRE Subject Test exists for Mechanical Engineering, Bioengineering, or Materials Science (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
            ETS_QUOTE,
            ETS_URL,
        ),
        "supervisor": (
            "Not required",
            "Individual CECS departments review applications for admission; students work with a research advisor and dissertation committee after admission.",
            "Each student is guided by a research advisor and a dissertation committee and must pass the following major milestones:",
            MECH_CAT,
            {
                "also": [
                    {
                        "quote": "Individual CECS departments review all applications for program admission requirements and make decisions on each applicant.",
                        "url": CECS_ADM,
                    }
                ]
            },
        ),
        "funding": (
            "Guaranteed",
            "All Ph.D. MSE students receive full funding via GSI and/or GSRA appointments (monthly stipend, health insurance, and tuition waiver) guaranteed for up to 5 years with good standing.",
            "To lessen financial concerns, all PhD students receive full funding in the form of appointments as a graduate student instructor, a research assistant, or both. The appointments provide a monthly stipend, health insurance, and a tuition waiver. Students are guaranteed full funding for up to five years provided they maintain good academic standing and adequate progress toward their degree.",
            MECH_URL,
        ),
        "entry_route": (
            "Either",
            "Admits exceptional applicants with a bachelor's or master's degree in engineering, applied math, computer science, or physical science (36 coursework + 24 dissertation credits for direct B.S. entrants, including an embedded M.S.E. in Mechanical Engineering or Bioengineering).",
            "The Ph.D. program is highly selective and offers admission to exceptional students who have completed a Bachelor's or Master's degree in engineering, applied math, computer science, or physical science. | Direct Ph.D. students, who are admitted with a Bachelor’s degree in mechanical engineering or a closely related field, but without a relevant Master’s degree. Students of this group must complete no fewer than 36 credit hours of coursework, 30 of which allow them to earn an embedded MSE in mechanical engineering or bioengineering.",
            MECH_CAT,
        ),
    },
    notes="Rackham Ph.D. in Mechanical Sciences and Engineering covering core mechanical/thermo-fluid sciences as well as explicit interfaces with bioengineering (embedded M.S.E. option) and materials sciences (mapped to mech with also_fields=['bme', 'materials']). Note: program page and deadlines table list January 15 (Fall) and August 1 (Winter), whereas the 2026-2027 Graduate Catalog states 'All admissions are for the Fall term only.' Separate Industrial and Systems Engineering Ph.D. is noted on umdearborn.json; D.Eng. in Automotive Systems and Mobility is excluded.",
)
print("Wrote umdearborn university + 3 program records to data/staging/")
