import json, pathlib

for name in ['utah--datasci.json', 'utah--cs.json']:
    p = pathlib.Path(f'data/programs/{name}')
    d = json.loads(p.read_text(encoding='utf-8'))
    d['fields']['supervisor'] = {
        'code': 'Not required',
        'value': 'Applications are evaluated centrally by the admissions committee after the December 15 deadline; no pre-arranged supervisor is required.',
        'quote': 'Evaluation of your application will begin only after the application fee is received and the December 15th deadline has past.',
        'url': 'https://www.cs.utah.edu/graduate/prospective-students/admissions/graduate-required-supporting-documents/'
    }
    d['checked'] = '2026-10-29'
    p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{name} updated.')
