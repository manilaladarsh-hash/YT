import json
from pathlib import Path

STAGE = Path('data/staging')
(STAGE / 'universities').mkdir(parents=True, exist_ok=True)
(STAGE / 'programs').mkdir(parents=True, exist_ok=True)

umaine_uni = {
  "id": "umaine",
  "institution": "University of Maine",
  "country": "USA",
  "region": "Maine",
  "grad_page": "https://gradcatalog.umaine.edu/content.php?catoid=41&navoid=1009",
  "checked": "2026-10-29",
  "fields": {
    "app_fee": {
      "code": "65 USD",
      "value": "A complete degree application includes a $65 application fee.",
      "quote": "$65 application fee",
      "url": "https://umaine.edu/graduate/apply/application-checklist/"
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Application fee waivers are available only for IRT Scholars, McNair Scholars, current and former US Armed Forces members/dependents, and UMS alumni.",
      "quote": "At this time, the only application fee waiver options at the Graduate School are for the following scenarios:\nIRT Scholars will receive an application fee waiver.\nMcNair Scholars will receive an application fee waiver.",
      "url": "https://umaine.edu/graduate/apply/faq/"
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Graduate examination scores (GRE and/or GMAT) are not required by the Graduate School, but they may be required for the program to which you are applying.",
      "quote": "Graduate examination scores (GRE and/or GMAT) are not required by the Graduate School, but they may be required for the program to which you are applying.",
      "url": "https://umaine.edu/graduate/apply/faq/"
    },
    "toefl_min": {
      "code": "82",
      "value": "The Graduate School requires a minimum score of 82 on the iBT TOEFL or equivalent.",
      "quote": "The Graduate School requires a minimum score of 82 on the iBT TOEFL or equivalent.",
      "url": "https://gradcatalog.umaine.edu/content.php?catoid=41&navoid=1009"
    },
    "ielts_min": {
      "code": "6.5",
      "value": "The minimum IELTS score required for admission is 6.5.",
      "quote": "Minimum Score: 6.5",
      "url": "https://umaine.edu/graduate/apply/test-scores/"
    },
    "english_waiver": {
      "code": "Yes",
      "value": "An English language proficiency exam is not needed if your undergraduate (or master's) degree was taught in English or if English is an official language of your home country.",
      "quote": "An English language proficiency exam is not needed if your undergraduate (or master’s) degree was taught in English or if English is an official language of your home country.",
      "url": "https://umaine.edu/graduate/apply/faq/"
    }
  },
  "notes": ""
}

with open(STAGE / 'universities' / 'umaine.json', 'w', encoding='utf-8') as f:
    json.dump(umaine_uni, f, indent=2, ensure_ascii=False)
print("Wrote data/staging/universities/umaine.json")

# Standard quotes:
ets_general_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_general_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

ets_chem_quote = "The GRE Chemistry Test was discontinued in May 2023."
ets_chem_url = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"

entry_quote = "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent."
entry_url = "https://gradcatalog.umaine.edu/content.php?catoid=41&navoid=1009"

funding_quote = "Fall applicants who wish to be considered for assistantships or fellowships should submit an application and all supporting materials no later than January 15th of that year."
funding_url = "https://gradcatalog.umaine.edu/content.php?catoid=41&navoid=1009"

programs = [
  {
    "field": "physics",
    "department": "Department of Physics and Astronomy",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5290&returnto=1015",
    "deadline": {
      "code": "2027-01-15",
      "value": "Application deadline: January 15, then rolling if space is available",
      "quote": "Application deadline: January 15, then rolling if space is available",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5290&returnto=1015",
      "inferred": "year",
      "rolling": True
    },
    "gre_subject": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5290&returnto=1015"
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5290&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Typically a total of 5 years are typically needed to complete the Ph.D. degree for a student who enters the program with a bachelor’s degree.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "chemistry",
    "department": "Department of Chemistry",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5487&returnto=1015",
    "deadline": {
      "code": "2027-01-15",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application and all supporting materials no later than January 15th of that year.",
      "quote": funding_quote,
      "url": funding_url,
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Chemistry Test was discontinued in May 2023.",
      "quote": ets_chem_quote,
      "url": ets_chem_url
    },
    "supervisor": {
      "code": "Not required",
      "value": "All chemistry students must select a research advisor and advisory committee by the end of the first semester of graduate study.",
      "quote": "All chemistry students must select a research advisor and advisory committee by the end of the first semester of graduate study and thereafter meet with the committee at least once each year.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5487&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "cs",
    "department": "School of Computing and Information Science",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5243&returnto=1015",
    "deadline": {
      "code": "2027-04-01",
      "value": "Application deadline: January 15 for funding consideration | April 1 (Fall) / November 1 (Spring/Summer)",
      "quote": "Application deadline: January 15 for funding consideration | April 1 (Fall) / November 1 (Spring/Summer)",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5243&returnto=1015",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Computer Science subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5243&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Application deadline: January 15 for funding consideration | April 1 (Fall) / November 1 (Spring/Summer)",
      "quote": "Application deadline: January 15 for funding consideration | April 1 (Fall) / November 1 (Spring/Summer)",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5243&returnto=1015"
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "ece",
    "department": "Department of Electrical and Computer Engineering",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5253&returnto=1015",
    "deadline": {
      "code": "Rolling",
      "value": "Application deadline: Rolling",
      "quote": "Application deadline: Rolling",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5253&returnto=1015",
      "rolling": True
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Electrical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5253&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Graduate assistantships and a limited number of teaching assistantships are available. Graduate research assistantships are contingent on funding.",
      "quote": "Graduate assistantships and a limited number of teaching assistantships are available. Graduate research assistantships are contingent on funding.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5253&returnto=1015"
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "mech",
    "department": "Department of Mechanical Engineering",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5494&returnto=1015",
    "deadline": {
      "code": "2027-01-15",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application and all supporting materials no later than January 15th of that year.",
      "quote": funding_quote,
      "url": funding_url,
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Mechanical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5494&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Research and teaching assistantships are available; contact Graduate Coordinator for additional details.",
      "quote": "Research and teaching assistantships are available; contact Graduate Coordinator for additional details",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5494&returnto=1015"
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "chemeng",
    "department": "Department of Chemical and Biomedical Engineering",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5237&returnto=1015",
    "deadline": {
      "code": "2026-12-20",
      "value": "Application deadline: December 20 (Fall)/September 30 (Spring)",
      "quote": "Application deadline: December 20 (Fall)/September 30 (Spring)",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5237&returnto=1015",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Chemical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5237&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "The Ph.D. degree requires a minimum of 45 semester hours, beyond the B.S. level, comprising four seminars and at least eight graduate courses (24 credits) in addition to a research thesis.",
      "quote": "The Ph.D. degree requires a minimum of 45 semester hours, beyond the B.S. level, comprising four seminars and at least eight graduate courses (24 credits) in addition to a research thesis.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5237&returnto=1015"
    }
  },
  {
    "field": "civil",
    "department": "Department of Civil and Environmental Engineering",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5239&returnto=1015",
    "deadline": {
      "code": "Rolling",
      "value": "Application deadline: Rolling",
      "quote": "Application deadline: Rolling",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5239&returnto=1015",
      "rolling": True
    },
    "gre_general": {
      "code": "Recommended",
      "value": "Test Required: GRE recommended but not required for admission.",
      "quote": "Test Required: GRE recommended but not required for admission.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5239&returnto=1015"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Civil Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5239&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "bme",
    "department": "Graduate School of Biomedical Science and Engineering",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5235&returnto=1015",
    "deadline": {
      "code": "2026-12-01",
      "value": "Application deadline: December 1",
      "quote": "Application deadline: December 1",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5235&returnto=1015",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Biomedical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5235&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "biology",
    "department": "School of Biology and Ecology",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015",
    "deadline": {
      "code": "2027-01-15",
      "value": "Application deadline: January 15 (Fall) / November 15 (Spring)",
      "quote": "Application deadline: January 15 (Fall) / November 15 (Spring)",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Biology subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Required",
      "value": "Applicants need to identify an area of research interest and a potential advisor at the time of application; they should feel free to contact members of the faculty to discuss possible research projects before submission of the application.",
      "quote": "Applicants need to identify an area of research interest and a potential advisor at the time of application; they should feel free to contact members of the faculty to discuss possible research projects before submission of the application. A research project is a central part of the PhD degree.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "All applicants will be automatically considered for teaching or research assistantships. Many students are supported by research grants to individual faculty members.",
      "quote": "All applicants will be automatically considered for teaching or research assistantships. Many students are supported by research grants to individual faculty members; interested students should contact faculty members directly for further information on grant-supported assistantships.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015"
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "earth",
    "department": "School of Earth and Climate Sciences",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5247&returnto=1015",
    "deadline": {
      "code": "2027-01-15",
      "value": "Application deadline: January 15 (Fall), then rolling if space is available / November 30 (Spring), then rolling if space is available",
      "quote": "Application deadline: January 15 (Fall), then rolling if space is available / November 30 (Spring), then rolling if space is available",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5247&returnto=1015",
      "inferred": "year",
      "rolling": True
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Earth Sciences subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5247&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "The PhD requires the completion of at least 15 credits of coursework beyond a master’s degree, and 33 credits if entering with a bachelor’s degree.",
      "quote": "The PhD requires the completion of at least 15 credits of coursework beyond a master’s degree, and 33 credits if entering with a bachelor’s degree; all PhD students must take at least 9 thesis credits.",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5247&returnto=1015"
    }
  },
  {
    "field": "environment",
    "department": "Ecology and Environmental Sciences Program",
    "program_page": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5248&returnto=1015",
    "deadline": {
      "code": "2027-01-15",
      "value": "Application deadline: January 15 / November 1",
      "quote": "Application deadline: January 15 / November 1",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5248&returnto=1015",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Environmental Sciences subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on catalog program page.",
      "quote": "",
      "url": "https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5248&returnto=1015"
    },
    "funding": {
      "code": "Typical",
      "value": "Fall applicants who wish to be considered for assistantships or fellowships should submit an application no later than January 15th.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Consideration for admission to the Graduate School will be given to applicants holding a bachelor’s degree from an accredited institution, or the equivalent.",
      "quote": entry_quote,
      "url": entry_url
    }
  }
]

for p in programs:
    fid = p["field"]
    prog_data = {
      "id": f"umaine--{fid}",
      "university": "umaine",
      "field": fid,
      "also_fields": [],
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
    if "gre_general" in p:
        prog_data["fields"]["gre_general"] = p["gre_general"]
    
    with open(STAGE / 'programs' / f"umaine--{fid}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote data/staging/programs/umaine--{fid}.json")
