import urllib.request, ssl

ctx = ssl.create_default_context()
urls = [
    'https://cosam.auburn.edu/biological_sciences/',
    'https://cosam.auburn.edu/departments/biological_sciences/',
    'https://www.vetmed.auburn.edu/education/biomedical-sciences-graduate-students/',
    'https://www.vetmed.auburn.edu/education/biomedical-sciences/'
]

for u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            print(f'{u} -> {r.status} {r.geturl()}')
    except Exception as e:
        print(f'{u} -> {e}')
