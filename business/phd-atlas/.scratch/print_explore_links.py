import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('url', '')
    if 'uoregon.edu' in u and 'explore-programs' in u:
        for text, url in rec.get('links', []):
            if any(k in text.lower() or k in url.lower() for k in ['doctoral', 'master', 'program', 'academic']):
                print(f"  {text} -> {url}")
