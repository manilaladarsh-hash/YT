with open('.scratch/save_wayne_programs.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('"entry_route": "Either"', '"entry_code": "Either"')

with open('.scratch/save_wayne_programs.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed")
