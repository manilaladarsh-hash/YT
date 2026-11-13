import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if 'uoregon.edu' in u and 'naturalsciences' in u:
        text = rec.get('text', '')
        for line in text.split('\n'):
            line = line.strip()
            if any(k in line.lower() for k in ['deadline', 'gre', 'toefl', 'application process', 'how to apply', 'december', 'january']):
                print(f"[{u.split('/')[-2]}/{u.split('/')[-1]}] {line}")
