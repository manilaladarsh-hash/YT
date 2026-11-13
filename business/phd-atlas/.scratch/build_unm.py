import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

apply_url = "https://grad.unm.edu/prospective-students/apply-now.html"
eng_url = "https://international.unm.edu/english-proficiency.html"
geo_acad_url = "https://geo.unm.edu/admission/graduate/requirements/academic.html"

unm_data = {
  "id": "unm",
  "institution": "University of New Mexico",
  "country": "USA",
  "region": "New Mexico",
  "grad_page": apply_url,
  "checked": "2026-10-30",
  "notes": "Application fee is $60 domestic, $70 international.",
  "fields": {
    "app_fee": {
      "code": "60 USD",
      "value": "$60 domestic, $70 international online application fee.",
      "quote": "When you have completed your application and are ready to submit it, you will be required to pay an application fee via credit card online ($60 for domestic applications, $70 for international applications).",
      "url": apply_url
    },
    "fee_waiver": {
      "code": "Domestic only",
      "value": "Application fee waivers are not available to international applicants.",
      "quote": "Application fee waivers are not available to international applicants.",
      "url": apply_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Each graduate and professional program has specific requirements for admissions.",
      "quote": "Each graduate and professional program has specific requirements for admissions, as well as its own deadlines. Before applying, be sure to review the application requirements and instructions for your program of interest, as well as the information below.",
      "url": apply_url
    },
    "toefl_min": {
      "code": "79",
      "value": "79 internet-based minimum TOEFL score.",
      "quote": "79 (4.5)",
      "url": eng_url
    },
    "ielts_min": {
      "code": "6.5",
      "value": "6.5 minimum IELTS Academic band score.",
      "quote": "6.5",
      "url": eng_url
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "Exemption granted for bachelor's degree from regionally-accredited US institution or recognized institution in English-speaking country.",
      "quote": "Bachelor's degree from a regionally-accredited US college or university or a recognized institution in English-Speaking Canada, the United Kingdom, South Africa, Australia, or New Zealand.",
      "url": eng_url
    }
  }
}

(uni_dir / "unm.json").write_text(json.dumps(unm_data, indent=2), encoding="utf-8")

# Common entry route for UNM
unm_entry_route = {
  "code": "Direct from bachelor's",
  "value": "Earned degree that is equivalent to a U.S. bachelor's degree.",
  "quote": "Previous Education: Earned degree that is the equivalent to a U.S. Bachelor degree.",
  "url": geo_acad_url
}

# 1. Physics
phys_url = "https://grad.unm.edu/graduate-programs/application-instructions/physics.html"
phys_prog = {
  "id": "unm--physics",
  "university": "unm",
  "field": "physics",
  "also_fields": [],
  "department": "Department of Physics and Astronomy",
  "program_page": phys_url,
  "checked": "2026-10-30",
  "notes": "Physics PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-19",
      "value": "December 19 application deadline for Fall admission.",
      "quote": "December 19th",
      "url": phys_url
    },
    "gre_general": {
      "code": "Optional",
      "value": "General GRE test scores are optional.",
      "quote": "General GRE test and Physics GRE subject test scores are optional.",
      "url": phys_url
    },
    "gre_subject": {
      "code": "Optional",
      "value": "Physics GRE subject test scores are optional.",
      "quote": "General GRE test and Physics GRE subject test scores are optional.",
      "url": phys_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "Strongly encouraged to list faculty members of interest in personal statement.",
      "quote": "Visit the department research page and list a few Physics & Astronomy Dept. faculty you are interested in working with.",
      "url": phys_url
    },
    "funding": {
      "code": "Typical",
      "value": "TAs provided for up to two years, after which students typically find RA employment.",
      "quote": "Depending upon budgetary restrictions, we provide TAs for up to two years pending continued satisfactory performance of teaching/grading duties. After the first two years, students typically find employment as Research Assistants (RAs) with one of our faculty.",
      "url": phys_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--physics.json").write_text(json.dumps(phys_prog, indent=2), encoding="utf-8")

# 2. CS
cs_url = "https://grad.unm.edu/graduate-programs/application-instructions/computer-science.html"
cs_prog = {
  "id": "unm--cs",
  "university": "unm",
  "field": "cs",
  "also_fields": [],
  "department": "Department of Computer Science",
  "program_page": cs_url,
  "checked": "2026-10-30",
  "notes": "Computer Science PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-15",
      "value": "January 15 priority application deadline for Fall admission.",
      "quote": "Priority Deadline: January 15th",
      "url": cs_url
    },
    "gre_general": {
      "code": "Optional",
      "value": "GRE scores are optional.",
      "quote": "GRE scores are optional; however, submitting strong scores may strengthen your application",
      "url": cs_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Computer Science.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "Select up to three faculty members you would like to work with.",
      "quote": "Select up to three faculty members you would like to work with.",
      "url": cs_url
    },
    "funding": {
      "code": "Typical",
      "value": "Teaching assistantships are limited and selection is competitive.",
      "quote": "Teaching assistantships are limited in number and the selection process is very competitive.",
      "url": cs_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--cs.json").write_text(json.dumps(cs_prog, indent=2), encoding="utf-8")

# 3. Chemistry
chem_url = "https://grad.unm.edu/graduate-programs/application-instructions/chemistry-chemical-biology.html"
chem_prog = {
  "id": "unm--chemistry",
  "university": "unm",
  "field": "chemistry",
  "also_fields": [],
  "department": "Department of Chemistry and Chemical Biology",
  "program_page": chem_url,
  "checked": "2026-10-30",
  "notes": "Chemistry PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-01",
      "value": "December 1 application deadline for Fall admission.",
      "quote": "December 1",
      "url": chem_url
    },
    "gre_general": {
      "code": "Recommended",
      "value": "GRE is not required but is recommended.",
      "quote": "The GRE is not required but is recommended.",
      "url": chem_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Chemistry.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": chem_url
    },
    "funding": {
      "code": "Not stated",
      "value": "Funding details not stated on program instructions page.",
      "quote": "",
      "url": chem_url
    },
    "entry_route": {
      "code": "Direct from bachelor's",
      "value": "A B.S. or equivalent degree in Chemistry or closely related discipline is required.",
      "quote": "A B.S. or equivalent degree in Chemistry or closely related discipline is required by the time of the start of graduate",
      "url": chem_url
    }
  }
}
(prog_dir / "unm--chemistry.json").write_text(json.dumps(chem_prog, indent=2), encoding="utf-8")

# 4. Math
math_url = "https://grad.unm.edu/graduate-programs/application-instructions/mathematics.html"
math_prog = {
  "id": "unm--math",
  "university": "unm",
  "field": "math",
  "also_fields": [],
  "department": "Department of Mathematics and Statistics",
  "program_page": math_url,
  "checked": "2026-10-30",
  "notes": "Mathematics PhD.",
  "fields": {
    "deadline": {
      "code": "2027-02-15",
      "value": "February 15 application deadline for Fall admission.",
      "quote": "February 15th",
      "url": math_url
    },
    "gre_general": {
      "code": "Not required",
      "value": "GRE scores are not required.",
      "quote": "GRE scores are not required.",
      "url": math_url
    },
    "gre_subject": {
      "code": "Not required",
      "value": "GRE scores are not required.",
      "quote": "GRE scores are not required.",
      "url": math_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": math_url
    },
    "funding": {
      "code": "Typical",
      "value": "Assistantships available; indicate interest in letter of intent.",
      "quote": "If you are interested in an assistantship, please indicate in your letter of intent.",
      "url": math_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--math.json").write_text(json.dumps(math_prog, indent=2), encoding="utf-8")

# 5. Biology
bio_url = "https://grad.unm.edu/graduate-programs/application-instructions/biology.html"
bio_prog = {
  "id": "unm--biology",
  "university": "unm",
  "field": "biology",
  "also_fields": [],
  "department": "Department of Biology",
  "program_page": bio_url,
  "checked": "2026-10-30",
  "notes": "Biology PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-01",
      "value": "December 1 priority application deadline for Fall admission.",
      "quote": "Priority Deadline: December 1st",
      "url": bio_url
    },
    "gre_general": {
      "code": "Not considered",
      "value": "GRE scores will not be considered in admission process.",
      "quote": "The GRE is optional. GRE scores will not be considered in the admission process",
      "url": bio_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Biology.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": bio_url
    },
    "funding": {
      "code": "Typical",
      "value": "Assistantship funding available for graduate students.",
      "quote": "Please let the program know if you would like to receive assistantship funding as you pursue your degree.",
      "url": bio_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--biology.json").write_text(json.dumps(bio_prog, indent=2), encoding="utf-8")

# 6. Biomed
biomed_url = "https://grad.unm.edu/graduate-programs/application-instructions/biomedical-sciences.html"
biomed_prog = {
  "id": "unm--biomed",
  "university": "unm",
  "field": "biomed",
  "also_fields": [],
  "department": "Biomedical Sciences Graduate Program",
  "program_page": biomed_url,
  "checked": "2026-10-30",
  "notes": "Biomedical Sciences PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-01",
      "value": "December 1 application deadline for Fall admission.",
      "quote": "December 1st",
      "url": biomed_url
    },
    "gre_general": {
      "code": "Optional",
      "value": "GRE scores are optional.",
      "quote": "GRE scores are optional and should only be submitted if they strengthen your application package.",
      "url": biomed_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Biomedical Sciences.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": biomed_url
    },
    "funding": {
      "code": "Not stated",
      "value": "Funding details not stated on program instructions page.",
      "quote": "",
      "url": biomed_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--biomed.json").write_text(json.dumps(biomed_prog, indent=2), encoding="utf-8")

# 7. BME
bme_url = "https://grad.unm.edu/graduate-programs/application-instructions/biomedical-engineering.html"
bme_prog = {
  "id": "unm--bme",
  "university": "unm",
  "field": "bme",
  "also_fields": [],
  "department": "Center for Biomedical Engineering",
  "program_page": bme_url,
  "checked": "2026-10-30",
  "notes": "Biomedical Engineering PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-15",
      "value": "January 15 priority date for financial aid consideration for Fall admission.",
      "quote": "Priority Date for Financial Aid Consideration: January 15th",
      "url": bme_url
    },
    "gre_general": {
      "code": "Not required",
      "value": "GRE scores are not required at this time.",
      "quote": "GRE scores are not required at this time.",
      "url": bme_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Biomedical Engineering.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": bme_url
    },
    "funding": {
      "code": "Typical",
      "value": "Priority date for financial aid consideration is January 15.",
      "quote": "Priority Date for Financial Aid Consideration: January 15th",
      "url": bme_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--bme.json").write_text(json.dumps(bme_prog, indent=2), encoding="utf-8")

# 8. ChemEng
chemeng_url = "https://grad.unm.edu/graduate-programs/application-instructions/chemical-engineering.html"
chemeng_prog = {
  "id": "unm--chemeng",
  "university": "unm",
  "field": "chemeng",
  "also_fields": [],
  "department": "Department of Chemical and Biological Engineering",
  "program_page": chemeng_url,
  "checked": "2026-10-30",
  "notes": "Chemical Engineering PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-15",
      "value": "January 15 priority application deadline for Fall admission.",
      "quote": "Priority: January 15th",
      "url": chemeng_url
    },
    "gre_general": {
      "code": "Required",
      "value": "General GRE exam is required.",
      "quote": "The General GRE exam is required. The institution code is 4845. No subject code is required.",
      "url": chemeng_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Chemical Engineering.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": chemeng_url
    },
    "funding": {
      "code": "Not stated",
      "value": "Funding details not stated on program instructions page.",
      "quote": "",
      "url": chemeng_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--chemeng.json").write_text(json.dumps(chemeng_prog, indent=2), encoding="utf-8")

# 9. Civil
civil_url = "https://grad.unm.edu/graduate-programs/application-instructions/civil-construction-environmental-engineering.html"
civil_prog = {
  "id": "unm--civil",
  "university": "unm",
  "field": "civil",
  "also_fields": [],
  "department": "Department of Civil, Construction and Environmental Engineering",
  "program_page": civil_url,
  "checked": "2026-10-30",
  "notes": "Civil Engineering PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-31",
      "value": "January 31 deadline for assistantship consideration for Fall admission.",
      "quote": "International and Domestic Students: January 31st",
      "url": civil_url
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE required with minimum combined 300 on verbal and quantitative sections.",
      "quote": "GRE required. A minimum combined score of 300 on the verbal and quantitative sections is required.",
      "url": civil_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Civil Engineering.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": civil_url
    },
    "funding": {
      "code": "Typical",
      "value": "Applications should be received by deadlines indicated to be considered for assistantships.",
      "quote": "To be considered for assistantships, applications should be received by the deadlines indicated above.",
      "url": civil_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--civil.json").write_text(json.dumps(civil_prog, indent=2), encoding="utf-8")

# 10. ECE
ece_url = "https://grad.unm.edu/graduate-programs/application-instructions/electrical-engineering.html"
ece_prog = {
  "id": "unm--ece",
  "university": "unm",
  "field": "ece",
  "also_fields": [],
  "department": "Department of Electrical and Computer Engineering",
  "program_page": ece_url,
  "checked": "2026-10-30",
  "notes": "Electrical Engineering PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-31",
      "value": "January 31 best consideration deadline for applicants seeking financial aid for Fall admission.",
      "quote": "Best Consideration if Seeking Financial Aid (Domestic and International): January 31st",
      "url": ece_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "GRE requirement not stated on instructions page.",
      "quote": "",
      "url": ece_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Electrical and Computer Engineering.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "State if any interest in or contact with an ECE faculty member in letter of intent.",
      "quote": "interest in or contact with an ECE faculty member",
      "url": ece_url
    },
    "funding": {
      "code": "Typical",
      "value": "Assistantships are limited and selection process is very competitive.",
      "quote": "Assistantships are limited and selection process is very competitive.",
      "url": ece_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--ece.json").write_text(json.dumps(ece_prog, indent=2), encoding="utf-8")

# 11. Mech
mech_url = "https://grad.unm.edu/graduate-programs/application-instructions/mechanical-engineering.html"
mech_prog = {
  "id": "unm--mech",
  "university": "unm",
  "field": "mech",
  "also_fields": [],
  "department": "Department of Mechanical Engineering",
  "program_page": mech_url,
  "checked": "2026-10-30",
  "notes": "Mechanical Engineering PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-01",
      "value": "January 1 deadline for domestic and international applicants requesting financial aid.",
      "quote": "Domestic and International applicants requesting financial aid: January 1st",
      "url": mech_url
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE scores are required and should be submitted to the University directly by ETS.",
      "quote": "GRE scores are required and should be submitted to the University directly by ETS",
      "url": mech_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Mechanical Engineering.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": mech_url
    },
    "funding": {
      "code": "Typical",
      "value": "Financial aid deadline January 1; submit TA/GA application form.",
      "quote": "Domestic and International applicants requesting financial aid: January 1st",
      "url": mech_url
    },
    "entry_route": unm_entry_route
  }
}
(prog_dir / "unm--mech.json").write_text(json.dumps(mech_prog, indent=2), encoding="utf-8")

print("Created UNM university and 11 program staging records successfully!")
