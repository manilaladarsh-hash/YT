# Research brief: one university, all its STEM PhD programs (schema 2.0)

You are researching **one university** for the STEM PhD Atlas 2027, a paid, source-cited guide for international (mostly Indian) PhD applicants for **Fall/Autumn 2027 entry**. Accuracy is the whole product: every value must be backed by an exact sentence on an official university page that you fetched. Never write from memory, a search snippet or a third-party site (no Yocket, Reddit, LeapScholar, etc.). If an official page doesn't say it, the code is `Not stated`. That's fine and honest.

Work in `/home/user/YT/business/phd-atlas`. Write **only** to `data/staging/` (set `ATLAS_OUT=data/staging`). Don't edit anything else, don't build, don't commit.

## What to produce
1. **One university record** (`save_university`). Use what the graduate school or university sets for every PhD applicant: application fee, international fee waiver, GRE General policy, TOEFL iBT minimum, IELTS Academic minimum, and whether an **English-medium degree from India** waives the English test.
2. **One program record per STEM field** the university runs a PhD in (`save_program`). Field ids are in `data/fields.json`:
   - physics, astronomy, chemistry, materials, math, statistics, cs, datasci;
   - biology, biomed, neuro, earth, environment;
   - ece, mech, chemeng, civil, bme.
   - Each program record holds the deadline, subject GRE, supervisor-first rule, funding and entry route. If the department states its own fee, GRE, TOEFL/IELTS or English rule, add that field to the program too (the department value wins).
   - Skip fields the university has no PhD in.
   - If one umbrella program covers several fields (e.g., "Biological and Biomedical Sciences", "Engineering Physics", a German graduate school), save it once under the main field and list the others in `also_fields`.
   - Don't save a program record whose every field would be Not stated (for example, every department page was blocked); list it under blocked URLs instead.
   - If a separate school inside the university admits the program (an engineering, medical or public-health school with its own application), and its fee, GRE or English rules differ from your university record, add them to the program as overrides. If you can't reach that school's rules, add those fields as `Not stated` overrides with a value saying the school sets them, so the graduate-school rule isn't shown by mistake.
   - Don't create a "datasci" record unless a PhD in data science, statistics + ML, AI or similar actually exists as its own program or official track.
3. If the university already has a `physics` program in `data/programs/<uid>--physics.json`, don't redo it from scratch:
   - Copy it into `data/staging/programs/` (keep every existing value, quote and url exactly).
   - Only replace its `Not stated` fields when a fetched official page answers them. In particular, add `ielts_min` there if the physics department states its own IELTS rule.
   - If one of its app_fee, fee_waiver, gre_general, toefl_min, ielts_min or english_waiver values quotes a graduate-school page (not a physics rule) and your university record covers the same field, delete that field from the physics record so it inherits the university value.
   - Then fill the university record and the other fields.
4. **Schools** (a Max Planck/IMPRS school, ICFO, SISSA, a cluster graduate school) are their own "university" record:
   - Fill the university record from the school's own application pages (fee, English rules and so on).
   - Improve the physics record as in step 3.
   - Add other fields only if the school itself runs a PhD program in them. If the same program covers a second field (e.g. chemistry), add it to `also_fields` in the physics record instead.

## Tools
- Find pages with WebSearch (`site:` the university domain helps), then **fetch every page you quote** with the cached fetcher:
  - `python3 scripts/research.py URL --profile` prints admissions facts by category;
  - `python3 scripts/research.py URL --kw deadline,fee,GRE,TOEFL,IELTS,India,waiver,stipend,funding,supervisor --max 20`;
  - `python3 scripts/research.py URL --links phd,doctoral,admission,apply,international,english,fee` lists the page's links.
- Quote from the fetched text only. Quotes are matched against the cached page after whitespace and curly-quote normalisation.
  - Join separate sentences with ` | `, and mark a gap inside a sentence with `...`.
  - Each piece must be at least 12 characters and appear verbatim.
- **Blocked pages** (403, Cloudflare, under 800 characters): try another official page (the graduate catalog, the PDF handbook, the department FAQ). If nothing works, record `Not stated` and list the blocked URL in your final reply.
- **Budget:** about 2–4 fetches per program and 4–6 for the university-wide pages. Prefer the graduate school's "international applicants", "English proficiency" (look for India or country lists), "application fee/waiver" and "GRE" pages. For each department, prefer its "PhD admissions" or "how to apply" page.

## Codes (validator-enforced)

| Field | Codes |
|---|---|
| deadline | ISO `YYYY-MM-DD` for Fall 2027 entry (2026-10-01 to 2027-08-31), `Rolling`, `Per position` or `Not stated`. Use the deadline for international applicants who want funding consideration (the earliest if there are several, with the others in the value). If the page shows a day and month without a year, use the 2026/27 cycle date and add `{"inferred": "year"}`. If acting earlier matters (a fee-waiver window, a scholarship round), add `{"time_sensitive": "YYYY-MM-DD"}` |
| app_fee | `90 USD`, `75 GBP`, `100 CHF`, `125 CAD`, `0 (no fee)`, `0 (waived)` or `Not stated`. Currencies: USD CAD GBP EUR CHF SEK DKK NOK AUD NZD |
| fee_waiver | `Available` (internationals can get one), `Limited` (narrow criteria or few), `Domestic only`, `None`, `No fee`, `Not stated` |
| gre_general, gre_subject | `Required`, `Recommended`, `Optional`, `Not required`, `Not considered`, `Not stated`. gre_subject is the field's own GRE Subject test (Physics, Chemistry, Mathematics; Psychology for neuroscience). Where no subject test exists for the field (CS, engineering, biology since 2023…), use `Not stated` unless the page says something |
| toefl_min | an integer such as `90`, `4.5 (new scale)`, `Sections` (only section minimums), `Not required` (the university asks for no English certificate at all, quoted) or `Not stated` |
| ielts_min | an overall band like `6.5` or `7`, `Not required` (as above) or `Not stated` |
| english_waiver | for a degree taught in English in India: `Yes` (India or "medium of instruction English" accepted outright), `Conditional` (needs a certificate or letter, or a minimum duration…), `No` (India not accepted; a test is required), `Check tool`, `Not stated` |
| supervisor | `Required` (must have a supervisor's agreement before or as part of admission), `Recommended` (advised to contact faculty), `Not required` (admission by committee, e.g. US cohorts with rotations), `Not stated` |
| funding | `Guaranteed` (all admitted PhD students are funded, e.g. a US 5-year guarantee or a salaried position), `Typical` (most are funded), `Competitive` (funding is competitive or scholarship-based), `Not stated` |
| entry_route | `Direct from bachelor's`, `Master's usually required`, `Either`, `Not stated` |

`value` is one or two plain-English sentences for an Indian applicant, stating the rule and any conditions. Every known code needs a quote. `url` must be the https page the quote is on. Extra supporting quotes go in `{"also": [{"quote": "...", "url": "..."}]}`.

## Saving (example)

```bash
cd /home/user/YT/business/phd-atlas && ATLAS_OUT=data/staging python3 - <<'PY'
import sys; sys.path.insert(0, "scripts")
from rec import save_university, save_program
G = "https://grad.example.edu/admissions/international"
save_university("example", "Example University", "USA", "California", G, {
    "app_fee": ("135 USD", "Application fee is $135 for all applicants.", "The application fee is $135", G),
    "fee_waiver": ("Domestic only", "Fee waivers are only for US citizens and permanent residents.", "Fee waivers are available to U.S. citizens and permanent residents", "https://grad.example.edu/fee-waivers"),
    "gre_general": ("Not stated", "Set by each program; see the program record.", "", G),
    "toefl_min": ("90", "TOEFL iBT 90 minimum.", "minimum TOEFL iBT score of 90", G),
    "ielts_min": ("7", "IELTS Academic 7.0 overall.", "IELTS score of 7", G),
    "english_waiver": ("No", "India is not on the exempt-country list, so Indian applicants need a test score.", "exempt if ... a country where English is the official language", G),
}, notes="")
D = "https://chem.example.edu/phd/apply"
save_program("example", "chemistry", "Department of Chemistry", D, {
    "deadline": ("2026-12-01", "Apply by December 1, 2026.", "Application deadline: December 1", D, {"inferred": "year"}),
    "gre_subject": ("Not considered", "The Chemistry GRE is not considered.", "GRE scores are not considered", D),
    "supervisor": ("Not required", "Admission is by committee; students join a group after rotations.", "students complete three rotations", D),
    "funding": ("Guaranteed", "All admitted PhD students receive full funding for five years.", "All admitted students are guaranteed five years of support", D),
    "entry_route": ("Direct from bachelor's", "Apply straight from a bachelor's degree.", "a bachelor's degree in chemistry or a related field", D),
}, notes="Rotations in the first year.")
PY
```

## Before you finish
- Run `python3 scripts/validate_data.py --dir data/staging --require-cache` and fix **every error in your own files** (`<uid>.json`, `<uid>--*.json`). Ignore other universities' errors; other agents are working in parallel.
- **Final reply** (short): the uid; the fields saved; the fields with no PhD there; the fields that are mostly Not stated and why; any blocked URLs. No other commentary.
