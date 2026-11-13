import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'application-fee-waivers-discounts' in u:
        text = rec.get('text', '')
        for line in text.split('\n'):
            line = line.strip()
            if line:
                print(line)
