import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'grad.unm.edu/graduate-programs/application-instructions/' in u:
        urls[u] = rec.get('text', '')

progs = [
    'physics', 'computer-science', 'chemistry-chemical-biology', 'mathematics',
    'biology', 'biomedical-sciences', 'biomedical-engineering', 'chemical-engineering',
    'civil-construction-environmental-engineering', 'electrical-engineering', 'mechanical-engineering'
]

for pr in progs:
    target = f"https://grad.unm.edu/graduate-programs/application-instructions/{pr}.html"
    text = urls.get(target, '')
    print(f"\n==================== {pr} ====================")
    # find lines between Application Deadlines and Application Requirements or similar
    lines = text.split('\n')
    for i, l in enumerate(lines):
        if any(h in l for h in ['Application Deadlines', 'Application Requirements', 'GRE', 'Assistantship', 'Financial Aid', 'Contact Information and Application Instructions']):
            # print snippet around it
            sub = [s.strip() for s in lines[max(0, i-2):min(len(lines), i+8)] if s.strip()]
            for s in sub:
                if len(s) < 200:
                    print("  ", s)
            print("  ---")
