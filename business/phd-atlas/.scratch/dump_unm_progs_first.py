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
    'biology', 'biomedical-sciences', 'mechanical-engineering'
]

for pr in progs:
    target = f"https://grad.unm.edu/graduate-programs/application-instructions/{pr}.html"
    text = urls.get(target, '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    start = False
    print(f"\n==================== {pr} ====================")
    captured = []
    for l in lines:
        if "Application Deadlines" in l:
            start = True
        if start:
            captured.append(l)
            if "Click here to visit the program website" in l or "ONLINE APPLICATION" in l:
                break
    for l in captured:
        print("  ", l)
