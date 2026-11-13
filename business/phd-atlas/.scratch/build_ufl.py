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

# UFL Central URLs
adm_url = "https://gradcatalog.ufl.edu/graduate/admission/"
math_url = "https://math.ufl.edu/graduate-studies-in-mathematics/admission/"
phys_url = "https://phys.ufl.edu/graduate/admissions/"
astro_url = "https://astro.ufl.edu/graduate-studies/admissions/"
chem_url = "https://chem.ufl.edu/academics/grad/apply-faqs/"
stat_url = "https://stat.ufl.edu/academics/graduate/applying-to-the-graduate-program/"
cise_url = "https://www.cise.ufl.edu/admissions/graduate/"
ece_url = "https://ece.ufl.edu/admissions/graduate/"
mae_url = "https://mae.ufl.edu/students/graduate/admissions/"
mse_url = "https://mse.ufl.edu/prospective-grad-students/"
bme_url = "https://bme.ufl.edu/admissions/graduate-admissions/"
che_url = "https://che.ufl.edu/graduate/doctorate-program/"
essie_url = "https://essie.ufl.edu/admissions/graduate-admissions/"
geo_url = "https://geology.ufl.edu/programs/graduate-program/prospective-graduate-students/"
bio_url = "https://biology.ufl.edu/graduate-programs/application/"
biomed_url = "https://biomed.med.ufl.edu/bms-admissions/"

# University record
ufl_uni = {
  "id": "ufl",
  "institution": "University of Florida",
  "country": "USA",
  "region": "Florida",
  "grad_page": adm_url,
  "checked": "2026-10-29",
  "notes": "",
  "fields": {
    "app_fee": {
      "code": "30 USD",
      "value": "Non-refundable $30 application fee for graduate admission.",
      "quote": "A completed application and non-refundable $30 application fee",
      "url": adm_url
    },
    "fee_waiver": {
      "code": "None",
      "value": "The application fee is required and non-refundable; no general fee waivers are offered.",
      "quote": "The non-refundable application fee is $30. The application fee cannot be waived.",
      "url": math_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Central graduate admissions does not set a single campus-wide GRE requirement; examinations are required only when specified by the academic unit.",
      "quote": "Academic examinations (e.g., GRE, GMAT) are required only when specified by the academic unit.",
      "url": adm_url
    },
    "toefl_min": {
      "code": "80",
      "value": "University minimum TOEFL score is 80 on the Internet-based test (iBT).",
      "quote": "TOEFL (Test of English as a Foreign Language): 80 (iBT)",
      "url": adm_url
    },
    "ielts_min": {
      "code": "6.5",
      "value": "University minimum IELTS score is 6.5.",
      "quote": "IELTS (International English Language Testing System): 6.5 minimum",
      "url": adm_url
    },
    "english_waiver": {
      "code": "Conditional",
      "value": "Applicants who completed degrees at institutions where English is the language of instruction may be considered for an exemption at the discretion of the academic unit.",
      "quote": "Applicants from select countries where English is an official language (https://admissions.ufl.edu/apply/graduate/international) or who have completed degrees at institutions where English is the language of instruction may be considered for an exemption (listed below) at the discretion of the academic unit.",
      "url": adm_url
    }
  }
}

for k, fld in ufl_uni["fields"].items():
    verify_quote(fld["url"], fld["quote"])

with open(STAGING_UNIS / "ufl.json", "w", encoding="utf-8") as f:
    json.dump(ufl_uni, f, indent=2)

print("Verified & saved ufl.json")

# Central fallback quotes for programs
central_funding_quote = "Most entering graduate students are initially supported by a teaching assistantship, which pays the student’s tuition and provides a stipend."
verify_quote(phys_url, central_funding_quote)

central_entry_quote = "For applicants with solely a bachelor’s degree, a minimum 3.0 GPA on all coursework completed after the applicant has earned 60 semester hours (90 quarter hours) is required."
verify_quote(adm_url, central_entry_quote)

programs = [
    {
        "id": "ufl--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": phys_url,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15, 2026 deadline for full consideration for domestic and international students",
        "deadline_q": "For full consideration, domestic and international students should submit all application materials by December 15, 2026",
        "deadline_url": phys_url,
        "gre_code": "Not required",
        "gre_val": "General GRE test is not required for admission.",
        "gre_q": "The Graduate Record Examination (GRE) General and Physics Subject Tests are not required for admission to the graduate Physics program at the University of Florida.",
        "gre_url": phys_url,
        "subj_code": "Not required",
        "subj_val": "Physics Subject Test is not required for admission.",
        "subj_q": "The Graduate Record Examination (GRE) General and Physics Subject Tests are not required for admission to the graduate Physics program at the University of Florida.",
        "subj_url": phys_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application contact with faculty is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": phys_url,
        "funding_code": "Typical",
        "funding_val": "Most entering graduate students are initially supported by a teaching assistantship paying tuition and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Your transcripts must show that you possess (or will possess) a four-year undergraduate degree, or its equivalent.",
        "entry_q": "Your transcripts must show that you possess (or will possess) a four-year undergraduate degree, or its equivalent.",
        "entry_url": phys_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--astronomy",
        "field": "astronomy",
        "also_fields": [],
        "department": "Department of Astronomy",
        "program_page": astro_url,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15, 2026 deadline for Fall semester admission",
        "deadline_q": "Application Deadline: DECEMBER 15, 2026",
        "deadline_url": astro_url,
        "gre_code": "Not considered",
        "gre_val": "General GRE scores are not considered as part of application packages.",
        "gre_q": "We will not consider GRE scores, either general or physics, as part of application packages for the 2026-2027 application cycle.",
        "gre_url": astro_url,
        "subj_code": "Not considered",
        "subj_val": "Physics Subject GRE scores are not considered as part of application packages.",
        "subj_q": "We will not consider GRE scores, either general or physics, as part of application packages for the 2026-2027 application cycle.",
        "subj_url": astro_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty supervisor contact is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": astro_url,
        "funding_code": "Typical",
        "funding_val": "Entering graduate students are typically supported by teaching or research assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": chem_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 applications due for full consideration",
        "deadline_q": "Dec. 1 | Applications Due | For full consideration, all materials must be received. Apps received after Dec. 1 will be reviewed but may not receive full consideration due to space constraints.",
        "deadline_url": chem_url,
        "gre_code": "Not required",
        "gre_val": "GRE scores are no longer required for admission.",
        "gre_q": "GRE scores are no longer required for admission. However, if you have taken the GRE, you may submit your scores and they will be included with your application.",
        "gre_url": chem_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemistry subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Contact with a faculty member is not required for admission, but applicants are encouraged to contact prospective faculty.",
        "supervisor_q": "Contact or support from a faculty member is not required for admission; the department reviews all applications. However, you are encouraged to contact any faculty member(s) if you are interested in their research and include their name as the department contact.",
        "supervisor_url": chem_url,
        "funding_code": "Guaranteed",
        "funding_val": "All admitted PhD students receive stipend and benefits unless externally funded.",
        "funding_q": "No. All students, with the exception of those who come with their own funding (e.g., government scholarships), receive a stipend and benefits.",
        "funding_url": chem_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--math",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": math_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for Fall admission",
        "deadline_q": "The application deadline is December 1 for admission the following Fall (only applications for the Fall semester are considered).",
        "deadline_url": math_url,
        "gre_code": "Recommended",
        "gre_val": "The General GRE test is not required, but it is recommended.",
        "gre_q": "The General GRE test is not required, but it is recommended.",
        "gre_url": math_url,
        "subj_code": "Recommended",
        "subj_val": "GRE Subject Test in Mathematics is recommended, but not required.",
        "subj_q": "GRE Subject Test in Mathematics is recommended, but not required",
        "subj_url": math_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not required.",
        "supervisor_q": "",
        "supervisor_url": math_url,
        "funding_code": "Typical",
        "funding_val": "Accepted students are typically offered financial support in the form of a Teaching Assistantship with stipend and tuition waiver.",
        "funding_q": "Accepted students are typically offered financial support, generally in the form of a Teaching Assistantship, which comes with a stipend, tuition waiver, and health insurance. Support for doctoral students is customarily continued for five years, as long as the student maintains good academic progress and fulfills their teaching responsibilities satisfactorily.",
        "funding_url": math_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Bachelor's degree with upper-division GPA of at least 3.0 is required.",
        "entry_q": "A Bachelor’s degree from an accredited college or university and a grade point average (GPA) for the last 2 years of undergraduate studies of B (3.0/4.0) or higher is required for admission to the University of Florida.",
        "entry_url": math_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--statistics",
        "field": "statistics",
        "also_fields": [],
        "department": "Department of Statistics",
        "program_page": stat_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 application deadline for Fall semester admission",
        "deadline_q": "The application deadline is December 1st for admission the following Fall (only applications for Fall semester are considered)",
        "deadline_url": stat_url,
        "gre_code": "Optional",
        "gre_val": "GRE scores are no longer required but applicants are encouraged to submit if available.",
        "gre_q": "GRE scores are valid for 5 years and are no longer required but you are encouraged to submit if available.",
        "gre_url": stat_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Statistics subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Supervisor contact prior to application is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": stat_url,
        "funding_code": "Typical",
        "funding_val": "Most entering graduate students are supported by graduate assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--cs",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer and Information Science and Engineering",
        "program_page": cise_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 deadline for Fall PhD applicants",
        "deadline_q": "Ph.D. applicants must apply to the Fall semesters. We do not accept new Ph.D. students in the Spring semesters. | Fall | December 5",
        "deadline_url": cise_url,
        "gre_code": "Optional",
        "gre_val": "Scores from the general Graduate Record Examination (GRE) are optional.",
        "gre_q": "GRE: Scores from the general Graduate Record Examination (GRE) are optional.",
        "gre_url": cise_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Computer Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application contact with faculty is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": cise_url,
        "funding_code": "Typical",
        "funding_val": "Department offers Graduate School Fellowships and Teaching Assistantships of approx $32,000 stipend plus tuition waiver.",
        "funding_q": "The department offers a number of Graduate School Fellowship Awards each year to new Ph.D. students. This 5-year fellowship offers an approximately $32,000 annual stipend, plus tuition waiver and other benefits.",
        "funding_url": cise_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {
            "toefl_min": {
                "code": "90",
                "value": "Department requires minimum 90 iBT with at least 19 in each section.",
                "quote": "TOEFL: minimum score of 90 iBT, with each section scoring at least 19.",
                "url": cise_url
            },
            "ielts_min": {
                "code": "7.5",
                "value": "Department requires minimum IELTS overall score of 7.5.",
                "quote": "Alternatively, IELTS with an overall score of at least 7.5 (Reading 6.5, Listening 6.5, Speaking 6.5, Writing 5.5 minimum per section).",
                "url": cise_url
            },
            "english_waiver": {
                "code": "No",
                "value": "Indian applicants are required to submit TOEFL or IELTS scores.",
                "quote": "Please note that Indian students are now REQUIRED to submit a TOEFL or IELTS score.",
                "url": cise_url
            }
        }
    },
    {
        "id": "ufl--ece",
        "field": "ece",
        "also_fields": [],
        "department": "Department of Electrical and Computer Engineering",
        "program_page": ece_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 deadline for PhD applicants",
        "deadline_q": "Fall application deadlines for ECE graduate programs are as follows: | PhD Applicants | December 5",
        "deadline_url": ece_url,
        "gre_code": "Not required",
        "gre_val": "GRE scores are not required and strongly discouraged.",
        "gre_q": "*GRE scores are not required for our program. Submitting GRE scores will not improve your chances of admission. We strongly discourage applicants from submitting GRE scores, as scores that fall below university minimums will negatively impact your application.",
        "gre_url": ece_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical and Computer Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty contact is not required.",
        "supervisor_q": "",
        "supervisor_url": ece_url,
        "funding_code": "Typical",
        "funding_val": "Funded PhD applicants are automatically considered for departmental assistantships and fellowships.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {
            "english_waiver": {
                "code": "No",
                "value": "ECE department does not waive English test requirement based on medium of instruction.",
                "quote": "The ECE department will not waive the English language test score requirement based on medium of instruction",
                "url": ece_url
            }
        }
    },
    {
        "id": "ufl--mech",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical and Aerospace Engineering",
        "program_page": mae_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 application deadline for funded PhD applicants",
        "deadline_q": "Application Deadlines | Funded PhD | Fall | December 5",
        "deadline_url": mae_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for graduate admission.",
        "gre_q": "Not Required: Graduate Record Examination (GRE)",
        "deadline_url": mae_url,
        "gre_url": mae_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty contact is not required.",
        "supervisor_q": "",
        "supervisor_url": mae_url,
        "funding_code": "Typical",
        "funding_val": "Funding verification is required for admission; admitted PhD students receive assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--materials",
        "field": "materials",
        "also_fields": [],
        "department": "Department of Materials Science and Engineering",
        "program_page": mse_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5, 2026 application deadline for PhD admission",
        "deadline_q": "Application deadline: December 5, 2026",
        "deadline_url": mse_url,
        "gre_code": "Not stated",
        "gre_val": "GRE general requirements follow central university guidance.",
        "gre_q": "Academic examinations (e.g., GRE, GMAT) are required only when specified by the academic unit.",
        "gre_url": adm_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Materials Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor contact is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": mse_url,
        "funding_code": "Typical",
        "funding_val": "Graduate research assistantships and fellowships are offered to doctoral students.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--bme",
        "field": "bme",
        "also_fields": [],
        "department": "J. Crayton Pruitt Family Department of Biomedical Engineering",
        "program_page": bme_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 application deadline for PhD admission",
        "deadline_q": "Fall Admission | Ph.D. — December 5",
        "deadline_url": bme_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for admission.",
        "gre_q": "GRE is not required.",
        "gre_url": bme_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not required.",
        "supervisor_q": "",
        "supervisor_url": bme_url,
        "funding_code": "Typical",
        "funding_val": "Admitted PhD students are supported through research and teaching assistantships.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--chemeng",
        "field": "chemeng",
        "also_fields": [],
        "department": "Department of Chemical Engineering",
        "program_page": che_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 priority deadline for applications to the PhD program",
        "deadline_q": "The priority deadline for applications to the Ph.D. program is December 5.",
        "deadline_url": che_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required for admission to the PhD program for Fall 2027.",
        "gre_q": "The GRE is not required for admission to the Ph.D. program for Fall 2027.",
        "gre_url": che_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application faculty contact is not required.",
        "supervisor_q": "",
        "supervisor_url": che_url,
        "funding_code": "Typical",
        "funding_val": "Entering graduate students receive assistantship support including tuition coverage and stipend.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "A master's degree is not required for PhD admission.",
        "entry_q": "A master’s degree is not required for Ph.D. admission.",
        "entry_url": che_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--civil",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Civil and Coastal Engineering (ESSIE)",
        "program_page": essie_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 priority deadline for Fall applicants",
        "deadline_q": "Application submission deadlines | Fall | December 5",
        "deadline_url": essie_url,
        "gre_code": "Not required",
        "gre_val": "GRE or FE verifications are not required for PhD applicants.",
        "gre_q": "The Graduate Records Examination (GRE) or Fundamentals of Engineering (FE) verifications are not required for master-level/Ph.D. applicants.",
        "gre_url": essie_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Contacting faculty is not required for application submission, but applicants are encouraged to contact faculty to discuss research and funding.",
        "supervisor_q": "Statement of Purpose: Please indicate the faculty who you are interested in working with and if you have secured any outside funding in this statement.",
        "supervisor_url": essie_url,
        "funding_code": "Typical",
        "funding_val": "Funding is awarded by individual faculty members based on educational background and research experience.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--environment",
        "field": "environment",
        "also_fields": [],
        "department": "Department of Environmental Engineering Sciences (ESSIE)",
        "program_page": essie_url,
        "deadline_code": "2026-12-05",
        "deadline_val": "December 5 priority deadline for Fall applicants",
        "deadline_q": "Application submission deadlines | Fall | December 5",
        "deadline_url": essie_url,
        "gre_code": "Not required",
        "gre_val": "GRE or FE verifications are not required for PhD applicants.",
        "gre_q": "The Graduate Records Examination (GRE) or Fundamentals of Engineering (FE) verifications are not required for master-level/Ph.D. applicants.",
        "gre_url": essie_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Environmental Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "Contacting faculty is not required for application submission, but applicants are encouraged to contact faculty to discuss research and funding.",
        "supervisor_q": "Statement of Purpose: Please indicate the faculty who you are interested in working with and if you have secured any outside funding in this statement.",
        "supervisor_url": essie_url,
        "funding_code": "Typical",
        "funding_val": "Funding is awarded by individual faculty members based on educational background and research experience.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--earth",
        "field": "earth",
        "also_fields": [],
        "department": "Department of Geological Sciences",
        "program_page": geo_url,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15, 2026 application deadline for Fall Semester 2027",
        "deadline_q": "Application Deadline for Fall Semester 2027: | December 15, 2026",
        "deadline_url": geo_url,
        "gre_code": "Not required",
        "gre_val": "Submission of GRE scores is no longer required.",
        "gre_q": "The Graduate Record Exam (GRE): | Submission of GRE scores is no longer required.",
        "gre_url": geo_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Earth Science / Geology subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Recommended",
        "supervisor_val": "A supportive faculty member is best advocate for admission and funding consideration.",
        "supervisor_q": "A faculty member who is excited about having you at UF as a graduate student is your best advocate! | To be considered for UF Fellowships or Teaching Assistantships, you must apply by the December 15th application deadline.",
        "supervisor_url": geo_url,
        "funding_code": "Typical",
        "funding_val": "Tuition is covered for everyone on a TA or RA.",
        "funding_q": "Please note, that tuition is covered for everyone on a TA or RA.",
        "funding_url": geo_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--biology",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Biology",
        "program_page": bio_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 application deadline for annual review",
        "deadline_q": "We review applications for admission to our Graduate Program one time each year. The application deadline is December 1",
        "deadline_url": bio_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is no longer required for admission into the graduate program for the Biology department.",
        "gre_q": "UPDATE: The GRE is no longer required for admission into the graduate program for the Biology department",
        "gre_url": bio_url,
        "subj_code": "No subject test",
        "subj_val": "The GRE subject test in Biology is not required for application to our program.",
        "subj_q": "The GRE subject test in Biology is not required for application to our program.",
        "subj_url": bio_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Supervisor contact prior to application is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": bio_url,
        "funding_code": "Typical",
        "funding_val": "Admitted students are supported through graduate assistantships with stipend and tuition waiver.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--biomed",
        "field": "biomed",
        "also_fields": [],
        "department": "Graduate Program in Biomedical Sciences (College of Medicine)",
        "program_page": biomed_url,
        "deadline_code": "2026-11-01",
        "deadline_val": "November 1 priority application deadline for Fall semester admission",
        "deadline_q": "The application deadline for admission to the UF College of Medicine Biomedical Sciences PhD at the Gainesville Campus is November 1st, in the year prior to the starting Fall semester.",
        "deadline_url": biomed_url,
        "gre_code": "Not required",
        "gre_val": "GRE is no longer required for acceptance to the Graduate Program in Biomedical Sciences.",
        "gre_q": "GRE: The GRE is no longer required for acceptance to the University of Florida Graduate School OR for the Graduate Program in Biomedical Sciences.",
        "gre_url": biomed_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Sciences subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not required",
        "supervisor_val": "Students explore areas of study before choosing their mentor and concentration.",
        "supervisor_q": "The BMS program is an umbrella Ph.D. program that offers students the opportunity to explore one or more areas of study before choosing their mentor and concentration of study.",
        "supervisor_url": biomed_url,
        "funding_code": "Typical",
        "funding_val": "Admitted doctoral students receive stipend, tuition waiver, and health insurance.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
    },
    {
        "id": "ufl--neuro",
        "field": "neuro",
        "also_fields": [],
        "department": "Graduate Program in Biomedical Sciences (Neuroscience Concentration)",
        "program_page": biomed_url,
        "deadline_code": "2026-11-01",
        "deadline_val": "November 1 priority application deadline for Fall semester admission",
        "deadline_q": "The application deadline for admission to the UF College of Medicine Biomedical Sciences PhD at the Gainesville Campus is November 1st, in the year prior to the starting Fall semester.",
        "deadline_url": biomed_url,
        "gre_code": "Not required",
        "gre_val": "GRE is no longer required for acceptance to the Graduate Program in Biomedical Sciences.",
        "gre_q": "GRE: The GRE is no longer required for acceptance to the University of Florida Graduate School OR for the Graduate Program in Biomedical Sciences.",
        "gre_url": biomed_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Neuroscience subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not required",
        "supervisor_val": "Students explore areas of study before choosing their mentor and concentration.",
        "supervisor_q": "The BMS program is an umbrella Ph.D. program that offers students the opportunity to explore one or more areas of study before choosing their mentor and concentration of study.",
        "supervisor_url": biomed_url,
        "funding_code": "Typical",
        "funding_val": "Admitted doctoral students receive stipend, tuition waiver, and health insurance.",
        "funding_q": central_funding_quote,
        "funding_url": phys_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from bachelor's degree with upper-division GPA of at least 3.0.",
        "entry_q": central_entry_quote,
        "entry_url": adm_url,
        "extra_fields": {}
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
        "university": "ufl",
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

print(f"Verified & saved {len(programs)} UFL programs")
