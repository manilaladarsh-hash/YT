import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

pages = [
    'https://naturalsciences.uoregon.edu/biology',
    'https://naturalsciences.uoregon.edu/chemistry-biochemistry',
    'https://naturalsciences.uoregon.edu/mathematics',
    'https://naturalsciences.uoregon.edu/earth-sciences',
    'https://naturalsciences.uoregon.edu/physics'
]

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if u in pages:
        print(f"\n=== {u} ===")
        for text, link in rec.get('links', []):
            if 'apply' in text.lower() or 'apply' in link.lower() or 'admiss' in text.lower():
                print(f"  {text} -> {link}")
