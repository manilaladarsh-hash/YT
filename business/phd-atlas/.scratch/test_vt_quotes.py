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
    # check html or text
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
    ('https://graduateschool.vt.edu/admissions/how-to-apply.html', 'Degree-seeking students must include a $75 fee with their application, though check to see if you qualify for a waiver or reduced fee. All application fees are non-refundable.'),
    ('https://graduateschool.vt.edu/admissions/tuition-and-costs/Application_Fees.html', 'Applicants may be eligible for a Virginia Tech Graduate School application fee waivers based on the qualifying events below. Documentation as evidence of eligibility must be provided for review and approval under each category.'),
    ('https://graduateschool.vt.edu/admissions/how-to-apply.html', 'The Graduate School does not require entrance tests, but check to see whether your department requires you to submit GRE, GMAT, or subject test scores with your application.'),
    ('https://graduateschool.vt.edu/admissions/how-to-apply/testing-requirements.html', 'For TOEFL tests taken prior to January 21, 2026, a minimum overall score of 90 and 20 on each subsection score is required. Some departments may require higher minimum scores.'),
    ('https://graduateschool.vt.edu/admissions/how-to-apply/testing-requirements.html', 'A minimum TOEFL score of 4.5 (IBT) or IELTS score of 6.5 is required for admission.'),
    ('https://graduateschool.vt.edu/admissions/how-to-apply/testing-requirements.html', 'English proficiency can also be demonstrated through a conferred bachelor’s degree from an accredited university where English is the medium of instruction. If this applies to you, we will code a waiver of the English proficiency requirement into your application once we receive and review your transcript showing degree conferral and medium of instruction as English.'),
    ('https://catalog.vt.edu/graduate/graduate-policies/', 'Regular admission to a graduate degree is open to applicants whose grade point average (GPA) meets or exceeds the 3.00 required by the Graduate School for the last half of the credits earned for the undergraduate (bachelor’s) degree, and whose academic background meets the requirements of the admitting academic unit.'),
    ('https://website.cs.vt.edu/academic/graduate/future-grads/ApplicationDeadlines.html', 'Dec. 1, 2026'),
    ('https://website.cs.vt.edu/academic/graduate/future-grads/ApplicationDeadlines.html', 'Graduate Record Examination (GRE): Not required for any degree programs.'),
    ('https://catalog.vt.edu/graduate/degree-programs/electrical-engineering/electrical-engineering-phd/', 'Program-specific: To be fully considered for funding, Jan 15 for fall admission and Sep 1 for spring admission'),
    ('https://catalog.vt.edu/graduate/degree-programs/electrical-engineering/electrical-engineering-phd/', 'GRE: optional'),
    ('https://catalog.vt.edu/graduate/degree-programs/biomedical-engineering/biomedical-engineering-phd/', 'Admission application deadlines: Dec 15 (or Friday before)'),
    ('https://catalog.vt.edu/graduate/degree-programs/biomedical-engineering/biomedical-engineering-phd/', 'GRE: optional'),
    ('https://catalog.vt.edu/graduate/degree-programs/chemical-engineering/chemical-engineering-phd/', 'Admission application deadlines: Jan 6 for Fall; Sep 1 for Spring'),
    ('https://catalog.vt.edu/graduate/degree-programs/chemical-engineering/chemical-engineering-phd/', 'GRE: optional'),
    ('https://catalog.vt.edu/graduate/degree-programs/civil-engineering/civil-engineering-phd/', 'Admission application deadlines: Graduate School default of Aug 1 for Fall; Jan 5 for Spring'),
    ('https://catalog.vt.edu/graduate/degree-programs/civil-engineering/civil-engineering-phd/', 'GRE: optional'),
    ('https://catalog.vt.edu/graduate/degree-programs/materials-science-engineering/materials-science-engineering-phd/', 'Admission application deadlines: Jan 15 for Fall; Sep 15 for Spring'),
    ('https://catalog.vt.edu/graduate/degree-programs/materials-science-engineering/materials-science-engineering-phd/', 'GRE: optional'),
    ('https://me.vt.edu/for-students/graduate/admissions-funding.html', 'January 4, 2027: priority deadline for funding'),
    ('https://me.vt.edu/for-students/graduate/admissions-funding.html', 'The GRE is optional for all applicants.'),
    ('https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html', 'For Fall admissions, the deadline is January 5th at 11:59 PM EST.'),
    ('https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html', 'Submission of GRE general and subject tests is optional.'),
    ('https://www.phys.vt.edu/Graduate/ProspectiveGraduateStudents.html', 'All of our offers include at least five years of support, typically starting with a teaching assistantship. All assistantships include a monthly stipend, full tuition, and a health insurance subsidy of 88% if you are enrolled in the university plan.'),
    ('https://catalog.vt.edu/graduate/degree-programs/chemistry/chemistry-phd/', 'GRE: optional'),
    ('https://catalog.vt.edu/graduate/degree-programs/chemistry/chemistry-phd/', 'Admission application deadlines: Dec 1'),
    ('https://www.math.vt.edu/grads-math/future-grads.html', 'To receive full consideration for admission and graduate assistant support beginning in the Fall term, please apply by January 1st.'),
    ('https://www.math.vt.edu/grads-math/future-grads.html', "We don't require applicants to report GRE scores from the general test or subject test. Students who submit applications without GRE scores will be given equal consideration."),
    ('https://www.math.vt.edu/grads-math/future-grads.html', 'Yes, all graduate students admitted into our graduate program are offered support through a graduate teaching assistnatship (GTA) or a graduate research assistantship (GRA). Assistantships cover the cost of tuition and provide a stipend to cover the cost of living in Blacksburg, VA.'),
    ('https://catalog.vt.edu/graduate/degree-programs/geosciences/geosciences-phd/', 'Admission application deadlines: Jan 5 for Fall; Sep 1 for Spring'),
    ('https://catalog.vt.edu/graduate/degree-programs/geosciences/geosciences-phd/', 'GRE: not needed'),
    ('https://biol.vt.edu/Graduates/how_to_apply.html', 'Fall admissions have a priority deadline of December 1. International applications will be reviewed on a rolling basis until March 31 and domestic applications will be reviewed until May 15.'),
    ('https://biol.vt.edu/Graduates/how_to_apply.html', '■GRE: neither required nor considered when making admissions decisions'),
    ('https://biol.vt.edu/Graduates.html', 'All others receive 12 months of GTA or GRA support'),
    ('https://catalog.vt.edu/graduate/degree-programs/neuroscience-phd/', 'GRE: optional'),
    ('https://catalog.vt.edu/graduate/degree-programs/neuroscience-phd/', 'Admission application deadlines: Dec 1')
]

all_ok = True
for url, q in tests:
    ok, msg = test_quote(url, q)
    if not ok:
        print('FAILED:', msg, '->', q[:60])
        all_ok = False
    else:
        print('PASSED:', q[:50])

print('ALL PASSED?', all_ok)
