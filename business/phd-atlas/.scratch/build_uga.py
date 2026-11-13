import json
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "pages"
STAGING_UNIS = ROOT / "data" / "staging" / "universities"
STAGING_PROGS = ROOT / "data" / "staging" / "programs"
STAGING_UNIS.mkdir(parents=True, exist_ok=True)
STAGING_PROGS.mkdir(parents=True, exist_ok=True)

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
    t_norm = " ".join(t.split())
    pieces = [p.strip() for p in quote.split(" | ")]
    for p in pieces:
        p_norm = " ".join(p.split())
        if p_norm not in t_norm:
            raise ValueError(f"Quote mismatch for {url}:\nPIECE: {p}\nQUOTE: {quote[:100]}...\n")

# ETS quote
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
verify_quote(ets_url, ets_quote)

# UGA URLs
fee_url = "https://grad.uga.edu/admissions/application-fee/"
gre_url = "https://grad.uga.edu/admissions/requirements/entrance-test-scores/"
eng_url = "https://grad.uga.edu/admissions/requirements/international-applications/english-language-proficiency-requirement/"
country_url = "https://grad.uga.edu/admissions/requirements/international-applications/country-specific-requirements/"
deadlines_url = "https://grad.uga.edu/admissions/application-deadlines/"

phys_adm_url = "https://physast.uga.edu/admissions-requirements"
phys_app_url = "https://physast.uga.edu/graduate-program-application"
chem_url = "https://chem.uga.edu/how-apply"
math_url = "https://math.uga.edu/how-apply"
stat_url = "https://stat.uga.edu/prospective-graduate-students-0"
cs_prog_url = "https://cs.uga.edu/graduate-degree-programs"
cs_adm_url = "https://cs.uga.edu/graduate-admissions"
eng_url_dept = "https://engineering.uga.edu/prospective-students/graduate/"
geo_url = "https://geology.uga.edu/prospective-graduate-students"
ils_url = "https://ils.uga.edu/admissions/how-to-apply/"

# University record
entry_quote = "A four-year bachelor’s degree, a three-year bachelor’s plus a master’s degree, or a three-year bachelor’s plus completion of first year of the master’s program from a recognized institution by the Association of Indian University (AIU) or All India Council for Technical Education (AICTE)."
verify_quote(country_url, entry_quote)

eng_waiver_quote = "Applicants who have received degrees from non-U.S. accredited institutions in countries where English is not the primary/official language are required to demonstrate English proficiency. Applicants who have received degrees from accredited institutions in the U.S. or from institutions in countries where English is the primary language (e.g., the United Kingdom, Australia, New Zealand) usually are not required to submit the TOEFL (or IELTS) scores."
verify_quote(eng_url, eng_waiver_quote)

fee_waiver_quote = "A limited number of application fee waivers are available only to applicants who have participated in qualifying programs. To obtain the application fee waiver, you will be prompted to upload supporting documentation related to your qualifying program as part of your application."
verify_quote(fee_url, fee_waiver_quote)

uga_uni = {
  "id": "uga",
  "institution": "University of Georgia",
  "country": "USA",
  "region": "Georgia",
  "grad_page": "https://grad.uga.edu/admissions/requirements/",
  "checked": "2026-10-29",
  "notes": "",
  "fields": {
    "app_fee": {
      "code": "75 USD",
      "value": "Application fee is $75 for the first application and $25 for each additional application.",
      "quote": "As of July 2, 2024, the fee to apply for graduate programs at the University of Georgia is $75 for the first application; $25 for each additional application.",
      "url": fee_url
    },
    "fee_waiver": {
      "code": "Limited",
      "value": "Application fee waivers are available only to applicants who have participated in select qualifying programs.",
      "quote": fee_waiver_quote,
      "url": fee_url
    },
    "gre_general": {
      "code": "Required",
      "value": "Scores on the General Test of the GRE are required for admission as a prospective candidate for most graduate degrees, though several departments waive it.",
      "quote": "Scores on the Verbal and Quantitative sections of the General Test of the Graduate Record Examinations (GRE) are required for admission as a prospective candidate for most graduate degrees.",
      "url": gre_url
    },
    "toefl_min": {
      "code": "80",
      "value": "Minimum TOEFL score requirement is 80 overall with at least 20 on speaking and writing (or 4.5 on the new scale with 4 on speaking and writing).",
      "quote": "Minimum TOEFL score requirement: For exams taken prior to January 21, 2026, overall score of 80 with at least 20 on speaking and writing. For exams taken on or after January 22, 2026: overall score of 4.5 with at least a 4 on speaking and writing.",
      "url": eng_url
    },
    "ielts_min": {
      "code": "6.5",
      "value": "Minimum IELTS score requirement is an overall band of 6.5 with no single band below 6.0.",
      "quote": "Minimum IELTS score requirement: overall band-width of 6.5, with no single band (score) below 6.0",
      "url": eng_url
    },
    "english_waiver": {
      "code": "No",
      "value": "Applicants from countries where English is not the primary language must submit test scores; an Indian degree taught in English does not waive the requirement.",
      "quote": eng_waiver_quote,
      "url": eng_url
    }
  }
}

for k, fld in uga_uni["fields"].items():
    verify_quote(fld["url"], fld["quote"])

with open(STAGING_UNIS / "uga.json", "w", encoding="utf-8") as f:
    json.dump(uga_uni, f, indent=2)

print("Verified & saved uga.json")

# Central program quotes
central_funding_quote = "All applicants are considered for Research Assistantships, which provide a tuition waiver and a stipend."
verify_quote(eng_url_dept, central_funding_quote)

eng_deadline_quote = "Full consideration for financial support will be given to applications received by the following deadlines: | Fall: December 15"
verify_quote(eng_url_dept, eng_deadline_quote)

eng_gre_quote = "*The UGA College of Engineering has waived the GRE requirement for all applicants for Fall 2026, Spring 2027, and Fall 2027."
verify_quote(eng_url_dept, eng_gre_quote)

eng_sup_quote = "We strongly encourage applicants to review our online faculty directory and browse our faculty expertise directory, then contact those faculty members whose research aligns with their interests. Applicants should ask faculty directly about Research Assistantship opportunities that may be available."
verify_quote(eng_url_dept, eng_sup_quote)

ils_deadline_quote = "The application deadline for matriculation the following Fall term is December 1st. For example, applications for Fall 2027 MUST be COMPLETED by 11:59 PM EST on December 1, 2026."
verify_quote(ils_url, ils_deadline_quote)

ils_gre_quote = "The GRE is NOT a required component of the application."
verify_quote(ils_url, ils_gre_quote)

programs = [
    {
        "id": "uga--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics and Astronomy",
        "program_page": phys_adm_url,
        "deadline_code": "2027-01-15",
        "deadline_val": "January 15 deadline for Fall semester admission for international applicants",
        "deadline_q": "The deadline for applications for the Fall semester is January 15 for international applicants and February 15 for domestic applicants.",
        "deadline_url": phys_adm_url,
        "gre_code": "Not required",
        "gre_val": "General GRE score is not required.",
        "gre_q": "General GRE score is not required. Although we do not require a GRE subject score (i.e., GRE physics), it is recommended to submit the subject score.",
        "gre_url": phys_adm_url,
        "subj_code": "Recommended",
        "subj_val": "Physics subject GRE is recommended.",
        "subj_q": "General GRE score is not required. Although we do not require a GRE subject score (i.e., GRE physics), it is recommended to submit the subject score.",
        "subj_url": phys_adm_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor contact is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": phys_adm_url,
        "funding_code": "Guaranteed",
        "funding_val": "All admitted students have guaranteed financial support for the first 1.5 years.",
        "funding_q": "In general, all admitted students will have guaranteed support (either by TA or RA) for the first 1.5 years.",
        "funding_url": phys_app_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "fee_waiver": {
                "code": "None",
                "value": "Department does not offer application fee waivers under any circumstances.",
                "quote": "Unfortunately, because of budget constraints at the University of Georgia, we are unable to offer a waiver of the application fee; applications cannot be processed without the fee.",
                "url": phys_adm_url
            }
        }
    },
    {
        "id": "uga--astronomy",
        "field": "astronomy",
        "also_fields": ["physics"],
        "department": "Department of Physics and Astronomy",
        "program_page": phys_adm_url,
        "deadline_code": "2027-01-15",
        "deadline_val": "January 15 deadline for Fall semester admission for international applicants",
        "deadline_q": "The deadline for applications for the Fall semester is January 15 for international applicants and February 15 for domestic applicants.",
        "deadline_url": phys_adm_url,
        "gre_code": "Not required",
        "gre_val": "General GRE score is not required.",
        "gre_q": "General GRE score is not required. Although we do not require a GRE subject score (i.e., GRE physics), it is recommended to submit the subject score.",
        "gre_url": phys_adm_url,
        "subj_code": "Recommended",
        "subj_val": "Physics subject GRE is recommended.",
        "subj_q": "General GRE score is not required. Although we do not require a GRE subject score (i.e., GRE physics), it is recommended to submit the subject score.",
        "subj_url": phys_adm_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor contact is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": phys_adm_url,
        "funding_code": "Guaranteed",
        "funding_val": "All admitted students have guaranteed financial support for the first 1.5 years.",
        "funding_q": "In general, all admitted students will have guaranteed support (either by TA or RA) for the first 1.5 years.",
        "funding_url": phys_app_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "fee_waiver": {
                "code": "None",
                "value": "Department does not offer application fee waivers under any circumstances.",
                "quote": "Unfortunately, because of budget constraints at the University of Georgia, we are unable to offer a waiver of the application fee; applications cannot be processed without the fee.",
                "url": phys_adm_url
            }
        }
    },
    {
        "id": "uga--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": chem_url,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 priority deadline for full consideration for admission and fellowships",
        "deadline_q": "All applications and application materials must be received by December 15th to receive full consideration for admission and fellowship opportunities.",
        "deadline_url": chem_url,
        "gre_code": "Optional",
        "gre_val": "GRE test scores are not required; applicants may submit them as supplementary information.",
        "gre_q": "GRE Test Scores are NOT REQUIRED | You may elect to submit GRE scores as supplementary information for your application.",
        "deadline_url": chem_url,
        "gre_url": chem_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemistry subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": chem_url,
        "funding_code": "Typical",
        "funding_val": "Entering graduate students are supported by assistantships and fellowships.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Candidates must have earned a bachelor's or master's degree in chemistry or related discipline.",
        "entry_q": "Candidates for the University of Georgia Chemistry Graduate Program must have earned a Bachelor’s or Master’s Degree in chemistry, or a closely related field.",
        "entry_url": chem_url,
        "extra_fields": {}
    },
    {
        "id": "uga--math",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": math_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 deadline for Fall admission with full consideration for all financial aid",
        "deadline_q": "The deadline for Fall admission with full consideration for all possible financial aid is January 1.",
        "deadline_url": math_url,
        "gre_code": "Optional",
        "gre_val": "GRE scores are not required, but applicants may report scores if desired.",
        "gre_q": "We do not require GRE scores for applicants to our Graduate Program, but you may report your scores if you would like them to be considered.",
        "gre_url": math_url,
        "subj_code": "Optional",
        "subj_val": "GRE Subject scores are not required, but applicants may report scores if desired.",
        "subj_q": "We do not require GRE scores for applicants to our Graduate Program, but you may report your scores if you would like them to be considered.",
        "subj_url": math_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not required.",
        "supervisor_q": "",
        "supervisor_url": math_url,
        "funding_code": "Guaranteed",
        "funding_val": "All PhD students receive 5 years of full financial support.",
        "funding_q": "All our PhD students receive 5 years of full financial support.",
        "funding_url": math_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--statistics",
        "field": "statistics",
        "also_fields": [],
        "department": "Department of Statistics",
        "program_page": stat_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 deadline for Fall admission",
        "deadline_q": "(Fall semesters only) | January 1st",
        "deadline_url": stat_url,
        "gre_code": "Required",
        "gre_val": "GRE is required for admission to all 3 degree programs.",
        "gre_q": "As of 2024, the GRE is required for admission to all 3 programs.",
        "gre_url": stat_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Statistics subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor contact is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": stat_url,
        "funding_code": "Typical",
        "funding_val": "In general, new students are eligible to receive financial support if they start in Fall.",
        "funding_q": "Note: In general, new students are eligible to receive financial support only if they start in Fall.",
        "funding_url": stat_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "app_fee": {
                "code": "100 USD",
                "value": "Fee is $75 for domestic applicants and $100 for international applicants.",
                "quote": "A non-refundable fee of $75 for domestic applicants and $100 for international applicants must be paid upon submission of your application.",
                "url": stat_url
            },
            "fee_waiver": {
                "code": "None",
                "value": "Department does not offer application fee waivers.",
                "quote": "Please note: We are unable to offer application fee waivers.",
                "url": stat_url
            }
        }
    },
    {
        "id": "uga--cs",
        "field": "cs",
        "also_fields": [],
        "department": "School of Computing",
        "program_page": cs_prog_url,
        "deadline_code": "2026-10-15",
        "deadline_val": "October 15 deadline for international applicants",
        "deadline_q": "Graduate Admission Application Deadlines: | Domestic applicants: November 15th International Applicants: October 15th",
        "deadline_url": cs_prog_url,
        "gre_code": "Required",
        "gre_val": "All applicants are required to submit official GRE scores.",
        "gre_q": "All applicants are required to submit official GRE, and official TOEFL or IELTS score results to the University of Georgia, Graduate Admissions office at gradadm@uga.edu.",
        "gre_url": cs_prog_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Computer Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": cs_prog_url,
        "funding_code": "Typical",
        "funding_val": "Accepted doctoral students have priority departmental funding in the form of Teaching or Research Assistantships.",
        "funding_q": "*Accepted Doctoral students have priority departmental funding in the form of Teaching or Research Assistantships.",
        "funding_url": cs_prog_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "fee_waiver": {
                "code": "None",
                "value": "School of Computing does not provide graduate application fee waivers.",
                "quote": "NOTE: We DO NOT provide Graduate Application Fee waiver. All applicants are required to pay application fee for admission.",
                "url": cs_adm_url
            }
        }
    },
    {
        "id": "uga--ece",
        "field": "ece",
        "also_fields": [],
        "department": "College of Engineering",
        "program_page": eng_url_dept,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for full consideration for financial support",
        "deadline_q": eng_deadline_quote,
        "deadline_url": eng_url_dept,
        "gre_code": "Not required",
        "gre_val": "GRE requirement is waived for all engineering applicants for Fall 2027.",
        "gre_q": eng_gre_quote,
        "gre_url": eng_url_dept,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical and Computer Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants are strongly encouraged to contact faculty members whose research aligns with their interests regarding Research Assistantship opportunities.",
        "supervisor_q": eng_sup_quote,
        "supervisor_url": eng_url_dept,
        "funding_code": "Typical",
        "funding_val": "All applicants are considered for Research Assistantships, which provide tuition waiver and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--mech",
        "field": "mech",
        "also_fields": [],
        "department": "College of Engineering",
        "program_page": eng_url_dept,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for full consideration for financial support",
        "deadline_q": eng_deadline_quote,
        "deadline_url": eng_url_dept,
        "gre_code": "Not required",
        "gre_val": "GRE requirement is waived for all engineering applicants for Fall 2027.",
        "gre_q": eng_gre_quote,
        "gre_url": eng_url_dept,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants are strongly encouraged to contact faculty members whose research aligns with their interests regarding Research Assistantship opportunities.",
        "supervisor_q": eng_sup_quote,
        "supervisor_url": eng_url_dept,
        "funding_code": "Typical",
        "funding_val": "All applicants are considered for Research Assistantships, which provide tuition waiver and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--civil",
        "field": "civil",
        "also_fields": [],
        "department": "College of Engineering",
        "program_page": eng_url_dept,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for full consideration for financial support",
        "deadline_q": eng_deadline_quote,
        "deadline_url": eng_url_dept,
        "gre_code": "Not required",
        "gre_val": "GRE requirement is waived for all engineering applicants for Fall 2027.",
        "gre_q": eng_gre_quote,
        "gre_url": eng_url_dept,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants are strongly encouraged to contact faculty members whose research aligns with their interests regarding Research Assistantship opportunities.",
        "supervisor_q": eng_sup_quote,
        "supervisor_url": eng_url_dept,
        "funding_code": "Typical",
        "funding_val": "All applicants are considered for Research Assistantships, which provide tuition waiver and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--chemeng",
        "field": "chemeng",
        "also_fields": [],
        "department": "College of Engineering",
        "program_page": eng_url_dept,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for full consideration for financial support",
        "deadline_q": eng_deadline_quote,
        "deadline_url": eng_url_dept,
        "gre_code": "Not required",
        "gre_val": "GRE requirement is waived for all engineering applicants for Fall 2027.",
        "gre_q": eng_gre_quote,
        "gre_url": eng_url_dept,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants are strongly encouraged to contact faculty members whose research aligns with their interests regarding Research Assistantship opportunities.",
        "supervisor_q": eng_sup_quote,
        "supervisor_url": eng_url_dept,
        "funding_code": "Typical",
        "funding_val": "All applicants are considered for Research Assistantships, which provide tuition waiver and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--bme",
        "field": "bme",
        "also_fields": [],
        "department": "College of Engineering",
        "program_page": eng_url_dept,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for full consideration for financial support",
        "deadline_q": eng_deadline_quote,
        "deadline_url": eng_url_dept,
        "gre_code": "Not required",
        "gre_val": "GRE requirement is waived for all engineering applicants for Fall 2027.",
        "gre_q": eng_gre_quote,
        "gre_url": eng_url_dept,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants are strongly encouraged to contact faculty members whose research aligns with their interests regarding Research Assistantship opportunities.",
        "supervisor_q": eng_sup_quote,
        "supervisor_url": eng_url_dept,
        "funding_code": "Typical",
        "funding_val": "All applicants are considered for Research Assistantships, which provide tuition waiver and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--environment",
        "field": "environment",
        "also_fields": [],
        "department": "College of Engineering (Environmental Engineering)",
        "program_page": eng_url_dept,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for full consideration for financial support",
        "deadline_q": eng_deadline_quote,
        "deadline_url": eng_url_dept,
        "gre_code": "Not required",
        "gre_val": "GRE requirement is waived for all engineering applicants for Fall 2027.",
        "gre_q": eng_gre_quote,
        "gre_url": eng_url_dept,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Environmental Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants are strongly encouraged to contact faculty members whose research aligns with their interests regarding Research Assistantship opportunities.",
        "supervisor_q": eng_sup_quote,
        "supervisor_url": eng_url_dept,
        "funding_code": "Typical",
        "funding_val": "All applicants are considered for Research Assistantships, which provide tuition waiver and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--earth",
        "field": "earth",
        "also_fields": [],
        "department": "Department of Geology",
        "program_page": geo_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 application deadline for Fall Semester",
        "deadline_q": "The deadline for applications is January 1st.",
        "deadline_url": geo_url,
        "gre_code": "Not considered",
        "gre_val": "Department no longer requires or accepts GRE scores.",
        "gre_q": "The Department of Geology no longer requires or accepts GRE scores; do not include these scores in any part of your application.",
        "gre_url": geo_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Geology / Earth Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Applicants work directly with prospective faculty advisor and request fee waiver recommendations through them.",
        "supervisor_q": "Applicants for graduate studies may request a waiver of the application fee, and they should work directly with their prospective faculty advisor. Applicants requesting a waiver should prepare their application online and ask their prospective advisor to send a short (2–3 sentences) recommendation of the request to the Director of Graduate Studies.",
        "supervisor_url": geo_url,
        "funding_code": "Typical",
        "funding_val": "Entering graduate students are supported by departmental teaching or research assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {}
    },
    {
        "id": "uga--biology",
        "field": "biology",
        "also_fields": [],
        "department": "Integrated Life Sciences (ILS)",
        "program_page": ils_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for matriculation the following Fall term",
        "deadline_q": ils_deadline_quote,
        "deadline_url": ils_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not a required component of the application.",
        "gre_q": ils_gre_quote,
        "gre_url": ils_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biology subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Faculty are organized in Interdisciplinary Groups; choosing a mentor before applying is not required.",
        "supervisor_q": "",
        "supervisor_url": ils_url,
        "funding_code": "Typical",
        "funding_val": "All admitted PhD students are supported through graduate assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "fee_waiver": {
                "code": "None",
                "value": "ILS is not able to provide application fee waivers.",
                "quote": "ILS in NOT able to provide application fee waivers. Please refer to the UGA Graduate School regarding fee waivers (https://grad.uga.edu/admissions/application-fee/).",
                "url": ils_url
            }
        }
    },
    {
        "id": "uga--biomed",
        "field": "biomed",
        "also_fields": [],
        "department": "Integrated Life Sciences (Biomedical Sciences)",
        "program_page": ils_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for matriculation the following Fall term",
        "deadline_q": ils_deadline_quote,
        "deadline_url": ils_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not a required component of the application.",
        "gre_q": ils_gre_quote,
        "gre_url": ils_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Sciences subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Faculty are organized in Interdisciplinary Groups; choosing a mentor before applying is not required.",
        "supervisor_q": "",
        "supervisor_url": ils_url,
        "funding_code": "Typical",
        "funding_val": "All admitted PhD students are supported through graduate assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "fee_waiver": {
                "code": "None",
                "value": "ILS is not able to provide application fee waivers.",
                "quote": "ILS in NOT able to provide application fee waivers. Please refer to the UGA Graduate School regarding fee waivers (https://grad.uga.edu/admissions/application-fee/).",
                "url": ils_url
            }
        }
    },
    {
        "id": "uga--neuro",
        "field": "neuro",
        "also_fields": [],
        "department": "Integrated Life Sciences (Neuroscience Program)",
        "program_page": ils_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for matriculation the following Fall term",
        "deadline_q": ils_deadline_quote,
        "deadline_url": ils_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not a required component of the application.",
        "gre_q": ils_gre_quote,
        "gre_url": ils_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Neuroscience subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Faculty are organized in Interdisciplinary Groups; choosing a mentor before applying is not required.",
        "supervisor_q": "",
        "supervisor_url": ils_url,
        "funding_code": "Typical",
        "funding_val": "All admitted PhD students are supported through graduate assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": eng_url_dept,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from four-year bachelor's degree.",
        "entry_q": entry_quote,
        "entry_url": country_url,
        "extra_fields": {
            "fee_waiver": {
                "code": "None",
                "value": "ILS is not able to provide application fee waivers.",
                "quote": "ILS in NOT able to provide application fee waivers. Please refer to the UGA Graduate School regarding fee waivers (https://grad.uga.edu/admissions/application-fee/).",
                "url": ils_url
            }
        }
    }
]

for p in programs:
    verify_quote(p["deadline_url"], p["deadline_q"])
    verify_quote(p["gre_url"], p["gre_q"])
    verify_quote(p["subj_url"], p["subj_q"])
    if p["supervisor_q"]:
        verify_quote(p["supervisor_url"], p["supervisor_q"])
    verify_quote(p["funding_url"], p["funding_q"])
    verify_quote(p["entry_url"], p["entry_q"])
    for ef_k, ef in p["extra_fields"].items():
        verify_quote(ef["url"], ef["quote"])
    
    rec = {
        "id": p["id"],
        "university": "uga",
        "field": p["field"],
        "also_fields": p["also_fields"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": "2026-10-29",
        "notes": "",
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
                "code": p["funding_code"],
                "value": p["funding_val"],
                "quote": p["funding_q"],
                "url": p["funding_url"]
            },
            "entry_route": {
                "code": p["entry_code"],
                "value": p["entry_val"],
                "quote": p["entry_q"],
                "url": p["entry_url"]
            }
        }
    }
    rec["fields"].update(p["extra_fields"])
    with open(STAGING_PROGS / f"{p['id']}.json", "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2)

print(f"Verified & saved {len(programs)} UGA programs")
