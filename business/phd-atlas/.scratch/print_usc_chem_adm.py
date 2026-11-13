import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import json
from pathlib import Path

for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    u = rec.get('final_url', rec.get('url', ''))
    if 'chemistry/graduate-admission' in u:
        for line in rec.get('text', '').split('\n'):
            line = line.strip()
            if any(k in line.lower() for k in ['gre', 'stipend', 'tuition', 'support', 'funding', 'fellowship', 'assistantship', 'fee', 'deadline']):
                print(line)
