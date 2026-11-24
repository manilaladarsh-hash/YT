import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from rec import OUT, save_program, save_university
from research import cache_paths
from validate_data import norm


B = "https://www.cityu.edu.hk"
C = "https://www.cb.cityu.edu.hk"
R = "/pg/research-degree-programmes"
ENTRY = B + R + "/entrance-requirements"
STEPS = B + R + "/steps-and-procedures"
FUNDS = B + R + "/scholarships-financial-aid-and-fees"
APPLY = C + "/en" + R + "/apply-now"
HANDBOOK = B + "/sgs/files/prospective/rpg/Admissions_Handbook.pdf"
HKPFS = C + "/en/pg/hong-kong-phd-fellowship-scheme/about-the-scheme"
CATALOGUE = B + "/pg/current/catalogue/catalogue_R.htm?page=R/R_programme_index.htm"
COMPUTING = B + "/en/cc/programmes/research-degree-programmes/admission-overview"
ENGINEERING = B + "/en/ceng/programmes/research-degree-programmes"
BMS_CHECKLIST = B + "/bms/doc/pg/rpg/adm-checksheet.pdf"
PROPOSAL = B + "/en" + R + "/research-proposal-guidelines"
UID = "cityuhk"
CHECKED = date.today().isoformat()
programmes = []


def cached(url):
    record = json.loads(cache_paths(url).read_text(encoding="utf-8"))
    assert record["status"] == 200 and len(record["text"]) >= 800, url
    return " ".join(record["text"].split())


def quote(url, excerpt):
    page = cached(url)
    start = norm(page).index(norm(excerpt))
    exact = page[start : start + len(excerpt)]
    assert norm(exact) == norm(excerpt), (url, excerpt)
    return {"quote": exact, "url": url}


def field(code, value, url, excerpt="", *support, **metadata):
    if excerpt:
        excerpt = quote(url, excerpt)["quote"]
    if support:
        metadata["also"] = [quote(*citation) for citation in support]
    return (code, value, excerpt, url, metadata)


BASE_DEADLINE = field(
    "2026-12-01",
    "The 2027/28 main round closes at 11:59 p.m. Hong Kong time. Later applications may be considered if places remain. HKPFS registration with the RGC is due by noon on the same date.",
    STEPS,
    "1 December 2026*",
    (STEPS, "Applications received after the above-mentioned deadline may be considered subject to the availability of student places."),
    (HKPFS, "Applicants must first register on the RGC’s Online Application System (OAS) and obtain a reference number before 1 December 2026 (12:00 noon Hong Kong time)."),
    time_sensitive="2026-12-01",
)
BASE_FUNDING = field(
    "Competitive",
    "Eligible full-time applicants are considered on academic merit. The studentship can run up to four years with annual renewal based on progress and duties. The published 2026/27 rates are HK$19,100 monthly before the qualifying exam and HK$19,600 after it.",
    FUNDS,
    "The postgraduate studentship is granted on the basis of academic merit.",
    (FUNDS, "Continuation and renewal of the award are subject to satisfactory study progress, achievement in coursework results and performance in any academic-related duties assigned."),
    (FUNDS, "PhD students may be granted the studentship for a maximum of four years"),
    (FUNDS, "the studentship Basic Rate is HK$19,100 per month (~US$2,440) and Advance Rate is HK$19,600 per month (~US$2,510)."),
)
BASE_SUPERVISOR = field(
    "Recommended",
    "The graduate application checklist instructs applicants to find a potential supervisor and seek consent.",
    STEPS,
    "Search for a potential supervisor and seek consent",
)
ENTRY_BACHELOR = "hold a Bachelor’s degree with first class honours (or equivalent qualification) from a recognised university."
ENTRY_MASTER = "hold a Master’s degree (or equivalent qualification) from a recognised university;"
BASE_ENTRY_VALUE = "A first-class honours bachelor's degree or equivalent, a recognised master's degree, or a higher research degree can qualify. CityUHK MPhil transfer is a separate route."


def entry_route(url, bachelor=ENTRY_BACHELOR, master=ENTRY_MASTER, value=BASE_ENTRY_VALUE):
    return field("Either", value, url, bachelor, (url, master))


def programme(
    field_id,
    department,
    name,
    path,
    catalogue_id,
    *,
    deadline=BASE_DEADLINE,
    supervisor=BASE_SUPERVISOR,
    funding=BASE_FUNDING,
    entry=None,
    notes="",
    also_fields=(),
):
    url = B + path if path.startswith("/") else path
    catalogue = B + "/catalogue/pg/202627/programme/" + catalogue_id + ".htm"
    assert norm(name) in norm(cached(CATALOGUE)), name
    cached(url)
    cached(catalogue)
    programmes.append(
        ((UID, field_id, department, url, {
            "deadline": deadline,
            "gre_subject": field("Not stated", "No distinct GRE Subject Test policy was identified on the programme or central pages checked.", url),
            "supervisor": supervisor,
            "funding": funding,
            "entry_route": entry if entry is not None else entry_route(ENTRY),
        }), dict(
            notes=f"Official research-degree catalogue: {catalogue}. {notes}".strip(),
            also_fields=also_fields,
            checked=CHECKED,
            name=name,
        )),
    )


assert OUT.name == "staging"
assert not (OUT / "universities" / f"{UID}.json").exists()
assert not list((OUT / "programs").glob(f"{UID}--*.json"))
university = (
    UID,
    "City University of Hong Kong (CityUHK)",
    "Hong Kong",
    "Hong Kong",
    ENTRY,
    {
        "app_fee": field(
            "Not stated",
            "The regular research-degree fee is HK$500 on the 2026/27 fee page. The 2027/28 HKPFS route also publishes HK$500 per programme, subject to revision. The regular 2027/28 amount is not confirmed.",
            APPLY,
            "The application fees for 2026-27 entry are as follows:",
            (APPLY, "Online Application HK$500 HK$1,000"),
            (HKPFS, "A non-refundable application fee of HK$500 (~US$64) (subject to revision) will be charged for each application for a programme."),
        ),
        "fee_waiver": field("Not stated", "No 2027/28 application-fee waiver policy for international research-degree applicants was located. Tuition scholarships are separate.", APPLY),
        "gre_general": field(
            "Optional",
            "The graduate handbook allows GRE or GMAT scores as supplementary information if available. These scores do not meet the English proficiency requirement.",
            HANDBOOK,
            "Graduate Record Examinations (GRE)/Graduate Management Admission Test (GMAT) scores are not accepted in fulfilment of the University’s English proficiency requirement for research degree programmes, but can be submitted as supplementary information for reference if available.",
        ),
        "toefl_min": field(
            "4.5 (new scale)",
            "TOEFL iBT 4.5 for tests from 21 January 2026. The previous scale minimum was 79. Scores must be valid at submission and are valid for two years.",
            ENTRY,
            "a score of 79 (for tests taken prior to 21 January 2026) or 4.5 (for tests taken from 21 January 2026 onwards) (Internet-based test) in the Test of English as a Foreign Language (TOEFL)",
            (ENTRY, "TOEFL and IELTS scores are considered valid for two years from the test date and must be valid at the time of submission of application."),
        ),
        "ielts_min": field(
            "6.5",
            "CityUHK lists IELTS 6.5 overall. The application notes exclude IELTS Indicator, One Skill Retake and IELTS Online.",
            ENTRY,
            "an overall band score of 6.5 in International English Language Testing System (IELTS)",
            (APPLY, "‘IELTS Indicator’, ‘IELTS One Skill Retake’ and ‘IELTS Online’ are not acceptable."),
        ),
        "english_waiver": field(
            "Conditional",
            "The university test requirement applies when the entrance qualification was taught in a language other than English. For HKPFS, a candidate from a non-English-speaking university must document English as the language of instruction for every course that qualifies them for admission.",
            HKPFS,
            "Applicants from non-English speaking universities are required to attach their TOEFL or IELTS score results with their PhD applications, unless they can provide proof that English is the language of instruction for all courses that qualify them for entrance to their proposed PhD programmes.",
            (ENTRY, "Applicants whose entrance qualification is obtained from an institution where the medium of instruction is not English should fulfill the following minimum English proficiency requirement"),
        ),
    },
)
university_options = dict(
    notes=f"Research-degree catalogue: {CATALOGUE}. CityUHK distinguishes government-funded and self-financing admission. HKPFS is a separate competitive route for new full-time PhD applicants, irrespective of nationality. The 2027/28 fellowship pays HK$28,700 per month for up to three years, with matching fourth-year support from CityUHK for awardees admitted to a four-year PhD. Check the published award terms for entrance scholarship, travel and fee details: {HKPFS}.",
    checked=CHECKED,
)

physics_url = B + "/phy/research-degree/phd-physics"
programme(
    "physics", "Department of Physics", "Doctor of Philosophy in Physics",
    physics_url, "PHY2_P", also_fields=("astronomy",),
    supervisor=field(
        "Recommended",
        "The department advises applicants to discuss their proposed work with a potential supervisor and obtain consent before submission.",
        physics_url,
        "The applicant is advised to obtain the consent of one of the academic staff members to be his/her supervisor before submitting the application.",
    ),
    entry=entry_route(
        physics_url,
        "hold a Bachelor’s degree with first-class honours (or equivalent qualification) in Physics or related fields from a recognised university;",
        "hold a Master’s degree (or equivalent qualification) in Physics or related fields from a recognised university;",
        "First-class honours bachelor’s or master’s entry is possible in Physics or a related field. Higher research degrees and CityUHK MPhil transfer are also listed.",
    ),
    notes="The catalogue explicitly lists Astrophysics and Particle Physics as an area to which Physics PhD students may be admitted. The degree is awarded in Physics.",
)

chem_url = B + "/en/chem/programmes/research-postgraduate-programme"
programme(
    "chemistry", "Department of Chemistry", "Doctor of Philosophy in Chemistry",
    chem_url, "CHEM2_P",
    entry=entry_route(
        chem_url,
        "hold a bachelor’s degree with first class honours (or equivalent qualification) from a recognized university;",
        "hold a master’s degree (or equivalent qualification) from a recognized university;",
    ),
    notes="Biological, environmental and materials chemistry are research options within this degree.",
)

mse_url = B + "/en/mse/prospective-students/admission/research-degree"
programme(
    "materials", "Department of Materials Science and Engineering",
    "Doctor of Philosophy in Materials Science and Engineering", mse_url, "MSE2_P",
    entry=entry_route(
        mse_url,
        "hold a Bachelor's degree with first class honours (or equivalent qualification) from a recognised university.",
        "hold a Master's degree (or equivalent qualification) from a recognised university;",
    ),
    notes="The department considers qualified full-time students for studentships and describes government-funded and self-financing study as separate options.",
)

math_url = B + "/en/ma/programmes/postgraduate/master-of-philosophy-mphil"
programme(
    "math", "Department of Mathematics", "Doctor of Philosophy in Mathematics", math_url, "MA2_P",
    entry=entry_route(
        math_url,
        "hold a Bachelor's degree with first class honours (or equivalent qualification) from a recognised university.",
        "hold a Master's degree (or equivalent qualification) from a recognised university;",
    ),
)

computing_funding = field(
    "Competitive",
    "The College of Computing lists a HK$19,100 monthly stipend during PhD study for admitted government-funded students. Access to a funded place is competitive. The college recommends outstanding candidates for HKPFS.",
    COMPUTING,
    "Admitted students will receive the university scholarship with a monthly stipend of HK$19,100 (US$2,433) during their PhD studies at CityUHK. (Applicable to government-funded students only)",
    (FUNDS, "The postgraduate studentship is granted on the basis of academic merit."),
)

bios_url = B + "/bios/pg/research.htm"
programme(
    "statistics", "Department of Biostatistics", "Doctor of Philosophy in Biostatistics",
    bios_url, "BIOS2_P", funding=computing_funding,
    entry=entry_route(
        bios_url,
        "hold a Bachelor's degree with first class honours (or equivalent qualification) from a recognised university.",
        "hold a Master's degree (or equivalent qualification) from a recognised university;",
    ),
)

cs_url = "https://www.cs.cityu.edu.hk/academic-programmes/master-philosophy-doctor-philosophy/admissions"
programme(
    "cs", "Department of Computer Science", "Doctor of Philosophy in Computer Science",
    cs_url, "CS3_P", funding=computing_funding,
    entry=entry_route(
        cs_url,
        "hold a Bachelor's degree with first class honours (or equivalent qualification) from a recognised university.",
        "hold a taught Master's degree (or equivalent qualification) from a recognised university;",
    ),
)

ds_url = "https://www.ds.cityu.edu.hk/en/programmes/postgraduate-programmes/phd-programme-data-science"
programme(
    "datasci", "Department of Data Science", "Doctor of Philosophy in Data Science",
    ds_url, "DS2_P", funding=computing_funding,
    entry=entry_route(
        ds_url,
        "hold a Bachelor’s degree with first-class honours (or equivalent qualification) from a recognised university.",
        "hold a Master’s degree (or equivalent qualification) from a recognised university;",
    ),
    supervisor=field(
        "Recommended", "The department strongly advises candidates to discuss the proposed research and seek consent before applying.",
        ds_url, "Applicants are strongly advised to contact a potential supervisor to seek consent and discuss the proposed research area before applying.",
    ),
)

bms_url = B + "/bms/pg/rpg.htm"
programme(
    "biomed", "Department of Biomedical Sciences", "Doctor of Philosophy in Biomedical Sciences",
    bms_url, "BMS3_P", also_fields=("biology",),
    deadline=field(
        "2026-12-01",
        "The main round closes on 1 December 2026 at 11:59 p.m. Hong Kong time. The department has rolling start dates and considers late applications subject to space.",
        bms_url, "APPLICATION DEADLINE 11:59 pm, 1 December 2026",
        (bms_url, "Applications received after deadline will be considered subject to the number of student places left outside the main admission round."),
        time_sensitive="2026-12-01",
    ),
    supervisor=field(
        "Required",
        "Upload the proposed supervisor’s consent email with the department application checklist.",
        BMS_CHECKLIST, "Proposed supervisor: 02 Supervisor’s consent email",
        (BMS_CHECKLIST, "must complete and upload this Check Sheet together with all required documents prescribed in the application guide to the online application system."),
    ),
    notes="The department and catalogue explicitly describe research training in both biology and biomedical sciences. The department links a checklist bearing the previous BMS2/P code. Its current catalogue record is BMS3/P. The separate CityUHK–Cornell interdisciplinary veterinary PhD and other Jockey Club College research doctorates are documented for classification in OWNER_REVIEW.md.",
)

programme(
    "neuro", "Department of Neuroscience", "Doctor of Philosophy in Neuroscience",
    "/neuro/edu/rpg.htm", "NS2_P",
)

see_url = B + "/en/see/programmes/research-degree-programme"
programme(
    "environment", "School of Energy and Environment", "Doctor of Philosophy in Energy and Environment",
    see_url, "E2_P",
    supervisor=field(
        "Recommended",
        "Discuss the topic with a School faculty member before applying and name the proposed supervisor in the application. The research statement guidelines advise discussion where possible and do not explicitly require prior consent.",
        see_url, "The name of the proposed supervisor should be specified in the application.",
        (PROPOSAL, "Applicant should indicate on his/her application form of his/her preferred supervisor."),
        (PROPOSAL, "If at all possible, the applicant is advised to seek comments on their statement by discussing it with the faculty member of the School"),
    ),
    notes="The PhD lists sustainability, energy and environment as qualifying examination streams. The programme page and central HKPFS page report different entrance scholarship estimates.",
)

ee_url = "https://www.ee.cityu.edu.hk/current_students/research_degree/application"
programme(
    "ece", "Department of Electrical Engineering", "Doctor of Philosophy in Electrical Engineering",
    ee_url, "EE2_P", entry=entry_route(ENGINEERING),
    deadline=field(
        "2026-12-01",
        "The Normal Round closes on 1 December 2026. Later applications can be considered. HKPFS applicants first register with RGC by noon Hong Kong time and submit to CityUHK by 11:59 p.m. the same day.",
        ee_url, "Normal Round 1 Dec 2026",
        (HKPFS, "Applicants are required to submit a full application, including supporting documents, to CityUHK through our Online Application System on or before 1 December 2026 (11:59 p.m. Hong Kong Time)."),
        time_sensitive="2026-12-01",
    ),
    supervisor=field(
        "Recommended",
        "Contact before applying is encouraged and expressly optional for the Normal Round. Applicants must declare a research area.",
        ee_url, "Applicants are encouraged to contact a potential supervisor prior to submitting an application to our university.",
        (ee_url, "While it is not mandatory for applicant to contact EE faculty prior to submitting an application, they must declare an research area of interest in the application form."),
    ),
    notes="The department's HKPFS scholarship estimate is older than the 2027/28 central HKPFS figure.",
)

for field_id, department, name, url, cat_code, degree_quote in (
    (
        "bme", "Department of Biomedical Engineering", "Doctor of Philosophy in Biomedical Engineering",
        B + "/bme/prg-phdmphil.htm", "BME2_P", "PhD (students with a bachelor’s or a master’s degree)",
    ),
    (
        "mech", "Department of Mechanical Engineering", "Doctor of Philosophy in Mechanical Engineering",
        B + "/mne/programmes/doctor-philosophy-phd-and-master-philosophy-mphil", "MNE_P", "PhD (students with a bachelor's or a master's degree)",
    ),
):
    programme(
        field_id, department, name, url, cat_code,
        supervisor=field(
            "Required",
            "The department instructs applicants to contact a faculty member before filing. Applications supported by the proposed supervisor are forwarded for a decision.",
            url, "Qualified applications supported by the proposed supervisor will then be forwarded",
            (url, "you should contact a faculty member of the Department in your proposed area of work who may eventually become your supervisor before you submit a full online application"),
        ),
        funding=field(
            "Competitive",
            "Government-funded places with studentship are limited. Candidates can apply as self-financed students as well.",
            url,
            "Government-funded PhD places with studentship are limited and therefore highly competitive. Suitably qualified candidates can also apply for admission as self-financed research students without studentship.",
        ),
        entry=field("Either", BASE_ENTRY_VALUE, url, degree_quote, (ENGINEERING, ENTRY_BACHELOR), (ENGINEERING, ENTRY_MASTER)),
        notes="The department page uses the legacy 79 iBT floor. The current graduate school's 79 legacy and 4.5 new-scale rule specifies the test date cutoff.",
    )

programme(
    "civil", "Department of Architecture and Civil Engineering",
    "Doctor of Philosophy in Architecture and Civil Engineering",
    "/en/ace/programmes-admissions/research-degree-programmes", "CA2_P",
    entry=entry_route(ENGINEERING),
)

assert len(programmes) == 14
save_university(*university, **university_options)
for args, kwargs in programmes:
    save_program(*args, **kwargs)
print(f"Staged {len(programmes)} {UID} programmes.")
