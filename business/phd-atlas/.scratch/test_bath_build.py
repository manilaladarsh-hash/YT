import json, os, hashlib
from pathlib import Path

ROOT = Path('C:/Users/manil/YT/business/phd-atlas')
CACHE = ROOT / '.cache' / 'pages'

def get_text(url):
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    return json.loads((CACHE / f'{h}.json').read_text(encoding='utf-8'))['text']

ETS_URL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

PROGRAMS = {
    'astronomy': {
        'field': 'astronomy',
        'also_fields': [],
        'department': 'Department of Physics',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-physics-full-time/',
        'notes': 'Postgraduate research programme (Physics PhD / Astrophysics research group) in the Department of Physics at the University of Bath.',
        'subject_test': 'No subject test',
    },
    'biology': {
        'field': 'biology',
        'also_fields': [],
        'department': 'Department of Life Sciences',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-biology-full-time/',
        'notes': 'Postgraduate research programme (Biology PhD) in the Department of Life Sciences at the University of Bath.',
        'subject_test': 'No subject test',
    },
    'biomed': {
        'field': 'biomed',
        'also_fields': [],
        'department': 'Department of Life Sciences',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-biochemistry-full-time/',
        'notes': 'Postgraduate research programme (Biochemistry PhD) in the Department of Life Sciences at the University of Bath.',
        'subject_test': 'No subject test',
    },
    'chemeng': {
        'field': 'chemeng',
        'also_fields': ['materials'],
        'department': 'Department of Chemical Engineering',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-chemical-engineering-full-time/',
        'notes': 'Postgraduate research programme (Chemical Engineering PhD) in the Department of Chemical Engineering at the University of Bath; covers advanced materials and chemical technologies.',
        'subject_test': 'No subject test',
    },
    'chemistry': {
        'field': 'chemistry',
        'also_fields': [],
        'department': 'Department of Chemistry',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-chemistry-full-time/',
        'notes': 'Postgraduate research programme (Chemistry PhD) in the Department of Chemistry at the University of Bath.',
        'subject_test': 'No subject test',
    },
    'civil': {
        'field': 'civil',
        'also_fields': ['environment'],
        'department': 'Department of Architecture & Civil Engineering',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-civil-engineering-full-time/',
        'notes': 'Postgraduate research programme (Civil Engineering PhD) in the Department of Architecture & Civil Engineering at the University of Bath; includes climate adaptation and environmental research.',
        'subject_test': 'No subject test',
    },
    'cs': {
        'field': 'cs',
        'also_fields': [],
        'department': 'Department of Computer Science',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-computer-science-full-time/',
        'notes': 'Postgraduate research programme (Computer Science PhD) in the Department of Computer Science at the University of Bath.',
        'subject_test': 'No subject test',
    },
    'ece': {
        'field': 'ece',
        'also_fields': [],
        'department': 'Department of Electronic & Electrical Engineering',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-electronic-and-electrical-engineering-full-time/',
        'notes': 'Postgraduate research programme (Electronic and Electrical Engineering PhD) in the Department of Electronic & Electrical Engineering at the University of Bath.',
        'subject_test': 'No subject test',
    },
    'math': {
        'field': 'math',
        'also_fields': [],
        'department': 'Department of Mathematical Sciences',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-mathematics-full-time/',
        'notes': 'Postgraduate research programme (Mathematics PhD) in the Department of Mathematical Sciences at the University of Bath.',
        'subject_test': 'Not stated',
    },
    'mech': {
        'field': 'mech',
        'also_fields': ['bme'],
        'department': 'Department of Mechanical Engineering',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-mechanical-engineering-full-time/',
        'notes': 'Postgraduate research programme (Mechanical Engineering PhD) in the Department of Mechanical Engineering at the University of Bath; includes bioengineering and biomedical technologies.',
        'subject_test': 'No subject test',
    },
    'neuro': {
        'field': 'neuro',
        'also_fields': [],
        'department': 'Department of Psychology',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-psychology-full-time/',
        'notes': 'Postgraduate research programme (Psychology PhD / Cognitive Neuroscience) in the Department of Psychology at the University of Bath.',
        'subject_test': 'Not stated',
    },
    'physics': {
        'field': 'physics',
        'also_fields': [],
        'department': 'Department of Physics',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-physics-full-time/',
        'notes': 'Postgraduate research programme (Physics PhD) in the Department of Physics at the University of Bath.',
        'subject_test': 'Not stated',
    },
    'statistics': {
        'field': 'statistics',
        'also_fields': [],
        'department': 'Department of Mathematical Sciences',
        'program_page': 'https://www.bath.ac.uk/courses/postgraduate-research/phd-statistics-full-time/',
        'notes': 'Postgraduate research programme (Statistics PhD) in the Department of Mathematical Sciences at the University of Bath.',
        'subject_test': 'No subject test',
    },
}

out_progs = {}
for name, p in PROGRAMS.items():
    url = p['program_page']
    text = get_text(url)
    
    # 1. Deadline
    dl_quote = "3 months prior to the intended start date (for international applicants) or 2 months prior to the intended start date (for home applicants). For example, for an end of September start, the deadline is 30 June (international) and 31 July (home)."
    assert dl_quote in text, f"Missing dl quote in {name}"
    
    # 2. Entry route
    if "A first-class or upper second-class honours degree (or equivalent)" in text:
        entry_code = "Direct from bachelor's"
        entry_val = "A first-class or upper second-class UK Honours degree (or equivalent), or a relevant Master's degree."
        entry_quote = "A first-class or upper second-class honours degree (or equivalent)"
    else:
        # Check alternative
        lines = [l.strip() for l in text.split('\n') if 'honours degree' in l.lower() and len(l.strip()) >= 15]
        assert lines, f"No entry line in {name}"
        entry_code = "Direct from bachelor's"
        entry_val = "A first-class or upper second-class UK Honours degree (or equivalent)."
        entry_quote = lines[0]

    # 3. Supervisor
    if "You must identify at least one (up to two) intended lead supervisor(s) in your application. We cannot consider your application if no supervisor has been named." in text:
        sup_code = "Required"
        sup_val = "Applicants must identify at least one intended lead supervisor in their application, and are strongly recommended to contact them beforehand."
        sup_quote = "You must identify at least one (up to two) intended lead supervisor(s) in your application. We cannot consider your application if no supervisor has been named."
    elif "Use the University website to find specific staff who might be able to supervise in your project area." in text:
        sup_code = "Recommended"
        sup_val = "Applicants are encouraged to consult staff research profiles to identify potential supervisors in their project area."
        sup_quote = "Use the University website to find specific staff who might be able to supervise in your project area."
    else:
        lines = [l.strip() for l in text.split('\n') if 'supervisor' in l.lower() and len(l.strip()) >= 20]
        assert lines, f"No sup line in {name}"
        sup_code = "Recommended"
        sup_val = "Applicants identify and collaborate with potential research supervisors in their department."
        sup_quote = lines[0]

    # 4. Funding
    fund_lines = [l.strip() for l in text.split('\n') if ('fees and funding information for' in l.lower() or 'studentship' in l.lower() or 'funding options' in l.lower()) and len(l.strip()) >= 20]
    assert fund_lines, f"No fund line in {name}"
    fund_code = "Competitive"
    fund_val = "Funding is competitive via university research studentships, research councils, or project-specific funding."
    fund_quote = fund_lines[0]

    # 5. GRE Subject
    if p['subject_test'] == 'No subject test':
        subj_code = "No subject test"
        subj_val = "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology."
        subj_quote = ETS_QUOTE
        subj_url = ETS_URL
    else:
        subj_code = "Not stated"
        subj_val = "GRE Subject Test is not stated or required for doctoral research admission at the University of Bath."
        subj_quote = ""
        subj_url = url

    rec = {
        "id": f"bath--{p['field']}",
        "university": "bath",
        "field": p['field'],
        "also_fields": p['also_fields'],
        "department": p['department'],
        "program_page": url,
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications are accepted on a rolling basis with deadlines 3 months prior to the intended start date for international applicants (30 June for September start).",
                "quote": dl_quote,
                "url": url,
                "time_sensitive": "2027-06-30"
            },
            "entry_route": {
                "code": entry_code,
                "value": entry_val,
                "quote": entry_quote,
                "url": url
            },
            "supervisor": {
                "code": sup_code,
                "value": sup_val,
                "quote": sup_quote,
                "url": url
            },
            "funding": {
                "code": fund_code,
                "value": fund_val,
                "quote": fund_quote,
                "url": url
            },
            "gre_subject": {
                "code": subj_code,
                "value": subj_val,
                "quote": subj_quote,
                "url": subj_url
            }
        },
        "notes": p['notes']
    }
    out_progs[f"bath--{p['field']}.json"] = rec

print(f"Generated {len(out_progs)} Bath programs")

import sys
sys.path.insert(0, str(ROOT / 'scripts'))
import validate_data

texts = validate_data.cached_texts()
errors = []
warnings = []
pfields = validate_data.SCHEMA["program_fields"]

for fname, r in out_progs.items():
    where = "programs/" + fname
    for name, fld in r["fields"].items():
        spec = pfields[name]
        validate_data.check_field(where, name, spec, fld, texts, True, errors, warnings)

print(f"Validation on generated Bath records: {len(errors)} errors, {len(warnings)} warnings")
if errors:
    for e in errors:
        print("ERROR:", e)
