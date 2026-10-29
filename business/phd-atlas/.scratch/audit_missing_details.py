import json
from pathlib import Path

ROOT = Path('.')

progs = {}
for p in (ROOT / 'data' / 'programs').glob('*.json'):
    progs[p.stem] = json.loads(p.read_text(encoding='utf-8'))

unis = {}
for p in (ROOT / 'data' / 'universities').glob('*.json'):
    unis[p.stem] = json.loads(p.read_text(encoding='utf-8'))

CACHE = ROOT / '.cache' / 'pages'

print("=== REMAINING MISSING IN MATH ===")
math_missing = []
for pid, prog in sorted(progs.items()):
    if prog['field'] == 'math':
        ns = []
        for f in ['deadline', 'gre_subject', 'supervisor', 'funding', 'entry_route']:
            if prog['fields'].get(f, {}).get('code') == 'Not stated':
                ns.append(f)
        if ns:
            math_missing.append((pid, prog['program_page'], ns))

for pid, url, ns in math_missing[:25]:
    print(f"{pid:<20} {', '.join(ns):<30} {url}")

print(f"\nTotal math programs with missing fields: {len(math_missing)}")

print("\n=== REMAINING MISSING IN PHYSICS ===")
phys_missing = []
for pid, prog in sorted(progs.items()):
    if prog['field'] == 'physics':
        ns = []
        for f in ['deadline', 'gre_subject', 'supervisor', 'funding', 'entry_route']:
            if prog['fields'].get(f, {}).get('code') == 'Not stated':
                ns.append(f)
        if ns:
            phys_missing.append((pid, prog['program_page'], ns))

for pid, url, ns in phys_missing[:25]:
    print(f"{pid:<20} {', '.join(ns):<30} {url}")

print(f"\nTotal physics programs with missing fields: {len(phys_missing)}")
