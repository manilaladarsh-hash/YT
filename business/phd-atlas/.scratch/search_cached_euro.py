import json, os
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

cached_by_uni = {k: [] for k in domains}

for p in CACHE.glob('*.json'):
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        url = data.get('url', '')
        host = urlparse(url).netloc.lower()
        for uni, doms in domains.items():
            if any(dom in host for dom in doms):
                cached_by_uni[uni].append((p.name, url))
    except Exception as e:
        pass

for uni, urls in cached_by_uni.items():
    print(f'=== {uni} ({len(urls)} cached pages) ===')
    for name, url in urls[:5]:
        print(f'  {name}: {url}')
