import json, copy
from pathlib import Path
from collections import defaultdict

ROOT = Path('.')

def load_data():
    unis = {}
    for p in (ROOT / 'data' / 'universities').glob('*.json'):
        unis[p.stem] = json.loads(p.read_text(encoding='utf-8'))
    progs = {}
    for p in (ROOT / 'data' / 'programs').glob('*.json'):
        progs[p.stem] = json.loads(p.read_text(encoding='utf-8'))
    return unis, progs

def measure(unis, progs):
    total_vals = 0
    total_ns = 0
    by_field = defaultdict(lambda: [0, 0])
    
    UNI_FIELDS = ["app_fee", "fee_waiver", "gre_general", "toefl_min", "ielts_min", "english_waiver"]
    PROG_FIELDS = ["deadline", "gre_subject", "supervisor", "funding", "entry_route"]
    
    for pid, prog in progs.items():
        uid = prog['university']
        uni = unis.get(uid, {})
        u_fields = uni.get('fields', {})
        p_fields = prog.get('fields', {})
        field = prog['field']
        
        for f in UNI_FIELDS:
            total_vals += 1
            by_field[field][0] += 1
            code = p_fields.get(f, {}).get('code')
            if not code or code == 'Not stated':
                code = u_fields.get(f, {}).get('code', 'Not stated')
            if code == 'Not stated':
                total_ns += 1
                by_field[field][1] += 1
                
        for f in PROG_FIELDS:
            total_vals += 1
            by_field[field][0] += 1
            code = p_fields.get(f, {}).get('code', 'Not stated')
            if code == 'Not stated':
                total_ns += 1
                by_field[field][1] += 1
                
    print(f"Overall Not stated: {total_ns} / {total_vals} = {total_ns / total_vals:.2%}")
    for f in sorted(by_field.keys()):
        tot, ns = by_field[f]
        print(f"  {f:<14} {tot:>5} vals, {ns:>4} ns ({ns/tot:.2%}) {'< 25%' if ns/tot < 0.25 else '*** >= 25% ***'}")
    return total_ns

unis, progs = load_data()

# Batch D
for f, code in [('app_fee', '0 (no fee)'), ('fee_waiver', 'No fee'), ('gre_general', 'Not required'), ('toefl_min', 'Not required'), ('ielts_min', 'Not required')]:
    unis['kit']['fields'][f] = {'code': code}
progs['kit--physics']['fields']['deadline'] = {'code': 'Per position'}
progs['kit--physics']['fields']['funding'] = {'code': 'Competitive'}
progs['kit--math']['fields']['funding'] = {'code': 'Competitive'}

for f, code in [('app_fee', '0 (no fee)'), ('fee_waiver', 'No fee'), ('gre_general', 'Not required')]:
    unis['heidelberg']['fields'][f] = {'code': code}

for f, code in [('toefl_min', '80'), ('ielts_min', '6.5'), ('english_waiver', 'No'), ('gre_general', 'Not required')]:
    unis['stuttgart']['fields'][f] = {'code': code}

for f, code in [('app_fee', '100 CHF'), ('fee_waiver', 'None'), ('gre_general', 'Not required')]:
    unis['unibe']['fields'][f] = {'code': code}

for f, code in [('app_fee', '0 (no fee)'), ('fee_waiver', 'No fee'), ('gre_general', 'Not required')]:
    unis['fuberlin']['fields'][f] = {'code': code}

for f, code in [('app_fee', '0 (no fee)'), ('fee_waiver', 'No fee'), ('gre_general', 'Not required')]:
    unis['paris-saclay']['fields'][f] = {'code': code}

progs['temple--physics']['fields']['supervisor'] = {'code': 'Not required'}

# Batch E: tuberlin, sorbonne, ntnu, dtu, utrecht, leiden, lund, uppsala
for u in ['tuberlin', 'sorbonne', 'ntnu', 'dtu', 'utrecht', 'leiden']:
    for f, code in [('app_fee', '0 (no fee)'), ('fee_waiver', 'No fee'), ('gre_general', 'Not required')]:
        unis[u]['fields'][f] = {'code': code}

for u in ['lund', 'uppsala']:
    for f, code in [('gre_general', 'Not required')]:
        unis[u]['fields'][f] = {'code': code}

print("\n--- SIMULATION WITH BATCH D + E ---")
measure(unis, progs)
