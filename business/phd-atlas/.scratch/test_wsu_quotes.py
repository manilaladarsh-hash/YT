import hashlib, json, sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

def test_quote(url, quote):
    if not quote:
        return True, 'empty quote'
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    p = Path(f'.cache/pages/{key}.json')
    if not p.exists():
        return False, f'cache missing for {url} ({key})'
    data = json.loads(p.read_text(encoding='utf-8'))
    matched = False
    if quote in data.get('text', ''):
        matched = True
    elif quote in data.get('html', ''):
        matched = True
    else:
        norm_q = ' '.join(quote.split())
        norm_t = ' '.join(data.get('text', '').split())
        norm_h = ' '.join(data.get('html', '').split())
        if norm_q in norm_t or norm_q in norm_h:
            matched = True
    if matched:
        return True, 'OK'
    return False, f'QUOTE NOT MATCHED IN {url} ({key})'

tests = [
    # University fields
    ('https://gradschool.wsu.edu/apply/', '$100 Non-refundable Application Fee*'),
    ('https://gradschool.wsu.edu/apply/', '*McNair Scholars and WSU Research Experience for Undergraduates (REU) students are eligible for an application fee waiver from the Graduate School. Please contact Dr. Raymond Herrera before applying. All other application fee waiver requests should be directed to the program(s) to which you are applying.'),
    ('https://gradschool.wsu.edu/international-requirements/', 'Please check with your specific Degree Program to determine whether a GRE test is required.'),
    ('https://gradschool.wsu.edu/international-requirements/', 'Exam TOEFL Essentials TOEFL (PBT) TOEFL (iBT) New TOEFL (iBT) (Effective Jan 21, 2026) IELTS Duolingo Cambridge B2 First, C1 Advanced, C2 Proficiency Michigan English Test (MET) Pearson Test for English (PTEA) International Test of English Proficiency (iTEP) Minimum Score 8 540 75 4 6.5 105 176 52 56 4.5'),
    ('https://gradschool.wsu.edu/international-requirements/', 'Hold a baccalaureate-level or higher degree from a college or university outside the United States where the language of instruction was English (provide an official letter or transcript from the school stating English was the language of instruction).'),
    ('https://gradschool.wsu.edu/international-requirements/', 'Have earned the equivalent of a U.S. bachelor’s degree from a regionally accredited institution. Typically, students should have completed a minimum of four years of study beyond grade 12.'),
    # Programs
    # CS
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/', 'Fall January 10th'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-computer-science/', 'GRE Optional'),
    # ECE
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/', 'Fall January 10th'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-electrical-and-computer-engineering/', 'GRE Optional'),
    # ChemEng
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemical-engineering/', 'Fall January 10 January 1'),
    # Civil
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/', 'Fall January 10'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-civil-engineering/', 'GRE No'),
    # Materials
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-materials-science/', 'Fall January 10'),
    # Mech
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/', 'Fall January 10'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mechanical-engineering/', 'Required application material includes an application, resume, statement of purpose, Student Interest Profile form, three letters of recommendation, official transcripts, official GRE scores, and official TOEFL scores (international applicants).'),
    # Physics
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/', 'Fall January 15'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/', 'GRE scores optional'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-physics/', 'Subject Physics GRE Strongly Recommended'),
    # Chemistry
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/', 'Fall Second Friday of December Priority deadline'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-chemistry/', 'GRE Scores-General Test Optional.'),
    # Math
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/', 'Fall December 10'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/', 'GRE scores are not required but encouraged'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-mathematics/', 'Students applying to the PhD in Mathematics will be automatically considered for an assistantship position.'),
    # Earth (Geology)
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/', 'Fall January 10th'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/', 'GRE tests requirement are waived until further notice.'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-geology/', 'The School of the Environment does not consider graduate applicants who have not secured a faculty advisor before applying, so please do not apply to one of our graduate degrees without first doing this step.'),
    # Biology
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/', 'Fall January 10'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-biology/', 'GRE is NOT required'),
    # Environment
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/', 'Fall January 10th'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/', 'GRE tests requirement are waived until further notice.'),
    ('https://gradschool.wsu.edu/degrees/doctor-of-philosophy-environmental-and-natural-resource-sciences/', 'The School of the Environment does not consider graduate applicants who have not secured a faculty advisor before applying, so please do not apply to one of our graduate degrees without first doing this step.')
]

all_ok = True
for url, q in tests:
    ok, msg = test_quote(url, q)
    if not ok:
        print('FAILED:', msg, '->', repr(q[:60]))
        all_ok = False
    else:
        print('PASSED:', repr(q[:50]))

print('ALL PASSED?', all_ok)
