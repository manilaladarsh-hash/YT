import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

how_to_apply = "https://graduatestudies.uoregon.edu/apply/how-to-apply"
waivers_url = "https://graduatestudies.uoregon.edu/apply/application-fee-waivers-discounts"
intl_url = "https://graduatestudies.uoregon.edu/apply/international-applicants"
math_adm_url = "https://naturalsciences.uoregon.edu/mathematics/apply/graduate-admissions"

# University record
uoregon_data = {
  "id": "uoregon",
  "institution": "University of Oregon",
  "country": "USA",
  "region": "Oregon",
  "grad_page": how_to_apply,
  "checked": "2026-10-30",
  "notes": "Application fee is $70 domestic, $90 international.",
  "fields": {
    "app_fee": {
      "code": "70 USD",
      "value": "Application fee of $70 for domestic applicants and $90 for international applicants.",
      "quote": "Domestic applicants: $70 | International applicants: $90",
      "url": how_to_apply
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Limited full fee waivers for international applicants with significant financial need who are nominated by their prospective program.",
      "quote": "We offer a limited number of full fee waivers for international applicants with significant financial need. Applicants must be nominated by their prospective program.",
      "url": waivers_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "GRE requirements determined by each graduate program.",
      "quote": "Submit GMAT or GRE scores (if required by your program)",
      "url": how_to_apply
    },
    "toefl_min": {
      "code": "88",
      "value": "Minimum TOEFL iBT score of 88.",
      "quote": "88 or 4.5",
      "url": intl_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Minimum IELTS score of 7.0 overall band score.",
      "quote": "7.0 Overall Band Score",
      "url": intl_url
    },
    "english_waiver": {
      "code": "No",
      "value": "English-medium-of-instruction certificates not accepted in place of approved documentation.",
      "quote": "The University of Oregon does not accept English-medium-of-instruction certificates in place of approved English proficiency documentation.",
      "url": intl_url
    }
  }
}
(uni_dir / "uoregon.json").write_text(json.dumps(uoregon_data, indent=2), encoding="utf-8")

common_entry_route = {
  "code": "Direct from bachelor's",
  "value": "Bachelor's degree or expected attainment by end of summer required for admission.",
  "quote": "To be considered for admission, you must have a bachelor’s degree or expect to attain one by the end of summer 2027.",
  "url": math_adm_url
}

# 1. Biology (also covers neuro)
bio_adm_url = "https://naturalsciences.uoregon.edu/biology/apply/graduate-admissions"
bio_prog_url = "https://naturalsciences.uoregon.edu/biology/graduate-programs"
bio_prog = {
  "id": "uoregon--biology",
  "university": "uoregon",
  "field": "biology",
  "also_fields": ["neuro"],
  "department": "Department of Biology",
  "program_page": bio_adm_url,
  "checked": "2026-10-30",
  "notes": "Biology PhD, housing training in Institute of Neuroscience, Institute of Molecular Biology, Institute of Ecology & Evolution, and Oregon Institute of Marine Biology.",
  "fields": {
    "deadline": {
      "code": "2026-12-02",
      "value": "December 2 application deadline for Fall admission.",
      "quote": "The deadline to apply is December 2, 2026.",
      "url": bio_adm_url
    },
    "gre_general": {
      "code": "Not considered",
      "value": "GRE scores are no longer considered in the application review process.",
      "quote": "IMPORTANT: GRE scores are no longer considered in our application review process. You will not see a place for them on the application and you do not need to send in a score report.",
      "url": bio_adm_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Biology.",
      "quote": ets_quote,
      "url": ets_url
    },
    "toefl_min": {
      "code": "105",
      "value": "Minimum TOEFL iBT score of 105.",
      "quote": "internet-based test =105, or 5.0 under the new 1–6 scale",
      "url": bio_adm_url
    },
    "ielts_min": {
      "code": "7.5",
      "value": "Minimum IELTS score of 7.5.",
      "quote": "IELTS: 7.5",
      "url": bio_adm_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": bio_adm_url
    },
    "funding": {
      "code": "Typical",
      "value": "Funding provided for doctoral students through Department and associated research institute resources (TAs and RAs).",
      "quote": "Funding is provided for doctoral students through a combination of Department of Biology and associated research institute resources.",
      "url": bio_prog_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "uoregon--biology.json").write_text(json.dumps(bio_prog, indent=2), encoding="utf-8")

# 2. Chemistry
chem_adm_url = "https://naturalsciences.uoregon.edu/chemistry-biochemistry/apply/graduate-admissions"
chem_apply_url = "https://naturalsciences.uoregon.edu/chemistry-biochemistry/apply"
chem_prog = {
  "id": "uoregon--chemistry",
  "university": "uoregon",
  "field": "chemistry",
  "also_fields": [],
  "department": "Department of Chemistry and Biochemistry",
  "program_page": chem_adm_url,
  "checked": "2026-10-30",
  "notes": "Chemistry PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-02",
      "value": "December 2 priority application deadline for Fall admission.",
      "quote": "The priority deadline for applications is December 2, 2026.",
      "url": chem_adm_url
    },
    "gre_general": {
      "code": "Optional",
      "value": "GRE general test is optional.",
      "quote": "The GRE general test (verbal, quantitative, analytical/writing) is optional for all applicants.",
      "url": chem_adm_url
    },
    "gre_subject": {
      "code": "Not required",
      "value": "The GRE subject test is not required.",
      "quote": "The GRE subject test is not required.",
      "url": chem_adm_url
    },
    "toefl_min": {
      "code": "90",
      "value": "Minimum TOEFL iBT score of 90 with speaking score of 26.",
      "quote": "Minimum Score: 90 or 4.5 (scores after January 21, 2026) with a speaking score of 26.",
      "url": chem_adm_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Minimum IELTS score of 7.0 overall band score.",
      "quote": "7.0 Overall Band Score",
      "url": intl_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": chem_adm_url
    },
    "funding": {
      "code": "Guaranteed",
      "value": "Students accepted into the doctoral program receive financial support in the form of teaching and research assistantships.",
      "quote": "Students accepted into the doctoral program receive financial support in the form of teaching and research assistantships unless other arrangements are made.",
      "url": chem_apply_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "uoregon--chemistry.json").write_text(json.dumps(chem_prog, indent=2), encoding="utf-8")

# 3. Computer Science
cs_adm_url = "https://scds.uoregon.edu/graduate-programs/admissions"
cs_prog = {
  "id": "uoregon--cs",
  "university": "uoregon",
  "field": "cs",
  "also_fields": [],
  "department": "School of Computer and Data Sciences",
  "program_page": cs_adm_url,
  "checked": "2026-10-30",
  "notes": "Computer Science PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-15",
      "value": "December 15 application deadline for Fall admission.",
      "quote": "December 15, 2026",
      "url": cs_adm_url
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE is required for the Computer Science PhD program.",
      "quote": "Only required for the Computer Science PhD program.",
      "url": cs_adm_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Computer Science.",
      "quote": ets_quote,
      "url": ets_url
    },
    "toefl_min": {
      "code": "100",
      "value": "Minimum TOEFL iBT score of 100.",
      "quote": "iBt (internet based TOEFL) = 100 (or 5.0 with the new scoring system)",
      "url": cs_adm_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Minimum IELTS score of 7.",
      "quote": "IELTS (International English Language Testing System) = 7",
      "url": cs_adm_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": cs_adm_url
    },
    "funding": {
      "code": "Not stated",
      "value": "Funding details not stated on admissions page.",
      "quote": "",
      "url": cs_adm_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "uoregon--cs.json").write_text(json.dumps(cs_prog, indent=2), encoding="utf-8")

# 4. Earth Sciences
earth_adm_url = "https://naturalsciences.uoregon.edu/earth-sciences/apply/graduate-admissions"
earth_prog = {
  "id": "uoregon--earth",
  "university": "uoregon",
  "field": "earth",
  "also_fields": [],
  "department": "Department of Earth Sciences",
  "program_page": earth_adm_url,
  "checked": "2026-10-30",
  "notes": "Earth Sciences PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-22",
      "value": "December 22 application deadline.",
      "quote": "The online application will close at the end of the day on December 22.",
      "url": earth_adm_url
    },
    "gre_general": {
      "code": "Not considered",
      "value": "No longer considering the GRE in applications.",
      "quote": "No. We are no longer considering the GRE in our applications.",
      "url": earth_adm_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Earth Sciences.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "Prospective students are encouraged to contact faculty regarding research opportunities.",
      "quote": "Prospective students are encouraged to browse the webpages of individual faculty members and inquire about research opportunities by contacting faculty via email.",
      "url": earth_adm_url
    },
    "funding": {
      "code": "Typical",
      "value": "Students typically receive graduate employee positions that provide tuition waivers, health insurance, and a stipend.",
      "quote": "Our students typically receive graduate employee positions that provide tuition waivers, health insurance, and a stipend.",
      "url": earth_adm_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "uoregon--earth.json").write_text(json.dumps(earth_prog, indent=2), encoding="utf-8")

# 5. Mathematics
math_prog = {
  "id": "uoregon--math",
  "university": "uoregon",
  "field": "math",
  "also_fields": [],
  "department": "Department of Mathematics",
  "program_page": math_adm_url,
  "checked": "2026-10-30",
  "notes": "Mathematics PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-15",
      "value": "January 15 application deadline for Fall admission.",
      "quote": "all of your materials must be received by the application deadline of January 15, 2027.",
      "url": math_adm_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "GRE general test requirement not stated on admissions page.",
      "quote": "",
      "url": math_adm_url
    },
    "gre_subject": {
      "code": "Recommended",
      "value": "Math subject GRE scores are recommended but not required.",
      "quote": "Math subject GRE scores are recommended but not required—the University of Oregon’s Institution Code is 4846.",
      "url": math_adm_url
    },
    "toefl_min": {
      "code": "100",
      "value": "Minimum TOEFL iBT score of 100 with at least 26 on speaking.",
      "quote": "TOEFL internet-based test: score of 100 or better (on the 0-120 scale) or 5 or better (on the new 1-6 scale), with at least 26 (on the 0-30 scale) or 5 (on the new 1-6 scale) on the speaking section.",
      "url": math_adm_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Minimum IELTS score of 7.0 overall band score.",
      "quote": "IELTS exam: overall band score of 7.0 or better, with at least 7.0 on the speaking band.",
      "url": math_adm_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": math_adm_url
    },
    "funding": {
      "code": "Guaranteed",
      "value": "All admitted doctoral students are supported by Graduate Employee positions with stipend, full tuition waiver, and health insurance.",
      "quote": "all of whom are supported by Graduate Employee positions that carry a stipend, full tuition waiver, and health insurance.",
      "url": math_adm_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "uoregon--math.json").write_text(json.dumps(math_prog, indent=2), encoding="utf-8")

# 6. Physics
phys_adm_url = "https://naturalsciences.uoregon.edu/physics/apply/graduate-admissions"
phys_prog = {
  "id": "uoregon--physics",
  "university": "uoregon",
  "field": "physics",
  "also_fields": [],
  "department": "Department of Physics",
  "program_page": phys_adm_url,
  "checked": "2026-10-30",
  "notes": "Physics PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-12",
      "value": "January 12 application deadline for Fall admission.",
      "quote": "We are currently accepting applications for Fall 2027 PhD admission with an application deadline of January 12, 2027.",
      "url": phys_adm_url
    },
    "gre_general": {
      "code": "Optional",
      "value": "GRE general scores are optional.",
      "quote": "GRE Scores (Optional)",
      "url": phys_adm_url
    },
    "gre_subject": {
      "code": "Optional",
      "value": "GRE subject scores optional; ideally received before January 15.",
      "quote": "Ideally, applicants should take the GRE test(s) in time for the official results to arrive before the January 15 deadline.",
      "url": phys_adm_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "List any research areas of interest and faculty members of interest.",
      "quote": "List any research areas of interest to you as well as faculty members you would be interested in working with. This section is not required for MS applicants.",
      "url": phys_adm_url
    },
    "funding": {
      "code": "Typical",
      "value": "PhD applicants applying by deadline are automatically considered for fellowships and awards.",
      "quote": "Students who apply to our PhD program by the deadline are automatically considered for a number of fellowships and/or awards that support graduate student success.",
      "url": phys_adm_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "uoregon--physics.json").write_text(json.dumps(phys_prog, indent=2), encoding="utf-8")

print("Created UOregon university and 6 program staging records successfully!")
