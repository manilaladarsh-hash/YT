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
    print(f"**************** {pr} ****************")
    for line in text.split('\n'):
        l = line.strip()
        if any(w in l.lower() for w in ['deadline', 'gre', 'assistantship', 'funding', 'financial']):
            print("  ", l)
