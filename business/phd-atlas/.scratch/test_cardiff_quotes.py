import json, hashlib

u_apply = 'https://www.cardiff.ac.uk/study/postgraduate/applying/how-to-apply'
u_pgr = 'https://www.cardiff.ac.uk/study/postgraduate/research'
u_lang = 'https://www.cardiff.ac.uk/study/international/english-language-requirements'
u_ets = 'https://www.ets.org/gre/score-users/about/subject-tests.html'

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f'.cache/pages/{key}.json', encoding='utf-8'))['text']

t_apply = get_text(u_apply)
t_pgr = get_text(u_pgr)
t_lang = get_text(u_lang)
t_ets = get_text(u_ets)

idx_fee = t_apply.find('Cardiff University does not charge an application fee for any of our postgraduate programmes.')
print('fee:', idx_fee != -1)

idx_dl = t_apply.find('Look at our funding pages to see the financial support available - if you intend to apply for funding, we advise that you submit your application at least two months before a scholarship deadline.')
print('dl:', idx_dl != -1)

idx_entry = t_apply.find('Check the entry requirements - if you have not yet met the entry requirements, you can usually still apply for a course. You may receive an offer of a place on the condition that you meet the requirements before you start the course.')
print('entry:', idx_entry != -1)

sup_str = "Research degrees are focused on independent study. Unlike taught students, you'll work with your supervisor to identify your study needs."
idx_sup = t_pgr.find(sup_str)
print('sup:', idx_sup != -1)

idx_fund = t_pgr.find('Find funded PhD studentships and projects, as well as projects available for applicants who are self-funded or have already secured funding.')
print('fund:', idx_fund != -1)

idx_ielts = t_lang.find('The university minimum requirement for English language is a grade C/4 at GCSE or IELTS (Academic) with 6.5 overall and a minimum of 5.5 in each of the subskills')
print('ielts:', idx_ielts != -1)

idx_waiver = t_lang.find('In addition to meeting the academic language standard, applicants who require a Student Route visa to study in the UK must present an acceptable English language qualification to meet UKVI (UK Visas and Immigration) requirements')
print('waiver:', idx_waiver != -1)

idx_toefl = t_lang.find('TOEFL iBT including')
print('toefl idx:', idx_toefl)
if idx_toefl != -1:
    print(repr(t_lang[idx_toefl:idx_toefl+120]))
