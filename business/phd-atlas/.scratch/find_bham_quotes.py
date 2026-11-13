import hashlib, json

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
    lines = [l.strip() for l in raw.split('\n') if l.strip()]
    
    # entry route
    entry_candidates = [l for l in lines if 'honours' in l.lower() or 'entry requirements' in l.lower()]
    # supervisor
    sup_candidates = [l for l in lines if 'supervisor' in l.lower() and len(l) > 25]
    # funding
    fund_candidates = [l for l in lines if ('scholarship' in l.lower() or 'funding' in l.lower() or 'stipend' in l.lower()) and len(l) > 30]
    # deadline
    dl_candidates = [l for l in lines if 'accepted all year round' in l.lower() or '1 june' in l.lower()]
    
    print(f'=== {field} ===')
    if entry_candidates:
        print('ENTRY:', entry_candidates[0][:100])
    if sup_candidates:
        print('SUP:', sup_candidates[0][:100])
    if fund_candidates:
        print('FUND:', fund_candidates[0][:100])
    if dl_candidates:
        print('DL:', dl_candidates[0][:100])
