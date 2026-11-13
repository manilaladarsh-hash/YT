import urllib.request, ssl

ctx = ssl.create_default_context()
urls = [
    ('astronomy', 'https://physics.ucf.edu/graduate-programs/'),
    ('biology', 'https://www.ucf.edu/degree/integrative-and-conservation-biology-phd/'),
    ('biomed', 'https://www.ucf.edu/degree/biomedical-sciences-phd/'),
    ('bme', 'https://www.ucf.edu/degree/biomedical-engineering-phd/'),
    ('chemistry', 'https://www.ucf.edu/degree/chemistry-phd/'),
    ('civil', 'https://www.ucf.edu/degree/civil-engineering-phd/'),
    ('datasci', 'https://www.ucf.edu/degree/big-data-analytics-phd/'),
    ('ece', 'https://www.ucf.edu/degree/electrical-engineering-phd/'),
    ('environment', 'https://www.ucf.edu/degree/environmental-engineering-phd/'),
    ('materials', 'https://www.ucf.edu/degree/materials-science-and-engineering-phd/'),
    ('math', 'https://www.ucf.edu/degree/mathematics-phd/'),
    ('mech', 'https://www.ucf.edu/degree/mechanical-engineering-phd/'),
    ('neuro', 'https://www.ucf.edu/degree/biomedical-sciences-phd/neuroscience-track/'),
    ('physics', 'https://www.ucf.edu/degree/physics-phd/'),
    ('statistics', 'https://sciences.ucf.edu/statistics/graduate/')
]

for name, u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            print(f'{name}: {r.status} -> {r.geturl()}')
    except Exception as e:
        print(f'{name}: {e}')
