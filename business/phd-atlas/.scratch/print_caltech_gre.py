import json, hashlib, re

h = hashlib.sha1('https://www.gradoffice.caltech.edu/documents/35541/New_Updated_GRE2026.pdf'.encode()).hexdigest()[:16]
d = json.load(open(f'.cache/pages/{h}.json', encoding='utf-8'))
t = d['text']
print("PDF text length:", len(t))
for line in t.split('\n'):
    line = line.strip()
    if line:
        print(" ", line)
