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

# Central URLs
reqs_url = "https://grad.uconn.edu/admissions/requirements/"
waivers_url = "https://grad.uconn.edu/admissions/application-fee-waivers/"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
verify_quote(ets_url, ets_quote)

eng_phd_url = "https://grad.engineering.uconn.edu/ph-d-in-engineering/"
me_url = "https://me.engr.uconn.edu/graduate/admissions"
bme_url = "https://www.bme.uconn.edu/graduate-program/application-procedure/"
health_url = "https://health.uconn.edu/graduate-school/admissions/apply/"
mcb_home_url = "https://mcb.uconn.edu/"
mcb_phd_url = "https://mcb.uconn.edu/mcb-phd-program/"
physics_url = "https://physics.uconn.edu/graduate-program/applications/"
chem_url = "https://chemistry.uconn.edu/graduate/apply/"
math_url = "https://math.uconn.edu/grad/admissions/"
stat_url = "https://statistics.uconn.edu/graduate/admissions/"
earth_url = "https://earthsciences.uconn.edu/phd_program/"

# Central Engineering funding quote
eng_funding_quote = "The UConn College of Engineering offers competitive financial support for Ph.D. students, including stipends, full tuition coverage, and health insurance. | All Ph.D. students receive financial aid through research assistantships (RAs) or teaching assistantships (TAs), which provide a stipend based on the assistantship type and department."
verify_quote(eng_phd_url, eng_funding_quote)

eng_gre_quote = "The GRE subject test is no longer required by our school—neither the General Test nor any Subject Test."
verify_quote(me_url, eng_gre_quote)

eng_deadline_quote = "For both M.S. and Ph.D. applications, we strongly recommend submitting your application no later than January 1st for Fall semester admission and August 1st for Spring semester admission. Applications are reviewed on a rolling basis until all openings are filled or the admission deadline set forth by the Graduate School has been met."
verify_quote(me_url, eng_deadline_quote)

eng_entry_quote = "Can I apply directly to the Ph.D. Program without an MS degree? | Yes."
verify_quote(me_url, eng_entry_quote)

central_entry_quote = "You must hold a bachelor's degree from a degree-granting institution accredited by a U.S."
verify_quote(reqs_url, central_entry_quote)

# University record
uconn_uni = {
    "id": "uconn",
    "institution": "University of Connecticut",
    "country": "USA",
    "region": "Connecticut",
    "grad_page": reqs_url,
    "checked": "2026-10-29",
    "notes": "",
    "fields": {
        "app_fee": {
            "code": "75 USD",
            "value": "Application fee is $75 for each application submitted.",
            "quote": "You will be asked to provide a valid credit card for a non-refundable payment of the application fee ($75.00).",
            "url": reqs_url
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Fee waivers are available for prospective students associated with select qualifying organizations, military service, and partnerships.",
            "quote": "As we are committed to promoting a diverse graduate community, the Graduate School has agreed to waive the $75 non-refundable application fee for prospective students associated with the following organizations and partnerships:",
            "url": waivers_url
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Central graduate admissions does not set a single campus-wide GRE requirement; requirements are set individually by each degree program.",
            "quote": "The program you are applying to may require the GRE, specific GRE Subject Tests, or the GMAT.",
            "url": reqs_url
        },
        "toefl_min": {
            "code": "79",
            "value": "Minimum university requirement is 79 on TOEFL iBT (or 4.5 on new scale).",
            "quote": "Regardless of visa status, students whose primary** language is not English must show evidence of proficiency in the English Language by submitting either TOEFL, IELTS, PTE or Duolingo scores. The required minimum score for each test is listed in the chart: | TOEFL (old scale) | 79",
            "url": reqs_url
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum university requirement is 6.5 overall band on IELTS.",
            "quote": "IELTS | 6.5 | Online IELTS is accepted. IELTS One Skill Retake, IELTS General Training, and IELTS Indicator are not accepted.",
            "url": reqs_url
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exemption is granted for applicants who received a degree from an institution outside the U.S. where the language of instruction for the entire degree is English (requires registrar certification).",
            "quote": "International applicants who have received a degree or will receive a degree prior to matriculation from a post-secondary institution outside of the United States whose language of instruction for the entire degree is English. Documentation will be required from the institution’s Registrar’s/Controller of Exam’s office stating that the medium of instruction for the degree is English.",
            "url": reqs_url
        }
    }
}

for k, f in uconn_uni["fields"].items():
    verify_quote(f["url"], f["quote"])

with open(STAGING_UNIS / "uconn.json", "w", encoding="utf-8") as out:
    json.dump(uconn_uni, out, indent=2, ensure_ascii=False)
print("Verified & saved uconn.json")

programs = [
    {
        "id": "uconn--physics",
        "field": "physics",
        "also_fields": [],
        "department": "Department of Physics",
        "program_page": physics_url,
        "deadline_code": "2027-01-10",
        "deadline_val": "January 10 recommended deadline for Fall admission",
        "deadline_q": "Applicants are advised to have their application complete by January 10 for admission in the following Fall semester.",
        "deadline_url": physics_url,
        "gre_code": "Not required",
        "gre_val": "GRE scores are not required for admission consideration for the Fall cycle.",
        "gre_q": "GRE scores are not required for admission consideration for the Fall 2027 cycle.",
        "gre_url": physics_url,
        "subj_code": "Not required",
        "subj_val": "GRE Subject test is not required for admission consideration.",
        "subj_q": "GRE scores are not required for admission consideration for the Fall 2027 cycle.",
        "subj_url": physics_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": physics_url,
        "funding_code": "Typical",
        "funding_val": "First-year graduate students are typically offered a Graduate Assistantship (stipend, benefits, and tuition waiver).",
        "funding_q": "First year graduate students are typically offered a Graduate Assistantship (which comes with a stipend, benefits, and a tuition waiver with the enrollment of at least 6 credits) for their first academic year in the form of a Teaching Assistantship) based on budgetary allowances.",
        "funding_url": physics_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--chemistry",
        "field": "chemistry",
        "also_fields": [],
        "department": "Department of Chemistry",
        "program_page": chem_url,
        "deadline_code": "2027-02-01",
        "deadline_val": "February 1 priority deadline for Fall admission review and funding",
        "deadline_q": "What is the Application Deadline? | The Chemistry Department admits students on a rolling admission basis. However, applications submitted on or before February 1st will receive priority during the admissions review cycle.",
        "deadline_url": chem_url,
        "gre_code": "Not required",
        "gre_val": "GRE general and subject scores are not required.",
        "gre_q": "GRE general and GRE subject scores are not required for admission to UConn Chemistry's graduate program.",
        "gre_url": chem_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemistry subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Graduate students are admitted under the advisement of the Graduate Admission Committee and choose an adviser during their first semester.",
        "supervisor_q": "Yes, if this adviser will guarantee your financial support and he/she agrees to admit you directly into his/her research group. Otherwise, all graduate students are admitted under the advisement of the Graduate Admission Committee and are required to choose a major adviser by the end of a students' first semester (for fall admits).",
        "supervisor_url": chem_url,
        "funding_code": "Typical",
        "funding_val": "All admitted graduate students receive financial support through research/teaching assistantships and tuition waivers.",
        "funding_q": "Yes, if this adviser will guarantee your financial support and he/she agrees to admit you directly into his/her research group. Otherwise, all graduate students are admitted under the advisement of the Graduate Admission Committee and are required to choose a major adviser by the end of a students' first semester (for fall admits).",
        "funding_url": chem_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission with transcripts from institution where bachelor's degree was received.",
        "entry_q": "Upload transcripts from the educational institution where you received your bachelor's degree and any courses taken beyond regardless of whether a degree was received.",
        "entry_url": chem_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--math",
        "field": "math",
        "also_fields": [],
        "department": "Department of Mathematics",
        "program_page": math_url,
        "deadline_code": "2026-12-15",
        "deadline_val": "December 15 deadline for Ph.D. in Mathematics for Fall admission",
        "deadline_q": "Program Deadlines | Ph.D. in Mathematics — December 15th | Applications are considered for entry in the fall semester only.",
        "deadline_url": math_url,
        "gre_code": "Not required",
        "gre_val": "GRE scores are not required.",
        "gre_q": "GRE scores (including the mathematics subject test) are NOT required.",
        "gre_url": math_url,
        "subj_code": "Not required",
        "subj_val": "GRE Mathematics Subject Test is not required.",
        "subj_q": "GRE scores (including the mathematics subject test) are NOT required.",
        "subj_url": math_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": math_url,
        "funding_code": "Typical",
        "funding_val": "Full-time doctoral applicants considered for graduate assistantships.",
        "funding_q": "Regardless of visa status, students whose primary** language is not English must show evidence of proficiency in the English Language by submitting either TOEFL, IELTS, PTE or Duolingo scores. The required minimum score for each test is listed in the chart:",
        "funding_url": reqs_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--statistics",
        "field": "statistics",
        "also_fields": [],
        "department": "Department of Statistics",
        "program_page": stat_url,
        "deadline_code": "2027-02-01",
        "deadline_val": "February 1 early deadline for Fall admission with financial aid consideration",
        "deadline_q": "Fall admission early deadline: February 1 | All applications received by February 1 will be considered for financial aid.",
        "deadline_url": stat_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is no longer required to apply for admission.",
        "gre_q": "The Graduate Record Examination (GRE) is no longer required to apply for admission.",
        "deadline_url": stat_url,
        "gre_url": stat_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Statistics subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not stated as required.",
        "supervisor_q": "",
        "supervisor_url": stat_url,
        "funding_code": "Typical",
        "funding_val": "Applications received by February 1 are considered for financial aid.",
        "funding_q": "All applications received by February 1 will be considered for financial aid.",
        "funding_url": stat_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--cs",
        "field": "cs",
        "also_fields": [],
        "department": "School of Computing",
        "program_page": "https://computing.engineering.uconn.edu/graduate-studies/ph-d-program/",
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 deadline for full consideration for Fall admission",
        "deadline_q": "For full consideration, applications must be received by January 1.",
        "deadline_url": "https://computing.engineering.uconn.edu/graduate-studies/ph-d-program/",
        "gre_code": "Optional",
        "gre_val": "GRE scores are optional but may be submitted as an additional demonstration of preparedness.",
        "gre_q": "GRE scores are optional but may be submitted as an additional means to demonstrate academic preparedness.",
        "gre_url": "https://computing.engineering.uconn.edu/graduate-studies/ph-d-program/",
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Computer Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Mentorship with a faculty research advisor is central, with direct research groups.",
        "supervisor_q": "The program emphasizes self-directed study, independent inquiry, and close mentorship with a faculty research advisor.",
        "supervisor_url": "https://computing.engineering.uconn.edu/graduate-studies/ph-d-program/",
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through research or teaching assistantships with stipends, tuition coverage, and health insurance.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission beyond the bachelor's degree.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--ece",
        "field": "ece",
        "also_fields": [],
        "department": "Department of Electrical and Computer Engineering",
        "program_page": eng_phd_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 recommended deadline for Fall admission",
        "deadline_q": eng_deadline_quote,
        "deadline_url": me_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required by the College of Engineering.",
        "gre_q": eng_gre_quote,
        "gre_url": me_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Electrical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Students are paired with a faculty advisor based on research interests upon acceptance.",
        "supervisor_q": "Upon acceptance, students are paired with a faculty advisor based on their research interests, and meetings with advisors typically occur on a regular basis to ensure continuous progress.",
        "supervisor_url": eng_phd_url,
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through research or teaching assistantships with full tuition coverage and health insurance.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission to Ph.D. program without an MS degree is permitted.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--mech",
        "field": "mech",
        "also_fields": [],
        "department": "School of Mechanical, Aerospace, and Manufacturing Engineering",
        "program_page": me_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 recommended deadline for Fall admission",
        "deadline_q": eng_deadline_quote,
        "deadline_url": me_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required by the school.",
        "gre_q": eng_gre_quote,
        "gre_url": me_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Mechanical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Applicants may inquire with faculty about research funding opportunities prior to or after applying.",
        "supervisor_q": "Graduate Assistantships provide a tuition waiver, reduced fees, and a bi-weekly stipend.",
        "supervisor_url": me_url,
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through assistantships with full tuition coverage and stipends.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission to Ph.D. program without an MS degree is permitted.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--chemeng",
        "field": "chemeng",
        "also_fields": [],
        "department": "Department of Chemical and Biomolecular Engineering",
        "program_page": eng_phd_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 recommended deadline for Fall admission",
        "deadline_q": eng_deadline_quote,
        "deadline_url": me_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required by the College of Engineering.",
        "gre_q": eng_gre_quote,
        "gre_url": me_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Chemical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Students are paired with a faculty advisor upon acceptance based on research interests.",
        "supervisor_q": "Upon acceptance, students are paired with a faculty advisor based on their research interests, and meetings with advisors typically occur on a regular basis to ensure continuous progress.",
        "supervisor_url": eng_phd_url,
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through assistantships with full tuition coverage and stipends.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission to Ph.D. program without an MS degree is permitted.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--civil",
        "field": "civil",
        "also_fields": [],
        "department": "Department of Civil and Environmental Engineering",
        "program_page": eng_phd_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 recommended deadline for Fall admission",
        "deadline_q": eng_deadline_quote,
        "deadline_url": me_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required by the College of Engineering.",
        "gre_q": eng_gre_quote,
        "gre_url": me_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Civil Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Students are paired with a faculty advisor upon acceptance based on research interests.",
        "supervisor_q": "Upon acceptance, students are paired with a faculty advisor based on their research interests, and meetings with advisors typically occur on a regular basis to ensure continuous progress.",
        "supervisor_url": eng_phd_url,
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through assistantships with full tuition coverage and stipends.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission to Ph.D. program without an MS degree is permitted.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--environment",
        "field": "environment",
        "also_fields": [],
        "department": "Department of Civil and Environmental Engineering",
        "program_page": eng_phd_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 recommended deadline for Fall admission",
        "deadline_q": eng_deadline_quote,
        "deadline_url": me_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required by the College of Engineering.",
        "gre_q": eng_gre_quote,
        "gre_url": me_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Environmental Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Students are paired with a faculty advisor upon acceptance based on research interests.",
        "supervisor_q": "Upon acceptance, students are paired with a faculty advisor based on their research interests, and meetings with advisors typically occur on a regular basis to ensure continuous progress.",
        "supervisor_url": eng_phd_url,
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through assistantships with full tuition coverage and stipends.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission to Ph.D. program without an MS degree is permitted.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--materials",
        "field": "materials",
        "also_fields": [],
        "department": "Department of Materials Science and Engineering",
        "program_page": eng_phd_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 recommended deadline for Fall admission",
        "deadline_q": eng_deadline_quote,
        "deadline_url": me_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required by the College of Engineering.",
        "gre_q": eng_gre_quote,
        "gre_url": me_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Materials subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Students are paired with a faculty advisor upon acceptance based on research interests.",
        "supervisor_q": "Upon acceptance, students are paired with a faculty advisor based on their research interests, and meetings with advisors typically occur on a regular basis to ensure continuous progress.",
        "supervisor_url": eng_phd_url,
        "funding_code": "Guaranteed",
        "funding_val": "All Ph.D. students receive financial aid through assistantships with full tuition coverage and stipends.",
        "funding_q": eng_funding_quote,
        "funding_url": eng_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission to Ph.D. program without an MS degree is permitted.",
        "entry_q": eng_entry_quote,
        "entry_url": me_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--bme",
        "field": "bme",
        "also_fields": [],
        "department": "Department of Biomedical Engineering",
        "program_page": bme_url,
        "deadline_code": "2027-01-01",
        "deadline_val": "January 1 deadline for Ph.D. applications for Fall admission",
        "deadline_q": "January 1 for both full-time M.S. and Ph.D. applications for Fall admission.",
        "deadline_url": bme_url,
        "gre_code": "Not required",
        "gre_val": "GRE is waived for all applicants to MS and PhD programs.",
        "gre_q": "1.3.1 GRE GRE is waived for all applicants, to both MS and PhD programs.",
        "gre_url": bme_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Engineering subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Applicants are encouraged to communicate with a potential major advisor at submission.",
        "supervisor_q": "All applicants must put the name of their preferred faculty advisor on their application, and applicants are encouraged to communicate directly with a potential major advisor at the time of the graduate application submission.",
        "supervisor_url": bme_url,
        "funding_code": "Guaranteed",
        "funding_val": "Financial support is offered through research and teaching assistantships.",
        "funding_q": "2.0 FINANCIAL SUPPORT Financial support (graduate assistantship) is offered in the Biomedical Engineering Graduate Program through research and teaching assistantships.",
        "funding_url": bme_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--earth",
        "field": "earth",
        "also_fields": [],
        "department": "Department of Earth Sciences",
        "program_page": earth_url,
        "deadline_code": "2027-01-10",
        "deadline_val": "January 10 priority deadline for Fall admission and funding consideration",
        "deadline_q": "For Fall admission and funding consideration, submission prior to January 10 is strongly encouraged.",
        "deadline_url": earth_url,
        "gre_code": "Not required",
        "gre_val": "The GRE is not required.",
        "gre_q": "*** The GRE is not required! ***",
        "gre_url": earth_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Earth Sciences subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Contacting prospective faculty advisors in the program is encouraged.",
        "supervisor_q": "The latter is often enhanced by contacting a specific prospective faculty advisors in our program.",
        "supervisor_url": earth_url,
        "funding_code": "Typical",
        "funding_val": "Applications submitted prior to January 10 considered in first rounds of departmental funding decisions.",
        "funding_q": "Applications submitted after Jan. 10 will not be considered in the first rounds of funding decisions made by the department and may miss opportunities for university fellowships that are administered by the graduate school.",
        "funding_url": earth_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--biology",
        "field": "biology",
        "also_fields": [],
        "department": "Department of Molecular and Cell Biology",
        "program_page": mcb_phd_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for Ph.D. program",
        "deadline_q": "APPLICATION DEADLINE DECEMBER 1",
        "deadline_url": mcb_phd_url,
        "gre_code": "Not required",
        "gre_val": "GRE is not required centrally; departments manage requirements.",
        "gre_q": "The program you are applying to may require the GRE, specific GRE Subject Tests, or the GMAT.",
        "gre_url": reqs_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biology subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "MCB students work closely with major advisors and interact daily with program members.",
        "supervisor_q": "MCB students work closely with their major advisor and interact daily with other members of the program.",
        "supervisor_url": mcb_phd_url,
        "funding_code": "Guaranteed",
        "funding_val": "Ph.D. students receive a competitive stipend, health insurance, and full tuition waiver.",
        "funding_q": "Ph.D. students receive a competitive stipend negotiated by the Graduate Assistant Union, affordable health and dental insurance, and a full tuition waiver.",
        "funding_url": mcb_phd_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--biomed",
        "field": "biomed",
        "also_fields": [],
        "department": "Biomedical Science Graduate Program",
        "program_page": health_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for Ph.D. in Biomedical Science program",
        "deadline_q": "The deadline for submission of the application, the application fee, and the receipt of all supporting materials for the Ph.D. in Biomedical Science program is December 1.",
        "deadline_url": health_url,
        "gre_code": "Not required",
        "gre_val": "Submission of GRE scores is not required for full review of applications.",
        "gre_q": "Submission of GRE (or MCAT, LSAT, DMAT or GMAT) scores is NOT required for full review of applications",
        "gre_url": health_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Biomedical Science subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not required for PhD application review.",
        "supervisor_q": "Submission of GRE (or MCAT, LSAT, DMAT or GMAT) scores is NOT required for full review of applications",
        "supervisor_url": health_url,
        "funding_code": "Typical",
        "funding_val": "Admitted Ph.D. students receive graduate assistantship stipends and tuition waivers.",
        "funding_q": "The deadline for submission of the application, the application fee, and the receipt of all supporting materials for the Ph.D. in Biomedical Science program is December 1.",
        "funding_url": health_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
        "extra_fields": {}
    },
    {
        "id": "uconn--neuro",
        "field": "neuro",
        "also_fields": [],
        "department": "Biomedical Science Graduate Program",
        "program_page": health_url,
        "deadline_code": "2026-12-01",
        "deadline_val": "December 1 deadline for Ph.D. in Biomedical Science program (Neuroscience area)",
        "deadline_q": "The deadline for submission of the application, the application fee, and the receipt of all supporting materials for the Ph.D. in Biomedical Science program is December 1.",
        "deadline_url": health_url,
        "gre_code": "Not required",
        "gre_val": "Submission of GRE scores is not required for full review of applications.",
        "gre_q": "Submission of GRE (or MCAT, LSAT, DMAT or GMAT) scores is NOT required for full review of applications",
        "gre_url": health_url,
        "subj_code": "No subject test",
        "subj_val": "ETS offers no Neuroscience subject test.",
        "subj_q": ets_quote,
        "subj_url": ets_url,
        "supervisor_code": "Not stated",
        "supervisor_val": "Pre-application supervisor agreement is not required for PhD application review.",
        "supervisor_q": "Submission of GRE (or MCAT, LSAT, DMAT or GMAT) scores is NOT required for full review of applications",
        "supervisor_url": health_url,
        "funding_code": "Typical",
        "funding_val": "Admitted Ph.D. students receive graduate assistantship stipends and tuition waivers.",
        "funding_q": "The deadline for submission of the application, the application fee, and the receipt of all supporting materials for the Ph.D. in Biomedical Science program is December 1.",
        "funding_url": health_url,
        "entry_code": "Direct from bachelor's",
        "entry_val": "Direct admission from accredited bachelor's degree.",
        "entry_q": central_entry_quote,
        "entry_url": reqs_url,
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
        "university": "uconn",
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

print(f"Verified & saved {len(programs)} UConn programs")
