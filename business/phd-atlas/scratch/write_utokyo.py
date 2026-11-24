import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate_data
import audit_quality

CHECKED = "2026-11-15"

ETS_SUBJ_ALL = "https://www.ets.org/gre/score-users/about/subject-tests.html"
ETS_SUBJ_ALL_QUOTE = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"

ETS_CHEM = "https://www.ets.org/gre/test-takers/subject-tests/scores.html"
ETS_CHEM_QUOTE = "The GRE Chemistry Test was discontinued in May 2023."

UTOKYO_TUITION_URL = "https://www.u-tokyo.ac.jp/en/prospective-students/tuition_fees.html"
UTOKYO_SCHOL_URL = "https://www.u-tokyo.ac.jp/en/prospective-students/scholarships.html"
UTOKYO_SCHOL_QUOTE = (
    "A variety of scholarships are available for students who wish to study in Japan. "
    "Although many of them are provided by external entities, there are some scholarships "
    "awarded directly by the University of Tokyo."
)

GSGC_GUIDE_URL = "https://www.s.u-tokyo.ac.jp/GSGC/pdf/Guidelines.pdf"
SCI_GRAD_URL = "https://www.s.u-tokyo.ac.jp/en/admission/graduate.html"

IST_ADM_GUIDE_URL = "https://www.i.u-tokyo.ac.jp/edu/entra/2027_ag_d_e.pdf"
IST_TOEFL_URL = "https://www.i.u-tokyo.ac.jp/edu/entra/Guidelines-for-toefl-scores_2027_e.pdf"
IST_FIN_URL = "https://www.i.u-tokyo.ac.jp/edu/financial-support/index_e.shtml"

IME_URL = "https://www.ime.t.u-tokyo.ac.jp/Prospectus-2027.html"
ENG_GEN_GUIDE_URL = (
    "https://www.t.u-tokyo.ac.jp/hubfs/admission/2026/international-admission/"
    "II%E3%80%90%E5%85%B1%E9%80%9A%E3%80%91General%20Application%20Guidelines%202027_Doctoral%20Degree.pdf"
)


def no_subject_test_field(url=ETS_SUBJ_ALL, quote=ETS_SUBJ_ALL_QUOTE, extra=""):
    val = "No ETS GRE Subject Test exists for this field (ETS offers Subject Tests only in Mathematics, Physics, and Psychology)."
    if extra:
        val += " " + extra
    return {
        "code": "No subject test",
        "value": val,
        "quote": quote,
        "url": url,
    }


def make_university():
    return {
        "id": "utokyo",
        "institution": "The University of Tokyo",
        "country": "Japan",
        "region": "Tokyo",
        "grad_page": "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
        "checked": CHECKED,
        "fields": {
            "app_fee": {
                "code": "30000 JPY",
                "value": "Standard UTokyo graduate entrance examination fee is JPY 30,000 for regular doctoral entrance examinations (e.g., IST, Medicine, GSFS); Special International Graduate Programs such as Science (GSGC / Special Selection) and Engineering (IME / Civil International Program) charge JPY 10,000 and override this centrally.",
                "quote": "Graduate (excl. School of Law) | Examination fee | ¥30,000",
                "url": UTOKYO_TUITION_URL,
                "also": [
                    {
                        "quote": "Examination fee | 1st stage | ¥30,000",
                        "url": UTOKYO_TUITION_URL,
                    }
                ],
            },
            "fee_waiver": {
                "code": "Limited",
                "value": "Japanese Government (MEXT) Scholarship recipients are exempt from examination, admission, and tuition fees; self-financed international applicants cannot obtain an upfront application/examination fee waiver based on financial need (post-enrollment admission/tuition exemptions are handled separately under tight budgets).",
                "quote": "Note: Students receiving a scholarship from the Japanese government (Ministry of Education, Culture, Sports, Science and Technology) do not need to pay tuition and certain other fees.",
                "url": UTOKYO_TUITION_URL,
                "also": [
                    {
                        "quote": "This system provides full or partial exemption from admission/tuition fees for those who are approved after screening based on their application.",
                        "url": "https://www.u-tokyo.ac.jp/en/prospective-students/exemptions.html",
                    }
                ],
            },
            "gre_general": {
                "code": "Not stated",
                "value": "UTokyo sets no university-wide GRE General policy; requirements are decided by each Graduate School and department (required by Engineering IME and most Science GSGC departments, not stated or omitted in IST, Mathematical Sciences, GSFS, and Medicine).",
                "quote": "",
                "url": "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
            },
            "toefl_min": {
                "code": "Not stated",
                "value": "UTokyo has no university-wide minimum TOEFL score; each Graduate School sets its own English proficiency requirement (for example, Medicine Doctoral expects TOEFL iBT new score 3.5 / former 60, whereas IST, Engineering, Science, and GSFS specify no numerical floor).",
                "quote": "",
                "url": "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
            },
            "ielts_min": {
                "code": "Not stated",
                "value": "UTokyo has no university-wide minimum IELTS score; IELTS Academic is accepted alongside TOEFL in certain Graduate Schools (such as Engineering IME, Medicine International Health, and GSFS GPSS), whereas IST and Science GSGC require TOEFL.",
                "quote": "",
                "url": "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
            },
            "english_waiver": {
                "code": "Not stated",
                "value": "English proficiency waiver rules are set separately by each Graduate School rather than centrally (ranging from No waiver in IST and Science [native-speaker exemption only] to Conditional institutional MOI certificate waivers in Engineering IME, Medicine International Health, and GSFS GPSS).",
                "quote": "",
                "url": "https://www.u-tokyo.ac.jp/en/prospective-students/graduate_course_list.html",
            },
        },
        "notes": (
            "QS WUR 2027 #39. Covers all 18 STEM PhD fields across the Graduate Schools of Science, "
            "Mathematical Sciences, Information Science and Technology (IST), Engineering, Frontier Sciences (GSFS), "
            "and Medicine (primarily Hongo, Komaba, and Kashiwa campuses in Greater Tokyo). Admission fee is JPY 282,000 "
            "and standard graduate annual tuition is JPY 535,800 (JPY 520,800 for certain doctoral cohorts). "
            "Most regular Japanese-system doctoral exams require a Master's degree, while Science GSGC provides a 5-year "
            "integrated Master's-to-Doctoral English track from a bachelor's degree."
        ),
    }


def sci_common(field, name, dept, prog_page, gre_gen, gre_subj, entry_route, supervisor_override=None, notes=""):
    fields = {
        "app_fee": {
            "code": "10000 JPY",
            "value": "Application fee for Graduate School of Science international tracks (GSGC and Special Selection for International Applicants) is JPY 10,000 paid by credit card (regular Japanese domestic entrance exams charge JPY 30,000).",
            "quote": "Application Fee | 10,000 yen (Embassy Recommended Monbukagakusho Scholarship Recipients are exempted from paying the Application Fee)",
            "url": SCI_GRAD_URL,
            "also": [{"quote": "10,000 yen (Monbukagakusho Scholarship recipients are exempted from paying the Application Fee.)", "url": GSGC_GUIDE_URL}],
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "Monbukagakusho (MEXT) Scholarship recipients are exempt from the JPY 10,000 application fee; no general need-based application fee waiver is offered.",
            "quote": "10,000 yen (Monbukagakusho Scholarship recipients are exempted from paying the Application Fee.)",
            "url": GSGC_GUIDE_URL,
        },
        "deadline": {
            "code": "2026-12-22",
            "time_sensitive": "2026-12-22",
            "value": "December 22, 2026 (JST) for the Global Science Graduate Course (GSGC) 5-year PhD intake for October 2027 entry (window opens December 7, 2026; Special Selection for International Applicants self-financed/University MEXT round closed October 30, 2026).",
            "quote": "From December 7 to December 22, 2026(J.S.T): for applicants wishing to enroll in October 2027 (with or without a Student Visa)",
            "url": GSGC_GUIDE_URL,
        },
        "gre_general": gre_gen,
        "gre_subject": gre_subj,
        "english_waiver": {
            "code": "No",
            "value": "Only native English speakers may request an advance TOEFL exemption from the Graduate School of Science; an English-medium degree from a non-native English country (such as India) does not waive TOEFL.",
            "quote": "Applicants whose native language is English may in some cases be exempted from submitting a TOEFL score, with the advance approval of the Graduate School of Science.",
            "url": GSGC_GUIDE_URL,
        },
        "supervisor": supervisor_override or {
            "code": "Required",
            "value": "Mandatory pre-application supervisor consultation and email proof of consent are required for GSGC and Special Selection applications.",
            "quote": "Please contact your potential supervisor and submit the proof of your prior consultation such as a copy of correspondence e-mails.",
            "url": GSGC_GUIDE_URL,
        },
        "funding": {
            "code": "Competitive",
            "value": "GSGC provides a monthly stipend of JPY 180,000 (for 2 years MSc + 3 years PhD) plus JSPS/MEXT/SPRING GX/WINGS/TA-RA opportunities across the Graduate School of Science (separate non-GSGC self-financed seats are unfunded at admission).",
            "quote": "10. GSGC Financial Assistance | We will provide a stipend of 180,000 yen per month while the student is on the course (for two years while they are in the Master's program, and for three years while they are in the Doctoral program).",
            "url": GSGC_GUIDE_URL,
        },
        "entry_route": entry_route,
    }
    return {
        "id": f"utokyo--{field}",
        "university": "utokyo",
        "field": field,
        "also_fields": [],
        "name": name,
        "department": dept,
        "program_page": prog_page,
        "checked": CHECKED,
        "fields": fields,
        "notes": notes,
    }


def ime_program(field, name, dept, prog_page, supervisor_field, notes=""):
    fields = {
        "app_fee": {
            "code": "10000 JPY",
            "value": "IME International Graduate Program examination fee is JPY 10,000 payable online by credit card during Procedure 7 (regular Graduate School of Engineering examinations charge JPY 30,000).",
            "quote": "10,000 Japanese Yen is required for the examination fee.",
            "url": IME_URL,
            "also": [{"quote": "10,000 yen is required as the examination fee.", "url": ENG_GEN_GUIDE_URL}],
        },
        "fee_waiver": {
            "code": "Limited",
            "value": "MEXT scholarship awardees are exempt (embassy-recommended primary selectees and CSC PhD candidates do not pay; university-recommended MEXT awardees receive a refund of the examination fee upon enrollment); no need-based waiver exists.",
            "quote": "Examination Fee (at the time of online application) | Students awarded the MEXT scholarships are exempt from the above fees, therefore, the examination fee will be refunded upon enrollment.",
            "url": IME_URL,
        },
        "deadline": {
            "code": "2027-02-17",
            "time_sensitive": "2027-02-17",
            "value": "February 17, 2027 for IME Graduate Program January Application online procedures 1-9 (preceded by July Application Aug 19, 2026 and September Application Oct 14, 2026 for October 2027 MEXT/scholarship rounds).",
            "quote": "January Application | Application Procedure 1-9 | 2/17/2027",
            "url": IME_URL,
        },
        "gre_general": {
            "code": "Required",
            "value": "GRE General Test score is required for all IME Graduate Program applicants (official ETS report to institution code 8596; GMAT is not accepted).",
            "quote": "GRE is required by IME Graduate Program. GMAT is not acceptable.",
            "url": IME_URL,
        },
        "gre_subject": no_subject_test_field(),
        "english_waiver": {
            "code": "Conditional",
            "value": "IME waives TOEFL/IELTS upon submission of an original or university-certified Certificate of English as the Medium of Instruction (or explicit MOI statement on the transcript); native English speakers submit proof of citizenship. (Note: Regular Engineering domestic entrance exams require TOEFL even from native speakers.)",
            "quote": "The Certificate of English as the Medium of Instruction from your university. One original or one certified copy (with certified seal/stamp of the university you belong to or graduated from) is required.",
            "url": IME_URL,
        },
        "supervisor": supervisor_field,
        "funding": {
            "code": "Competitive",
            "value": "Top-qualified September Applicants to IME are nominated for Japanese Government (MEXT) Scholarships or equivalent IME scholarships; SPRING GX, BOOST NAIS, and SEUT-RA doctoral fellowships are also available after entry.",
            "quote": "Top qualified September Applicants who have exceptional academic records will be awarded the Japanese Government's MEXT scholarship by recommendation of the University of Tokyo or scholarships provided by IME Graduate Program",
            "url": IME_URL,
        },
        "entry_route": {
            "code": "Master's usually required",
            "value": "Doctoral Degree International Admission requires a Master's or equivalent degree (with exceptions only via individual eligibility screening for 2+ years of post-bachelor's research or age >= 24; Japanese university graduates are ineligible for International Admission).",
            "quote": "A person who has been conferred, or is expected to be conferred by the day before the admission date in April or October 2027, a degree equivalent to a master’s, doctoral or a professional degree in a country other than Japan.",
            "url": ENG_GEN_GUIDE_URL,
        },
    }
    return {
        "id": f"utokyo--{field}",
        "university": "utokyo",
        "field": field,
        "also_fields": [],
        "name": name,
        "department": dept,
        "program_page": prog_page,
        "checked": CHECKED,
        "fields": fields,
        "notes": notes,
    }


def ist_program(field, name, dept, prog_page, gre_subj, supervisor_field, notes=""):
    fields = {
        "deadline": {
            "code": "2026-11-17",
            "time_sensitive": "2026-11-17",
            "value": "November 17, 2026 at 14:00 JST for the AY2027 Doctoral Program Winter Entrance Examination (application window runs November 11-17, 2026 for October 2027 standard entry or April 2027 early entry; Summer exams run annually in June/August).",
            "quote": "Winter Entrance Examinations | Applications are accepted from Wednesday, November 11, until 14:00 on Tuesday, November 17, 2026 (JST).",
            "url": IST_ADM_GUIDE_URL,
        },
        "gre_subject": gre_subj,
        "english_waiver": {
            "code": "No",
            "value": "All IST applicants, including native English speakers and English-medium graduates, must submit an official TOEFL iBT (or Home Edition; Test Date Score only) to institution code 8445; only UTokyo IST Master's completers may be exempt.",
            "quote": "Even applicants who are native English speakers must submit a TOEFL score.",
            "url": IST_TOEFL_URL,
        },
        "supervisor": supervisor_field,
        "funding": {
            "code": "Competitive",
            "value": "Competitive doctoral financial support at IST includes WINGS TAKUETSU RA (World-leading Innovative Graduate Study Program), Doctoral Student Special Research Assistant (IST-RA), SPRING GX, BOOST NAIS, and MEXT/UTokyo Fellowships.",
            "quote": "Scholarship Information for Self-Supported Students | WINGS (World-leading Innovative Graduate Study Program), UTokyo | Doctoral Student Special Research Assitant (IST-RA) (For doctoral students only) | SPRING GX (For doctoral students only)",
            "url": IST_FIN_URL,
        },
        "entry_route": {
            "code": "Master's usually required",
            "value": "Applicants must hold (or expect to complete) a Master's or Professional degree in Japan or a foreign equivalent (or pass individual eligibility screening with >= 2 years of post-bachelor's research or age >= 24).",
            "quote": "Those who have obtained, or are expected to obtain by March 31, 2027, a Master’s or Professional degree at a Japanese university. | Those who have obtained, or are expected to obtain by March 31, 2027, a degree equivalent to a Master’s or Professional degree in a foreign country.",
            "url": IST_ADM_GUIDE_URL,
        },
    }
    return {
        "id": f"utokyo--{field}",
        "university": "utokyo",
        "field": field,
        "also_fields": [],
        "name": name,
        "department": dept,
        "program_page": prog_page,
        "checked": CHECKED,
        "fields": fields,
        "notes": notes,
    }


def make_programs():
    progs = []

    # 1-5: Graduate School of Science (GSGC + Special Selection)
    sci_either_quote = (
        "One who has been conferred a degree equivalent to that of a bachelor’s degree or is expected to be conferred one before entering the Master’s Program of the University of Tokyo | "
        "If you are currently enrolled in a master’s program or a doctoral program, have completed one such program, or have withdrawn after having fulfilled the requirements of one such program, please submit a transcript of the program."
    )
    sci_either_field = {
        "code": "Either",
        "value": "GSGC accepts Bachelor's graduates into an integrated 5-year Master's-to-Doctoral course, while the Special Selection for International Applicants admits both Master's and Doctoral applicants directly.",
        "quote": sci_either_quote,
        "url": GSGC_GUIDE_URL,
    }

    progs.append(sci_common(
        "physics", "Physics (GSGC / Doctoral), Ph.D.",
        "Graduate School of Science — Department of Physics",
        SCI_GRAD_URL,
        {
            "code": "Not required",
            "value": "Department of Physics requires the GRE Subject Test in Physics rather than the GRE General Test for GSGC and Special Selection.",
            "quote": "The GRE Subject or General Test Score. | Physics required: Physics not required",
            "url": GSGC_GUIDE_URL,
        },
        {
            "code": "Required",
            "value": "GRE Physics Subject Test is required for Department of Physics international applicants (GRE institutional code 7048).",
            "quote": "The GRE Subject or General Test Score. | Physics required: Physics not required",
            "url": GSGC_GUIDE_URL,
        },
        sci_either_field,
        notes="Department of Physics GSGC applicants may list only one potential supervising professor. Regular Special Selection non-GSGC intake closed October 30, 2026; GSGC runs Dec 7-22, 2026.",
    ))

    progs.append(sci_common(
        "astronomy", "Astronomy (GSGC / Doctoral), Ph.D.",
        "Graduate School of Science — Department of Astronomy",
        "https://www.s.u-tokyo.ac.jp/GSGC/overview/index.html",
        {
            "code": "Not required",
            "value": "Department of Astronomy requires the GRE Physics Subject Test and does not require the GRE General Test.",
            "quote": "The GRE Subject or General Test Score. | Astronomy required: Physics not required",
            "url": GSGC_GUIDE_URL,
        },
        {
            "code": "Required",
            "value": "GRE Physics Subject Test is required for Department of Astronomy international applicants (GRE institutional code 7048).",
            "quote": "The GRE Subject or General Test Score. | Astronomy required: Physics not required",
            "url": GSGC_GUIDE_URL,
        },
        sci_either_field,
        notes="Includes research groups on the Hongo Campus, Institute of Astronomy (Mitaka), and associated observatories.",
    ))

    progs.append(sci_common(
        "chemistry", "Chemistry (GSGC / Doctoral), Ph.D.",
        "Graduate School of Science — Department of Chemistry",
        "https://www.chem.s.u-tokyo.ac.jp/chem_graduate/apply_en.html",
        {
            "code": "Required",
            "value": "Department of Chemistry requires the GRE General Test (institutional code 7048); Subject Test is not required.",
            "quote": "The GRE Subject or General Test Score. | Chemistry not required required",
            "url": GSGC_GUIDE_URL,
        },
        no_subject_test_field(
            url=ETS_CHEM,
            quote=ETS_CHEM_QUOTE,
            extra="GSGC table marks Subject Test 'not required' for Chemistry.",
        ),
        sci_either_field,
        notes="Regular Special Selection non-GSGC Doctoral admission closed Oct 30, 2026; GSGC runs Dec 7-22, 2026.",
    ))

    progs.append(sci_common(
        "earth", "Earth and Planetary Science (GSGC / Doctoral), Ph.D.",
        "Graduate School of Science — Department of Earth and Planetary Science",
        "https://www.eps.s.u-tokyo.ac.jp/index.php?page_id=16483",
        {
            "code": "Required",
            "value": "GRE score is required: applicants must submit either the GRE General Test or the GRE Subject Test in Physics or Mathematics, subject to prior confirmation with their prospective supervisor.",
            "quote": "Regarding GRE scores in the application materials You must submit a score for either general, subject Physics or subject Mathematics.",
            "url": "https://www.eps.s.u-tokyo.ac.jp/index.php?page_id=16483",
        },
        no_subject_test_field(
            extra="Department accepts GRE Subject Physics or Mathematics as an alternative to the GRE General Test upon supervisor confirmation."
        ),
        sci_either_field,
        notes="Spans Atmospheric & Oceanic Science, Space & Planetary Science, Earth & Planetary System Science, Solid Earth Science, and Geosphere & Biosphere Science. GSGC Master's applicants take a 20-minute online aptitude exam in mathematics, physics, or earth science.",
    ))

    progs.append(sci_common(
        "biology", "Biological Sciences (GSGC / Doctoral), Ph.D.",
        "Graduate School of Science — Department of Biological Sciences",
        "https://www.bs.s.u-tokyo.ac.jp/admission/",
        {
            "code": "Required",
            "value": "GRE General Test score is required (Analytical Writing is not factored into decisions; applicants may alternatively submit a GRE Subject Test score in Mathematics, Physics, or Chemistry).",
            "quote": "Applicants are required to report their TOEFL and GRE General Test score. | Applicants may submit their GRE Subject Test score (in Mathematics, Physics or Chemistry) instead of a GRE General Test score.",
            "url": "https://www.bs.s.u-tokyo.ac.jp/admission/",
        },
        no_subject_test_field(),
        {
            "code": "Direct from bachelor's",
            "value": "The open December 7-22, 2026 international intake for Biological Sciences is the 5-year GSGC Master's-to-Doctoral track admitting Bachelor's holders (the non-GSGC Special Selection Doctoral window closed Oct 30, 2026; Regular Doctoral in Jan 4-6, 2027 is conducted in Japanese).",
            "quote": "One who has been conferred a degree equivalent to that of a bachelor’s degree or is expected to be conferred one before entering the Master’s Program of the University of Tokyo",
            "url": GSGC_GUIDE_URL,
        },
        supervisor_override={
            "code": "Required",
            "value": "All applicants to the Department of Biological Sciences must contact their potential supervisor(s) well before applying.",
            "quote": "All applicants to the Department of Biological Sciences must contact their potential supervisor(s) well before applying.",
            "url": "https://www.bs.s.u-tokyo.ac.jp/admission/",
        },
        notes="Note: Department web page still lists legacy GRE Chemistry alongside Physics and Mathematics even though ETS discontinued GRE Chemistry in May 2023. GSGC interview for Oct 2027 entry is scheduled for January 27, 2027.",
    ))

    # 6: Mathematical Sciences
    math_guide_url = "https://www.ms.u-tokyo.ac.jp/kyoumu_e/liaison/guide_e.html"
    math_pdf_url = "https://www.ms.u-tokyo.ac.jp/kyoumu/ab618a1da5ae3af387a2609065bc68980102cda1.pdf"
    progs.append({
        "id": "utokyo--math",
        "university": "utokyo",
        "field": "math",
        "also_fields": [],
        "name": "Mathematical Sciences, Ph.D.",
        "department": "Graduate School of Mathematical Sciences",
        "program_page": math_guide_url,
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "2027-01-07",
                "time_sensitive": "2027-01-07",
                "value": "January 7, 2027 (15:00 JST, window Jan 5-7, 2027) for the Regular Ph.D. Entrance Examination for April 2027 enrollment (Special Selection for Overseas Residents for April 2027 enrollment closed September 30, 2026).",
                "quote": "Application forms are posted on the website from late April of the previous year. The deadline for the application is in early January.",
                "url": math_guide_url,
                "also": [
                    {
                        "quote": "令和 9（2027）年１月 5 日（火）10 時から１月 7 日（木）15 時まで",
                        "url": math_pdf_url,
                    }
                ],
            },
            "gre_subject": {
                "code": "Not stated",
                "value": "The Graduate School of Mathematical Sciences does not state any GRE General or GRE Mathematics Subject Test requirement for either the Regular Ph.D. Entrance Examination or the Special Selection for Overseas Residents.",
                "quote": "",
                "url": math_guide_url,
            },
            "supervisor": {
                "code": "Not stated",
                "value": "The AY2027 Ph.D. Entrance Examination Guide does not state a pre-application prospective UTokyo supervisor consent requirement (it only requires an academic-advisor Japanese-proficiency certificate for non-Japanese-degree holders; Overseas Special Selection lists 'names of the possible supervisors' without stating prior consent is required).",
                "quote": "",
                "url": math_guide_url,
            },
            "funding": {
                "code": "Competitive",
                "value": "Competitive funding via MEXT Scholarships (Embassy or University recommendation), the University of Tokyo Fellowship, and limited private scholarships.",
                "quote": "Overseas applicants are eligible for the Japanese Government Scholarships, sometimes called the Monbukagakusho (MEXT) Scholarships. In addition, there are the University of Tokyo Fellowship and a few private scholarships that provide a lesser amount of support.",
                "url": math_guide_url,
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Ph.D. entry usually requires a Master's degree (note that the International Liaison Guide recommends overseas Master's holders enter the Master's course for smooth transition, though direct Ph.D. entry is offered for Master's holders).",
                "quote": "Two years in residence for a Master's degree and three years for a Ph.D. are usually required.",
                "url": math_guide_url,
            },
        },
        "notes": "Special Selection for Overseas Residents charges a JPY 10,000 application fee (regular Ph.D. entrance exam is JPY 30,000) and closed September 30, 2026 for 2027 enrollment. Regular Ph.D. exam is oral and held in early February 2027 at Komaba Campus.",
    })

    # 7-9: Graduate School of Information Science and Technology (cs, statistics, datasci)
    progs.append(ist_program(
        "cs",
        "Computer Science, Ph.D.",
        "Graduate School of Information Science and Technology — Department of Computer Science",
        "https://www.i.u-tokyo.ac.jp/edu/course/cs/admission_e.shtml",
        no_subject_test_field(),
        {
            "code": "Required",
            "value": "Before submitting the Application Form for Winter/Doctoral admission, applicants must contact their prospective supervisor and show their research proposals.",
            "quote": "Before sending an Application Form, applicants must contact their prospective supervisor and show their research proposals.",
            "url": "https://www.i.u-tokyo.ac.jp/edu/course/cs/cs_admission_guide2027_en.pdf",
        },
        notes="English-based Winter Entrance Examination accepts Doctoral applications Nov 11-17, 2026 (no Master's intake in Winter). Official TOEFL Institutional Score Report must reach IST by Dec 8, 2026.",
    ))

    progs.append(ist_program(
        "statistics",
        "Mathematical Informatics (Statistics & Applied Mathematics), Ph.D.",
        "Graduate School of Information Science and Technology — Department of Mathematical Informatics",
        "https://www.i.u-tokyo.ac.jp/edu/course/mi/admission_e.shtml",
        {
            "code": "Not stated",
            "value": "Department of Mathematical Informatics does not state a GRE General or GRE Mathematics Subject Test requirement (written/oral exams and TOEFL iBT are required).",
            "quote": "",
            "url": "https://www.i.u-tokyo.ac.jp/edu/course/mi/upload/mi-2027-e.pdf",
        },
        {
            "code": "Required",
            "value": "Applicants are required to meet with their preferred faculty advisor prior to the submission of their applications.",
            "quote": "Applicants are required to meet with their preferred faculty advisor prior to the submission of their applications.",
            "url": "https://www.i.u-tokyo.ac.jp/edu/course/mi/upload/mi-2027-e.pdf",
        },
        notes="Covers statistical science, mathematical informatics, optimization, and systems engineering.",
    ))

    progs.append(ist_program(
        "datasci",
        "Creative Informatics (Data Science & AI), Ph.D.",
        "Graduate School of Information Science and Technology — Department of Creative Informatics",
        "https://www.i.u-tokyo.ac.jp/edu/course/ci/admission_e.shtml",
        no_subject_test_field(),
        {
            "code": "Not stated",
            "value": "The Department of Creative Informatics 2027 Admission Guide advises Doctoral applicants to 'make close contact with their prospective faculty advisor before the application period' and select an advisor in the Web Application System, without stating a formal acceptance-letter requirement.",
            "quote": "",
            "url": "https://www.i.u-tokyo.ac.jp/edu/course/ci/2026/2027admin-guide-en.pdf",
        },
        notes="Cross-departmental Data Science training is also offered via The University of Tokyo Data Science School (UTokyoDSS, https://dss.i.u-tokyo.ac.jp/), alongside AI/ML research in Computer Science and Mathematical Informatics.",
    ))

    # 10-14: Graduate School of Engineering — IME (mech, ece, materials, chemeng, bme)
    ime_sup_req = {
        "code": "Required",
        "value": "Only applicants who obtain an Acceptance Letter from a prospective IME supervisor during Procedure 10-11 may advance to final paper submission (Procedure 12).",
        "quote": "Only those who receive an acceptance letter from prospective supervisor are eligible to proceed to the next application step for IME Graduate Program.",
        "url": IME_URL,
    }
    mech_sup_not_req = {
        "code": "Not required",
        "value": "Unlike other IME departments, Department of Mechanical Engineering applicants do NOT need a prospective supervisor acceptance letter (admission instead uses a document-based first screening; Feb 24, 2027 for January Application).",
        "quote": "Acceptance Letter from your prospective supervisor. (Exept Mechanical Engineering) | Applicants of Department of Mechanical Engineering don’t need to receive the acceptance letter, instead there is the first screening.",
        "url": IME_URL,
    }

    progs.append(ime_program(
        "mech",
        "Mechanical Engineering (IME / Engineering), Ph.D.",
        "Graduate School of Engineering — Department of Mechanical Engineering",
        "https://www2.mech.t.u-tokyo.ac.jp/admissions/?lang=en",
        mech_sup_not_req,
        notes="IME offers both April and October Doctoral entry; the School of Engineering also operates a Schedule B (Winter) Regular Doctoral Exam (Japanese/English track).",
    ))

    progs.append(ime_program(
        "ece",
        "Electrical Engineering and Information Systems (IME / Engineering), Ph.D.",
        "Graduate School of Engineering — Department of Electrical Engineering and Information Systems",
        "https://www.eeis.t.u-tokyo.ac.jp/en/index.html",
        ime_sup_req,
        notes="Participates in IME April and October Doctoral intakes as well as Schedule B (Winter) Regular Doctoral Exam.",
    ))

    progs.append(ime_program(
        "materials",
        "Materials Engineering (IME / Engineering), Ph.D.",
        "Graduate School of Engineering — Department of Materials Engineering",
        "https://www.material.t.u-tokyo.ac.jp/e/prospective_students/",
        ime_sup_req,
        notes="IME Materials Engineering Course admits Doctoral applicants for October 2027 entry; does not offer Schedule B Winter regular admission in AY2027.",
    ))

    progs.append(ime_program(
        "chemeng",
        "Chemical System Engineering (IME / Engineering), Ph.D.",
        "Graduate School of Engineering — Department of Chemical System Engineering",
        "https://www.chemsys.t.u-tokyo.ac.jp/curriculum/graduate/admission/?lang=en",
        ime_sup_req,
        notes="Participates in both IME (October 2027 Doctoral entry) and Schedule B (Winter) Regular Doctoral Exam.",
    ))

    progs.append(ime_program(
        "bme",
        "Bioengineering (IME / Engineering), Ph.D.",
        "Graduate School of Engineering — Department of Bioengineering",
        "https://bioeng.t.u-tokyo.ac.jp/admissions/",
        ime_sup_req,
        notes="IME Bioengineering offers the Doctoral course only (October 2027 entry).",
    ))

    # 15: Civil Engineering (Engineering — Civil Special International Graduate Program)
    civil_url = "https://www.civil.t.u-tokyo.ac.jp/en/admission/"
    progs.append({
        "id": "utokyo--civil",
        "university": "utokyo",
        "field": "civil",
        "also_fields": [],
        "name": "Civil Engineering (International Graduate Program), Ph.D.",
        "department": "Graduate School of Engineering — Department of Civil Engineering",
        "program_page": civil_url,
        "checked": CHECKED,
        "fields": {
            "app_fee": {
                "code": "10000 JPY",
                "value": "Graduate School of Engineering International Admission Programs examination fee is JPY 10,000 paid online via T-cens / E-shiharai.",
                "quote": "10,000 yen is required as the examination fee.",
                "url": ENG_GEN_GUIDE_URL,
            },
            "fee_waiver": {
                "code": "Limited",
                "value": "MEXT Embassy-recommended primary selectees and CSC PhD course applicants are exempt from the JPY 10,000 examination fee (University-recommended MEXT awardees are refunded upon enrollment); no general need-based waiver is available.",
                "quote": "*MEXT scholarship candidates who have passed the primary selection at the Japanese embassy in their home countries, and applicants for CSC PhD course are not required to pay this fee.",
                "url": ENG_GEN_GUIDE_URL,
            },
            "deadline": {
                "code": "2027-03-19",
                "time_sensitive": "2027-03-19",
                "value": "March 19, 2027 for 2027 Autumn intake (International Graduate Program in Civil Engineering and Infrastructure Studies; opened September 1, 2026 via T-cens).",
                "quote": "Application Period for 2027 Autumn intake：01 September 2026 - 19 March 2027",
                "url": civil_url,
            },
            "gre_subject": no_subject_test_field(),
            "supervisor": {
                "code": "Not stated",
                "value": "The Department of Civil Engineering international admission page does not state whether pre-application supervisor contact is mandatory prior to registering on T-cens.",
                "quote": "",
                "url": civil_url,
            },
            "funding": {
                "code": "Competitive",
                "value": "Department nominates ~30 candidates annually across partner scholarship organizations (MEXT University/Embassy Recommendation, ADB-Japan Scholarship, UEDA Foundation); international track requires a full scholarship (or approved external scholarship such as JICA/LPDP).",
                "quote": "The Department of Civil Engineering will nominate qualified candidates and recommend them to partner scholarship organizations, as listed below. Approximately 30 scholarships are disbursed through the following partner organizations every year.",
                "url": civil_url,
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Doctoral course applicants must have completed (or expect to complete) 18 years of school education with a Master's or equivalent degree.",
                "quote": "Doctoral course applicants | 5.Those who have completed, or are expected to complete, 18 years of school education by September 30 of the enrolment year, upon completion of their Master's or equivalent degree.*",
                "url": civil_url,
            },
        },
        "notes": "Students already residing in Japan are ineligible for the International Graduate Program and must apply through Regular Admission. English proficiency is required ('linguistic skills required to take classes and receive research guidance in English'), with no specific TOEFL/IELTS score cutoff stated.",
    })

    # 16: Graduate School of Frontier Sciences (environment)
    gpss_pdf_url = "https://www.k.u-tokyo.ac.jp/en/assets/files/12GPSS_BD_e.pdf"
    progs.append({
        "id": "utokyo--environment",
        "university": "utokyo",
        "field": "environment",
        "also_fields": [],
        "name": "Sustainability Science & Environmental Studies (GSFS), Ph.D.",
        "department": "Graduate School of Frontier Sciences — Graduate Program in Sustainability Science (GPSS) / Division of Environmental Studies",
        "program_page": "https://www.k.u-tokyo.ac.jp/en/exam/info/",
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "2026-11-17",
                "time_sensitive": "2026-11-17",
                "value": "November 17, 2026 at 23:00 JST (Schedule B application period Nov 11-17, 2026) for the Graduate Program in Sustainability Science (GPSS) Doctoral Program.",
                "quote": "Graduate Program in Sustainability Science | 【Deadline】November 17, 2026",
                "url": gpss_pdf_url,
            },
            "gre_subject": no_subject_test_field(),
            "english_waiver": {
                "code": "Conditional",
                "value": "GPSS exempts applicants from TOEFL/IELTS if they graduated (or will graduate) from a university or graduate school where English is the official language, provided an official university-issued document proves this at application. (Note: sister Department of Natural Environmental Studies restricts waiver to US/UK/Australia/Canada/NZ graduates.)",
                "quote": "graduate from a university or a graduate school where English is the official language | are exempted from submitting English Language Competency Test Score Reports. In case 3) above, applicants must submit an official document issued by the university to prove it at the time of application.",
                "url": gpss_pdf_url,
            },
            "supervisor": {
                "code": "Required",
                "value": "Doctoral course applicants at GSFS must contact prospective professors prior to application to confirm research alignment.",
                "quote": "If you are a doctoral course applicant, please be sure to contact professors prior to application.",
                "url": "https://www.k.u-tokyo.ac.jp/en/exam/faq/",
            },
            "funding": {
                "code": "Competitive",
                "value": "Competitive doctoral support at GSFS includes SPRING GX (JPY 180,000/mo; JPY 90,000/mo for international recipients from FY2027 + JPY 360k/yr research), BOOST NAIS (JPY 280,000/mo), WINGS TAKUETSU RA (up to JPY 180,000/mo), JSPS DC1/DC2 (JPY 227,000/mo), and RA/TA positions.",
                "quote": "Research stipend: 180,000 yen/month (90,000 yen/month for international recipients from FY2027)",
                "url": "https://www.k.u-tokyo.ac.jp/en/gsfs/financial_support/",
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "GSFS Doctoral Schedule B requires a Master's or equivalent degree (with Master's thesis/equivalent research submission and summary; bachelor's holders qualify only with >= 2 years of post-bachelor's research via individual screening).",
                "quote": "Submit a summary written in English of your master’s thesis work or equivalent",
                "url": gpss_pdf_url,
            },
        },
        "notes": "GSFS Kashiwa campus Division of Environmental Studies also includes Department of Natural Environmental Studies (Schedule B additional docs deadline Jan 15, 2027) and Department of Ocean Technology, Policy, and Environment.",
    })

    # 17: Medicine — School of International Health (biomed)
    sih_pdf_url = "https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/koukikoku2027E.pdf"
    sih_eng_url = "https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/englishnotes_2027koukikokuho_en.pdf"
    progs.append({
        "id": "utokyo--biomed",
        "university": "utokyo",
        "field": "biomed",
        "also_fields": [],
        "name": "International Health (Global Health Sciences), Ph.D.",
        "department": "Graduate School of Medicine — School of International Health",
        "program_page": "https://www.sih.m.u-tokyo.ac.jp/",
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "2027-01-07",
                "time_sensitive": "2027-01-07",
                "value": "January 7, 2027 (application window Jan 5-7, 2027 for April 2027 entry; TOEFL/IELTS exemption requests for April 2027 entry closed Nov 9, 2026; October 2026 entry closed June 17, 2026).",
                "quote": "application for April 2027 entry between Tuesday, 5 January and Thursday, 7 January, 2027",
                "url": sih_pdf_url,
            },
            "gre_subject": no_subject_test_field(),
            "english_waiver": {
                "code": "Conditional",
                "value": "TOEFL/IELTS waiver is available if the applicant's entire bachelor's institution (not just the department) had English as the primary language of instruction and an institutional certificate is submitted for advance review (Nov 9, 2026 for April 2027 entry; master's MOI does not qualify).",
                "quote": "where English is the primary language of instruction for the entire institution, not just the applicant's specific department or program. In this case, the applicant must provide a certificate issued by the institution, confirming the primary language of instruction.",
                "url": sih_eng_url,
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants to the School of International Health Doctoral Program must contact a faculty member before applying.",
                "quote": "Applicants must contact faculty member before applying.",
                "url": sih_pdf_url,
            },
            "funding": {
                "code": "Competitive",
                "value": "Competitive funding via MEXT Scholarships, the University of Tokyo Fellowship, MEXT Honors Scholarship, JSPS DC fellowships, and private foundation scholarships.",
                "quote": UTOKYO_SCHOL_QUOTE,
                "url": UTOKYO_SCHOL_URL,
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Requires a Master's or professional degree from a Japanese or foreign university (or 2+ years of post-bachelor's research via individual eligibility review).",
                "quote": "Persons who have been awarded or are expected to be awarded by 31 March 2027 (Note 5) an academic degree in a foreign country which is equivalent to a master's or professional degree",
                "url": sih_pdf_url,
            },
        },
        "notes": "School of International Health admits for both October and April entries using English TOEFL/IELTS screening + online oral exam (no Japanese proficiency certificate required, unlike the 4-year Doctoral Program in Medicine). Also covers Human Genetics and Biomedical Chemistry majors.",
    })

    # 18: Medicine — Doctoral Program in Medicine / Neuroscience (neuro)
    med_pdf_url = "https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/doctor2027E.pdf"
    med_eng_url = "https://www.m.u-tokyo.ac.jp/daigakuin/apply/file/englishnotes2027DR_0507en.pdf"
    progs.append({
        "id": "utokyo--neuro",
        "university": "utokyo",
        "field": "neuro",
        "also_fields": [],
        "name": "Medicine (Neuroscience Specializations), Ph.D.",
        "department": "Graduate School of Medicine — Doctoral Program in Medicine",
        "program_page": "https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html",
        "checked": CHECKED,
        "fields": {
            "deadline": {
                "code": "Not stated",
                "value": "AY2027 Doctoral Program in Medicine applications closed July 14, 2026 (July 3-14, 2026); AY2028 dates have not yet been published.",
                "quote": "",
                "url": "https://www.m.u-tokyo.ac.jp/english/daigakuin/apply/appguidemain.html",
            },
            "gre_subject": {
                "code": "Not stated",
                "value": "The Graduate School of Medicine Doctoral Program in Medicine Application Guide does not state any GRE Subject Test requirement.",
                "quote": "",
                "url": med_pdf_url,
            },
            "toefl_min": {
                "code": "3.5 (new scale)",
                "value": "Expected baseline English proficiency at enrollment is TOEFL iBT new score 3.5 (formerly 60; Institution Code 8426); applicants below this level may still apply but risk being judged lacking research English ability.",
                "quote": "As a basic expectation at the time of enrollment, applicants are expected to demonstrate English proficiency equivalent to TOEFL iBT new score 3.5 (formerly 60).",
                "url": med_eng_url,
            },
            "english_waiver": {
                "code": "No",
                "value": "TOEFL exemptions are strictly limited to applicants who completed all 18 years of primary, secondary, and tertiary education ending in medicine, dentistry, pharmacy, or veterinary medicine in a country whose primary language of instruction is English (non-medical Indian STEM degrees are not eligible).",
                "quote": "the applicant who have completed or are expected to complete an 18-year school education (primary, secondary, and tertiary education) in which the final field of study is medicine, dentistry, pharmacy, or veterinary medicine in a country in which the primary language of instruction is English.",
                "url": med_eng_url,
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants must contact their prospective faculty member before applying.",
                "quote": "Applicants must contact faculty member before applying.",
                "url": med_pdf_url,
            },
            "funding": {
                "code": "Competitive",
                "value": "Competitive funding via MEXT Scholarships, the University of Tokyo Fellowship, MEXT Honors Scholarship, JSPS DC fellowships, and private foundation scholarships.",
                "quote": UTOKYO_SCHOL_QUOTE,
                "url": UTOKYO_SCHOL_URL,
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Requires an 18-year/5-year degree in medicine, dentistry, pharmacy, or veterinary medicine, OR a Master's degree (with individual pre-application eligibility review for foreign Master's holders) or >= 2 years of post-bachelor's research.",
                "quote": "This clause pertains to persons on whom a Master's degree has been conferred by a foreign university; note that, before applying for admission, applicants must undergo an individual eligibility review",
                "url": med_pdf_url,
            },
        },
        "notes": "4-year Ph.D. in Medicine offering Neuropathology, Neurochemistry, Neurobiology, Developmental Neuroscience, Cognitive Neuroscience, Systems Medical Neuroscience, and Sensory Motor Neuroscience. Non-Japanese applicants who did not graduate from a Japanese university must also submit a Certificate of Japanese Language Ability.",
    })

    return progs


def main():
    texts = validate_data.cached_texts()
    odd = set()
    for p in (ROOT / ".cache" / "pages").glob("*.json"):
        r = json.loads(p.read_text(encoding="utf-8"))
        if "via" in r or "method" not in r:
            odd.update({r["url"], r.get("final_url", r["url"])})

    uni = make_university()
    progs = make_programs()
    assert len(progs) == 18

    # Preflight check on quotes, audit_quality rules, and odd cache
    issues = []
    for rec in [uni] + progs:
        rid = rec["id"]
        for k, fld in rec["fields"].items():
            sources = [(fld.get("quote", ""), fld.get("url", ""))] + [
                (a.get("quote", ""), a.get("url", "")) for a in fld.get("also", [])
            ]
            for q, u in sources:
                if not q:
                    continue
                if u in odd:
                    issues.append(f"ODD_CACHE {rid}.{k}: {u}")
                page = texts.get(u)
                if page is None:
                    issues.append(f"UNCACHED {rid}.{k}: {u}")
                    continue
                for part in validate_data.quote_parts(q):
                    if validate_data.norm(part) not in page:
                        issues.append(f"QUOTE_MISMATCH {rid}.{k} on {u}: {part[:90]}")
            q0 = fld.get("quote", "")
            code0 = fld.get("code", "")
            if q0 and code0 not in ("Not stated", "No subject test"):
                if k in audit_quality.KW and not re.search(audit_quality.KW[k], q0, re.I):
                    issues.append(f"OFF_TOPIC {rid}.{k} ({code0}): {q0[:90]}")
                if k in audit_quality.ABSENCE and code0 == audit_quality.ABSENCE[k][0] and not re.search(audit_quality.ABSENCE[k][1], q0, re.I):
                    issues.append(f"ABSENCE {rid}.{k} ({code0}): {q0[:90]}")

    if issues:
        print("PREFLIGHT FAILED:")
        for it in issues:
            print("  ", it)
        sys.exit(1)

    u_dir = ROOT / "data" / "staging" / "universities"
    p_dir = ROOT / "data" / "staging" / "programs"
    u_dir.mkdir(parents=True, exist_ok=True)
    p_dir.mkdir(parents=True, exist_ok=True)

    (u_dir / "utokyo.json").write_text(json.dumps(uni, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for p in progs:
        (p_dir / f"{p['id']}.json").write_text(json.dumps(p, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Add to data/universities.json if absent
    ulist_path = ROOT / "data" / "universities.json"
    ulist = json.loads(ulist_path.read_text(encoding="utf-8"))
    if not any(u["id"] == "utokyo" for u in ulist["universities"]):
        ulist["universities"].append({
            "id": "utokyo",
            "name": "The University of Tokyo",
            "country": "Japan",
            "region": "Tokyo",
            "kind": "university",
            "wave": 5,
        })
        ulist_path.write_text(json.dumps(ulist, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    # Update handoff/qs_top300.csv row 40
    csv_path = ROOT / "handoff" / "qs_top300.csv"
    lines = csv_path.read_text(encoding="utf-8").splitlines()
    updated = False
    for i, line in enumerate(lines):
        if line == "39,The University of Tokyo,Japan,High income,,add":
            lines[i] = "39,The University of Tokyo,Japan,High income,utokyo,covered"
            updated = True
            break
    if updated:
        csv_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote staging utokyo.json + {len(progs)} programs (0 preflight issues). csv_updated={updated}")


if __name__ == "__main__":
    main()
