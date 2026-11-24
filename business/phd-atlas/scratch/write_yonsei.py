import json
import os
import sys

GUIDE_URL = "https://graduate.yonsei.ac.kr/_res/graduate/etc/s_f_guide_2027-1_e.pdf"
FALL_SCHED_URL = "https://graduate.yonsei.ac.kr/graduate_en/admission/forein_fall_schedule.do"
SPRING_SCHED_URL = "https://graduate.yonsei.ac.kr/graduate_en/admission/forein_schedule.do"
SCHOL_INTL_URL = "https://graduate.yonsei.ac.kr/graduate_en/academic/scholarship02.do"
SCHOL_ONCAMPUS_URL = "https://graduate.yonsei.ac.kr/graduate_en/academic/scholarship.do"
ETS_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"

ETS_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

uni_data = {
    "id": "yonsei",
    "institution": "Yonsei University",
    "country": "South Korea",
    "region": "Seoul",
    "grad_page": "https://graduate.yonsei.ac.kr/graduate_en/admission/forein_schedule.do",
    "checked": "2026-11-15",
    "fields": {
        "app_fee": {
            "code": "130000 KRW",
            "value": "KRW 130,000 (or USD 130 if paid via PayPal) for Master's, Ph.D., and Integrated M.S.-Ph.D. applicants on the International Student Track.",
            "quote": "Application Fee | Admission Track | Master / Ph. D / Integrated Notice | 130,000 KRW",
            "url": GUIDE_URL
        },
        "fee_waiver": {
            "code": "None",
            "value": "The Graduate School Admission Guideline for International Students states that the KRW 130,000 application fee is non-refundable once paid and does not offer an application fee waiver for international applicants.",
            "quote": "Applications CANNOT be CANCELED, REPLACED (submitted documents) or CHANGED (applying information) once paying the application fee, and the fee is non-refundable.",
            "url": GUIDE_URL
        },
        "gre_general": {
            "code": "Not stated",
            "value": "The Graduate School Admission Guideline for International Students lists required application documents and language proficiency tests without stating a GRE General requirement.",
            "quote": "",
            "url": GUIDE_URL
        },
        "toefl_min": {
            "code": "3.5 (new scale)",
            "value": "Most STEM departments require TOEFL iBT 3.5 on the post-January 21, 2026 1-6 scale (59 on the prior 0-120 scale); Electrical and Electronic Engineering, Industrial Engineering, and Medical Sciences (BK21 Project) require 4.0 (72).",
            "quote": "3) In accordance with the changes to the TOEFL iBT scoring system, applicants who took the TOEFL iBT before January 21, 2026, may submit scores that meet or exceed the minimum TOEFL score indicated in parentheses | Physics Lv. 3 O 3.5(59) 750 285 5.5 O",
            "url": GUIDE_URL
        },
        "ielts_min": {
            "code": "5.5",
            "value": "Most STEM departments require IELTS Academic 5.5 minimum; Electrical and Electronic Engineering, Industrial Engineering, and Medical Sciences (BK21 Project) require IELTS 6.0.",
            "quote": "Chemical and Biomolecular Engineering Lv. 3 O 3.5(59) 750 285 5.5 O | Electrical and Electronic Engineering Lv. 3 O 4.0(72) 750 285 6.0 O",
            "url": GUIDE_URL
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "All STEM departments permit substitution ('O') of the English proficiency test if the applicant completed all curriculum of a Bachelor's, Master's, or Ph.D. degree program in English (either in an English-speaking country or in a non-English-speaking country such as India, documented by an official certificate with the university seal).",
            "quote": "B. Submission of Substitute Documents for Language Proficiency Test (Korean/English) | - Applicants can submit the following documents for substituting Language Proficiency Test (Korean/English) results. This is only applicable if the applicant uploads the proof (PDF file) during the application process. | 2) English | A) Holders of nationality from English-speaking countries※ | B) Completion of one of ⓐ~ⓓ in English-speaking state※ [All curriculum means from the first semester of the first year to graduation.] | C) Completion of one of ⓐ~ⓒ in non-English speaking country [All curriculum means from the first semester of the first year to graduation.] | ⓐ All curriculum of Bachelor’s Degree Program ⓑ All curriculum of Master’s Degree Program | ⓒ All curriculum of Ph.D Program",
            "url": GUIDE_URL
        }
    },
    "notes": "QS WUR 2027 #42. Covers all 18 STEM PhD fields through Yonsei University Graduate School (Sinchon/Seoul Campus and Songdo International Campus). International Student Track offers two admissions cycles per year: Spring 2027 online application ran October 7-14, 2026, and Fall 2027 online application runs April 6-13, 2027. Full-time international students in non-Medical/Dental/Nursing Graduate School departments automatically receive the Yonsei International Companion Scholarship (KRW 3,000,000/semester for 4 semesters in Ph.D.; KRW 2,000,000/semester for 6 semesters in Integrated M.S.-Ph.D.) unless receiving a full-tuition scholarship; competitive full-tuition Graduate Student Assistantships, Yonsei Graduate Fellowships (up to KRW 7.5M), BK21 Four scholarships, and Global Korea Scholarships (GKS) are also available."
}

DEADLINE_FIELD = {
    "code": "2027-04-13",
    "time_sensitive": "2027-04-13",
    "value": "April 13, 2027 (17:00 KST; online application window April 6-13, 2027) for the Fall 2027 International Student Track (note: the web schedule table has a typo '2026' on row 1 alongside '2027' on rows 2-4 under '2027 Fall Admission'; Spring 2027 application closed October 14, 2026).",
    "quote": "2027 Fall Graduate School Admissions for International Students | Application Procedure | 2027 Fall Admission | 1 | Application Period | Apr. 6th (Tue) 10:00 ~ Apr. 13th(Tue) 17:00, 2026 | 2 | Notification of Interview/Performance Assessments candidates | May 10th(Mon) 17:00, 2027",
    "url": FALL_SCHED_URL,
    "also": [
        {
            "quote": "2027 Graduate School Admission for International Students | Application Procedure | 2027 Spring | 1 | Application Period | Oct. 7th (Wed) 10:00 ~ Oct. 14th (Wed) 17:00, 2026",
            "url": SPRING_SCHED_URL
        }
    ]
}

FUNDING_STD = {
    "code": "Competitive",
    "value": "Full-time international students in non-Medical/Dental/Nursing Graduate School departments automatically receive the Yonsei International Companion Scholarship (KRW 3,000,000/semester for 4 semesters in Ph.D.; KRW 2,000,000/semester for 6 semesters in Integrated M.S.-Ph.D.) unless receiving a full-tuition scholarship; full-tuition Graduate Student Assistantships, Yonsei Graduate Fellowships (up to KRW 7,500,000), and GKS scholarships are competitive.",
    "quote": "Yonsei International Companion Scholarship | Eligibility: Full-time international students enrolled in regular semesters through the international student admission track at the Graduate School | Master's Program: | KRW 2,000,000 per semester | Doctoral Program: | KRW 3,000,000 per semester | Integrated Program: | KRW 2,000,000 per semester | Regular semester | (4 semesters for master’s and PhD, | 6 semesters for integrated master’s and PhD program)",
    "url": SCHOL_INTL_URL,
    "also": [
        {
            "quote": "Scholarship Type | Qualifications | Amount of Scholarship | Graduate student assistant | Enrolled student (including new students) | Within the tuition fee range",
            "url": SCHOL_ONCAMPUS_URL
        }
    ]
}

FUNDING_MED = {
    "code": "Competitive",
    "value": "Students in the College of Medicine are ineligible for the Yonsei International Companion Scholarship, but are eligible for competitive Graduate Student Assistantships (within the tuition fee range), Yonsei Graduate Fellowships (research incentives up to KRW 7.5 million), BK21 Four Medical Sciences scholarships, and GKS full-tuition plus living-stipend scholarships.",
    "quote": "Scholarship Type | Qualifications | Amount of Scholarship | Graduate student assistant | Enrolled student (including new students) | Within the tuition fee range | YGF | (Yonsei Graduate Fellowship) | Outstanding students pursuing PhD or integrated master’s and PhD degrees | (up to the third semester for PhD and the fifth semester for integrated degrees) | Research incentives up to KRW 7.5 million",
    "url": SCHOL_ONCAMPUS_URL,
    "also": [
        {
            "quote": "Yonsei International Companion Scholarship | Eligibility: Full-time international students enrolled in regular semesters through the international student admission track at the Graduate School | Ineligible | 1. Students receiving full tuition scholarships(from Graduate School) for regular semesters | 2. Students in the College of Medicine, College of Dentistry, or College of Nursing",
            "url": SCHOL_INTL_URL
        }
    ]
}

SUPERVISOR_STD = {
    "code": "Not stated",
    "value": "The Graduate School Admission Guideline for International Students only requires pre-application advisor selection in the application/study plan for Psychology, Cognitive Science, and Integrated Design, and does not state a pre-application supervisor requirement for this department.",
    "quote": "",
    "url": GUIDE_URL
}

ENTRY_ELIG_QUOTE = "1. Eligibility for All Applicants | Master / Integrated Ph. D | w Someone who (will) be awarded a Bachelor’s Degree w Someone who (will) be awarded a Master’s Degree"

PROGRAMS = [
    {
        "field": "math",
        "name": "Mathematics, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Science — School of Mathematics and Computing (Department of Mathematics)",
        "program_page": "https://math.yonsei.ac.kr/math/index.do",
        "entry_quote": "Mathematics and Computing ○ ○ ○ Mathematics, Computational Science and Engineering",
        "gre_subj": {
            "code": "Not stated",
            "value": "Neither the Graduate School International Admission Guideline nor the Department of Mathematics specifies a GRE Mathematics Subject Test requirement.",
            "quote": "",
            "url": GUIDE_URL
        },
        "notes": "School of Mathematics and Computing offers both Mathematics and Computational Science & Engineering majors at the graduate level (BK21 Four Yonsei Mathematical Sciences and Computation)."
    },
    {
        "field": "statistics",
        "name": "Statistics and Data Science, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Commerce and Economics — Department of Statistics and Data Science",
        "program_page": "https://stat.yonsei.ac.kr/stat_en/index.do",
        "entry_quote": "Econo-mi Statistics and Data Science ○ ○ ○ [Master] Statistics, Data Science Ph.D., Integrated: No sub",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Statistics and Data Science.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Housed in the College of Commerce and Economics (BK21 Four Big Data program); covers theoretical and applied statistics, biostatistics, econometrics, and data science."
    },
    {
        "field": "physics",
        "name": "Physics, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Science — Department of Physics",
        "program_page": "https://phys.yonsei.ac.kr/ymphys/index.do",
        "entry_quote": "Physics ○ ○ ○ | Science | Chemistry ○ ○ ○",
        "gre_subj": {
            "code": "Not stated",
            "value": "Neither the Graduate School International Admission Guideline nor the College of Science graduate physics program specifies a GRE Physics Subject Test requirement.",
            "quote": "",
            "url": GUIDE_URL
        },
        "notes": "The Physics Graduate School (TPGS) hosts the BK21 Four Yonsei Physics Education and Research Institute (YPERI), Surface Science SRC, Van der Waals Physics SRC, and Nanomedical CRC."
    },
    {
        "field": "chemistry",
        "name": "Chemistry, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Science — Department of Chemistry",
        "program_page": "https://chem.yonsei.ac.kr/greeting",
        "entry_quote": "Physics ○ ○ ○ | Science | Chemistry ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (the GRE Chemistry Subject Test was discontinued).",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Hosts the BK21 Four Chemistry Education Center for Sustainability across physical, organic, inorganic, analytical, and biological/materials chemistry."
    },
    {
        "field": "earth",
        "name": "Earth System Sciences, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Science — School of Earth, Astronomy, and Atmospheric Sciences (Earth System Sciences / Atmospheric Sciences)",
        "program_page": "https://geo.yonsei.ac.kr/en",
        "entry_quote": "Earth System Sciences, Atmospheric Sciences, | Earth System Sciences ○ ○ ○ Astronomy",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Earth System or Atmospheric Sciences.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Covers both Earth System Sciences (geology, geophysics, hydrogeology, oceanography) and Atmospheric Sciences under the School of Earth, Astronomy, and Atmospheric Sciences."
    },
    {
        "field": "astronomy",
        "name": "Astronomy, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Science — School of Earth, Astronomy, and Atmospheric Sciences (Department of Astronomy)",
        "program_page": "https://astro.yonsei.ac.kr/galaxy_en/index.do",
        "entry_quote": "Earth System Sciences, Atmospheric Sciences, | Earth System Sciences ○ ○ ○ Astronomy",
        "gre_subj": {
            "code": "Not stated",
            "value": "Neither the Graduate School International Admission Guideline nor the Department of Astronomy specifies a GRE Physics Subject Test requirement.",
            "quote": "",
            "url": GUIDE_URL
        },
        "notes": "Admitted under Earth System Sciences (Astronomy) in the Graduate School; research groups include galaxy evolution, observational cosmology, stellar populations, astrodynamics, and gravitational lensing."
    },
    {
        "field": "chemeng",
        "name": "Chemical and Biomolecular Engineering, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Engineering — Department of Chemical and Biomolecular Engineering",
        "program_page": "https://engineering.yonsei.ac.kr/engineering_en/about/major_1_1.do",
        "entry_quote": "Chemical and Biomolecular Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Chemical and Biomolecular Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Research spans catalysis and reaction engineering, secondary batteries and energy storage, semiconductor materials/processes, polymers, and biomolecular engineering."
    },
    {
        "field": "ece",
        "name": "Electrical and Electronic Engineering, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Engineering — School of Electrical and Electronic Engineering",
        "program_page": "https://ee.yonsei.ac.kr/ee_en/index.do",
        "entry_quote": "Electrical and Electronic Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Electrical and Electronic Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Note higher departmental English proficiency requirement on the International Student Track: TOEFL iBT 4.0 (72 on pre-January 2026 scale) or IELTS 6.0, or TOPIK Level 3."
    },
    {
        "field": "civil",
        "name": "Civil and Environmental Engineering, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Engineering — Department of Civil and Environmental Engineering",
        "program_page": "https://civil.yonsei.ac.kr/civil_en/",
        "entry_quote": "ering Civil and Environmental Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Civil and Environmental Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Covers Infrastructure Systems (structural, geotechnical, construction materials), Water and Environmental Systems, and Information and Management Systems (geospatial/GIS, smart city infrastructure)."
    },
    {
        "field": "environment",
        "name": "Civil and Environmental Engineering (Environmental Engineering / Climate Change Energy Engineering), Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Engineering — Department of Civil and Environmental Engineering (Water and Environmental Systems)",
        "program_page": "https://engineering.yonsei.ac.kr/engineering_en/about/major_5_1.do",
        "entry_quote": "ering Civil and Environmental Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Environmental Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Seoul Campus offers environmental and water-resources doctoral training within the Department of Civil and Environmental Engineering and the Interdisciplinary Program in Climate Change Energy Engineering (Mirae Campus also houses a separate Department of Environmental Engineering)."
    },
    {
        "field": "mech",
        "name": "Mechanical Engineering, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Engineering — School of Mechanical Engineering",
        "program_page": "https://me.yonsei.ac.kr/en",
        "entry_quote": "Mechanical Engineering ○ ○ ○ | Materials Science and Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Mechanical Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Research divisions span mechanics and materials, design and manufacturing, robotics and control, thermo-fluids and energy, micro/nano engineering, and bio-photonics."
    },
    {
        "field": "materials",
        "name": "Materials Science and Engineering, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Engineering — Department of Materials Science and Engineering",
        "program_page": "https://mse.yonsei.ac.kr/mse/index.do",
        "entry_quote": "Mechanical Engineering ○ ○ ○ | Materials Science and Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Materials Science and Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Research clusters include Energy & Sustainability, Health & Medicine, Electronics/Optics/Photonics, Structural Materials & Robotics, and Computation/Theory/AI."
    },
    {
        "field": "biology",
        "name": "Life Sciences (Systems Biology / Biochemistry / Biotechnology), Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Life Science and Biotechnology — Department of Systems Biology / Biochemistry / Biotechnology",
        "program_page": "https://systemsbiology.yonsei.ac.kr/l_system/index.do",
        "entry_quote": "Life Sciences ○ ○ ○ Systems Biology, Biochemistry, Biotechnology",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (the GRE Biology and Biochemistry Subject Tests were discontinued).",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "College of Life Science and Biotechnology admits doctoral and integrated M.S.-Ph.D. students into Life Sciences (Systems Biology), Life Sciences (Biochemistry), Life Sciences (Biotechnology), and Interdisciplinary Integrated OMICS for Biomedical Science."
    },
    {
        "field": "cs",
        "name": "Computer Science, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Computing — Department of Computer Science",
        "program_page": "https://cs.yonsei.ac.kr/csai_en/index.do",
        "entry_quote": "Compu- Computer Science ○ ○ ○ | ting Artificial Intelligence ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (the GRE Computer Science Subject Test was discontinued).",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "Housed in the College of Computing; research labs cover computer systems, networking, cloud computing, databases/data engineering, theory, computer graphics, HCI, computer vision, NLP, and machine learning."
    },
    {
        "field": "datasci",
        "name": "Artificial Intelligence / Digital Analytics, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Computing — Department of Artificial Intelligence & Interdisciplinary Program in Digital Analytics",
        "program_page": "https://ai.yonsei.ac.kr/csai_en/index.do",
        "entry_quote": "Compu- Computer Science ○ ○ ○ | ting Artificial Intelligence ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Artificial Intelligence or Data Science.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "notes": "College of Computing offers both the Department of Artificial Intelligence (AI Graduate School Program / BK21 Four AI) and the Interdisciplinary Graduate Program in Digital Analytics."
    },
    {
        "field": "biomed",
        "name": "Medical Sciences (BK21 Project) / Medicine, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "College of Medicine — Department of Medical Sciences (BK21 Project) & Department of Medicine",
        "program_page": "https://medicine.yonsei.ac.kr/medicine/education/graduate/medical.do",
        "entry_quote": "Medicine ○ ○ ○ Neurosurgery, Orthopedic Surgery, Biomedical Science",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Medical Sciences.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "funding": FUNDING_MED,
        "notes": "Medical Sciences (BK21 Project) comprises five tracks (Molecular, Cellular & Cancer Biology; Infectious Diseases & Immunobiology; Genomics & Data Sciences; Brain & Cognitive Sciences; Regenerative Biology & Translational Medicine) and requires TOEFL iBT 4.0 (72) or IELTS 6.0."
    },
    {
        "field": "neuro",
        "name": "Cognitive Science / Brain and Cognitive Sciences, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "Interdisciplinary Graduate Program in Cognitive Science / Department of Medical Sciences (Brain & Cognitive Sciences)",
        "program_page": "https://cogsci.yonsei.ac.kr/",
        "entry_quote": "Cognitive Science ○ ○ ○ advisor down in the application and study plan",
        "gre_subj": {
            "code": "Not stated",
            "value": "Neither the Graduate School International Admission Guideline nor the Interdisciplinary Program in Cognitive Science specifies a GRE Subject Test requirement.",
            "quote": "",
            "url": GUIDE_URL
        },
        "supervisor": {
            "code": "Required",
            "value": "Applicants to the Interdisciplinary Graduate Program in Cognitive Science must check the department website for academic advisors and write the name of an intended advisor in the application and study plan.",
            "quote": "Check the website \"http://cogsci.yonsei.ac.kr\" for | academic advisors and write the name of an intended | Cognitive Science ○ ○ ○ advisor down in the application and study plan",
            "url": GUIDE_URL
        },
        "notes": "Cognitive Science accepts TOPIK Level 3, TOEFL iBT 3.5 (59), or IELTS 5.5, and requires naming an intended advisor in the application and study plan. Neuroscience is also offered via the Brain and Cognitive Sciences track in Medical Sciences (BK21 Project)."
    },
    {
        "field": "bme",
        "name": "Nano Biomedical Engineering / Biomedical Engineering, Ph.D. / Integrated M.S.-Ph.D.",
        "department": "Department of Nano Biomedical Engineering (IBS Center for Nanomedicine) & Interdisciplinary Program in Biomedical Engineering",
        "program_page": "https://ibs.yonsei.ac.kr/program.asp?mid=m05_01",
        "entry_quote": "Science Nano Biomedical Engineering ○ ○ ○",
        "gre_subj": {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for Biomedical Engineering.",
            "quote": ETS_QUOTE,
            "url": ETS_URL
        },
        "funding": {
            "code": "Guaranteed",
            "value": "Students in the Department of Nano Biomedical Engineering receive financial support equivalent to Yonsei University tuition and a monthly stipend through IBS Center for Nanomedicine research funding, plus additional doctoral scholarship support.",
            "quote": "Financial support: Students receive financial support equivalent to Yonsei University tuition and a monthly stipend through IBS research funding. Ph.D. and Integrated M.S.-Ph.D. students may also receive additional doctoral scholarship support in accordance with university regulations.",
            "url": "https://ibs.yonsei.ac.kr/program.asp?mid=m05_04"
        },
        "notes": "Yonsei offers Ph.D. and Integrated M.S.-Ph.D. degrees in Nano Biomedical Engineering (supported by the IBS Center for Nanomedicine with full tuition and monthly stipend) as well as the Interdisciplinary Program in Biomedical Engineering in the College of Medicine."
    }
]


def main():
    os.makedirs("data/staging/universities", exist_ok=True)
    os.makedirs("data/staging/programs", exist_ok=True)

    with open("data/staging/universities/yonsei.json", "w", encoding="utf-8") as f:
        json.dump(uni_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    for spec in PROGRAMS:
        fid = spec["field"]
        pid = f"yonsei--{fid}"
        pobj = {
            "id": pid,
            "university": "yonsei",
            "field": fid,
            "also_fields": [],
            "name": spec["name"],
            "department": spec["department"],
            "program_page": spec["program_page"],
            "checked": "2026-11-15",
            "fields": {
                "deadline": DEADLINE_FIELD,
                "gre_subject": spec["gre_subj"],
                "supervisor": spec.get("supervisor", SUPERVISOR_STD),
                "funding": spec.get("funding", FUNDING_STD),
                "entry_route": {
                    "code": "Either",
                    "value": "Yonsei University Graduate School offers both the Integrated Master's-Ph.D. Program (open to applicants holding a Bachelor's degree) and the Ph.D. Program (open to applicants holding a Master's degree) in this department.",
                    "quote": f"{ENTRY_ELIG_QUOTE} | {spec['entry_quote']}",
                    "url": GUIDE_URL
                }
            },
            "notes": spec["notes"]
        }
        path = f"data/staging/programs/{pid}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(pobj, f, indent=2, ensure_ascii=False)
            f.write("\n")

    print(f"Wrote yonsei.json and {len(PROGRAMS)} programs to data/staging/")


if __name__ == "__main__":
    main()
