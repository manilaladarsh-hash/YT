import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'apply-now.html' in u:
        text = rec.get('text', '')
        for line in text.split('\n'):
            if 'application fee' in line.lower() or '60' in line:
                print('apply-now line:', repr(line.strip()))
    if 'physics.html' in u:
        text = rec.get('text', '')
        for line in text.split('\n'):
            if 'assistantship' in line.lower() or 'financial aid' in line.lower():
                print('physics line:', repr(line.strip()))
    if 'biology.html' in u:
        text = rec.get('text', '')
        for line in text.split('\n'):
            if 'gre' in line.lower():
                print('biology line:', repr(line.strip()))
