import json

data = json.load(open('.cache/pages/ec36b14bb02ece73.json', 'r', encoding='utf-8'))
text = data.get('text', '')
lines = text.splitlines()

# Search for the sections for each PhD
phd_indices = [i for i, l in enumerate(lines) if 'Ph.D.' in l]
for idx in phd_indices:
    print("="*60)
    start = max(0, idx - 1)
    end = min(len(lines), idx + 25)
    print("\n".join(lines[start:end]))
