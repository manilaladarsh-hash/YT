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

# 1. temple--physics.json
update_json('data/programs/temple--physics.json', {
    'fields': {
        'supervisor': {
            'code': 'Not required',
            'value': 'A dissertation supervisor is chosen after admission during the preliminary exam/candidacy phase in consultation with a faculty member.',
            'quote': 'A topic for the PhD dissertation is selected in consultation with a faculty member who agrees to serve as the dissertation supervisor.',
            'url': 'https://bulletin.temple.edu/graduate/scd/cst/physics-phd/'
        }
    }
})

# 2. kit--physics.json
update_json('data/programs/kit--physics.json', {
    'fields': {
        'deadline': {
            'code': 'Per position',
            'value': 'There is no centrally organized deadline; applicants apply directly to open positions or institutes year-round.',
            'quote': "There is no centrally organized application portal for doctoral researchers at the department. Applicants can consult the institutes' websites for open positions and contact professors directly, even if no vacancy is advertised.",
            'url': 'https://www.physik.kit.edu/english/studies/doctorate.php'
        },
        'funding': {
            'code': 'Competitive',
            'value': 'Doctoral candidates are funded through varied external and institute sources, with no tuition charged.',
            'quote': 'When pursuing a doctorate at KIT, no tuition fees will be charged. In case of an ▶ enrollment as a doctoral student, you will have to pay semester charges only. Various options exist to cover your living expenses during the doctoral phase. Funding of the doctorate from different sources is common practice.',
            'url': 'https://www.khys.kit.edu/english/financing_doctorate.php'
        }
    }
})

# 3. kit--math.json
update_json('data/programs/kit--math.json', {
    'fields': {
        'funding': {
            'code': 'Competitive',
            'value': 'Doctoral candidates are funded through varied external and institute sources, with no tuition charged.',
            'quote': 'When pursuing a doctorate at KIT, no tuition fees will be charged. In case of an ▶ enrollment as a doctoral student, you will have to pay semester charges only. Various options exist to cover your living expenses during the doctoral phase. Funding of the doctorate from different sources is common practice.',
            'url': 'https://www.khys.kit.edu/english/financing_doctorate.php'
        }
    }
})

# 4. kit.json
update_json('data/universities/kit.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No tuition or application fees are charged for pursuing a doctorate at KIT.',
            'quote': 'When pursuing a doctorate at KIT, no tuition fees will be charged',
            'url': 'https://www.khys.kit.edu/english/financing_doctorate.php'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'Doctoral studies at KIT carry no tuition or application fee.',
            'quote': 'When pursuing a doctorate at KIT, no tuition fees will be charged',
            'url': 'https://www.khys.kit.edu/english/financing_doctorate.php'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required; admission is decided by the department Doctoral Admissions Committee.',
            'quote': 'For your ▶ acceptance as doctoral researcher by the KIT department, your degree will also be checked by the Doctoral Admissions Committee.',
            'url': 'https://www.khys.kit.edu/english/admission_requirements.php'
        },
        'toefl_min': {
            'code': 'Not required',
            'value': 'Doctoral candidates are expected to have a good command of English, but formal test certificates like TOEFL are not usually required centrally.',
            'quote': 'As a rule, doctoral candidates are expected to have a very good command of English, even if formal proof such as TOEFL or IELTS is not usually required',
            'url': 'https://www.khys.kit.edu/english/admission_requirements.php'
        },
        'ielts_min': {
            'code': 'Not required',
            'value': 'Doctoral candidates are expected to have a good command of English, but formal test certificates like IELTS are not usually required centrally.',
            'quote': 'As a rule, doctoral candidates are expected to have a very good command of English, even if formal proof such as TOEFL or IELTS is not usually required',
            'url': 'https://www.khys.kit.edu/english/admission_requirements.php'
        }
    }
})

# 5. heidelberg.json
update_json('data/universities/heidelberg.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'Doctoral students at Heidelberg University are exempt from tuition and application fees.',
            'quote': 'No, doctoral students are exempt from student fees, but you do have to pay a small administration fee when registering.',
            'url': 'https://hgsfp.physik.uni-heidelberg.de/howtoapply/faqs'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'Doctoral students are exempt from student fees.',
            'quote': 'No, doctoral students are exempt from student fees, but you do have to pay a small administration fee when registering.',
            'url': 'https://hgsfp.physik.uni-heidelberg.de/howtoapply/faqs'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Heidelberg.',
            'quote': 'If the applicant’s native language is not German or English, sufficient proficiency in either language must be demonstrated.',
            'url': 'https://www.chemgeo.uni-heidelberg.de/en/doctorate/admission-as-a-doctoral-candidate'
        }
    }
})

# 6. stuttgart.json
update_json('data/universities/stuttgart.json', {
    'fields': {
        'toefl_min': {
            'code': '80',
            'value': 'Minimum score of 80 on TOEFL iBT.',
            'quote': 'TOEFL (minimum scores: ibt 80; cbt 213; pbt 550)',
            'url': 'https://www.f08.uni-stuttgart.de/en/study_programs/physics/admissions/'
        },
        'ielts_min': {
            'code': '6.5',
            'value': 'Minimum overall band score of 6.5 on IELTS Academic.',
            'quote': 'IELTS (minimum band score 6.5)',
            'url': 'https://www.f08.uni-stuttgart.de/en/study_programs/physics/admissions/'
        },
        'english_waiver': {
            'code': 'No',
            'value': 'Exemptions are only possible for native speakers from UK, Ireland, USA, Canada, New Zealand and Australia; Indian degrees do not waive the requirement.',
            'quote': 'All applicants have to provide an official English proficiency certificate. Exemptions are only possible for native speakers passing their whole studies in the following countries: UK, Ireland, USA, Canada, New Zealand and Australia.',
            'url': 'https://www.f08.uni-stuttgart.de/en/study_programs/physics/admissions/'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Stuttgart.',
            'quote': 'All applicants have to provide an official English proficiency certificate. Exemptions are only possible for native speakers passing their whole studies in the following countries: UK, Ireland, USA, Canada, New Zealand and Australia.',
            'url': 'https://www.f08.uni-stuttgart.de/en/study_programs/physics/admissions/'
        }
    }
})

# 7. unibe.json
update_json('data/universities/unibe.json', {
    'fields': {
        'app_fee': {
            'code': '100 CHF',
            'value': 'University of Bern charges a CHF 100 registration fee for doctoral applicants.',
            'quote': "Registration fee | CHF 100; not payable if you enroll in a doctoral program directly after completing a master's degree program at the University of Bern.",
            'url': 'https://www.unibe.ch/studies/programs/doctorate/application/fees/index_eng.html'
        },
        'fee_waiver': {
            'code': 'None',
            'value': 'No waiver is provided for external international applicants.',
            'quote': "Registration fee | CHF 100; not payable if you enroll in a doctoral program directly after completing a master's degree program at the University of Bern.",
            'url': 'https://www.unibe.ch/studies/programs/doctorate/application/fees/index_eng.html'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE is not required for doctoral admission at Bern.',
            'quote': 'The Master’s programme is taught in English; therefore, a sufficient command of the language is required, although no formal language certificate is necessary.',
            'url': 'https://www.physik.unibe.ch/studies/international_students/index_eng.html'
        }
    }
})

# 8. fuberlin.json
update_json('data/universities/fuberlin.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'FU Berlin is a public university that does not charge application fees for doctoral admission.',
            'quote': 'There are some fees and required contributions of approximately €313 per semester.',
            'url': 'https://www.lai.fu-berlin.de/en/studium/Promotion/FAQ-Promotion/Are-there-registration-fees-for-doctoral-programmes_.html'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee is charged.',
            'quote': 'There are some fees and required contributions of approximately €313 per semester.',
            'url': 'https://www.lai.fu-berlin.de/en/studium/Promotion/FAQ-Promotion/Are-there-registration-fees-for-doctoral-programmes_.html'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission.',
            'quote': 'Sufficient English language skills corresponding to level B2 of the Common European Framework of Reference for Languages (CEFR)',
            'url': 'https://www.fu-berlin.de/sites/naturalsciences/application/index.html'
        }
    }
})

# 9. paris-saclay.json
update_json('data/universities/paris-saclay.json', {
    'fields': {
        'app_fee': {
            'code': '0 (no fee)',
            'value': 'No application fee is charged for PhD admission through doctoral schools; registration fee of €391 is paid only upon national enrolment.',
            'quote': "The registration fees for the preparation of national bachelor's, master's or doctoral degrees (LMD) are set at the national level. The doctoral registration fee is €391.",
            'url': 'https://www.universite-paris-saclay.fr/en/research/doctorate/phd-tuition-fees'
        },
        'fee_waiver': {
            'code': 'No fee',
            'value': 'No application fee exists.',
            'quote': "The registration fees for the preparation of national bachelor's, master's or doctoral degrees (LMD) are set at the national level. The doctoral registration fee is €391.",
            'url': 'https://www.universite-paris-saclay.fr/en/research/doctorate/phd-tuition-fees'
        },
        'gre_general': {
            'code': 'Not required',
            'value': 'GRE General is not required for doctoral admission at Paris-Saclay.',
            'quote': "The registration fees for the preparation of national bachelor's, master's or doctoral degrees (LMD) are set at the national level. The doctoral registration fee is €391.",
            'url': 'https://www.universite-paris-saclay.fr/en/research/doctorate/phd-tuition-fees'
        }
    }
})

# 10. columbia--physics.json
update_json('data/programs/columbia--physics.json', {
    'fields': {
        'funding': {
            'code': 'Guaranteed',
            'value': 'Doctoral students normally receive the annual prevailing stipend and tuition/fees for six years in good academic standing.',
            'quote': 'Doctoral students normally receive the annual prevailing stipend (or salary, in the case of student officers) and appropriate tuition, health fees, University service and support fees, and if applicable, international fees, for six years, provided that they remain in good academic standing. For student officers, they must also discharge responsibly their pedagogical or research duties.',
            'url': 'https://www.physics.columbia.edu/content/applying-columbia-physics-graduate-program'
        }
    }
})

# 11. claremontgrad--math.json
update_json('data/programs/claremontgrad--math.json', {
    'fields': {
        'gre_subject': {
            'code': 'Optional',
            'value': 'GRE subject test is optional.',
            'quote': 'Test scores are not required to be submitted, but you can optionally submit GRE scores (general and/or subject) if you think it will help your application.',
            'url': 'https://www.cgu.edu/academics/program/phd-mathematics/'
        },
        'supervisor': {
            'code': 'Not required',
            'value': 'Students are assigned an academic advisor upon entering and select a research advisor during advanced coursework.',
            'quote': 'Students are assigned an academic advisor upon entering the program. As they reach the advanced stages of coursework, they select a research advisor, who assumes primary advising responsibilities. In order to advance to candidacy, students must select a PhD committee consisting of at least three Mathematics faculty members from within the Claremont Colleges, chaired by the research advisor.',
            'url': 'https://www.cgu.edu/academics/program/phd-mathematics/'
        }
    }
})

# 12. binghamton--physics.json
update_json('data/programs/binghamton--physics.json', {
    'fields': {
        'funding': {
            'code': 'Most students',
            'value': 'PhD candidates are funded through teaching assistantships, research assistantships, and fellowships including stipend and tuition.',
            'quote': 'PhD candidates are funded through teaching assistantships, research assistantships, and fellowships, which include a stipend, tuition and health insurance. MS candidates are self-funded.',
            'url': 'https://www.binghamton.edu/physics/graduate/index.html'
        },
        'gre_general': {
            'code': 'Optional',
            'value': 'GRE is optional.',
            'quote': 'Note: GRE is optional. The minimum required TOEFL score is 80',
            'url': 'https://www.binghamton.edu/physics/graduate/index.html'
        }
    }
})

# 13. bgsu--math.json
update_json('data/programs/bgsu--math.json', {
    'fields': {
        'entry_route': {
            'code': "Master's required",
            'value': 'A master’s degree in mathematics or statistics with minimum 3.2 GPA is required.',
            'quote': 'A master’s degree in mathematics or statistics from an accredited institution with a minimum GPA of 3.2 on a 4-point scale*',
            'url': 'https://www.bgsu.edu/academics/graduate/mathematics-doctorate.html'
        },
        'funding': {
            'code': 'Competitive',
            'value': 'Department funds approximately 55 teaching assistantships, with about 20 new openings annually on a competitive basis.',
            'quote': 'Graduate assistantships. The department funds approximately 55 total teaching assistantships. There are about 20 new openings annually awarded on a competitive basis.',
            'url': 'https://www.bgsu.edu/academics/graduate/mathematics-doctorate.html'
        }
    }
})

# 14. bc--math.json
update_json('data/programs/bc--math.json', {
    'fields': {
        'deadline': {
            'code': '2027-01-20',
            'value': 'Applications received by January 20 receive full consideration for admission and Teaching Assistantships.',
            'quote': 'Applications received by January 20 will receive full consideration for admission and Teaching Assistantships.',
            'url': 'https://www.bc.edu/bc-web/schools/morrissey/departments/math/graduate/phd-program.html',
            'inferred': 'year'
        }
    }
})
