import sys, json
sys.path.insert(0, '.')
from scripts.research import cache_paths

fee_url = "https://grad.ucsd.edu/admissions/requirements/application-fee-and-fee-waiver/index.html"
exam_url = "https://grad.ucsd.edu/admissions/requirements/exam-requirements.html"
eng_url = "https://grad.ucsd.edu/admissions/requirements/international-students/english-proficiency.html"
prog_url = "https://grad.ucsd.edu/admissions/programs.html"

print("--- FEE ---")
t_fee = json.load(open(cache_paths(fee_url), "r", encoding="utf-8"))["text"]
for l in t_fee.splitlines():
    if any(k in l.lower() for k in ["fee", "$", "waiver"]):
        print(" ", l.strip()[:140])

print("\n--- EXAM ---")
t_exam = json.load(open(cache_paths(exam_url), "r", encoding="utf-8"))["text"]
for l in t_exam.splitlines():
    if any(k in l.lower() for k in ["gre", "general", "subject"]):
        print(" ", l.strip()[:140])

print("\n--- ENGLISH ---")
t_eng = json.load(open(cache_paths(eng_url), "r", encoding="utf-8"))["text"]
for l in t_eng.splitlines():
    if any(k in l.lower() for k in ["toefl", "ielts", "minimum", "waiv"]):
        print(" ", l.strip()[:140])
