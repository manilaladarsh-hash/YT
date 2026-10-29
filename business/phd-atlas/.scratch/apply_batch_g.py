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

# 1. freiburg.json
update_json('data/universities/freiburg.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for international doctoral candidates; only semester fees are paid upon enrolment.',
            'quote': 'No, international doctoral candidates only have to pay the normal semester fees.',
            'url': 'https://uni-freiburg.de/en/studies/getting-started/enrolment/enrolment-doctoral-candidates/'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'No, international doctoral candidates only have to pay the normal semester fees.',
            'url': 'https://uni-freiburg.de/en/studies/getting-started/enrolment/enrolment-doctoral-candidates/'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required; admission is regulated by faculty doctoral regulations.',
            'quote': 'for non-German applicants, documentation of sufficient knowledge of German or English',
            'url': 'https://uni-freiburg.de/mathphys/wp-content/uploads/sites/31/promotionsordnung-fr-2016_eng.pdf'
        },
        'toefl_min': {
            'code': 'Not required',
            'value': 'No university-wide TOEFL is required centrally; documentation of sufficient German or English knowledge is required.',
            'quote': 'for non-German applicants, documentation of sufficient knowledge of German or English',
            'url': 'https://uni-freiburg.de/mathphys/wp-content/uploads/sites/31/promotionsordnung-fr-2016_eng.pdf'
        },
        'ielts_min': {
            'code': 'Not required',
            'value': 'No university-wide IELTS is required centrally; documentation of sufficient German or English knowledge is required.',
            'quote': 'for non-German applicants, documentation of sufficient knowledge of German or English',
            'url': 'https://uni-freiburg.de/mathphys/wp-content/uploads/sites/31/promotionsordnung-fr-2016_eng.pdf'
        }
    }
})

# 2. uga-fr.json
update_json('data/universities/uga-fr.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged; €398 national registration fee is paid only after admission to the Doctoral School.',
            'quote': 'The registration fee is €398 for all PhD registrations for the academic year 2026/2027.',
            'url': 'https://doctorat.univ-grenoble-alpes.fr/preparing-a-phd/doctorate-enrolment/registration-at-doctoral-college-890540.kjsp'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'The registration fee is €398 for all PhD registrations for the academic year 2026/2027.',
            'url': 'https://doctorat.univ-grenoble-alpes.fr/preparing-a-phd/doctorate-enrolment/registration-at-doctoral-college-890540.kjsp'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at UGA.',
            'quote': 'The registration fee is €398 for all PhD registrations for the academic year 2026/2027.',
            'url': 'https://doctorat.univ-grenoble-alpes.fr/preparing-a-phd/doctorate-enrolment/registration-at-doctoral-college-890540.kjsp'
        }
    }
})

# 3. upc.json
update_json('data/universities/upc.json', {
    'fields': {
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral access at UPC.',
            'quote': "As a rule, applicants must hold a Spanish bachelor's degree or equivalent and a Spanish master's degree or equivalent",
            'url': 'https://doctorat.upc.edu/en/future-doctoral-candidates/access-and-admission/general-entrance-requirements'
        }
    }
})

# 4. ugent.json
update_json('data/universities/ugent.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for PhD applicants; tuition is paid only upon first enrolment.',
            'quote': 'Doctoral studies are open to holders of a master degree (or a degree of minimum four years of study considered equivalent)',
            'url': 'https://www.ugent.be/prospect/en/administration/application/requirement/phd.htm'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'Doctoral studies are open to holders of a master degree (or a degree of minimum four years of study considered equivalent)',
            'url': 'https://www.ugent.be/prospect/en/administration/application/requirement/phd.htm'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral research admission at Ghent University.',
            'quote': 'Doctoral studies are open to holders of a master degree (or a degree of minimum four years of study considered equivalent)',
            'url': 'https://www.ugent.be/prospect/en/administration/application/requirement/phd.htm'
        }
    }
})
