from collections import defaultdict
import json, os

unis = {p.replace('.json', ''): json.load(open(f'data/universities/{p}', encoding='utf-8')) for p in os.listdir('data/universities') if p.endswith('.json')}
progs = {p.replace('.json', ''): json.load(open(f'data/programs/{p}', encoding='utf-8')) for p in os.listdir('data/programs') if p.endswith('.json')}

per_field = defaultdict(lambda: [0, 0])
UNI_FIELDS = ['app_fee', 'fee_waiver', 'gre_general', 'toefl_min', 'ielts_min', 'english_waiver']
PROG_FIELDS = ['deadline', 'gre_subject', 'supervisor', 'funding', 'entry_route']

for pid, p in progs.items():
    f = p['field']
    u = unis.get(p['university'], {})
    uf = u.get('fields', {})
    pf = p.get('fields', {})
    for k in UNI_FIELDS:
        code = pf.get(k, {}).get('code') or uf.get(k, {}).get('code', 'Not stated')
        per_field[f][0] += 1
        if code == 'Not stated':
            per_field[f][1] += 1
    for k in PROG_FIELDS:
        code = pf.get(k, {}).get('code', 'Not stated')
        per_field[f][0] += 1
        if code == 'Not stated':
            per_field[f][1] += 1

all_passed = True
print(f'Total fields: {len(per_field)}')
for f in sorted(per_field.keys()):
    tot, ns = per_field[f]
    pct = ns / tot
    passed = pct < 0.25
    if not passed:
        all_passed = False
    print(f'  {f:<14}: {ns:>4}/{tot:>4} = {pct:>6.2%}  {"PASS" if passed else "FAIL"}')

print(f'\nALL 18 FIELDS < 25%: {all_passed}')
