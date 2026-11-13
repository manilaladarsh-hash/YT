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
    ('https://gradstudies.artsci.washu.edu/admissions-faqs', 'The application fee for graduate programs in Arts & Sciences is $45.'),
    ('https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html', 'Graduate applicants: Attend an info session and skip the application fee'),
    ('https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html', 'While the GRE General Test is optional for many programs, applicants are still encouraged to submit valid GRE scores if a test has already been taken or can take the test and provide results by our application deadline, as it gives us additional information when evaluating an application.'),
    ('https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/', 'Test of English as a Foreign Language (TOEFL) iBT – 5.0 overall (new scale) OR 4.5 ≥ 90 overall (old scale)'),
    ('https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/', 'International English Language Testing System (IELTS) Academic – 6.5 minimum composite score'),
    ('https://provost.washu.edu/vpge/graduate-admissions-academics-and-policies/', 'Citizenship from one of the following countries: Australia, Bermuda, Cameroon, Canada, Caribbean Commonwealth countries and British Caribbean territories (Anguilla, Antigua and Barbuda, The Bahamas, Barbados, Belize, British Virgin Islands, Cayman Islands, Dominica, Grenada, Guyana, Jamaica, Montserrat, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Trinidad and Tobago, Turks and Caicos Islands), Ghana, Gibraltar, Hong Kong, India, Ireland, Kenya, Liberia, New Zealand, Nigeria, Sierra Leone, Singapore, South Africa, Uganda, United Kingdom, United States, Zambia, Zimbabwe.'),
    # Engineering general
    ('https://engineering.washu.edu/academics/graduate-admissions/application-checklist.html', 'All eligible applicants must have earned or will have earned an undergraduate degree by the start of their graduate program.'),
    ('https://gradstudies.artsci.washu.edu/admissions-faqs', 'PhD students at WashU receive full tuition remission and a monthly stipend for living expenses for the duration of their program length.'),
    ('https://engineering.washu.edu/academics/graduate-admissions/deadlines.html', 'December 1'),
    # Physics
    ('https://gradstudies.artsci.washu.edu/physics', 'PhD - December 1, 2026 at 11:59 PM Eastern Standard Time'),
    ('https://physics.washu.edu/graduate', 'The GRE General and Subject test scores are optional.'),
    ('https://physics.washu.edu/graduate', 'Students who are admitted to the PhD program in Physics receive a complete financial support package including full tuition and a stipend/salary for the academic year. Financial support is guaranteed by the department for the first five years for students who are making satisfactory progress towards their PhD.'),
    ('https://gradstudies.artsci.washu.edu/admissions-faqs', "Applicants may apply to a PhD program so long as the equivalent of a bachelor's degree is earned prior to the application semester."),
    # Chemistry
    ('https://gradstudies.artsci.washu.edu/chemistry', 'Application deadline: December 1, 2026 at 11:59 PM Eastern Standard Time'),
    ('https://chemistry.washu.edu/graduate', "All Chemistry PhD students receive a generous stipend ($36,050 for the '24-25 twelve-month academic year) and a tuition fellowship for the duration of the program."),
    # Math
    ('https://gradstudies.artsci.washu.edu/mathematics', 'PhD - December 1, 2026 at 11:59 PM Eastern Standard Time'),
    ('https://math.washu.edu/graduate', 'The completion of the doctoral degree requires about five years of full-time study, and virtually all students receive full financial support (stipends and tuition waiver) during their study.'),
    # Earth
    ('https://gradstudies.artsci.washu.edu/earth-environmental-and-planetary-sciences', 'Application deadline: December 1, 2026 at 11:59 PM Eastern Standard Time'),
    ('https://eeps.washu.edu/graduate', "For those choosing to submit GRE scores, please use WashU's school code 6929 and the department code 0806. However, please note that GRE scores are optional."),
    # DBBS (Biology & Neuro)
    ('https://dbbs.wustl.edu/admissions/', 'APPLICATION DATES: September 1 – November 15 at 11:59 PM EST'),
    ('https://dbbs.wustl.edu/admissions/', 'GRE NOT REQUIRED NOR ACCEPTED'),
    ('https://dbbs.wustl.edu/admissions/', 'full tuition and yearly stipend are guaranteed to all accepted students.')
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
