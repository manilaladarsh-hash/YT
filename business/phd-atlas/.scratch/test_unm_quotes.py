import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'unm.edu' in u:
        urls[u] = rec.get('text', '')

print(f"Total UNM cached URLs: {len(urls)}")
for u in urls:
    print(u)
