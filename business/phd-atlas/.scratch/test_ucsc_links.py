import urllib.request, ssl

ctx = ssl.create_default_context()
urls = [
    ('astronomy', 'https://www.astro.ucsc.edu/'),
    ('biology', 'https://www.eeb.ucsc.edu/'),
    ('biomed', 'https://pbse.ucsc.edu/'),
    ('bme', 'https://engineering.ucsc.edu/departments/biomolecular-engineering/'),
    ('chemistry', 'https://chemistry.ucsc.edu/'),
    ('cs', 'https://engineering.ucsc.edu/departments/computer-science-and-engineering/'),
    ('earth', 'https://eps.ucsc.edu/'),
    ('ece', 'https://engineering.ucsc.edu/departments/electrical-and-computer-engineering/'),
    ('environment', 'https://envs.ucsc.edu/'),
    ('materials', 'https://engineering.ucsc.edu/materials-science-and-engineering/'),
    ('math', 'https://math.ucsc.edu/'),
    ('physics', 'https://physics.ucsc.edu/'),
    ('statistics', 'https://engineering.ucsc.edu/departments/statistics/')
]

for name, u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            print(f'{name}: {r.status} -> {r.geturl()}')
    except Exception as e:
        print(f'{name}: {e}')
