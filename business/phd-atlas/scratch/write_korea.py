import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING_UNI = ROOT / "data" / "staging" / "universities"
STAGING_PROG = ROOT / "data" / "staging" / "programs"
STAGING_UNI.mkdir(parents=True, exist_ok=True)
STAGING_PROG.mkdir(parents=True, exist_ok=True)

CHECKED = "2026-11-24"

URL_MAIN = "https://graduate2.korea.ac.kr/main/main.html"
URL_SCHED = "https://graduate2.korea.ac.kr/admission/schedule.html"
URL_PROC = "https://graduate2.korea.ac.kr/admission/procedure.html"
URL_ELIG = "https://graduate2.korea.ac.kr/admission/eligibility.html"
URL_SCHOL = "https://graduate2.korea.ac.kr/scholarship/scholarships.html"
URL_INFO02 = "https://graduate2.korea.ac.kr/academic/info02.html"
URL_ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"

uni_data = {
    "id": "korea",
    "institution": "Korea University",
    "country": "South Korea",
    "region": "Seoul",
    "grad_page": URL_MAIN,
    "checked": CHECKED,
    "fields": {
        "app_fee": {
            "code": "127000 KRW",
            "value": "Total online application payment is KRW 127,000 (KRW 120,000 application fee + KRW 7,000 commission fee), payable at the time of online application submission.",
            "quote": "Total payment: KRW 127,000 | (Application fee: KRW 120,000 + commission fee: KRW 7,000)",
            "url": URL_SCHED,
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Korea University Graduate School's Admission Schedule lists the KRW 127,000 total payment (KRW 120,000 application fee + KRW 7,000 commission fee) and does not state an application fee waiver policy for international applicants.",
            "quote": "",
            "url": URL_SCHED,
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Korea University Graduate School's Eligibility page and 2027 International Application Guide specify academic credentials and language proficiency requirements without stating a GRE General requirement.",
            "quote": "",
            "url": URL_ELIG,
        },
        "toefl_min": {
            "code": "3.5 (new scale)",
            "value": "Minimum TOEFL iBT 3.5 for tests taken on or after January 21, 2026 (71 on the prior 0-120 scale; Home Edition accepted; TOEFL MyBest Scores not accepted). Applicants may alternatively meet the language requirement via TOPIK Level 3+, Academic IELTS 5.5+, New TEPS 326+, or CEFR B2+. Note: KU international admission scholarships require higher scores (TOEFL iBT 82 / 4.5 for Type B/C, 90 / 5.0 for Type A; Home Edition not accepted for scholarships).",
            "quote": "1) TOEFL iBT 71(including Home Edition, a score of 3.5 for tests taken on or after Jan 21. 2026) or higher | TOEFL My Best Scores is NOT acceptable",
            "url": URL_ELIG,
        },
        "ielts_min": {
            "code": "5.5",
            "value": "Minimum Academic IELTS 5.5 or higher (IELTS Indicator not accepted). Applicants may alternatively meet the language requirement via TOEFL iBT 3.5/71+, TOPIK Level 3+, New TEPS 326+, or CEFR B2+. Note: KU international admission scholarships require Academic IELTS 6.0 (Type B/C) or 7.0 (Type A).",
            "quote": "2) Academic IELTS 5.5 or higher | The IELTS Indicator is NOT acceptable.",
            "url": URL_ELIG,
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exempt from submitting an English proficiency test score for admission if the applicant is a native English speaker from KU's listed exempt countries, completed a degree program (BA, MA, or Ph.D.) in an English-speaking country or Korea, completed a degree program 100% in English, or receives a departmental language proficiency recommendation letter. Note: an original test score is still mandatory to apply for KU Graduate School Scholarships.",
            "quote": "C. Others | Applicants who meet one of the following options below: | 1) Native English Speaker(Refer to the list of the countries exempt from the English Proficiency Requirement) | 2) Applicants who have completed their degree program(BA, MA, and Ph.D) in the English speaking countries | 5) Applicants who have completed their degree program(BA, MA, and Ph.D) 100% in English",
            "url": URL_ELIG,
        },
    },
    "notes": "QS WUR 2027 =#52. Covers 17 offered STEM PhD/Integrated MA-PhD fields across Korea University's Seoul Campus General Graduate School (no standalone Astronomy & Astrophysics PhD; Physics covers Condensed Matter, Elementary Particle/High-Energy, Nuclear, Nonlinear Dynamics & Biophysics, Statistical Physics, Quantum Optics, and Quantum Information Physics). International admissions run twice per year: Spring 2027 online applications ran September 1-10, 2026, while Fall 2027 exact dates are not yet published (Admission Procedure places Fall semester submission in March; Fall 2027 semester begins September 1, 2027). Tuition (AY 2026) is KRW 6,339,000/semester for Natural Sciences, KRW 7,392,000/semester for Engineering, KRW 6,866,000/semester for Health Science, and KRW 9,267,000/semester for Medicine (plus one-time entrance fee KRW 1,142,000-1,206,000). Competitive KU International Student Scholarships (Type A: 100% tuition/entrance fee + KRW 500,000/mo living support for 4 months/semester; Type C Natural Science & Engineering: 65% tuition) are evaluated automatically with admission; GKS and BK21 support are also available.",
}

(STAGING_UNI / "korea.json").write_text(
    json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

PROGRAMS = [
    {
        "field": "biology",
        "name": "Life Sciences, Ph.D. / Integrated MA-PhD",
        "department": "College of Life Sciences and Biotechnology — Department of Life Sciences",
        "program_page": "https://ls.korea.edu/ls_en/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Biochemistry, Molecular Biology, Cell Biology, and Molecular Medical Science. Note: Korea University's 2027 Spring International Application Guide lists Department of Life Sciences among the designated departments requiring one academic recommendation letter (emailed by a previous university professor). Companion departments in the same college include Biotechnology and Plant Biotechnology.",
    },
    {
        "field": "biomed",
        "name": "Biomedical Sciences, Ph.D. / Integrated MA-PhD",
        "department": "College of Medicine — Department of Biomedical Sciences",
        "program_page": "https://bk21kumedicine.korea.ac.kr/bk21kumedicine/index.do",
        "funding_note": "Note: Korea University's Scholarship page specifies that international students in the College of Medicine are granted Scholarship C (65% tuition waiver) only, alongside BK21 and lab research support.",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Biomedical Science, Biomedical Engineering, Clinical Biomedical Engineering, and Fusion Translational Medicine. Note: Korea University's 2027 Spring International Application Guide (p. 2) states that all applicants for the Department of Biomedical Sciences should obtain permission from an academic advisor before submitting their application. Companion College of Health Science department: Integrated Biomedical and Life Sciences.",
    },
    {
        "field": "bme",
        "name": "Bioengineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Health Science — Department of Bioengineering",
        "program_page": "https://bmeng.korea.ac.kr/main/main.html",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Bioengineering within the College of Health Science (Seoul Campus). Companion biomedical engineering tracks also exist in the College of Medicine (Department of Biomedical Sciences: Biomedical Engineering and Clinical Biomedical Engineering).",
    },
    {
        "field": "chemeng",
        "name": "Chemical and Biological Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Engineering — Department of Chemical and Biological Engineering",
        "program_page": "https://eng.korea.ac.kr/eng/education/graduate.html",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Chemical and Biological Engineering within the College of Engineering (Seoul Campus), covering petrochemicals, advanced materials, energy and environment, nanobiocatalysis, and biological engineering.",
    },
    {
        "field": "chemistry",
        "name": "Chemistry, Ph.D. / Integrated MA-PhD",
        "department": "College of Science — Department of Chemistry",
        "program_page": "https://science.korea.edu/science_en/graduate/Graduate_Chemistry1.do",
        "fund_also": {
            "quote": "Due to the active research of its members, the Department was selected for BK21 projects by the Korea Research Foundation in 1999 and BK21 PLUS projects administered by the Ministry of Education in 2013, thereby providing financial support for outstanding students.",
            "url": "https://science.korea.edu/science_en/graduate/Graduate_Chemistry1.do",
        },
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Analytical Chemistry, Organic Chemistry, Biochemistry, Inorganic Chemistry, Physical Chemistry, and Polymer Chemistry, supported by BK21 and research/teaching assistantships.",
    },
    {
        "field": "civil",
        "name": "Civil, Environmental and Architectural Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Engineering — Department of Civil, Environmental and Architectural Engineering",
        "program_page": "https://ace.korea.ac.kr/eng/",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Smart Construction & Mobility, Built Environment, Energy Systems, Water & Ecosystems, and Seismic Resilience within the College of Engineering (Seoul Campus).",
    },
    {
        "field": "cs",
        "name": "Computer Science and Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Informatics — Department of Computer Science and Engineering",
        "program_page": "https://cs.korea.edu/en_cs/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Software, Computer Security, Artificial Intelligence Applications, Radio Communications Engineering, and Computer Education within the College of Informatics (Seoul Campus).",
    },
    {
        "field": "datasci",
        "name": "Artificial Intelligence, Ph.D. / Integrated MA-PhD",
        "department": "College of Informatics — Department of Artificial Intelligence",
        "program_page": "https://info.korea.edu/en_info/grad/ai_intro.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Artificial Intelligence within the College of Informatics (Seoul Campus). Statistical Data Science and Intelligent Statistical Learning Ph.D./Integrated MA-PhD tracks are also offered in the Department of Statistics, and Big Data Science is offered at Sejong Campus.",
    },
    {
        "field": "earth",
        "name": "Earth and Environmental Sciences, Ph.D. / Integrated MA-PhD",
        "department": "College of Science — Department of Earth and Environmental Sciences",
        "program_page": "https://ees.korea.edu/ees_en/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Geology, Geophysics, Environmental Geology, and Atmospheric Environment within the College of Science (Seoul Campus).",
    },
    {
        "field": "ece",
        "name": "Electrical and Computer Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Engineering — Department of Electrical and Computer Engineering",
        "program_page": "https://ee.korea.ac.kr/eng/main/main.html",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Semiconductor and Nano Systems, Signal Processing and Multimedia, Control, Robotics and Systems, Electrical Energy, Computer Engineering, Communication and Networks, and Integrated Circuits.",
    },
    {
        "field": "environment",
        "name": "Environmental Science and Ecological Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Life Sciences and Biotechnology — Department of Environmental Science & Ecological Engineering",
        "program_page": "https://eco.korea.ac.kr/",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Environmental Science and Ecological Engineering (Seoul Campus). Companion environmental tracks also exist in Civil, Environmental and Architectural Engineering (Water & Ecosystems) and Earth and Environmental Sciences (Environmental Geology, Atmospheric Environment).",
    },
    {
        "field": "materials",
        "name": "Materials Science and Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Engineering — Department of Materials Science and Engineering",
        "program_page": "https://mse.korea.ac.kr/index.php",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Advanced Materials Science and Engineering within the College of Engineering (Seoul Campus).",
    },
    {
        "field": "math",
        "name": "Mathematics, Ph.D. / Integrated MA-PhD",
        "department": "College of Science — Department of Mathematics",
        "program_page": "https://math.korea.edu/math_en/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Analysis, Probability, Algebra and Number Theory, Topology, Geometry, and Applied Mathematics (note: Mathematical Data Science in Mathematics is a 1.5-year Master's-only major).",
    },
    {
        "field": "mech",
        "name": "Mechanical Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Engineering — Department of Mechanical Engineering",
        "program_page": "https://me.korea.ac.kr/main/main.html",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Mechanical Engineering within the College of Engineering (Seoul Campus).",
    },
    {
        "field": "neuro",
        "name": "Brain and Cognitive Engineering, Ph.D. / Integrated MA-PhD",
        "department": "College of Informatics — Department of Brain and Cognitive Engineering",
        "program_page": "https://bce.korea.edu/bce_en/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD in Brain and Cognitive Engineering within the College of Informatics (Seoul Campus). Companion Behavioral and Cognitive Neuroscience Ph.D./Integrated MA-PhD track is also offered in the Department of Psychology.",
    },
    {
        "field": "physics",
        "name": "Physics, Ph.D. / Integrated MA-PhD",
        "department": "College of Science — Department of Physics",
        "program_page": "https://physics.korea.edu/phys_en/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Condensed Matter Physics, Elementary Particle (High-Energy) Physics, Nuclear Physics, Nonlinear Dynamics & Biophysics, Statistical Physics, Quantum Optics, and Quantum Information Physics.",
    },
    {
        "field": "statistics",
        "name": "Statistics, Ph.D. / Integrated MA-PhD",
        "department": "College of Political Science & Economics — Department of Statistics",
        "program_page": "https://stat.korea.edu/stat_en/index.do",
        "notes": "Offers Ph.D. and Integrated MA-PhD majors in Mathematical Statistics, Statistical Data Science, and Intelligent Statistical Learning (Seoul Campus).",
    },
]

for p in PROGRAMS:
    fid = p["field"]
    if fid in {"math", "physics", "neuro"}:
        gre_s = {
            "code": "Not stated",
            "value": "Korea University Graduate School's Eligibility page and 2027 International Application Guide do not state a GRE Subject Test requirement for this department.",
            "quote": "",
            "url": URL_ELIG,
        }
    else:
        gre_s = {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for this discipline.",
            "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            "url": URL_ETS_SUBJ,
        }

    fund_val = (
        "International applicants are evaluated automatically and simultaneously for Korea University Graduate School Scholarships for International Students: "
        "Global Leader Scholarship (Type A: 100% entrance and tuition fee waiver + KRW 500,000/month living support for 4 months per semester; requires CGPA >= 3.57/4.0 or 4.0/4.5 and TOEFL iBT 90 / IELTS 7.0) "
        "and Natural Science and Engineering Scholarship (Type C: 65% tuition fee waiver; requires CGPA >= 3.14/4.0 or 3.5/4.5 and TOEFL iBT 82 / IELTS 6.0). "
        "Scholarships cover the first semester and are renewed competitively by GPA each semester; GKS and BK21 assistantships are also available."
    )
    if "funding_note" in p:
        fund_val += " " + p["funding_note"]

    fund_field = {
        "code": "Competitive",
        "value": fund_val,
        "quote": "Korea University Graduate School Scholarship for International Students | Both admission evaluation and scholarship award evaluation will be conducted automatically and simultaneously. | Foreign Student Scholarship A | 100% of entrance fee and tuition fee | Living support fee (Only 4 months during semester) | Foreign Student Scholarship C | 65% of tuition fee | Living support fee (KRW500,000 per month)",
        "url": URL_SCHOL,
    }
    if "fund_also" in p:
        fund_field["also"] = [p["fund_also"]]

    rec = {
        "id": f"korea--{fid}",
        "university": "korea",
        "field": fid,
        "also_fields": [],
        "name": p["name"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "Not stated",
                "time_sensitive": "2027-03-01",
                "value": "Exact Fall 2027 international admission dates have not yet been published; Korea University Graduate School's Admission Procedure states that Fall semester applications and required documents are submitted in March (Spring 2027 online applications ran September 1-10, 2026; Fall 2027 semester begins September 1, 2027).",
                "quote": "STEP1 | Submission of application form & required documents | September (Spring semester) | March (Fall semester)",
                "url": URL_PROC,
                "also": [
                    {
                        "quote": "Beginning of Semester | (Spring 2027) March 2, 2027 | (Fall 2027) September 1, 2027",
                        "url": URL_SCHED,
                    }
                ],
            },
            "gre_subject": gre_s,
            "supervisor": {
                "code": "Not stated",
                "value": (
                    "Korea University Graduate School's Eligibility page does not state a pre-application supervisor requirement (note: the 2027 Spring International Application Guide PDF states applicants to the Department of Biomedical Sciences should obtain permission from an academic advisor before submitting the application)."
                    if fid == "biomed"
                    else "Korea University Graduate School's Eligibility page and 2027 International Application Guide do not state a pre-application supervisor requirement for this department."
                ),
                "quote": "",
                "url": URL_ELIG,
            },
            "funding": fund_field,
            "entry_route": {
                "code": "Either",
                "value": "Korea University Graduate School offers both the Doctoral (Ph.D.) program (for Master's degree holders) and the Integrated Master's-Doctoral (Integrated MA-PhD) program (for Bachelor's degree holders) in this department.",
                "quote": "The applicant must have completed regular primary, secondary and higher education, equivalent to Grades 1 to 12 and Bachelor (or Master or Ph.D) in the Korean education system in overseas.",
                "url": URL_ELIG,
                "also": [
                    {
                        "quote": "Integrated MA-PhD | Doctoral | Time Limits for Course of Study",
                        "url": URL_INFO02,
                    }
                ],
            },
        },
        "notes": p["notes"],
    }
    (STAGING_PROG / f"korea--{fid}.json").write_text(
        json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

print(f"Wrote korea.json and {len(PROGRAMS)} programs to data/staging/")
