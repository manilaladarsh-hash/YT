import hashlib
import json

checks = [
    ('https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions', 'Applications for Fall 2027 open on September 1st, 2026 and will close on November 13th, 2026.'),
    ('https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions', 'Are GRE scores required?\nNo.'),
    ('https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions', 'An admitted applicant is expected to have a TOEFL score above 80 (iBT), 550 (paper-based), or an IELTS score above 6.5.'),
    ('https://www.ohsu.edu/school-of-medicine/biomedical-sciences-graduate-program/admissions', 'A baccalaureate degree or equivalent, from an accredited U.S. academic institution, or equivalent international institution in chemistry, physics or one of the biological, medical sciences.'),
    ('https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions', 'We encourage prospective Ph.D. students to apply by Dec. 10 to start in the fall of the following year. We also accept applications year-round and review off-cycle applications three months prior to the start of each term.'),
    ('https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions', 'We provide a stipend to all students in our program. Please see the stipend policy for current rates. All tuition and student fees are waived for full-time students who are members of Graduate Researchers United. Students are also eligible for health and dental insurance.'),
    ('https://www.ohsu.edu/school-of-medicine/biomedical-engineering/admissions', 'What GRE score do I need? Do I need to complete a GRE subject test?\nWe do not require the GRE and there are no GRE subject test requirements.'),
    ('https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information', 'The $70.00 application fee is due by December 1st, along with all other application components.'),
    ('https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information', 'Tuition, fees, and health insurance is entirely covered for students. After the first year, students join a lab and are funded through the lab or the department.'),
    ('https://www.ohsu.edu/school-of-medicine/neuroscience-graduate-program/application-information', 'GRE score submission is optional and scores are not used as a component in the NGP\u2019s application review process.'),
    ('https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements', 'Applications are due Jan. 15.'),
    ('https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements', 'GRE scores. No minimum score required. At-home test accepted.'),
    ('https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements', 'Internet-Based (iBT): For exams taken before January 2026: minimum total score of 90; minimum section scores of:'),
    ('https://www.ohsu.edu/school-of-medicine/medical-physics-graduate-program/admission-requirements', 'IELTS: Overall score of 6.5'),
    ('https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information', 'Terms begin in July. You can apply from Sept. 1 through Dec. 1.'),
    ('https://www.ohsu.edu/school-of-medicine/medical-informatics-and-clinical-epidemiology/admissions-information', 'Our program pairs you with a mentor with whom you will work closely. You\u2019ll be asked to name and rank two or three faculty members who could be potential mentors.')
]

for u, q in checks:
    k = hashlib.sha1(u.encode()).hexdigest()[:16]
    with open(f'.cache/pages/{k}.json', encoding='utf-8') as f:
        d = json.load(f)
    print(f"{q in d['text']}: {q[:50]}...")
