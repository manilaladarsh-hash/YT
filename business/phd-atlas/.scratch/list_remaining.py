import json
from pathlib import Path

with open('data/universities.json', 'r', encoding='utf-8') as f:
    listed = json.load(f)['universities']

existing = {p.stem for p in Path('data/universities').glob('*.json')}
missing = [u for u in listed if u['id'] not in existing]
print(f"Remaining: {len(missing)}")
for u in missing:
    print(f"{u['id']}: {u['name']} ({u['country']}) [wave {u.get('wave')}]")
