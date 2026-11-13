import json, os, hashlib, shutil
from pathlib import Path

ROOT = Path('C:/Users/manil/YT/business/phd-atlas')
STAGE = ROOT / 'data' / 'staging'
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
        'department': 'School of Physics and Astronomy',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/physics-and-astronomy-courses/physics-astronomy-phd',
        'notes': 'Postgraduate research programme (Physics and Astronomy PhD / MSc by Research) in the School of Physics and Astronomy at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'biology': {
        'field': 'biology',
        'also_fields': [],
        'department': 'School of Biosciences',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/biosciences-courses/biosciences-phd',
        'notes': 'Postgraduate research programme (Biosciences PhD) in the School of Biosciences at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'biomed': {
        'field': 'biomed',
        'also_fields': [],
        'department': 'College of Medicine and Health',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/medicine-courses/biomedical-sciences-phd',
        'notes': 'Postgraduate research programme (Biomedical Sciences PhD / MSc by Research) in the College of Medicine and Health at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'chemeng': {
        'field': 'chemeng',
        'also_fields': [],
        'department': 'School of Chemical Engineering',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/chemical-engineering-courses/chemical-engineering-phd',
        'notes': 'Postgraduate research programme (Chemical Engineering PhD / MSc by Research) in the School of Chemical Engineering at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'chemistry': {
        'field': 'chemistry',
        'also_fields': [],
        'department': 'School of Chemistry',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/chemistry-courses/chemistry-phd',
        'notes': 'Postgraduate research programme (Chemistry PhD / MSc by Research) in the School of Chemistry at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'civil': {
        'field': 'civil',
        'also_fields': [],
        'department': 'Department of Civil Engineering',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/civil-engineering-courses/civil-engineering-phd',
        'notes': 'Postgraduate research programme (Civil Engineering PhD / MPhil) in the Department of Civil Engineering at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'cs': {
        'field': 'cs',
        'also_fields': [],
        'department': 'School of Computer Science',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/computer-science-and-data-science-courses/computer-science-phd',
        'notes': 'Postgraduate research programme (Computer Science PhD) in the School of Computer Science at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'earth': {
        'field': 'earth',
        'also_fields': [],
        'department': 'School of Geography, Earth and Environmental Sciences',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/geography-earth-and-environmental-sciences-courses/earth-sciences-phd',
        'notes': 'Postgraduate research programme (Earth Sciences PhD / MPhil) in the School of Geography, Earth and Environmental Sciences at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'ece': {
        'field': 'ece',
        'also_fields': [],
        'department': 'Department of Electronic, Electrical and Systems Engineering',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/electronic-electrical-and-systems-engineering-courses/electronic-electrical-systems-engineering-phd',
        'notes': 'Postgraduate research programme (Electronic, Electrical and Systems Engineering PhD / MSc by Research) in the Department of Electronic, Electrical and Systems Engineering at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'environment': {
        'field': 'environment',
        'also_fields': [],
        'department': 'School of Geography, Earth and Environmental Sciences',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/geography-earth-and-environmental-sciences-courses/environmental-health-and-risk-management-phd',
        'notes': 'Postgraduate research programme (Environmental Health and Risk Management PhD) in the School of Geography, Earth and Environmental Sciences at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'materials': {
        'field': 'materials',
        'also_fields': [],
        'department': 'School of Metallurgy and Materials',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/materials-science-and-engineering-courses/metallurgy-materials-phd',
        'notes': 'Postgraduate research programme (Metallurgy and Materials PhD / MSc by Research) in the School of Metallurgy and Materials at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
    'math': {
        'field': 'math',
        'also_fields': [],
        'department': 'School of Mathematics',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/mathematics-courses/pure-mathematics-phd',
        'notes': 'Postgraduate research programme (Pure Mathematics PhD) in the School of Mathematics at the University of Birmingham.',
        'subject_test': 'Not stated',
    },
    'mech': {
        'field': 'mech',
        'also_fields': ['bme'],
        'department': 'Department of Mechanical Engineering',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/mechanical-engineering-courses/mechanical-engineering-phd',
        'notes': 'Postgraduate research programme (Mechanical Engineering PhD / MSc by Research) in the Department of Mechanical Engineering at the University of Birmingham; includes Biomedical Engineering research group.',
        'subject_test': 'No subject test',
    },
    'neuro': {
        'field': 'neuro',
        'also_fields': [],
        'department': 'School of Psychology',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/psychology-courses/psychology-phd',
        'notes': 'Postgraduate research programme (Psychology PhD / MSc by Research) in the School of Psychology / Centre for Human Brain Health at the University of Birmingham.',
        'subject_test': 'Not stated',
    },
    'physics': {
        'field': 'physics',
        'also_fields': [],
        'department': 'School of Physics and Astronomy',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/physics-and-astronomy-courses/physics-astronomy-phd',
        'notes': 'Postgraduate research programme (Physics and Astronomy PhD / MSc by Research) in the School of Physics and Astronomy at the University of Birmingham.',
        'subject_test': 'Not stated',
    },
    'statistics': {
        'field': 'statistics',
        'also_fields': [],
        'department': 'School of Mathematics',
        'program_page': 'https://www.birmingham.ac.uk/study/postgraduate/subjects/mathematics-courses/statistics-phd',
        'notes': 'Postgraduate research programme (Statistics PhD) in the School of Mathematics at the University of Birmingham.',
        'subject_test': 'No subject test',
    },
}

out_progs = {}
for name, p in PROGRAMS.items():
    url = p['program_page']
    text = get_text(url)
    
    # 1. Deadline
    # Birmingham standard text:
    # "If you are submitting your own research proposal, applications are accepted all year round. However, if you wish to start in September, we would strongly encourage you to apply by 1 June."
    dl_quote = "If you are submitting your own research proposal, applications are accepted all year round. However, if you wish to start in September, we would strongly encourage you to apply by 1 June."
    if dl_quote not in text:
        # Check alternative on biomed:
        # "This PhD programme can be undertaken full-time (minimum 36 months) or part-time (minimum 72 months)."
        for piece in ["applications are accepted all year round", "apply by 1 June"]:
            assert piece in text, f"Missing deadline piece in {name}"
    
    # 2. Entry route
    # Look for "2:1 Honours degree" or "A 2:1 Honours degree" or "2.1 Honours degree"
    entry_code = "Bachelor's"
    if "A 2.1 Honours degree or equivalent, or a postgraduate Masters, in a relevant subject." in text:
        entry_code = "Either"
        entry_val = "A 2.1 Honours degree or equivalent, or a postgraduate Master's, in a relevant subject."
        entry_quote = "A 2.1 Honours degree or equivalent, or a postgraduate Masters, in a relevant subject."
    elif "2:1 Honours degree" in text:
        entry_code = "Direct from bachelor's"
        entry_val = "A 2:1 UK Honours degree or equivalent qualification in a relevant discipline."
        entry_quote = "2:1 Honours degree"
    elif "2:1 Honours Degree" in text:
        entry_code = "Direct from bachelor's"
        entry_val = "A 2:1 UK Honours degree or equivalent qualification in a relevant discipline."
        entry_quote = "2:1 Honours Degree (for the PhD)"
    elif "2.1 Honours degree" in text:
        entry_code = "Direct from bachelor's"
        entry_val = "A 2:1 UK Honours degree or equivalent qualification in a relevant discipline."
        entry_quote = "2.1 Honours degree"
    else:
        raise ValueError(f"Unknown entry route in {name}")

    # 3. Supervisor
    if "When you apply, you can suggest one or two potential supervisors, who you think might be a good fit for you. However, this is not essential." in text:
        sup_code = "Recommended"
        sup_val = "Applicants proposing their own research can suggest potential supervisors, but can also apply without naming one."
        sup_quote = "When you apply, you can suggest one or two potential supervisors, who you think might be a good fit for you. However, this is not essential."
    elif "If you’d rather propose your own research, the first step is to find your supervisor. We encourage you to browse the biographies of faculty members to familiarise yourself with the research going on in your preferred areas." in text:
        sup_code = "Recommended"
        sup_val = "Applicants proposing their own research are encouraged to find a supervisor by browsing faculty research profiles."
        sup_quote = "If you’d rather propose your own research, the first step is to find your supervisor. We encourage you to browse the biographies of faculty members to familiarise yourself with the research going on in your preferred areas."
    else:
        # Generic match for supervisor mention
        lines = [l.strip() for l in text.split('\n') if 'supervisor' in l.lower() and len(l.strip()) >= 15]
        assert lines, f"No supervisor line in {name}"
        sup_code = "Recommended"
        sup_val = "Applicants devise their research topic and consult or collaborate closely with supervisors throughout their studies."
        sup_quote = lines[0]

    # 4. Funding
    if "A limited number of scholarships and studentships may be available to outstanding applicants." in text:
        fund_code = "Competitive"
        fund_val = "A limited number of scholarships and studentships may be available to outstanding applicants."
        fund_quote = "A limited number of scholarships and studentships may be available to outstanding applicants."
    elif "Apply for a PhD that already has funding attached" in text:
        fund_code = "Competitive"
        fund_val = "Advertised projects may be fully funded or competition funded; self-proposed research may search for scholarships."
        fund_quote = "Apply for a PhD that already has funding attached"
    else:
        lines = [l.strip() for l in text.split('\n') if ('scholarship' in l.lower() or 'funding' in l.lower()) and len(l.strip()) >= 20]
        assert lines, f"No funding line in {name}"
        fund_code = "Competitive"
        fund_val = "Funding is competitive via university scholarships, research councils and studentships."
        fund_quote = lines[0]

    # 5. GRE Subject
    if p['subject_test'] == 'No subject test':
        subj_code = "No subject test"
        subj_val = "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology."
        subj_quote = ETS_QUOTE
        subj_url = ETS_URL
    else:
        subj_code = "Not stated"
        subj_val = "GRE Subject Test is not stated or required for postgraduate research admission at Birmingham."
        subj_quote = ""
        subj_url = url

    rec = {
        "id": f"birmingham--{p['field']}",
        "university": "birmingham",
        "field": p['field'],
        "also_fields": p['also_fields'],
        "department": p['department'],
        "program_page": url,
        "checked": "2026-10-31",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "Applications for self-proposed research are accepted all year round, with 1 June recommended for September entry and early spring for funding.",
                "quote": dl_quote,
                "url": url,
                "time_sensitive": "2027-06-01"
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
    out_progs[f"birmingham--{p['field']}.json"] = rec

print(f"Generated {len(out_progs)} programs")

# Test quotes against validate_data
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

print(f"Validation on generated records: {len(errors)} errors, {len(warnings)} warnings")
if errors:
    for e in errors:
        print("ERROR:", e)
