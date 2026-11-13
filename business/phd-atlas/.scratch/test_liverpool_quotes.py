import json, hashlib

u_apply = 'https://www.liverpool.ac.uk/study/postgraduate-research/how-to-apply/'
u_pgr = 'https://www.liverpool.ac.uk/study/postgraduate-research/'
u_req = 'https://www.liverpool.ac.uk/study/international/apply/english-language/'
u_tests = 'https://www.liverpool.ac.uk/international/applying/entry-requirements/english-language-requirements/international-english-language-tests/'
u_ets = 'https://www.ets.org/gre/score-users/about/subject-tests.html'

def get_text(u):
    key = hashlib.sha1(u.encode()).hexdigest()[:16]
    return json.load(open(f'.cache/pages/{key}.json', encoding='utf-8'))['text']

t_apply = get_text(u_apply)
t_pgr = get_text(u_pgr)
t_req = get_text(u_req)
t_tests = get_text(u_tests)
t_ets = get_text(u_ets)

idx_dl = t_apply.find("You should apply as early as possible if you're also applying for funding, or if you need to secure a UK visa.")
print('dl:', idx_dl != -1)

idx_sup = t_apply.find("It’s useful to contact potential supervisors before you make your application. This gives you the chance to discuss their availability and your proposed research.")
print('sup:', idx_sup != -1)

idx_fund = t_pgr.find("Be part of the next generation of researchers, combining expert collaboration and structured training on a funded PhD.")
print('fund:', idx_fund != -1)

idx_entry = t_apply.find("University transcripts\u202fand degree certificates to date")
print('entry:', idx_entry != -1)

idx_ielts = t_tests.find("Most of our postgraduate research courses require one of:\nIELTS 6.5 overall, with no component less than 5.5, or equivalent")
print('ielts:', idx_ielts != -1)

idx_toefl = t_tests.find("TOEFL iBT (excluding TOEFL Home Edition which is not accepted)")
print('toefl:', idx_toefl != -1)

idx_waiver = t_req.find("For most international students, unless you're a national of a majority English speaking country, you'll need to provide")
print('waiver:', idx_waiver != -1)
