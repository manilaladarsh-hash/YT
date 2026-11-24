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
UID = "cuhk"

GS_REQ = "https://www.gs.cuhk.edu.hk/admissions/admissions/requirements"
GS_DOCS = "https://www.gs.cuhk.edu.hk/admissions/admissions/documents-required"
GS_FAQ = "https://www.gs.cuhk.edu.hk/admissions/faqs"
GS_FEES = "https://www.gs.cuhk.edu.hk/admissions/scholarships-fees/fees"
GS_PGS = "https://www.gs.cuhk.edu.hk/admissions/scholarships-fees/studentships"
GS_OPT = "https://www.gs.cuhk.edu.hk/programmes/study-options"
ETS_SUBJ = "https://www.ets.org/gre/score-users/about/subject-tests.html"

NO_SUBJ = (
    "No subject test",
    "ETS offers GRE Subject Tests only in Mathematics, Physics, and Psychology (none in this field).",
    "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study",
    ETS_SUBJ,
)

GS_FUNDING = (
    "Typical",
    "Qualified full-time research postgraduate students receive Postgraduate Studentships (HK$229,200/yr, approx. HK$19,100/mo or US$29,400/yr in 2026-27) during the normative study period; HKPFS provides HK$28,700/mo plus HK$14,400/yr travel allowance and CUHK tuition waiver.",
    "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
    GS_PGS,
)

GS_ENTRY = (
    "Either",
    "Articulated MPhil-PhD programme admits both bachelor's holders (direct to pre-candidacy PhD or MPhil stream) and master's holders.",
    "Articulated MPhil-PhD programmes provide a pathway for students with a Bachelor's degree to pursue a PhD. Initially, students are admitted as either MPhil students or pre-candidacy PhD students.",
    GS_OPT,
)


def main():
    by_url = {}
    for p in CACHE.glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        by_url[d["url"]] = d["text"]

    # Check unicode punctuation on uncertain lines before saving
    def pick(url, *candidates):
        txt = by_url[url]
        for c in candidates:
            if c in txt:
                return c
        raise ValueError(f"None matched in {url}:\n{candidates}")

    rec.save_university(
        UID,
        "The Chinese University of Hong Kong",
        "Hong Kong",
        "Hong Kong",
        GS_REQ,
        {
            "app_fee": (
                "500 HKD",
                "Non-refundable, non-transferable application fee of HK$500 per programme.",
                "The application fee is HK$500 per programme (except for MBA, MBA in Finance and MSc in Finance).",
                GS_FAQ,
                {
                    "also": [
                        {
                            "quote": "All fees, once paid, are non-refundable and non-transferable under any circumstances.",
                            "url": GS_FEES,
                        }
                    ]
                },
            ),
            "fee_waiver": (
                "Not stated",
                "CUHK Graduate School fees page lists the HK$500 non-refundable application fee and does not state an application fee waiver policy.",
                "",
                GS_FEES,
            ),
            "gre_general": (
                "Not stated",
                "CUHK Graduate School general admissions requirements do not state a university-wide GRE General requirement for PhD programmes (individual Graduate Divisions may recommend or require GRE; see ECE).",
                "",
                GS_REQ,
            ),
            "toefl_min": (
                "4.5 (new scale)",
                "Minimum TOEFL iBT score is 4.5 of 6 on the new scale (or 79 of 120 on the 0-120 scale; Home Edition accepted; single-attempt scores only, MyBest Scores not accepted).",
                "TOEFL: 79 of 120 / 4.5 of 6 (Internet-based/Home Edition);",
                GS_REQ,
                {
                    "also": [
                        {
                            "quote": "No, we only accept the test result from each individual attempt.",
                            "url": GS_FAQ,
                        }
                    ]
                },
            ),
            "ielts_min": (
                "6.5",
                "Minimum IELTS Academic score is 6.5 (Test Centre based or Online; single-attempt scores only, One Skill Retake not accepted).",
                "IELTS (Academic): 6.5 (Test Centre based/Online);",
                GS_REQ,
            ),
            "english_waiver": (
                "Conditional",
                "English proficiency test is waived for applicants who obtained a degree from a university in Hong Kong or completed a degree programme whose medium of instruction was English (requires certifying letter from the university Registry).",
                "obtained a Degree from a university in Hong Kong1 or taken a degree programme of which the medium of instruction was English;",
                GS_REQ,
                {
                    "also": [
                        {
                            "quote": "A certifying letter issued by the Registry of the university confirming the medium of instruction of your degree programme was English",
                            "url": GS_DOCS,
                        }
                    ]
                },
            ),
        },
        notes=(
            "CUHK offers articulated MPhil-PhD programmes across 16 covered STEM fields (no Civil Engineering or Chemical Engineering PhD is offered; "
            "Faculty of Engineering consists of 6 departments: Biomedical Engineering, Computer Science & Engineering, Electronic Engineering, Information Engineering, Mechanical & Automation Engineering, and Systems Engineering & Engineering Management). "
            "General Regulations allow individual Graduate Divisions to set additional test requirements (Electronic Engineering highly recommends GRE General for non-Hong Kong graduates). "
            "Application fee is HK$500 per programme (non-refundable); TOEFL MyBest Scores and IELTS One Skill Retake are not accepted. "
            "Tuition is HK$49,500/yr for 2027-28 (waived for eligible local full-time research postgraduate students and HKPFS awardees); standard Postgraduate Studentship is HK$229,200/yr (~HK$19,100/mo) in 2026-27, rising to HK$28,700/mo under HKPFS."
        ),
        checked=CHECKED,
    )

    programs = [
        (
            "cs",
            "Faculty of Engineering — Department of Computer Science and Engineering",
            "https://www.cse.cuhk.edu.hk/admission/mphil-phd/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-computer-science-and-engineering",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Not stated",
                    "Department MPhil-PhD admission page does not state a pre-application supervisor contact requirement.",
                    "",
                    "https://www.cse.cuhk.edu.hk/admission/mphil-phd/",
                ),
                "funding": (
                    "Guaranteed",
                    "All full-time research students receive Postgraduate Studentships (HK$229,200/yr in 2026-27, approx. HK$19,100/mo) during their normative study period.",
                    "All full-time research students will receive Studentships during their normative study period.",
                    "https://www.cse.cuhk.edu.hk/admission/mphil-phd/",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": GS_ENTRY,
            },
            "CSE also runs an online pre-application review portal (dept-eappsrv.cse.cuhk.edu.hk/pgas2027/). Companion Department of Information Engineering (ie.cuhk.edu.hk) also supervises PhD research in networking, communications, cybersecurity, information theory, and AI.",
        ),
        (
            "datasci",
            "Faculty of Engineering — Department of Systems Engineering and Engineering Management",
            "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/qualifications-for-admission/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-systems-engineering-and-engineering-management",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Not stated",
                    "Department qualifications page does not state a pre-application supervisor contact requirement.",
                    "",
                    "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/qualifications-for-admission/",
                ),
                "funding": (
                    "Guaranteed",
                    "All full-time MPhil and PhD students receive financial support (HK$19,100/month Postgraduate Studentship for regular students, HK$28,700/month under HKPFS).",
                    pick(
                        "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/m-phil-ph-d-programme-finanical-aid/",
                        "All full-time M.Phil. and Ph.D. students receive fnancial support. | HK$19,100",
                        "All full-time M.Phil. and Ph.D. students receive fnancial support.",
                    ),
                    "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/m-phil-ph-d-programme-finanical-aid/",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": (
                    "Either",
                    "Admits master's holders as well as exceptional candidates with a bachelor's degree directly to the PhD programme (or MPhil-PhD articulated stream).",
                    "Exceptional candidates with a bachelor degree may apply directly to the Ph.D. Programme.",
                    "https://www.se.cuhk.edu.hk/programmes/postgraduate-programmes/research-postgraduate-programmes/qualifications-for-admission/",
                ),
            },
            "SEEM covers operations research, data analytics, AI/machine learning, financial engineering, and systems engineering. Note verbatim source spelling 'fnancial' on the SEEM financial aid page. Related data science and AI PhD training is also offered by the Department of Statistics and Data Science (statistics), CSE (cs), and Information Engineering.",
        ),
        (
            "ece",
            "Faculty of Engineering — Department of Electronic Engineering",
            "https://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/admission",
            {
                "gre_general": (
                    "Recommended",
                    "GRE General Test is highly recommended (but not compulsory) by the Division Head for non-Hong Kong university graduates.",
                    "For non-Hong Kong university graduates, Graduate Record Examination (GRE) General Test is highly recommended by the Division Head",
                    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-electronic-engineering",
                    {
                        "also": [
                            {
                                "quote": "GRE is highly recommended, but not compulsory.",
                                "url": "https://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/faq",
                            }
                        ]
                    },
                ),
                "deadline": (
                    "2026-12-01",
                    "Main Round application deadline for 2027-28 entry is December 1, 2026 (applicants seeking early December interview consideration are encouraged to submit by November 2, 2026; Clearing Round: March 31, 2027).",
                    "The main round admission will close on 1 December 2026.",
                    "https://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/admission",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Recommended",
                    "Applicants are advised to contact professors in their research interest area before submitting an application.",
                    "Applicants are advised to contact the professors that fall into your research interest first before you submit the application.",
                    "https://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/admission",
                ),
                "funding": (
                    "Typical",
                    "Subject to satisfactory academic performance and research progress, postgraduate studentships (HK$19,100 - HK$19,660/month in FAQ; HK$229,200/yr in GS schedule) are provided throughout the normative period.",
                    "Subject to satisfactory academic performance and research progress, postgraduate studentships will be provided to students throughout their normative period.",
                    "https://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/admission",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": (
                    "Either",
                    "Eligible to apply for PhD studies with a bachelor's degree even without holding a research-based master's degree, or with a master's degree.",
                    "Applicants are eligible to apply for PhD studies even without holding a research-based master's degree.",
                    "https://www.ee.cuhk.edu.hk/en-gb/curriculum/mphil-phd-programme/admission",
                ),
            },
            "Department of Electronic Engineering (EE) highlights a November 2, 2026 priority target for early December interviews alongside the December 1, 2026 Main Round deadline. Studentship continuation requires passing the qualifying/screening test within 9 months.",
        ),
        (
            "mech",
            "Faculty of Engineering — Department of Mechanical and Automation Engineering",
            "https://www4.mae.cuhk.edu.hk/research-postgraduate-programme/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-mechanical-and-automation-engineering",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Not stated",
                    "MAE research postgraduate admission page does not state a pre-application supervisor contact requirement.",
                    "",
                    "https://www4.mae.cuhk.edu.hk/research-postgraduate-programme/",
                ),
                "funding": (
                    "Typical",
                    "Financial support (Postgraduate Studentships of HK$229,200/yr in 2026-27, approx. HK$19,100/mo, or HKPFS HK$28,700/mo) is available to successful applicants.",
                    "Financial supports are available to successful applicants.",
                    "https://www4.mae.cuhk.edu.hk/research-postgraduate-programme/",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": GS_ENTRY,
            },
            "Department of Mechanical and Automation Engineering covers robotics, control, precision engineering, energy/thermofluids, and design & manufacturing.",
        ),
        (
            "bme",
            "Faculty of Engineering — Department of Biomedical Engineering",
            "https://www.bme.cuhk.edu.hk/new/mphil-phd.php",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/engineering/mphil-phd-biomedical-engineering",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Not stated",
                    "BME MPhil-PhD programme page does not state a pre-application supervisor contact requirement.",
                    "",
                    "https://www.bme.cuhk.edu.hk/new/mphil-phd.php",
                ),
                "funding": (
                    "Typical",
                    "Regular MPhil-PhD students receive HK$19,100 - HK$19,660 per month (HKPFS awardees receive HK$28,700 per month plus tuition waiver).",
                    "Financial Assistance | Regular MPhil-PhD students: HK$19,100 - HK$19,660 per month",
                    "https://www.bme.cuhk.edu.hk/new/mphil-phd.php",
                ),
                "entry_route": GS_ENTRY,
            },
            "Department of Biomedical Engineering spans medical imaging, biomaterials, biomechanics, neural engineering, and point-of-care diagnostics.",
        ),
        (
            "materials",
            "Faculty of Science — Division of Materials Science and Engineering (Department of Physics)",
            "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-materials-science-engineering/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027).",
                    "CUHK Application Deadline: 1 December 2026 (Main round) and 31 March 2027 (Clearing round)",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-materials-science-engineering/",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": (
                    "Optional",
                    "GRE Subject Test score (in Physics, Chemistry, or Mathematics) is listed as optional on the Division admissions page (note ETS discontinued the Chemistry Subject Test in May 2023).",
                    "[Optional] Provide Graduate Record Examination (GRE) Subject Test Score",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-materials-science-engineering/",
                ),
                "supervisor": (
                    "Recommended",
                    "Potential applicants are encouraged to contact individual professors before making selections to discuss research fit and openings.",
                    "Before making selections, potential applicants are encouraged to contact the individual professors to find out more about their research, their group and what kind of students they are looking for.",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-materials-science-engineering/",
                ),
                "funding": (
                    "Typical",
                    "Regular students receive HK$19,100 - HK$19,660 per month with no separate application required (HKPFS awardees receive HK$28,700/month).",
                    "Fee and Financial Support | Regular students: HKD19,100-19,660 per month (separate application is not required)",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-materials-science-engineering/",
                ),
                "entry_route": GS_ENTRY,
            },
            "Administered by the Graduate Division of Materials Science and Engineering hosted in the Department of Physics; shortlisted PhD applicants are invited to an entrance exam/interview in December or February.",
        ),
        (
            "physics",
            "Faculty of Science — Department of Physics",
            "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027).",
                    "CUHK Application Deadlines: 1 December 2026 (Main round) and 31 March 2027 (Clearing round)",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": (
                    "Optional",
                    "GRE Subject Test score (Physics, Chemistry, or Mathematics) is optional.",
                    "[Optional] Provide Graduate Record Examination (GRE) Subject Test Score",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                ),
                "supervisor": (
                    "Recommended",
                    "Potential applicants are encouraged to contact individual professors before making selections to learn about research groups and openings.",
                    "Before making selections, potential applicants are encouraged to contact the individual professors to find out more about their research, their group and what kind of students they are looking for.",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                ),
                "funding": (
                    "Typical",
                    "Regular students receive HK$19,100 - HK$19,660 per month with no separate application required.",
                    "Fee and Financial Support | Regular students: HKD19,100-19,660 per month (separate application is not required)",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                ),
                "entry_route": GS_ENTRY,
            },
            "Shortlisted PhD applicants take a Physics entrance examination and interview (around December 2026 for Main Round / February 2027).",
        ),
        (
            "astronomy",
            "Faculty of Science — Department of Physics (Astrophysics and Fundamental Physics)",
            "https://app.phy.cuhk.edu.hk/research-areas/astrophysics-fundamental-physics/",
            {
                "deadline": (
                    "2026-12-01",
                    "Admitted through the Department of Physics MPhil-PhD programme: Main Round and HKPFS deadline is December 1, 2026 (Clearing Round: March 31, 2027).",
                    "CUHK Application Deadlines: 1 December 2026 (Main round) and 31 March 2027 (Clearing round)",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": (
                    "Optional",
                    "GRE Subject Test score (Physics, Chemistry, or Mathematics) is optional.",
                    "[Optional] Provide Graduate Record Examination (GRE) Subject Test Score",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                ),
                "supervisor": (
                    "Recommended",
                    "Potential applicants are encouraged to contact individual Physics/Astrophysics faculty before applying.",
                    "Before making selections, potential applicants are encouraged to contact the individual professors to find out more about their research, their group and what kind of students they are looking for.",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                ),
                "funding": (
                    "Typical",
                    "Regular students receive HK$19,100 - HK$19,660 per month with no separate application required.",
                    "Fee and Financial Support | Regular students: HKD19,100-19,660 per month (separate application is not required)",
                    "https://app.phy.cuhk.edu.hk/postgraduate-admissions/mphil-phd-in-physics/",
                ),
                "entry_route": GS_ENTRY,
            },
            "Astrophysics and Fundamental Physics research group in the Department of Physics (cosmology, gravitational waves, high-energy astrophysics, particle physics).",
        ),
        (
            "math",
            "Faculty of Science — Department of Mathematics",
            "https://www.math.cuhk.edu.hk/postgraduates/research-programmes",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 per CUHK Graduate School (Clearing Round: March 31, 2027).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-mathematics",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": (
                    "Optional",
                    "GRE Subject Test in Mathematics is not universally required but may be required in some cases.",
                    "Graduate Record Examination in Mathematics may also be required in some cases.",
                    "https://www.math.cuhk.edu.hk/postgraduates/research-programmes",
                ),
                "supervisor": (
                    "Recommended",
                    "Prospective applicants are advised to approach professors early to discuss research fields; the Accelerated MPhil-PhD option directly after a bachelor's degree requires a prospective supervisor's recommendation.",
                    "Non-final-year undergraduates aiming for graduate studies in Mathematics are advised to approach professors early to discuss their proposed fields of research and expectations in graduate school.",
                    "https://www.math.cuhk.edu.hk/postgraduates/admission",
                    {
                        "also": [
                            {
                                "quote": "Since 2004, qualified undergraduate degree holders and MPhil students may opt for our Accelerated MPhil-PhD degree programme to study for a PhD directly. It is more demanding on the student and requires a recommendation from the prospective supervisor apart from typical application procedures.",
                                "url": "https://www.math.cuhk.edu.hk/postgraduates/research-programmes",
                            }
                        ]
                    },
                ),
                "funding": (
                    "Typical",
                    "Financial aid (CUHK Postgraduate Studentships of HK$229,200/yr in 2026-27) is available to qualified full-time research postgraduate students.",
                    "Funding Nature Financial aid available",
                    "https://www.math.cuhk.edu.hk/postgraduates/research-programmes",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": (
                    "Either",
                    "Admits both qualified undergraduate degree holders (via Accelerated MPhil-PhD with supervisor recommendation or MPhil stream) and MPhil/master's holders.",
                    "Since 2004, qualified undergraduate degree holders and MPhil students may opt for our Accelerated MPhil-PhD degree programme to study for a PhD directly.",
                    "https://www.math.cuhk.edu.hk/postgraduates/research-programmes",
                ),
            },
            "Department's own /postgraduates/research-programmes page still displays the prior year's 2025 deadline; Graduate School lists Main Round: 1 December 2026 for 2027-28 entry.",
        ),
        (
            "statistics",
            "Faculty of Science — Department of Statistics and Data Science",
            "https://www.sta.cuhk.edu.hk/programmes/m-phil-ph-d-in-statistics/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for August 2027 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "For applicants who apply for M.Phil./Ph.D. programme directly with CUHK (i.e. non-HKPFS applicants), the application deadline for Main Round is 1 December 2026, and that for Clearing Round is 31 March 2027",
                    "https://www.sta.cuhk.edu.hk/programmes/m-phil-ph-d-in-statistics/",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Recommended",
                    "Department notes that indicating a preference for a prospective advisor increases admission odds.",
                    "Please note that indication of the preference for your future advisor will increase your odds to get admitted to our PhD/MPhil in Statistics program",
                    "https://www.sta.cuhk.edu.hk/programmes/m-phil-ph-d-in-statistics/",
                ),
                "funding": GS_FUNDING,
                "entry_route": GS_ENTRY,
            },
            "Department of Statistics and Data Science offers research specializations across mathematical statistics, biostatistics, financial statistics, data science, and machine learning.",
        ),
        (
            "chemistry",
            "Faculty of Science — Department of Chemistry",
            "https://chem.cuhk.edu.hk/postgraduate/mphil-phd/",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-chemistry",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Not stated",
                    "Department MPhil-PhD page does not state a pre-application supervisor contact requirement.",
                    "",
                    "https://chem.cuhk.edu.hk/postgraduate/mphil-phd/",
                ),
                "funding": GS_FUNDING,
                "entry_route": GS_ENTRY,
            },
            "Department of Chemistry covers analytical, inorganic, organic, physical, computational, and materials/biological chemistry.",
        ),
        (
            "biology",
            "Faculty of Science — School of Life Sciences (Biology)",
            "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-biology",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-biology",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Recommended",
                    "Applicants are advised to contact a prospective advisor to discuss their research area before submitting an application.",
                    "Applicants are advised to contact a prospective advisor to discuss their area of interest before submitting an application.",
                    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-biology",
                ),
                "funding": GS_FUNDING,
                "entry_route": GS_ENTRY,
            },
            "School of Life Sciences also administers companion articulated MPhil-PhD divisions in Biochemistry, Cell & Molecular Biology, Molecular Biotechnology, and Food & Nutritional Sciences (same December 1, 2026 Main Round deadline and advisor-contact recommendation).",
        ),
        (
            "environment",
            "Faculty of Science — School of Life Sciences (Environmental Science)",
            "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-environmental-science",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027, subject to availability).",
                    "Main Round: 1 December 2026",
                    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-environmental-science",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Recommended",
                    "Applicants are advised to contact a prospective advisor to discuss their research area before submitting an application.",
                    "Applicants are advised to contact a prospective advisor to discuss their area of interest before submitting an application.",
                    "https://www.gs.cuhk.edu.hk/programmes/science/mphil-phd-environmental-science",
                ),
                "funding": GS_FUNDING,
                "entry_route": GS_ENTRY,
            },
            "Related environmental PhD research at CUHK is also conducted in the Department of Earth and Environmental Sciences (earth), Department of Geography and Resource Management, and the inter-faculty Earth System and GeoInformation Science (ESGS) division.",
        ),
        (
            "earth",
            "Faculty of Science — Department of Earth and Environmental Sciences",
            "https://www.ees.cuhk.edu.hk/programme/postgraduate-programmes/postgraduate-programme/",
            {
                "deadline": (
                    "2027-01-31",
                    "Direct regular CUHK admission deadline for MPhil and PhD programmes is January 31, 2027 (HKPFS deadline is December 1, 2026; departmental review begins around December 2, 2026).",
                    "31 January 2027 (For applicants who apply for MPhil programme and PhD programme directly with CUHK).",
                    "https://www.ees.cuhk.edu.hk/programme/postgraduate-programmes/postgraduate-programme/",
                    {"time_sensitive": "2027-01-31"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Not stated",
                    "EES postgraduate admission page does not state a pre-application supervisor contact requirement.",
                    "",
                    "https://www.ees.cuhk.edu.hk/programme/postgraduate-programmes/postgraduate-programme/",
                ),
                "funding": (
                    "Typical",
                    "Postgraduate studentship for MPhil-PhD students is HK$19,100/month (HK$229,200/yr in GS schedule; applications submitted after January 31, 2027 may not be considered for financial support).",
                    "Applications submitted after 31 January 2027 may not be considered for financial support.",
                    "https://www.ees.cuhk.edu.hk/programme/postgraduate-programmes/postgraduate-programme/",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": GS_ENTRY,
            },
            "Department of Earth and Environmental Sciences (formerly Earth System Science) sets a January 31, 2027 regular CUHK deadline while starting review around December 2, 2026 and maintaining December 1, 2026 for HKPFS.",
        ),
        (
            "biomed",
            "Faculty of Medicine — School of Biomedical Sciences",
            "https://www3.sbs.cuhk.edu.hk/en/admission/",
            {
                "deadline": (
                    "2026-12-01",
                    "Regular non-HKPFS application and supporting document deadline for the Articulated MPhil-PhD Programme in Biomedical Sciences is December 1, 2026 (HKPFS deadline is also December 1, 2026).",
                    "For applicants applying via regular admission to the Articulated MPhil-PhD Programme in Biomedical Sciences on the CUHK Online Application System (i.e. non-HKPFS applicants), please note that the deadline for both the application and the submission of required documents is 1 December 2026.",
                    "https://www3.sbs.cuhk.edu.hk/en/admission/",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": NO_SUBJ,
                "supervisor": (
                    "Recommended",
                    "Applicants are highly advised to contact a potential supervisor/PI to secure research support before or during the application process.",
                    "You are highly advised to contact your potential supervisor/PI to secure their support for your research study before or during your application process.",
                    "https://www3.sbs.cuhk.edu.hk/en/admission/",
                ),
                "funding": (
                    "Typical",
                    "CUHK offers Postgraduate Studentships (HK$19,100/month in 2026-27, approx. US$2,450/month) for up to 2 years (MPhil) and up to 4 years (PhD) during the normative period of study.",
                    "CUHK offers Postgraduate Studentships (PGS) for up to 2 years to all full-time MPhil students and for up to 4 years to all full-time PhD students. The annual studentship for 2026-27 is HK$19,100 (approx. US$2,450) per month, payable during the normative period of study.",
                    "https://www3.sbs.cuhk.edu.hk/en/admission/",
                ),
                "entry_route": (
                    "Either",
                    "Articulated MPhil-PhD programme admits Bachelor's holders (preferably Second Upper Honours or above in biomedical or life sciences) as well as Master's holders.",
                    "In addition to the general requirements of the Graduate School, applicants should preferably hold a Bachelor's degree with honours (preferably with Second Upper Honours or above) in a field related to biomedical or life sciences.",
                    "https://www.gs.cuhk.edu.hk/programmes/medicine/mphil-phd-biomedical-sciences",
                ),
            },
            "Faculty of Medicine also offers PhD programmes in Medical Sciences, Microbiology, Pharmacy, Translational Genomics, and Public Health.",
        ),
        (
            "neuro",
            "Faculty of Social Science — Department of Psychology (Neuropsychology and Cognition)",
            "https://www.psy.cuhk.edu.hk/en/graduate/m-phil-ph-d-in-psychology.html",
            {
                "deadline": (
                    "2026-12-01",
                    "Main Round and HKPFS application deadline for 2027-28 entry is December 1, 2026 (Clearing Round: March 31, 2027).",
                    "Main Round: Dec 1, 2026",
                    "https://www.psy.cuhk.edu.hk/en/graduate/application-period.html",
                    {"time_sensitive": "2026-12-01"},
                ),
                "gre_subject": (
                    "Not stated",
                    "Department of Psychology and CUHK Graduate School programme pages do not state a GRE Subject Test in Psychology requirement.",
                    "",
                    "https://www.psy.cuhk.edu.hk/en/graduate/m-phil-ph-d-in-psychology.html",
                ),
                "supervisor": (
                    "Recommended",
                    "Applicants must clearly indicate their potential supervisor in the heading of their personal statement.",
                    "Remarks: Please clearly indicate the potential supervisor in the heading of a statement.",
                    "https://www.gs.cuhk.edu.hk/programmes/social-science/mphil-phd-psychology",
                ),
                "funding": (
                    "Guaranteed",
                    "All full-time MPhil and PhD students receive studentships (HK$229,200/yr standard GS rate in 2026-27) provided they remain in good academic standing.",
                    "All our full-time M.Phil. and Ph.D. students receive some form of studentships, as long as they are in good academic standing.",
                    "https://www.psy.cuhk.edu.hk/en/graduate/admission-faqs.html",
                    {
                        "also": [
                            {
                                "quote": "Annual studentship for 2026-27 is HK$229,200 (approx. US$29,400). Payable during the normative period of study.",
                                "url": GS_PGS,
                            }
                        ]
                    },
                ),
                "entry_route": (
                    "Either",
                    "Articulated MPhil-PhD programme admits applicants holding a Bachelor's degree in Psychology or a related field as well as Master's holders.",
                    "possess a Bachelor's degree in Psychology or in a related field;",
                    "https://www.gs.cuhk.edu.hk/programmes/social-science/mphil-phd-psychology",
                ),
            },
            "Department of Psychology covers Neuropsychology and Cognition alongside Developmental, Health/Clinical, and Social Psychology. Neuroscience PhD research is also conducted in the School of Biomedical Sciences (Neural, Vascular, and Metabolic Biology theme, under biomed) and Department of Medicine & Therapeutics (PhD in Medical Sciences).",
        ),
    ]

    for field, dept, page, fields, notes in programs:
        rec.save_program(UID, field, dept, page, fields, notes=notes, checked=CHECKED)
    print(f"Wrote 1 university + {len(programs)} programs for {UID} to {rec.OUT}")


if __name__ == "__main__":
    main()
