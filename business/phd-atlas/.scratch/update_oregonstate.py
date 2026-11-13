import json, pathlib

for name in ['oregonstate--datasci.json', 'oregonstate--cs.json']:
    p = pathlib.Path(f'data/programs/{name}')
    d = json.loads(p.read_text(encoding='utf-8'))
    d['fields']['entry_route'] = {
        'code': 'Either',
        'value': 'Applicants must hold a baccalaureate degree or equivalent; completion of an M.S. is typical but not strictly required before entry.',
        'quote': 'Applicants must have or will complete a baccalaureate degree from an accredited college or university before the start of their entry term.',
        'url': 'https://engineering.oregonstate.edu/academics/programs/computer-science/graduate'
    }
    d['checked'] = '2026-10-29'
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{name} updated.')
