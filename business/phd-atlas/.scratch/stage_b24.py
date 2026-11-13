import json, shutil

def stage(fn, fn_edit):
    shutil.copy(f'data/programs/{fn}', f'data/staging/programs/{fn}')
    with open(f'data/staging/programs/{fn}', encoding='utf-8') as f:
        d = json.load(f)
    fn_edit(d)
    with open(f'data/staging/programs/{fn}', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write('\n')

def edit_clemson_math(d):
    d['fields']['supervisor']['quote'] = (
        'Year Two | Complete all prelims during this year. | Choose a research adviser during this year as well.'
    )
    d['fields']['supervisor']['url'] = 'https://www.clemson.edu/science/academics/departments/mathstat/academics/grad-math.html'

def edit_clemson_physics(d):
    d['fields']['funding']['quote'] = (
        'All of our applicants are considered for teaching assistantships, which provide a tuition waiver and stipend. '
        'While a TA is not guaranteed, we strive to offer a TA to each student selected for admission. '
        'The availability of TAs is dependent on available funding and the number of positions available.'
    )
    d['fields']['toefl_min']['code'] = '4.0 (new scale)'
    d['fields']['toefl_min']['value'] = "The department's TOEFL iBT minimum is 4.0 on the 1-6 scale."
    d['fields']['toefl_min']['quote'] = 'TOEFL iBT: | Minimum score of 4.0.'

def edit_clemson_stat(d):
    d['fields']['supervisor']['quote'] = (
        'Choose a research advisor during this year as well. | '
        'Complete a GS2 committee selection form in consultation with your research advisor.'
    )
    d['fields']['supervisor']['url'] = 'https://www.clemson.edu/science/academics/departments/mathstat/academics/grad-stat-ds.html'

def edit_cmu_physics(d):
    d['fields']['fee_waiver']['quote'] = (
        'We regret that it is not possible to waive this small fee, '
        'with the exception of specific cases (at present for GEM Fellowship and Rales Fellowship applicants only).'
    )

def edit_colostate_bce(d):
    d['fields']['deadline']['quote'] = (
        'For full consideration for funding, application materials must be received by the following dates. | '
        'Fall semester: | M.S. and Ph.D. programs: | December 15'
    )

def edit_colostate_civil(d):
    d['fields']['deadline']['quote'] = (
        'Master of Science and Ph.D. Applicants | Fall Start (August) | Application deadline: December 1'
    )

def edit_colostate_math(d):
    d['fields']['deadline']['quote'] = (
        'We admit for fall semester only. The deadline for a complete application are: | '
        'February 1: To be considered for admission'
    )
    d['fields']['ielts_min']['quote'] = 'Minimum scores are as follows: | IELTS – 6.5'

stage('clemson--math.json', edit_clemson_math)
stage('clemson--physics.json', edit_clemson_physics)
stage('clemson--statistics.json', edit_clemson_stat)
stage('cmu--physics.json', edit_cmu_physics)
stage('colostate--bme.json', edit_colostate_bce)
stage('colostate--chemeng.json', edit_colostate_bce)
stage('colostate--civil.json', edit_colostate_civil)
stage('colostate--math.json', edit_colostate_math)
print("Staged 8 Batch 24 programs (including clemson--physics toefl_min fix) cleanly.")
