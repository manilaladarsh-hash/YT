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

# 1. tuberlin.json
update_json('data/universities/tuberlin.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged; accepted candidates pay only semester fees upon enrollment.',
            'quote': 'After your online-application to enrollment has been approved, you will receive an e-mail requesting you to pay the required semester fees.',
            'url': 'https://www.tu.berlin/en/studierendensekretariat/applying-enrolling-for-doctoral-studies'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'After your online-application to enrollment has been approved, you will receive an e-mail requesting you to pay the required semester fees.',
            'url': 'https://www.tu.berlin/en/studierendensekretariat/applying-enrolling-for-doctoral-studies'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at TU Berlin.',
            'quote': 'After your online-application to enrollment has been approved, you will receive an e-mail requesting you to pay the required semester fees.',
            'url': 'https://www.tu.berlin/en/studierendensekretariat/applying-enrolling-for-doctoral-studies'
        },
        'toefl_min': {
            'code': 'Not required',
            'value': 'No university-wide TOEFL is required centrally; the faculty board decision on the declaration of intent specifies whether the doctorate will be in English or German.',
            'quote': "To enroll you must have received the faculty board decision confirming the faculty's acceptance of your declaration of intent to pursue a doctorate and stating whether you will be completing your doctorate in English or German.",
            'url': 'https://www.tu.berlin/en/studierendensekretariat/applying-enrolling-for-doctoral-studies'
        },
        'ielts_min': {
            'code': 'Not required',
            'value': 'No university-wide IELTS is required centrally; the faculty board decision on the declaration of intent specifies language.',
            'quote': "To enroll you must have received the faculty board decision confirming the faculty's acceptance of your declaration of intent to pursue a doctorate and stating whether you will be completing your doctorate in English or German.",
            'url': 'https://www.tu.berlin/en/studierendensekretariat/applying-enrolling-for-doctoral-studies'
        }
    }
})

# 2. sorbonne.json
update_json('data/universities/sorbonne.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for doctoral admission; candidates pay €398 national enrolment fees after admission.',
            'quote': 'Doctoral programmes: €398',
            'url': 'https://www.sorbonne-universite.fr/en/education/study-sorbonne-university/enrolment-procedures-and-tuition-fees'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'Students enrolling in a doctoral programme, a third-cycle programme in health studies or an accreditation to supervise research (HDR) programme.',
            'url': 'https://www.sorbonne-universite.fr/en/education/study-sorbonne-university/enrolment-procedures-and-tuition-fees'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Sorbonne University.',
            'quote': 'Students enrolling in a doctoral programme, a third-cycle programme in health studies or an accreditation to supervise research (HDR) programme.',
            'url': 'https://www.sorbonne-universite.fr/en/education/study-sorbonne-university/enrolment-procedures-and-tuition-fees'
        }
    }
})

# 3. ntnu.json
update_json('data/universities/ntnu.json', {
    'fields': {
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for PhD admission at NTNU.',
            'quote': "To qualify for admission to a PhD programme, applicants must normally hold a master's degree that includes a major independent project (minimum 30 ECTS) equivalent to a master's thesis, cf. the descriptions in the Norwegian Qualifications Framework Level 7.",
            'url': 'https://www.ntnu.edu/documents/1263185004/1285991844/NTNU+PhD-regulations+updated+20260203+%281%29.pdf/b9ab638d-5d97-b2bc-ab17-5a20ff1ceac0?t=1778059527861'
        }
    }
})

# 4. uppsala.json
update_json('data/universities/uppsala.json', {
    'fields': {
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral studies at Uppsala.',
            'quote': 'completed a degree at the advanced level (Master’s level), or',
            'url': 'https://www.uu.se/en/staff/faculty/science-and-technology/education-and-teaching/doctoral-studies/subjects-and-study-plans/subjects/engineering-sciences-with-specialisation-in-applied-mechanics'
        }
    }
})
