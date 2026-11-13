import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

# University record
uiowa_data = {
  "id": "uiowa",
  "institution": "University of Iowa",
  "country": "USA",
  "region": "Iowa",
  "grad_page": "https://grad.admissions.uiowa.edu/instructions/graduate-college",
  "checked": "2026-10-30",
  "notes": "Application fee $60 domestic, $100 international.",
  "fields": {
    "app_fee": {
      "code": "60 USD",
      "value": "Application fee is $60 for domestic applicants and $100 for international applicants.",
      "quote": "Submit the online application to the Graduate College and pay the $60 application fee by credit card ($100 for international applicants).",
      "url": "https://grad.admissions.uiowa.edu/instructions/graduate-college"
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Applicants for whom payment of the application fee presents a significant financial hardship may request an application fee waiver.",
      "quote": "Applicants for whom payment of the application fee presents a significant financial hardship may request an application fee waiver.",
      "url": "https://grad.admissions.uiowa.edu/cost-and-funding"
    },
    "gre_general": {
      "code": "Not stated",
      "value": "GRE requirements vary by academic program and are not stated centrally.",
      "quote": "Application deadlines and required supplemental materials vary by academic program so it’s important that you review the program-specific instructions including supplemental materials required by your academic program.",
      "url": "https://grad.admissions.uiowa.edu/instructions/graduate-college"
    },
    "toefl_min": {
      "code": "81",
      "value": "Total score 81 required on TOEFL.",
      "quote": "Total score 81",
      "url": "https://grad.admissions.uiowa.edu/english-proficiency-requirements"
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Overall score of 7 with no subscore less than 6.",
      "quote": "Overall score of 7 with no subscore less than 6",
      "url": "https://grad.admissions.uiowa.edu/english-proficiency-requirements"
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "Waiver given if applicant is a citizen or earned equivalent bachelor's, master's, or PhD in the US or exempt countries.",
      "quote": "Applicants will be given a waiver if they are a citizen, or have earned the equivalent of a bachelor’s degree, master's degree, or Ph.D. in the United States, or any of the following countries:",
      "url": "https://grad.admissions.uiowa.edu/english-proficiency-requirements"
    }
  }
}

(uni_dir / "uiowa.json").write_text(json.dumps(uiowa_data, indent=2), encoding="utf-8")

uiowa_entry_route = {
  "code": "Direct from bachelor's",
  "value": "Submit the online application to the Graduate College; direct entry with bachelor's or graduate degree depending on program.",
  "quote": "Submit the online application to the Graduate College and pay the $60 application fee by credit card ($100 for international applicants).",
  "url": "https://grad.admissions.uiowa.edu/instructions/graduate-college"
}

programs = [
  {
    "id": "uiowa--physics",
    "university": "uiowa",
    "field": "physics",
    "also_fields": [],
    "department": "Department of Physics and Astronomy",
    "program_page": "https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Physics (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-15",
        "value": "January 15 application deadline.",
        "quote": "Jan. 15",
        "url": "https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd"
      },
      "gre_subject": {
        "code": "Not stated",
        "value": "GRE Subject test requirement not stated on profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not stated on profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd"
      },
      "funding": {
        "code": "Typical",
        "value": "Competitive support packages available for admitted students.",
        "quote": "Attention Fall 2026 Applicants: We anticipate admissions this year to be extremely competitive and will likely have fewer than five support packages available.",
        "url": "https://grad.admissions.uiowa.edu/academics/physics-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--cs",
    "university": "uiowa",
    "field": "cs",
    "also_fields": [],
    "department": "Department of Computer Science",
    "program_page": "https://grad.admissions.uiowa.edu/academics/computer-science-phd",
    "checked": "2026-10-30",
    "notes": "Computer Science (PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-01",
        "value": "January 1 application deadline.",
        "quote": "Jan. 1",
        "url": "https://grad.admissions.uiowa.edu/academics/computer-science-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/computer-science-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/computer-science-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--chemistry",
    "university": "uiowa",
    "field": "chemistry",
    "also_fields": [],
    "department": "Department of Chemistry",
    "program_page": "https://grad.admissions.uiowa.edu/academics/chemistry-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Chemistry (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-01",
        "value": "January 1 application deadline.",
        "quote": "January 1",
        "url": "https://grad.admissions.uiowa.edu/academics/chemistry-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/chemistry-ms-or-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/chemistry-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--math",
    "university": "uiowa",
    "field": "math",
    "also_fields": [],
    "department": "Department of Mathematics",
    "program_page": "https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Mathematics (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-15",
        "value": "January 15 application deadline.",
        "quote": "Jan. 15",
        "url": "https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd"
      },
      "gre_subject": {
        "code": "Not stated",
        "value": "GRE Subject test requirement not stated on profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd"
      },
      "funding": {
        "code": "Typical",
        "value": "Teaching assistantships usually offered February through May.",
        "quote": "*Offers of admission and teaching assistantships are usually sent out February through May.",
        "url": "https://grad.admissions.uiowa.edu/academics/mathematics-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--statistics",
    "university": "uiowa",
    "field": "statistics",
    "also_fields": [],
    "department": "Department of Statistics and Actuarial Science",
    "program_page": "https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Statistics (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-15",
        "value": "January 15 deadline for students requesting financial support.",
        "quote": "Decisions for graduate financial support are typically made by April 15 for the upcoming academic year, so applications from students requesting financial support should reach us by Jan. 15.",
        "url": "https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd"
      },
      "funding": {
        "code": "Typical",
        "value": "All applicants considered for graduate assistantships (RA, TA, grader).",
        "quote": "All applicants are considered for financial support, for graduate assistantships, such as research assistants, teaching assistants and graders. However, it is important to note, that the applications must be fully complete by the deadline dates to be considered for this financial support.",
        "url": "https://grad.admissions.uiowa.edu/academics/statistics-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--biology",
    "university": "uiowa",
    "field": "biology",
    "also_fields": [],
    "department": "Department of Biology",
    "program_page": "https://grad.admissions.uiowa.edu/academics/integrated-biology-phd",
    "checked": "2026-10-30",
    "notes": "Integrated Biology (PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-01",
        "value": "January 1 PhD application deadline.",
        "quote": "PhD Deadline: January 1",
        "url": "https://grad.admissions.uiowa.edu/academics/integrated-biology-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/integrated-biology-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/integrated-biology-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--biomed",
    "university": "uiowa",
    "field": "biomed",
    "also_fields": [],
    "department": "Carver College of Medicine",
    "program_page": "https://grad.admissions.uiowa.edu/academics/biomedical-science-phd",
    "checked": "2026-10-30",
    "notes": "Biomedical Science (PhD)",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 application deadline.",
        "quote": "Dec. 1",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-science-phd"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE scores are not required for this program.",
        "quote": "GRE scores are not required for this program.",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-science-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-science-phd"
      },
      "funding": {
        "code": "Guaranteed",
        "value": "Admitted PhD students receive competitive stipend, health insurance allowance, and full tuition and mandatory fees.",
        "quote": "Students admitted to the PhD program receive a nationally competitive stipend and a health insurance allowance in addition to full payment of their tuition and mandatory fees.",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-science-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--bme",
    "university": "uiowa",
    "field": "bme",
    "also_fields": [],
    "department": "Department of Biomedical Engineering",
    "program_page": "https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Biomedical Engineering (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-01",
        "value": "January 1 application deadline.",
        "quote": "Jan. 1",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Recommended",
        "value": "Department strongly encourages identifying and contacting a research advisor prior to applying.",
        "quote": "The department strongly encourages prospective students to identify and contact a research advisor prior to applying.",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/biomedical-engineering-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--chemeng",
    "university": "uiowa",
    "field": "chemeng",
    "also_fields": [],
    "department": "Department of Chemical and Biochemical Engineering",
    "program_page": "https://grad.admissions.uiowa.edu/academics/chemical-and-biochemical-engineering-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Chemical and Biochemical Engineering (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-15",
        "value": "January 15 application deadline.",
        "quote": "Jan. 15",
        "url": "https://grad.admissions.uiowa.edu/academics/chemical-and-biochemical-engineering-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/chemical-and-biochemical-engineering-ms-or-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/chemical-and-biochemical-engineering-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--civil",
    "university": "uiowa",
    "field": "civil",
    "also_fields": [],
    "department": "Department of Civil and Environmental Engineering",
    "program_page": "https://grad.admissions.uiowa.edu/academics/civil-environmental-engineering-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Civil and Environmental Engineering (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-15",
        "value": "January 15 priority date for financial aid.",
        "quote": "Jan. 15 is the priority date to be considered for financial aid.",
        "url": "https://grad.admissions.uiowa.edu/academics/civil-environmental-engineering-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/civil-environmental-engineering-ms-or-phd"
      },
      "funding": {
        "code": "Typical",
        "value": "January 15 is the priority date to be considered for financial aid.",
        "quote": "Jan. 15 is the priority date to be considered for financial aid.",
        "url": "https://grad.admissions.uiowa.edu/academics/civil-environmental-engineering-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--ece",
    "university": "uiowa",
    "field": "ece",
    "also_fields": [],
    "department": "Department of Electrical and Computer Engineering",
    "program_page": "https://grad.admissions.uiowa.edu/academics/electrical-computer-engineering-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Electrical and Computer Engineering (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "Priority consideration given to complete applications received by December 15.",
        "quote": "Fall: Priority consideration will be given to all complete applications received by Dec. 15th.",
        "url": "https://grad.admissions.uiowa.edu/academics/electrical-computer-engineering-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/electrical-computer-engineering-ms-or-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/electrical-computer-engineering-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  },
  {
    "id": "uiowa--mech",
    "university": "uiowa",
    "field": "mech",
    "also_fields": [],
    "department": "Department of Mechanical Engineering",
    "program_page": "https://grad.admissions.uiowa.edu/academics/mechanical-engineering-ms-or-phd",
    "checked": "2026-10-30",
    "notes": "Mechanical Engineering (MS, PhD)",
    "fields": {
      "deadline": {
        "code": "2027-01-15",
        "value": "January 15 application deadline.",
        "quote": "Jan. 15 (Admission Decision: March 1)",
        "url": "https://grad.admissions.uiowa.edu/academics/mechanical-engineering-ms-or-phd"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/mechanical-engineering-ms-or-phd"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on academics profile.",
        "quote": "",
        "url": "https://grad.admissions.uiowa.edu/academics/mechanical-engineering-ms-or-phd"
      },
      "entry_route": uiowa_entry_route
    }
  }
]

for prog in programs:
  (prog_dir / f"{prog['id']}.json").write_text(json.dumps(prog, indent=2), encoding="utf-8")

print(f"Generated uiowa.json and {len(programs)} program records.")
