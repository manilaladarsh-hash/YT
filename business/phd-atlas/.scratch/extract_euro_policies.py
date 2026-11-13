import json, re
from pathlib import Path
from urllib.parse import urlparse

CACHE = Path('.cache/pages')

domains = {
    'heidelberg': ['uni-heidelberg.de'],
    'kit': ['kit.edu'],
    'tuberlin': ['tu.berlin', 'tu-berlin.de'],
    'fuberlin': ['fu-berlin.de'],
    'sorbonne': ['sorbonne-universite.fr', 'sorbonne.fr'],
    'paris-saclay': ['universite-paris-saclay.fr'],
    'stuttgart': ['uni-stuttgart.de'],
    'unibe': ['unibe.ch'],
    'ntnu': ['ntnu.edu', 'ntnu.no'],
    'dtu': ['dtu.dk'],
    'utrecht': ['uu.nl'],
    'leiden': ['universiteitleiden.nl'],
    'lund': ['lu.se', 'lunduniversity.lu.se'],
    'uppsala': ['uu.se'],
    'ugent': ['ugent.be'],
    'upc': ['upc.edu'],
    'chalmers': ['chalmers.se']
}

KEYWORDS = ['application fee', 'tuition fee', 'no tuition', 'exempt', 'gre', 'toefl', 'ielts', 'language certificate', 'proficiency in english', 'admission fee', 'semester fee', 'administrative fee']

results = {k: [] for k in domains}

for p in CACHE.glob('*.json'):
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        url = data.get('url', '')
        text = data.get('text', '')
        if not text:
            continue
        host = urlparse(url).netloc.lower()
        for uni, doms in domains.items():
            if any(dom in host for dom in doms):
                for line in text.splitlines():
                    line_clean = line.strip()
                    if len(line_clean) < 15 or len(line_clean) > 300:
                        continue
                    line_lower = line_clean.lower()
                    for kw in KEYWORDS:
                        if kw in line_lower:
                            results[uni].append((p.name, url, kw, line_clean))
                            break
    except Exception:
        pass

for uni, matches in results.items():
    print(f'=== {uni}: {len(matches)} matches ===')
    seen = set()
    for fname, url, kw, line in matches:
        if line in seen:
            continue
        seen.add(line)
        print(f'[{kw}] ({fname}) {line[:120]}')
        if len(seen) >= 8:
            break
