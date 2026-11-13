import json
import hashlib
import sys

key = hashlib.sha1('https://uwyo.catalog.acalog.com/content.php?catoid=19&navoid=2018'.encode()).hexdigest()[:16]
with open(f'.cache/pages/{key}.json', encoding='utf-8') as f:
    text = json.load(f)['text']

with open('.scratch/uwyo_adm.txt', 'w', encoding='utf-8') as out:
    out.write(text)

print("Wrote .scratch/uwyo_adm.txt. Length:", len(text))
for line in text.split('\n'):
    l = line.lower()
    if any(k in l for k in ['fee', 'waiver', 'toefl', 'ielts', 'gre', 'english', 'deadline', '50']):
        print('  •', line.strip()[:140])
