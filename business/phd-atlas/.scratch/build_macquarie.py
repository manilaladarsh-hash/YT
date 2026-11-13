import json
from pathlib import Path

staging_unis = Path("data/staging/universities")
staging_progs = Path("data/staging/programs")
staging_unis.mkdir(parents=True, exist_ok=True)
staging_progs.mkdir(parents=True, exist_ok=True)

# Central Macquarie Record
macquarie_uni = {
    "id": "macquarie",
    "institution": "Macquarie University",
    "country": "Australia",
    "region": "New South Wales",
    "grad_page": "https://www.mq.edu.au/research/phd-and-research-degrees",
    "checked": "2026-10-30",
    "fields": {
        "app_fee": {
            "code": "Not stated",
            "value": "The Graduate Research Admissions Policy states the university may charge an application fee, but specifies no fee amount for research degree applications.",
            "quote": "(17) The University may charge an application fee.",
            "url": "https://policies.mq.edu.au/document/view.php?id=369"
        },
        "fee_waiver": {
            "code": "Not stated",
            "value": "No fee amount is specified for research applications, and no fee waiver provision is stated.",
            "quote": "",
            "url": "https://policies.mq.edu.au/document/view.php?id=369"
        },
        "gre_general": {
            "code": "Not stated",
            "value": "No GRE requirement is stated in Macquarie University graduate research admission policies.",
            "quote": "",
            "url": "https://policies.mq.edu.au/document/view.php?id=369"
        },
        "toefl_min": {
            "code": "86",
            "value": "Schedule 1 sets TOEFL iBT minimum score of 86 overall (18 reading, 21 writing, 17 listening, 21 speaking) for most Graduate Research courses.",
            "quote": "Competent English 86 18 21 17 21 Most Graduate Research courses",
            "url": "https://policies.mq.edu.au/download.php?id=759&version=9&associated"
        },
        "ielts_min": {
            "code": "6.5",
            "value": "Schedule 1 sets IELTS Academic minimum score of 6.5 overall (minimum 6.0 in all bands) for most Graduate Research courses.",
            "quote": "Competent English 6.5 6.0 6.0 6.0 6.0 Most Graduate Research courses",
            "url": "https://policies.mq.edu.au/download.php?id=759&version=9&associated"
        },
        "english_waiver": {
            "code": "Conditional",
            "value": "Macquarie accepts prior study in specified English-speaking countries (Australia, Canada, New Zealand, South Africa, Ireland, UK, USA) or postgraduate study taught in English from 13 listed countries (not including India).",
            "quote": "Section 2: Study undertaken in specified English-speaking countries\nThe University may accept as meeting English proficiency requirements:",
            "url": "https://policies.mq.edu.au/download.php?id=759&version=9&associated"
        }
    },
    "notes": "Macquarie University admits doctoral candidates under the centralized Graduate Research Admissions Policy. Minimum degree requirements and English language standards are governed centrally by the Graduate Research Academy and Academic Senate."
}

with open(staging_unis / "macquarie.json", "w", encoding="utf-8") as f:
    json.dump(macquarie_uni, f, indent=2, ensure_ascii=False)
    f.write("\n")

# Programs
departments = {
    "cs": ("School of Computing", []),
    "ece": ("School of Engineering", []),
    "mech": ("School of Engineering", []),
    "civil": ("School of Engineering", []),
    "bme": ("School of Engineering", []),
    "math": ("School of Mathematical and Physical Sciences", []),
    "physics": ("School of Mathematical and Physical Sciences", []),
    "astronomy": ("School of Mathematical and Physical Sciences / Australian Astronomical Optics", []),
    "chemistry": ("School of Natural Sciences", []),
    "biology": ("School of Natural Sciences", []),
    "earth": ("School of Natural Sciences", []),
    "environment": ("School of Natural Sciences", []),
}

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
prog_url = "https://www.mq.edu.au/research/phd-and-research-degrees/explore-research-degrees/doctor-of-philosophy"
apply_url = "https://www.mq.edu.au/research/phd-and-research-degrees/how-to-apply"
schol_url = "https://www.mq.edu.au/research/phd-and-research-degrees/how-to-apply/scholarship-opportunities"

for field, (dept, also_fields) in departments.items():
    if field in ("math", "physics"):
        gre_sub = {
            "code": "Not stated",
            "value": "No GRE Subject test is required or mentioned for research degree admission.",
            "quote": "",
            "url": prog_url
        }
    else:
        gre_sub = {
            "code": "No subject test",
            "value": "No GRE Subject Test exists for this field; ETS offers Subject Tests only in Mathematics, Physics and Psychology.",
            "quote": ets_quote,
            "url": ets_url
        }

    prog_data = {
        "id": f"macquarie--{field}",
        "university": "macquarie",
        "field": field,
        "also_fields": also_fields,
        "department": dept,
        "program_page": prog_url,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "2026-10-31",
                "value": "Session 1 International Road to Research Scholarship applications close on 31 October 2026.",
                "quote": "International Road to Research Scholarship Monday 15 June 2026 Saturday 31 October 2026",
                "url": schol_url,
                "also": [
                    {
                        "quote": "International Research Scholarship Round Monday 15 June 2026 Friday 31 July 2026",
                        "url": schol_url
                    }
                ]
            },
            "entry_route": {
                "code": "Master's usually required",
                "value": "Admission requires a Master of Research (MRes) with at least 75% in the second year, an MPhil, or a 2-year master's degree with a major research component at Distinction level (75% or greater).",
                "quote": "In addition, you’ll need to meet one of the following requirements: a Master of Research (MRes) with at least 75 per cent in second year a Master of Philosophy a two-year master's degree with a major research component at Distinction level (75 per cent or greater).",
                "url": prog_url
            },
            "supervisor": {
                "code": "Required",
                "value": "Applicants must find a supervisor and work with them to develop a research proposal prior to applying.",
                "quote": "work with your proposed supervisor to develop a research proposal",
                "url": apply_url
            },
            "funding": {
                "code": "Competitive",
                "value": "PhD candidates may be awarded competitive scholarships providing a tuition fee offset, living allowance stipend ($40,900 per annum in 2027), and OSHC.",
                "quote": "PhD students may be eligible for scholarships that provide financial support during their three years of research, including a stipend valued at $40,900 per annum in 2027, indexed annually.",
                "url": prog_url
            },
            "toefl_min": {
                "code": "86",
                "value": "Schedule 1 requires TOEFL iBT 86 overall (18 reading, 21 writing, 17 listening, 21 speaking) for most Graduate Research courses.",
                "quote": "Competent English 86 18 21 17 21 Most Graduate Research courses",
                "url": "https://policies.mq.edu.au/download.php?id=759&version=9&associated"
            },
            "ielts_min": {
                "code": "6.5",
                "value": "Schedule 1 requires IELTS Academic 6.5 overall with minimum 6.0 in each band for most Graduate Research courses.",
                "quote": "Competent English 6.5 6.0 6.0 6.0 6.0 Most Graduate Research courses",
                "url": "https://policies.mq.edu.au/download.php?id=759&version=9&associated"
            },
            "gre_subject": gre_sub
        },
        "notes": f"Macquarie University offers the Doctor of Philosophy in {dept} under centralized Graduate Research Academy admissions."
    }

    with open(staging_progs / f"macquarie--{field}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Generated macquarie and {len(departments)} programs.")
