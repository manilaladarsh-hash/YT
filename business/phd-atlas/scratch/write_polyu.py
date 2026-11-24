import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGING_UNI = ROOT / "data" / "staging" / "universities"
STAGING_PROG = ROOT / "data" / "staging" / "programs"
STAGING_UNI.mkdir(parents=True, exist_ok=True)
STAGING_PROG.mkdir(parents=True, exist_ok=True)

CHECKED = "2026-11-15"

URL_GS = "https://www.polyu.edu.hk/gs/"
URL_ADM_REQ = "https://www.polyu.edu.hk/study/pg/research-postgraduate/admission-requirements-rpg"
URL_APP_FEE = "https://www.polyu.edu.hk/study/pg/research-postgraduate-application-fee"
URL_FELLOWSHIPS = "https://www.polyu.edu.hk/gs/prospective-students/fellowship-scholarship-schemes/"
URL_DEADLINES = "https://www.polyu.edu.hk/gs/prospective-students/how-to-apply/application-deadline/"
URL_SUPP_DOCS = "https://www.polyu.edu.hk/study/pg/research-postgraduate/supporting-documents-application-rpg"
URL_FAQ = "https://www.polyu.edu.hk/study/pg/research-postgraduate/frequently-asked-questions-rpg"
URL_TUITION = "https://www.polyu.edu.hk/study/pg/research-postgraduate/tuition-fee-and-registration-fee-rpg"
URL_ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"

uni_data = {
    "id": "polyu",
    "institution": "The Hong Kong Polytechnic University",
    "country": "Hong Kong",
    "region": "Hong Kong",
    "grad_page": URL_GS,
    "checked": CHECKED,
    "fields": {
        "app_fee": {
            "code": "600 HKD",
            "value": "Non-refundable, non-transferable application fee is HK$600 per application for the 2027/28 intake cohort (increased from HK$500 for 2026/27), payable online upon application submission.",
            "quote": "Intake Cohort | 2026/27 (HK$) | 2027/28 (HK$) | Application Fee | 500 | 600 | The application fee is non-refundable and non-transferrable. You must settle the application fee upon submission of your online application.",
            "url": URL_APP_FEE,
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "PolyU's Research Postgraduate Application Fee page states that the HK$600 application fee is non-refundable and non-transferable and must be settled upon submission for the application to be processed; no fee waiver policy is stated.",
            "quote": "",
            "url": URL_APP_FEE,
        },
        "gre_general": {
            "code": "Not required",
            "value": "Not required for STEM Research Postgraduate programmes; on PolyU's Supporting Documents for Application page, GRE or GMAT scores are required only by Faculty of Business departments.",
            "quote": "GMAT or GRE results are required. | Department of Logistics and Maritime Studies | Department of Computing | Academic Referee's Report | Curriculum Vitae | Research Proposal | Transcript / Certificate",
            "url": URL_SUPP_DOCS,
        },
        "toefl_min": {
            "code": "80",
            "value": "Minimum TOEFL iBT score is 80 or above in a single attempt taken at a test centre (valid for two years after the test date; no sub-score minimums; PolyU institutional code 0732).",
            "quote": "A Test of English as a Foreign Language (TOEFL) score of 80 or above for the Internet-based test. | All English language test scores are considered valid for two years after the date of the test. | Remarks: Only tests taken at a test centre and scores in one single attempt are accepted.",
            "url": URL_ADM_REQ,
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Minimum IELTS Academic Module overall score is 6.5 in a single attempt taken at a test centre (valid for two years after the test date; no sub-score minimums).",
            "quote": "An overall score of at least 6.5 in the International English Language Testing System (IELTS) Academic Module; OR | All English language test scores are considered valid for two years after the date of the test. | Remarks: Only tests taken at a test centre and scores in one single attempt are accepted.",
            "url": URL_ADM_REQ,
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Exempt from IELTS/TOEFL if the applicant holds (or will obtain) a degree for which English was the language of instruction at a recognised university, verified by an official transcript or institutional testimonial.",
            "quote": "The requirements for those who do not have a degree for which English was the language of instruction at a recognised university are: | An overall score of at least 6.5 in the International English Language Testing System (IELTS) Academic Module; OR",
            "url": URL_ADM_REQ,
            "also": [
                {
                    "quote": "Applicants with a degree for which English was the language of instruction at a recognised university are regarded as meeting the English language requirements.",
                    "url": URL_FAQ,
                }
            ],
        },
    },
    "notes": "PolyU Graduate School (GS) administers PhD (3-year full-time with research master's/MPhil; 4-year full-time with taught master's or First-Class Honours bachelor's) and MPhil (2-year full-time) programmes across seven faculties and three schools. Effective 1 July 2026, the former Department of Applied Biology and Chemical Technology (ABCT) split into the Department of Chemistry (CHEM) and Department of Life Sciences (LS), and LSGI was retitled the Department of Land Surveying and Geospatial Science (LSGS). For 2027/28 Semester 1 (Sept 2027 Entry), applications open 1 September 2026; most STEM departments close 31 May 2027 (Department of Rehabilitation Sciences closes 30 April 2027; Department of Building Environment and Energy Engineering closes 11 April 2027; HKPFS single-round deadline is 1 December 2026). Full-time PhD funding includes the PolyU Research Postgraduate Scholarship (PRPgS) and International PhD Fellowship Scheme (IPFS) at HK$230,640/yr (rising to HK$235,920/yr after confirmation of registration) plus HK$25,000 conference grant, PolyU Presidential PhD Fellowship Scheme (PPPFS) and Kuok Group Fellowship at HK$340,800/yr + tuition waiver + HK$40,000 Year-1 / HK$20,000/yr cash award + HK$25,000 conference grant, and Hong Kong PhD Fellowship Scheme (HKPFS) with PolyU top-up at HK$344,400/yr + tuition waiver + HK$14,400/yr conference grant + cash award. 2027/28 full-time tuition is HK$47,000/yr for students with stipend (waived under HKPFS/PPPFS/Kuok/IPFS and UGC local tuition waiver scheme) or HK$99,000/yr without stipend.",
}

(STAGING_UNI / "polyu.json").write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

PROGRAMS = [
    {
        "field": "biology",
        "also_fields": [],
        "name": "PhD in Life Sciences",
        "department": "Faculty of Science — Department of Life Sciences (LS)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/ls",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | To better reflect our evolving research strengths and foster specialised academic growth, the Department of Applied Biology and Chemical Technology (ABCT) has been restructured into two new departments—the Department of Chemistry (CHEM) and the Department of Life Sciences (LS) from 1 July 2026.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Life Sciences (LS) | 31 May 2027",
        "notes": "Established 1 July 2026 from the restructuring of the former Department of Applied Biology and Chemical Technology (ABCT). Covers five research pillars: Computational Biology and AI-enhanced Drug Discovery and Disease Prediction; Disease Elucidation with Advanced Molecular and Chemical Biology; Advanced Biotherapeutics; Cancer Immunotherapy and Vaccine Development; and Structural Biology.",
    },
    {
        "field": "biomed",
        "also_fields": [],
        "name": "PhD in Health Technology and Informatics",
        "department": "Faculty of Health and Social Sciences — Department of Health Technology and Informatics (HTI)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/hti",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | The Department of Health Technology and Informatics offers opportunities for research studies leading to Doctor of Philosophy (PhD) and Master of Philosophy (MPhil) degrees in the following focused research areas.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Health Technology and Informatics (HTI) | 31 May 2027",
        "sup_also": {
            "quote": "A standard form must be used for the submission of a research proposal. Please click here to download the form. | Please indicate your proposed Chief Supervisor in your research proposal.",
            "url": "https://www.polyu.edu.hk/study/pg/rpg/2027/hti",
        },
        "notes": "Covers biomedical and clinical laboratory sciences across Diabetes and Metabolic Diseases: From Pathogenesis to Therapy, Immunometabolism, Intelligent Medical Imaging in Disease Diagnosis and Prognosis Assessment, Microbiology and Antimicrobial Resistance in One Health, Neuroimaging and Neuropathology, and Precision Diagnostics and Therapeutics.",
    },
    {
        "field": "bme",
        "also_fields": [],
        "name": "PhD in Biomedical Engineering and Sports Technology",
        "department": "Faculty of Engineering — Department of Biomedical Engineering and Sports Technology (BEST)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/best",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | The Department of Biomedical Engineering and Sports Technology (BEST) 生物醫學工程及體育科技學系 | (previously known as the Department of Biomedical Engineering (BME) 生物醫學工程學系)",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Biomedical Engineering and Sports Technology (BEST) | 31 May 2027",
        "notes": "Covers six thematic research areas: Biomedical Imaging, Sensing, AI and Wearable Technology; Brain-Machine Interface and Neural Engineering; Molecular/Cellular Engineering and Biomaterials; Precision Diagnostics and Therapy; Prosthetics-Orthotics, Smart Ageing and Rehabilitation Engineering; and Sports Science and Technology.",
    },
    {
        "field": "chemeng",
        "also_fields": [],
        "name": "PhD in Chemical Technology, Catalysis and Energy Conversion",
        "department": "Faculty of Science — Department of Chemistry (CHEM, formerly Department of Applied Biology and Chemical Technology)",
        "program_page": "https://www.polyu.edu.hk/chem/study/research-postgraduate-programme/research-postgraduate-programme/",
        "deadline_code": "2027-05-31",
        "deadline_url": URL_DEADLINES,
        "deadline_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Chemistry (CHEM) | 31 May 2027",
        "entry_also": {
            "quote": "PhD (3-year full-time/ 6-year part-time) | Normally hold an MPhil or equivalent (a research postgraduate degree with a dissertation as an award requirement) and a Bachelor’s degree, conferred by a recognised university. | PhD (4-year full-time/ 8-year part-time) | A Master’s degree and a Bachelor’s degree, conferred by a recognised university; OR | A Bachelor’s degree with First Class Honours (or equivalent qualification), conferred by a recognised university.",
            "url": "https://www.polyu.edu.hk/chem/study/research-postgraduate-programme/research-postgraduate-programme/",
        },
        "notes": "Housed in the Department of Chemistry (restructured on 1 July 2026 from the former Department of Applied Biology and Chemical Technology, ABCT), covering chemical technology, AI-driven green chemistry and catalysis, energy storage and conversion technologies, macromolecular sciences, and advanced nanomaterials (alongside Research Centre for Carbon-Strategic Catalysis).",
    },
    {
        "field": "chemistry",
        "also_fields": [],
        "name": "PhD in Chemistry",
        "department": "Faculty of Science — Department of Chemistry (CHEM)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/chem",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | Driven by the global mandate for sustainability, CHEM channels its cutting-edge research capacity into six strategic pillars: Advanced Nanomaterials, AI-driven Green Chemistry and Catalysis, Macromolecular Sciences, Chemical Sensors and Imaging, Energy Storage and Conversion Technologies, and Photonic and Optoelectronic Materials.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Chemistry (CHEM) | 31 May 2027",
        "notes": "Established 1 July 2026 from the restructuring of the Department of Applied Biology and Chemical Technology (ABCT). Focuses on Advanced Nanomaterials, AI-driven Green Chemistry and Catalysis, Macromolecular Sciences, Chemical Sensors and Imaging, Energy Storage and Conversion Technologies, and Photonic and Optoelectronic Materials.",
    },
    {
        "field": "civil",
        "also_fields": [],
        "name": "PhD in Civil and Environmental Engineering",
        "department": "Faculty of Construction and Environment — Department of Civil and Environmental Engineering (CEE)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/cee",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | The Research Postgraduate Programmes offered by CEE are a combination of coursework and independent research leading to the degree of Master of Philosophy (MPhil) and Doctor of Philosophy (PhD).",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Civil and Environmental Engineering (CEE) | 31 May 2027",
        "sup_also": {
            "quote": "All research postgraduate applicants are strongly encouraged to contact potential supervisors and, preferably, list their prospective supervisor's name on their application.",
            "url": "https://www.polyu.edu.hk/study/pg/rpg/2027/cee",
        },
        "notes": "Principal research areas in CEE include Structural Engineering, Geotechnical Engineering, Coastal & Hydraulic Engineering, Construction & Transportation, and Environmental Engineering & Science.",
    },
    {
        "field": "cs",
        "also_fields": [],
        "name": "PhD in Computing",
        "department": "Faculty of Computer and Mathematical Sciences — Department of Computing (COMP)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/comp",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | The Department of Computing has established a solid foundation in Algorithm and Theory, Machine Learning and Artificial Intelligence, Big Data Analytics, Cyber Security and Privacy, Networking and Mobile Computing, and System Modelling and Software Engineering.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Computing (COMP) | 31 May 2027",
        "fund_also": {
            "quote": "Excellent Remuneration Package | A scholarship for at least three years with an annual stipend of HK$235,920 and financial support to attend international top conferences for paper presentations.",
            "url": "https://www.polyu.edu.hk/comp/study/research-postgraduate-programme/phd-and-mphil-in-computing/",
        },
        "notes": "Department of Computing sits in the Faculty of Computer and Mathematical Sciences (FCMS). Research groups cover Artificial Intelligence and Big Data Computing; Blockchain, Cyber Security and Privacy; Graphics, Multimedia and Virtual Reality; Networking and Mobile Computing; Pattern Recognition and Natural Language Processing; and Systems Modelling and Software Engineering.",
    },
    {
        "field": "datasci",
        "also_fields": [],
        "name": "PhD in Data Science and Artificial Intelligence",
        "department": "Faculty of Computer and Mathematical Sciences — Department of Data Science and Artificial Intelligence (DSAI)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/dsai",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | To position The Hong Kong Polytechnic University (PolyU) as a leader in the said fields, the Department of Data Science and Artificial Intelligence (DSAI) was officially established in July 2024.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Data Science and Artificial Intelligence (DSAI) | 31 May 2027",
        "notes": "Established in July 2024 within the Faculty of Computer and Mathematical Sciences (FCMS). Covers Machine Learning, Biometrics and Human Language Processing, Computer Vision and Graphics, Data Technologies and Governance, Statistical Learning and Optimization Methods, and AI + X (Science, Healthcare, Neuroscience).",
    },
    {
        "field": "earth",
        "also_fields": [],
        "name": "PhD in Land Surveying and Geospatial Science",
        "department": "Faculty of Construction and Environment — Department of Land Surveying and Geospatial Science (LSGS)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/lsgs",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | Established in 1982, the Department of Land Surveying and Geospatial Science (LSGS), retitled from the Department of Land Surveying and Geo-Informatics in July 2026, is the only academic unit amongst the local tertiary institutions offering a range of opportunities for education, training and research in the fields of Land Surveying and Geospatial Science.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Land Surveying and Geo-Informatics (LSGI) | 31 May 2027",
        "notes": "Retitled in July 2026 from the Department of Land Surveying and Geo-Informatics (LSGI). Covers Geodesy and Geodynamics (physical/satellite geodesy, geophysics, geodynamics, climate change, InSAR, crustal deformation, sea-level change), Photogrammetry and Remote Sensing (including planetary mapping and Earth observations), GIS, Hydrographic Survey, and Urban Informatics.",
    },
    {
        "field": "ece",
        "also_fields": [],
        "name": "PhD in Electrical and Electronic Engineering",
        "department": "Faculty of Engineering — Department of Electrical and Electronic Engineering (EEE)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/eee",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | Applications are now invited for registration in our programme leading to the Degree of Doctor of Philosophy (PhD)/Master of Philosophy (MPhil) by research in EEE.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Electrical and Electronic Engineering (EEE) | 31 May 2027",
        "notes": "Covers six major research areas: Artificial Intelligence, Robotics and Materials Engineering; Communications and Information Security; Electric Vehicles and Smart Mobility; Microelectronics and Quantum Technology; Photonics and Smart Devices; and Power and Energy Systems.",
    },
    {
        "field": "environment",
        "also_fields": [],
        "name": "PhD in Environmental Engineering and Science",
        "department": "Faculty of Construction and Environment — Department of Civil and Environmental Engineering (CEE)",
        "program_page": "https://www.polyu.edu.hk/cee/prospective-students/research-postgraduate-programme/",
        "deadline_code": "2027-05-31",
        "deadline_url": URL_DEADLINES,
        "deadline_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Civil and Environmental Engineering (CEE) | 31 May 2027",
        "sup_also": {
            "quote": "Prospective students are advised to look up the Major Research Areas of CEE Staff to have a feel of the research focuses of individual academic staff members and contact them for more details before they apply.",
            "url": "https://www.polyu.edu.hk/cee/prospective-students/research-postgraduate-programme/",
        },
        "fund_also": {
            "quote": "Full-time research students are normally offered a stipend.",
            "url": "https://www.polyu.edu.hk/cee/prospective-students/research-postgraduate-programme/",
        },
        "entry_also": {
            "quote": "The Department admits both MPhil and PhD students. The normal duration of study for an MPhil degree is two years and for a PhD degree is three years for students with an MPhil or equivalent (a research postgraduate degree with a dissertation as an award requirement) or four years for those with a Master’s degree or a Bachelor’s degree with First Class Honours (or equivalent qualification).",
            "url": "https://www.polyu.edu.hk/cee/prospective-students/research-postgraduate-programme/",
        },
        "notes": "Environmental Engineering & Science is a core PhD research division within the Department of Civil and Environmental Engineering (CEE, deadline 31 May 2027), alongside the CAS GIG-PolyU Guangdong-Hong Kong-Macao Joint Laboratory for Environmental Pollution and Control and Research Centre for Resources Engineering towards Carbon Neutrality. PolyU also offers a separate PhD in the Department of Building Environment and Energy Engineering (BEEE, `/study/pg/rpg/2027/beee`, deadline 11 April 2027).",
    },
    {
        "field": "materials",
        "also_fields": [],
        "name": "PhD in Physics and Materials (Materials Science and Nanomaterials)",
        "department": "Faculty of Science — Department of Physics and Materials (PM)",
        "program_page": "https://www.polyu.edu.hk/pm/study/rpg-prog/",
        "deadline_code": "2027-05-31",
        "deadline_url": URL_DEADLINES,
        "deadline_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Physics and Materials (PM) | 31 May 2027",
        "notes": "Housed in the Department of Physics and Materials (PM, Programme Code 11601), covering Nanomaterials & Micro/Nanoelectronics, Green Energy & Carbon Neutrality (batteries, ferroelectric/dielectric and photovoltaic materials), and Photonics, Plasmonics & Optoelectronics.",
    },
    {
        "field": "math",
        "also_fields": [],
        "name": "PhD in Applied Mathematics",
        "department": "Faculty of Computer and Mathematical Sciences — Department of Applied Mathematics (AMA)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/ama",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | CAS AMSS-POLYU Joint Laboratory of Applied Mathematics",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Applied Mathematics (AMA) | 31 May 2027",
        "gre_subj": {
            "code": "Not required",
            "value": "GRE Subject Test in Mathematics is not required; Department of Applied Mathematics supporting documents list only two academic referee reports, CV, personal statement, research proposal, and transcripts/certificates.",
            "quote": "GMAT or GRE results are required. | Department of Applied Mathematics | Academic Referee's Report | Compulsory - Two Academic Referee's Reports are required. | Curriculum Vitae | Personal Statement | Research Proposal | Transcript / Certificate",
            "url": URL_SUPP_DOCS,
        },
        "notes": "Covers Applied Optimisation and Optimal Control, Engineering and Computational Mathematics, Differential Equations, Financial Mathematics, and Operations Research within the Faculty of Computer and Mathematical Sciences (FCMS).",
    },
    {
        "field": "mech",
        "also_fields": [],
        "name": "PhD in Mechanical Engineering",
        "department": "Faculty of Engineering — Department of Mechanical Engineering (ME)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/me",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | As one of the founding departments of the University in 1937, the Department of Mechanical Engineering has been at the forefront of the vast evolvement of its field.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Mechanical Engineering (ME) | 31 May 2027",
        "sup_also": {
            "quote": "Please refer to the Department webpage for the information on the potential supervisors. | You are advised to contact the potential supervisors before submitting an application.",
            "url": "https://www.polyu.edu.hk/study/pg/rpg/2027/me",
        },
        "notes": "Covers Aerospace Engineering, Energy and Environment, Manufacturing, Materials and Mechanics, Robotics and Control, Sound and Vibration, and Thermofluids and Combustion. PolyU also offers a separate PhD in the Department of Aeronautical and Aviation Engineering (`/study/pg/rpg/2027/aae`) and Department of Industrial and Systems Engineering (`/study/pg/rpg/2027/ise`), both closing 31 May 2027.",
    },
    {
        "field": "neuro",
        "also_fields": [],
        "name": "PhD in Rehabilitation Sciences (Translational Neuroscience)",
        "department": "Faculty of Health and Social Sciences — Department of Rehabilitation Sciences (RS)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/rs",
        "deadline_code": "2027-04-30",
        "deadline_quote": "PhD & MPhil | 30-Apr-2027 | Research Area | Translational Research in Neuroscience | Translational Research in Musculoskeletal and Sports Science",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Rehabilitation Sciences (RS) | 30 Apr 2027",
        "gre_subj": {
            "code": "Not required",
            "value": "GRE Subject Test in Psychology is not required; Department of Rehabilitation Sciences supporting documents require only transcripts/certificates, two academic referee reports, CV, research proposal, and vision statement.",
            "quote": "GMAT or GRE results are required. | Department of Rehabilitation Sciences | Transcript / Certificate | Academic Referee's Report | Curriculum Vitae | Research Proposal | Personal Statement",
            "url": URL_SUPP_DOCS,
        },
        "sup_also": {
            "quote": "In the case that a candidate who does not have a research topic or supervisor in mind at the time of application, the candidate may still be considered for admission into our RPg programme and the student has up to 2 months after admission to propose a Chief Supervisor and research topic to the chairman of DRC.",
            "url": "https://www.polyu.edu.hk/rs/study/research-postgraduate-studies/phd-or-mphil/",
        },
        "notes": "Translational Research in Neuroscience is a flagship research pillar in the Department of Rehabilitation Sciences (alongside the University Research Facility in Behavioral and Systems Neuroscience and Research Centre for Non-invasive Brain Computer Interface in BEST). Note the earlier departmental deadline of 30 April 2027 for September 2027 entry.",
    },
    {
        "field": "physics",
        "also_fields": [],
        "name": "PhD in Physics and Materials",
        "department": "Faculty of Science — Department of Physics and Materials (PM)",
        "program_page": "https://www.polyu.edu.hk/study/pg/rpg/2027/pm",
        "deadline_code": "2027-05-31",
        "deadline_quote": "PhD & MPhil | 31-May-2027 | The Department of Physics and Materials (PM) focuses on five research areas: (1) Green Energy & Carbon Neutrality, (2) Machine Learning & Computational Physics, (3) Nanomaterials & Micro/Nanoelectronics, (4) Photonics, Plasmonics & Optoelectronics, and (5) Quantum Physics & Devices.",
        "deadline_also_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Physics and Materials (PM) | 31 May 2027",
        "gre_subj": {
            "code": "Not required",
            "value": "GRE Subject Test in Physics is not required; Department of Physics and Materials supporting documents require only two academic referee reports, CV, personal statement, research proposal, and transcripts/certificates.",
            "quote": "GMAT or GRE results are required. | Department of Physics and Materials | Academic Referee's Report | Curriculum Vitae | Personal Statement | Research Proposal | Transcript / Certificate",
            "url": URL_SUPP_DOCS,
        },
        "notes": "Covers Machine Learning & Computational Physics, Quantum Physics & Devices, Photonics, Plasmonics & Optoelectronics, Nanomaterials & Micro/Nanoelectronics, and Green Energy & Carbon Neutrality.",
    },
    {
        "field": "statistics",
        "also_fields": [],
        "name": "PhD in Applied Mathematics (Applied Statistics)",
        "department": "Faculty of Computer and Mathematical Sciences — Department of Applied Mathematics (AMA)",
        "program_page": "https://www.polyu.edu.hk/ama/study/research-postgraduate-programme/",
        "deadline_code": "2027-05-31",
        "deadline_url": URL_DEADLINES,
        "deadline_quote": "2027/28 | Semester One | (Sep 2027 Entry) | Department of Applied Mathematics (AMA) | 31 May 2027",
        "fund_also": {
            "quote": "PolyU offers Research Studentships to full-time PhD or MPhil students. The Studentship is a scholarship intended to be a means of financial support to allow full-time research students to fully focus on their studies. It shall be awarded on the basis of academic merit.",
            "url": "https://www.polyu.edu.hk/ama/study/research-postgraduate-programme/",
        },
        "entry_also": {
            "quote": "3-year full-time / 6-year part-time PhD programme | normally hold an MPhil or equivalent (a research postgraduate degree with a dissertation as an award requirement) and a Bachelor’s degree, conferred by a recognised university | 4-year full-time / 8-year part-time PhD programme | A Master’s degree and a Bachelor’s degree, conferred by a recognised university; OR | A Bachelor’s degree with First Class Honours (or equivalent qualification), conferred by a recognised university.",
            "url": "https://www.polyu.edu.hk/ama/study/research-postgraduate-programme/",
        },
        "notes": "Applied Statistics is one of five core MPhil/PhD research areas in the Department of Applied Mathematics (AMA), covering Biostatistics, High-dimensional Data Analysis, Network Analysis, Statistical Learning, Survival Analysis, Time Series Analysis, and Data Science.",
    },
]

for p in PROGRAMS:
    fid = p["field"]
    d_url = p.get("deadline_url", p["program_page"])
    d_field = {
        "code": p["deadline_code"],
        "value": f"2027/28 Semester One (September 2027 entry) application deadline is {p['deadline_code']} (31 May 2027 for most STEM departments; 30 April 2027 for Rehabilitation Sciences; HKPFS single-round deadline is 1 December 2026).",
        "quote": p["deadline_quote"],
        "url": d_url,
        "time_sensitive": p["deadline_code"],
    }
    if "deadline_also_quote" in p:
        d_field["also"] = [{"quote": p["deadline_also_quote"], "url": URL_DEADLINES}]

    if "gre_subj" in p:
        gre_s = p["gre_subj"]
    else:
        gre_s = {
            "code": "No subject test",
            "value": "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology; no GRE Subject Test exists for this discipline.",
            "quote": "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
            "url": URL_ETS_SUBJ,
        }

    sup_field = {
        "code": "Recommended",
        "value": "Applicants are advised to contact a potential supervisor before submitting an application, though an application can still be submitted without identifying a supervisor in advance.",
        "quote": "17. Do I need to contact a supervisor in advance before applying? | Applicants are advised to contact a potential supervisor before submission of an application. However, you can still submit an application without identifying a potential supervisor.",
        "url": URL_FAQ,
    }
    if "sup_also" in p:
        sup_field["also"] = [p["sup_also"]]

    fund_field = {
        "code": "Competitive",
        "value": "Full-time PhD applicants are automatically considered for the PolyU Research Postgraduate Scholarship (PRPgS: HK$230,640/yr, rising to HK$235,920/yr after confirmation of registration, plus HK$25,000 conference grant), International PhD Fellowship Scheme (IPFS: HK$230,640–235,920/yr + tuition waiver), PolyU Presidential PhD Fellowship (PPPFS: HK$340,800/yr + tuition waiver), and HKPFS (HK$344,400/yr + tuition waiver).",
        "quote": "PolyU Research Postgraduate Scholarship (PRPgS) | PRPgS aims to provide financial support to PhD and MPhil students during their normal study period, allowing them to fully focus on their studies. Applicants will concurrently be considered for the PRPgS once they submit an application via RPgAdmission, no separate application is required. The PRPgS package includes: | Annual Stipend: HK$230,640 | HK$235,920 for PhD students who have confirmed registration",
        "url": URL_FELLOWSHIPS,
    }
    if "fund_also" in p:
        fund_field["also"] = [p["fund_also"]]

    entry_field = {
        "code": "Either",
        "value": "Admits applicants with a Bachelor's degree with First Class Honours or a Master's degree into the 4-year full-time PhD programme, and applicants with an MPhil or research Master's degree (with dissertation) into the 3-year full-time PhD programme.",
        "quote": "Doctor of Philosophy (PhD) | (3-year full-time/6-year part-time) | normally hold a Master of Philosophy (MPhil) or equivalent (a research postgraduate degree with a dissertation as an award requirement) and a Bachelor's degree, conferred by a recognised university | Doctor of Philosophy (PhD) | (4-year full-time/8-year part-time) | A Master’s degree and a Bachelor's degree, conferred by a recognised university; OR | A Bachelor’s degree with First Class Honours (or equivalent qualification), conferred by a recognised university.",
        "url": URL_ADM_REQ,
    }
    if "entry_also" in p:
        entry_field["also"] = [p["entry_also"]]

    rec = {
        "id": f"polyu--{fid}",
        "university": "polyu",
        "field": fid,
        "also_fields": p["also_fields"],
        "name": p["name"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": CHECKED,
        "fields": {
            "deadline": d_field,
            "gre_subject": gre_s,
            "supervisor": sup_field,
            "funding": fund_field,
            "entry_route": entry_field,
        },
        "notes": p["notes"],
    }
    (STAGING_PROG / f"polyu--{fid}.json").write_text(
        json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

print(f"Wrote polyu.json and {len(PROGRAMS)} programs to data/staging/")
