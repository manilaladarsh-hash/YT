import json
from pathlib import Path

STAGE = Path('data/staging')
(STAGE / 'universities').mkdir(parents=True, exist_ok=True)
(STAGE / 'programs').mkdir(parents=True, exist_ok=True)

ohsu_uni = {
  "id": "ohsu",
  "institution": "Oregon Health & Science University",
  "country": "USA",
  "region": "Oregon",
  "grad_page": "https://www.ohsu.edu/school-of-medicine/graduate-studies/admissions",
  "checked": "2026-10-29",
  "fields": {
    "app_fee": {
      "code": "70 USD",
      "value": "A complete degree application includes a $70 application fee.",
      "quote": "$70 application fee",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Applicants applying to any OHSU School of Medicine graduate program who are economically disadvantaged, have extenuating circumstances and/or participated in a qualifying program are eligible to request an application fee waiver based on funding availability.",
      "quote": "Applicants applying to any OHSU School of Medicine graduate program who are economically disadvantaged, have extenuating circumstances and/or participated in a qualifying program are eligible to request an application fee waiver. Graduate Studies provides a limited number of application fee waivers each academic year and these waivers are granted based on funding availability and are not guaranteed.",
      "url": "https://www.ohsu.edu/school-of-medicine/graduate-studies/admissions"
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Standardized tests are not a requirement for admission to the School of Medicine. However, individual graduate programs may choose to require the Graduate Record Examination (GRE) during admissions.",
      "quote": "Standardized tests are not a requirement for admission to the School of Medicine. However, individual graduate programs may choose to require the Graduate Record Examination (GRE) during admissions.",
      "url": "https://www.ohsu.edu/school-of-medicine/graduate-studies/admissions"
    },
    "toefl_min": {
      "code": "Not stated",
      "value": "There is no central Graduate Studies minimum TOEFL score requirement; minimums are determined by individual degree programs.",
      "quote": "What minimum TOEFL score is required?\nPlease check directly with the program(s) in which you are applying.",
      "url": "https://www.ohsu.edu/school-of-medicine/graduate-studies/admissions"
    },
    "ielts_min": {
      "code": "Not stated",
      "value": "There is no central Graduate Studies minimum IELTS score requirement; minimums are determined by individual degree programs.",
      "quote": "What minimum TOEFL score is required?\nPlease check directly with the program(s) in which you are applying.",
      "url": "https://www.ohsu.edu/school-of-medicine/graduate-studies/admissions"
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "These will only be waived if the applicant has obtained an undergraduate or graduate degree at an accredited college or university in the United States or other native English-speaking country.",
      "quote": "These will only be waived if the applicant has obtained an undergraduate or graduate degree at an accredited college or university in the United States or other native English-speaking country.",
      "url": "https://www.ohsu.edu/school-of-medicine/graduate-studies/admissions"
    }
  },
  "notes": ""
}

with open(STAGE / 'universities' / 'ohsu.json', 'w', encoding='utf-8') as f:
    json.dump(ohsu_uni, f, indent=2, ensure_ascii=False)
print("Wrote data/staging/universities/ohsu.json")

# Standard ETS quotes:
ets_general_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_general_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

programs = [
  {
    "field": "biomed",
    "also_fields": ["biology"],
    "department": "Graduate Program in Biomedical Sciences (PBMS)",
    "program_page": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions",
    "deadline": {
      "code": "2026-11-13",
      "value": "Applications for Fall 2027 open on September 1st, 2026 and will close on November 13th, 2026.",
      "quote": "Applications for Fall 2027 open on September 1st, 2026 and will close on November 13th, 2026.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    },
    "gre_general": {
      "code": "Not required",
      "value": "Are GRE scores required? No.",
      "quote": "Are GRE scores required?\nNo.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Biomedical Sciences subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "toefl_min": {
      "code": "80",
      "value": "An admitted applicant is expected to have a TOEFL score above 80 (iBT), 550 (paper-based), or an IELTS score above 6.5.",
      "quote": "An admitted applicant is expected to have a TOEFL score above 80 (iBT), 550 (paper-based), or an IELTS score above 6.5.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    },
    "ielts_min": {
      "code": "6.5",
      "value": "An admitted applicant is expected to have a TOEFL score above 80 (iBT), 550 (paper-based), or an IELTS score above 6.5.",
      "quote": "An admitted applicant is expected to have a TOEFL score above 80 (iBT), 550 (paper-based), or an IELTS score above 6.5.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program admissions page.",
      "quote": "",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    },
    "funding": {
      "code": "Guaranteed",
      "value": "In addition to the annual stipend, we cover 100% of tuition and university fees, full health, vision, and dental benefits, and access to the March Wellness Fitness Center for our students.",
      "quote": "In addition to the annual stipend, we cover 100% of tuition and university fees, full health, vision, and dental benefits, and access to the March Wellness Fitness Center for our students.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/resources"
    },
    "entry_route": {
      "code": "Direct from bachelor's",
      "value": "A baccalaureate degree or equivalent in chemistry, physics or one of the biological, medical sciences is required.",
      "quote": "A baccalaureate degree or equivalent, from an accredited U.S. academic institution, or equivalent international institution in chemistry, physics or one of the biological, medical sciences.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions"
    }
  },
  {
    "field": "bme",
    "also_fields": [],
    "department": "Department of Biomedical Engineering",
    "program_page": "https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions",
    "deadline": {
      "code": "2026-12-10",
      "value": "We encourage prospective Ph.D. students to apply by Dec. 10 to start in the fall of the following year. We also accept applications year-round and review them quarterly.",
      "quote": "We encourage prospective Ph.D. students to apply by Dec. 10 to start in the fall of the following year. We also accept applications year-round and review them quarterly.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions",
      "inferred": "year",
      "rolling": True
    },
    "gre_general": {
      "code": "Not required",
      "value": "We do not require the GRE and there are no GRE subject test requirements.",
      "quote": "What GRE score do I need? Do I need to complete a GRE subject test?\nWe do not require the GRE and there are no GRE subject test requirements.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Biomedical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program admissions page.",
      "quote": "",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions"
    },
    "funding": {
      "code": "Guaranteed",
      "value": "We provide a stipend to all students in our program. All tuition and student fees are waived for full-time students who are members of Graduate Researchers United.",
      "quote": "We provide a stipend to all students in our program. Please see the stipend policy for current rates. All tuition and student fees are waived for full-time students who are members of Graduate Researchers United. Students are also eligible for health and dental insurance.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions"
    },
    "entry_route": {
      "code": "Direct from bachelor's",
      "value": "Applicants should have taken undergraduate classes in engineering or other basic sciences with a strong math component; there are no specific undergraduate course requirements for admission.",
      "quote": "Applicants should have taken undergraduate classes in engineering or other basic sciences with a strong math component. However, there are no specific undergraduate course requirements for admission. The GRE is not required.",
      "url": "https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions"
    }
  },
  {
    "field": "neuro",
    "also_fields": [],
    "department": "Neuroscience Graduate Program (NGP)",
    "program_page": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information",
    "deadline": {
      "code": "2026-12-01",
      "value": "The $70.00 application fee is due by December 1st, along with all other application components.",
      "quote": "The $70.00 application fee is due by December 1st, along with all other application components.",
      "url": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Optional",
      "value": "GRE score submission is optional and scores are not used as a component in the NGP’s application review process.",
      "quote": "GRE score submission is optional and scores are not used as a component in the NGP’s application review process.",
      "url": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Neuroscience subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not required",
      "value": "In the first year, incoming students do rotations; after the first year, students join a lab.",
      "quote": "Tuition, fees, and health insurance is entirely covered for students. After the first year, students join a lab and are funded through the lab or the department.",
      "url": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information"
    },
    "funding": {
      "code": "Guaranteed",
      "value": "Tuition, fees, and health insurance is entirely covered for students. After the first year, students join a lab and are funded through the lab or the department.",
      "quote": "Tuition, fees, and health insurance is entirely covered for students. After the first year, students join a lab and are funded through the lab or the department.",
      "url": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information"
    },
    "entry_route": {
      "code": "Direct from bachelor's",
      "value": "The NGP does not have a minimum cumulative GPA requirement, but considers undergraduate grades and research preparation.",
      "quote": "The NGP does not have a minimum cumulative GPA requirement. However, if an applicant’s cumulative GPA falls below 3.0 or if individual course grades fall below a B- (in the course categories listed What We Look For in Prospective Applicants page), we ask for an explanation in the application portal.",
      "url": "https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information"
    }
  },
  {
    "field": "physics",
    "also_fields": [],
    "department": "Medical Physics Graduate Program",
    "program_page": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements",
    "deadline": {
      "code": "2027-01-15",
      "value": "Applications open Sept. 1; applications are due Jan. 15.",
      "quote": "Applications are due Jan. 15.",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE scores. No minimum score required. At-home test accepted.",
      "quote": "GRE scores. No minimum score required. At-home test accepted.",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    },
    "gre_subject": {
      "code": "Not stated",
      "value": "Not stated on program admission requirements page.",
      "quote": "",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    },
    "toefl_min": {
      "code": "90",
      "value": "Internet-Based (iBT): For exams taken before January 2026: minimum total score of 90; minimum section scores of: Writing: a minimum score of 24 out of 30.",
      "quote": "Internet-Based (iBT): For exams taken before January 2026: minimum total score of 90; minimum section scores of:",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    },
    "ielts_min": {
      "code": "6.5",
      "value": "IELTS: Overall score of 6.5.",
      "quote": "IELTS: Overall score of 6.5",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program admission requirements page.",
      "quote": "",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    },
    "funding": {
      "code": "Not stated",
      "value": "Not stated on program admission requirements page.",
      "quote": "",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    },
    "entry_route": {
      "code": "Direct from bachelor's",
      "value": "Your bachelor's degree and prerequisite coursework can be in-progress at the time of application submission, but must be fully complete before the start of the program.",
      "quote": "Note: Your bachelor's degree and prerequisite coursework can be in-progress at the time of application submission, but must be fully complete before the start of the program if offered admission.",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements"
    }
  },
  {
    "field": "datasci",
    "also_fields": ["cs"],
    "department": "Division of Informatics, Clinical Epidemiology and Translational Data Science (DICE)",
    "program_page": "https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information",
    "deadline": {
      "code": "2026-12-01",
      "value": "Terms begin in July. You can apply from Sept. 1 through Dec. 1.",
      "quote": "Terms begin in July. You can apply from Sept. 1 through Dec. 1.",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Data Science subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "Our program pairs you with a mentor with whom you will work closely. You’ll be asked to name and rank two or three faculty members who could be potential mentors.",
      "quote": "Our program pairs you with a mentor with whom you will work closely. You’ll be asked to name and rank two or three faculty members who could be potential mentors.",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information"
    },
    "funding": {
      "code": "Typical",
      "value": "Predoctoral positions funded nationally by the National Library of Medicine (NLM) Biomedical Informatics Training Grant are open to PhD students in the OHSU Biomedical Informatics Graduate Program.",
      "quote": "National Library of Medicine (NLM) Fellowships\nOHSU is one of 14 programs funded nationally by the National Library of Medicine (NLM) Biomedical Informatics Training Grant. Postdoctoral positions are open to any qualified individual with a doctoral degree (MD, PhD, DDS, etc.), with the fellow also strongly encouraged to also pursue a master's degree in the OHSU program. Predoctoral positions are open to PhD students in the OHSU Biomedical Informatics Graduate Program.",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information"
    },
    "entry_route": {
      "code": "Either",
      "value": "Minimum GPA of 3.0 and baccalaureate or advanced degree preparation required.",
      "quote": "Minimum GPA of 3.0",
      "url": "https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information"
    }
  }
]

for p in programs:
    fid = p["field"]
    prog_data = {
      "id": f"ohsu--{fid}",
      "university": "ohsu",
      "field": fid,
      "also_fields": p.get("also_fields", []),
      "department": p["department"],
      "program_page": p["program_page"],
      "checked": "2026-10-29",
      "fields": {
        "deadline": p["deadline"],
        "gre_subject": p["gre_subject"],
        "supervisor": p["supervisor"],
        "funding": p["funding"],
        "entry_route": p["entry_route"]
      },
      "notes": ""
    }
    for opt in ["gre_general", "toefl_min", "ielts_min"]:
        if opt in p:
            prog_data["fields"][opt] = p[opt]
    
    with open(STAGE / 'programs' / f"ohsu--{fid}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote data/staging/programs/ohsu--{fid}.json")
