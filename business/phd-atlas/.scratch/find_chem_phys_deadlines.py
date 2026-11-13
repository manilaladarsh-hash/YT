import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if 'chemistry-biochemistry/apply/graduate-admissions' in u:
        print("=== CHEMISTRY ===")
        for line in rec.get('text', '').split('\n'):
            if any(k in line.lower() for k in ['deadline', 'december', 'january', 'february', 'fall']):
                print("  ", line.strip())
    if 'physics/apply/graduate-admissions' in u:
        print("=== PHYSICS ===")
        for line in rec.get('text', '').split('\n'):
            if any(k in line.lower() for k in ['deadline', 'december', 'january', 'february', 'fall']):
                print("  ", line.strip())
