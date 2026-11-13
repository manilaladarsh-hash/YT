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

# Central pages
applying_url = "https://graduate.ucf.edu/applying-to-ucf/"
doctoral_reqs_url = "https://graduate.ucf.edu/application-deadlines-and-requirements/doctoral/2026/"
intl_url = "https://graduate.ucf.edu/international-applicants/"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
verify_quote(ets_url, ets_quote)

cs_deg_url = "https://www.ucf.edu/degree/computer-science-phd/"
physics_deg_url = "https://www.ucf.edu/degree/physics-phd/"

central_funding_quote = "Fall Priority Deadline: Applicants who plan to enroll full time in a degree program and who wish to be considered for university fellowships or assistantships should apply by January 15 (or earlier if your program has a deadline prior to January 15)."
verify_quote(doctoral_reqs_url, central_funding_quote)

central_entry_quote = "All applicants for graduate study at the University of Central Florida must hold a U.S. bachelor’s degree, or its equivalent, from an accredited or governmentally recognized institution of higher learning."
verify_quote(intl_url, central_entry_quote)

# University record
ucf_uni = {
    "id": "ucf",
    "institution": "University of Central Florida",
    "country": "USA",
    "region": "Florida",
    "grad_page": applying_url,
    "checked": "2026-10-29",
    "notes": "",
    "fields": {
        "app_fee": {
            "code": "30 USD",
            "value": "Application fee is $30 for each application submitted.",
            "quote": "Complete a graduate application online and submit the non-refundable $30 application fee.",
            "url": applying_url
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Application fee waivers are available for specific qualifying graduate programs/scholars; no hardship fee waivers are provided.",
            "quote": "An application fee waiver may be available for students applying to specific graduate programs. | The College of Graduate Studies does not provide hardship fee waivers.",
            "url": applying_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "The university does not set a campus-wide GRE requirement; requirements are set individually by each degree program.",
            "quote": "If the GRE or GMAT is required, the specific test will be explicitly stated in the “Admissions Requirements” section of the program.",
            "url": doctoral_reqs_url
        },
        "toefl_min": {
            "code": "80",
            "value": "Minimum university requirement is 80 on TOEFL iBT (or 4 on revised test). Certain programs require higher scores.",
            "quote": "Minimum UCF Requirement for TOEFL/IELTS/Duolingo | TOEFL iBT | 80 | NOTE: Certain graduate programs require higher TOEFL iBT, IELTS or DET scores. Review your program’s application requirements for minimum score requirements.",
            "url": intl_url
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum university requirement is 6.5 overall band.",
            "quote": "IELTS | 6.5 | Sent electronically via IELTS",
            "url": intl_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exemption is granted for applicants who earned a degree from an institution where English is the only official language of instruction.",
            "quote": "Those who have earned a degree equivalent to a U.S. Bachelor’s, Master’s, or Doctoral degree from a university where English is the only official language of instruction. | Applicants who meet the criteria will have this requirement waived once an application fee has been received and their application has been processed.",
            "url": intl_url
        }
    }
}

# Verify university fields
for k, f in ucf_uni["fields"].items():
    verify_quote(f["url"], f["quote"])

with open(STAGING_UNIS / "ucf.json", "w", encoding="utf-8") as out:
    json.dump(ucf_uni, out, indent=2, ensure_ascii=False)
print("Verified & saved ucf.json")

programs = [
    {
        "id": "ucf--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": physics_deg_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Physics PhD | Application Deadline | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Physics PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "Optional",
        "subj_val": "The Physics Subject Test of the GRE is optional.",
        "subj_q": "The Physics Subject Test of the GRE is optional",
        "subj_url": doctoral_reqs_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Applicants should identify research areas and faculty in their statement of goals; pre-application contact is not stated as required.",
        "supervisor_q": "Statement of goals. The final 1-2 paragraphs of each applicant’s personal statement should make explicitly clear which research areas and faculty they have interest in working with within our program.",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission for students with coursework generally required for a bachelor's degree in physics.",
        "entry_q": "Students entering the Physics graduate program with regular status are normally expected to have completed course work generally required for a bachelor's degree in physics, including classical mechanics, electricity and magnetism, thermal and statistical physics, and quantum mechanics.",
        "entry_url": physics_deg_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--astronomy",
        "field": "astronomy",
        "also_fields": ["earth"],
        "department": "Department of Physics",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Planetary and Space Sciences PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Planetary and Space Sciences PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Astronomy subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Expected coursework generally required for a bachelor's degree in physics, astronomy, geology, or closely related field.",
        "entry_q": "Students entering the Planetary & Space Sciences program with regular status are normally expected to have completed coursework generally required for a bachelor’s degree in a closely related science field such as physics, astronomy, geology, geophysics, atmospheric science",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Chemistry PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Chemistry PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemistry subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission with a Bachelor of Science degree in the Chemical Sciences or closely related field.",
        "entry_q": "A Bachelor of Science degree in the Chemical Sciences or a closely related field.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--materials",
        "field": "materials",
        "also_fields": [],
        "department": "Department of Materials Science and Engineering",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Materials Science and Engineering PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission into this program.",
        "gre_q": "The GRE is not required for admission into this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Materials subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Master’s and/or bachelor’s degree in Materials Science and Engineering or a closely related discipline.",
        "entry_q": "Master’s and/or bachelor’s degree in Materials Science and Engineering or a closely related discipline.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--math",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Mathematics PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Mathematics PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "Not stated",
        "subj_val": "GRE Mathematics Subject Test is not stated as required.",
        "subj_q": "",
        "subj_url": doctoral_reqs_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission with a Bachelor's degree in a related field.",
        "entry_q": "Bachelor’s degree in related field.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--statistics",
        "field": "statistics",
        "also_fields": [],
        "department": "Department of Statistics and Data Science",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Big Data Analytics PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Required",
        "gre_val": "Official, competitive GRE score taken within the last five years is required.",
        "gre_q": "Big Data Analytics PhD | Official, competitive GRE score taken within the last five years.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Statistics subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission with a Bachelor's degree or equivalent in statistics, data analytics or related field.",
        "entry_q": "A Bachelor’s degree or its equivalent in statistics, data analytics or a related field from an accredited U.S. institution recognized by UCF or its equivalent from a foreign institution.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--datasci",
        "field": "datasci",
        "also_fields": [],
        "department": "Department of Statistics and Data Science",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Big Data Analytics PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Required",
        "gre_val": "Official, competitive GRE score taken within the last five years is required.",
        "gre_q": "Big Data Analytics PhD | Official, competitive GRE score taken within the last five years.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Data Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission with a Bachelor's degree or equivalent in statistics, data analytics or related field.",
        "entry_q": "A Bachelor’s degree or its equivalent in statistics, data analytics or a related field from an accredited U.S. institution recognized by UCF or its equivalent from a foreign institution.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--cs",
        "field": "cs",
        "also_fields": [],
        "department": "Department of Computer Science",
        "program_page": cs_deg_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Computer Science PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Required",
        "gre_val": "Official, competitive GRE score taken within the last five years is required.",
        "gre_q": "Computer Science PhD | Official, competitive GRE score taken within the last five years.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Computer Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission beyond the bachelor's degree; an undergraduate degree in Computer Science is desirable but not required.",
        "entry_q": "Total Credit Hours Required: 72 Credit Hours Minimum beyond the Bachelor's Degree | An undergraduate degree in Computer Science is desirable but not required.",
        "entry_url": cs_deg_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--ece",
        "field": "ece",
        "also_fields": [],
        "department": "Department of Electrical and Computer Engineering",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Electrical Engineering PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Required",
        "gre_val": "Official, competitive GRE score taken within the last five years is required.",
        "gre_q": "Electrical Engineering PhD | Official, competitive GRE score taken within the last five years.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical/Computer Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Bachelor’s or Master’s degree in Electrical Engineering or a closely related discipline.",
        "entry_q": "Bachelor’s or Master’s degree in Electrical Engineering or a closely related discipline.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--mech",
        "field": "mech",
        "also_fields": [],
        "department": "Department of Mechanical and Aerospace Engineering",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Mechanical Engineering PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Mechanical Engineering PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Bachelor’s or Master’s degree in Mechanical or Aerospace Engineering or a closely related discipline.",
        "entry_q": "Bachelor’s or Master’s degree in Mechanical or Aerospace Engineering or a closely related discipline.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--civil",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Civil, Environmental and Construction Engineering",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Civil Engineering PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Required",
        "gre_val": "Official, competitive GRE score taken in the last five years is required.",
        "gre_q": "Civil Engineering PhD | Official, competitive GRE score taken in the last five years.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Master’s or bachelor’s degree in Civil Engineering or a closely related discipline.",
        "entry_q": "Master’s or bachelor’s degree in Civil Engineering or a closely related discipline.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--environment",
        "field": "environment",
        "also_fields": [],
        "department": "Department of Civil, Environmental and Construction Engineering",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Environmental Engineering PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Required",
        "gre_val": "Official, competitive GRE score taken in the last five years is required.",
        "gre_q": "Environmental Engineering PhD | Official, competitive GRE score taken in the last five years.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Environmental Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "A Bachelor’s and/or Master’s degree in Environmental Engineering or a closely related discipline.",
        "entry_q": "A Bachelor’s and/or Master’s degree in Environmental Engineering or a closely related discipline.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--bme",
        "field": "bme",
        "also_fields": [],
        "department": "Department of Mechanical and Aerospace Engineering",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Biomedical Engineering PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Biomedical Engineering PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Bachelor’s or Master’s degree in Biomedical Engineering or Mechanical Engineering or closely related discipline.",
        "entry_q": "Bachelor’s or Master’s degree in Biomedical Engineering or Mechanical Engineering or closely related discipline.",
        "entry_url": doctoral_reqs_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--biology",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Biology",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Integrative and Conservation Biology PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Integrative and Conservation Biology PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biology subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": intl_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--biomed",
        "field": "biomed",
        "also_fields": [],
        "department": "Burnett School of Biomedical Sciences",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Biomedical Sciences PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Biomedical Sciences PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Sciences subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": intl_url,
        "extra_fields": {}
    },
    {
        "id": "ucf--neuro",
        "field": "neuro",
        "also_fields": [],
        "department": "Burnett School of Biomedical Sciences",
        "program_page": doctoral_reqs_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 Fall international application deadline",
        "deadline_q": "Biomedical Sciences PhD | International Applicants | December 1",
        "deadline_url": doctoral_reqs_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required for admission to this program.",
        "gre_q": "Biomedical Sciences PhD | The GRE is not required for admission to this program.",
        "gre_url": doctoral_reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Neuroscience subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": doctoral_reqs_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for university fellowships or assistantships by priority deadline.",
        "funding_q": central_funding_quote,
        "funding_url": doctoral_reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": intl_url,
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
        "university": "ucf",
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
    
    with open(STAGING_PROGS / f"{p['id']}.json", "w", encoding="utf-8") as out:
        json.dump(rec, out, indent=2, ensure_ascii=False)

print(f"Verified & saved {len(programs)} UCF programs")
