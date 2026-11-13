import json

data = json.load(open('.cache/pages/307454e2314cb615.json', 'r', encoding='utf-8'))
lines = data.get('text', '').splitlines()

# Search for lines that end with "PhD" or "Ph.D." or "PhD in ..."
phd_blocks = []
for i, line in enumerate(lines):
    l = line.strip()
    if ('PhD' in l or 'Ph.D.' in l) and len(l) < 50:
        phd_blocks.append((i, l))

print(f"Found {len(phd_blocks)} PhD matches:")
for idx, name in phd_blocks:
    print("="*60)
    print(f"Line {idx}: {name}")
    start = max(0, idx - 2)
    end = min(len(lines), idx + 25)
    for k in range(start, end):
        clean = lines[k].encode('ascii', errors='replace').decode('ascii')
        print(f"  [{k}] {clean}")
