import hashlib
import json

checks = [
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5290&returnto=1015', 'Application deadline: January 15, then rolling if space is available'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5487&returnto=1015', 'All chemistry students must select a research advisor and advisory committee by the end of the first semester of graduate study and thereafter meet with the committee at least once each year.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5243&returnto=1015', 'Application deadline: January 15 for funding consideration | April 1 (Fall) / November 1 (Spring/Summer)'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5253&returnto=1015', 'Application deadline: Rolling'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5253&returnto=1015', 'Graduate assistantships and a limited number of teaching assistantships are available. Graduate research assistantships are contingent on funding.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5494&returnto=1015', 'Research and teaching assistantships are available; contact Graduate Coordinator for additional details'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5237&returnto=1015', 'Application deadline: December 20 (Fall)/September 30 (Spring)'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5237&returnto=1015', 'The Ph.D. degree requires a minimum of 45 semester hours, beyond the B.S. level, comprising four seminars and at least eight graduate courses (24 credits) in addition to a research thesis.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5239&returnto=1015', 'Application deadline: Rolling'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5239&returnto=1015', 'Test Required: GRE recommended but not required for admission.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5235&returnto=1015', 'Application deadline: December 1'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015', 'Application deadline: January 15 (Fall) / November 15 (Spring)'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015', 'Applicants need to identify an area of research interest and a potential advisor at the time of application; they should feel free to contact members of the faculty to discuss possible research projects before submission of the application. A research project is a central part of the PhD degree.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5234&returnto=1015', 'All applicants will be automatically considered for teaching or research assistantships. Many students are supported by research grants to individual faculty members; interested students should contact faculty members directly for further information on grant-supported assistantships.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5247&returnto=1015', 'Application deadline: January 15 (Fall), then rolling if space is available / November 30 (Spring), then rolling if space is available'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5247&returnto=1015', 'The PhD requires the completion of at least 15 credits of coursework beyond a master’s degree, and 33 credits if entering with a bachelor’s degree; all PhD students must take at least 9 thesis credits.'),
    ('https://gradcatalog.umaine.edu/preview_program.php?catoid=41&poid=5248&returnto=1015', 'Application deadline: January 15 / November 1'),
]

for u, q in checks:
    k = hashlib.sha1(u.encode()).hexdigest()[:16]
    with open(f'.cache/pages/{k}.json', encoding='utf-8') as f:
        d = json.load(f)
    print(f"{q in d['text']}: {q[:50]}...")
