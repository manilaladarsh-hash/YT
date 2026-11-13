import json
from pathlib import Path

staging_progs = Path("data/staging/programs")
staging_progs.mkdir(parents=True, exist_ok=True)

# Update notes on qut.json to reflect updated status
uni_file = Path("data/staging/universities/qut.json")
uni_data = json.loads(uni_file.read_text(encoding="utf-8"))
uni_data["notes"] = "QUT Doctor of Philosophy (CRICOS 006367J) is governed under the Higher Degree Research Candidates Policy (MOPP id=128). Research admissions are accepted year-round ('Start any time') across faculties including Engineering and Science."
uni_data["checked"] = "2026-10-30"
uni_file.write_text(json.dumps(uni_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

departments = {
    "cs": ("School of Computer Science", []),
    "math": ("School of Mathematical Sciences", []),
    "statistics": ("School of Mathematical Sciences", []),
    "chemistry": ("School of Chemistry and Physics", []),
    "physics": ("School of Chemistry and Physics", []),
    "earth": ("School of Earth and Atmospheric Sciences", []),
    "biology": ("School of Biology and Environmental Science", []),
    "civil": ("School of Civil and Environmental Engineering", []),
    "environment": ("School of Civil and Environmental Engineering", []),
    "ece": ("School of Electrical Engineering and Robotics", []),
    "mech": ("School of Mechanical, Medical and Process Engineering", []),
    "bme": ("School of Mechanical, Medical and Process Engineering", []),
    "chemeng": ("School of Mechanical, Medical and Process Engineering", []),
    "materials": ("School of Mechanical, Medical and Process Engineering", []),
}

ets_quote = "The GRE Subject Tests in Mathematics, Physics and Psychology measure undergraduate achievement in a particular field of study"
ets_url = "https://www.ets.org/gre/score-users/about/subject-tests.html"
prog_url = "https://www.qut.edu.au/courses/doctor-of-philosophy"
mopp_url = "https://mopp.qut.edu.au/document/view.php?id=128&version=1"

for field, (dept, also_fields) in departments.items():
    if field in ("math", "physics"):
        gre_sub = {
            "code": "Not stated",
            "value": "No GRE Subject test requirement is specified for doctoral admission.",
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
        "id": f"qut--{field}",
        "university": "qut",
        "field": field,
        "also_fields": also_fields,
        "department": dept,
        "program_page": prog_url,
        "checked": "2026-10-30",
        "fields": {
            "deadline": {
                "code": "Rolling",
                "value": "The Doctor of Philosophy degree accepts applications on a rolling basis ('Start any time').",
                "quote": "Start any time",
                "url": prog_url
            },
            "entry_route": {
                "code": "Not stated",
                "value": "Admission criteria for Doctor of Philosophy and Master of Philosophy degrees are outlined in the respective course requirements on the QUT website.",
                "quote": "(8) Admission criteria for Doctor of Philosophy (PhD) and Master of Philosophy (MPhil) degrees are outlined in the respective course requirements and published on the QUT website.",
                "url": mopp_url
            },
            "supervisor": {
                "code": "Required",
                "value": "All higher degree research candidates must have a minimum of two academic supervisors (Principal and Associate).",
                "quote": "(13) All higher degree research (HDR) candidates must have a minimum of two Supervisors, one of whom will be the Principal Supervisor and the other an Associate Supervisor. Both Supervisors must be current academic staff members.",
                "url": mopp_url,
                "also": [
                    {
                        "quote": "Maintain regular contact with supervisors and participate in University scholarly activities such as seminars, teaching and publication; a program of supervised research and investigation; and preparation of a thesis.",
                        "url": prog_url
                    }
                ]
            },
            "funding": {
                "code": "Competitive",
                "value": "Domestic HDR candidates are eligible for RTP tuition fee exemptions; QUT offers a limited number of sponsorships to international students.",
                "quote": "(16) Consistent with the Australian Government Research Training Program, all domestic higher degree research (HDR) candidates are normally eligible for a period of tuition fee exemption. QUT offers a limited number of sponsorships to international students based on faculty recommendations.",
                "url": mopp_url
            },
            "gre_subject": gre_sub
        },
        "notes": f"QUT offers the Doctor of Philosophy in {dept} under centralized Higher Degree Research Candidature regulations."
    }

    with open(staging_progs / f"qut--{field}.json", "w", encoding="utf-8") as f:
        json.dump(prog_data, f, indent=2, ensure_ascii=False)
        f.write("\n")

print(f"Generated QUT and {len(departments)} programs.")
