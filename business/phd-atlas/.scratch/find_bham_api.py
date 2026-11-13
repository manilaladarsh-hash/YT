import requests, re

r = requests.get('https://www.birmingham.ac.uk/study/postgraduate/research/course-search', headers={'User-Agent': 'Mozilla/5.0'})
matches = re.findall(r'[\'"]([^\'"]*(?:api|search|json|results)[^\'"]*)[\'"]', r.text, re.I)
for m in sorted(set(matches)):
    if any(k in m.lower() for k in ['course', 'search', 'api']):
        print(m)
