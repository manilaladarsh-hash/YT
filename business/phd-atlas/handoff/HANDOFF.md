# Handoff v2: repair, finish the US top 300, close the gap

Written 2026-10-31 after auditing the 50 commits made since the first handoff (`f304198` to `6e21f34`). Every number here was measured on that date; re-measure in Phase 0. Paths are relative to `business/phd-atlas/` in `manilaladarsh-hash/YT`. Branch: `claude/magical-dirac-6pfq3g`.

The rules in §8 still apply: no guessing, staging first, check exit codes, no secrets, no PR unless the owner asks.

---

## 1. Where the project stands

| | First handoff (Oct 29) | Now (Oct 31) |
|---|---|---|
| Universities with programs | 283 | **332** (of 340 listed) |
| Programs | 2,968 | **3,649** |
| Validation (`--require-cache`) | 0 errors | 0 errors ✅ |
| Not stated overall | 30% | **20.7%** (8,304 / 40,139); the gate is 15% ❌ |
| Fields under 25% | 0 of 18 | 17 of 18. **Math is 25.4%** ❌ (it was 24.95% before the last universities were added) |
| US universities | 206 | 206, which covers **205 of the 326 Carnegie R1 + R2** universities |
| Explorer | 1.58 MB | 1.75 MB (8.1 MB raw data); build OK, **24 of 24 tests pass** ✅ |

**What went well.** The "No subject test" fix (D1) was done correctly, with a cited ETS quote. The wave 1 review items were resolved as recommended. University-level passes cut Not stated quickly. The validator and gate code were **not** weakened; the only changes were UTF-8 and Windows fixes. The spot check below found no sign of invented quotes.

**What went wrong.** These issues pass the validator, but they would mislead a buyer. Phase A fixes them before anything else.

| Problem | Size | Example |
|---|---|---|
| **Programs with no evidence they exist.** Every program at the university points to one generic "how to apply" page, gets the same quotes, and has a department name typed from memory | **426 programs at 37 universities** (345 of them added since Oct 29) | Bath has 17 programs, all citing `bath.ac.uk/guides/how-to-apply-for-doctoral-study/`. Its "earth" program is listed as "Architecture & Civil Engineering / Life Sciences". UCR has 16 programs, all citing `graduate.ucr.edu/programs`. Most affected: 11 UK universities with 17 each, plus UCL, UCR, KU Leuven, Caltech, QUT, UCF, Monash, UCSC and Macquarie |
| **Quote doesn't support the code.** The quote is on the page, but it's about something else | **742 flagged**; a sample suggests about half are real problems | `uic--chemeng` funding "Typical" quotes a deadline sentence. `dtu` fee waiver "No fee" quotes an exam rule. `newcastle--ece` deadline "Rolling" quotes a sentence about studentship titles |
| **Inferred from silence.** A code such as "Not required" or "No fee" where the page never mentions the item | **123** | `floridatech--chemistry` GRE "Not required" from a list of materials that leaves the GRE out. `dalhousie` GRE "Not required" from a sentence about minimum standards |
| **Non-standard cache entries.** Pages cached by another fetch path (`via`/`html_hash` fields, not `research.py`) | 46 values (uark, uwyo) | Should be re-fetched through `research.py` |
| **Gaps in the log.** `PROGRESS.md` stops at 288 universities; the last ~44 additions (UK, Australia, US) aren't logged | — | — |

The live spot check re-fetched 40 random new quotes with a plain HTTP client. 28 were found on the live page. The other 12 were bot blocks (403), PDFs or JavaScript-only pages, which `research.py` handles with headless Chromium. None of them looked invented. Phase A4 runs the full check.

Tools added for this handoff:
- `scripts/audit_quality.py` runs the four checks above. Its findings as of today are in `handoff/audit_2026-10-31.csv`.
- `handoff/us_r1r2.csv` lists all 326 Carnegie 2025 R1 + R2 institutions with their atlas status.

## 2. Definition of "top 300 US universities"

The plan uses the **2025 Carnegie Classification R1 + R2 list (187 + 139 = 326)**. It is public and free, and it is defined by research spending and doctorate output, which suits a PhD guide. Rankings like US News are paywalled and can't be cited in full. Source: ACE Carnegie Classifications, 2025 Research Activity Designations (carnegieclassifications.acenet.edu). `handoff/us_r1r2.csv` was built from Wikipedia's copy of that list. **First, check it against the official public data file** on the Carnegie site, the "2025 Research Activity Designation Public Data File".

Status of the 326 (column `status` in the CSV):

| Status | Count | Meaning |
|---|---|---|
| `covered` | 205 | Already in the atlas (171 of the 187 R1s) |
| `add` | 47 | Has, or is likely to have, STEM PhDs in our 18 fields; research it fully. 3 are R1 (CUNY Graduate Center, IU Indianapolis, UMass Boston) and 44 are R2 |
| `screen-check-stem-phd` | 48 | Mainly teaching, regional or professional schools (Cal States, Seton Hall, Pepperdine, American, Catholic, Nova Southeastern…). Use one fetch of the official doctoral program list to decide: add it only if it offers a PhD in one of the 18 fields. Otherwise set the status to `screened-out` with the URL |
| `screen-health-sciences` | 26 | Medical and health-science universities (UCSF, UT Southwestern, Baylor College of Medicine, Weill Cornell, Icahn, MUSC…). Research **only biomed, neuro, bme, and biology where it exists** |

The matching was automatic, with a manual alias list. Check any row that looks wrong. If the owner meant a different list, such as US News top 300, ask once in Phase 0, then use the CSV approach with that list.

Expected size: about 47 + 26 + ~20 screened in, so **roughly 90 new US universities and 600–900 new programs**. New R2 universities usually publish less detail, so **this will push Not stated up** unless Phase C keeps pace. Plan for that from the start.

## 3. Owner decisions (ask in one message in Phase 0)

| # | Question | Recommendation |
|---|---|---|
| E1 | Is "top 300 US" = Carnegie R1 + R2 (326)? | Yes |
| E2 | For the 426 generic-page programs: keep only programs with their own official PhD page, and **move** the rest to `data/staging/_removed/` (not delete) with a reason? | Yes. A program with no evidence it exists shouldn't be sold |
| E3 | Inferred from silence: forbid it (use Not stated), or allow it only when the page is an explicit, complete list of required materials, flagged `{"inferred": "not listed"}` and shown as "Not listed in requirements"? | Forbid it, except for explicit statements such as "Test scores: None" |
| E4 | Health-science universities: biomed, neuro and bme only? | Yes |
| E5 | If Not stated stalls above 15% after Phase C: (a) launch with an honest coverage note, (b) keep researching, or (c) revise the gate? | Owner's call |

## 4. Phases

### Phase 0: verify (no changes)

```bash
git pull origin claude/magical-dirac-6pfq3g && cd business/phd-atlas
python3 scripts/validate_data.py --dir data --require-cache; echo rc=$?   # 332 universities, 3649 programs, 0 errors
python3 scripts/coverage.py --gate; echo rc=$?                            # 20.7%, NOT MET
python3 scripts/audit_quality.py --csv /tmp/audit.csv                     # 426 / 742 / 123 / 46
python3 product/build.py && python3 -m pytest -q tests; echo rc=$?
```

Fill the gap in the log: add a `PROGRESS.md` entry listing every university added after the 288-university entry, with the commits from `git log f304198..HEAD`. Then send E1–E5.

### Phase A: repair (before adding any university)

**A1. Generic-page programs (426).** For each of the 37 universities in the `generic_page` rows:
1. Fetch the university's official list of doctoral programs.
2. For each field, find the department or program's own PhD page, which must name the PhD in that field. If none exists, the program goes to `_removed/` (E2), with the reason in `PROGRESS.md`.
3. Set `program_page` to that page and `department` to the name **as written on that page**.
4. Re-research the program-level values (deadline, supervisor, funding, entry route) from that page. University-wide pages are fine for university-level values only.
5. Work in staging: copy the records in, edit, validate, then run `promote.py`. A record moved to `_removed/` needs the owner's OK under E2.

Order: start with the UK eleven (Birmingham, Bath, Leeds, Sheffield, Exeter, Newcastle, Cardiff, Manchester, Liverpool, Nottingham, Southampton), then UCL, UCR, KU Leuven, Caltech, QUT, UCF, Monash, UCSC, Macquarie, then the rest.

UK note: many UK PhDs really are applied through one central portal, which is fine for the deadline, fee and English values. **Existence and supervisor/funding** still need the department's own research-degree page.

**A2. Off-topic quotes (742) and inferred-from-silence (123).** Work through `audit.csv` row by row. For each row, re-read the cached page and either:
- replace the quote with one that supports the code,
- change the code to match what the page says, or
- set it to `Not stated`.

About half of the off-topic rows are false alarms; for example, "We do not accept them" is a valid GRE quote. Mark those `ok` in a reviewed copy of the CSV so they aren't re-checked.

**A3. Odd cache (46).** Re-fetch those URLs with `scripts/research.py`, so every cache entry has the standard format, then re-validate.

**A4. Full source check.** `python3 scripts/check_sources.py --out /tmp/sources.md`. Review every quote that's missing from a page that was fetched successfully. List bot-blocked pages for the owner, who can save them by hand with `scripts/import_saved_page.py`.

**A5. Guard against repeats.** Add the `generic_page` check to `validate_data.py` as a **warning**, so it appears on every run. Re-run `audit_quality.py` after each batch from now on. Phase A is done when `generic_page` is 0 (apart from rows the owner approved), every off-topic and absence row is resolved or marked ok, and validation shows 0 errors.

Commit after each university or small group: `Repair <uid>: program pages, quotes`.

### Phase B: finish the US top 300

**B0.** Confirm `us_r1r2.csv` against the official Carnegie data file and fix any mismatches.

**B1. For each new university:**
1. Add it to `data/universities.json`: `id` (short, lowercase, unique), `name` (official), `country: "USA"`, `region` (state name, matching existing entries), `kind: "university"`, `wave: 5`. Check that the id doesn't already exist.
2. **Program list first:** fetch the official graduate catalogue or doctoral program list and record which of the 18 fields have a real PhD there (see `data/fields.json` for field ids and scope). Don't create a record for a field without a PhD. A master's-only department doesn't count.
3. **University-level values (6)** from the graduate school's admissions, international and fee pages: `save_university(...)`.
4. **Program-level values (5)** from each program's own page: `save_program(...)`. `program_page` must be that page.
5. Validate staging, run `audit_quality.py --dir data/staging`, fix what it finds, run `promote.py`, then commit: `Add <name> (<uid>): N STEM PhD programs`.
6. Update the `status` and `atlas_id` columns in `us_r1r2.csv`.

**Batches of 10.** After each batch: run `coverage.py`, `measure.py` and `audit_quality.py`, write a `PROGRESS.md` entry, and push.

**Order:**
1. B2: 3 R1 `add` + 10 R1 health-science + 3 R1 screen (American, Catholic, Nova Southeastern). **That completes all 187 R1s.**
2. B3: 44 R2 `add`.
3. B4: 45 R2 screen. One fetch each, and research fully only those that pass.
4. B5: 16 R2 health-science.

Phase B is done when every row in `us_r1r2.csv` is `covered` or `screened-out` with a URL.

### Phase C: close the gap to the gate (in parallel with B from batch 3 on)

At today's size, the gate needs **about 2,285 more values resolved**. Phase B will add more.
- Rebuild the gap-fill queue from live data, sorted by **absolute** Not stated count per university, not by rate. `handoff/queue.txt` is out of date; regenerate it with the same logic, largest first.
- University-level values first: one page fixes every program at that university.
- Math (25.4%) and physics (24.1%) are closest to failing per field. The unanswered values there are mostly `gre_subject` and `supervisor`. Check the math and physics department admissions FAQs; they often state the Subject GRE policy.
- Rule of thumb from the data so far: university-level passes cut Not stated by 10–25 points per university; program-level passes cut it by 5–10.
- Stop rule: if two consecutive batches of 20 each move the overall rate by less than 0.5 points, stop and ask the owner (E5).

### Phase D: rebuild, test, documents, gate

Use the steps from the first handoff (still valid):
- Run `python3 product/build.py && python3 -m pytest -q tests`, then the `handoff/qa/*.js` checks. Look at every screenshot.
- The explorer must stay ≤5 MB and load in under 2 s at 4× CPU slowdown. Watch the raw data size, now 8.1 MB, as about 800 programs are added.
- Update every count in `product/content/*.md`, `store/LISTING_COPY.src.md`, `store/EMAILS.md`, `launch/`, `README.md` and `BUSINESS_PLAN_README.md` §2 from the final `coverage.py` output. Re-render store images that show counts.
- Run `python3 scripts/coverage.py --gate` and report each gate item with real numbers. Commit and push. No PR unless asked.

## 5. Program record rules (stricter than before; these come from the audit)

1. **One program = one official page that names that PhD.** A generic "how to apply" or "all programs" page can't be `program_page`.
2. **`department` is copied from that page**, not written from memory. Don't combine departments ("X / Y") to cover a field the university doesn't offer.
3. **University-level values come from graduate-school pages.** A rule found only on a department page goes in that program as an override (`overrides`), not in the university record.
4. **The quote must state the rule behind the code.** If you have to explain why a quote implies the code, it doesn't qualify.
5. **Never infer from silence** (E3).
6. **Deadlines are for Fall 2027 entry.** Scholarship dates and "review begins" dates go in `time_sensitive`, not `deadline`.
7. When two official pages conflict, use the more specific one, note the other in `notes`, and list the conflict in `PROGRESS.md`.

## 6. Throughput and order of work

Since Oct 29, Gemini added about 47 universities and enriched about 100 in two days. At that pace:

| Phase | Work | Rough size |
|---|---|---|
| A | Repair 37 universities and review ~865 flags | 1–2 days |
| B | ~90 new US universities | 3–5 days |
| C | Gap-fill until the gate or the stop rule | 2–4 days |
| D | Build, docs, gate | 0.5 day |

Do **A before B**. If the generic-page pattern spreads to 90 more universities, it costs far more to undo.

## 7. Progress log format (every batch, no exceptions)

```
## <Phase><batch> — YYYY-MM-DD
Universities: added … | repaired … | screened out … (url)
Programs: +N new, −M moved to _removed (reason)
Not stated: overall X% -> Y%   math A% physics B%
audit_quality: generic_page / off_topic / absence / odd_cache = …
Blocked pages (for owner): …
Owner questions: …
Commit: <sha>
```

## 8. Ground rules (unchanged)

- No value without a verbatim quote from an official page fetched with `scripts/research.py`. No third-party sites. No memory.
- Research in `data/staging/` with `ATLAS_OUT=data/staging`; promote only with `scripts/promote.py`.
- Check `rc=$?`; never commit after a failed check.
- No secrets, credentials or ID numbers. Never disable TLS verification or unset proxy variables.
- Ask before spending money, sending messages, deleting files or reorganising folders. Moving a record to `_removed/` counts as a deletion, so it needs E2.
- Never invent customers, testimonials, sales or demand.
- Commit at every checkpoint, push to `claude/magical-dirac-6pfq3g`, no PR unless the owner asks, no AI model names in commits or files.
- If you have Notion access, update the existing project records after each phase (no duplicates, never mark an archive record "Full" unless its content was imported).
