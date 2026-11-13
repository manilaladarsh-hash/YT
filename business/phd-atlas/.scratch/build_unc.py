import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

unc_instructions_url = "https://gradschool.unc.edu/admissions/instructions.html"

# University record
unc_data = {
  "id": "unc",
  "institution": "University of North Carolina at Chapel Hill",
  "country": "USA",
  "region": "North Carolina",
  "grad_page": "https://gradschool.unc.edu/admissions/instructions.html",
  "checked": "2026-10-30",
  "notes": "Non-refundable $95 application fee per program.",
  "fields": {
    "app_fee": {
      "code": "95 USD",
      "value": "A non-refundable $95.00 application fee is required for each program to which you apply.",
      "quote": "A non-refundable $95.00 application fee is required for each program to which you apply.",
      "url": unc_instructions_url
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "There are several categories of applicants who may qualify for an application fee waiver.",
      "quote": "Fee waiver. There are several categories of applicants who may qualify for an application fee waiver. Please see Information on Application Fee Waiver requests.",
      "url": unc_instructions_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Standardized test score requirements determined by specific program listings.",
      "quote": "Please see specific program listings for test score requirement information.",
      "url": unc_instructions_url
    },
    "toefl_min": {
      "code": "90",
      "value": "Recommended minimum internet-based TOEFL score is 90.",
      "quote": "TOEFL tests taken prior to January 26, 2026 = 90",
      "url": unc_instructions_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Recommended minimum IELTS exam score is 7.0.",
      "quote": "The IELTS exam = 7",
      "url": unc_instructions_url
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "Exemption granted if applicant received or will receive degree from an accredited university where English is sole language of instruction.",
      "quote": "applicants who have received or will receive a degree from an accredited university where English is the SOLE language of instruction.",
      "url": unc_instructions_url
    }
  }
}

(uni_dir / "unc.json").write_text(json.dumps(unc_data, indent=2), encoding="utf-8")

unc_entry_route = {
  "code": "Direct from bachelor's",
  "value": "A bachelor's degree based on a four-year curriculum completed before graduate study begins or international equivalent required.",
  "quote": "a bachelor’s degree (based on a four-year curriculum) completed before graduate study begins or its international equivalent",
  "url": unc_instructions_url
}

programs = [
  {
    "id": "unc--physics",
    "university": "unc",
    "field": "physics",
    "also_fields": [],
    "department": "Department of Physics and Astronomy",
    "program_page": "https://gradschool.sites.unc.edu/physics-and-astronomy/",
    "checked": "2026-10-30",
    "notes": "Physics and Astronomy Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline for Fall admission.",
        "quote": "Doctoral PHD PHYS Fall December 1, 2026",
        "url": "https://gradschool.sites.unc.edu/physics-and-astronomy/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required for admission.",
        "quote": "GRE not required",
        "url": "https://gradschool.sites.unc.edu/physics-and-astronomy/"
      },
      "gre_subject": {
        "code": "Not required",
        "value": "GRE not required for admission.",
        "quote": "GRE not required",
        "url": "https://gradschool.sites.unc.edu/physics-and-astronomy/"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://gradschool.sites.unc.edu/physics-and-astronomy/"
      },
      "funding": {
        "code": "Typical",
        "value": "Fall Graduate School Fellowships deadline December 15.",
        "quote": "Fall Graduate School Fellowships December 15, 2026",
        "url": "https://gradschool.sites.unc.edu/physics-and-astronomy/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--cs",
    "university": "unc",
    "field": "cs",
    "also_fields": [],
    "department": "Department of Computer Science",
    "program_page": "https://gradschool.sites.unc.edu/computer-science/",
    "checked": "2026-10-30",
    "notes": "Computer Science Ph.D.",
    "fields": {
      "deadline": {
        "code": "2027-01-05",
        "value": "January 5 deadline for Computer Science Research and Teaching Assistantships.",
        "quote": "Computer Science Research and Teaching Assistantships January 5, 2027",
        "url": "https://gradschool.sites.unc.edu/computer-science/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE scores are not required.",
        "quote": "GRE scores are not required",
        "url": "https://gradschool.sites.unc.edu/computer-science/"
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
        "url": "https://gradschool.sites.unc.edu/computer-science/"
      },
      "funding": {
        "code": "Typical",
        "value": "Computer Science Research and Teaching Assistantships consideration for applicants by January 5.",
        "quote": "Computer Science Research and Teaching Assistantships January 5, 2027",
        "url": "https://gradschool.sites.unc.edu/computer-science/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--chemistry",
    "university": "unc",
    "field": "chemistry",
    "also_fields": [],
    "department": "Department of Chemistry",
    "program_page": "https://gradschool.sites.unc.edu/chemistry/",
    "checked": "2026-10-30",
    "notes": "Chemistry Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Doctoral PhD CHEM Fall* December 15, 2026",
        "url": "https://gradschool.sites.unc.edu/chemistry/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required for admission.",
        "quote": "GRE not required",
        "url": "https://gradschool.sites.unc.edu/chemistry/"
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
        "url": "https://gradschool.sites.unc.edu/chemistry/"
      },
      "funding": {
        "code": "Typical",
        "value": "Academic Program Aid and Financial Assistance recommended deadline December 15.",
        "quote": "Academic Program Aid/Financial Assistance December 15, 2026 (Recommended)",
        "url": "https://gradschool.sites.unc.edu/chemistry/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--math",
    "university": "unc",
    "field": "math",
    "also_fields": [],
    "department": "Department of Mathematics",
    "program_page": "https://gradschool.sites.unc.edu/mathematics/",
    "checked": "2026-10-30",
    "notes": "Mathematics Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline.",
        "quote": "Doctoral PhD MATH Fall* December 1, 2026",
        "url": "https://gradschool.sites.unc.edu/mathematics/"
      },
      "gre_general": {
        "code": "Optional",
        "value": "GRE General and Subject exams are optional.",
        "quote": "Test Requirements GRE General and Subject exams are optional",
        "url": "https://gradschool.sites.unc.edu/mathematics/"
      },
      "gre_subject": {
        "code": "Optional",
        "value": "GRE General and Subject exams are optional.",
        "quote": "Test Requirements GRE General and Subject exams are optional",
        "url": "https://gradschool.sites.unc.edu/mathematics/"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://gradschool.sites.unc.edu/mathematics/"
      },
      "funding": {
        "code": "Typical",
        "value": "Fall Graduate School Fellowships consideration by December 15.",
        "quote": "Fall Graduate School Fellowships December 15, 2026",
        "url": "https://gradschool.sites.unc.edu/mathematics/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--statistics",
    "university": "unc",
    "field": "statistics",
    "also_fields": [],
    "department": "Department of Statistics and Operations Research",
    "program_page": "https://gradschool.sites.unc.edu/statistics-and-operations-research/",
    "checked": "2026-10-30",
    "notes": "Statistics and Operations Research Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Doctoral – Statistics and Operations Research PhD STOR Fall December 15, 2026",
        "url": "https://gradschool.sites.unc.edu/statistics-and-operations-research/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required.",
        "quote": "Test Requirements GRE not required",
        "url": "https://gradschool.sites.unc.edu/statistics-and-operations-research/"
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
        "url": "https://gradschool.sites.unc.edu/statistics-and-operations-research/"
      },
      "funding": {
        "code": "Typical",
        "value": "Fall Graduate School Fellowships consideration by December 15.",
        "quote": "Fall Graduate School Fellowships December 15, 2026",
        "url": "https://gradschool.sites.unc.edu/statistics-and-operations-research/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--biology",
    "university": "unc",
    "field": "biology",
    "also_fields": [],
    "department": "Department of Biology",
    "program_page": "https://gradschool.sites.unc.edu/biology/",
    "checked": "2026-10-30",
    "notes": "Biology Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-11-17",
        "value": "November 17 PhD application deadline.",
        "quote": "Doctoral PhD BIOL Fall* November 17, 2026",
        "url": "https://gradschool.sites.unc.edu/biology/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required.",
        "quote": "GRE not required",
        "url": "https://gradschool.sites.unc.edu/biology/"
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
        "url": "https://gradschool.sites.unc.edu/biology/"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on program profile.",
        "quote": "",
        "url": "https://gradschool.sites.unc.edu/biology/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--biomed",
    "university": "unc",
    "field": "biomed",
    "also_fields": [],
    "department": "Biological and Biomedical Sciences Program (BBSP)",
    "program_page": "https://gradschool.sites.unc.edu/biological-and-biomedical-sciences/",
    "checked": "2026-10-30",
    "notes": "Biological and Biomedical Sciences Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-11-17",
        "value": "November 17 PhD application deadline.",
        "quote": "Doctoral PhD BBSP Fall* November 17, 2026",
        "url": "https://gradschool.sites.unc.edu/biological-and-biomedical-sciences/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE scores are neither required nor typically recommended.",
        "quote": "GRE scores are neither required nor typically recommended",
        "url": "https://gradschool.sites.unc.edu/biological-and-biomedical-sciences/"
      },
      "gre_subject": {
        "code": "No subject test",
        "value": "ETS offers no subject test in this discipline.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified; lab rotations in first year.",
        "quote": "",
        "url": "https://gradschool.sites.unc.edu/biological-and-biomedical-sciences/"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on program profile.",
        "quote": "",
        "url": "https://gradschool.sites.unc.edu/biological-and-biomedical-sciences/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--bme",
    "university": "unc",
    "field": "bme",
    "also_fields": [],
    "department": "Joint Department of Biomedical Engineering",
    "program_page": "https://gradschool.sites.unc.edu/biomedical-engineering/",
    "checked": "2026-10-30",
    "notes": "Biomedical Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline.",
        "quote": "Doctoral PhD BMEJ Fall* December 1, 2026",
        "url": "https://gradschool.sites.unc.edu/biomedical-engineering/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required.",
        "quote": "GRE not required",
        "url": "https://gradschool.sites.unc.edu/biomedical-engineering/"
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
        "url": "https://gradschool.sites.unc.edu/biomedical-engineering/"
      },
      "funding": {
        "code": "Typical",
        "value": "Application must be completed by December 19 to be considered for departmental financial support.",
        "quote": "To be considered for departmental financial support, your application must be completed by December 19th.",
        "url": "https://gradschool.sites.unc.edu/biomedical-engineering/"
      },
      "entry_route": unc_entry_route
    }
  },
  {
    "id": "unc--datasci",
    "university": "unc",
    "field": "datasci",
    "also_fields": [],
    "department": "Department of Biostatistics",
    "program_page": "https://gradschool.sites.unc.edu/biostatistics/",
    "checked": "2026-10-30",
    "notes": "Biostatistics Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline.",
        "quote": "Doctoral PhD BIOS Fall* December 1, 2026",
        "url": "https://gradschool.sites.unc.edu/biostatistics/"
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required.",
        "quote": "GRE not required",
        "url": "https://gradschool.sites.unc.edu/biostatistics/"
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
        "url": "https://gradschool.sites.unc.edu/biostatistics/"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on program profile.",
        "quote": "",
        "url": "https://gradschool.sites.unc.edu/biostatistics/"
      },
      "entry_route": unc_entry_route
    }
  }
]

for prog in programs:
  (prog_dir / f"{prog['id']}.json").write_text(json.dumps(prog, indent=2), encoding="utf-8")

print(f"Generated unc.json and {len(programs)} program records.")
