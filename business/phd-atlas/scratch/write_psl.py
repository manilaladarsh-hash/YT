import json
import os
from pathlib import Path

OUT = Path(os.environ.get("ATLAS_OUT", "data/staging"))
UNIS = OUT / "universities"
PROGS = OUT / "programs"
UNIS.mkdir(parents=True, exist_ok=True)
PROGS.mkdir(parents=True, exist_ok=True)

CHECKED = "2026-11-14"

COLLEGE_URL = "https://psl.eu/en/education/find-your-curriculum/doctoral-college-universite-psl"
FAQ_URL = "https://psl.eu/en/education/find-your-curriculum/phd-track/psl-phd-track-faq"
FINAID_URL = "https://psl.eu/en/lifepsl/campus-life-paris/financial-aids"
MINES_URL = "https://www.minesparis.psl.eu/formations/doctorat/"
ISMME_URL = "https://www.minesparis.psl.eu/ismme/"
ISMME_ADM_URL = "https://www.minesparis.psl.eu/ismme/la-vie-de-lecole-doctorale/sujets-de-these-candidatures-et-recrutement/"
CHIMIE_PHD_URL = "https://www.chimieparistech.psl.eu/en/program/phd/"
CHIMIE_ADM_URL = "https://www.chimieparistech.psl.eu/en/admissions/phd-admissions/"
EPHE_URL = "https://www.ephe.psl.eu/formations-conferences/doctorat"
DAUPHINE_ADM_URL = "https://ecole-doctorale.dauphine.psl.eu/candidature/1ere-annee-de-these"
DAUPHINE_INFO_URL = "https://ecole-doctorale.dauphine.psl.eu/programmes-doctoraux/informatique"
DAUPHINE_MATH_URL = "https://ecole-doctorale.dauphine.psl.eu/programmes-doctoraux/mathematique"
OBSPM_ED_URL = "https://ecole-doctorale.obspm.fr"
CURIE_URL = "https://enseignement.curie.fr/article/faire-son-doctorat"
STIC_URL = "https://webusers.i3s.unice.fr/edstic/index-en.php"

GP_ASTRO = "https://psl.eu/en/graduate-programs/astrophysics"
GP_PHYS = "https://psl.eu/en/graduate-programs/physics"
GP_CHEM = "https://psl.eu/en/graduate-programs/chemistry"
GP_CS = "https://psl.eu/en/graduate-programs/computer-science"
GP_DATA = "https://psl.eu/en/programmes-gradues/programme-data"
GP_MATH = "https://psl.eu/en/graduate-programs/mathematics-and-applications"
GP_ISAI = "https://psl.eu/en/graduate-programs/engineering-isai"
GP_EARTH = "https://psl.eu/en/graduate-programs/earth-science-and-biodiversity"
GP_LIFE = "https://psl.eu/en/graduate-programs/life-sciences"
DS_LIFE = "https://psl.eu/en/research/doctoral-studies-and-postdoctoral-fellowships/college-doctoral/life-sciences-ds"
DS_COG = "https://psl.eu/en/research/doctoral-studies-and-postdoctoral-fellowships/college-doctoral/ed-cognitive-science"

ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_SUBJ_Q = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ETS_SCORES = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"
ETS_BIO_Q = "The GRE Biology Test and the GRE Literature in English Test were discontinued in May 2021."
ETS_CHEM_Q = "The GRE Chemistry Test was discontinued in May 2023."

uni = {
    "id": "psl",
    "institution": "Université PSL",
    "country": "France",
    "region": "Île-de-France",
    "grad_page": COLLEGE_URL,
    "checked": CHECKED,
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "No doctoral application fee is stated on PSL's Doctoral College, ADUM, or component-school PhD admission pages; annual national doctoral registration fees are €398/year (2026/27 rate, all nationalities) plus the ~€105/year CVEC campus contribution.",
            "quote": "",
            "url": COLLEGE_URL,
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "Not stated on the page checked (several exemptions exist for the annual CVEC campus tax).",
            "quote": "",
            "url": COLLEGE_URL,
        },
        "gre_general": {
            "code": "Not stated",
            "value": "Not stated on the page checked; no GRE General requirement is published across PSL's Doctoral College or component-school PhD pages.",
            "quote": "",
            "url": COLLEGE_URL,
        },
        "toefl_min": {
            "code": "Not stated",
            "value": "No university-wide TOEFL minimum is stated on PSL's Doctoral College or constituent-school PhD admission pages; specific doctoral schools set their own language checks (e.g. ED 621 ISMME requires CEFR B2 English; the separate 5-year Bachelor-entry PhD Track recommends C1 English).",
            "quote": "",
            "url": COLLEGE_URL,
        },
        "ielts_min": {
            "code": "Not stated",
            "value": "No university-wide IELTS minimum is stated on PSL's Doctoral College or constituent-school PhD admission pages (the separate 5-year Bachelor-entry PhD Track recommends C1 English, with official TOEFL/IELTS scores optional when not from an English-speaking university).",
            "quote": "",
            "url": COLLEGE_URL,
        },
        "english_waiver": {
            "code": "Not stated",
            "value": "No university-wide English-test exemption rule is stated for standard 3-year PhD enrollment; for the separate 5-year Bachelor-entry PhD Track, applicants whose first language is English or who earned a degree at an English-speaking university include a statement rather than TOEFL/IELTS scores.",
            "quote": "",
            "url": FAQ_URL,
        },
    },
    "notes": (
        "Université PSL's Collège Doctoral federates 30 accredited and co-accredited doctoral schools and 15 thesis-preparation component institutions "
        "(including ENS - PSL, Mines Paris - PSL, Chimie ParisTech - PSL, ESPCI Paris - PSL, Paris Dauphine - PSL, Observatoire de Paris - PSL, EPHE - PSL, Collège de France, and Institut Curie), "
        "all conferring the Doctorat de l'Université PSL with online registration via ADUM (https://adum.fr/index.pl?site=PSL). "
        "Annual registration fees for 2026/27 are €398/year (all nationalities) plus ~€105/year CVEC (https://psl.eu/en/lifepsl/campus-life-paris/financial-aids). "
        "Beside the standard 3-year PhD (Master's required, supervisor agreement and funding secured prior to enrollment), PSL also runs selective 5-year Bachelor-entry English-taught PhD Tracks "
        "(2026 call October 14 - December 14, 2026; €10,000/yr Master's grant followed by a doctoral contract; C1 English recommended; https://psl.eu/en/education/find-your-curriculum/phd-track/psl-phd-track-faq). "
        "Unreachable/error external ED URLs during verification: edpif.org (timeout), ed386.upmc.fr / ed397.upmc.fr / ed398.sorbonne-universite.fr (SSL cert errors), collegedoctoral.psl.eu / phys.ens.psl.eu (502), dauphine.psl.eu/en/training/doctorate & espci.psl.eu/en/education/phd-studies/ & ed129.sorbonne-universite.fr (404)."
    ),
}

(UNIS / "psl.json").write_text(json.dumps(uni, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

SUP_Q = "Before enrolling in the program, doctoral students must obtain approval from their dissertation advisor and be admitted to a research unit or team that belongs to a PSL-accredited or co-accredited doctoral school."
FUND_Q = "Each graduate program assigns doctoral contracts to doctoral schools accredited or co-accredited by Université PSL and affiliated with the graduate program. | Doctoral school students are selected by a jury usually comprised of PSL faculty and external members."
DEADLINE_Q = "This generally takes place from September 1st until mid-December for the current year."

PROGRAMS = [
    {
        "field": "astronomy",
        "also_fields": [],
        "department": "Astrophysics Graduate Program / Astronomy and Astrophysics of the Paris Region (ED 127 AAIF)",
        "program_page": GP_ASTRO,
        "gre_subject": ("Not stated", "No GRE Subject Test requirement is stated on the Astrophysics Graduate Program or ED 127 AAIF pages.", "", GP_ASTRO),
        "entry_quote": ("Chaque année, l’Ecole doctorale accueille environ 50 nouveaux étudiants issus de Masters ou équivalent, sans condition de nationalité ni d’université d’origine.", OBSPM_ED_URL),
        "extra_sup": None,
        "extra_fund": ("Ils préparent en 3 ans et en étant rémunérés par des contrats divers, un doctorat dans des laboratoires situés en Ile-de-France ou parfois à l’étranger.", OBSPM_ED_URL),
        "notes": "Led by Observatoire de Paris - PSL and ENS - PSL through ED 127 AAIF (Astronomy and Astrophysics of Île-de-France) and ED 564 PIF. Also offers a 5-year Bachelor-entry PSL PhD Track in Astrophysics.",
    },
    {
        "field": "physics",
        "also_fields": [],
        "department": "Physics Graduate Program / Physics in the Paris Region (ED 564 PIF)",
        "program_page": GP_PHYS,
        "gre_subject": ("Not stated", "No GRE Subject Test requirement is stated on PSL's Physics Graduate Program or Doctoral College pages (ED PIF site https://www.edpif.org timed out).", "", GP_PHYS),
        "entry_quote": ("Pour être éligible en doctorat, le candidat devra démontrer qu’il détient un diplôme de master ou de niveau équivalent au moment de démarrer son doctorat.", MINES_URL),
        "extra_sup": None,
        "extra_fund": None,
        "notes": "Coordinated across ENS - PSL, ESPCI Paris - PSL, Observatoire de Paris - PSL, Institut Curie, and Collège de France through ED 564 Physics in Île-de-France (PIF). Also offers a 5-year Bachelor-entry PSL PhD Track in Physics.",
    },
    {
        "field": "chemistry",
        "also_fields": [],
        "department": "Chemistry Graduate Program (ED 388, ED 406, ED 563)",
        "program_page": GP_CHEM,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field: ETS discontinued the GRE Chemistry Test in May 2023.", ETS_CHEM_Q, ETS_SCORES),
        "entry_quote": ("Students must first hold a Master’s 2 and have the agreement of the PhD school and of the thesis director to register their thesis with Chimie ParisTech - PSL.", CHIMIE_ADM_URL),
        "extra_sup": ("Students must first hold a Master’s 2 and have the agreement of the PhD school and of the thesis director to register their thesis with Chimie ParisTech - PSL.", CHIMIE_ADM_URL),
        "extra_fund": None,
        "notes": "Brings together Chimie ParisTech - PSL, ENS - PSL, ESPCI Paris - PSL, Institut Curie, and Collège de France across ED 388 (Physical & Analytical Chemistry, https://ed388.sorbonne-universite.fr/en), ED 406 (Molecular Chemistry, https://ed406.sorbonne-universite.fr/), and ED 563. Also offers a 5-year Bachelor-entry PSL PhD Track in Chemistry.",
    },
    {
        "field": "materials",
        "also_fields": [],
        "department": "Chimie ParisTech - PSL / Materials Science and Engineering (ED 397 & ED 621 ISMME)",
        "program_page": CHIMIE_PHD_URL,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Students must first hold a Master’s 2 and have the agreement of the PhD school and of the thesis director to register their thesis with Chimie ParisTech - PSL.", CHIMIE_ADM_URL),
        "extra_sup": ("Students must first have the agreement of the PhD school and of the thesis director to proceed with their registration.", CHIMIE_PHD_URL),
        "extra_fund": ("Of the approximately one hundred students doing their thesis at Chimie ParisTech - PSL, 25% are financed by the industry (CEA, ADEME, IFP, companies, etc.), of which 16% are under a CIFRE agreement.", CHIMIE_PHD_URL),
        "notes": "Covers Materials Chemistry, Materials Physics, and Materials Science & Engineering across Chimie ParisTech - PSL (IRCP), ESPCI Paris - PSL (SIMM, LPEM, C3M), and Mines Paris - PSL (CEMEF, CMAT) via ED 397 (Physique et Chimie des Matériaux) and ED 621 (ISMME).",
    },
    {
        "field": "mech",
        "also_fields": [],
        "department": "Engineering, Applied Sciences and Innovation (ISAI) / Mechanical & Systems Engineering (ED 621 ISMME & ED 391 SMAER)",
        "program_page": ISMME_URL,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Prérequis : pour être inscrit en doctorat, le candidat doit être titulaire d’un diplôme de l’union européenne de master ou d’un autre diplôme conférant le grade de master (diplôme d’ingénieur ou d’architecte)", ISMME_ADM_URL),
        "extra_sup": ("Pour être admis en doctorat, le candidat doit trouver un directeur de thèse habilité à diriger des recherches (HDR) avec qui il s’accorde sur un projet", ISMME_ADM_URL),
        "extra_fund": ("Toutes les sujets de thèse proposés par les laboratoires de l’École Doctorale garantissent un financement sur 3 ans du doctorant au moins égal au montant du contrat doctoral de droit public.", ISMME_ADM_URL),
        "notes": "ED 621 ISMME (Mines Paris - PSL, Chimie ParisTech - PSL) requires a Master's/engineering degree, supervisor agreement, and CEFR B2 English proficiency (oral/written check if no certificate is supplied; A2/B1 French recommended for non-French speakers) and guarantees 3-year funding on all published ED thesis offers; also connected with ED 391 SMAER (Mechanical, Acoustic, Electronic and Robotic Sciences, https://ed391.sorbonne-universite.fr/).",
    },
    {
        "field": "chemeng",
        "also_fields": [],
        "department": "Énergétique et Génie des Procédés (Mines Paris - PSL / ED 621 ISMME)",
        "program_page": MINES_URL,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Pour être éligible en doctorat, le candidat devra démontrer qu’il détient un diplôme de master ou de niveau équivalent au moment de démarrer son doctorat.", MINES_URL),
        "extra_sup": ("Pour être admis en doctorat, le candidat doit trouver un directeur de thèse habilité à diriger des recherches (HDR) avec qui il s’accorde sur un projet visant à être intégré dans une unité ou une équipe de recherche affiliée à une école doctorale accréditée ou co-accréditée par PSL.", MINES_URL),
        "extra_fund": ("Tous les doctorants sont financés pendant leur thèse. L’obtention d’un financement est indispensable pour l’inscription.", MINES_URL),
        "notes": "Doctoral specialty 'Énergétique et génie des procédés' within Mines Paris - PSL and ED 621 ISMME (30% CIFRE industry-funded theses across Mines Paris). Note ED 621 ISMME specifies CEFR B2 English proficiency (https://www.minesparis.psl.eu/ismme/la-vie-de-lecole-doctorale/sujets-de-these-candidatures-et-recrutement/).",
    },
    {
        "field": "ece",
        "also_fields": [],
        "department": "Information & Communication Sciences and Technologies / Electronics & Robotics (ED 84 STIC & ED 391 SMAER)",
        "program_page": STIC_URL,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Pour être éligible en doctorat, le candidat devra démontrer qu’il détient un diplôme de master ou de niveau équivalent au moment de démarrer son doctorat.", MINES_URL),
        "extra_sup": ("Pour être admis en doctorat, le candidat doit trouver un directeur de thèse habilité à diriger des recherches (HDR) avec qui il s’accorde sur un projet visant à être intégré dans une unité ou une équipe de recherche affiliée à une école doctorale accréditée ou co-accréditée par PSL.", MINES_URL),
        "extra_fund": ("Tous les doctorants sont financés pendant leur thèse. L’obtention d’un financement est indispensable pour l’inscription.", MINES_URL),
        "notes": "ED 84 STIC is co-accredited by Université Côte d'Azur and Université PSL (hosting Mines Paris - PSL Sophia Antipolis teams in electronics, automatic control, robotics, signal/image processing, and computing), alongside Paris-based ED 391 SMAER (Sciences Mécaniques, Acoustique, Électronique et Robotique).",
    },
    {
        "field": "cs",
        "also_fields": [],
        "department": "Computer Science Graduate Program (ED 386 & ED 543 SDOSE)",
        "program_page": GP_CS,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Diplôme de Master et relevés de notes (si le M2 est en cours, fournir les notes à disposition du candidat)", DAUPHINE_ADM_URL),
        "extra_sup": ("Pour effectuer une thèse, il faut impérativement obtenir l'accord d'un membre habilité à diriger des recherches.", DAUPHINE_INFO_URL),
        "extra_fund": ("Justificatif de financement de la thèse ou preuve de dépôt d’une demande de financement (sauf pour les candidatures aux contrats doctoraux de l’ED SDOSE)", DAUPHINE_ADM_URL),
        "notes": "Unites ENS - PSL (DI ENS UMR 8548 via ED 386) and Paris Dauphine - PSL (LAMSADE UMR 7243 via ED 543 SDOSE), plus the PRAIRIE AI institute and PSAI. Also offers a 5-year Bachelor-entry PSL PhD Track in Computer Science.",
    },
    {
        "field": "datasci",
        "also_fields": [],
        "department": "PSL DATA Program / Artificial Intelligence & Data Science (ED 543 SDOSE, ED 386, AI4theSciences)",
        "program_page": GP_DATA,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Diplôme de Master et relevés de notes (si le M2 est en cours, fournir les notes à disposition du candidat)", DAUPHINE_ADM_URL),
        "extra_sup": ("Avant de candidater, il est essentiel de : Obtenir l’accord d’un directeur ou d’une directrice de thèse | Trouver un financement pour votre thèse", DAUPHINE_ADM_URL),
        "extra_fund": ("Launched in 2020, this six-year programme will fund 26 doctoral contracts at the interface of artificial intelligence and massive data processing over three cohorts.", COLLEGE_URL),
        "notes": "Covers doctoral research in AI, Machine Learning, and Data Science through Dauphine-PSL LAMSADE ('Sciences des Données; Intelligence artificielle, apprentissage automatique, apprentissage profond' on ED 543 SDOSE), ENS-PSL, and Mines Paris-PSL (COFUND AI4theSciences & Paris School of AI).",
    },
    {
        "field": "math",
        "also_fields": ["statistics"],
        "department": "Mathematics and Applications Graduate Program (ED 386, ED 543 SDOSE CEREMADE, ED 574 EDMH)",
        "program_page": GP_MATH,
        "gre_subject": ("Not stated", "No GRE Subject Test requirement is stated on PSL's Mathematics Graduate Program or SDOSE Mathematics pages.", "", GP_MATH),
        "entry_quote": ("Diplôme de Master et relevés de notes (si le M2 est en cours, fournir les notes à disposition du candidat)", DAUPHINE_ADM_URL),
        "extra_sup": ("Pour effectuer une thèse, il faut impérativement obtenir l'accord d'un membre habilité à diriger des recherches.", DAUPHINE_MATH_URL),
        "extra_fund": ("Le contrat doctoral public | Financement sur 3 ans assuré par un établissement public.", DAUPHINE_MATH_URL),
        "notes": "Includes fundamental/applied mathematics, probability, and statistics (Dauphine-PSL CEREMADE Groupe Probabilités et statistiques, ENS-PSL DMA, Mines Paris-PSL CAS, and Observatoire IMCCE) across ED 386, ED 543 SDOSE, ED 574 EDMH, and ED 127. Covers the Atlas 'statistics' field via CEREMADE's Probability & Statistics and Statistical & Financial Engineering tracks.",
    },
    {
        "field": "biology",
        "also_fields": [],
        "department": "Life Sciences Doctoral School (ED 657 SdV) & Complexity of Life (ED 515)",
        "program_page": DS_LIFE,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field: ETS discontinued the GRE Biology Test in May 2021.", ETS_BIO_Q, ETS_SCORES),
        "entry_quote": ("Les candidats titulaires d'un master recherche ou d'un diplôme de niveau équivalent sont admis à préparer un doctorat, après avis favorable de la commission compétente.", EPHE_URL),
        "extra_sup": None,
        "extra_fund": ("The DS's mission is to evaluate students from French and foreign universities wishing to undertake a thesis at Université PSL; to award doctoral contracts through a jury of excellence", DS_LIFE),
        "notes": "Led by Université PSL via ED 657 Life Sciences (Collège de France CIRB, ENS-PSL IBENS, ESPCI Paris-PSL, Institut Curie) alongside co-accredited ED 515 (Complexité du Vivant, https://ed515.sorbonne-universite.fr/en/ed-515) and ED 472 (EPHE-PSL).",
    },
    {
        "field": "biomed",
        "also_fields": ["bme"],
        "department": "Life Sciences & ISAI BioMedical Engineering / Oncology & Health Doctoral Schools (ED 561, ED 562, ED 563, ED 582, Institut Curie)",
        "program_page": GP_LIFE,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Students must first hold a Master’s 2 and have the agreement of the PhD school and of the thesis director to register their thesis with Chimie ParisTech - PSL.", CHIMIE_ADM_URL),
        "extra_sup": None,
        "extra_fund": None,
        "notes": "Covers biomedical sciences, oncology, immunology, pharmacology, and biomedical engineering ('Engineering for Health', 'Biology for Health', Physics for Medicine at ESPCI, and Master/PhD Track ST4Health shared with Engineering ISAI GP at https://psl.eu/en/graduate-programs/engineering-isai) across Institut Curie (IC-PhD, https://enseignement.curie.fr/article/faire-son-doctorat), ED 561 HOB (https://ed561.u-paris.fr/), ED 562, ED 563 MTCI, and ED 582. Also offers a 5-year Bachelor-entry PSL PhD Track in Life Sciences.",
    },
    {
        "field": "neuro",
        "also_fields": [],
        "department": "Cognitive Sciences Doctoral School (EDSC) & Brain, Cognition, Behavior (ED 158 ED3C)",
        "program_page": DS_COG,
        "gre_subject": ("Not stated", "No GRE Subject Test requirement is stated on PSL's Cognitive Science Doctoral School, Cognitive Sciences GP, or ED 158 pages.", "", DS_COG),
        "entry_quote": ("Les candidats titulaires d'un master recherche ou d'un diplôme de niveau équivalent sont admis à préparer un doctorat, après avis favorable de la commission compétente.", EPHE_URL),
        "extra_sup": None,
        "extra_fund": None,
        "notes": "Led by ENS - PSL Department of Cognitive Studies (LNC2, LSP, LSCP, IJN) through PSL's EDSC alongside co-accredited ED 158 ED3C (Brain, Cognition, Behavior, https://ed3c.sorbonne-universite.fr/) and IBENS/CIRB/ESPCI Brain Plasticity neuroscience units.",
    },
    {
        "field": "earth",
        "also_fields": [],
        "department": "Earth Science and Biodiversity Graduate Program (ED 398 GRNE & ED 560 STEP'UP)",
        "program_page": GP_EARTH,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Pour être éligible en doctorat, le candidat devra démontrer qu’il détient un diplôme de master ou de niveau équivalent au moment de démarrer son doctorat.", MINES_URL),
        "extra_sup": None,
        "extra_fund": None,
        "notes": "Spans ENS - PSL (Geology Lab, LMD Meteorology), Mines Paris - PSL (Centre de Géosciences), and EPHE - PSL (METIS, EPOC, Biogéosciences) through ED 398 GRNE (Geosciences, Natural Resources & Environment) and ED 560 STEP'UP (Earth Science & Physics of the Universe).",
    },
    {
        "field": "environment",
        "also_fields": [],
        "department": "EPHE - PSL Doctoral School ED 472 (SIEB: Integrated Systems, Environment and Biodiversity) & ED 129 SEIF",
        "program_page": EPHE_URL,
        "gre_subject": ("No subject test", "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.", ETS_SUBJ_Q, ETS_SUBJ),
        "entry_quote": ("Les candidats titulaires d'un master recherche ou d'un diplôme de niveau équivalent sont admis à préparer un doctorat, après avis favorable de la commission compétente.", EPHE_URL),
        "extra_sup": ("À tout moment dans l’année, vous pouvez prendre contact par courriel avec un enseignant-chercheur dont la spécialité est proche de la thématique de votre projet de recherche.", EPHE_URL),
        "extra_fund": ("En Doctorat SIEB, justificatif du financement", EPHE_URL),
        "notes": "Covers biodiversity, ecology, and environmental sciences via EPHE-PSL ED 472 (Mention SIEB) and co-accredited ED 129 (Environmental Sciences of the Paris Region, SEIF). Note EPHE's published 2026-2027 SIEB Session 1 deadline was October 15, 2026 (prior to the Fall 2027 admission cycle), so Fall 2027 deadline is Not stated.",
    },
]

for p in PROGRAMS:
    fld = p["field"]
    sup_entry = {
        "code": "Required",
        "value": "Doctoral candidates must obtain agreement from an accredited dissertation advisor (HDR) and admission to a PSL-affiliated research unit before enrolling.",
        "quote": SUP_Q,
        "url": COLLEGE_URL,
    }
    if p["extra_sup"]:
        sup_entry["also"] = [{"quote": p["extra_sup"][0], "url": p["extra_sup"][1]}]

    fund_entry = {
        "code": "Competitive",
        "value": "Doctoral contracts are allocated competitively via Graduate Program and Doctoral School juries (alongside CIFRE industrial agreements, ANR/agency grants, and international fellowships); secured 3-year funding is generally required to enroll in science/engineering schools.",
        "quote": FUND_Q,
        "url": COLLEGE_URL,
    }
    if p["extra_fund"]:
        fund_entry["also"] = [{"quote": p["extra_fund"][0], "url": p["extra_fund"][1]}]

    entry_q, entry_u = p["entry_quote"]
    rec = {
        "id": f"psl--{fld}",
        "university": "psl",
        "field": fld,
        "also_fields": p["also_fields"],
        "department": p["department"],
        "program_page": p["program_page"],
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "Not stated",
                "value": "Standard 3-year PhD enrollment runs September 1 to mid-December after supervisor, funding, and doctoral-school jury selection; Fall 2027 doctoral-contract competition dates are not yet published (separate 5-year Bachelor-entry PhD Track call runs Oct 14 - Dec 14, 2026).",
                "quote": DEADLINE_Q,
                "url": COLLEGE_URL,
            },
            "gre_subject": {
                "code": p["gre_subject"][0],
                "value": p["gre_subject"][1],
                "quote": p["gre_subject"][2],
                "url": p["gre_subject"][3],
            },
            "supervisor": sup_entry,
            "funding": fund_entry,
            "entry_route": {
                "code": "Master's usually required",
                "value": "A Master's degree or equivalent is required for standard 3-year PhD admission under French national doctoral regulations (Article 10) and constituent-school rules; PSL also offers a separate 5-year Bachelor-entry PhD Track in select Graduate Programs.",
                "quote": entry_q,
                "url": entry_u,
            },
        },
        "notes": p["notes"],
    }
    (PROGS / f"psl--{fld}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Wrote psl.json and {len(PROGRAMS)} program files to {OUT}")
