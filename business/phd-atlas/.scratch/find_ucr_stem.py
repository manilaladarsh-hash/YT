import json, hashlib

h = hashlib.sha1('https://graduate.ucr.edu/programs'.encode()).hexdigest()[:16]
d = json.load(open(f'.cache/pages/{h}.json', encoding='utf-8'))
for l in d.get('links', []):
    if any(k in l[0].lower() for k in [
        'computer science', 'bioengineering', 'chemical', 'chemistry', 'civil',
        'electrical', 'environmental', 'materials', 'mechanical', 'mathematics',
        'physics', 'astronomy', 'statistics', 'neuroscience', 'biology', 'biomedical'
    ]):
        print(l)
