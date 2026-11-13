import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'uoregon.edu' in u:
        print("URL:", u)
        print("Final URL:", rec.get('final_url'))
        for line in rec.get('text', '').split('\n'):
            line = line.strip()
            if any(k in line.lower() for k in ['fee', 'waiver', '$', 'toefl', 'ielts', 'duolingo', 'english']):
                print("  ", line)
