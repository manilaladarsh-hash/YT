import json, pathlib
p = pathlib.Path('data/programs/uchicago--datasci.json')
d = json.loads(p.read_text(encoding='utf-8'))
d['fields']['entry_route'] = {
    'code': "Direct from bachelor's",
    'value': "Students can enter with an undergraduate degree and earn an MS on the way to the PhD.",
    'quote': "candidates in our PhD program will have the opportunity to earn their MS prior to completion of their doctoral study.",
    'url': "https://codas.uchicago.edu/frequently-asked-questions/"
}
d['checked'] = '2026-10-29'
p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('uchicago--datasci updated.')
