import json
from pathlib import Path

uni_list = json.load(open('data/universities.json'))['universities']
live_ids = {p.stem for p in Path('data/universities').glob('*.json')}

remaining = [u for u in uni_list if u['id'] not in live_ids]
print(f"Total remaining: {len(remaining)}")
for r in remaining:
    print(f"  {r['id']}: {r['name']} ({r['country']}, wave {r.get('wave')})")
