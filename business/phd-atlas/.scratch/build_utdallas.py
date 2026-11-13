import json
from pathlib import Path

staging_dir = Path("data/staging")
uni_dir = staging_dir / "universities"
prog_dir = staging_dir / "programs"

uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

today = "2026-10-30"

# Central UT Dallas Admissions URLs
deadlines_fees_url = "https://graduate-admissions.utdallas.edu/deadlines-and-fees/"
fee_waiver_url = "https://graduate-admissions.utdallas.edu/graduate-application-fee-waiver-program/"
intl_url = "https://graduate-admissions.utdallas.edu/international-students/"
cs_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/ecs/computer-science"

# University record
utdallas_uni = {
    "id": "utdallas",
    "institution": "The University of Texas at Dallas",
    "country": "USA",
    "region": "Texas",
    "grad_page": deadlines_fees_url,
    "checked": today,
    "notes": "Application fee is $75 for graduate applicants.",
    "fields": {
        "app_fee": {
            "code": "75 USD",
            "value": "Application fee of $75 for all graduate applicants unless fee waiver applies.",
            "quote": "All applicants are required to submit a $75 application fee within the application or Applicant Portal, unless you meet one of the fee waiver criteria below. The application fee is non-refundable.",
            "url": deadlines_fees_url
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Application fee waivers available for eligible participants in select programs; limited to U.S. citizens or permanent residents.",
            "quote": "To qualify, students must be applying for a PhD or master’s degree at UT Dallas. Non-degree applicants are not eligible for fee waivers. Only U.S. citizens, or permanent residents, are eligible to request a fee waiver.",
            "url": fee_waiver_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "GRE or GMAT score required only if applicable by program.",
            "quote": "GRE or GMAT score (if applicable)",
            "url": intl_url
        },
        "toefl_min": {
            "code": "80",
            "value": "Minimum TOEFL iBT score of 80 for tests taken on or before January 26, 2026 (or 4 on new scale).",
            "quote": "Test of English as a Foreign Language iBT (Internet-based test) Minimum score: 80 (for tests taken on or before January 26, 2026)",
            "url": intl_url
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum IELTS Academic score of 6.5.",
            "quote": "International English Language Testing System, Academic (IELTS) Minimum score: 6.5",
            "url": intl_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exempt from English exam if degree earned through instruction and examination in English.",
            "quote": "Your bachelor’s or master’s degree (or its equivalent) was earned through instruction and examination in English.",
            "url": intl_url
        }
    }
}
(uni_dir / "utdallas.json").write_text(json.dumps(utdallas_uni, indent=2), encoding="utf-8")

# Common ETS quote for non-subject test fields
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

# Common bachelor's entry quote from CS catalog:
common_bachelor_quote = "Admission Option Two A BS in related area that includes two semesters of calculus and linear algebra with A GPA of at least 3.5 in the last 60 semester credit hours"

# 1. Computer Science
cs_prog = {
    "id": "utdallas--cs",
    "university": "utdallas",
    "field": "cs",
    "also_fields": [],
    "department": "Department of Computer Science",
    "program_page": cs_cat_url,
    "checked": today,
    "notes": "Computer Science PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 priority funding deadline for Fall admission.",
            "quote": "Fall Deadline - December 15",
            "url": cs_cat_url
        },
        "gre_general": {
            "code": "Recommended",
            "value": "GRE scores are not required but applicants are encouraged to submit them.",
            "quote": "While not required, applicants are encouraged to submit any of the following supplemental items to be considered: GRE Scores.",
            "url": cs_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Computer Science.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": cs_cat_url
        },
        "funding": {
            "code": "Typical",
            "value": "Priority consideration for funding for applications received by posted deadlines.",
            "quote": "For priority consideration for funding, completed application files should be received by the deadlines posted below.",
            "url": cs_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Direct entry from bachelor's with BS in related area and GPA of at least 3.5.",
            "quote": common_bachelor_quote,
            "url": cs_cat_url
        }
    }
}
(prog_dir / "utdallas--cs.json").write_text(json.dumps(cs_prog, indent=2), encoding="utf-8")

# 2. Biomedical Engineering
bme_cat_url = "https://catalog.utdallas.edu/current/graduate/programs/ecs/biomedical-engineering"
bme_prog = {
    "id": "utdallas--bme",
    "university": "utdallas",
    "field": "bme",
    "also_fields": [],
    "department": "Department of Bioengineering",
    "program_page": bme_cat_url,
    "checked": today,
    "notes": "Biomedical Engineering PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": bme_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not stated in doctoral section.",
            "quote": "",
            "url": bme_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Biomedical Engineering.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Recommended",
            "value": "Students are encouraged to directly contact faculty about research opportunities and willingness to serve as supervisor.",
            "quote": "Students are encouraged to directly contact faculty about research opportunities and their willingness to serve as their supervising professor.",
            "url": bme_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated in doctoral admissions section.",
            "quote": "",
            "url": bme_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": bme_cat_url
        }
    }
}
(prog_dir / "utdallas--bme.json").write_text(json.dumps(bme_prog, indent=2), encoding="utf-8")

# 3. Electrical Engineering
ece_cat_url = "https://catalog.utdallas.edu/current/graduate/programs/ecs/electrical-engineering"
ece_prog = {
    "id": "utdallas--ece",
    "university": "utdallas",
    "field": "ece",
    "also_fields": [],
    "department": "Department of Electrical and Computer Engineering",
    "program_page": ece_cat_url,
    "checked": today,
    "notes": "Electrical Engineering PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": ece_cat_url
        },
        "gre_general": {
            "code": "Not required",
            "value": "GRE scores are temporarily being waived.",
            "quote": "GRE scores are temporarily being waived",
            "url": ece_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Electrical Engineering.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": ece_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": ece_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": ece_cat_url
        }
    }
}
(prog_dir / "utdallas--ece.json").write_text(json.dumps(ece_prog, indent=2), encoding="utf-8")

# 4. Materials Science
mat_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/ecs/materials-science"
mat_prog = {
    "id": "utdallas--materials",
    "university": "utdallas",
    "field": "materials",
    "also_fields": [],
    "department": "Department of Materials Science and Engineering",
    "program_page": mat_cat_url,
    "checked": today,
    "notes": "Materials Science and Engineering PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": mat_cat_url
        },
        "gre_general": {
            "code": "Recommended",
            "value": "GRE scores recommended as 154 verbal, 154 quant, 4 analytical writing.",
            "quote": "GRE revised scores which are recommended as 154 or above, 154 or above, and 4 for the verbal, quantitative, and analytical writing components, respectively, are advisable based on our experience with student success in the program.",
            "url": mat_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Materials Science.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": mat_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": mat_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": mat_cat_url
        }
    }
}
(prog_dir / "utdallas--materials.json").write_text(json.dumps(mat_prog, indent=2), encoding="utf-8")

# 5. Mechanical Engineering
mech_cat_url = "https://catalog.utdallas.edu/current/graduate/programs/ecs/mechanical-engineering"
mech_prog = {
    "id": "utdallas--mech",
    "university": "utdallas",
    "field": "mech",
    "also_fields": [],
    "department": "Department of Mechanical Engineering",
    "program_page": mech_cat_url,
    "checked": today,
    "notes": "Mechanical Engineering PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": mech_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not stated in doctoral section.",
            "quote": "",
            "url": mech_cat_url
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
            "url": mech_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": mech_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "78 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "78 semester credit hours minimum beyond the baccalaureate degree",
            "url": mech_cat_url
        }
    }
}
(prog_dir / "utdallas--mech.json").write_text(json.dumps(mech_prog, indent=2), encoding="utf-8")

# 6. Physics
phys_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/nsm/physics"
phys_prog = {
    "id": "utdallas--physics",
    "university": "utdallas",
    "field": "physics",
    "also_fields": [],
    "department": "Department of Physics",
    "program_page": phys_cat_url,
    "checked": today,
    "notes": "Physics PhD.",
    "fields": {
        "deadline": {
            "code": "2027-05-01",
            "value": "May 1 application deadline for Fall semester.",
            "quote": "Fall Deadline - May 1",
            "url": phys_cat_url
        },
        "gre_general": {
            "code": "Not required",
            "value": "GRE scores are temporarily being waived.",
            "quote": "GRE scores are temporarily being waived.",
            "url": phys_cat_url
        },
        "gre_subject": {
            "code": "Not stated",
            "value": "GRE physics subject test requirement not stated on catalog page.",
            "quote": "",
            "url": phys_cat_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": phys_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": phys_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": phys_cat_url
        }
    }
}
(prog_dir / "utdallas--physics.json").write_text(json.dumps(phys_prog, indent=2), encoding="utf-8")

# 7. Chemistry
chem_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/nsm/chemistry-and-biochemistry"
chem_prog = {
    "id": "utdallas--chemistry",
    "university": "utdallas",
    "field": "chemistry",
    "also_fields": [],
    "department": "Department of Chemistry and Biochemistry",
    "program_page": chem_cat_url,
    "checked": today,
    "notes": "Chemistry PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": chem_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not stated in doctoral section.",
            "quote": "",
            "url": chem_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Chemistry.",
            "quote": ets_quote,
            "url": ets_url
        },
        "toefl_min": {
            "code": "100",
            "value": "Foreign students with TOEFL scores less than 100 on internet test are admitted only in special circumstances.",
            "quote": "Foreign students with TOEFL scores less than 600 (paper test), 250 (computer test), or 100 (internet test) are admitted only in special circumstances.",
            "url": chem_cat_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": chem_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": chem_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": chem_cat_url
        }
    }
}
(prog_dir / "utdallas--chemistry.json").write_text(json.dumps(chem_prog, indent=2), encoding="utf-8")

# 8. Mathematics
math_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/nsm/mathematics"
math_prog = {
    "id": "utdallas--math",
    "university": "utdallas",
    "field": "math",
    "also_fields": [],
    "department": "Department of Mathematical Sciences",
    "program_page": math_cat_url,
    "checked": today,
    "notes": "Mathematics PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": math_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Standardized tests used in conjunction with other measures, no rigid minimum cutoff.",
            "quote": "",
            "url": math_cat_url
        },
        "gre_subject": {
            "code": "Not stated",
            "value": "Subject GRE requirement not stated on catalog page.",
            "quote": "",
            "url": math_cat_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": math_cat_url
        },
        "funding": {
            "code": "Typical",
            "value": "First-round consideration for assistantships and scholarships deadline is December 15.",
            "quote": "First-round Scholarship Deadline: For first-round consideration for assistantships and scholarships, complete application files must be received by the following deadlines: Fall Deadline - December 15",
            "url": math_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": math_cat_url
        }
    }
}
(prog_dir / "utdallas--math.json").write_text(json.dumps(math_prog, indent=2), encoding="utf-8")

# 9. Statistics / Data Science
stat_prog = {
    "id": "utdallas--statistics",
    "university": "utdallas",
    "field": "statistics",
    "also_fields": ["datasci"],
    "department": "Department of Mathematical Sciences",
    "program_page": math_cat_url,
    "checked": today,
    "notes": "Data Science and Statistics PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": math_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Standardized tests used in conjunction with other measures, no rigid minimum cutoff.",
            "quote": "",
            "url": math_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Statistics or Data Science.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": math_cat_url
        },
        "funding": {
            "code": "Typical",
            "value": "Applications received by December 15 reviewed for first-round scholarships and assistantships.",
            "quote": "All complete application files received by the December 15 deadline will be reviewed for first-round scholarships and assistantships consideration.",
            "url": math_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": math_cat_url
        }
    }
}
(prog_dir / "utdallas--statistics.json").write_text(json.dumps(stat_prog, indent=2), encoding="utf-8")

# 10. Earth Sciences / Geosciences
earth_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/nsm/sustainable-earth-systems-sciences"
earth_prog = {
    "id": "utdallas--earth",
    "university": "utdallas",
    "field": "earth",
    "also_fields": [],
    "department": "Department of Sustainable Earth Systems Sciences",
    "program_page": earth_cat_url,
    "checked": today,
    "notes": "Geosciences PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": earth_cat_url
        },
        "gre_general": {
            "code": "Not required",
            "value": "GRE scores are temporarily being waived.",
            "quote": "GRE scores are temporarily being waived.",
            "url": earth_cat_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Geosciences / Earth Sciences.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": earth_cat_url
        },
        "funding": {
            "code": "Typical",
            "value": "First-round Scholarship Deadline for assistantships and scholarships is December 15.",
            "quote": "First-round Scholarship Deadline: For first-round consideration for assistantships and scholarships, complete application files must be received by the following deadlines: Fall Deadline - December 15",
            "url": earth_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": earth_cat_url
        }
    }
}
(prog_dir / "utdallas--earth.json").write_text(json.dumps(earth_prog, indent=2), encoding="utf-8")

# 11. Biological Sciences
bio_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/nsm/biological-sciences"
bio_prog = {
    "id": "utdallas--biology",
    "university": "utdallas",
    "field": "biology",
    "also_fields": [],
    "department": "Department of Biological Sciences",
    "program_page": bio_cat_url,
    "checked": today,
    "notes": "Molecular and Cell Biology PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-15",
            "value": "December 15 doctoral application deadline for Fall semester.",
            "quote": "Fall Deadline - December 15",
            "url": bio_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not stated in doctoral section.",
            "quote": "",
            "url": bio_cat_url
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
            "url": bio_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": bio_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": bio_cat_url
        }
    }
}
(prog_dir / "utdallas--biology.json").write_text(json.dumps(bio_prog, indent=2), encoding="utf-8")

# 12. Cognition and Neuroscience
neuro_cat_url = "https://catalog.utdallas.edu/2026/graduate/programs/bbs/doctoral-programs"
neuro_prog = {
    "id": "utdallas--neuro",
    "university": "utdallas",
    "field": "neuro",
    "also_fields": [],
    "department": "School of Behavioral and Brain Sciences",
    "program_page": neuro_cat_url,
    "checked": today,
    "notes": "Cognition and Neuroscience PhD.",
    "fields": {
        "deadline": {
            "code": "2026-12-01",
            "value": "December 1 application deadline for Fall admission.",
            "quote": "Fall Deadline - December 1",
            "url": neuro_cat_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not stated specifically for Cognition and Neuroscience.",
            "quote": "",
            "url": neuro_cat_url
        },
        "gre_subject": {
            "code": "Not stated",
            "value": "Psychology GRE subject test requirement not stated on catalog page.",
            "quote": "",
            "url": neuro_cat_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": neuro_cat_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": neuro_cat_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "75 semester credit hours minimum beyond the baccalaureate degree.",
            "quote": "75 semester credit hours minimum beyond the baccalaureate degree",
            "url": neuro_cat_url
        }
    }
}
(prog_dir / "utdallas--neuro.json").write_text(json.dumps(neuro_prog, indent=2), encoding="utf-8")

print("Created UT Dallas university and 12 program staging records successfully!")
