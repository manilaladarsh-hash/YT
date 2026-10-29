# Handoff: finish STEM PhD Atlas 2027

This document is for the coding agent taking over this project. The owner reads it too. It was written on 2026-10-29, and every number in it was measured on that date. Re-measure in Phase 0 before you rely on any of them.

Paths are relative to `business/phd-atlas/` in the repo `manilaladarsh-hash/YT`, unless they start with `/`.

---

## 1. What you are finishing

The **STEM PhD Atlas 2027** is a paid, offline kit for international (mostly Indian) applicants to STEM PhDs in the US, Canada, the UK, Europe, Australia and New Zealand. It contains:

| File | Built from |
|---|---|
| `Atlas.html` (offline explorer: filters, fit check, My plan, .ics and CSV export) | `product/templates/atlas.html` and `product/build.py` |
| `Atlas.xlsx` (planner workbook) and `Atlas.csv` | `product/build.py` |
| `Playbook.pdf` and `START-HERE.pdf` | `product/content/*.md`, `product/pdf.cjs` |
| `Free-Sample-STEM-PhD-Atlas-2027.pdf` | `product/sample.py` |
| ZIP for Gumroad | `product/build.py` writes `dist/STEM-PhD-Atlas-2027-v2.0.zip` |

Every data value is a **code, a plain-English value, a verbatim quote, and the URL** of the official page the quote is on. `scripts/validate_data.py --require-cache` checks that each quote appears on the cached copy of that page, stored in `.cache/pages/`. Unknown values are `Not stated`. They are never guessed. This is what the product sells, so protect it above everything else.

Background on the business, pricing and decisions is in `BUSINESS_PLAN_README.md`, and §0 and §2 are the most important parts. There are **no customers, sales or testimonials**, and none may be invented.

## 2. The finish line: the release gate

The project is finished only when **all** of the following are true:

| Gate | How to check | Status on 2026-10-29 |
|---|---|---|
| ≥180 universities with programs | `python3 scripts/coverage.py --gate` | 283 ✅ |
| ≥12 fields with 30+ programs | same | 18 ✅ |
| Not stated **<15% overall** | same | **30%** ❌ (9,920 of 32,648 values) |
| Not stated **<25% in every field** with 30+ programs | same | **all 18 fields between 26% and 35%** ❌ |
| Every quote verified, 0 errors | `python3 scripts/validate_data.py --dir data --require-cache` | 0 errors ✅ |
| Explorer tests on desktop and phone; loads in under 2 s at 4× CPU slowdown; offline | `python3 -m pytest -q tests` (24 tests) | passing ✅ |
| Explorer file ≤5 MB | test suite | 1.58 MB ✅ |
| PDFs render cleanly | test suite and a visual check | passing ✅ (re-check after data changes) |

**The data gap is the only gate item that fails.** Most of the remaining work is closing it without breaking the no-guessing rule. After that, rebuild, re-test and release.

## 3. Where the Not stated values are (and the plan to close the gap)

Live data: 2,968 programs × 11 values each. Not stated by value:

| Value | Level | Not stated | Share of programs |
|---|---|---|---|
| gre_subject | program | 2,305 | 78% |
| gre_general | university* | 1,229 | 41% |
| supervisor | program | 1,150 | 39% |
| fee_waiver | university* | 952 | 32% |
| funding | program | 939 | 32% |
| english_waiver | university* | 605 | 20% |
| entry_route | program | 599 | 20% |
| deadline | program | 599 | 20% |
| toefl_min | university* | 573 | 19% |
| app_fee | university* | 499 | 17% |
| ielts_min | university* | 470 | 16% |

\* University-level values are set once per university, and every one of its programs inherits them unless the department states its own rule. **One fetch at university level fixes the value for every program at that university.** That makes it the cheapest work there is.

To reach 15% overall, about **5,000 Not stated values must be resolved**. The plan below gets there in four steps, cheapest first:

1. **Decision D1 (subject tests), about −1,950.** ETS now offers GRE Subject Tests only in Mathematics, Physics and Psychology. Chemistry, Biology and Literature were discontinued; verify this on ets.org and cite it. For a CS, engineering, chemistry or biology program, "GRE Subject: Not stated" is not a missing fact: **no such test exists.** The fix is a new code meaning "no Subject Test exists for this field", taken out of the Not stated count. It needs one cited ETS quote and the owner's approval (D1), because it changes the schema. Modelled effect: overall Not stated falls from 30% to **26.3%**. Every field then sits between 25% and 31%.
2. **A university-level pass on every university**, about −1,500 to −2,500. Fill the 6 university values (fee, waiver, GRE General, TOEFL, IELTS, English waiver) from the graduate school's admissions and international pages. That takes 2–4 fetches per university. 78 universities still have 3 or more of their 6 university values Not stated.
3. **A program-level pass, in the order of `handoff/queue.txt`**, which lists the universities by absolute Not stated count, biggest first. The top 60 universities hold 3,517 of the 8,223 Not stated values in the queue. Fill deadline, supervisor, funding, entry route, and GRE Subject (math, physics and neuroscience only).
4. **Review and promote** after each batch (§6, Phase 3), then re-measure.

Expected outcome, honestly: wave 1 (25 universities, full depth) took those universities from 69% to 56% Not stated. Many official pages simply do not publish a supervisor rule, a GRE stance or a funding promise. **Reaching 15% from official pages alone may not be possible.** If two consecutive batches each move the overall rate by less than 1 point, stop and bring decision D3 to the owner. **Never lower the gate yourself.**

## 4. Decisions the owner must make (ask at the start, in one message)

| # | Question | Recommendation |
|---|---|---|
| D1 | Add a `gre_subject` code for "no GRE Subject Test exists for this field" (cited to ETS), and stop counting it as Not stated? | **Yes.** It's a fact, not a guess, and it's the single biggest gain. |
| D2 | Run time and cost: full university-level pass on all ~250 remaining universities, then program-level passes in batches of 20 until gains flatten? | **Yes**, with a progress report after each batch. |
| D3 | If gains flatten above 15%: (a) launch with an honest coverage note, (b) keep researching, or (c) revise the gate? | Owner's call only. Report the numbers. |
| D4 | UAB has Interdisciplinary Engineering, Environmental Health Sciences and Materials Engineering PhDs that don't map to one field. Map each to its closest field with `also_fields`, or skip them? | Map, with a note saying the program spans several fields. |
| D5 | NAU (Northern Arizona) pages fail TLS: the emSign root CA is missing from the CA bundle in the previous environment. Retry in your own environment. If it still fails, skip NAU? | Retry. **Never** disable TLS verification. |

## 5. Ground rules (non-negotiable)

1. **No guessing.** A value without a verbatim quote from an official page you fetched is `Not stated`. Never fill a value from memory or "general knowledge". Third-party sites (blogs, aggregators, rankings) are never sources.
2. **Staging first.** Research writes to `data/staging/` only, with `ATLAS_OUT=data/staging` on every save. Live `data/` changes only through `scripts/promote.py`. *(An earlier agent ran the build without `ATLAS_OUT`, which overwrote 13 live files. They were restored from git.)*
3. **Check exit codes.** Never pipe a check through `tail` or `head` and then commit. Use `cmd; rc=$?` and commit only when `rc` is 0. Validate staging and live before every commit.
4. **Never** store secrets, credentials, API keys or ID numbers anywhere. **Never** disable TLS verification or unset proxy variables.
5. **Ask first** before spending money, sending any message, posting anywhere, creating accounts, deleting files, or reorganising folders. Adding new files is fine.
6. **Never invent** customers, testimonials, sales, demand, reviews or validation, and never present an estimate as a fact.
7. **Git:** work on branch `claude/magical-dirac-6pfq3g`, commit at every checkpoint with a clear message, and push with `git push -u origin claude/magical-dirac-6pfq3g`. **No pull request unless the owner asks.** Do not put AI model names in commit messages or files.
8. Keep `handoff/PROGRESS.md` up to date (§8) so the next session can resume after an interruption.
9. The owner keeps long-term memory in a Notion "Second Brain". If you have Notion access, read the project's records before deciding anything that depends on past choices, and update the existing records after major milestones (don't create duplicates). Never mark a Conversation Archive record "Full" unless the original content was actually imported. Don't delete or move anything in Notion without asking.

## 6. Phases

### Phase 0: set up and verify (do not change anything yet)

Requirements: Python 3.11+ with `requests beautifulsoup4 openpyxl pytest`; Node 18+ with `playwright` and Chromium; LibreOffice (`soffice`), which is optional and only needed for one workbook test.

```bash
git checkout claude/magical-dirac-6pfq3g && git pull origin claude/magical-dirac-6pfq3g
cd business/phd-atlas
python3 scripts/validate_data.py --dir data --require-cache; echo rc=$?          # expect 285 universities, 2968 programs, 0 errors
python3 scripts/validate_data.py --dir data/staging --require-cache; echo rc=$?  # expect 36 universities, 227 programs, 0 errors
python3 scripts/coverage.py                                                       # expect 30% overall
python3 handoff/measure.py | tail -1                                              # staged universities: 69% -> 56%
python3 product/build.py && python3 -m pytest -q tests; echo rc=$?                # expect 24 passed (1 may skip without LibreOffice)
```

If any number differs, write down the difference in `PROGRESS.md` and find out why before going further. Then send the owner the D1–D5 questions in one message.

### Phase 1: subject-test fix (only if D1 = yes)

1. Fetch the ETS page that lists the current GRE Subject Tests: `python3 scripts/research.py <ets url> --kw Subject,Mathematics,Physics,Psychology,discontinued`. Keep the exact quote.
2. Add the new code to `gre_subject` in `data/schema.json`. Suggested wording: `"No subject test"`, labelled "No GRE Subject Test exists for this field". Update the validator's enum check if it hard-codes values, and the brief (`data/staging/RESEARCH_BRIEF.md`, line 48).
3. Write a one-off script that, for every program whose field has no ETS Subject Test (everything except `physics`, `math` and `neuro`), changes `gre_subject` **only where the code is currently `Not stated`** to the new code. Use the ETS quote and URL. A program-specific statement that is already recorded (for example "GRE scores are not considered") stays as it is.
4. Teach the explorer, CSV, workbook and PDFs to show the new code sensibly. Grep `product/` for `gre_subject` and `Not stated`. The fit engine must treat it like "Not required".
5. Validate, run `coverage.py`, run the tests, and commit.

### Phase 2: research waves

**Order:** university-level pass across the whole queue first, then the program-level pass from the top of `handoff/queue.txt`. Work in **batches of 20 universities**.

**For each university:**

1. Run `python3 handoff/research_prompt.py <uid>`. It prints the exact task: what exists live, what is already staged, and the rules. Read `data/staging/RESEARCH_BRIEF.md` once at the start. It defines every code, the save helpers (`scripts/rec.py`: `save_university`, `save_program`), the quote rules and the reply format.
2. Fetch only with `python3 scripts/research.py URL [URL...] --kw a,b,c`. It caches the page, which the validator needs, and prints the matching sentences. Budget: 4–6 fetches for university-wide pages, plus 1–2 per department.
3. Copy the live records into staging, fill **only** the Not stated values, and keep every verified value. Save with `ATLAS_OUT=data/staging`.
4. Before each save, apply the quality checks:
   - **Deadline** must be for **Fall 2027 entry**. Do not use a scholarship date, a "review begins" date, or a Spring date. If the year is inferred, set `{"inferred": "year"}`. If the date is already in the past, it's the wrong cycle.
   - **A campus-wide deadline** applies to a department only if the department page doesn't set its own date. Note when you applied it.
   - **TOEFL "new scale"** (1–6) only when the page says so.
   - **English waiver = Yes** only when India or "medium of instruction English" is accepted outright. Wording such as "generally not necessary" is `Conditional` at most.
   - **Funding = Guaranteed** only for "all admitted students are funded" or salaried positions. "Limited contracts" means `Competitive`.
   - If two official pages conflict, use the more specific page (the department over the catalogue), record the other in `notes`, and add it to the review list.
5. Run `python3 scripts/validate_data.py --dir data/staging --require-cache; echo rc=$?` and fix every error in this university's files.

**After each batch:** run `python3 handoff/measure.py` for the before-and-after, commit `data/staging` and `.cache/pages` together, push, append the results and any flags to `PROGRESS.md`, and promote the reviewed universities (Phase 3).

Pages that block automated reads: record them as blocked in `PROGRESS.md`. The owner can save a page from their own browser and import it with `scripts/import_saved_page.py`. List these pages for the owner; do not work around blocks.

### Phase 3: review and promote (after each batch)

1. Go through the open review items (§7) and the flags from the new batch. Fix each one from its source page, or set the value to `Not stated` if the source can't settle it. Ask the owner only about judgement calls.
2. Run `python3 scripts/promote.py <uid> [<uid> ...]` for the reviewed universities. The script validates first and refuses to promote if there is any error.
3. Run `python3 scripts/validate_data.py --dir data --require-cache; echo rc=$?` (must be 0), then `python3 scripts/coverage.py`, then commit and push.

### Phase 4: explorer and build checks (after data changes and before release)

The explorer UI overhaul and desktop layout are **done and approved**. Don't redesign them. Do only these checks:

```bash
python3 product/build.py && python3 -m pytest -q tests; echo rc=$?
mkdir -p /tmp/atlas-qa && cd /tmp/atlas-qa
QA_OUT=/tmp/atlas-qa node <repo>/business/phd-atlas/handoff/qa/test.js   # desktop and phone: load, filters, search, detail, plan, CSV; prints JSON
QA_OUT=/tmp/atlas-qa node <repo>/business/phd-atlas/handoff/qa/ui.js     # screenshots: fit, popovers, table, dark mode, detail
node <repo>/business/phd-atlas/handoff/qa/wide.js                        # screenshots at 1920 / 1536 / 1280 in the current folder
```

Pass criteria:
- In `test.js`: `errors: []`, `externalRequests: 0`, `horizontalOverflowPx: 0`, and `loadMs` well under 2000.
- In the screenshots: no words broken mid-word, 4/3/2 card columns at 1920/1536/1280, and the phone layout uses the bottom tab bar.
- **Look** at every screenshot. Don't just check that it exists.

AGENTS.md design rule: avoid unnecessary secondary labels and descriptions, and let the layout do the explaining.

### Phase 5: documents (task #20)

The documents are already written for STEM v2. What's left is to make every number and claim in them match the final data:

- `product/content/playbook.md`, `product/content/start-here.md`, `product/sample.py` output, `store/LISTING_COPY.src.md` (then `store/LISTING_COPY.md`), `store/EMAILS.md`, `launch/LAUNCH_PLAN.md` and its messages, `README.md`, and `BUSINESS_PLAN_README.md` §2 status table.
- Grep for counts of universities, programs, fields, countries and Not stated %. Replace each one with the figure from `coverage.py` or the build output, and don't round up.
- Leftovers from the physics edition: `README.md` still mentions v1.2 and physics. Update it to describe v2.0. Don't delete the v1.2 history notes.
- Re-render the store images if they show counts (`store/render_images.py`).
- Run `python3 product/build.py`, then open every PDF and check it page by page: START-HERE is one page, the sample is ≤3 pages, nothing is cut off, and no table has empty rows.

### Phase 6: release gate and handback (task #21)

1. Run `python3 scripts/coverage.py --gate; echo rc=$?`, the full test suite, and the Phase 4 QA.
2. Fill in the gate table from §2 with the real numbers. Commit and push.
3. Give the owner a report covering:
   - the gate result for each item;
   - what changed;
   - the open review items;
   - blocked pages they could save by hand;
   - and the remaining owner actions: create the Gumroad account (`store/GUMROAD_SETUP.md`), decide whether to make the repo private (risk R1 in the business plan: the repo is public), upload the ZIP, and send the launch messages. These are the owner's own actions; you do not do them.

## 7. Open review items (staged, not yet promoted)

| University | File(s) | Issue | Suggested action |
|---|---|---|---|
| Colorado School of Mines | `data/staging/programs/mines--*.json` | 2027-03-01 applied to every program; the table has no Fall or Spring labels, and Fall may be Oct 1 | Re-check the source table. Use per-department dates or `Not stated`. |
| Missouri S&T | `mst.json`, `mst--*.json` | Campus-wide deadline 2027-02-15 applied to all programs. TOEFL conflict: catalogue says 4.5, ECE says 80 | Use department dates where they're published. Record TOEFL as an ECE override. |
| Akron | `akron--chemistry.json` | The "deadline" is a date when review begins | Set to `Rolling` or `Not stated`, with a note. |
| TU Wien | `tuwien.json` | English waiver `Yes` based on "generally not necessary" | Change to `Conditional` unless a page names India or English-medium degrees. |
| Paris-Saclay | `paris-saclay--physics.json` | Funding `Guaranteed`, but the quote says contracts are limited | Change to `Competitive`. |
| Bologna | `unibo.json` | App fee EUR 10 in the call, but "no application fee" for Health & Technologies | Keep EUR 10 at university level and add a program override where it applies. |
| South Dakota | `southdakota.json` | App fee $38 on the page vs $40 in the catalogue | Use the admissions page and note the conflict. |
| South Dakota State | `southdakotastate.json` | TOEFL "4.0 (new scale)" was inferred | `Not stated` unless the page says it's the new scale. |
| Bern | `unibe--*.json` | Deadline 2026-10-15 has already passed, so the year is likely wrong | Find the 2027 date or set `Not stated`. |
| Canterbury NZ | live `data/programs/canterbury-nz--biomed.json`; staged `canterbury-nz--datasci.json` | The research found no Biomedical Sciences PhD, but the live biomed record still exists. The staged datasci deadline 2027-05-15 is a scholarship date | Ask the owner before removing the live biomed record. Set datasci to `Rolling` if a page says so, otherwise `Not stated`. |
| Auburn | `auburn--chemistry.json` | The notes need checking against the quote | Re-check the source. |
| UAB | — | 3 PhDs not saved | See D4. |
| NAU | — | TLS failure | See D5. |
| uwyo, wayne, wpi | `data/staging/universities/*.json` | University record staged but 0 programs | Finish their programs, or promote the university record alone. |

## 8. Progress log

Create `handoff/PROGRESS.md` and append one entry per batch:

```
## Batch N — YYYY-MM-DD
Universities: ...
Not stated (these universities): before -> after      Overall (coverage.py): X% -> Y%
Promoted: ...                Held for review: ... (why)
Blocked pages: ...           Owner questions: ...
Commit: <sha>
```

## 9. Known traps

- `scripts/research.py` can hang on a slow site. Run it with a timeout (for example `timeout 120`), and if it times out, carry on with the pages that are already cached.
- The validator only checks against cached pages. A quote copied from a browser, not a `research.py` fetch, will fail. Fetch it properly, or use `import_saved_page.py` for pages the owner saved.
- `.cache/pages/` is evidence: commit it together with the data, and don't clean it.
- `product/build.py` reads live `data/`, not staging. Staged changes don't show up in the explorer until they're promoted.
- Paid outputs (`dist/STEM-PhD-Atlas-2027/` and `dist/*.zip`) are git-ignored on purpose. Don't force-add them.
- Don't run several research processes against the same university at once.
