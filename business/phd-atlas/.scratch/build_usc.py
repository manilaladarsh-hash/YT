import json
from pathlib import Path

staging = Path("data/staging")
uni_dir = staging / "universities"
prog_dir = staging / "programs"
uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

apply_url = "https://gradadm.usc.edu/domestic-students/how-to-apply/"
waivers_url = "https://gradadm.usc.edu/tools-resources/fee-waivers/"
eng_url = "https://gradadm.usc.edu/prospective-international-students/english-proficiency/"

# University record
usc_data = {
  "id": "usc",
  "institution": "University of Southern California",
  "country": "USA",
  "region": "California",
  "grad_page": apply_url,
  "checked": "2026-10-30",
  "notes": "Application fee is $120 for most graduate programs.",
  "fields": {
    "app_fee": {
      "code": "120 USD",
      "value": "Application fee of $120 for most USC graduate programs.",
      "quote": "The application fee for most USC graduate programs is $120 ($105 for programs beginning in fall 2026).",
      "url": apply_url
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Fee waivers available for Fulbright applicants or applicants whose graduate program informs them they will pay the fee; financial hardship waivers are domestic only.",
      "quote": "This option is not available to international students. | Eligibility Requirements: Your intended graduate program has informed you in writing that they will be paying for your USC application fee.",
      "url": waivers_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Most graduate programs require GRE or GMAT scores; check program website for specific requirements.",
      "quote": "Most USC graduate programs require either GRE or GMAT scores. Please review your program’s website for their test score requirements.",
      "url": apply_url
    },
    "toefl_min": {
      "code": "100",
      "value": "Minimum TOEFL score of 100 with 20 in each section for PhD programs.",
      "quote": "100 or above, with 20 or above in each section.",
      "url": eng_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "Minimum IELTS score of 7 or above with 6 on each band for PhD programs.",
      "quote": "7 or above, with 6 or above on each band.",
      "url": eng_url
    },
    "english_waiver": {
      "code": "No",
      "value": "USC does not waive English proficiency based on English-taught programs in non-Anglophone countries.",
      "quote": "USC does not waive the English-proficiency requirement based on any other consideration such as work experience, ESL enrollment, amount of time spent in the U.S., etc. It also cannot be waived on the basis of programs taught in English in non-Anglophone countries.",
      "url": eng_url
    }
  }
}
(uni_dir / "usc.json").write_text(json.dumps(usc_data, indent=2), encoding="utf-8")

common_entry_route = {
  "code": "Direct from bachelor's",
  "value": "Bachelor's degree from a regionally accredited U.S. university or equivalent required.",
  "quote": "You hold a bachelor’s degree from a regionally accredited university in the United States or the equivalent of a U.S. bachelor’s degree from an officially recognized university in another qualifying Anglophone country where English is both the only official language and the language of instruction.",
  "url": eng_url
}

viterbi_apply = "https://viterbigradadmission.usc.edu/doctoral/how-to-apply-phd/"
viterbi_faq = "https://viterbigradadmission.usc.edu/doctoral/phd-faq/"

# Common viterbi program generator
def make_viterbi_prog(field_id, field_name, dept_name):
  return {
    "id": f"usc--{field_id}",
    "university": "usc",
    "field": field_id,
    "also_fields": [],
    "department": dept_name,
    "program_page": viterbi_apply,
    "checked": "2026-10-30",
    "notes": f"{field_name} PhD.",
    "fields": {
      "deadline": {
        "code": "2026-12-15",
        "value": "December 15 application deadline for Fall admission.",
        "quote": "Fall 2027 deadline: December 15, 2026",
        "url": viterbi_apply
      },
      "gre_general": {
        "code": "Not required",
        "value": "GRE not required for Viterbi School PhD programs except ASTE and ISE.",
        "quote": "GRE Not Required (2027 Applications): All Viterbi School PhD programs except ASTE and ISE",
        "url": viterbi_apply
      },
      "gre_subject": {
        "code": "No subject test",
        "value": f"ETS offers no GRE Subject Test in {field_name}.",
        "quote": ets_quote,
        "url": ets_url
      },
      "supervisor": {
        "code": "Not stated",
        "value": "Prior supervisor contact not specified.",
        "quote": "",
        "url": viterbi_apply
      },
      "funding": {
        "code": "Typical",
        "value": "USC tries to fully fund all of its doctoral students with tuition, stipend, and health benefits.",
        "quote": "USC tries to fully fund all of its doctoral students. This generally consists of tuition, a stipend for living expenses, and a health benefits package.",
        "url": viterbi_faq
      },
      "entry_route": common_entry_route
    }
  }

# Viterbi programs
viterbi_progs = [
  ("cs", "Computer Science", "Department of Computer Science"),
  ("bme", "Biomedical Engineering", "Department of Biomedical Engineering"),
  ("chemeng", "Chemical Engineering", "Mork Family Department of Chemical Engineering and Materials Science"),
  ("civil", "Civil Engineering", "Sonny Astani Department of Civil and Environmental Engineering"),
  ("ece", "Electrical and Computer Engineering", "Ming Hsieh Department of Electrical and Computer Engineering"),
  ("materials", "Materials Science", "Mork Family Department of Chemical Engineering and Materials Science"),
  ("mech", "Mechanical Engineering", "Department of Aerospace and Mechanical Engineering"),
]

for fid, fname, dname in viterbi_progs:
  pdata = make_viterbi_prog(fid, fname, dname)
  (prog_dir / f"usc--{fid}.json").write_text(json.dumps(pdata, indent=2), encoding="utf-8")

# Dornsife programs
# 8. Physics
phys_url = "https://dornsife.usc.edu/physics/graduate-admissions/"
phys_prog = {
  "id": "usc--physics",
  "university": "usc",
  "field": "physics",
  "also_fields": [],
  "department": "Department of Physics and Astronomy",
  "program_page": phys_url,
  "checked": "2026-10-30",
  "notes": "Physics PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-15",
      "value": "December 15 application deadline.",
      "quote": "The deadline for submission of applications is December 15, 2026.",
      "url": phys_url
    },
    "gre_general": {
      "code": "Not required",
      "value": "General GRE not required.",
      "quote": "Do not require general GRE",
      "url": phys_url
    },
    "gre_subject": {
      "code": "Recommended",
      "value": "Physics GRE subject test is recommended.",
      "quote": "For the Physics PhD program, the Physics GRE is recommended.",
      "url": phys_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": phys_url
    },
    "funding": {
      "code": "Typical",
      "value": "Department provides Fee Waiver Memo to ensure application fee is paid by department for selected students.",
      "quote": "Your Fee Waiver Memo is also necessary to ensure your application fee is paid for by the department.",
      "url": phys_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "usc--physics.json").write_text(json.dumps(phys_prog, indent=2), encoding="utf-8")

# 9. Chemistry
chem_url = "https://dornsife.usc.edu/chemistry/graduate-admission/"
chem_prog = {
  "id": "usc--chemistry",
  "university": "usc",
  "field": "chemistry",
  "also_fields": [],
  "department": "Department of Chemistry",
  "program_page": chem_url,
  "checked": "2026-10-30",
  "notes": "Chemistry PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-18",
      "value": "December 18 application deadline.",
      "quote": "Application deadline: The deadline for submission of applications is December 18, 2026. All application materials, including transcripts and letters of recommendation, must be submitted by this date.",
      "url": chem_url
    },
    "gre_general": {
      "code": "Not required",
      "value": "General GRE not required.",
      "quote": "We do not require subject or general GRE",
      "url": chem_url
    },
    "gre_subject": {
      "code": "Not required",
      "value": "Subject GRE not required.",
      "quote": "We do not require subject or general GRE",
      "url": chem_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": chem_url
    },
    "funding": {
      "code": "Typical",
      "value": "Early admission and university-sponsored fellowships offered to qualified candidates.",
      "quote": "often offer early admission and university-sponsored fellowships to qualified candidates",
      "url": chem_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "usc--chemistry.json").write_text(json.dumps(chem_prog, indent=2), encoding="utf-8")

# 10. Mathematics
math_url = "https://dornsife.usc.edu/mathematics/admissions/"
math_prog = {
  "id": "usc--math",
  "university": "usc",
  "field": "math",
  "also_fields": [],
  "department": "Department of Mathematics",
  "program_page": math_url,
  "checked": "2026-10-30",
  "notes": "Mathematics PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-15",
      "value": "December 15 application deadline.",
      "quote": "Application Deadline: December 15",
      "url": math_url
    },
    "gre_general": {
      "code": "Not considered",
      "value": "GRE general test is not considered as part of application review.",
      "quote": "No. We do not require GRE scores. If you choose to include the GRE mathematics subject test in your application, we will factor your score into our review. However we do not consider the GRE general test or other subject tests as part of our application review.",
      "url": math_url
    },
    "gre_subject": {
      "code": "Optional",
      "value": "GRE mathematics subject test score factored into review if included.",
      "quote": "However, students coming from lesser known schools or with non-traditional paths are encouraged to include a GRE mathematics subject test score in their applications.",
      "url": math_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Prior supervisor contact not specified.",
      "quote": "",
      "url": math_url
    },
    "funding": {
      "code": "Guaranteed",
      "value": "All admitted students receive comprehensive support with full tuition remission, competitive stipend, and health insurance.",
      "quote": "Everyone, regardless of nationality or country of residence, admitted to our PhD Programs receives a comprehensive support package that includes full tuition remission, a competitive stipend, and health and dental insurance.",
      "url": math_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "usc--math.json").write_text(json.dumps(math_prog, indent=2), encoding="utf-8")

# 11. Earth Sciences
earth_url = "https://dornsife.usc.edu/earth/graduate/grad-admissions/"
earth_prog = {
  "id": "usc--earth",
  "university": "usc",
  "field": "earth",
  "also_fields": [],
  "department": "Department of Earth Sciences",
  "program_page": earth_url,
  "checked": "2026-10-30",
  "notes": "Earth Sciences PhD.",
  "fields": {
    "deadline": {
      "code": "2027-01-05",
      "value": "January 5 application deadline for Fall semester.",
      "quote": "The deadline to apply is January 5th for each Fall semester.",
      "url": earth_url
    },
    "gre_general": {
      "code": "Not required",
      "value": "Department does not require GRE scores for admission.",
      "quote": "The department does not require GRE scores for admission. It is not a necessary expense, nor will it necessarily help your application.",
      "url": earth_url
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "ETS offers no GRE Subject Test in Earth Sciences.",
      "quote": ets_quote,
      "url": ets_url
    },
    "supervisor": {
      "code": "Required",
      "value": "Important to contact potential advisor(s) in advance before deadline closes.",
      "quote": "Step 1: Contact your potential advisor(s).",
      "url": earth_url
    },
    "funding": {
      "code": "Guaranteed",
      "value": "USC Earth Sciences offers a 5-year, fully funded PhD program including tuition and yearly stipend.",
      "quote": "USC Earth Sciences offers a 5-year, fully funded Ph.D. program. Support includes tuition and a yearly stipend (the current 26-27 rate is $47,936) funded by a combination of research assistantship (RA), teaching assistantship (TA), and, in some cases, fellowships.",
      "url": earth_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "usc--earth.json").write_text(json.dumps(earth_prog, indent=2), encoding="utf-8")

# 12. Biology
mcb_adm_url = "https://dornsife.usc.edu/mcb/admissions/"
mcb_prog_url = "https://dornsife.usc.edu/mcb/the-mcb-phd-program/"
bio_prog = {
  "id": "usc--biology",
  "university": "usc",
  "field": "biology",
  "also_fields": [],
  "department": "Department of Molecular and Cellular Biosciences",
  "program_page": mcb_adm_url,
  "checked": "2026-10-30",
  "notes": "Molecular and Cellular Biosciences PhD.",
  "fields": {
    "deadline": {
      "code": "2026-12-01",
      "value": "December 1 admission deadline.",
      "quote": "Admission Deadline: December 1",
      "url": mcb_adm_url
    },
    "gre_general": {
      "code": "Not required",
      "value": "GRE scores are not required for admission to the PhD program.",
      "quote": "Note: GRE scores are not required for admission to the PhD program",
      "url": mcb_adm_url
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
      "url": mcb_adm_url
    },
    "funding": {
      "code": "Guaranteed",
      "value": "Department provides funding for the first five years through teaching/research assistantships, fellowships, and scholarships.",
      "quote": "Funding: Our department provides funding for the first five years of your program through a variety of teaching and research assistantships, fellowships, and scholarships.",
      "url": mcb_prog_url
    },
    "entry_route": common_entry_route
  }
}
(prog_dir / "usc--biology.json").write_text(json.dumps(bio_prog, indent=2), encoding="utf-8")

print("Created USC university and 12 program staging records successfully!")
