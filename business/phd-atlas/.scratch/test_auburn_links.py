import urllib.request, ssl

ctx = ssl.create_default_context()
urls = [
    ('biology', 'https://www.auburn.edu/cosam/departments/biological-sciences/'),
    ('biomed', 'https://www.vetmed.auburn.edu/education/biomedical-sciences-graduate-program/'),
    ('chemeng', 'https://eng.auburn.edu/chen/academics/graduate/'),
    ('chemistry', 'https://www.auburn.edu/cosam/departments/chemistry/'),
    ('civil', 'https://eng.auburn.edu/civil/academics/graduate/'),
    ('cs', 'https://eng.auburn.edu/csse/academics/graduate/'),
    ('earth', 'https://www.auburn.edu/cosam/departments/geosciences/'),
    ('ece', 'https://eng.auburn.edu/ece/academics/graduate/'),
    ('materials', 'https://eng.auburn.edu/matl/academics/graduate/'),
    ('math', 'https://www.auburn.edu/cosam/departments/math/'),
    ('mech', 'https://eng.auburn.edu/mech/academics/graduate/')
]

for name, u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            print(f'{name}: {r.status} -> {r.geturl()}')
    except Exception as e:
        print(f'{name}: {e}')
