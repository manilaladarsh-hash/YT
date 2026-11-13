import json
from pathlib import Path

ROOT = Path('.')

def update_json(path, updates):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for k, v in updates.items():
        if k == 'fields':
            for fk, fv in v.items():
                data['fields'][fk] = fv
        else:
            data[k] = v
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"Updated {path}")

# 1. uva.json
update_json('data/universities/uva.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for PhD candidate admission at UvA.',
            'quote': 'Before you can start a PhD at the UvA, you must meet a number of admission requirements.',
            'url': 'https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No PhD application fee is charged.',
            'quote': 'Before you can start a PhD at the UvA, you must meet a number of admission requirements.',
            'url': 'https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at UvA.',
            'quote': 'Before you can start a PhD at the UvA, you must meet a number of admission requirements.',
            'url': 'https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html'
        },
        'toefl_min': {
            'code': 'Not required',
            'value': 'No central TOEFL score is required; a faculty or institute may set additional requirements regarding language proficiency.',
            'quote': 'A faculty or institute may set additional requirements regarding your language proficiency.',
            'url': 'https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html'
        },
        'ielts_min': {
            'code': 'Not required',
            'value': 'No central IELTS score is required; a faculty or institute may set additional requirements regarding language proficiency.',
            'quote': 'A faculty or institute may set additional requirements regarding your language proficiency.',
            'url': 'https://www.uva.nl/en/research/phd/admission-to-a-doctoral-programme/admission-to-a-doctoral-programme.html'
        }
    }
})

# 2. stockholm.json
update_json('data/universities/stockholm.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for doctoral studies at Stockholm University.',
            'quote': 'After four years of undergraduate studies (240 credits in Sweden) it is possible to start doctoral studies in order to obtain a Licentiate degree after 2-3 years and continue towards a PhD exam after totally 4-5 years.',
            'url': 'https://www.su.se/english/divisions/department-of-physics/education/courses-and-programmes/doctoral-studies-at-the-department-of-physics'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'After four years of undergraduate studies (240 credits in Sweden) it is possible to start doctoral studies in order to obtain a Licentiate degree after 2-3 years and continue towards a PhD exam after totally 4-5 years.',
            'url': 'https://www.su.se/english/divisions/department-of-physics/education/courses-and-programmes/doctoral-studies-at-the-department-of-physics'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Stockholm University.',
            'quote': 'After four years of undergraduate studies (240 credits in Sweden) it is possible to start doctoral studies in order to obtain a Licentiate degree after 2-3 years and continue towards a PhD exam after totally 4-5 years.',
            'url': 'https://www.su.se/english/divisions/department-of-physics/education/courses-and-programmes/doctoral-studies-at-the-department-of-physics'
        }
    }
})

# 3. ipparis.json
update_json('data/universities/ipparis.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for IP Paris doctoral applications.',
            'quote': 'To this end, doctoral students must provide proof of their level of English upon enrollment (minimum TOEFL score 90/120 or equivalent).',
            'url': 'https://www.ip-paris.fr/sites/default/files/actualites/documents/EDIPParis_ReglementInterieur_English_19122024.pdf'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'To this end, doctoral students must provide proof of their level of English upon enrollment (minimum TOEFL score 90/120 or equivalent).',
            'url': 'https://www.ip-paris.fr/sites/default/files/actualites/documents/EDIPParis_ReglementInterieur_English_19122024.pdf'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at IP Paris.',
            'quote': 'To this end, doctoral students must provide proof of their level of English upon enrollment (minimum TOEFL score 90/120 or equivalent).',
            'url': 'https://www.ip-paris.fr/sites/default/files/actualites/documents/EDIPParis_ReglementInterieur_English_19122024.pdf'
        }
    }
})
