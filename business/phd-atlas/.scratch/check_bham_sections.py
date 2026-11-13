import hashlib, json, re

urls = {
    'astronomy': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/physics-and-astronomy-courses/physics-astronomy-phd',
    'biology': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/biosciences-courses/biosciences-phd',
    'biomed': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/medicine-courses/biomedical-sciences-phd',
    'chemeng': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/chemical-engineering-courses/chemical-engineering-phd',
    'chemistry': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/chemistry-courses/chemistry-phd',
    'civil': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/civil-engineering-courses/civil-engineering-phd',
    'cs': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/computer-science-and-data-science-courses/computer-science-phd',
    'earth': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/geography-earth-and-environmental-sciences-courses/earth-sciences-phd',
    'ece': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/electronic-electrical-and-systems-engineering-courses/electronic-electrical-systems-engineering-phd',
    'environment': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/geography-earth-and-environmental-sciences-courses/environmental-health-and-risk-management-phd',
    'materials': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/materials-science-and-engineering-courses/metallurgy-materials-phd',
    'math': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/mathematics-courses/pure-mathematics-phd',
    'mech': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/mechanical-engineering-courses/mechanical-engineering-phd',
    'neuro': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/psychology-courses/psychology-phd',
    'physics': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/physics-and-astronomy-courses/physics-astronomy-phd',
    'statistics': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/mathematics-courses/statistics-phd',
}

for field, u in urls.items():
    h = hashlib.sha1(u.encode()).hexdigest()[:16]
    raw = json.loads(open(f'.cache/pages/{h}.json', encoding='utf-8').read())['text']
    
    # check deadline
    has_dl = 'applications are accepted all year round' in raw or 'apply by 1 june' in raw.lower()
    # check entry route
    has_entry = 'honours degree' in raw.lower()
    # check supervisor
    has_sup = 'supervisor' in raw.lower()
    # check funding
    has_fund = 'scholarships' in raw.lower() or 'funding' in raw.lower()
    print(f'{field:12} dl={has_dl} entry={has_entry} sup={has_sup} fund={has_fund}')
