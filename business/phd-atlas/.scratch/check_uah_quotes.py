import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

t = json.load(open(cache_paths('https://www.uah.edu/admissions/graduate/apply-for-admission'), 'r', encoding='utf-8'))['text']
q1 = 'A full-time (9-12 enrolled hours) assistantship (20 hours/week) typically covers full tuition benefits, full health insurance (single person), a stipend, and associated fees.'
q2 = "To qualify for unconditional admission to the UAH Graduate School, you must hold a bachelor's degree, or equivalent, from an approved institution and have a minimum 3.0 GPA on your undergraduate record."
print('q1 match:', ' '.join(q1.split()) in ' '.join(t.split()))
print('q2 match:', ' '.join(q2.split()) in ' '.join(t.split()))
