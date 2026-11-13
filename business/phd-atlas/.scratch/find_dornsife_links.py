import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

urls = [
    'https://dornsife.usc.edu/chemistry/',
    'https://dornsife.usc.edu/mathematics/',
    'https://dornsife.usc.edu/earth/graduate/'
]

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if u in urls:
        print(f"\n=== {u} ===")
        for text, link in rec.get('links', []):
            if any(k in text.lower() or k in link.lower() for k in ['grad', 'phd', 'apply', 'admiss']):
                print(f"  {text} -> {link}")
