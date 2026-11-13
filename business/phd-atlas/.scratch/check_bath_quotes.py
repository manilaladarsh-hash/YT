import json, os, hashlib
from pathlib import Path

ROOT = Path('C:/Users/manil/YT/business/phd-atlas')
CACHE = ROOT / '.cache' / 'pages'

def get_text(url):
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    return json.loads((CACHE / f'{h}.json').read_text(encoding='utf-8'))['text']

urls = {
    'cs': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-computer-science-full-time/',
    'math': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-mathematics-full-time/',
    'statistics': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-statistics-full-time/',
    'chemistry': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-chemistry-full-time/',
    'physics': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-physics-full-time/',
    'biology': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-biology-full-time/',
    'biomed': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-biochemistry-full-time/',
    'chemeng': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-chemical-engineering-full-time/',
    'civil': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-civil-engineering-full-time/',
    'ece': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-electronic-and-electrical-engineering-full-time/',
    'mech': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-mechanical-engineering-full-time/',
    'neuro': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-psychology-full-time/',
}

for name, u in urls.items():
    text = get_text(u)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f'=== {name} ===')
    
    # Entry
    entry = [l for l in lines if 'honours' in l.lower() or 'undergraduate degree' in l.lower() or 'entry requirements' in l.lower()]
    if entry:
        print('  ENTRY:', entry[0][:100])
    
    # Supervisor
    sup = [l for l in lines if 'supervis' in l.lower() and len(l) > 20]
    if sup:
        print('  SUP:', sup[0][:100])
        
    # Deadline
    dl = [l for l in lines if 'deadline' in l.lower() and len(l) > 20]
    if dl:
        print('  DL:', dl[0][:100])
        
    # Funding
    fund = [l for l in lines if ('funding' in l.lower() or 'scholarship' in l.lower() or 'stipend' in l.lower()) and len(l) > 20]
    if fund:
        print('  FUND:', fund[0][:100])
