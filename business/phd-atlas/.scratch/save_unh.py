import json
from pathlib import Path

STAGE = Path('data/staging')
(STAGE / 'universities').mkdir(parents=True, exist_ok=True)
(STAGE / 'programs').mkdir(parents=True, exist_ok=True)

unh_uni = {
  "id": "unh",
  "institution": "University of New Hampshire",
  "country": "USA",
  "region": "New Hampshire",
  "grad_page": "https://gradschool.unh.edu/admissions/international-students",
  "checked": "2026-10-29",
  "fields": {
    "app_fee": {
      "code": "65 USD",
      "value": "The application fee is $65 for a degree program and $25 for a graduate certificate.",
      "quote": "The application fee is $65 for a degree program and $25 for a graduate certificate.",
      "url": "https://gradschool.unh.edu/admissions/international-students"
    },
    "fee_waiver": {
      "code": "None",
      "value": "Application fee waivers are not available for most programs in most circumstances.",
      "quote": "Application fee waivers are not available for most programs in most circumstances.",
      "url": "https://gradschool.unh.edu/admissions/international-students"
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Many UNH graduate programs require applicants to submit GRE, GMAT, PRAXIS, or other examination scores; specific testing requirements vary by program.",
      "quote": "Many UNH graduate programs require applicants to submit GRE, GMAT, PRAXIS, or other examination scores.",
      "url": "https://gradschool.unh.edu/admissions/test-scores"
    },
    "toefl_min": {
      "code": "80",
      "value": "TOEFL iBT: 80",
      "quote": "TOEFL iBT: 80",
      "url": "https://gradschool.unh.edu/admissions/international-students"
    },
    "ielts_min": {
      "code": "6.5",
      "value": "IELTS (International English Language Testing System): 6.5",
      "quote": "IELTS (International English Language Testing System): 6.5",
      "url": "https://gradschool.unh.edu/admissions/international-students"
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "Applicants whose first language is English, whose prior education was conducted in English, or who have earned a degree from a U.S. institution may be eligible to request a waiver.",
      "quote": "Applicants whose first language is English, whose prior education was conducted in English, or who have earned a degree from a U.S. institution may be eligible to request a waiver.",
      "url": "https://gradschool.unh.edu/admissions/international-students"
    }
  },
  "notes": ""
}

with open(STAGE / 'universities' / 'unh.json', 'w', encoding='utf-8') as f:
    json.dump(unh_uni, f, indent=2, ensure_ascii=False)
print("Wrote data/staging/universities/unh.json")

# Quotes:
ets_general_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_general_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"

ets_chem_quote = "The GRE Chemistry Test was discontinued in May 2023."
ets_chem_url = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"

entry_quote = "While applicants with bachelor's degrees may apply directly to certain doctoral programs, the Graduate School also reserves the right to offer applicants admission at the master's degree level in its place."
entry_url = "https://catalog.unh.edu/graduate/general-information/admissions/"

funding_quote = "Tuition Waivers: Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment."
funding_url = "https://catalog.unh.edu/graduate/general-information/fees-financial-support/"

programs = [
  {
    "field": "physics",
    "department": "Department of Physics and Astronomy",
    "program_page": "https://gradschool.unh.edu/program/phd/physics",
    "deadline": {
      "code": "2027-04-15",
      "value": "Fall: Jan. 15 (for funding); after that on rolling basis until April 15",
      "quote": "Fall: Jan. 15 (for funding); after that on rolling basis until April 15",
      "url": "https://gradschool.unh.edu/program/phd/physics",
      "inferred": "year",
      "rolling": True
    },
    "gre_general": {
      "code": "Optional",
      "value": "The GRE scores are optional, if you wish to provide scores please email the scores directly to the department once you have submitted your application online.",
      "quote": "The GRE scores are optional, if you wish to provide scores please email the scores directly to the department once you have submitted your application online.",
      "url": "https://gradschool.unh.edu/program/phd/physics"
    },
    "gre_subject": {
      "code": "Optional",
      "value": "The GRE scores are optional, if you wish to provide scores please email the scores directly to the department once you have submitted your application online.",
      "quote": "The GRE scores are optional, if you wish to provide scores please email the scores directly to the department once you have submitted your application online.",
      "url": "https://gradschool.unh.edu/program/phd/physics"
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/physics"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs; Graduate School reserves right to offer admission at master's level.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "chemistry",
    "department": "Department of Chemistry",
    "program_page": "https://gradschool.unh.edu/program/phd/chemistry",
    "deadline": {
      "code": "2027-04-01",
      "value": "Fall: Jan. 15 (for funding); April 1 (final)",
      "quote": "Fall: Jan. 15 (for funding); April 1 (final)",
      "url": "https://gradschool.unh.edu/program/phd/chemistry",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Chemistry Test was discontinued in May 2023.",
      "quote": ets_chem_quote,
      "url": ets_chem_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "Applicants should identify UNH Chemistry faculty whose research interests them and explain why in the statement.",
      "quote": "3) Those UNH Chemistry faculty whose research interests you and why.",
      "url": "https://gradschool.unh.edu/program/phd/chemistry"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "math",
    "department": "Department of Mathematics and Statistics",
    "program_page": "https://gradschool.unh.edu/program/phd/mathematics",
    "deadline": {
      "code": "2027-02-15",
      "value": "Fall: February 15",
      "quote": "Fall: February 15",
      "url": "https://gradschool.unh.edu/program/phd/mathematics",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "Not stated",
      "value": "Not stated on Mathematics Ph.D. program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/mathematics"
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/mathematics"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "statistics",
    "department": "Department of Mathematics and Statistics",
    "program_page": "https://gradschool.unh.edu/program/phd/statistics",
    "deadline": {
      "code": "2027-02-15",
      "value": "Fall: February 15",
      "quote": "Fall: February 15",
      "url": "https://gradschool.unh.edu/program/phd/statistics",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Statistics subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/statistics"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "cs",
    "department": "Department of Computer Science",
    "program_page": "https://gradschool.unh.edu/program/phd/computer-science",
    "deadline": {
      "code": "2027-04-01",
      "value": "Fall: Jan. 1 (for special funding opportunities); March 1 (for full funding opportunities); April 1 (final)",
      "quote": "Fall: Jan. 1 (for special funding opportunities); March 1 (for full funding opportunities); April 1 (final)",
      "url": "https://gradschool.unh.edu/program/phd/computer-science",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE General test scores are normally required but may be waived for students who have taken computer science courses at UNH.",
      "quote": "GRE General test scores are normally required but may be waived for students who have taken computer science courses at UNH.",
      "url": "https://gradschool.unh.edu/program/phd/computer-science"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Computer Science subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/computer-science"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "A Ph.D. student who has previously completed a Masters degree must take classes from at least three faculty; all other students must take classes from at least five faculty.",
      "quote": "To satisfy this requirement, a Ph.D. student who has previously completed a Masters degree, must take classes from at least three different faculty. All other students must take classes from at least five different faculty.",
      "url": "https://gradschool.unh.edu/program/phd/computer-science"
    }
  },
  {
    "field": "ece",
    "department": "Department of Electrical and Computer Engineering",
    "program_page": "https://gradschool.unh.edu/program/phd/electrical-computer-engineering",
    "deadline": {
      "code": "2027-04-01",
      "value": "Fall: Feb. 15 (for funding); April 1 (recommended US; final international); July 1 (final)",
      "quote": "Fall: Feb. 15 (for funding); April 1 (recommended US; final international); July 1 (final)",
      "url": "https://gradschool.unh.edu/program/phd/electrical-computer-engineering",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE General test scores are normally required, but UNH ECE alumni with a minimum GPA of 3.0 may request a waiver.",
      "quote": "GRE General test scores are normally required, but UNH ECE alumni with a minimum GPA of 3.0 may request a waiver using our waiver process.",
      "url": "https://gradschool.unh.edu/program/phd/electrical-computer-engineering"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Electrical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/electrical-computer-engineering"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Students entering the Ph.D. program with a B.S. degree must successfully complete program requirements.",
      "quote": "Students entering the Ph.D. program with a B.S. degree must successfully complete the following minimum program requirements:",
      "url": "https://gradschool.unh.edu/program/phd/electrical-computer-engineering"
    }
  },
  {
    "field": "mech",
    "department": "Department of Mechanical Engineering",
    "program_page": "https://gradschool.unh.edu/program/phd/mechanical-engineering",
    "deadline": {
      "code": "2027-02-15",
      "value": "Fall: February 15",
      "quote": "Fall: February 15",
      "url": "https://gradschool.unh.edu/program/phd/mechanical-engineering",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE General test scores are normally required but are waived for UNH Mechanical Engineering alumni with a minimum GPA of 3.0.",
      "quote": "GRE General test scores are normally required but are waived for UNH Mechanical Engineering alumni with a minimum GPA of 3.0.",
      "url": "https://gradschool.unh.edu/program/phd/mechanical-engineering"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Mechanical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/mechanical-engineering"
    },
    "funding": {
      "code": "Typical",
      "value": "With teaching assistantships and diverse coursework options, this program prepares you for careers in academia, government, and industry.",
      "quote": "With teaching assistantships and diverse coursework options, this program prepares you for careers in academia, government, and industry.",
      "url": "https://gradschool.unh.edu/program/phd/mechanical-engineering"
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "chemeng",
    "department": "Department of Chemical Engineering",
    "program_page": "https://gradschool.unh.edu/program/phd/chemical-engineering",
    "deadline": {
      "code": "2027-02-15",
      "value": "Fall: February 15",
      "quote": "Fall: February 15",
      "url": "https://gradschool.unh.edu/program/phd/chemical-engineering",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Required",
      "value": "GRE scores are required. Request that official test scores be sent directly to the Graduate School by the testing service.",
      "quote": "GRE scores are required. Request that official test scores be sent directly to the Graduate School by the testing service.",
      "url": "https://gradschool.unh.edu/program/phd/chemical-engineering"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Chemical Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/chemical-engineering"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "civil",
    "department": "Department of Civil and Environmental Engineering",
    "program_page": "https://gradschool.unh.edu/program/phd/civil-environmental-engineering",
    "deadline": {
      "code": "2027-04-01",
      "value": "Fall: Jan. 15 (for funding); April 1 (recommended US; final international); July 1 (final)",
      "quote": "Fall: Jan. 15 (for funding); April 1 (recommended US; final international); July 1 (final)",
      "url": "https://gradschool.unh.edu/program/phd/civil-environmental-engineering",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Optional",
      "value": "The GRE scores are optional, if you wish to provide scores please email the scores directly to the department once you have submitted your application online.",
      "quote": "The GRE scores are optional, if you wish to provide scores please email the scores directly to the department once you have submitted your application online.",
      "url": "https://gradschool.unh.edu/program/phd/civil-environmental-engineering"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Civil Engineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/civil-environmental-engineering"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "bme",
    "department": "Bioengineering Graduate Program",
    "program_page": "https://gradschool.unh.edu/program/phd/bioengineering",
    "deadline": {
      "code": "2027-02-15",
      "value": "Fall: February 15",
      "quote": "Fall: February 15",
      "url": "https://gradschool.unh.edu/program/phd/bioengineering",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Bioengineering subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/bioengineering"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "biology",
    "department": "Department of Biological Sciences",
    "program_page": "https://gradschool.unh.edu/program/phd/integrative-biology",
    "deadline": {
      "code": "2027-02-01",
      "value": "Fall: December 15 (priority*); February 1 (final) *Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "quote": "Fall: December 15 (priority*); February 1 (final) *Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "url": "https://gradschool.unh.edu/program/phd/integrative-biology",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Not required",
      "value": "The GRE (general or topical) is NOT REQUIRED for admission by any of the programs in the Department of Biological Sciences.",
      "quote": "The GRE (general or topical) is NOT REQUIRED for admission by any of the programs in the Department of Biological Sciences.",
      "url": "https://gradschool.unh.edu/program/phd/integrative-biology"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Biology subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/integrative-biology"
    },
    "funding": {
      "code": "Typical",
      "value": "Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "quote": "Fall: December 15 (priority*); February 1 (final) *Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "url": "https://gradschool.unh.edu/program/phd/integrative-biology"
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "biomed",
    "department": "Department of Molecular, Cellular, and Biomedical Sciences",
    "program_page": "https://gradschool.unh.edu/program/phd/biochemistry",
    "deadline": {
      "code": "2027-04-15",
      "value": "Fall: December 15 (priority), April 15 (final) - Applications completed by December 15 will be given priority consideration for admission and financial support with an assistantship. Applications completed after December 15 will be considered based on openings and funding. Applications are accepted until April 15, the final deadline.",
      "quote": "Fall: December 15 (priority), April 15 (final) - Applications completed by December 15 will be given priority consideration for admission and financial support with an assistantship. Applications completed after December 15 will be considered based on openings and funding. Applications are accepted until April 15, the final deadline.",
      "url": "https://gradschool.unh.edu/program/phd/biochemistry",
      "inferred": "year"
    },
    "gre_general": {
      "code": "Not required",
      "value": "Please note the GRE is no longer required. No GRE score is needed to apply.",
      "quote": "Please note the GRE is no longer required. No GRE score is needed to apply.",
      "url": "https://gradschool.unh.edu/program/phd/biochemistry"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Biochemistry subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Recommended",
      "value": "Applicants should review MCBS graduate program faculty research descriptions and identify by name two or three potential mentors for graduate studies.",
      "quote": "3) a review of MCBS graduate program faculty research descriptions and the identification by name of two or three potential mentors for your graduate studies.",
      "url": "https://gradschool.unh.edu/program/phd/biochemistry"
    },
    "funding": {
      "code": "Typical",
      "value": "Students admitted to the Ph.D. Program are typically supported by Research Assistantships or Teaching Assistantships.",
      "quote": "Students admitted to the Ph.D. Program are typically supported by Research Assistantships or Teaching Assistantships",
      "url": "https://gradschool.unh.edu/program/phd/biochemistry"
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "neuro",
    "department": "Neuroscience and Behavior Graduate Program",
    "program_page": "https://gradschool.unh.edu/program/phd/neuroscience-behavior",
    "deadline": {
      "code": "2027-02-01",
      "value": "Fall: December 15 (priority*); February 1 (final) *Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "quote": "Fall: December 15 (priority*); February 1 (final) *Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "url": "https://gradschool.unh.edu/program/phd/neuroscience-behavior",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Neuroscience subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Not stated",
      "value": "Not stated on program page.",
      "quote": "",
      "url": "https://gradschool.unh.edu/program/phd/neuroscience-behavior"
    },
    "funding": {
      "code": "Typical",
      "value": "Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "quote": "Fall: December 15 (priority*); February 1 (final) *Applications completed by December 15 will be given priority consideration for admission and financial support. Applications completed after December 15 will be considered based on openings and funding.",
      "url": "https://gradschool.unh.edu/program/phd/neuroscience-behavior"
    },
    "entry_route": {
      "code": "Either",
      "value": "Applicants with bachelor's degrees may apply directly to doctoral programs.",
      "quote": entry_quote,
      "url": entry_url
    }
  },
  {
    "field": "earth",
    "department": "Department of Earth Sciences",
    "program_page": "https://gradschool.unh.edu/program/phd/earth-environmental-sciences",
    "deadline": {
      "code": "2027-08-01",
      "value": "Fall: May 15 (recommended); August 1 (final; timely processing of applications not guaranteed for late submissions)",
      "quote": "Fall: May 15 (recommended); August 1 (final; timely processing of applications not guaranteed for late submissions)",
      "url": "https://gradschool.unh.edu/program/phd/earth-environmental-sciences",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Earth Sciences subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Required",
      "value": "Applicants must secure a faculty member from the current list of NRESS faculty who will agree to serve as advisor and potentially provide funding for the student’s doctoral studies.",
      "quote": "Applicants must secure a faculty member from the current list of NRESS faculty who will agree to serve as advisor and potentially provide funding for the student’s doctoral studies.",
      "url": "https://gradschool.unh.edu/program/phd/earth-environmental-sciences"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Students entering the program without a master's degree are expected to complete a minimum of 36 credit hours.",
      "quote": "Students Entering the Program without a Master's Degree",
      "url": "https://gradschool.unh.edu/program/phd/earth-environmental-sciences"
    }
  },
  {
    "field": "environment",
    "department": "Natural Resources and Earth Systems Science Program",
    "program_page": "https://gradschool.unh.edu/natural-resources-earth-systems-science-phd/program/phd/natural-resources-environmental-studies",
    "deadline": {
      "code": "2027-08-01",
      "value": "Fall: May 15 (recommended); August 1 (final; timely processing of applications not guaranteed for late submissions)",
      "quote": "Fall: May 15 (recommended); August 1 (final; timely processing of applications not guaranteed for late submissions)",
      "url": "https://gradschool.unh.edu/natural-resources-earth-systems-science-phd/program/phd/natural-resources-environmental-studies",
      "inferred": "year"
    },
    "gre_subject": {
      "code": "No subject test",
      "value": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study; ETS offers no Environmental Studies subject test.",
      "quote": ets_general_quote,
      "url": ets_general_url
    },
    "supervisor": {
      "code": "Required",
      "value": "Applicants must secure a faculty member from the current list of NRESS faculty who will agree to serve as advisor and potentially provide funding for the student’s doctoral studies.",
      "quote": "Applicants must secure a faculty member from the current list of NRESS faculty who will agree to serve as advisor and potentially provide funding for the student’s doctoral studies.",
      "url": "https://gradschool.unh.edu/natural-resources-earth-systems-science-phd/program/phd/natural-resources-environmental-studies"
    },
    "funding": {
      "code": "Typical",
      "value": "Students appointed as assistants, graduate fellows and graduate part-time lecturers receive tuition waivers in addition to their stipends during the period of their appointment.",
      "quote": funding_quote,
      "url": funding_url
    },
    "entry_route": {
      "code": "Either",
      "value": "Students entering the program without a master's degree are expected to complete a minimum of 36 credit hours.",
      "quote": "Students Entering the Program without a Master's Degree",
      "url": "https://gradschool.unh.edu/natural-resources-earth-systems-science-phd/program/phd/natural-resources-environmental-studies"
    }
  }
]

for p in programs:
    fid = p["field"]
    prog_data = {
      "id": f"unh--{fid}",
      "university": "unh",
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
    
    with open(STAGE / 'programs' / f"unh--{fid}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote data/staging/programs/unh--{fid}.json")
