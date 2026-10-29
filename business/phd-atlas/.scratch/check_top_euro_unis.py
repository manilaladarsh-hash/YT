import json, os
from pathlib import Path

ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

unis = ['heidelberg', 'kit', 'tuberlin', 'fuberlin', 'sorbonne', 'paris-saclay', 'stuttgart', 'unibe', 'ntnu', 'dtu', 'utrecht', 'leiden', 'lund', 'uppsala', 'ugent', 'upc', 'chalmers']

for u in unis:
    uni_file = ROOT / 'data' / 'universities' / f'{u}.json'
    if not uni_file.exists():
        print(f'{u}: NO FILE')
        continue
    data = json.loads(uni_file.read_text(encoding='utf-8'))
    grad_page = data.get('grad_page', '')
    ns_fields = [k for k, v in data.get('fields', {}).items() if v.get('code') == 'Not stated']
    print(f'{u}: {len(ns_fields)} Not stated ({", ".join(ns_fields)}), grad_page: {grad_page}')
