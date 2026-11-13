import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

coe_deadlines_url = "https://www.engin.umich.edu/admissions/graduate-professional/deadlines/"

# University record
umich_data = {
  "id": "umich",
  "institution": "University of Michigan",
  "country": "USA",
  "region": "Michigan",
  "grad_page": "https://rackham.umich.edu/admissions/",
  "checked": "2026-10-30",
  "notes": "Application fee is $75 for US citizens/permanent residents and $90 for non-US citizens.",
  "fields": {
    "app_fee": {
      "code": "75 USD",
      "value": "Application fee is $75 for US citizens and permanent residents, and $90 for non-US citizens.",
      "quote": "United States citizens and those with permanent resident visa status: $75",
      "url": "https://rackham.umich.edu/admissions/applying/application-fee-and-payment/"
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Rackham fee waivers available for US citizens and permanent residents who have demonstrated financial need.",
      "quote": "At this time, Rackham application fee waivers are available for U.S. citizens and permanent residents who have demonstrated financial need.",
      "url": "https://rackham.umich.edu/admissions/applying/application-fee-and-payment/"
    },
    "gre_general": {
      "code": "Not considered",
      "value": "GRE general test scores are no longer included in the admissions process for Rackham doctoral programs.",
      "quote": "GRE general test scores are no longer included in the admissions process for Rackham’s doctoral programs.",
      "url": "https://rackham.umich.edu/admissions/applying/tests/"
    },
    "toefl_min": {
      "code": "84",
      "value": "Minimum required TOEFL iBT score is 84.",
      "quote": "Before January 21, 2026 = 84.",
      "url": "https://rackham.umich.edu/admissions/applying/tests/"
    },
    "ielts_min": {
      "code": "6.5",
      "value": "Minimum required overall IELTS score is 6.5 Academic.",
      "quote": "Academic version 6.5",
      "url": "https://rackham.umich.edu/admissions/applying/tests/"
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "Exemption granted if applicant completed undergraduate degree where instruction is English only.",
      "quote": "You completed all of your undergraduate education and earned an undergraduate degree at an institution where the language of instruction is English only.",
      "url": "https://rackham.umich.edu/admissions/applying/tests/"
    }
  }
}

(uni_dir / "umich.json").write_text(json.dumps(umich_data, indent=2), encoding="utf-8")

umich_entry_route = {
  "code": "Direct from bachelor's",
  "value": "Earned undergraduate degree at an accredited institution required for graduate admission.",
  "quote": "You completed all of your undergraduate education and earned an undergraduate degree at an institution where the language of instruction is English only.",
  "url": "https://rackham.umich.edu/admissions/applying/tests/"
}

programs = [
  {
    "id": "umich--physics",
    "university": "umich",
    "field": "physics",
    "also_fields": [],
    "department": "Applied Physics Program",
    "program_page": "https://lsa.umich.edu/appliedphysics",
    "checked": "2026-10-30",
    "notes": "Applied Physics Ph.D.",
    "fields": {
      "deadline": {
        "code": "2027-01-05",
        "value": "January 5 PhD application deadline.",
        "quote": "Applied Physics N/A – See bridge program Jan 5",
        "url": coe_deadlines_url
      },
      "gre_subject": {
        "code": "Not stated",
        "value": "GRE Subject test requirements determined by program.",
        "quote": "",
        "url": "https://lsa.umich.edu/appliedphysics"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://lsa.umich.edu/appliedphysics"
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on program home page.",
        "quote": "",
        "url": "https://lsa.umich.edu/appliedphysics"
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--cs",
    "university": "umich",
    "field": "cs",
    "also_fields": [],
    "department": "Computer Science and Engineering",
    "program_page": "https://cse.engin.umich.edu/academics/graduate/funding/",
    "checked": "2026-10-30",
    "notes": "Computer Science and Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Computer Science and Engineering Jan 15 Dec 15",
        "url": coe_deadlines_url
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
        "url": "https://cse.engin.umich.edu/academics/graduate/funding/"
      },
      "funding": {
        "code": "Guaranteed",
        "value": "All CSE PhD students receive guaranteed financial aid covering tuition, fees, stipend, and health insurance.",
        "quote": "All CSE guaranteed financial aid (PhD) students are placed first.",
        "url": "https://cse.engin.umich.edu/academics/graduate/funding/"
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--chemistry",
    "university": "umich",
    "field": "chemistry",
    "also_fields": [],
    "department": "Department of Chemistry",
    "program_page": "https://lsa.umich.edu/chem/graduates/phd-program.html",
    "checked": "2026-10-30",
    "notes": "Chemistry Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 application deadline for all applicants.",
        "quote": "December 1 for all applicants.",
        "url": "https://lsa.umich.edu/chem/graduates/phd-program/how-to-apply.html"
      },
      "gre_subject": {
        "code": "Not considered",
        "value": "GRE subject scores are not required nor reviewed for admission.",
        "quote": "Note that GRE scores (general and subject) are NOT required for admission, nor are they reviewed.",
        "url": "https://lsa.umich.edu/chem/graduates/phd-program/how-to-apply.html"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Rotations in any of 50 research groups; prior contact not specified.",
        "quote": "",
        "url": "https://lsa.umich.edu/chem/graduates/phd-program.html"
      },
      "funding": {
        "code": "Guaranteed",
        "value": "PhD students are fully-funded during their tenure with competitive stipend and healthcare coverage.",
        "quote": "Our PhD students are fully-funded during their tenure here.",
        "url": "https://lsa.umich.edu/chem/graduates/phd-program.html"
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--math",
    "university": "umich",
    "field": "math",
    "also_fields": [],
    "department": "Department of Mathematics",
    "program_page": "https://lsa.umich.edu/math/graduates/Admissions.html",
    "checked": "2026-10-30",
    "notes": "Mathematics Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Ph.D. Admissions: Application deadline is December 15, 2026.",
        "url": "https://lsa.umich.edu/math/graduates/Admissions.html"
      },
      "gre_subject": {
        "code": "Not stated",
        "value": "GRE Subject test requirements determined by department.",
        "quote": "",
        "url": "https://lsa.umich.edu/math/graduates/Admissions.html"
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Advisor contact prior to admission not specified.",
        "quote": "",
        "url": "https://lsa.umich.edu/math/graduates/Admissions.html"
      },
      "funding": {
        "code": "Guaranteed",
        "value": "All PhD students receive support in the form of GSI, GSRA, and fellowships.",
        "quote": "All of these students received support from the Department in the form of Graduate Student Instructorships, Graduate Student Research Assistantships, and fellowships.",
        "url": "https://lsa.umich.edu/math/graduates/Admissions.html"
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--statistics",
    "university": "umich",
    "field": "statistics",
    "also_fields": [],
    "department": "Department of Statistics",
    "program_page": "https://lsa.umich.edu/stats/phd-students/ProspectiveGraduateStudents/graduate-degree-application.html",
    "checked": "2026-10-30",
    "notes": "Statistics Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 application deadline for Fall admission.",
        "quote": "Applications for Fall admission to the PhD program in Statistics are due December 15.",
        "url": "https://lsa.umich.edu/stats/phd-students/ProspectiveGraduateStudents/graduate-degree-application.html"
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
        "url": "https://lsa.umich.edu/stats/phd-students/ProspectiveGraduateStudents/graduate-degree-application.html"
      },
      "funding": {
        "code": "Typical",
        "value": "Faculty frequently support senior PhD students as research assistants on federally funded research grants.",
        "quote": "Most faculty have multiple federally funded research grants and frequently support their senior Ph.D. students as research assistants.",
        "url": "https://lsa.umich.edu/stats/phd-students/ProspectiveGraduateStudents.html"
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--bme",
    "university": "umich",
    "field": "bme",
    "also_fields": [],
    "department": "Department of Biomedical Engineering",
    "program_page": coe_deadlines_url,
    "checked": "2026-10-30",
    "notes": "Biomedical Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline.",
        "quote": "Biomedical Engineering Jan 15 Dec 1",
        "url": coe_deadlines_url
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
        "url": coe_deadlines_url
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on central deadline page.",
        "quote": "",
        "url": coe_deadlines_url
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--chemeng",
    "university": "umich",
    "field": "chemeng",
    "also_fields": [],
    "department": "Department of Chemical Engineering",
    "program_page": coe_deadlines_url,
    "checked": "2026-10-30",
    "notes": "Chemical Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline.",
        "quote": "Chemical Engineering Jan 15 Dec 1",
        "url": coe_deadlines_url
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
        "url": coe_deadlines_url
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on central deadline page.",
        "quote": "",
        "url": coe_deadlines_url
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--civil",
    "university": "umich",
    "field": "civil",
    "also_fields": [],
    "department": "Department of Civil and Environmental Engineering",
    "program_page": coe_deadlines_url,
    "checked": "2026-10-30",
    "notes": "Civil and Environmental Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Civil and Environmental Engineering Jan 15 Dec 15",
        "url": coe_deadlines_url
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
        "url": coe_deadlines_url
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on central deadline page.",
        "quote": "",
        "url": coe_deadlines_url
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--ece",
    "university": "umich",
    "field": "ece",
    "also_fields": [],
    "department": "Department of Electrical and Computer Engineering",
    "program_page": coe_deadlines_url,
    "checked": "2026-10-30",
    "notes": "Electrical and Computer Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Electrical and Computer Engineering Jan 15 Dec 15",
        "url": coe_deadlines_url
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
        "url": coe_deadlines_url
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on central deadline page.",
        "quote": "",
        "url": coe_deadlines_url
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--materials",
    "university": "umich",
    "field": "materials",
    "also_fields": [],
    "department": "Department of Materials Science and Engineering",
    "program_page": coe_deadlines_url,
    "checked": "2026-10-30",
    "notes": "Materials Science and Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 PhD application deadline.",
        "quote": "Materials Science and Engineering Jan 15 Dec 15",
        "url": coe_deadlines_url
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
        "url": coe_deadlines_url
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on central deadline page.",
        "quote": "",
        "url": coe_deadlines_url
      },
      "entry_route": umich_entry_route
    }
  },
  {
    "id": "umich--mech",
    "university": "umich",
    "field": "mech",
    "also_fields": [],
    "department": "Department of Mechanical Engineering",
    "program_page": coe_deadlines_url,
    "checked": "2026-10-30",
    "notes": "Mechanical Engineering Ph.D.",
    "fields": {
      "deadline": {
        "code": "2026-12-01",
        "value": "December 1 PhD application deadline.",
        "quote": "Mechanical Engineering Jan 15 Dec 1",
        "url": coe_deadlines_url
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
        "url": coe_deadlines_url
      },
      "funding": {
        "code": "Not stated",
        "value": "Funding details not stated on central deadline page.",
        "quote": "",
        "url": coe_deadlines_url
      },
      "entry_route": umich_entry_route
    }
  }
]

for prog in programs:
  (prog_dir / f"{prog['id']}.json").write_text(json.dumps(prog, indent=2), encoding="utf-8")

print(f"Generated umich.json and {len(programs)} program records.")
