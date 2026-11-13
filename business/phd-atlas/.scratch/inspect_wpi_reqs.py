import json

data = json.load(open('.cache/pages/307454e2314cb615.json', 'r', encoding='utf-8'))
text = data.get('text', '')
lines = text.splitlines()

print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines):
    if any(k in line.lower() for k in ['deadline', 'gre', 'funding', 'assistantship', 'stipend', 'supervisor', 'bachelor', 'master', 'doctoral', 'phd']):
        print(f"[{i}] {line[:120]}")
