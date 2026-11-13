import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'grad.unm.edu/graduate-programs/application-instructions/' in u:
        urls[u] = rec.get('text', '')

for pr in ['chemistry-chemical-biology', 'biology', 'biomedical-sciences', 'mechanical-engineering']:
    target = f"https://grad.unm.edu/graduate-programs/application-instructions/{pr}.html"
    text = urls.get(target, '')
    print(f"=== {pr} ===")
    for line in text.split('\n'):
        if any(w in line.lower() for w in ['gre', 'december', 'january 1st', 'not required but is recommended']):
            print("  ", repr(line.strip()))
