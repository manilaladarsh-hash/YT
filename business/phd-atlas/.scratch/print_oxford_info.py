import glob, json

urls = [
    'https://www.ox.ac.uk/admissions/graduate/application-guide/declaration-and-payment/application-fee',
    'https://www.ox.ac.uk/admissions/graduate/application-guide/declaration-and-payment/application-fee-waivers',
    'https://www.ox.ac.uk/admissions/graduate/application-guide/qualifications-experience-languages-funding/english-language-proficiency',
    'https://www.ox.ac.uk/admissions/graduate/application-guide/qualifications-experience-languages-funding/english-language-test-waivers'
]

cache = {}
for p in glob.glob('.cache/pages/*.json'):
    try:
        d = json.load(open(p, encoding='utf-8'))
        u = d.get('url')
        if u in urls:
            cache[u] = d.get('text', '')
    except:
        pass

for u in urls:
    print('==================================================')
    print('URL:', u)
    text = cache.get(u, 'NOT CACHED')
    for line in text.splitlines():
        if any(w in line.lower() for w in ['£', 'fee', 'waiver', 'india', 'ielts', 'toefl', 'exemption', 'majority']):
            print('  ', line[:140])
