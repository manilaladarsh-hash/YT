import json
from pathlib import Path

with open('data/universities.json', encoding='utf-8') as f:
    target_unis = json.load(f)['universities']

existing_uni_records = {p.stem for p in Path('data/universities').glob('*.json')}
existing_progs = {p.stem.split('--')[0] for p in Path('data/programs').glob('*.json')}

missing_uni_records = [u for u in target_unis if u['id'] not in existing_uni_records]
missing_progs = [u for u in target_unis if u['id'] not in existing_progs]

print(f"Total target universities: {len(target_unis)}")
print(f"Existing uni records: {len(existing_uni_records)}")
print(f"Existing unis with progs: {len(existing_progs)}")
print(f"\nMissing uni records ({len(missing_uni_records)}):")
for u in missing_uni_records:
    print(f"  {u['id']}: {u['name']} ({u['country']})")

print(f"\nMissing progs ({len(missing_progs)}):")
for u in missing_progs:
    print(f"  {u['id']}: {u['name']} ({u['country']})")
