import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "pages"
STAGING_UNIS = ROOT / "data" / "staging" / "universities"
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_UNIS.mkdir(parents=True, exist_ok=True)
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

# Clean out old uah--*.json files if any were created
for old_f in STAGING_PROGS.glob("uah--*.json"):
    old_f.unlink()

import hashlib
def cache_file(url):
    k = hashlib.sha1(url.encode()).hexdigest()[:16]
    return CACHE / f"{k}.json"

def verify_quote(url, quote):
    if not quote:
        return
    f = cache_file(url)
    if not f.exists():
        raise FileNotFoundError(f"Cache missing for {url}")
    t = json.load(open(f, "r", encoding="utf-8"))["text"]
    q_norm = " ".join(quote.split())
    t_norm = " ".join(t.split())
    if q_norm not in t_norm:
        raise ValueError(f"Quote mismatch for {url}:\nQUOTE: {quote[:100]}...\n")

# ETS quote
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
verify_quote(ets_url, ets_quote)

# Common UAH quotes
uah_adm_url = "https://www.uah.edu/admissions/graduate/apply-for-admission"
uah_intl_url = "https://www.uah.edu/admissions/graduate/apply-for-admission/international-students"
uah_test_url = "https://www.uah.edu/admissions/graduate/apply-for-admission/test-score-requirements"
uah_prog_url = "https://www.uah.edu/graduate/programs"

uah_funding_quote = "A full-time (9-12 enrolled hours) assistantship (20 hours/week) typically covers full tuition benefits, full health insurance (single person), a stipend, and associated fees."
uah_entry_quote = "To qualify for unconditional admission to the UAH Graduate School, you must hold a bachelor's degree, or equivalent, from an approved institution and have a minimum 3.0 GPA on your undergraduate record."

verify_quote(uah_adm_url, uah_funding_quote)
verify_quote(uah_adm_url, uah_entry_quote)

# -------------------------------------------------------------
# 1. ALABAMAHUNTSVILLE (UAH) UNIVERSITY
# -------------------------------------------------------------
uah_uni = {
  "id": "alabamahuntsville",
  "institution": "University of Alabama in Huntsville",
  "country": "USA",
  "region": "Alabama",
  "grad_page": "https://www.uah.edu/admissions/graduate/apply-for-admission",
  "checked": "2026-10-29",
  "notes": "",
  "fields": {
    "app_fee": {
      "code": "60 USD",
      "value": "$60 nonrefundable application fee",
      "quote": "Complete your application through your Charger account and pay the nonrefundable $60 application fee.",
      "url": uah_adm_url
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Fee waivers are available for current UAH JUMP students and full-time employees, with discounted fees for UAH graduates, but UAH has no general waiver process for others.",
      "quote": "Current UAH JUMP students and full-time UAH employees will automatically have their application fees waived upon applying. Current UAH undergraduate students and graduates of UAH will receive a discounted application fee of $35.00. If you are a current UAH graduate student seeking to switch or add a program, you might be eligible for a fee waiver. Please email admissions@uah.edu to see if you are eligible. If you do not fall into one of the above categories, then we will not be able to waive or discount your application fee. We do not have a process for applying for an application fee waiver.",
      "url": uah_adm_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Central graduate admissions does not set a single campus-wide GRE requirement; requirements vary by program.",
      "quote": "Are GRE or GMAT scores required for admission? It depends on the program to which you are applying. Please view our test score requirements to determine if your program requires test scores for admissions consideration.",
      "url": uah_adm_url
    },
    "toefl_min": {
      "code": "79",
      "value": "TOEFL iBT minimum score is 79 (no sub-score below 19) on the old scale or 4 on the new scale.",
      "quote": "TOEFL iBT: Old scoring scale - 79 (no sub-score below 19) OR New scoring scale - 4 (no section score below 3.5)",
      "url": uah_intl_url
    },
    "ielts_min": {
      "code": "6.0",
      "value": "IELTS Academic minimum overall band is 6.0 (no sub-score below 6.0).",
      "quote": "IELTS: 6.0 (no sub-score below 6.0)",
      "url": uah_intl_url
    },
    "english_waiver": {
      "code": "No",
      "value": "No waiver for English-medium education outside approved exempt countries (US accredited institution, IB diploma, or schooling in an official English language country).",
      "quote": "You do not need to submit a language test score if: You graduated from an accredited high school or university in the United States. You graduated from an International Baccalaureate high school with an IB diploma. Your first language is English and you completed your schooling in English in a country where English is an official language.",
      "url": uah_intl_url
    }
  }
}

for k, fld in uah_uni["fields"].items():
    verify_quote(fld["url"], fld["quote"])

with open(STAGING_UNIS / "alabamahuntsville.json", "w", encoding="utf-8") as f:
    json.dump(uah_uni, f, indent=2)

print("Verified & saved alabamahuntsville.json")

# -------------------------------------------------------------
# 2. UAH PROGRAMS
# -------------------------------------------------------------
uah_progs = [
    {
        "id": "alabamahuntsville--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics & Astronomy",
        "program_page": "https://www.uah.edu/science/departments/physics/ph-graduate-programs",
        "deadline_code": "2027-01-16",
        "deadline_val": "January 16 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 16 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for the Physics PhD program.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "Not stated",
        "subj_val": "GRE Subject test requirement is not stated.",
        "subj_q": "",
        "subj_url": uah_test_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--astronomy",
        "field": "astronomy",
        "also_fields": ["physics"],
        "department": "Department of Space Science",
        "program_page": "https://www.uah.edu/science/departments/space-science/graduate-programs",
        "deadline_code": "2027-02-01",
        "deadline_val": "February 1 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "February 1 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for the Space Science PhD program.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Space Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--math",
        "field": "math",
        "also_fields": ["statistics"],
        "department": "Department of Mathematical Sciences",
        "program_page": "https://www.uah.edu/science/departments/math/ma-graduate-programs",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Recommended",
        "gre_val": "GRE scores are not required but highly recommended for graduate assistantship consideration.",
        "gre_q": "Not required but highly recommended. Providing GRE scores will greatly increase student's chance in receiving a graduate assistantship",
        "gre_url": uah_test_url,
        "subj_code": "Not stated",
        "subj_val": "GRE Mathematics Subject Test requirement is not stated.",
        "subj_q": "",
        "subj_url": uah_test_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": "https://www.uah.edu/science/departments/chemistry",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 application deadline for Fall entry term",
        "deadline_q": "January 31 - Application Deadline for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for the Chemistry PhD program.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "Not stated",
        "subj_val": "GRE Chemistry subject test requirement is not stated.",
        "subj_q": "",
        "subj_url": uah_test_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--cs",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science",
        "program_page": "https://www.uah.edu/science/departments/computer-science/cs-graduate-programs",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for the Computer Science PhD program.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Computer Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--ece",
        "field": "ece",
        "also_fields": [],
        "department": "Department of Electrical and Computer Engineering",
        "program_page": "https://www.uah.edu/eng/departments/ece",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for Electrical Engineering PhD; Computer Engineering PhD requires GRE.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical and Computer Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": "Electrical Engineering PhD does not require GRE; Computer Engineering PhD requires GRE."
    },
    {
        "id": "alabamahuntsville--mech",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical & Aerospace Engineering",
        "program_page": "https://www.uah.edu/eng/departments/mae",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term; final deadline June 15",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for Mechanical Engineering or Aerospace Systems Engineering PhD programs.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--civil",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Civil and Environmental Engineering",
        "program_page": "https://www.uah.edu/eng/departments/cee/graduate-program/cee-phd-requirements",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required per central test score requirements table.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--materials",
        "field": "materials",
        "also_fields": [],
        "department": "Department of Chemical & Materials Engineering",
        "program_page": "https://www.uah.edu/eng/departments/cme/programs/graduate",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for Materials Science - Engineering Track; required for Science Track.",
        "gre_q": "Not required",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Materials Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": "Materials Science Engineering Track does not require GRE; Science Track requires GRE."
    },
    {
        "id": "alabamahuntsville--earth",
        "field": "earth",
        "also_fields": ["environment"],
        "department": "Department of Atmospheric & Earth Science",
        "program_page": "https://www.uah.edu/science/departments/atmospheric-earth-science/aes-graduate-programs/admission-requirements",
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 priority application deadline for Fall entry term",
        "deadline_q": "January 1 - Priority Application Deadline for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Recommended",
        "gre_val": "GRE scores are not required but highly recommended for assistantship consideration.",
        "gre_q": "Not required but highly recommended. Providing GRE scores will greatly increase student's chance in receiving a graduate assistantship",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Atmospheric and Earth Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "alabamahuntsville--biology",
        "field": "biology",
        "also_fields": ["biomed"],
        "department": "Biotechnology Science and Engineering Program",
        "program_page": "https://www.uah.edu/science/departments/biotechnology/admission-requirements",
        "deadline_code": "2027-01-31",
        "deadline_val": "January 31 priority deadline for GRA/GTA consideration for Fall entry term",
        "deadline_q": "January 31 - Priority Deadline for GRA/GTA consideration for Fall entry term",
        "deadline_url": uah_prog_url,
        "gre_code": "Recommended",
        "gre_val": "GRE scores not required but strongly encouraged for Graduate Research Assistant applicants.",
        "gre_q": "GRE scores not required but strongly encouraged for Graduate Research Assistant applicants",
        "gre_url": uah_test_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biotechnology subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": "Interdisciplinary PhD program spanning Biology, Chemistry, and Chemical & Materials Engineering."
    }
]

for p in uah_progs:
    verify_quote(p["deadline_url"], p["deadline_q"])
    verify_quote(p["gre_url"], p["gre_q"])
    if p["subj_q"]:
        verify_quote(p["subj_url"], p["subj_q"])
    
    rec = {
        "id": p["id"],
        "university": "alabamahuntsville",
        "field": p["field"],
        "also_fields": p["also_fields"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": "2026-10-29",
        "notes": p["notes"],
        "fields": {
            "deadline": {
                "code": p["deadline_code"],
                "value": p["deadline_val"],
                "quote": p["deadline_q"],
                "url": p["deadline_url"]
            },
            "gre_general": {
                "code": p["gre_code"],
                "value": p["gre_val"],
                "quote": p["gre_q"],
                "url": p["gre_url"]
            },
            "gre_subject": {
                "code": p["subj_code"],
                "value": p["subj_val"],
                "quote": p["subj_q"],
                "url": p["subj_url"]
            },
            "supervisor": {
                "code": "Not stated",
                "value": "Pre-application supervisor requirement is not stated.",
                "quote": "",
                "url": p["program_page"]
            },
            "funding": {
                "code": "Typical",
                "value": "Full-time assistantship typically covers full tuition benefits, health insurance, a stipend, and fees.",
                "quote": uah_funding_quote,
                "url": uah_adm_url
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Unconditional admission requires a bachelor's degree or equivalent with minimum 3.0 GPA.",
                "quote": uah_entry_quote,
                "url": uah_adm_url
            }
        }
    }
    with open(STAGING_PROGS / f"{p['id']}.json", "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2)

print(f"Verified & saved {len(uah_progs)} UAH programs")

# -------------------------------------------------------------
# 3. ALASKAFAIRBANKS (UAF) UNIVERSITY
# -------------------------------------------------------------
uaf_adm_page = "https://www.uaf.edu/gradschool/prospective-students/graduate-admissions.php"
uaf_cat_adm = "https://catalog.uaf.edu/getting-started/admission/"
uaf_asst_url = "https://www.uaf.edu/gradschool/current-students/assistantships.php"

uaf_uni = {
  "id": "alaskafairbanks",
  "institution": "University of Alaska Fairbanks",
  "country": "USA",
  "region": "Alaska",
  "grad_page": uaf_adm_page,
  "checked": "2026-10-29",
  "notes": "",
  "fields": {
    "app_fee": {
      "code": "75 USD",
      "value": "$75 nonrefundable application fee",
      "quote": "$75 nonrefundable application fee",
      "url": uaf_adm_page
    },
    "fee_waiver": {
      "code": "Available",
      "value": "Ph.D. applicants can apply for free using fee waiver code #UAFR1.",
      "quote": "Apply to UAF for Free! For a limited time, you can apply to our Ph.D. program for free using the fee waiver code #UAFR1.",
      "url": uaf_adm_page
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Central graduate admissions does not set a single campus-wide GRE requirement; requirements vary by department.",
      "quote": "The University of Alaska Fairbanks does not require submission of Graduate Record Exam (GRE) scores from all students. However, individual departments may require or allow submission of GRE scores.",
      "url": uaf_cat_adm
    },
    "toefl_min": {
      "code": "79",
      "value": "TOEFL minimum score is 79.",
      "quote": "A minimum TOEFL score of 79",
      "url": uaf_cat_adm
    },
    "ielts_min": {
      "code": "6.5",
      "value": "IELTS Academic minimum overall band is 6.5.",
      "quote": "A minimum IELTS score of 6.5",
      "url": uaf_cat_adm
    },
    "english_waiver": {
      "code": "No",
      "value": "No waiver for English-medium education outside approved exempt countries; India is not exempt.",
      "quote": "Applicants who have completed secondary or baccalaureate education, where the primary language of instruction was English, from one of the following countries or territories** are exempt from this requirement:",
      "url": uaf_cat_adm
    }
  }
}

for k, fld in uaf_uni["fields"].items():
    verify_quote(fld["url"], fld["quote"])

with open(STAGING_UNIS / "alaskafairbanks.json", "w", encoding="utf-8") as f:
    json.dump(uaf_uni, f, indent=2)

print("Verified & saved alaskafairbanks.json")

# -------------------------------------------------------------
# 4. UAF PROGRAMS
# -------------------------------------------------------------
uaf_funding_quote = "Compensation: Regular stipend, graduate health insurance, tuition support, and in select cases, mandatory student fee coverage."
verify_quote(uaf_asst_url, uaf_funding_quote)

uaf_entry_quote = "In general, applicants may be admitted to a graduate program if they have a bachelor’s degree from an accredited institution with at least a 3.0 (B) cumulative undergraduate GPA and a 3.0 (B) GPA in their major."
verify_quote(uaf_cat_adm, uaf_entry_quote)

uaf_deadline_general = "Applicants should apply to a graduate degree program at least six to nine months before the beginning of the semester in which they plan to enroll. Most departments require earlier submission of credentials for acceptance to their program. Contact the department for specific deadlines."
verify_quote(uaf_cat_adm, uaf_deadline_general)

uaf_progs = [
    {
        "id": "alaskafairbanks--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": "https://catalog.uaf.edu/phd/physics/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/physics/",
        "subj_code": "Optional",
        "subj_val": "GRE Physics Subject test scores are not required, but may be considered if submitted.",
        "subj_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "subj_url": "https://catalog.uaf.edu/phd/physics/",
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/physics/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--astronomy",
        "field": "astronomy",
        "also_fields": ["physics"],
        "department": "Department of Physics",
        "program_page": "https://catalog.uaf.edu/phd/physics-space/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/physics-space/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Space Physics subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/physics-space/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--math",
        "field": "math",
        "also_fields": ["statistics"],
        "department": "Department of Mathematical Sciences",
        "program_page": "https://catalog.uaf.edu/phd/mathematics/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE test scores are not required; GRE general or GRE math subject test scores may still be submitted without penalty for absence.",
        "gre_q": "Note: GRE test scores are not required as part of a complete application for the Ph.D. program in mathematics. You may still submit GRE general or GRE math subject test scores if you choose, but their absence will not negatively impact your application.",
        "gre_url": "https://catalog.uaf.edu/phd/mathematics/",
        "subj_code": "Optional",
        "subj_val": "GRE Mathematics Subject Test is not required; applicant may submit if desired.",
        "subj_q": "Note: GRE test scores are not required as part of a complete application for the Ph.D. program in mathematics. You may still submit GRE general or GRE math subject test scores if you choose, but their absence will not negatively impact your application.",
        "subj_url": "https://catalog.uaf.edu/phd/mathematics/",
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/mathematics/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--biology",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Biology & Wildlife",
        "program_page": "https://catalog.uaf.edu/phd/biological-sciences/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/biological-sciences/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biological Sciences subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Required",
        "supervisor_val": "Students are typically not admitted unless a faculty advisor has agreed to serve as mentor prior to application.",
        "supervisor_q": "Note: Students are typically not admitted to the program unless a faculty advisor has agreed to serve as the mentor. Applicants should contact potential advisors before applying.",
        "supervisor_url": "https://catalog.uaf.edu/phd/biological-sciences/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--neuro",
        "field": "neuro",
        "also_fields": ["biomed"],
        "department": "Biochemistry & Neuroscience Program",
        "program_page": "https://catalog.uaf.edu/phd/biochemistry-neuroscience/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/biochemistry-neuroscience/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Neuroscience subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Required",
        "supervisor_val": "Students are typically not admitted unless a faculty advisor has agreed to serve as mentor prior to application.",
        "supervisor_q": "Note: Students are typically not admitted to the program unless a faculty advisor has agreed to serve as the mentor. Applicants should contact potential advisors before applying.",
        "supervisor_url": "https://catalog.uaf.edu/phd/biochemistry-neuroscience/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--chemistry",
        "field": "chemistry",
        "also_fields": ["environment"],
        "department": "Department of Chemistry and Biochemistry",
        "program_page": "https://catalog.uaf.edu/phd/environmental-chemistry/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/environmental-chemistry/",
        "subj_code": "Not stated",
        "subj_val": "GRE Subject test requirement is not stated.",
        "subj_q": "",
        "subj_url": "https://catalog.uaf.edu/phd/environmental-chemistry/",
        "supervisor_code": "Required",
        "supervisor_val": "Students are typically not admitted unless a faculty advisor has agreed to serve as mentor prior to application.",
        "supervisor_q": "Note: Students are typically not admitted to the program unless a faculty advisor has agreed to serve as the mentor. Applicants should contact potential advisors before applying.",
        "supervisor_url": "https://catalog.uaf.edu/phd/environmental-chemistry/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--earth",
        "field": "earth",
        "also_fields": [],
        "department": "Department of Atmospheric Sciences",
        "program_page": "https://catalog.uaf.edu/phd/atmospheric-sciences/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Not stated",
        "gre_val": "Program catalog does not specify a GRE requirement; central UAF policy leaves GRE to individual departments.",
        "gre_q": "The University of Alaska Fairbanks does not require submission of Graduate Record Exam (GRE) scores from all students. However, individual departments may require or allow submission of GRE scores.",
        "gre_url": uaf_cat_adm,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Atmospheric Sciences subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/atmospheric-sciences/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--environment",
        "field": "environment",
        "also_fields": [],
        "department": "Department of Natural Resources and Environment",
        "program_page": "https://catalog.uaf.edu/phd/natural-resources-sustainability/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/natural-resources-sustainability/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Environmental Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Required",
        "supervisor_val": "Students are required to have a faculty sponsor upon entering the program.",
        "supervisor_q": "Students are required to have a faculty sponsor upon entering the program. A letter of support from a DNRE or HSEM faculty member in addition to three letters of recommendation must be submitted with the graduate application.",
        "supervisor_url": "https://catalog.uaf.edu/phd/natural-resources-sustainability/",
        "notes": ""
    },
    {
        "id": "alaskafairbanks--civil",
        "field": "civil",
        "also_fields": [],
        "department": "College of Engineering and Mines",
        "program_page": "https://catalog.uaf.edu/phd/engineering/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/engineering/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/engineering/",
        "notes": "Ph.D. in Engineering with concentration in Civil Engineering."
    },
    {
        "id": "alaskafairbanks--mech",
        "field": "mech",
        "also_fields": [],
        "department": "College of Engineering and Mines",
        "program_page": "https://catalog.uaf.edu/phd/engineering/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/engineering/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/engineering/",
        "notes": "Ph.D. in Engineering with concentration in Mechanical Engineering."
    },
    {
        "id": "alaskafairbanks--ece",
        "field": "ece",
        "also_fields": ["cs"],
        "department": "College of Engineering and Mines",
        "program_page": "https://catalog.uaf.edu/phd/engineering/",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not specify a separate closing date; applicants should apply at least six to nine months prior to enrollment.",
        "deadline_q": uaf_deadline_general,
        "deadline_url": uaf_cat_adm,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but may be considered if submitted.",
        "gre_q": "Official test results: GRE scores are not required for this program, but may be considered if submitted",
        "gre_url": "https://catalog.uaf.edu/phd/engineering/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical/Computer Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor requirement is not stated.",
        "supervisor_q": "",
        "supervisor_url": "https://catalog.uaf.edu/phd/engineering/",
        "notes": "Ph.D. in Engineering with concentration in Electrical Engineering or Computer Engineering."
    }
]

for p in uaf_progs:
    verify_quote(p["deadline_url"], p["deadline_q"])
    verify_quote(p["gre_url"], p["gre_q"])
    if p["subj_q"]:
        verify_quote(p["subj_url"], p["subj_q"])
    if p["supervisor_q"]:
        verify_quote(p["supervisor_url"], p["supervisor_q"])
    
    rec = {
        "id": p["id"],
        "university": "alaskafairbanks",
        "field": p["field"],
        "also_fields": p["also_fields"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": "2026-10-29",
        "notes": p["notes"],
        "fields": {
            "deadline": {
                "code": p["deadline_code"],
                "value": p["deadline_val"],
                "quote": p["deadline_q"],
                "url": p["deadline_url"]
            },
            "gre_general": {
                "code": p["gre_code"],
                "value": p["gre_val"],
                "quote": p["gre_q"],
                "url": p["gre_url"]
            },
            "gre_subject": {
                "code": p["subj_code"],
                "value": p["subj_val"],
                "quote": p["subj_q"],
                "url": p["subj_url"]
            },
            "supervisor": {
                "code": p["supervisor_code"],
                "value": p["supervisor_val"],
                "quote": p["supervisor_q"],
                "url": p["supervisor_url"]
            },
            "funding": {
                "code": "Typical",
                "value": "Graduate assistantships provide regular stipend, graduate health insurance, and tuition support.",
                "quote": uaf_funding_quote,
                "url": uaf_asst_url
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Admission requires a bachelor's degree from an accredited institution with at least 3.0 cumulative and major GPA.",
                "quote": uaf_entry_quote,
                "url": uaf_cat_adm
            }
        }
    }
    with open(STAGING_PROGS / f"{p['id']}.json", "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2)

print(f"Verified & saved {len(uaf_progs)} UAF programs")
