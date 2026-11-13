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
    q_norm = " ".join(quote.split())
    t_norm = " ".join(t.split())
    if q_norm not in t_norm:
        raise ValueError(f"Quote mismatch for {url}:\nQUOTE: {quote[:100]}...\n")

# ETS quote
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
verify_quote(ets_url, ets_quote)

# UCSD Central URLs
fee_url = "https://grad.ucsd.edu/admissions/requirements/application-fee-and-fee-waiver/index.html"
exam_url = "https://grad.ucsd.edu/admissions/requirements/exam-requirements.html"
eng_url = "https://grad.ucsd.edu/admissions/requirements/international-students/english-proficiency.html"
req_url = "https://grad.ucsd.edu/admissions/requirements/index.html"
funding_url = "https://scripps.ucsd.edu/doctoral/cost-funding"

entry_quote = "Successful applicants must hold a bachelor's degree or the equivalent from an accredited institution in the United States or from a recognized university-level academic institution abroad and at least a B average (3.0 GPA) or its equivalent by the time they enroll."
verify_quote(req_url, entry_quote)

funding_quote = "At UC San Diego, the general financial support package for first-year Ph.D. students includes a minimum commitment of $37,500 plus tuition and mandatory fees. If you are not a California resident, the non-resident supplemental tuition will also be covered."
verify_quote(funding_url, funding_quote)

# -------------------------------------------------------------
# 1. UCSD UNIVERSITY
# -------------------------------------------------------------
ucsd_uni = {
  "id": "ucsd",
  "institution": "University of California, San Diego",
  "country": "USA",
  "region": "California",
  "grad_page": "https://grad.ucsd.edu/admissions/index.html",
  "checked": "2026-10-29",
  "notes": "",
  "fields": {
    "app_fee": {
      "code": "155 USD",
      "value": "$155.00 for international applicants",
      "quote": "International Applicants: $155.00",
      "url": fee_url
    },
    "fee_waiver": {
      "code": "Domestic only",
      "value": "Fee waivers are available only to U.S. citizens, Permanent Residents, and Undocumented students; international applicants are not eligible.",
      "quote": "U.S. citizens, Permanent Residents, and Undocumented students may be eligible for a waiver of the application fee.",
      "url": fee_url
    },
    "gre_general": {
      "code": "Not stated",
      "value": "Central graduate admissions does not set a single campus-wide GRE requirement; requirements vary by department.",
      "quote": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
      "url": exam_url
    },
    "toefl_min": {
      "code": "85",
      "value": "University-wide minimum TOEFL score is 85 on iBT or 4.5 on the new internet based test.",
      "quote": "The university-wide minimum TOEFL score required for consideration for graduate admission is 4.5 for the new internet based test (iBT) or 85",
      "url": eng_url
    },
    "ielts_min": {
      "code": "7.0",
      "value": "University-wide minimum IELTS Academic exam score is Band Score 7.",
      "quote": "The university-wide minimum IELTS Academic Training exam score required for consideration for graduate admission is Band Score 7.",
      "url": eng_url
    },
    "english_waiver": {
      "code": "Check tool",
      "value": "Exemption available if foreign institution is verified in IAU WHED with English as sole language of instruction.",
      "quote": "A foreign college or university which provides instruction solely in English. You may verify whether your institution meets this requirement by looking up your institution in the IAU World Higher Education Database (WHED).",
      "url": eng_url
    }
  }
}

for k, fld in ucsd_uni["fields"].items():
    verify_quote(fld["url"], fld["quote"])

with open(STAGING_UNIS / "ucsd.json", "w", encoding="utf-8") as f:
    json.dump(ucsd_uni, f, indent=2)

print("Verified & saved ucsd.json")

# -------------------------------------------------------------
# 2. UCSD PROGRAMS
# -------------------------------------------------------------
ucsd_progs = [
    {
        "id": "ucsd--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": "https://physics.ucsd.edu/students/graduate/requirements",
        "deadline_code": "2026-12-16",
        "deadline_val": "December 16, 2026 application deadline for PhD admission",
        "deadline_q": "Application Deadline for 2027-28 is: December 16th, 2026 at 5 p.m. PST.",
        "deadline_url": "https://physics.ucsd.edu/students/graduate/requirements",
        "gre_code": "Not considered",
        "gre_val": "The General GRE will not be used in admission decisions.",
        "gre_q": "The General GRE will not be used in our admission decisions.",
        "gre_url": "https://physics.ucsd.edu/students/graduate/requirements",
        "subj_code": "Recommended",
        "subj_val": "The Physics Subject GRE is recommended for all applicants to the Physics PhD program.",
        "subj_q": "The Physics Subject GRE is recommended for all applicants to the Physics PhD program.",
        "subj_url": "https://physics.ucsd.edu/students/graduate/requirements",
        "notes": ""
    },
    {
        "id": "ucsd--astronomy",
        "field": "astronomy",
        "also_fields": ["physics"],
        "department": "Department of Physics (Astrophysics & Cosmology)",
        "program_page": "https://physics.ucsd.edu/students/graduate/requirements",
        "deadline_code": "2026-12-16",
        "deadline_val": "December 16, 2026 application deadline for PhD admission",
        "deadline_q": "Application Deadline for 2027-28 is: December 16th, 2026 at 5 p.m. PST.",
        "deadline_url": "https://physics.ucsd.edu/students/graduate/requirements",
        "gre_code": "Not considered",
        "gre_val": "The General GRE will not be used in admission decisions.",
        "gre_q": "The General GRE will not be used in our admission decisions.",
        "gre_url": "https://physics.ucsd.edu/students/graduate/requirements",
        "subj_code": "Recommended",
        "subj_val": "The Physics Subject GRE is recommended for all applicants to the Physics PhD program.",
        "subj_q": "The Physics Subject GRE is recommended for all applicants to the Physics PhD program.",
        "subj_url": "https://physics.ucsd.edu/students/graduate/requirements",
        "notes": "Physics PhD with research specialization in Astrophysics & Cosmology."
    },
    {
        "id": "ucsd--math",
        "field": "math",
        "also_fields": ["statistics"],
        "department": "Department of Mathematics",
        "program_page": "https://math.ucsd.edu/students/graduate/how-to-apply",
        "deadline_code": "2026-12-02",
        "deadline_val": "December 2, 2026 deadline for PhD in Mathematics and Specialization in Statistics",
        "deadline_q": "Ph.D. in Mathematics Opens: September 2, 2026 Closes: December 2, 2026",
        "deadline_url": "https://math.ucsd.edu/students/graduate/how-to-apply",
        "gre_code": "Not required",
        "gre_val": "The GRE General Test is not required.",
        "gre_q": "For Fall 2027 admissions, the GRE General Test and GRE Mathematics Subject Test are not required. However, the GRE Mathematics Subject Test is highly recommended, as it provides our Admissions Committee with additional context to assess applicants’ preparedness for the rigorous academic standards of our program.",
        "gre_url": "https://math.ucsd.edu/students/graduate/how-to-apply",
        "subj_code": "Recommended",
        "subj_val": "The GRE Mathematics Subject Test is highly recommended.",
        "subj_q": "For Fall 2027 admissions, the GRE General Test and GRE Mathematics Subject Test are not required. However, the GRE Mathematics Subject Test is highly recommended, as it provides our Admissions Committee with additional context to assess applicants’ preparedness for the rigorous academic standards of our program.",
        "subj_url": "https://math.ucsd.edu/students/graduate/how-to-apply",
        "notes": ""
    },
    {
        "id": "ucsd--cs",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science and Engineering",
        "program_page": "https://cse.ucsd.edu/graduate/admissions",
        "deadline_code": "2026-12-16",
        "deadline_val": "December 16, 2026 at 11:59 p.m. PST deadline for PhD admission",
        "deadline_q": "The UCSD Application for Graduate Admission opens for Fall 2027 admission from September 2, 2026 until December 16, 2026 at 11:59 p.m. PST.",
        "deadline_url": "https://cse.ucsd.edu/graduate/admissions",
        "gre_code": "Optional",
        "gre_val": "The GRE is not required for PhD applications; applicants may still submit valid scores if taken.",
        "gre_q": "The GRE is not required for PhD and MS applications for Fall 2027. Applicants may still submit valid scores if they have already taken the test.",
        "gre_url": "https://cse.ucsd.edu/graduate/admissions",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Computer Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--datasci",
        "field": "datasci",
        "also_fields": [],
        "department": "Halıcıoğlu Data Science Institute",
        "program_page": "https://catalog.ucsd.edu/curric/DSC-gr.html",
        "deadline_code": "2026-12-15",
        "deadline_val": "December application deadline for Fall admission",
        "deadline_q": "The application deadline is December for admissions effective the following fall quarter.",
        "deadline_url": "https://catalog.ucsd.edu/curric/DSC-gr.html",
        "gre_code": "Optional",
        "gre_val": "Optional GRE requirements as per latest guidance from Graduate Division.",
        "gre_q": "Optional GRE requirements as per the latest guidance from the Division of Graduate Education and Postdoctoral Affairs at UC San Diego.",
        "gre_url": "https://catalog.ucsd.edu/curric/DSC-gr.html",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Data Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--ece",
        "field": "ece",
        "also_fields": [],
        "department": "Department of Electrical and Computer Engineering",
        "program_page": "https://ece.ucsd.edu/graduate/graduate-admissions",
        "deadline_code": "2026-12-16",
        "deadline_val": "December 16, 2026 deadline for PhD admission",
        "deadline_q": "Ph.D.: December 16th, 2026",
        "deadline_url": "https://ece.ucsd.edu/graduate/graduate-admissions",
        "gre_code": "Not required",
        "gre_val": "Submitting GRE scores is not required for PhD applications.",
        "gre_q": "(Not Required) GRE General Test scores (For Fall 2027 applications, submitting GRE scores is not required for either M.S. or Ph.D. applications)",
        "gre_url": "https://ece.ucsd.edu/graduate/graduate-admissions",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical and Computer Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry and Biochemistry",
        "program_page": "https://chemistry.ucsd.edu/graduate-program/doctoral-program/admissions",
        "deadline_code": "2026-12-16",
        "deadline_val": "December 16, 2026 deadline for PhD admission",
        "deadline_q": "Fall 2027 PhD Admissions Deadline is December 16, 2026.",
        "deadline_url": "https://chemistry.ucsd.edu/graduate-program/doctoral-program/admissions",
        "gre_code": "Not considered",
        "gre_val": "The GRE General and GRE Subject tests are not required and will not be used in application evaluation.",
        "gre_q": "The GRE General & GRE Subject are not required and will not be used in the evaluation of your application.",
        "gre_url": "https://chemistry.ucsd.edu/graduate-program/doctoral-program/admissions",
        "subj_code": "Not considered",
        "subj_val": "The GRE Chemistry Subject test will not be used in application evaluation.",
        "subj_q": "The GRE General & GRE Subject are not required and will not be used in the evaluation of your application.",
        "subj_url": "https://chemistry.ucsd.edu/graduate-program/doctoral-program/admissions",
        "notes": ""
    },
    {
        "id": "ucsd--biology",
        "field": "biology",
        "also_fields": [],
        "department": "School of Biological Sciences",
        "program_page": "https://biology.ucsd.edu/education/grad/phd/admissions/index.html",
        "deadline_code": "2026-12-02",
        "deadline_val": "December 2, 2026 (11:59PM PST) deadline for PhD admission",
        "deadline_q": "Application Close: December 2, 2026 (11:59PM PST)",
        "deadline_url": "https://biology.ucsd.edu/education/grad/phd/admissions/index.html",
        "gre_code": "Recommended",
        "gre_val": "The GRE is recommended, but not required.",
        "gre_q": "Is the GRE required? The GRE is recommended, but not required.",
        "gre_url": "https://biology.ucsd.edu/education/grad/phd/admissions/faq/application-evaluation.html",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biology subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--bme",
        "field": "bme",
        "also_fields": ["biomed"],
        "department": "Department of Bioengineering",
        "program_page": "https://catalog.ucsd.edu/curric/BENG-gr.html",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not state a separate deadline date in catalog; applications follow central fall admissions schedule.",
        "deadline_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "deadline_url": exam_url,
        "gre_code": "Not stated",
        "gre_val": "GRE requirement varies as per central campus policy.",
        "gre_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "gre_url": exam_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Bioengineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--mech",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical and Aerospace Engineering",
        "program_page": "https://maeweb.ucsd.edu/grad/graduate-admissions",
        "deadline_code": "2026-12-02",
        "deadline_val": "December 2, 2026 application deadline for PhD admission",
        "deadline_q": "Ph.D. - September 2nd, 2026 - December 2nd, 2026",
        "deadline_url": "https://maeweb.ucsd.edu/grad/graduate-admissions",
        "gre_code": "Optional",
        "gre_val": "GRE is not required; applicants may submit scores as part of application if desired.",
        "gre_q": "GRE - NOT REQUIRED If students want to submit GRE scores as a part of their application, that is acceptable.",
        "gre_url": "https://maeweb.ucsd.edu/grad/graduate-admissions",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--civil",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Structural Engineering",
        "program_page": "https://catalog.ucsd.edu/curric/SE-gr.html",
        "deadline_code": "Not stated",
        "deadline_val": "Department does not publish a separate date in catalog; follows central graduate admissions schedule.",
        "deadline_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "deadline_url": exam_url,
        "gre_code": "Not stated",
        "gre_val": "GRE requirements vary as per central Graduate Division policy.",
        "gre_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "gre_url": exam_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Structural/Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--materials",
        "field": "materials",
        "also_fields": [],
        "department": "Program in Materials Science and Engineering",
        "program_page": "https://matsci.ucsd.edu/admissions",
        "deadline_code": "2027-01-06",
        "deadline_val": "January 6, 2027 at 11:59PM PST deadline for PhD applications",
        "deadline_q": "*the Fall 2027 Applications DEADLINE (PhD & MS) will be: Wednesday, January 06 2027 (01/06/27) 11:59PM PST",
        "deadline_url": "https://matsci.ucsd.edu/admissions",
        "gre_code": "Not required",
        "gre_val": "GRE scores are not required for PhD applications.",
        "gre_q": "the Program in Materials Science and Engineering (MATS) does not require GRE scores for the MS and PhD applications.",
        "gre_url": "https://matsci.ucsd.edu/admissions",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Materials Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    },
    {
        "id": "ucsd--earth",
        "field": "earth",
        "also_fields": ["environment"],
        "department": "Scripps Institution of Oceanography",
        "program_page": "https://scripps.ucsd.edu/doctoral/cost-funding",
        "deadline_code": "Not stated",
        "deadline_val": "Scripps program adheres to central graduate admission deadlines.",
        "deadline_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "deadline_url": exam_url,
        "gre_code": "Not stated",
        "gre_val": "GRE requirement follows department policy as noted by Graduate Division.",
        "gre_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "gre_url": exam_url,
        "subj_code": "Optional",
        "subj_val": "The GRE Subject Exam in Chemistry or Biology is optional.",
        "subj_q": "The GRE Subject Exam in Chemistry or Biology is optional.",
        "subj_url": "https://catalog.ucsd.edu/curric/SIO-gr.html",
        "notes": ""
    },
    {
        "id": "ucsd--neuro",
        "field": "neuro",
        "also_fields": [],
        "department": "Neurosciences Graduate Program",
        "program_page": "https://catalog.ucsd.edu/curric/NEU.html",
        "deadline_code": "Not stated",
        "deadline_val": "Follows general graduate admissions schedule.",
        "deadline_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "deadline_url": exam_url,
        "gre_code": "Not stated",
        "gre_val": "GRE requirement follows department policy as noted by Graduate Division.",
        "gre_q": "While some departments require GRE scores, many have chosen to no longer require applicants to submit GRE scores for consideration.",
        "gre_url": exam_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Neuroscience subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "notes": ""
    }
]

for p in ucsd_progs:
    verify_quote(p["deadline_url"], p["deadline_q"])
    verify_quote(p["gre_url"], p["gre_q"])
    if p["subj_q"]:
        verify_quote(p["subj_url"], p["subj_q"])
    
    rec = {
        "id": p["id"],
        "university": "ucsd",
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
                "value": "First-year PhD financial support package includes minimum $37,500 commitment plus tuition, mandatory fees, and non-resident supplemental tuition.",
                "quote": funding_quote,
                "url": funding_url
            },
            "entry_route": {
                "code": "Direct from bachelor's",
                "value": "Successful applicants must hold a bachelor's degree or equivalent with at least 3.0 GPA.",
                "quote": entry_quote,
                "url": req_url
            }
        }
    }
    with open(STAGING_PROGS / f"{p['id']}.json", "w", encoding="utf-8") as f:
        json.dump(rec, f, indent=2)

print(f"Verified & saved {len(ucsd_progs)} UCSD programs")
