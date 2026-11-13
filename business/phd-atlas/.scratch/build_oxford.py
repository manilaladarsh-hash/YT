import json
from pathlib import Path

staging_dir = Path("data/staging")
(staging_dir / "universities").mkdir(parents=True, exist_ok=True)
(staging_dir / "programs").mkdir(parents=True, exist_ok=True)

fee_url = "https://www.ox.ac.uk/admissions/graduate/application-guide/declaration-and-payment/application-fee"
waiver_url = "https://www.ox.ac.uk/admissions/graduate/application-guide/declaration-and-payment/application-fee-waivers"
gre_url = "https://www.ox.ac.uk/admissions/graduate/application-guide/supporting-documents/other-supporting-documents"
lang_url = "https://www.ox.ac.uk/admissions/graduate/application-guide/qualifications-experience-languages-funding/english-language-proficiency"
eng_waiver_url = "https://www.ox.ac.uk/admissions/graduate/application-guide/qualifications-experience-languages-funding/english-language-test-waivers"

uni_record = {
    "id": "oxford",
    "institution": "University of Oxford",
    "country": "United Kingdom",
    "region": "England",
    "grad_page": "https://www.ox.ac.uk/admissions/graduate/application-guide",
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "20 GBP",
            "value": "An application fee of GBP 20 is payable for applications to research courses (including DPhil and MSc by Research).",
            "quote": "The application fee for applications to research courses is...Research courses comprise Centres for Doctoral Training",
            "url": fee_url
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Application fee waivers are available for residents of eligible low-income countries, refugees, and UK applicants from low-income backgrounds.",
            "quote": "If you indicate on the application form that you are resident in one of the eligible countries in this section of the guidance, you will be asked additional questions relating to this waiver scheme.",
            "url": waiver_url,
            "also": [
                {
                    "quote": "Some UK applicants from low-income backgrounds are eligible for a fee waiver.",
                    "url": waiver_url
                }
            ]
        },
        "gre_general": {
            "code": "Not required",
            "value": "GRE General Test scores are not required for most courses; only a small number of courses require or encourage them.",
            "quote": "For a small number of courses, applicants are required or encouraged to submit GRE General Test scores. For other courses, they are not required.",
            "url": gre_url
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "English language proficiency is required at the University's standard or higher level; each course page states the required level for that course.",
            "quote": "To take up a place on one of our courses, you must be able to demonstrate English language proficiency at the University's standard or higher level. Each course page states the required level for that course.",
            "url": lang_url
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "English language proficiency is required at the University's standard or higher level; each course page states the required level for that course.",
            "quote": "To take up a place on one of our courses, you must be able to demonstrate English language proficiency at the University's standard or higher level. Each course page states the required level for that course.",
            "url": lang_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "You may apply for a waiver if you have completed or are completing a degree-level course of at least nine months taught and assessed entirely in English within 2 academic years; evidence must be uploaded if not from a majority English speaking country.",
            "quote": "undertaken at a recognised institution where teaching and assessment throughout the course is undertaken entirely in English; and",
            "url": eng_waiver_url
        }
    },
    "notes": "Graduate research courses at Oxford lead to the degree of Doctor of Philosophy (DPhil). Applicants apply to specific DPhil courses and colleges."
}

with open(staging_dir / "universities" / "oxford.json", "w", encoding="utf-8") as f:
    json.dump(uni_record, f, indent=2, ensure_ascii=False)
    f.write("\n")

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

programs_data = [
    {
        "id": "cs",
        "dept": "Department of Computer Science",
        "title": "DPhil in Computer Science",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-computer-science",
        "dl_date": "2026-12-02",
        "dl_quote": "12:00 midday UK time on Wednesday 2 December 2026",
        "entry_route": "Either",
        "entry_val": "Applicants are expected to achieve either a first-class or strong upper second-class four-year undergraduate degree with honours, or a bachelor's and a master's degree with merit or distinction.",
        "entry_quote": "a first-class or a strong upper second-class four-year undergraduate degree with honours in a relevant subject, or a first-class or a strong upper second-class three-year undergraduate degree with honours and a master's degree with merit or distinction",
        "sup_code": "Recommended",
        "sup_val": "Applicants can contact potential supervisors directly before applying, but are not required to secure a supervisor in advance.",
        "sup_quote": "Academic staff profiles contain information on their research interests and will help you identify potential supervisors. You can contact potential supervisors directly",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "ece",
        "dept": "Department of Engineering Science",
        "title": "DPhil in Engineering Science (Electrical and Optoelectronic Engineering)",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-engineering-science",
        "dl_date": "2026-12-02",
        "dl_quote": "12:00 midday UK time on Wednesday 2 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours; a previous master's qualification is not required.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours in engineering or a related discipline relevant for the proposed area of research, such as physics, materials science, computer science, applied mathematics or chemistry. a previous master's qualification is not required.",
        "sup_code": "Recommended",
        "sup_val": "The department recommends contacting potential supervisors ahead of submitting an application.",
        "sup_quote": "We recommend contacting a potential supervisor(s) ahead of submitting your application.",
        "fund_quote": "final application deadline to be considered for oxford scholarships"
    },
    {
        "id": "mech",
        "dept": "Department of Engineering Science",
        "title": "DPhil in Engineering Science (Mechanical and Aerospace Engineering)",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-engineering-science",
        "dl_date": "2026-12-02",
        "dl_quote": "12:00 midday UK time on Wednesday 2 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours; a previous master's qualification is not required.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours in engineering or a related discipline relevant for the proposed area of research, such as physics, materials science, computer science, applied mathematics or chemistry. a previous master's qualification is not required.",
        "sup_code": "Recommended",
        "sup_val": "The department recommends contacting potential supervisors ahead of submitting an application.",
        "sup_quote": "We recommend contacting a potential supervisor(s) ahead of submitting your application.",
        "fund_quote": "final application deadline to be considered for oxford scholarships"
    },
    {
        "id": "civil",
        "dept": "Department of Engineering Science",
        "title": "DPhil in Engineering Science (Civil and Offshore Engineering)",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-engineering-science",
        "dl_date": "2026-12-02",
        "dl_quote": "12:00 midday UK time on Wednesday 2 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours; a previous master's qualification is not required.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours in engineering or a related discipline relevant for the proposed area of research, such as physics, materials science, computer science, applied mathematics or chemistry. a previous master's qualification is not required.",
        "sup_code": "Recommended",
        "sup_val": "The department recommends contacting potential supervisors ahead of submitting an application.",
        "sup_quote": "We recommend contacting a potential supervisor(s) ahead of submitting your application.",
        "fund_quote": "final application deadline to be considered for oxford scholarships"
    },
    {
        "id": "chemeng",
        "dept": "Department of Engineering Science",
        "title": "DPhil in Engineering Science (Chemical and Process Engineering)",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-engineering-science",
        "dl_date": "2026-12-02",
        "dl_quote": "12:00 midday UK time on Wednesday 2 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours; a previous master's qualification is not required.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours in engineering or a related discipline relevant for the proposed area of research, such as physics, materials science, computer science, applied mathematics or chemistry. a previous master's qualification is not required.",
        "sup_code": "Recommended",
        "sup_val": "The department recommends contacting potential supervisors ahead of submitting an application.",
        "sup_quote": "We recommend contacting a potential supervisor(s) ahead of submitting your application.",
        "fund_quote": "final application deadline to be considered for oxford scholarships"
    },
    {
        "id": "bme",
        "dept": "Department of Engineering Science",
        "title": "DPhil in Engineering Science (Biomedical Engineering)",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-engineering-science",
        "dl_date": "2026-12-02",
        "dl_quote": "12:00 midday UK time on Wednesday 2 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours; a previous master's qualification is not required.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours in engineering or a related discipline relevant for the proposed area of research, such as physics, materials science, computer science, applied mathematics or chemistry. a previous master's qualification is not required.",
        "sup_code": "Recommended",
        "sup_val": "The department recommends contacting potential supervisors ahead of submitting an application.",
        "sup_quote": "We recommend contacting a potential supervisor(s) ahead of submitting your application.",
        "fund_quote": "final application deadline to be considered for oxford scholarships"
    },
    {
        "id": "materials",
        "dept": "Department of Materials",
        "title": "DPhil in Materials",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-materials",
        "dl_date": "2026-11-13",
        "dl_quote": "12:00 midday UK time on Friday 13 November 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in a suitable science subject.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Not required",
        "sup_val": "There is no need to contact any supervisor before making an application.",
        "sup_quote": "there is no need to contact any supervisor before making an application",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "math",
        "dept": "Mathematical Institute",
        "title": "DPhil in Mathematics",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-mathematics",
        "dl_date": "2027-01-06",
        "dl_quote": "12:00 midday UK time on Wednesday 6 January 2027",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class undergraduate degree with honours in mathematics or a related discipline; a previous master's degree is not required.",
        "entry_quote": "a first-class undergraduate degree with honours in mathematics or a related discipline. A previous master's degree is not required",
        "sup_code": "Not required",
        "sup_val": "Applicants do not need to contact the department or secure agreement from an academic before applying.",
        "sup_quote": "you do not need to contact the department before you apply",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "statistics",
        "dept": "Department of Statistics",
        "title": "DPhil in Statistics",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-statistics",
        "dl_date": "2027-01-06",
        "dl_quote": "12:00 midday UK time on Wednesday 6 January 2027",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in an appropriate subject.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Recommended",
        "sup_val": "Applicants are advised to look at research interests and contact a potential supervisor via email.",
        "sup_quote": "contact a potential supervisor via email to clarify your proposed research area",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "physics",
        "dept": "Department of Physics",
        "title": "DPhil in Theoretical Physics",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-theoretical-physics",
        "dl_date": "2027-01-06",
        "dl_quote": "12:00 midday UK time on Wednesday 6 January 2027",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in physics, mathematics or relevant science.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Recommended",
        "sup_val": "Applicants do not need to contact the department before applying but are encouraged to visit departmental webpages.",
        "sup_quote": "you do not need to contact the department before you apply but you are encouraged",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "astronomy",
        "dept": "Department of Physics (Sub-department of Astrophysics)",
        "title": "DPhil in Astrophysics",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-astrophysics",
        "dl_date": "2027-01-06",
        "dl_quote": "12:00 midday UK time on Wednesday 6 January 2027",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in physics, astrophysics or astronomy.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Recommended",
        "sup_val": "Applicants do not need to contact the department before applying but are encouraged to visit departmental webpages.",
        "sup_quote": "you do not need to contact the department before you apply but you are encouraged",
        "fund_quote": "considered for Oxford scholarships. For the majority of Oxford scholarships, your application will automatically be"
    },
    {
        "id": "chemistry",
        "dept": "Department of Chemistry",
        "title": "DPhil in Chemistry",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-chemistry",
        "dl_date": "2026-11-13",
        "dl_quote": "12:00 midday UK time on Friday 13 November 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in a relevant subject.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Recommended",
        "sup_val": "Applicants should make contact with the academic(s) in their area of research to discuss potential topics and funding.",
        "sup_quote": "You should make contact with the academic(s) in your area of research to discuss potential research topics",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "biology",
        "dept": "Department of Biology",
        "title": "DPhil in Biology",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-biology",
        "dl_date": "2027-01-06",
        "dl_quote": "12:00 midday UK time on Wednesday 6 January 2027",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in appropriate subjects.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Required",
        "sup_val": "Before applying, applicants must identify potential supervisors and contact them directly.",
        "sup_quote": "You must contact your potential supervisor",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "earth",
        "dept": "Department of Earth Sciences",
        "title": "DPhil in Earth Sciences",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-earth-sciences",
        "dl_date": "2027-01-27",
        "dl_quote": "12:00 midday UK time on Wednesday 27 January 2027",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in science or mathematics.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Required",
        "sup_val": "Before applying, applicants should identify an academic supervisor who is willing to supervise and support the project.",
        "sup_quote": "identify an academic member of staff who is willing to supervise you",
        "fund_quote": "Final application deadline to be considered for Oxford scholarships"
    },
    {
        "id": "neuro",
        "dept": "Nuffield Department of Clinical Neurosciences",
        "title": "DPhil in Neuroscience",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-neuroscience",
        "dl_date": "2026-12-01",
        "dl_quote": "12:00 midday UK time on Tuesday 1 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in any scientific discipline.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Recommended",
        "sup_val": "It is recommended that applicants contact the course lecturer before applying.",
        "sup_quote": "It is recommended that you contact the course lecturer before you apply",
        "fund_quote": "considered for Oxford scholarships. For the majority of Oxford scholarships, your application will automatically be"
    },
    {
        "id": "biomed",
        "dept": "Medical Sciences Division / Radcliffe Department of Medicine",
        "title": "DPhil in Medical Sciences",
        "url": "https://www.ox.ac.uk/admissions/graduate/courses/dphil-medical-sciences",
        "dl_date": "2026-12-01",
        "dl_quote": "12:00 midday UK time on Tuesday 1 December 2026",
        "entry_route": "Direct from bachelor's",
        "entry_val": "Applicants should hold or be predicted to achieve a first-class or strong upper second-class undergraduate degree with honours in a biomedical or science subject.",
        "entry_quote": "a first-class or strong upper second-class undergraduate degree with honours",
        "sup_code": "Recommended",
        "sup_val": "Before applying, applicants should contact prospective supervisors to discuss research opportunities.",
        "sup_quote": "you should contact prospective supervisors to discuss the research opportunities available",
        "fund_quote": "considered for Oxford scholarships. For the majority of Oxford scholarships, your application will automatically be"
    }
]

for p in programs_data:
    field_id = p["id"]
    curl = p["url"]
    title = p["title"]
    
    if field_id in ("math", "statistics", "physics", "astronomy", "neuro"):
        gre_sub = {
            "code": "Not stated",
            "value": f"GRE Subject Test is not stated or required for {title} at Oxford.",
            "quote": "",
            "url": curl
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": ets_url
        }

    prog_record = {
        "id": f"oxford--{field_id}",
        "university": "oxford",
        "field": field_id,
        "also_fields": [],
        "department": p["dept"],
        "program_page": curl,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": p["dl_date"],
                "value": f"The deadline for admission and Oxford scholarship consideration is {p['dl_date']}.",
                "quote": p["dl_quote"],
                "url": curl
            },
            "entry_route": {
                "code": p["entry_route"],
                "value": p["entry_val"],
                "quote": p["entry_quote"],
                "url": curl
            },
            "supervisor": {
                "code": p["sup_code"],
                "value": p["sup_val"],
                "quote": p["sup_quote"],
                "url": curl
            },
            "funding": {
                "code": "Competitive",
                "value": "All eligible applicants who apply by the deadline are automatically considered for Oxford scholarships.",
                "quote": p["fund_quote"],
                "url": curl
            },
            "gre_subject": gre_sub
        },
        "notes": f"{title} at the University of Oxford."
    }

    with open(staging_dir / "programs" / f"oxford--{field_id}.json", "w", encoding="utf-8") as f:
        json.dump(prog_record, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Staged oxford and {len(programs_data)} programs successfully.")
