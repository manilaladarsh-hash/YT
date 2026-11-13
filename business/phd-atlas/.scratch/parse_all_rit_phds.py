import json

data = json.load(open('.cache/pages/ec36b14bb02ece73.json', 'r', encoding='utf-8'))
lines = data.get('text', '').splitlines()

phd_indices = [i for i, l in enumerate(lines) if 'Ph.D.' in l]
for idx in phd_indices:
    name = lines[idx].strip()
    block = lines[idx:idx+20]
    print("="*60)
    print("PROGRAM:", name)
    for j, b in enumerate(block):
        print(f"  [{j}] {b.strip()}")
