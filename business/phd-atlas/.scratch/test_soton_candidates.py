import urllib.request

candidates = [
    "https://www.southampton.ac.uk/courses/computer-science-phd",
    "https://www.southampton.ac.uk/courses/computer-science-degree-phd",
    "https://www.southampton.ac.uk/courses/chemistry-phd",
    "https://www.southampton.ac.uk/courses/physics-phd",
    "https://www.southampton.ac.uk/courses/mathematics-phd",
    "https://www.southampton.ac.uk/courses/biological-sciences-phd",
    "https://www.southampton.ac.uk/courses/civil-engineering-phd",
    "https://www.southampton.ac.uk/courses/mechanical-engineering-phd",
    "https://www.southampton.ac.uk/courses/research/computer-science",
    "https://www.southampton.ac.uk/courses/research/chemistry",
]

for u in candidates:
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"{u}: status={resp.status}")
    except Exception as e:
        print(f"{u}: {e}")
