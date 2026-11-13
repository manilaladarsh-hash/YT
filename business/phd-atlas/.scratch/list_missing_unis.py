import json, os

with open('data/universities.json', encoding='utf-8') as f:
    d = json.load(f)

unis = d['universities']
existing_uni_files = set(p.replace('.json', '') for p in os.listdir('data/universities') if p.endswith('.json'))
prog_files = os.listdir('data/programs')
uni_with_progs = set(p.split('--')[0] for p in prog_files if '--' in p)

print(f"Total universities in plan: {len(unis)}")
for u in unis:
    uid = u['id']
    if uid not in existing_uni_files:
        print(f"Wave {u.get('wave')}: {uid} ({u['name']}, {u['country']}) - NO UNI FILE")
    elif uid not in uni_with_progs:
        print(f"Wave {u.get('wave')}: {uid} ({u['name']}, {u['country']}) - NO PROGRAMS")
