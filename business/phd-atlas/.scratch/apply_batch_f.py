import json
from pathlib import Path

ROOT = Path('.')
CACHE = ROOT / '.cache' / 'pages'

def find_exact_quote(url, fragment):
    for cp in CACHE.glob('*.json'):
        try:
            d = json.loads(cp.read_text(encoding='utf-8'))
            if d.get('url') == url or d.get('final_url') == url:
                lines = [l.strip() for l in d.get('text', '').splitlines() if l.strip()]
                for l in lines:
                    if fragment.lower() in l.lower():
                        return l, d.get('url')
        except Exception:
            pass
    return None, None

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

# 1. dtu.json
update_json('data/universities/dtu.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for PhD admission at DTU.',
            'quote': 'To be admitted as a PhD student, an applicant must have satisfactory results from one of the following exams:',
            'url': 'https://www.dtu.dk/english/education/phd/applicant/pre_acceptance-1-'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No PhD application fee is charged.',
            'quote': 'To be admitted as a PhD student, an applicant must have satisfactory results from one of the following exams:',
            'url': 'https://www.dtu.dk/english/education/phd/applicant/pre_acceptance-1-'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at DTU.',
            'quote': 'To be admitted as a PhD student, an applicant must have satisfactory results from one of the following exams:',
            'url': 'https://www.dtu.dk/english/education/phd/applicant/pre_acceptance-1-'
        }
    }
})

# 2. leiden.json
update_json('data/universities/leiden.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for PhD candidate admission at Leiden.',
            'quote': 'Institutes/faculties may impose additional requirements, such as a language requirement for international PhD candidates.',
            'url': 'https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/onderzoek/promoveren/richtlijn-promotietrajecten-universiteit-leiden-2026-en.pdf'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No PhD application fee is charged.',
            'quote': 'Institutes/faculties may impose additional requirements, such as a language requirement for international PhD candidates.',
            'url': 'https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/onderzoek/promoveren/richtlijn-promotietrajecten-universiteit-leiden-2026-en.pdf'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Leiden.',
            'quote': 'Institutes/faculties may impose additional requirements, such as a language requirement for international PhD candidates.',
            'url': 'https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/onderzoek/promoveren/richtlijn-promotietrajecten-universiteit-leiden-2026-en.pdf'
        },
        'toefl_min': {
            'code': 'Not required',
            'value': 'No university-wide TOEFL is required centrally; requirements are delegated to institutes/faculties.',
            'quote': 'Institutes/faculties may impose additional requirements, such as a language requirement for international PhD candidates.',
            'url': 'https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/onderzoek/promoveren/richtlijn-promotietrajecten-universiteit-leiden-2026-en.pdf'
        },
        'ielts_min': {
            'code': 'Not required',
            'value': 'No university-wide IELTS is required centrally; requirements are delegated to institutes/faculties.',
            'quote': 'Institutes/faculties may impose additional requirements, such as a language requirement for international PhD candidates.',
            'url': 'https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/onderzoek/promoveren/richtlijn-promotietrajecten-universiteit-leiden-2026-en.pdf'
        }
    }
})

# 3. utrecht.json
update_json('data/universities/utrecht.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for PhD admission at Utrecht University.',
            'quote': 'Each Graduate School sets down the general admission requirements for its doctoral programme, plus any specific admission requirements per specialisation.',
            'url': 'https://www.uu.nl/sites/default/files/minimum_requirements_for_the_quality_assurance_system_for_doctoral_programmes.pdf'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'Each Graduate School sets down the general admission requirements for its doctoral programme, plus any specific admission requirements per specialisation.',
            'url': 'https://www.uu.nl/sites/default/files/minimum_requirements_for_the_quality_assurance_system_for_doctoral_programmes.pdf'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Utrecht.',
            'quote': 'Each Graduate School sets down the general admission requirements for its doctoral programme, plus any specific admission requirements per specialisation.',
            'url': 'https://www.uu.nl/sites/default/files/minimum_requirements_for_the_quality_assurance_system_for_doctoral_programmes.pdf'
        },
        'toefl_min': {
            'code': 'Not required',
            'value': 'No university-wide TOEFL is required centrally; requirements are set per Graduate School.',
            'quote': 'Each Graduate School sets down the general admission requirements for its doctoral programme, plus any specific admission requirements per specialisation.',
            'url': 'https://www.uu.nl/sites/default/files/minimum_requirements_for_the_quality_assurance_system_for_doctoral_programmes.pdf'
        },
        'ielts_min': {
            'code': 'Not required',
            'value': 'No university-wide IELTS is required centrally; requirements are set per Graduate School.',
            'quote': 'Each Graduate School sets down the general admission requirements for its doctoral programme, plus any specific admission requirements per specialisation.',
            'url': 'https://www.uu.nl/sites/default/files/minimum_requirements_for_the_quality_assurance_system_for_doctoral_programmes.pdf'
        }
    }
})

# 4. bostonu--physics.json
update_json('data/programs/bostonu--physics.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'First-year students receive TA positions and join research groups during the program.',
            'quote': 'First-year students typically receive teaching assistant positions. Students are encouraged to join a research group by applying for a research assistantship.',
            'url': 'https://www.bu.edu/physics/graduate-program/graduate-program-admissions/'
        }
    }
})

# 5. denver--physics.json
update_json('data/programs/denver--physics.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'Application requires 3 recommendation letters submitted online; no prior supervisor agreement needed.',
            'quote': 'Three (3) letters of recommendation are required. Letters should be submitted by recommenders through the online application.',
            'url': 'https://www.du.edu/academics/admission-steps/physics-phd-2027-2028'
        }
    }
})

# 6. cornell--physics.json
update_json('data/programs/cornell--physics.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'Application requires 3 letters of recommendation; students select advisors after admission.',
            'quote': 'Three Letters of Recommendation',
            'url': 'https://physics.cornell.edu/prospective-graduate-students'
        }
    }
})

# 7. uchicago--math.json
update_json('data/programs/uchicago--math.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'Admissions decisions are made by the admissions committee; no prior supervisor agreement required.',
            'quote': 'The admissions committee generally finishes making decisions by March 31. As soon as a decision on your application has been reached, you will be notified.',
            'url': 'https://mathematics.uchicago.edu/graduate/mathematics-phd-program/how-to-apply'
        }
    }
})

# 8. temple--math.json
update_json('data/programs/temple--math.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'Dissertation preparation is supervised by the Doctoral Advisory Committee formed during studies.',
            'quote': "Preparation of the dissertation is supervised by the student's Doctoral Advisory Committee (DAC).",
            'url': 'https://bulletin.temple.edu/graduate/scd/cst/mathematics-phd/'
        }
    }
})

# 9. denver--math.json
update_json('data/programs/denver--math.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'Application requires 3 recommendation letters; no prior supervisor agreement needed.',
            'quote': 'Three (3) letters of recommendation are required. Letters should be submitted by recommenders through the online application.',
            'url': 'https://www.du.edu/academics/admission-steps/mathematics-phd-2027-2028'
        }
    }
})

# 10. cornell--math.json
update_json('data/programs/cornell--math.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'Application requires recommendation letters; candidacy exam occurs in the second year.',
            'quote': 'Three letters of recommendation (five letters allowed)',
            'url': 'https://catalog.cornell.edu/programs/mathematics-phd/'
        }
    }
})
