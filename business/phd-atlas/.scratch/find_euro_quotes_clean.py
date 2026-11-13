import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
CACHE = Path('.cache/pages')

unis_to_check = {
    'tuberlin': 'tu.berlin',
    'sorbonne': 'sorbonne-universite.fr',
    'ntnu': 'ntnu.edu',
    'dtu': 'dtu.dk',
    'utrecht': 'uu.nl',
    'leiden': 'universiteitleiden.nl',
    'lund': 'lu.se',
    'uppsala': 'uu.se'
}

for uid, domain in unis_to_check.items():
    print(f"\n====================== {uid.upper()} ======================")
    matching = []
    for cp in CACHE.glob('*.json'):
        try:
            d = json.loads(cp.read_text(encoding='utf-8'))
            url = d.get('url', '')
            if domain in url:
                text = d.get('text', '')
                for line in text.splitlines():
                    ls = line.strip()
                    if any(w in ls.lower() for w in ['tuition fee', 'no tuition', 'application fee', 'no fee', 'gre', 'administrative fee', 'semester fee', 'toefl', 'ielts']):
                        if 15 < len(ls) < 200:
                            matching.append((cp.name, url, ls))
        except Exception:
            pass
    seen = set()
    for fname, url, ls in matching:
        if ls in seen:
            continue
        seen.add(ls)
        print(f"[{fname}] {ls}")
        print(f"   URL: {url}")
        if len(seen) >= 6:
            break
