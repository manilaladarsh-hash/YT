import json

data = json.load(open('.cache/pages/ec36b14bb02ece73.json', 'r', encoding='utf-8'))
lines = data.get('text', '').splitlines()

for i, l in enumerate(lines[:150]):
    clean = l.encode('ascii', errors='replace').decode('ascii')
    print(f"{i}: {clean}")
