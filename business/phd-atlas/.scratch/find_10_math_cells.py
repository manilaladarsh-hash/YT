import json, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

progs = [json.loads(p.read_text(encoding='utf-8')) for p in Path('data/programs').glob('*--math.json')]
unis = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in Path('data/universities').glob('*.json')}

UNI_FIELDS = ["app_fee", "fee_waiver", "gre_general", "toefl_min", "ielts_min", "english_waiver"]
PROG_FIELDS = ["deadline", "gre_subject", "supervisor", "funding", "entry_route"]

missing_by_prog = []
for p in progs:
    uid = p['university']
    u = unis.get(uid, {})
    u_f = u.get('fields', {})
    p_f = p.get('fields', {})
    
    missing = []
    for f in UNI_FIELDS:
        c = p_f.get(f, {}).get('code') or u_f.get(f, {}).get('code')
        if not c or c == 'Not stated':
            missing.append(f"uni:{f}")
    for f in PROG_FIELDS:
        c = p_f.get(f, {}).get('code')
        if not c or c == 'Not stated':
            missing.append(f"prog:{f}")
    if missing:
        missing_by_prog.append((len(missing), p['id'], p['program_page'], missing))

missing_by_prog.sort(reverse=True)
for count, pid, page, missing in missing_by_prog[:20]:
    print(f"{pid:<20} ({count} missing): {', '.join(missing)}")
    print(f"   Page: {page}")
