import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Add uncw to data/universities.json
uni_list_path = ROOT / "data" / "universities.json"
uni_data = json.loads(uni_list_path.read_text(encoding="utf-8"))
if not any(u["id"] == "uncw" for u in uni_data["universities"]):
    uni_data["universities"].append({
        "id": "uncw",
        "name": "University of North Carolina Wilmington",
        "country": "USA",
        "region": "North Carolina",
        "kind": "university",
        "wave": 5,
    })
    uni_list_path.write_text(json.dumps(uni_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. University record -> data/staging/universities/uncw.json
uni_rec = {
    "id": "uncw",
    "institution": "University of North Carolina Wilmington",
    "country": "USA",
    "region": "North Carolina",
    "grad_page": "https://www.uncw.edu/admissions/graduate/index.html",
    "checked": "2026-11-14",
    "fields": {
        "app_fee": {
            "code": "75 USD",
            "value": "$75 USD non-refundable, non-transferable application fee due upon online submission (MasterCard, Visa, or Discover).",
            "quote": "A $75 USD (non-transferable and non-refundable) application fee is due upon submission and is payable by MasterCard, Visa, or Discover via the online application.",
            "url": "https://www.uncw.edu/admissions/graduate/getting-started.html",
            "also": [
                {
                    "quote": "$75 USD application fee (payable by MasterCard, Visa or Discover) | Application fees are non-refundable and non-transferable and due upon submission",
                    "url": "https://www.uncw.edu/admissions/graduate/apply/index.html",
                }
            ],
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Application fee waivers are limited to United States Service Members, McNair Scholars, and UNCW Faculty/Staff or Dependents; no general need-based or international waiver is available.",
            "quote": "If you are eligible for an application fee waiver, complete the proper form (including any required approvals) from the choices below and upload it into the application when prompted. | United States Service Member | McNair Scholar (form located within the online application) | UNCW Faculty/Staff or Dependent",
            "url": "https://www.uncw.edu/admissions/graduate/getting-started.html",
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE requirements are set by individual graduate programs rather than centrally by the Graduate School (UNCW institution code 5907; test scores valid for five years). Applied Coastal & Ocean Sciences and Integrative, Comparative & Marine Biology do not require GRE scores; Pharmaceutical Chemistry lists no GRE in the 2026-2027 Graduate Catalogue.",
            "quote": "",
            "url": "https://www.uncw.edu/admissions/graduate/getting-started.html",
        },
        "toefl_min": {
            "code": "4.5 (new scale)",
            "value": "Graduate School minimum TOEFL iBT score is 4.5 on the 1-6 scale for exams taken on or after January 21, 2026 (79 on the 0-120 scale for exams taken before January 21, 2026; institution code 5907; scores valid 2 years; Duolingo 115 also accepted).",
            "quote": "TOEFL iBT | School Code: 5907 | For exams taken before January 21, 2026: | Minimum total score: 79 | For exams taken on or after January 21, 2026: | Minimum total score: 4.5",
            "url": "https://www.uncw.edu/admissions/graduate/int-graduate.html",
            "also": [
                {
                    "quote": "A minimum score of 79 for tests taken before January 21, 2026; 4.5 for tests taken on or after January 21, 2026 (TOEFL iBT), 6.5 on the IELTS, or 115 on the Duolingo English Test is required for admission.",
                    "url": "https://catalogue.uncw.edu/content.php?catoid=82&navoid=12358",
                }
            ],
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Graduate School minimum IELTS score is 6.5 for admission and 7.0 for Teaching Assistantship consideration (scores valid 2 years).",
            "quote": "IELTS | IELTS (GENERAL) | School Code: UNCW Graduate School | Minimum Score Requirement: 6.5 for acceptance & 7.0 for teaching assistantship consideration",
            "url": "https://www.uncw.edu/admissions/graduate/int-graduate.html",
        },
        "english_waiver": {
            "code": "Yes",
            "value": "India is explicitly listed under UNCW's 'Additional Approved Country' section of 'Approved Countries with English as the Primary Language', exempting applicants from India from English proficiency test scores (graduates of accredited U.S. colleges/universities are also exempt).",
            "quote": "You are exempt from submitting English language proficiency scores if you meet any of the following conditions: | You are from a country where English is the official primary language (see the approved country list). | Approved Countries with English as the Primary Language | Additional Approved Country | India",
            "url": "https://www.uncw.edu/admissions/graduate/int-graduate.html",
        },
    },
    "notes": "2026-2027 Graduate Catalogue (catoid=82&navoid=12361) and OISS DHS STEM Designated Programs directory confirm 3 STEM-designated Ph.D. programs at UNCW: Applied Coastal and Ocean Sciences (CIP 30.3201), Integrative, Comparative and Marine Biology (CIP 26.9999), and Pharmaceutical Chemistry (CIP 51.2004). Excluded non-STEM/clinical doctorates: Psychology Ph.D. (concentrations in ABAI Applied Behavior Analysis, APA General Clinical, and Psychological Science; not on UNCW's DHS STEM-designated list and has no standalone Neuroscience concentration), Educational Leadership Ed.D., Doctor of Nursing Practice (D.N.P.), and Doctor of Physical Therapy (D.P.T.). International transcripts require an official NACES course-by-course credential evaluation after admission (unofficial transcripts in English may be uploaded for review). Graduate Research Assistants in doctoral programs receive both the NC Resident and NC Non-Resident portions of tuition in addition to their monthly stipend.",
}

# 3. Programs
programs = [
    {
        "id": "uncw--environment",
        "university": "uncw",
        "field": "environment",
        "also_fields": ["earth"],
        "name": "Applied Coastal and Ocean Sciences, Ph.D.",
        "department": "Center for Marine Science",
        "program_page": "https://www.uncw.edu/academics/majors-programs/cms/applied-coastal-ocean-sciences-phd/index.html",
        "checked": "2026-11-14",
        "fields": {
            "deadline": {
                "code": "2027-06-01",
                "value": "Fall 2027 application deadline is June 1, 2027, with an Application Priority Deadline of January 15, 2027 (applications opened September 1, 2026; complete applications are reviewed as received).",
                "quote": "Fall 2027 | 09/01/2026 | 01/15/2027 | 06/01/2027",
                "url": "https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DCOS_IDS",
                "time_sensitive": "2027-01-15",
            },
            "gre_general": {
                "code": "Not required",
                "value": "2026-2027 Graduate Catalogue explicitly states no standardized test scores (including GRE) are required for admission.",
                "quote": "No test scores are required.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16886",
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "No GRE Subject Test exists for coastal/ocean/environmental/earth sciences (ETS offers Subject Tests only in Mathematics, Physics, and Psychology).",
                "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
                "url": "https://www.ets.org/gre/score-users/about/subject-tests.html",
            },
            "supervisor": {
                "code": "Recommended",
                "value": "Applicants should make initial contact with prospective faculty mentors across CMS-participating departments prior to applying.",
                "quote": "Potential UNCW Faculty Mentor(s): Applicants should make initial contact with prospective faculty mentors prior to applying. Please contact the graduate program coordinator if you need assistance with this process.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16886",
                "also": [
                    {
                        "quote": "It is best to make initial contact with prospective faculty mentors prior to applying.",
                        "url": "https://www.uncw.edu/academics/majors-programs/cms/applied-coastal-ocean-sciences-phd/details/index.html",
                    }
                ],
            },
            "funding": {
                "code": "Competitive",
                "value": "No automatic program-wide stipend is published; Ph.D. students compete for faculty-funded Graduate Research Assistantships (which cover both NC Resident and Non-Resident tuition plus monthly stipend per Graduate School policy), departmental Teaching Assistantships, and Graduate School fellowships (e.g., Ahuja Academy of Water Quality Fellowship, New Scholar Award).",
                "quote": "Graduate Research Assistants receive tuition support in addition to their monthly stipend. Students enrolled in master's programs will receive the equivalent of the NC Resident (In-State) portion of their tuition, while students enrolled in doctoral programs will receive both the NC Resident and NC Non-Resident portions of their tuition.",
                "url": "https://www.uncw.edu/myUNCW/academics/graduate-school/students/assistantships.html",
                "also": [
                    {
                        "quote": "A limited number of scholarships are available to students entering any of UNCW's graduate programs for the first time. Students do not apply for these scholarships. Instead, nominations originate with the departments, which submit their recommendations to the dean of the Graduate School.",
                        "url": "https://www.uncw.edu/academics/graduate-school/prospective-students/financial/scholarships-fellowships.html",
                    }
                ],
            },
            "entry_route": {
                "code": "Either",
                "value": "Open to STEM BA/BS (60-credit track) and MA/MS (40-credit track) graduates; bachelor's-only applicants upload a document stating 'No master's thesis', though the Program Details page notes successful applicants usually hold an M.S. in science or engineering.",
                "quote": "Total credits required: | 60 post-baccalaureate degree | 40 post-master’s degree | Target audience: STEM graduates (BA/BS/MA/MS) with an interest in the application of ocean science to issues of societal relevance and potential application beyond academia.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16886",
                "also": [
                    {
                        "quote": "Successful program applicants have a master's degree in science or engineering with an interest in applying their knowledge of marine science to real-world issues.",
                        "url": "https://www.uncw.edu/academics/majors-programs/cms/applied-coastal-ocean-sciences-phd/details/index.html",
                    }
                ],
            },
        },
        "notes": "DHS STEM-designated Ph.D. (CIP 30.3201 Marine Sciences) hosted at UNCW's Center for Marine Science (CMS), spanning faculty across Biology & Marine Biology, Chemistry & Biochemistry, Earth & Ocean Sciences, Environmental Sciences, and Physics & Physical Oceanography.",
    },
    {
        "id": "uncw--biology",
        "university": "uncw",
        "field": "biology",
        "also_fields": [],
        "name": "Integrative, Comparative and Marine Biology, Ph.D.",
        "department": "Department of Biology and Marine Biology",
        "program_page": "https://www.uncw.edu/academics/majors-programs/cse/integrative-comparative-marine-biology-phd/index.html",
        "checked": "2026-11-14",
        "fields": {
            "deadline": {
                "code": "2027-02-01",
                "value": "Fall 2027 application deadline is February 1, 2027 (Spring 2027: November 1, 2026; Summer 2027 Sessions 1 & 2: February 1, 2027). Teaching assistantship applications are due February 15.",
                "quote": "Fall 2027 | 09/01/2026 | 02/01/2027",
                "url": "https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DIMB_BIO",
                "time_sensitive": "2027-02-15",
                "also": [
                    {
                        "quote": "The deadline for applying, if you wish to have a teaching assistantship, is February 15.",
                        "url": "https://www.uncw.edu/academics/colleges/cse/departments/biology/graduate.html",
                    }
                ],
            },
            "gre_general": {
                "code": "Not required",
                "value": "GRE General Test is not required for admission to the Ph.D. in Integrative, Comparative and Marine Biology.",
                "quote": "NOTE: The Graduate Record of Examination (GRE) General Test is not required for admission.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16798",
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "No GRE Subject Test exists for Biology (ETS discontinued the GRE Biology Test in May 2021; department FAQ also states the Biology subject GRE is not required).",
                "quote": "The GRE Biology Test and the GRE Literature in English Test were discontinued in May 2021.",
                "url": "https://www.ets.org/gre/test-takers/subject-tests/scores.html",
                "also": [
                    {
                        "quote": "The Biology subject GRE is not required.",
                        "url": "https://www.uncw.edu/academics/colleges/cse/departments/biology/graduate.html",
                    }
                ],
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants must contact prospective faculty and secure acceptance/sponsorship into a faculty advisor's research group to be admitted.",
                "quote": "The applicant must secure a position in a faculty advisor’s research group in order to be admitted into the program.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16798",
                "also": [
                    {
                        "quote": "Students who are not selected by a faculty member for a position in their lab will not be accepted into the program.",
                        "url": "https://www.uncw.edu/academics/colleges/cse/departments/biology/graduate.html",
                    }
                ],
            },
            "funding": {
                "code": "Competitive",
                "value": "Department offers competitive Teaching Assistantships ($21,000 for the 9-month academic year paid over 10 months, normally renewed for 4 years with satisfactory performance, Feb 15 request deadline) and faculty-grant Research Assistantships (doctoral GRAs receive full NC Resident + Non-Resident tuition support per Graduate School policy), subject to funding availability.",
                "quote": "The Department of Biology and Marine Biology offers teaching assistantships to students enrolled in the Biology Master's and Marine Biology Master's and Ph.D. programs based on the continued availability of funding. | Teaching assistantships are currently valued at $13,000 for the 9-month academic year for Master's students and $21,000 for the 9-month academic year for Ph.D. students but are paid over 10 months.",
                "url": "https://www.uncw.edu/academics/colleges/cse/departments/biology/graduate.html",
                "also": [
                    {
                        "quote": "Teaching assistantships are awarded for one academic year. Master's students may normally expect to be continued for a second year and Ph.D. students for four years if performance is satisfactory.",
                        "url": "https://www.uncw.edu/myUNCW/academics/colleges/cse/departments/biology/student-resources/graduate.html",
                    },
                    {
                        "quote": "Graduate Research Assistants receive tuition support in addition to their monthly stipend. Students enrolled in master's programs will receive the equivalent of the NC Resident (In-State) portion of their tuition, while students enrolled in doctoral programs will receive both the NC Resident and NC Non-Resident portions of their tuition.",
                        "url": "https://www.uncw.edu/myUNCW/academics/graduate-school/students/assistantships.html",
                    },
                ],
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Admits applicants directly with a four-year bachelor's degree in biology or related discipline (>= 3.0 GPA, 60 post-baccalaureate credit hours); prior M.S. holders may count up to 30 credit hours toward the doctorate.",
                "quote": "A bachelor’s degree in biology or a related discipline from an accredited U.S. college or university or its equivalent at an international institution based on a four-year program. | Degree Requirements (60 post-baccalaureate credit hours) | The maximum amount of credit that a Ph.D. student may count toward a doctorate from a master’s degree program is 30 credit hours.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16798",
            },
        },
        "notes": "DHS STEM-designated Ph.D. (CIP 26.9999 Biological and Biomedical Sciences, Other). Teaching assistantships require IELTS 7.0 (vs 6.5 for admission) or speaking proficiency if international. Slate also notes M.S. students may apply to transition after their first year.",
    },
    {
        "id": "uncw--chemistry",
        "university": "uncw",
        "field": "chemistry",
        "also_fields": ["biomed"],
        "name": "Pharmaceutical Chemistry, Ph.D.",
        "department": "Department of Chemistry and Biochemistry",
        "program_page": "https://www.uncw.edu/academics/majors-programs/cse/pharmaceutical-chemistry-phd/index.html",
        "checked": "2026-11-14",
        "fields": {
            "deadline": {
                "code": "2027-07-01",
                "value": "Fall 2027 final application deadline is July 1, 2027, with an Application Priority Deadline of January 1, 2027; complete applications are reviewed as a group after the priority deadline.",
                "quote": "Complete applications are reviewed for admission by the program as a group after the priority deadline. | Fall 2027 | 09/01/2026 | 01/01/2027 | 07/01/2027",
                "url": "https://gradapply.uncw.edu/portal/apply?cmd=prog_details&program=SE_PHD_DPCH_CHEM",
                "time_sensitive": "2027-01-01",
            },
            "gre_general": {
                "code": "Not stated",
                "value": "Neither the 2026-2027 Graduate Catalogue nor the Slate application portal lists a GRE score requirement for Pharmaceutical Chemistry Ph.D. admission (removing an earlier catalog edition's 65th/75th percentile GRE threshold), though no explicit 'GRE not required' statement is printed.",
                "quote": "",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16891",
            },
            "gre_subject": {
                "code": "No subject test",
                "value": "No GRE Subject Test exists for Chemistry (ETS discontinued the GRE Chemistry Test in May 2023).",
                "quote": "The GRE Chemistry Test was discontinued in May 2023.",
                "url": "https://www.ets.org/gre/test-takers/subject-tests/scores.html",
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Neither the 2026-2027 Graduate Catalogue nor the Slate portal states whether securing a faculty research advisor prior to admission is required (Slate advises contacting the graduate program coordinator before applying to confirm eligibility).",
                "quote": "",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16891",
            },
            "funding": {
                "code": "Competitive",
                "value": "Funding is available competitively via dedicated donor-supported Research Assistantships and named doctoral fellowships (Sayed, Maravai LifeSciences, Alcami Corporation Leadership Fellowships), departmental lab Teaching Assistantships, and Graduate School doctoral GRA tuition support (NC Resident + Non-Resident tuition) plus monthly stipend.",
                "quote": "Three students have been awarded fellowships in the UNCW Department of Chemistry and Biochemistry’s pharmaceutical chemistry doctoral program. | “We are grateful to the donors for their support in funding dedicated research assistantships that provide advanced training opportunities.”",
                "url": "https://www.uncw.edu/news/academic-affairs/cse/2026/02/uncw-students-receive-pharmaceutical-chemistry-fellowships.html",
                "also": [
                    {
                        "quote": "Graduate Research Assistants receive tuition support in addition to their monthly stipend. Students enrolled in master's programs will receive the equivalent of the NC Resident (In-State) portion of their tuition, while students enrolled in doctoral programs will receive both the NC Resident and NC Non-Resident portions of their tuition.",
                        "url": "https://www.uncw.edu/myUNCW/academics/graduate-school/students/assistantships.html",
                    },
                    {
                        "quote": "Graduate students also have many opportunities to teach undergraduate labs and mentor younger students in research, including undergraduates and new graduate students.",
                        "url": "https://www.uncw.edu/academics/colleges/cse/departments/chemistry/graduate-programs.html",
                    },
                ],
            },
            "entry_route": {
                "code": "Either",
                "value": "Three entry pathways: (1) direct post-M.S. entry (>= 3.0 GPA, 40 post-M.S. credits), (2) B.S.-to-M.S. transition (>= 3.0 GPA, applying to Ph.D. after 2 years with committee approval), or (3) direct B.S.-to-Ph.D. entry (>= 3.5 GPA and evidence of independent research, 60 post-B.S. credits).",
                "quote": "1. Students with a M.S in Chemistry or other STEM-related discipline entering directly into the Ph.D. program, or | 2. Students with a B.S. (based on a 4-year program) in Chemistry or other STEM-related discipline entering the MS in Pharmaceutical Chemistry and transitioning into the Ph.D. program, or | 3. Students with a B.S. in Chemistry or other STEM-related discipline entering directly into the Ph.D. program.",
                "url": "https://catalogue.uncw.edu/preview_program.php?catoid=82&poid=16891",
            },
        },
        "notes": "DHS STEM-designated Ph.D. (CIP 51.2004 Medicinal and Pharmaceutical Chemistry); cross-listed under biomed because drug discovery and biologics formulation span pharmaceutical chemistry and biomedical research. 2026-2027 Catalogue also states TOEFL >= 79 online / 550 paper or IELTS 6.5/7.0 (Graduate School applies 4.5 on the post-Jan 21, 2026 TOEFL 1-6 scale and exempts India). Department scholarship applications via UNCW common scholarship portal are due March 1.",
    },
]

staging_uni_dir = ROOT / "data" / "staging" / "universities"
staging_prog_dir = ROOT / "data" / "staging" / "programs"
staging_uni_dir.mkdir(parents=True, exist_ok=True)
staging_prog_dir.mkdir(parents=True, exist_ok=True)

(staging_uni_dir / "uncw.json").write_text(json.dumps(uni_rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
for prog in programs:
    (staging_prog_dir / f"{prog['id']}.json").write_text(json.dumps(prog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print("Wrote UNCW staging files successfully.")
