import json
from pathlib import Path

staging_dir = Path("data/staging")
uni_dir = staging_dir / "universities"
prog_dir = staging_dir / "programs"

uni_dir.mkdir(parents=True, exist_ok=True)
prog_dir.mkdir(parents=True, exist_ok=True)

today = "2026-10-30"

# Central UTK Admissions URLs
tuition_url = "https://onestop.utk.edu/tuition-detail/"
catalog_policy_url = "https://catalog.utk.edu/content.php?catoid=57&navoid=12403"
testing_req_url = "https://gradschool.utk.edu/future-students/office-of-graduate-admissions/applying-to-graduate-school/admission-requirements/testing-requirements/"
intl_deadlines_url = "https://gradschool.utk.edu/future-students/office-of-graduate-admissions/applying-to-graduate-school/admissions-for-international-students/"

# University record
utk_uni = {
    "id": "utk",
    "institution": "University of Tennessee, Knoxville",
    "country": "USA",
    "region": "Tennessee",
    "grad_page": "https://gradschool.utk.edu/admissions/",
    "checked": today,
    "notes": "Application fee is $60 for prospective graduate students.",
    "fields": {
        "app_fee": {
            "code": "60 USD",
            "value": "Application fee of $60 nonrefundable fee for prospective graduate students.",
            "quote": "Graduate Application Fee $60 nonrefundable fee due for prospective graduate students with each first-time admissions application.",
            "url": tuition_url
        },
        "fee_waiver": {
            "code": "None",
            "value": "Non-refundable application fee required before individual can become a graduate student; central waiver not available.",
            "quote": "A non-refundable Graduate Admissions Application Fee must be submitted with each first-time admissions application before an individual will be permitted to become a University of Tennessee graduate student or attend classes and before an individual student account will be established.",
            "url": catalog_policy_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Standardized testing such as GRE or GMAT depends on the specific program.",
            "quote": "The program to which you are applying may require test scores such as the GRE or the GMAT. Please check with your desired program to see if they require any standardized test scores.",
            "url": testing_req_url
        },
        "toefl_min": {
            "code": "80",
            "value": "Minimum TOEFL score of 80 with at least 20 on speaking and writing (or 4.5 on scale after Jan 22, 2026).",
            "quote": "Minimum TOEFL score requirement: For exams taken prior to January 21, 2026, an overall score of 80 with at least 20 on speaking and writing is required. For exams taken on or after January 22, 2026, an overall score of 4.5 with at least a 4 on speaking and writing is required.",
            "url": testing_req_url
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum IELTS score of 6.5 overall with no single band below 6.0.",
            "quote": "Minimum IELTS score requirement: An overall bandwidth of 6.5, with no single band (score) below 6.0 is required.",
            "url": testing_req_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exempt if English is an official language in applicant's country of citizenship.",
            "quote": "An applicant may be exempted from the English Certification requirement if: English is an official language in the applicant’s country of citizenship, according to standards published by the Graduate School",
            "url": testing_req_url
        }
    }
}
(uni_dir / "utk.json").write_text(json.dumps(utk_uni, indent=2), encoding="utf-8")

# Common ETS quote
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

# Common deadline quote
common_deadline_quote = "The online submission deadline is when the initial application must be submitted online, provided the department has no earlier deadline. By the file completion deadline, admission must be granted and all documents required to obtain a student visa must be submitted to the Division of Global Engagement."

# Common bachelor's entry quote
common_bachelor_quote = "Admission to graduate study requires a bachelor’s degree with a satisfactory grade point average (GPA) from a college or university accredited by the appropriate regional accrediting agency, an institution accredited by another organization recognized by the Council on Higher Education Accreditation (CHEA), or foreign equivalent."

# 1. Computer Science
cs_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36749"
cs_prog = {
    "id": "utk--cs",
    "university": "utk",
    "field": "cs",
    "also_fields": [],
    "department": "Min H. Kao Department of Electrical Engineering and Computer Science",
    "program_page": cs_url,
    "checked": today,
    "notes": "Computer Science Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not specified in catalog program section.",
            "quote": "",
            "url": cs_url
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
            "url": cs_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": cs_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Exceptional students holding a bachelor's degree may be admitted without first obtaining a master's degree.",
            "quote": "Exceptional students holding the bachelor’s degree may be admitted to the doctoral program without first obtaining a master’s degree.",
            "url": cs_url
        }
    }
}
(prog_dir / "utk--cs.json").write_text(json.dumps(cs_prog, indent=2), encoding="utf-8")

# 2. Electrical Engineering
ece_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36786"
ece_prog = {
    "id": "utk--ece",
    "university": "utk",
    "field": "ece",
    "also_fields": [],
    "department": "Min H. Kao Department of Electrical Engineering and Computer Science",
    "program_page": ece_url,
    "checked": today,
    "notes": "Electrical Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not specified in catalog program section.",
            "quote": "",
            "url": ece_url
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
            "url": ece_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": ece_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Exceptional students holding a bachelor's degree may be admitted without first obtaining a master's degree.",
            "quote": "Exceptional students holding the bachelor’s degree may be admitted to the doctoral program without first obtaining a master’s degree.",
            "url": ece_url
        }
    }
}
(prog_dir / "utk--ece.json").write_text(json.dumps(ece_prog, indent=2), encoding="utf-8")

# 3. Biomedical Engineering
bme_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36726"
bme_prog = {
    "id": "utk--bme",
    "university": "utk",
    "field": "bme",
    "also_fields": [],
    "department": "Department of Mechanical, Aerospace, and Biomedical Engineering",
    "program_page": bme_url,
    "checked": today,
    "notes": "Biomedical Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Required",
            "value": "General GRE is required of all applicants for admission.",
            "quote": "The general GRE is required of all applicants for admission.",
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
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": bme_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor's degree required per university graduate admission policies.",
            "quote": common_bachelor_quote,
            "url": catalog_policy_url
        }
    }
}
(prog_dir / "utk--bme.json").write_text(json.dumps(bme_prog, indent=2), encoding="utf-8")

# 4. Chemical Engineering
chemeng_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36734"
chemeng_prog = {
    "id": "utk--chemeng",
    "university": "utk",
    "field": "chemeng",
    "also_fields": [],
    "department": "Department of Chemical and Biomolecular Engineering",
    "program_page": chemeng_url,
    "checked": today,
    "notes": "Chemical Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Required",
            "value": "Graduate Record Examination scores are required for admission.",
            "quote": "Students may apply directly to the PhD program either with or without having completed a master’s degree. Students proceeding directly to the PhD program from a baccalaureate degree should submit evidence of outstanding performance in a rigorous undergraduate program and the ability to perform independent research at the doctoral level. Graduate Record Examination scores and at least three letters of reference are required for admission.",
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
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": chemeng_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Students may apply directly to the PhD program either with or without having completed a master's degree.",
            "quote": "Students may apply directly to the PhD program either with or without having completed a master’s degree. Students proceeding directly to the PhD program from a baccalaureate degree should submit evidence of outstanding performance in a rigorous undergraduate program and the ability to perform independent research at the doctoral level. Graduate Record Examination scores and at least three letters of reference are required for admission.",
            "url": chemeng_url
        }
    }
}
(prog_dir / "utk--chemeng.json").write_text(json.dumps(chemeng_prog, indent=2), encoding="utf-8")

# 5. Civil Engineering
civil_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36740"
civil_prog = {
    "id": "utk--civil",
    "university": "utk",
    "field": "civil",
    "also_fields": [],
    "department": "Department of Civil and Environmental Engineering",
    "program_page": civil_url,
    "checked": today,
    "notes": "Civil Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Required",
            "value": "All applicants to the degree programs must submit scores from the General GRE.",
            "quote": "All applicants to the degree programs must submit scores from the General Graduate Record Examination (GRE).",
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
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": civil_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor's degree required per university graduate admission policies.",
            "quote": common_bachelor_quote,
            "url": catalog_policy_url
        }
    }
}
(prog_dir / "utk--civil.json").write_text(json.dumps(civil_prog, indent=2), encoding="utf-8")

# 6. Materials Science
materials_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36829"
materials_prog = {
    "id": "utk--materials",
    "university": "utk",
    "field": "materials",
    "also_fields": [],
    "department": "Department of Materials Science and Engineering",
    "program_page": materials_url,
    "checked": today,
    "notes": "Materials Science and Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Required",
            "value": "All applicants must submit scores from the general Graduate Record Examination (GRE).",
            "quote": "All applicants must submit scores from the general Graduate Record Examination (GRE).",
            "url": materials_url
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
            "url": materials_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": materials_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor's degree in engineering or science with GPA of at least 2.70 required.",
            "quote": "Applicants for admission to the PhD program in materials science and engineering are expected to have completed a bachelor’s degree in an area of engineering or science with a grade-point-average of at least 2.70 out of 4.00 (or 3.00 during the senior year of undergraduate study).",
            "url": materials_url
        }
    }
}
(prog_dir / "utk--materials.json").write_text(json.dumps(materials_prog, indent=2), encoding="utf-8")

# 7. Mechanical Engineering
mech_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36835"
mech_prog = {
    "id": "utk--mech",
    "university": "utk",
    "field": "mech",
    "also_fields": [],
    "department": "Department of Mechanical, Aerospace, and Biomedical Engineering",
    "program_page": mech_url,
    "checked": today,
    "notes": "Mechanical Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Optional",
            "value": "The general GRE test is optional.",
            "quote": "The general GRE test is optional.",
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
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": mech_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor's degree required per university graduate admission policies.",
            "quote": common_bachelor_quote,
            "url": catalog_policy_url
        }
    }
}
(prog_dir / "utk--mech.json").write_text(json.dumps(mech_prog, indent=2), encoding="utf-8")

# 8. Data Science
datasci_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36923"
datasci_prog = {
    "id": "utk--datasci",
    "university": "utk",
    "field": "datasci",
    "also_fields": [],
    "department": "Bredesen Center for Interdisciplinary Research and Graduate Education",
    "program_page": datasci_url,
    "checked": today,
    "notes": "Data Science and Engineering Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not specified in catalog program section.",
            "quote": "",
            "url": datasci_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Data Science.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": datasci_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": datasci_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor of Science degree in engineering or scientific field required.",
            "quote": "In addition, the student must have a Bachelor of Science degree in either engineering or a scientific field (e.g., analytics, biology, chemistry, computational science, mathematics, physics, statistics, etc.), or the equivalent.",
            "url": datasci_url
        }
    }
}
(prog_dir / "utk--datasci.json").write_text(json.dumps(datasci_prog, indent=2), encoding="utf-8")

# 9. Physics
physics_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36859"
physics_prog = {
    "id": "utk--physics",
    "university": "utk",
    "field": "physics",
    "also_fields": [],
    "department": "Department of Physics and Astronomy",
    "program_page": physics_url,
    "checked": today,
    "notes": "Physics Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Optional",
            "value": "General GRE is optional.",
            "quote": "The Graduate Record Examination (general and subject) are optional.",
            "url": physics_url
        },
        "gre_subject": {
            "code": "Optional",
            "value": "Subject GRE is optional.",
            "quote": "The Graduate Record Examination (general and subject) are optional.",
            "url": physics_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": physics_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": physics_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Undergraduate major in physics or equivalent required; 72 graduate credit hours beyond bachelor's.",
            "quote": "Credit Hours Required 72 graduate credit hours beyond the bachelor’s degree",
            "url": physics_url
        }
    }
}
(prog_dir / "utk--physics.json").write_text(json.dumps(physics_prog, indent=2), encoding="utf-8")

# 10. Chemistry
chemistry_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36736"
chemistry_prog = {
    "id": "utk--chemistry",
    "university": "utk",
    "field": "chemistry",
    "also_fields": [],
    "department": "Department of Chemistry",
    "program_page": chemistry_url,
    "checked": today,
    "notes": "Chemistry Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not specified in catalog program section.",
            "quote": "",
            "url": chemistry_url
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
            "url": chemistry_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": chemistry_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "52 graduate credit hours required beyond the bachelor's degree.",
            "quote": "Credit Hours Required 52 graduate credit hours beyond the bachelor’s degree",
            "url": chemistry_url
        }
    }
}
(prog_dir / "utk--chemistry.json").write_text(json.dumps(chemistry_prog, indent=2), encoding="utf-8")

# 11. Mathematics
math_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36832"
math_prog = {
    "id": "utk--math",
    "university": "utk",
    "field": "math",
    "also_fields": [],
    "department": "Department of Mathematics",
    "program_page": math_url,
    "checked": today,
    "notes": "Mathematics Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "General GRE requirement not specified in catalog program section.",
            "quote": "",
            "url": math_url
        },
        "gre_subject": {
            "code": "Not stated",
            "value": "Mathematics subject GRE requirement not specified on catalog page.",
            "quote": "",
            "url": math_url
        },
        "supervisor": {
            "code": "Not stated",
            "value": "Prior supervisor contact not specified.",
            "quote": "",
            "url": math_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": math_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Minimum of 72 graduate credit hours beyond the bachelor's degree.",
            "quote": "Minimum of 72 graduate credit hours beyond the Bachelor’s or Minimum of 48 graduate credit hours beyond the Master’s",
            "url": math_url
        }
    }
}
(prog_dir / "utk--math.json").write_text(json.dumps(math_prog, indent=2), encoding="utf-8")

# 12. Earth Sciences / Geology
earth_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36808"
earth_prog = {
    "id": "utk--earth",
    "university": "utk",
    "field": "earth",
    "also_fields": [],
    "department": "Department of Earth and Planetary Sciences",
    "program_page": earth_url,
    "checked": today,
    "notes": "Geology Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Required",
            "value": "General GRE scores required for admission.",
            "quote": "For admission, an applicant must provide transcripts of previous university work, three rating forms or letters of recommendation, and GRE scores (general).",
            "url": earth_url
        },
        "gre_subject": {
            "code": "No subject test",
            "value": "ETS offers no GRE Subject Test in Earth Sciences / Geology.",
            "quote": ets_quote,
            "url": ets_url
        },
        "supervisor": {
            "code": "Required",
            "value": "Upon admission, each student selects a major advisor before entering the Department.",
            "quote": "Upon admission, each student selects a major advisor before entering the Department.",
            "url": earth_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": earth_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor's degree in geosciences or other field required.",
            "quote": "Prerequisite for either graduate degree is a Bachelor’s degree in the geosciences or other field (typically, but not exclusively, from the physical, natural, or life sciences or engineering).",
            "url": earth_url
        }
    }
}
(prog_dir / "utk--earth.json").write_text(json.dumps(earth_prog, indent=2), encoding="utf-8")

# 13. Biology (BCMB)
biology_url = "https://catalog.utk.edu/preview_program.php?catoid=57&poid=36724"
biology_prog = {
    "id": "utk--biology",
    "university": "utk",
    "field": "biology",
    "also_fields": [],
    "department": "Department of Biochemistry and Cellular and Molecular Biology",
    "program_page": biology_url,
    "checked": today,
    "notes": "Biochemistry and Cellular and Molecular Biology Major, PhD.",
    "fields": {
        "deadline": {
            "code": "2027-04-15",
            "value": "April 15 online submission deadline for Fall admission.",
            "quote": common_deadline_quote,
            "url": intl_deadlines_url
        },
        "gre_general": {
            "code": "Required",
            "value": "Graduate Record Examination scores required for admission.",
            "quote": "Graduate Record Examination scores. A minimum grade point average of 3.0 out of 4.0.",
            "url": biology_url
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
            "url": biology_url
        },
        "funding": {
            "code": "Not stated",
            "value": "Funding package details not stated on catalog page.",
            "quote": "",
            "url": biology_url
        },
        "entry_route": {
            "code": "Direct from bachelor's",
            "value": "Bachelor's degree required per university graduate admission policies.",
            "quote": common_bachelor_quote,
            "url": catalog_policy_url
        }
    }
}
(prog_dir / "utk--biology.json").write_text(json.dumps(biology_prog, indent=2), encoding="utf-8")

print("Created UTK university and 13 program staging records successfully!")
