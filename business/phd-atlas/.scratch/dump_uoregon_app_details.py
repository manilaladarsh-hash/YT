import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

urls = [
    'https://naturalsciences.uoregon.edu/physics/apply',
    'https://scds.uoregon.edu/graduate-programs/admissions',
    'https://naturalsciences.uoregon.edu/mathematics/apply',
    'https://naturalsciences.uoregon.edu/chemistry-biochemistry/apply',
    'https://naturalsciences.uoregon.edu/biology/graduate-programs',
    'https://naturalsciences.uoregon.edu/earth-sciences/apply'
]

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if u in urls:
        print(f"\n==================== {u} ====================")
        for line in rec.get('text', '').split('\n'):
            line = line.strip()
            if any(k in line.lower() for k in ['deadline', 'gre', 'december', 'january', 'february', 'stipend', 'tuition waiver', 'funding', 'assistantship', 'bachelor', 'master', 'advisor', 'supervisor', 'faculty']):
                print("  ", line)
