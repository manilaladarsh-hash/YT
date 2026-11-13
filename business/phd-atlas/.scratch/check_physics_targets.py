import json
from pathlib import Path

ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

progs = {}
for p in (ROOT / 'data' / 'programs').glob('*--physics.json'):
    progs[p.stem] = json.loads(p.read_text(encoding='utf-8'))

unis = {}
for p in (ROOT / 'data' / 'universities').glob('*.json'):
    unis[p.stem] = json.loads(p.read_text(encoding='utf-8'))

UNI_FIELDS = ["app_fee", "fee_waiver", "gre_general", "toefl_min", "ielts_min", "english_waiver"]
PROG_FIELDS = ["deadline", "gre_subject", "supervisor", "funding", "entry_route"]

results = []
for pid, p in progs.items():
    uid = p['university']
    u = unis.get(uid, {})
    u_f = u.get('fields', {})
    p_f = p.get('fields', {})
    
    missing = []
    for f in UNI_FIELDS:
        code = p_f.get(f, {}).get('code') or u_f.get(f, {}).get('code')
        if not code or code == 'Not stated':
            missing.append(f"uni:{f}")
    for f in PROG_FIELDS:
        code = p_f.get(f, {}).get('code')
        if not code or code == 'Not stated':
            missing.append(f"prog:{f}")
    if missing:
        results.append((len(missing), pid, p['program_page'], missing))

results.sort(reverse=True)
for count, pid, page, missing in results[:20]:
    print(f"{pid:<22} ({count} missing): {', '.join(missing)}")
    print(f"   Page: {page}")
