import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'international-applicants' in u:
        print("keys:", list(rec.keys()))
        print("html in rec:", 'html' in rec, len(rec.get('html', '')))
