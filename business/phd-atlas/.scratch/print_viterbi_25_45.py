import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if u == 'https://viterbigradadmission.usc.edu/':
        lines = [l.strip() for l in rec.get('text', '').split('\n') if l.strip()]
        for i in range(25, 45):
            if i < len(lines):
                print(f"{i}: {lines[i]}")
