import json
from pathlib import Path

urls = {}
for p in Path('.cache/pages').glob('*.json'):
    rec = json.loads(p.read_text(encoding='utf-8'))
    for u in {rec['url'], rec.get('final_url', rec['url'])}:
        urls[u] = rec.get('text', '')

def check(u, q):
    t = urls.get(u, '')
    if q not in t:
        print(f"FAILED: {q!r} NOT in {u}")
        return False
    else:
        print(f"OK: {q[:35]}... in {u.split('/')[-2]}/{u.split('/')[-1]}")
        return True

# University level
apply_url = "https://gradadm.usc.edu/domestic-students/how-to-apply/"
waivers_url = "https://gradadm.usc.edu/tools-resources/fee-waivers/"
eng_url = "https://gradadm.usc.edu/prospective-international-students/english-proficiency/"

check(apply_url, "The application fee for most USC graduate programs is $120 ($105 for programs beginning in fall 2026).")
check(waivers_url, "This option is not available to international students.")
check(waivers_url, "Eligibility Requirements: Your intended graduate program has informed you in writing that they will be paying for your USC application fee.")
check(apply_url, "Most USC graduate programs require either GRE or GMAT scores. Please review your program’s website for their test score requirements.")
check(eng_url, "100 or above, with 20 or above in each section.")
check(eng_url, "7 or above, with 6 or above on each band.")
check(eng_url, "USC does not waive the English-proficiency requirement based on any other consideration such as work experience, ESL enrollment, amount of time spent in the U.S., etc. It also cannot be waived on the basis of programs taught in English in non-Anglophone countries.")
check(eng_url, "You hold a bachelor’s degree from a regionally accredited university in the United States or the equivalent of a U.S. bachelor’s degree from an officially recognized university in another qualifying Anglophone country where English is both the only official language and the language of instruction.")

# Viterbi
viterbi_apply = "https://viterbigradadmission.usc.edu/doctoral/how-to-apply-phd/"
viterbi_faq = "https://viterbigradadmission.usc.edu/doctoral/phd-faq/"
check(viterbi_apply, "Fall 2027 deadline: December 15, 2026")
check(viterbi_apply, "GRE Not Required (2027 Applications): All Viterbi School PhD programs except ASTE and ISE")
check(viterbi_faq, "USC tries to fully fund all of its doctoral students. This generally consists of tuition, a stipend for living expenses, and a health benefits package.")

# Physics
phys_url = "https://dornsife.usc.edu/physics/graduate-admissions/"
check(phys_url, "The deadline for submission of applications is December 15, 2026.")
check(phys_url, "Do not require general GRE")
check(phys_url, "For the Physics PhD program, the Physics GRE is recommended.")
check(phys_url, "Your Fee Waiver Memo is also necessary to ensure your application fee is paid for by the department.")

# Chemistry
chem_url = "https://dornsife.usc.edu/chemistry/graduate-admission/"
check(chem_url, "Application deadline: The deadline for submission of applications is December 18, 2026. All application materials, including transcripts and letters of recommendation, must be submitted by this date.")
check(chem_url, "We do not require subject or general GRE")
check(chem_url, "often offer early admission and university-sponsored fellowships to qualified candidates")

# Math
math_url = "https://dornsife.usc.edu/mathematics/admissions/"
check(math_url, "Application Deadline: December 15")
check(math_url, "No. We do not require GRE scores. If you choose to include the GRE mathematics subject test in your application, we will factor your score into our review. However we do not consider the GRE general test or other subject tests as part of our application review.")
check(math_url, "However, students coming from lesser known schools or with non-traditional paths are encouraged to include a GRE mathematics subject test score in their applications.")
check(math_url, "Everyone, regardless of nationality or country of residence, admitted to our PhD Programs receives a comprehensive support package that includes full tuition remission, a competitive stipend, and health and dental insurance.")

# Earth
earth_url = "https://dornsife.usc.edu/earth/graduate/grad-admissions/"
check(earth_url, "The deadline to apply is January 5th for each Fall semester.")
check(earth_url, "The department does not require GRE scores for admission. It is not a necessary expense, nor will it necessarily help your application.")
check(earth_url, "USC Earth Sciences offers a 5-year, fully funded Ph.D. program. Support includes tuition and a yearly stipend (the current 26-27 rate is $47,936) funded by a combination of research assistantship (RA), teaching assistantship (TA), and, in some cases, fellowships.")
check(earth_url, "Step 1: Contact your potential advisor(s).")

# MCB (Biology)
mcb_adm_url = "https://dornsife.usc.edu/mcb/admissions/"
mcb_prog_url = "https://dornsife.usc.edu/mcb/the-mcb-phd-program/"
check(mcb_adm_url, "Admission Deadline: December 1")
check(mcb_adm_url, "Note: GRE scores are not required for admission to the PhD program")
check(mcb_prog_url, "Funding: Our department provides funding for the first five years of your program through a variety of teaching and research assistantships, fellowships, and scholarships.")
