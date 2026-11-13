import json

with open('.cache/pages/d4ec329dac6a3ff2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("URL:", data.get('url'))
print("Final URL:", data.get('final_url'))
links = data.get('links', [])
for item in links:
    if isinstance(item, list) and len(item) == 2:
        text, href = item
    else:
        text, href = "", str(item)
    if any(k in href.lower() or k in text.lower() for k in ['deadline', 'requirement', 'phd', 'degree', 'program', 'table', 'academics']):
        print(f"  {text} -> {href}")
