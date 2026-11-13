import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if u == 'https://viterbigradadmission.usc.edu/':
        for text, link in rec.get('links', []):
            if any(k in text.lower() or k in link.lower() for k in ['phd', 'doctoral', 'deadline', 'step', 'requirement', 'degree']):
                print(f"  {text} -> {link}")
