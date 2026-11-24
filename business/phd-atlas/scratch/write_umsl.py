import json
import os
import sys
from pathlib import Path

os.environ.setdefault("ATLAS_OUT", "data/staging")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import rec  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "pages"
CHECKED = "2026-11-14"
UID = "umsl"

GS_HOW = "https://www.umsl.edu/gradschool/prospective/how-to-apply.html"
GS_FEE = "https://www.umsl.edu/gradschool/prospective/application-fee.html"
GS_FAQ = "https://www.umsl.edu/gradschool/prospective/admissions-faq.html"
GS_DOC = "https://www.umsl.edu/gradschool/gradprograms/doctoral.html"
GS_ASST = "https://www.umsl.edu/gradschool/funding/assistantship.html"
GLOBAL_GRAD = "https://www.umsl.edu/global/admissions/grad.html"
GLOBAL_ENG = "https://www.umsl.edu/global/admissions/englishrequirements.html"
ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"

NO_SUBJ = (
    "No subject test",
    "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (none in this field).",
    "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
    ETS_SUBJ,
)


def main():
    by_url = {}
    for p in CACHE.glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        by_url[d["url"]] = d["text"]

    def pick(url, *candidates):
        txt = by_url[url]
        for c in candidates:
            if c in txt and "\ufffd" not in c:
                return c
        raise ValueError(f"None matched cleanly in {url}:\n{candidates}")

    rec.save_university(
        UID,
        "University of Missouri-St. Louis",
        "USA",
        "Missouri",
        GS_HOW,
        {
            "app_fee": (
                "40 USD",
                "$40 for international applicants ($50 for U.S. domestic applicants), non-refundable and paid only once across UMSL graduate applications.",
                "pay the non refundable application fee ($50 for U.S. applicants, $40 for international applicants) | Applicants to the Graduate School are only required to pay the application fee once.",
                GS_FEE,
                {
                    "also": [
                        {
                            "quote": "Complete the international student application and submit the $40 application fee.",
                            "url": GLOBAL_GRAD,
                        }
                    ]
                },
            ),
            "fee_waiver": (
                "Limited",
                "Fee waivers apply only to prior UMSL graduate applicants who already paid the fee, U.S. military veterans, McNair Scholars, applicants with an UMSL recruitment event/mailer waiver code, or occasional department-level waivers.",
                "The Graduate School only waives application fees on the following conditions: | The applicant has paid the Graduate-level fee before. | The applicant is a veteran. | The applicant is a Mc Nair Scholar | The applicant has received a waiver code from an event or mailer | Sometimes programs will offer fee waivers to just their applicants.",
                GS_HOW,
                {
                    "also": [
                        {
                            "quote": "McNair Scholars - The University of Missouri-St. Louis welcomes McNair Scholars by waiving the application fee.",
                            "url": GS_FEE,
                        }
                    ]
                },
            ),
            "gre_general": (
                "Not stated",
                "UMSL Graduate School does not require the GRE centrally, noting that test requirements are set by individual degree programs (none of UMSL's four active STEM Ph.D. programs require GRE General).",
                "",
                GS_FAQ,
            ),
            "toefl_min": (
                "4.5 (new scale)",
                "Recommended UMSL Global graduate minimum is TOEFL iBT 4.5 on the 1-6 scale (79 on the 0-120 scale; institution code 6889; requirements vary by department, e.g., Biology requires 80 iBT).",
                "Minimum requirements vary by department, but it is recommended that graduate applicants have at least a: | TOEFL: 79 (4.5)",
                GLOBAL_GRAD,
            ),
            "ielts_min": (
                "6.5",
                "Recommended UMSL Global graduate minimum is IELTS Academic 6.5 (requirements vary by department).",
                "Minimum requirements vary by department, but it is recommended that graduate applicants have at least a: | IELTS Academic: 6.5",
                GLOBAL_GRAD,
            ),
            "english_waiver": (
                "Conditional",
                "Exempt for U.S. citizens/permanent residents, current U.S. H-1B/L-1 visa holders, ELS Level 112 completers, citizens of UMSL-recognized English-speaking countries (Section 1.5; excludes India), or graduates of U.S./recognized English-speaking-country institutions within the past two years (or with 2 of the past 3 years' residence in an English-speaking country). International TAs must also demonstrate oral English proficiency.",
                "Graduate applicants seeking a waiver of the English language proficiency requirement based on prior academic experience must have graduated from a U.S. institution or a UMSL-recognized English-speaking country within the past two years to qualify for an automatic exemption.",
                GLOBAL_ENG,
                {
                    "also": [
                        {
                            "quote": "Applicants whose qualifying degree was awarded more than two years prior to the date of application must demonstrate that they have resided in an English-speaking country for at least two of the past three years.",
                            "url": GLOBAL_ENG,
                        }
                    ]
                },
            ),
        },
        notes=(
            "UMSL offers 4 active STEM Ph.D. fields: biology (Biology Ph.D., also covers environment via the Ecology, Evolution and Behavior emphasis), "
            "chemistry (Chemistry Ph.D.), cs (Mathematical and Computational Science Ph.D., Computer Science Option), and neuro (Psychology Ph.D., Psychological and Brain Sciences, CIP 42.2799). "
            "Suspended STEM Ph.D. programs no longer accepting applications since Fall 2021: Physics Ph.D. (bulletin.umsl.edu/programs/physics-phd/) and Mathematical and Computational Science Ph.D. Mathematics & Statistics emphases. "
            "UMSL offers Engineering only at the undergraduate B.S. level via the UMSL/Washington University Joint Undergraduate Engineering Program (no Engineering Ph.D.s). "
            "Excluded non-STEM/clinical doctorates: Business Administration DBA & Ph.D. (Supply Chain and Analytics), Criminology and Criminal Justice Ph.D., Education Ph.D. & Ed.D., Nursing Ph.D. & DNP, Political Science Ph.D., Optometry O.D., and Clinical Community Psychology Ph.D."
        ),
        checked=CHECKED,
    )

    # 1. Biology Ph.D. (also environment)
    bio_app = "https://www.umsl.edu/~biology/Graduate%20Programs/applic.html"
    bio_pdf = "https://www.umsl.edu/gradschool/gradprograms/profiles/doc/phd-bioprofile.pdf"
    bio_eeb = "https://bulletin.umsl.edu/programs/biology-phd-ecology-evolution-and-behavior-emphasis/"
    rec.save_program(
        UID,
        "biology",
        "Department of Biology",
        bio_app,
        {
            "deadline": (
                "2026-12-01",
                "Department Application and Admission page and Graduate School Doctoral directory list December 1 for Fall admission (Graduate School profile PDF prints December 15).",
                "Applications are due by December 1 for admission for the following academic year.",
                bio_app,
                {
                    "inferred": "year",
                    "also": [
                        {"quote": "Biology Ph.D. | Application Deadlines | Fall - December 1", "url": GS_DOC},
                        {"quote": "Fall Semester: December 15", "url": bio_pdf},
                    ],
                },
            ),
            "gre_general": (
                "Not required",
                "GRE General scores are optional/encouraged but not required for Biology Ph.D. admission.",
                "GRE Scores (Optional) | GRE scores (Verbal, Quantitative, and Analytical) are encouraged but not required.",
                bio_app,
            ),
            "gre_subject": NO_SUBJ,
            "supervisor": (
                "Required",
                "Department states applicants are not admitted to the Ph.D. program without support from a potential faculty advisor and must identify faculty members in the statement of purpose (Bulletin notes EEB admits typically enter with an advisor agreement while CMB admits may rotate through three labs).",
                "Students are not admitted to the Ph.D. program without support from a potential faculty advisor. Prospective students interested in the Ph.D. program or the thesis-based M.S. program are strongly encouraged to contact faculty members in their area of interest prior to applying.",
                bio_app,
                {
                    "also": [
                        {
                            "quote": "Students entering the program with an agreement in hand may join the lab in their first semester (this is more common for the EEB emphasis). Alternatively, students entering the program may rotate through three labs to identify a permanent lab and advisor (more common for the CMB emphasis).",
                            "url": bio_eeb,
                        }
                    ]
                },
            ),
            "funding": (
                "Typical",
                "Competitive GTA/GRA support for Ph.D. students provides at least $10,000 per Fall/Spring semester ($20,000 for 10 months) plus Graduate School or advisor tuition coverage for up to five years (profile PDF prints legacy $8,000/term).",
                "Teaching and research assistantships are awarded competitively to qualified Ph.D. students. | A minimum of $10,000 per semester for up to five years (Fall and Spring semesters; totaling 10 months). | Tuition is covered by the Graduate School (for teaching assistants) or by research advisors (for research assistants).",
                bio_app,
                {
                    "also": [
                        {
                            "quote": "Assistantships are currently funded at $8,000 per academic term",
                            "url": bio_pdf,
                        }
                    ]
                },
            ),
            "entry_route": (
                "Either",
                "Admits applicants with an accredited bachelor's or M.S. degree in biology or equivalent preparation (minimum 3.0 overall and biology GPA).",
                "Applicants should have a bachelor's or M.S. degree from an accredited United States college or university or evidence of equivalent training at an accredited institution outside the United States.",
                bio_eeb,
            ),
            "toefl_min": (
                "80",
                "Department overrides the general 79 (4.5) UMSL Global guideline with a minimum TOEFL iBT score of 80 (550 PBT / 213 CBT); all incoming international students take a diagnostic English exam during orientation.",
                "Minimum TOEFL scores for admission are 550 (for paper-based test), 213 (for computer-based test), and 80 (for internet-based test),",
                bio_app,
            ),
        },
        also_fields=["environment"],
        notes="Ph.D. in Biology has three Bulletin emphases: Cell and Molecular Biology (CMB), Ecology, Evolution and Behavior (EEB; covers environment/ecology), and Integrative Biology. Note discrepancy between December 1 (department & GS doctoral page) and December 15 (profile PDF), and between department current stipend ($10,000/semester) and profile PDF ($8,000/term).",
        checked=CHECKED,
    )

    # 2. Chemistry Ph.D.
    chem_page = "https://www.umsl.edu/chemistry/degrees-and-programs/phd.html"
    chem_pdf = "https://www.umsl.edu/gradschool/gradprograms/profiles/doc/phd-chemistryprofile.pdf"
    chem_bul = "https://bulletin.umsl.edu/programs/chemistry-phd/"
    rec.save_program(
        UID,
        "chemistry",
        "Department of Chemistry and Biochemistry",
        chem_page,
        {
            "deadline": (
                "2027-02-21",
                "International Fall admission deadline is February 21 (Domestic Fall: July 1; International Spring: September 1; Domestic Spring: December 1).",
                "International Applicants: Fall - February 21",
                chem_pdf,
                {
                    "inferred": "year",
                    "also": [
                        {
                            "quote": "Chemistry Ph.D. | Application Deadlines | Domestic - Fall - July 1 | International - Fall - February 21",
                            "url": GS_DOC,
                        }
                    ],
                },
            ),
            "gre_general": (
                "Not required",
                "GRE General Test is not required for Chemistry Ph.D. admission, though scores may enhance the application.",
                "The GRE General Test is not required but may enhance your application.",
                chem_pdf,
            ),
            "gre_subject": NO_SUBJ,
            "supervisor": (
                "Not stated",
                "Chemistry Ph.D. department, Bulletin, and Graduate School profile pages do not state a pre-application supervisor requirement.",
                "",
                chem_page,
            ),
            "funding": (
                "Typical",
                "Graduate Assistantships for entering August/January Ph.D. students are currently funded at $21,000 per year plus a Graduate School tuition scholarship for graduate coursework (department webpage prints legacy 'in excess of $18,000'; support not normally beyond year 5).",
                "Graduate Assistantships, for those entering the Ph.D. program in either August or January, are presently funded $21,000. | A tuition scholarship for graduate coursework is provided by the Graduate School.",
                chem_pdf,
                {
                    "also": [
                        {
                            "quote": "Graduate Assistantships, for those entering the PhD program in either August or January, are presently in excess of $18,000.",
                            "url": chem_page,
                        },
                        {
                            "quote": "Teaching assistantships are available to qualified applicants. Research assistantships and fellowships are available for advanced students. Departmental support is not normally available beyond the fifth year in the program.",
                            "url": chem_bul,
                        },
                    ]
                },
            ),
            "entry_route": (
                "Either",
                "Requires at least a bachelor's degree with above-average chemistry, physics, and math background (minimum 3.0 GPA); applicants with bachelor's or master's degrees may enter (master's coursework reduces post-MS credit requirements).",
                "Applicants must have at least a baccalaureate degree with above-average performance in all areas of chemistry as well as physics and mathematics | Minimum GPA of 3.0 on 4.0 scale",
                chem_pdf,
                {
                    "also": [
                        {
                            "quote": "Individuals with at least the equivalent of the B.A. degree in the natural sciences may be admitted to the Graduate School as candidates for the M.S. degree or as precandidates for the Ph.D. degree in chemistry.",
                            "url": chem_bul,
                        }
                    ]
                },
            ),
        },
        notes="Ph.D. in Chemistry covers Biochemistry, Organic, Inorganic, and Physical Chemistry (60 credit hours minimum). International Fall deadline is Feb 21 vs July 1 for domestic applicants; Graduate School profile PDF states $21,000 GA stipend (vs legacy '$18,000' on department overview).",
        checked=CHECKED,
    )

    # 3. Computer Science Ph.D.
    cs_page = "https://www.umsl.edu/cmpsci/degrees-and-programs/graduate-studies/phd-cs.html"
    cs_asst = "https://www.umsl.edu/cmpsci/degrees-and-programs/graduate-studies/assistantships.html"
    cs_pdf = "https://www.umsl.edu/gradschool/gradprograms/profiles/doc/phd-mathcompprofile.pdf"
    rec.save_program(
        UID,
        "cs",
        "Department of Computer Science",
        cs_page,
        {
            "deadline": (
                "2027-02-01",
                "February 1 is the Fall funding-consideration priority deadline in the Graduate School directory/profile PDF (rolling general Fall deadline July 1; departmental GTA application deadline March 20; typical international visa cutoff May 31).",
                "Fall - July 1 (February 1, if requesting funding)",
                cs_pdf,
                {
                    "inferred": "year",
                    "also": [
                        {
                            "quote": "GTA applications are processed in the middle of a semester when/if a position is available for the following semester. Deadlines are March 20 for the fall and October 1 for the spring semester.",
                            "url": cs_asst,
                        },
                        {
                            "quote": "The department admits students for the Fall and Spring semesters on a rolling basis. For international students, the deadlines are determined by the visa processing times and usually are May 31 for the Fall semester and October 31 for the Spring semester.",
                            "url": cs_page,
                        },
                    ],
                },
            ),
            "gre_general": (
                "Not required",
                "GRE General Test is not required per Graduate School profile PDF (though department advises applicants—especially direct bachelor's entrants—to submit scores within 5 years).",
                "The GRE General Test is not required but may enhance your application.",
                cs_pdf,
                {
                    "also": [
                        {
                            "quote": "Applicants are advised to submit scores from the GRE general test, which are not more than 5 years old.",
                            "url": cs_page,
                        }
                    ]
                },
            ),
            "gre_subject": NO_SUBJ,
            "supervisor": (
                "Not required",
                "Advisor is selected after admission during Ph.D. candidacy Step B; pre-application faculty contact is only encouraged when seeking a faculty-funded GRA.",
                "The student finds a research direction/area and the appropriate advisor, constitutes a research committee, and then must do one of the following",
                cs_page,
                {
                    "also": [
                        {
                            "quote": "Students interested in GRA positions are also encouraged to review the research interests of our faculty, the list of current or past sponsored projects, the list of posted openings, and approach selected faculty directly.",
                            "url": cs_asst,
                        }
                    ]
                },
            ),
            "funding": (
                "Competitive",
                "Department offers a limited number of competitive GTA and faculty-funded GRA positions (easier to obtain after enrolling; separate GTA/GRA email application required by March 20 for Fall). GTA includes stipend plus full tuition remission for 9 graduate credits/semester.",
                "The department offers some assistantships, and individual faculty may offer research assistantships.",
                cs_page,
                {
                    "also": [
                        {
                            "quote": "Both assistantships are easier to get once in the program after establishing a relationship with the department (GTA), or with faculty (GRA). | Both assistantships come with a stipend and possible tuition reduction/remission. GTA includes full tuition remission of educational fees for 9 hours of graduate-level courses per semester",
                            "url": cs_asst,
                        }
                    ]
                },
            ),
            "entry_route": (
                "Either",
                "Applicants normally hold a Master's in CS or a related area (GPA >= 3.0), but exceptional bachelor's holders without a master's are also considered for direct Ph.D. admission.",
                "An applicant for admission to the Ph.D. in Mathematical and Computational Science - Computer Science option should have completed a Master's in Computer Science or a related area, with a GPA of at least 3.0/4.0. An applicant without a related Master's but with an exceptional record will also be considered for admission into the Ph.D. program.",
                cs_page,
            ),
        },
        notes="Degree title is Ph.D. in Mathematical and Computational Science — Computer Science Option (60 credit hours). Mathematics and Statistics emphases under the same degree stopped accepting applications in Fall 2021. Two letters of recommendation required. International applicants are automatically considered for UMSL Global tuition scholarships if not awarded an assistantship.",
        checked=CHECKED,
    )

    # 4. Psychological and Brain Sciences Ph.D. (neuro)
    neuro_page = "https://www.umsl.edu/sswpbs/psychological-sciences/graduate-programs/pbs/doctorate.html"
    neuro_pdf = "https://www.umsl.edu/gradschool/gradprograms/profiles/doc/phd-psychbnprofile.pdf"
    neuro_bul = "https://bulletin.umsl.edu/programs/psychology-phd-psychological-and-brain-sciences-emphasis/"
    rec.save_program(
        UID,
        "neuro",
        "Department of Psychological Sciences",
        neuro_page,
        {
            "deadline": (
                "2026-12-01",
                "Fall-only admission; all admission materials are due December 1.",
                "Fall Semester Only - The deadline for receipt of all admission materials is December 1 of each year for admission",
                neuro_pdf,
                {
                    "time_sensitive": "2026-12-01",
                    "also": [
                        {
                            "quote": "The Application Deadline for the Psychological and Brain Sciences Program is December 1.",
                            "url": neuro_bul,
                        }
                    ],
                },
            ),
            "gre_general": (
                "Not stated",
                "Psychological and Brain Sciences Ph.D. webpage, Bulletin entry, and Graduate School profile PDF do not state a GRE General requirement.",
                "",
                neuro_page,
            ),
            "gre_subject": (
                "Not stated",
                "Department webpages and profile PDF do not state whether the ETS GRE Psychology Subject Test is required, optional, or not required.",
                "",
                neuro_page,
            ),
            "supervisor": (
                "Recommended",
                "Uses a mentorship/apprenticeship model where each student works continuously with a faculty member, and the personal statement requires naming which faculty member(s) you would like to work with and why.",
                "It also has an apprenticeship model in which each student works closely and continuously with a faculty member within the realm of the faculty member's research interests. | Describe your interest in the biological basis of behavior, any prior research experience, your career goals, and which faculty member(s) you would like to work with and why",
                neuro_page,
            ),
            "funding": (
                "Typical",
                "Ph.D. students receive a Graduate Teaching Assistantship ($21,000/year stipend plus tuition remission up to $28,872/year) in Years 1 and 2; funding in later years is not guaranteed and may come from grants or teaching.",
                "Students in the Ph.D. program receive a Graduate Teaching Assistantship ($21,000/year stipend + tuition remission) in their first and second year. Funding in later years is not guaranteed, but could come from grant funding and/or teaching courses.",
                neuro_page,
            ),
            "entry_route": (
                "Either",
                "Requires at least a bachelor's degree before enrollment (minimum 3.0 overall GPA, 3.2 in psychology courses, and >= 12 undergraduate psychology/neuroscience credits); up to 30 prior graduate credit hours may transfer toward the 60-credit Ph.D.",
                "Successful applicants must have completed at least a baccalaureate degree before beginning the program.",
                neuro_page,
                {
                    "also": [
                        {
                            "quote": "A minimum of 60 credit hours are required for the degree program. A maximum of 30 hours credit may be transferred.",
                            "url": neuro_pdf,
                        }
                    ]
                },
            ),
        },
        notes="Ph.D. in Psychology — Psychological and Brain Sciences (CIP 42.2799, STEM OPT eligible; biological basis of behavior, psychophysiology, psychopharmacology, neuroendocrinology, cognitive neuroscience, neuropsychology). UMSL's Clinical Community Psychology Ph.D. is excluded as clinical practice, and Industrial/Organizational Psychology Ph.D. is suspended.",
        checked=CHECKED,
    )

    print("Staged umsl + 4 programs successfully.")


if __name__ == "__main__":
    main()
