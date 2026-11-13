import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'unm.edu' in u:
        urls[u] = rec.get('text', '')

checks = [
    ("https://grad.unm.edu/graduate-programs/application-instructions/physics.html", "December 19th"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/physics.html", "General GRE test and Physics GRE subject test scores are optional."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/physics.html", "Depending upon budgetary restrictions, we provide TAs for up to two years"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/computer-science.html", "Priority Deadline: January 15th"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/computer-science.html", "GRE scores are optional; however, submitting strong scores may strengthen your application"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/computer-science.html", "Teaching assistantships are limited in number and the selection process is very competitive."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/chemistry-chemical-biology.html", "December 1"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/chemistry-chemical-biology.html", "The GRE is not required but is recommended."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/mathematics.html", "February 15th"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/mathematics.html", "GRE scores are not required."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/mathematics.html", "If you are interested in an assistantship, please indicate in your letter of intent."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biology.html", "Priority Deadline: December 1st"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biology.html", "The GRE is optional. GRE scores will not be considered in the admission process"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biology.html", "Please let the program know if you would like to receive assistantship funding as you pursue your degree."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biomedical-sciences.html", "December 1st"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biomedical-sciences.html", "GRE scores are optional and should only be submitted if they strengthen your application package."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biomedical-engineering.html", "Priority Date for Financial Aid Consideration: January 15th"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/biomedical-engineering.html", "GRE scores are not required at this time."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/chemical-engineering.html", "Priority: January 15th"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/chemical-engineering.html", "The General GRE exam is required. The institution code is 4845. No subject code is required."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/civil-construction-environmental-engineering.html", "International and Domestic Students: January 31st"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/civil-construction-environmental-engineering.html", "GRE required. A minimum combined score of 300 on the verbal and quantitative sections is required."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/civil-construction-environmental-engineering.html", "To be considered for assistantships, applications should be received by the deadlines indicated above."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/electrical-engineering.html", "Best Consideration if Seeking Financial Aid (Domestic and International): January 31st"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/electrical-engineering.html", "Assistantships are limited and selection process is very competitive."),
    ("https://grad.unm.edu/graduate-programs/application-instructions/mechanical-engineering.html", "Domestic and International applicants requesting financial aid: January 1st"),
    ("https://grad.unm.edu/graduate-programs/application-instructions/mechanical-engineering.html", "GRE scores are required and should be submitted to the University directly by ETS"),
]

all_ok = True
for u, q in checks:
    t = urls.get(u, '')
    if q not in t:
        print(f"FAILED: {q!r} NOT in {u}")
        all_ok = False
    else:
        print(f"OK: {q[:30]}... in {u.split('/')[-1]}")

if all_ok:
    print("\nALL PROGRAM QUOTES VERIFIED!")
