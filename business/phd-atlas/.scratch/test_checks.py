import sys, os
sys.path.insert(0, os.getcwd())
from scripts.validate_data import cached_texts, norm, quote_parts

texts = cached_texts()

checks = [
    # materials
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-materials",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "there is no need to contact any supervisor before making an application",
     "Final application deadline to be considered for Oxford scholarships"),
    # math
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-mathematics",
     "a first-class undergraduate degree with honours in mathematics or a related discipline. A previous master's degree is not required",
     "you do not need to contact the department before you apply",
     "Final application deadline to be considered for Oxford scholarships"),
    # statistics
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-statistics",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "contact a potential supervisor via email to clarify your proposed research area",
     "Final application deadline to be considered for Oxford scholarships"),
    # physics
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-theoretical-physics",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "you do not need to contact the department before you apply but you are encouraged",
     "Final application deadline to be considered for Oxford scholarships"),
    # astronomy
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-astrophysics",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "you do not need to contact the department before you apply but you are encouraged",
     "considered for Oxford scholarships. For the majority of Oxford scholarships, your application will automatically be"),
    # chemistry
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-chemistry",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "You should make contact with the academic(s) in your area of research to discuss potential research topics",
     "Final application deadline to be considered for Oxford scholarships"),
    # biology
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-biology",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "You must contact your potential supervisor",
     "Final application deadline to be considered for Oxford scholarships"),
    # earth
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-earth-sciences",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "identify an academic member of staff who is willing to supervise you",
     "Final application deadline to be considered for Oxford scholarships"),
    # neuro
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-neuroscience",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "It is recommended that you contact the course lecturer before you apply",
     "considered for Oxford scholarships. For the majority of Oxford scholarships, your application will automatically be"),
    # biomed
    ("https://www.ox.ac.uk/admissions/graduate/courses/dphil-medical-sciences",
     "a first-class or strong upper second-class undergraduate degree with honours",
     "you should contact prospective supervisors to discuss the research opportunities available",
     "considered for Oxford scholarships. For the majority of Oxford scholarships, your application will automatically be"),
]

all_ok = True
for url, q_deg, q_sup, q_fund in checks:
    page = texts[url]
    m_deg = norm(q_deg) in page
    m_sup = norm(q_sup) in page
    m_fund = norm(q_fund) in page
    name = url.split("/")[-1]
    print(f"{name}: deg={m_deg}, sup={m_sup}, fund={m_fund}")
    if not (m_deg and m_sup and m_fund):
        all_ok = False

print("ALL OK?", all_ok)
