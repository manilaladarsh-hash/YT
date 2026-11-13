import urllib.request, ssl

ctx = ssl.create_default_context()
urls = [
    ('cs', 'https://vds-cs.univie.ac.at/'),
    ('math', 'https://vds-mathematics.univie.ac.at/'),
    ('physics', 'https://vds-physics.univie.ac.at/'),
    ('chemistry', 'https://doschem.univie.ac.at/'),
    ('biology', 'https://vds-lifesciences.univie.ac.at/'),
    ('neuro', 'https://vds-cobene.univie.ac.at/'),
    ('earth', 'https://vds-esga.univie.ac.at/'),
    ('astronomy', 'https://astro.univie.ac.at/'),
    ('environment', 'https://vds-mes.univie.ac.at/')
]

for name, u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            print(f'{name}: {r.status} -> {r.geturl()}')
    except Exception as e:
        print(f'{name}: {e}')
