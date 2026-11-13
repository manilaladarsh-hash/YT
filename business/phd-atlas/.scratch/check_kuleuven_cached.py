import json, glob

url_map = {
    'astronomy': 'https://fys.kuleuven.be/ster',
    'biology': 'https://bio.kuleuven.be/',
    'bme': 'https://www.mech.kuleuven.be/en/bme',
    'chemeng': 'https://cit.kuleuven.be/english',
    'chemistry': 'https://chem.kuleuven.be/en',
    'civil': 'https://bwk.kuleuven.be/',
    'cs': 'https://wms.cs.kuleuven.be/cs/english/research/phd',
    'earth': 'https://ees.kuleuven.be/en',
    'ece': 'https://www.esat.kuleuven.be/english',
    'materials': 'https://www.mtm.kuleuven.be/',
    'math': 'https://wis.kuleuven.be/english',
    'mech': 'https://www.mech.kuleuven.be/en',
    'neuro': 'https://gbiomed.kuleuven.be/english/research/50000666',
    'physics': 'https://fys.kuleuven.be/english',
    'statistics': 'https://lstat.kuleuven.be/'
}

cached = {}
for f in glob.glob('.cache/pages/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    u = d.get('url')
    if u:
        cached[u] = f

for field, u in url_map.items():
    hit = u in cached or u.rstrip('/') in cached or (u + '/') in cached
    print(f"{field}: {u} -> {'CACHED' if hit else 'MISSING'}")
