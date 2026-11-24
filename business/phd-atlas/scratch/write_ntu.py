import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING_UNI = ROOT / "data" / "staging" / "universities"
STAGING_PROG = ROOT / "data" / "staging" / "programs"
STAGING_UNI.mkdir(parents=True, exist_ok=True)
STAGING_PROG.mkdir(parents=True, exist_ok=True)

CHECKED = "2026-11-24"

URL_INTL = "https://admissions.ntu.edu.tw/apply/degree-students/international-students/"
URL_GUIDE = "https://admissions.ntu.edu.tw/wp-content/uploads/116-1Admission-Guidelines-for-Intl-Degree-Students_ENG_V3.pdf"
URL_LANG = "https://admissions.ntu.edu.tw/apply/degree-students/admission-information/language-proficiency-requirements/"
URL_SCHOL = "https://admissions.ntu.edu.tw/fees-scholarships/scholarships/"
URL_MATH = "https://oiasystem.ntu.edu.tw/globaladmission/foreign/requirement/dept.detail/id/MCF9BXADkkHV/degree_key/D/sn/9855?lang=en"
URL_ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"

uni_data = {
    "id": "ntu",
    "institution": "National Taiwan University",
    "country": "Taiwan",
    "region": "Taipei",
    "grad_page": URL_INTL,
    "checked": CHECKED,
    "fields": {
        "app_fee": {
            "code": "2000 TWD",
            "value": "Regular application fee is NTD 2,000 (or USD 80 for international payments) per department/graduate institute/division; NTD 1,500 (USD 60) per additional application from the third application onward, or for prior NTU students.",
            "quote": "The regular fee is NTD 2,000 or USD 80 per department/graduate institute/division. Where an applicant applies for three or more departments/graduate institutes/divisions, the fee is NTD 1,500 or USD 60 per additional application from the third application onwards.",
            "url": URL_GUIDE,
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "NTU's 2027/2028 September Entry Admission Guidelines state that application fees are non-refundable under any circumstances and unpaid applications will not be processed; discounts apply for 3+ applications or prior NTU students, with no fee waiver stated.",
            "quote": "",
            "url": URL_GUIDE,
        },
        "gre_general": {
            "code": "Not stated",
            "value": "NTU's 2027/2028 September Entry Admission Guidelines do not state a university-wide GRE General requirement; individual programs specify whether GRE is optional (e.g., TIGP Interdisciplinary Neuroscience).",
            "quote": "",
            "url": URL_GUIDE,
        },
        "toefl_min": {
            "code": "4 (new scale)",
            "value": "English-taught programs require CEFR B2 or above: TOEFL iBT 4 or above on the post-January 2026 new scoring scale (or TOEFL iBT 72 or above on the prior 0-120 scale). Some departments recommend CEFR C1.",
            "quote": "TOEFL (iBT) 72 or above | TOEFL iBT (New Scoring Scale) 4 or above",
            "url": URL_MATH,
            "also": [
                {
                    "quote": "If you are applying for a program that is conducted in English, you will need to submit an English proficiency certificate at CEFR B2 (Vantage) or above. | TOEFL iBT: 72",
                    "url": URL_LANG,
                }
            ],
        },
        "ielts_min": {
            "code": "5.5",
            "value": "English-taught programs require CEFR B2 or above: IELTS Academic 5.5 or above.",
            "quote": "If you are applying for a program that is conducted in English, you will need to submit an English proficiency certificate at CEFR B2 (Vantage) or above. | IELTS (Academic): 5.5",
            "url": URL_LANG,
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exempt from submitting an English proficiency certificate if the applicant is from an English-speaking country, or obtained their previous degree from an institution in an English-speaking country or conducted entirely in English (official proof required).",
            "quote": "Applicants from one of the English-speaking countries may be exempt from the English language proficiency requirement. Applicants whose previous degree was obtained from an institution in an English-speaking country or conducted in English shall submit relevant proof in place of an English proficiency certificate.",
            "url": URL_GUIDE,
        },
    },
    "notes": "QS WUR 2027 #54. Covers 17 STEM PhD programs spanning all 18 Atlas fields (Statistics is covered via also_fields on Department of Mathematics, as NTU's Institute of Statistics and Data Science and Master Program in Statistics are Master's-only). For 2027/2028 September Entry, Round 1 ran September 29 to November 19, 2026 and Round 2 runs December 1, 2026 to January 28, 2027 (4pm GMT+8); PhD programs require a Master's degree (except Graduate School of Advanced Technology direct-entry doctoral tracks). Competitive funding includes NTU International Graduate Student Scholarships (applied for via checkbox in the online application), college/department fellowships (e.g., EECS Global Elite Cultivation Fellowship at NT$20,000/month for up to 4 years; College of Medicine International Student Scholarship; Academia Sinica TIGP Scholarship), and Taiwan MOE/MOFA Scholarships.",
}

(STAGING_UNI / "ntu.json").write_text(
    json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)

BASE_DETAIL = "https://oiasystem.ntu.edu.tw/globaladmission/foreign/requirement/dept.detail/id/MCF9BXADkkHV/degree_key/D/sn/{}?lang=en"

PROGRAMS = [
    {
        "field": "astronomy",
        "also_fields": [],
        "sn": 9917,
        "name": "Astrophysics, Ph.D.",
        "department": "College of Science — Institute of Astrophysics",
        "supervisor": {
            "code": "Recommended",
            "value": "Institute of Astrophysics advises applicants to confirm a dissertation advisor before submitting their application, and notes that scholarship applications require the cooperation of the dissertation advisor.",
            "quote": "1. Applicants are advised to confirm a dissertation advisor before submitting their application. | 2. Scholarship applications require the cooperation of the dissertation advisor.",
        },
        "notes": "English-taught PhD program in the Institute of Astrophysics (College of Science; 18 graduation credits). Open in both Round 1 (Nov 19, 2026) and Round 2 (Jan 28, 2027) for 2027 September Entry.",
    },
    {
        "field": "biology",
        "also_fields": [],
        "sn": 10309,
        "name": "Life Science, Ph.D.",
        "department": "College of Life Science — Department of Life Science",
        "supervisor": {
            "code": "Recommended",
            "value": "The Department of Life Science Admission Committee strongly suggests contacting potential supervisor(s) to discuss a study plan before the application deadline.",
            "quote": "The Admission Committee strongly suggests you contact the department's potential supervisor(s) to discuss your study plan before application deadline.",
        },
        "notes": "English-taught PhD program in the Department of Life Science (College of Life Science). Companion PhD institutes in the College of Life Science include Molecular and Cellular Biology, Plant Biology, Ecology and Evolutionary Biology, Biochemical Sciences, and Genome and Systems Biology.",
    },
    {
        "field": "biomed",
        "also_fields": [],
        "sn": 10015,
        "name": "Molecular Medicine, Ph.D.",
        "department": "College of Medicine — Institute of Molecular Medicine",
        "fund_also_quote": "Name : National Taiwan University College of Medicine Regulations Governing Scholarship for International Students",
        "notes": "English-taught PhD program in the Institute of Molecular Medicine (College of Medicine); shortlisted candidates complete an in-person or online Webex interview. Companion College of Medicine PhD institutes include Biochemistry & Molecular Biology, Physiology, Pharmacology, Pathology, Microbiology, Immunology, Oncology, and Medical Genomics & Proteomics.",
    },
    {
        "field": "bme",
        "also_fields": [],
        "sn": 10391,
        "name": "Biomedical Engineering, Ph.D.",
        "department": "College of Engineering — Department of Biomedical Engineering",
        "notes": "English-taught PhD program in the Department of Biomedical Engineering (College of Engineering). Companion biomedical engineering/imaging PhD programs include the Institute of Medical Device and Imaging (College of Medicine) and Graduate Institute of Biomedical Electronics and Bioinformatics (College of EECS).",
    },
    {
        "field": "chemeng",
        "also_fields": [],
        "sn": 10087,
        "name": "Chemical Engineering, Ph.D.",
        "department": "College of Engineering — Department of Chemical Engineering",
        "notes": "English-taught PhD program in the Department of Chemical Engineering (College of Engineering). Companion PhD institutes include Polymer Science and Engineering and TIGP Sustainable Chemical Science and Technology.",
    },
    {
        "field": "chemistry",
        "also_fields": [],
        "sn": 9869,
        "name": "Chemistry, Ph.D. (Chemistry Division)",
        "department": "College of Science — Department of Chemistry",
        "notes": "English-taught PhD program in the Department of Chemistry (Chemistry Division; Chemical Biology Division is also offered under `sn/9871`). Note: department page still lists the discontinued GRE Chemistry Subject Test as an optional document ('if applicable'); department recommends CEFR C1 English alongside the university CEFR B2 minimum.",
    },
    {
        "field": "civil",
        "also_fields": [],
        "sn": 10041,
        "name": "Civil Engineering, Ph.D. (Structural Engineering Division)",
        "department": "College of Engineering — Department of Civil Engineering",
        "supervisor": {
            "code": "Recommended",
            "value": "Department notes that while advisor confirmation is not required to apply, applicants are encouraged to contact professors they are interested in working with prior to applying.",
            "quote": "Although you do not need an advisor's confirmation to apply to NTU, you are encouraged to contact professors whom you are genuinely interested in working with",
        },
        "notes": "English-taught PhD program in the Department of Civil Engineering across eight divisions: Structural Engineering (`sn/10041`), Geotechnical (`sn/10037`), Hydraulic (`sn/10045`), Transportation (`sn/10049`), Construction Engineering & Management (`sn/10053`), Computer-Aided Engineering (`sn/10057`), Surveying & Geospatial (`sn/10061`), and AI for Engineering Applications (`sn/10063`).",
    },
    {
        "field": "cs",
        "also_fields": [],
        "sn": 10273,
        "name": "Computer Science and Information Engineering, Ph.D.",
        "department": "College of Electrical Engineering and Computer Science — Department of Computer Science and Information Engineering",
        "fund_also_quote": "EECS Global Elite Cultivation Fellowship Application form ( if applicable)",
        "notes": "PhD in Computer Science and Information Engineering (sufficient English-taught courses to meet the 18-credit graduation requirement; department recommends CEFR C1 English and requests Chinese proficiency proof or a 500-word study plan for Chinese). Eligible for the EECS Global Elite Cultivation Fellowship (NT$20,000/month up to 4 years). Companion EECS PhD institute: Graduate Institute of Networking and Multimedia.",
    },
    {
        "field": "datasci",
        "also_fields": [],
        "sn": 10397,
        "name": "Data Science Degree Program, Ph.D.",
        "department": "College of Electrical Engineering and Computer Science — Data Science Degree Program",
        "fund_also_quote": "Name : EECS Global Elite Cultivation Fellowship",
        "notes": "Interdisciplinary PhD jointly drawing on EECS, Mathematics, and Applied Mathematical Sciences (18 graduation credits; listed as a Chinese-taught program requiring CEFR A2 Chinese and recommending CEFR C1 English, with sufficient English-taught electives). Applicants list 2-3 faculty members of interest in their Statement of Purpose and may apply for the EECS Global Elite Cultivation Fellowship.",
    },
    {
        "field": "earth",
        "also_fields": [],
        "sn": 9879,
        "name": "Geosciences, Ph.D.",
        "department": "College of Science — Department of Geosciences",
        "notes": "English-taught PhD program in the Department of Geosciences (College of Science; 18 graduation credits; open in Round 2 closing January 28, 2027). Companion College of Science PhD units include Atmospheric Sciences, Institute of Oceanography, and TIGP Earth System Science.",
    },
    {
        "field": "ece",
        "also_fields": [],
        "sn": 10269,
        "name": "Electrical Engineering, Ph.D.",
        "department": "College of Electrical Engineering and Computer Science — Department of Electrical Engineering",
        "fund_also_quote": "2. Doctoral Students: The maximum funding period is four years, with a monthly stipend of NT$20,000.",
        "notes": "English-taught PhD program in the Department of Electrical Engineering covering 11 research areas; applicants specify one of three area tracks in their Statement of Purpose and may apply for the EECS Global Elite Cultivation Fellowship (NT$20,000/month for up to 4 years). Companion EECS PhD institutes include Electronics Engineering, Communication Engineering, and Photonics & Optoelectronics.",
    },
    {
        "field": "environment",
        "also_fields": [],
        "sn": 10105,
        "name": "Environmental Engineering, Ph.D.",
        "department": "College of Engineering — Graduate Institute of Environmental Engineering",
        "notes": "English-taught PhD program in the Graduate Institute of Environmental Engineering (College of Engineering). Companion environmental PhD programs include the International Doctoral Degree Program in Climate Change and Sustainable Development (College of Science) and Environmental & Occupational Health Sciences (College of Public Health).",
    },
    {
        "field": "materials",
        "also_fields": [],
        "sn": 10099,
        "name": "Materials Science and Engineering, Ph.D.",
        "department": "College of Engineering — Department of Materials Science and Engineering",
        "notes": "English-taught PhD program in the Department of Materials Science and Engineering (College of Engineering). Companion programs include the Graduate School of Advanced Technology PhD Programs for Semiconductor Device, Material, and Hetero-integration and Nanoengineering & Nanoscience.",
    },
    {
        "field": "math",
        "also_fields": ["statistics"],
        "sn": 9855,
        "name": "Mathematics, Ph.D.",
        "department": "College of Science — Department of Mathematics",
        "notes": "English-taught PhD program in the Department of Mathematics covering pure mathematics (algebra, analysis, geometry), applied and computational mathematics, and statistical sciences (NTU's Institute of Statistics and Data Science and Master Program in Statistics are Master's-only).",
    },
    {
        "field": "mech",
        "also_fields": [],
        "sn": 11631,
        "name": "Mechanical Engineering, Ph.D. (Thermal and Fluid Science Division)",
        "department": "College of Engineering — Department of Mechanical Engineering",
        "notes": "English-taught PhD program in the Department of Mechanical Engineering across five divisions: Thermal and Fluid Science (`sn/11631`), Solid Mechanics (`sn/11633`), Design (`sn/11635`), Manufacturing (`sn/11637`), and Control System (`sn/11639`). Companion unit: Institute of Applied Mechanics.",
    },
    {
        "field": "neuro",
        "also_fields": [],
        "sn": 10377,
        "name": "TIGP - Interdisciplinary Neuroscience, Ph.D.",
        "department": "College of Life Science — Taiwan International Graduate Program (TIGP) in Interdisciplinary Neuroscience",
        "gre_general_override": {
            "code": "Optional",
            "value": "GRE score is listed as optional ('if applicable') among the application documents for TIGP Interdisciplinary Neuroscience.",
            "quote": "GRE score ( if applicable)",
        },
        "fund_also_quote": "Name : TIGP Scholarship",
        "notes": "English-taught PhD program jointly run by NTU and Academia Sinica under the Taiwan International Graduate Program (TIGP); interview required. TIGP applicants apply via the TIGP portal (`tigp.apps.sinica.edu.tw`) and are funded via the TIGP Scholarship (rather than NTU OIA scholarships).",
    },
    {
        "field": "physics",
        "also_fields": [],
        "sn": 9861,
        "name": "Physics, Ph.D.",
        "department": "College of Science — Department of Physics",
        "supervisor": {
            "code": "Recommended",
            "value": "Department of Physics advises applicants to confirm a dissertation advisor before submitting their application, and notes that scholarship applications require the cooperation of the dissertation advisor.",
            "quote": "1. Applicants are advised to confirm a dissertation advisor before submitting their application. | 2. Scholarship applications require the cooperation of the dissertation advisor.",
        },
        "notes": "English-taught PhD program in the Department of Physics (College of Science; 18 graduation credits). Companion unit: Graduate Institute of Applied Physics (`sn/9921`).",
    },
]

for p in PROGRAMS:
    fid = p["field"]
    prog_url = BASE_DETAIL.format(p["sn"])

    if fid in {"math", "physics", "neuro"}:
        gre_s = {
            "code": "Not stated",
            "value": "Neither NTU's 2027/2028 Admission Guidelines nor this department's OIA application requirements page states a GRE Subject Test requirement.",
            "quote": "",
            "url": prog_url,
        }
    else:
        gre_s = {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for this discipline.",
            "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            "url": URL_ETS_SUBJ,
        }

    if "supervisor" in p:
        sup_field = {
            "code": p["supervisor"]["code"],
            "value": p["supervisor"]["value"],
            "quote": p["supervisor"]["quote"],
            "url": prog_url,
        }
    else:
        sup_field = {
            "code": "Not stated",
            "value": "This department's 2027/2028 OIA application requirements page does not state a pre-application supervisor contact requirement.",
            "quote": "",
            "url": prog_url,
        }

    fund_also = [
        {
            "quote": "NTU has many scholarships available for overseas students that can be applied for along with submitting your application. The government of Taiwan, other organizations, and your respective colleges also provide scholarships for international students.",
            "url": URL_SCHOL,
        }
    ]
    if "fund_also_quote" in p:
        fund_also.append({"quote": p["fund_also_quote"], "url": prog_url})

    fields_obj = {
        "deadline": {
            "code": "2027-01-28",
            "time_sensitive": "2027-01-28",
            "value": "2027/2028 September Entry Second Round online application deadline is January 28, 2027 at 4:00 PM GMT+8 (Round 2 opens December 1, 2026; Round 1 closed November 19, 2026).",
            "quote": "2027 September Entry Dates & Deadlines | 1st Round (2026-2027) | 2nd Round (2026-2027) | Online application deadline | November 19 | January 28",
            "url": URL_INTL,
            "also": [
                {
                    "quote": "Doctoral Degree | 2027/2028 First Semester Second Round",
                    "url": prog_url,
                }
            ],
        },
        "gre_subject": gre_s,
        "supervisor": sup_field,
        "funding": {
            "code": "Competitive",
            "value": "International PhD applicants may apply concurrently for NTU International Graduate Student Scholarships (via checkbox in the online application, no extra documents required), college/department fellowships (such as EECS Global Elite Cultivation Fellowship at NT$20,000/month up to 4 years, College of Medicine International Student Scholarship, or Academia Sinica TIGP Scholarship), and Taiwan MOE/MOFA Scholarships.",
            "quote": "VII. Scholarships | NTU provides a variety of scholarships for international degree students. Applicants will be asked whether to apply for NTU scholarships during the online degree application. No extra documents are needed.",
            "url": URL_GUIDE,
            "also": fund_also,
        },
        "entry_route": {
            "code": "Master's usually required",
            "value": "NTU's 2027/2028 Admission Guidelines require a Master's degree (or MOE-recognized equivalent educational level) to apply for PhD programs (direct-entry doctoral admission for graduating undergraduates is restricted to the Graduate School of Advanced Technology).",
            "quote": "Applicants with a high school diploma are eligible to apply for undergraduate programs, a Bachelor’s degree for Master’s programs, and a Master’s degree for PhD programs.",
            "url": URL_GUIDE,
        },
    }

    if "gre_general_override" in p:
        fields_obj["gre_general"] = {
            "code": p["gre_general_override"]["code"],
            "value": p["gre_general_override"]["value"],
            "quote": p["gre_general_override"]["quote"],
            "url": prog_url,
        }

    rec = {
        "id": f"ntu--{fid}",
        "university": "ntu",
        "field": fid,
        "also_fields": p["also_fields"],
        "name": p["name"],
        "department": p["department"],
        "program_page": prog_url,
        "checked": CHECKED,
        "fields": fields_obj,
        "notes": p["notes"],
    }
    (STAGING_PROG / f"ntu--{fid}.json").write_text(
        json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

print(f"Wrote ntu.json and {len(PROGRAMS)} programs to data/staging/")
