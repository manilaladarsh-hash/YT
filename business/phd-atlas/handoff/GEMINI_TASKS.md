# Task cards for the coding agent

Read this whole file once. Then work **one card at a time**. Never do two things at once.

Every command runs from the folder `business/phd-atlas`.

---

## CARD 0: Start of every session

1. Run `git pull origin claude/magical-dirac-6pfq3g`.
2. Run `bash handoff/check.sh`.
   - If it says `ALL CHECKS PASSED`, continue.
   - If it says `FAILED`, fix that one problem first and do nothing else.
3. Run `python3 handoff/next.py`.
4. It prints the name of a card (for example `CARD 4`). Do **that card only**.
5. When the card is finished, run `python3 handoff/next.py` again and do the card it prints.

You never choose the work yourself. `next.py` chooses it.

---

## CARD 1: The rules. Read them before every card.

**You must:**
- Copy every value from an official university web page. The page must be fetched with `python3 scripts/research.py URL`.
- Put the exact sentence from the page in `quote`, with no changes.
- Write `Not stated` if the page does not say the answer.
- Save new work in `data/staging/` first, never straight into `data/`.
- Run `bash handoff/check.sh` before every commit.
- Commit after every card, then push with `git push -u origin claude/magical-dirac-6pfq3g`.
- Add one line to `handoff/PROGRESS.md` after every card (format at the end of this file).

**You must never:**
- Guess a value or use what you "know". If you didn't see it on the page, it's `Not stated`.
- Use blogs, rankings, Reddit, Wikipedia or any non-university site as a source.
- Write "Not required" or "No fee" because a page *doesn't mention* something. That means `Not stated`.
- Delete any file. If something should go, write it in `handoff/OWNER_REVIEW.md` and leave it.
- Change `scripts/validate_data.py`, `scripts/coverage.py`, the release gate, or the tests to make a check pass.
- Turn off TLS or SSL checks, or change proxy settings.
- Send any message, post anywhere, create accounts, or spend money.
- Write customer counts, sales, reviews or testimonials. There are none.
- Write passwords, keys, tokens or ID numbers into any file.
- Open a pull request.

**If you are unsure, stop.** Write the question in `handoff/OWNER_REVIEW.md` and go to the next card.

---

## CARD 2: Repair a university whose programs all share one generic page

**Why:** some universities have up to 17 programs that all point to one general "how to apply" page. That doesn't prove each PhD exists. Each program needs its own page.

`next.py` gives you the university id (for example `bath`) and the list of its program files.

For each program file in the list:

1. Find that department's own PhD page on the university website. It must name the PhD in that subject (for example "PhD in Physics").
   - Fetch the university's list of research degrees: `python3 scripts/research.py "<url>" --kw PhD,doctoral,research`.
   - Then fetch the department page: `python3 scripts/research.py "<url>" --kw PhD,deadline,supervisor,funding,studentship`.
2. **If you find the page:**
   1. Copy the program file into staging: `cp data/programs/<file> data/staging/programs/`.
   2. In the staging copy, set `program_page` to the department page URL.
   3. Set `department` to the department name exactly as the page writes it.
   4. For `deadline`, `supervisor`, `funding` and `entry_route`: if the department page states the rule, replace the quote and url with the department page's sentence. If it doesn't, keep the old value.
3. **If no PhD page exists for that subject** (the university doesn't offer that PhD):
   1. Don't touch the file.
   2. Add a line to `handoff/OWNER_REVIEW.md`: `REMOVE? <file> — no PhD page found. Searched: <url>`.
   3. Add the row to `handoff/audit_reviewed.csv` as `generic_page,<file>,program_page`, so `next.py` moves on.

When every program in the list is done:

```
python3 scripts/validate_data.py --dir data/staging --require-cache
python3 scripts/promote.py <uid>
bash handoff/check.sh
git add -A && git commit -m "Repair <uid>: own program pages" && git push -u origin claude/magical-dirac-6pfq3g
```

If `audit_reviewed.csv` doesn't exist yet, create it with this first line: `check,file,field`.

---

## CARD 3: Review 10 flagged values

`next.py` prints 10 rows. Each row is a value whose quote may not support the answer. Do each row like this:

1. Read the quote and the code.
2. Ask: **does this sentence say the answer, by itself?**
   - "We do not accept GRE scores" → GRE `Not considered`. ✅ Supports it.
   - "February 15, 2027: International PhD applicants…" used for **funding** → ❌ It's about a deadline, not funding.
3. **If yes:** add the row to `handoff/audit_reviewed.csv` as `<check>,<file>,<field>`. Done.
4. **If no:**
   1. Fetch the url again: `python3 scripts/research.py "<url>" --kw <word>`. Use a word that fits the field, such as `funding`, `GRE` or `deadline`.
   2. If the page has a sentence that does say the answer, use that sentence as the new quote.
   3. If it doesn't, set `code` to `Not stated`, `value` to `Not stated on the page checked`, and `quote` to `""`.
   4. Make the edit in a staging copy (`cp data/programs/<file> data/staging/programs/`). For a university file, use `data/staging/universities/`.
5. For `odd_cache` rows: re-fetch the url with `python3 scripts/research.py "<url>" --refresh`, then add the row to `audit_reviewed.csv`.

After the 10 rows:

```
python3 scripts/validate_data.py --dir data/staging --require-cache
python3 scripts/promote.py <every uid you edited>
bash handoff/check.sh
git add -A && git commit -m "Review 10 audit rows" && git push -u origin claude/magical-dirac-6pfq3g
```

---

## CARD 4: Add one new US university

`next.py` prints the official name and state.

1. **Find which PhDs exist first:** fetch the official list of doctoral programs from the graduate school website. Write down which of these 18 fields have a real PhD: physics, astronomy, chemistry, materials, math, statistics, cs, datasci, biology, biomed, neuro, earth, environment, ece, mech, chemeng, civil, bme. A master's-only program doesn't count.
   - **If none exist**, set the row's `status` in `handoff/us_r1r2.csv` to `screened-out`, write the URL in `handoff/PROGRESS.md`, commit, and stop this card.
2. **Pick an id:** short and lowercase, for example `umassboston`.
3. **Add it to the list** with the helper (never edit the file by hand):
   `python3 handoff/add_university.py <id> "<official name>" "<state name>"`
   If it says the id or name already exists, pick another id, or stop and check `handoff/us_r1r2.csv`.
4. **Do the university rules** (6 values: app_fee, fee_waiver, gre_general, toefl_min, ielts_min, english_waiver). Use the graduate school's admissions pages.
5. **Do each program** (5 values: deadline, gre_subject, supervisor, funding, entry_route). Use the department's own PhD page. `program_page` must be that page.
6. For how to save, copy the example in `data/staging/RESEARCH_BRIEF.md` ("Saving (example)"). Always start the command with `ATLAS_OUT=data/staging`.
7. Finish:
   - In `handoff/us_r1r2.csv`, set this row's `atlas_id` to your id and `status` to `covered`.
   - Then run:
     ```
     python3 scripts/validate_data.py --dir data/staging --require-cache
     python3 scripts/audit_quality.py --dir data/staging
     python3 scripts/promote.py <id>
     bash handoff/check.sh
     git add -A && git commit -m "Add <name> (<id>): N STEM PhD programs" && git push -u origin claude/magical-dirac-6pfq3g
     ```

`audit_quality.py --dir data/staging` must show `generic_page 0` for your university. If it doesn't, fix the program pages before you promote.

**Health-science schools** (`next.py` says so): only do biomed, neuro and bme, plus biology if it has a PhD.

---

## CARD 5: Screen one US university

This is a quick check. Use one or two fetches only.

1. Fetch the university's official list of doctoral or PhD programs.
2. Does it have a PhD in any of the 18 fields from CARD 4?
   - **Yes:** in `handoff/us_r1r2.csv`, change this row's `status` to `add`, then do CARD 4 for it.
   - **No:** change `status` to `screened-out`, and write in `handoff/PROGRESS.md`: `Screened out <name>: no STEM PhD. Source: <url>`.
3. Commit: `Screen <name>`.

---

## CARD 6: Gap-fill one university

`next.py` prints the university with the most `Not stated` values.

1. Run `python3 handoff/research_prompt.py <uid>` and follow what it prints.
2. Fill **only** values that are `Not stated`. Never change a value that already has a quote.
3. Do the 6 university rules first, because one answer fixes every program at that university.
4. Then run:
   ```
   python3 handoff/measure.py <uid>
   python3 scripts/validate_data.py --dir data/staging --require-cache
   python3 scripts/promote.py <uid>
   bash handoff/check.sh
   git add -A && git commit -m "Gap-fill <uid>" && git push -u origin claude/magical-dirac-6pfq3g
   ```
5. **Stop rule:** if 10 gap-fills in a row each changed the overall Not stated number (shown by `bash handoff/check.sh`) by less than 0.1%, stop all gap-fill work. Write `GAP-FILL STALLED at X%` in `handoff/OWNER_REVIEW.md`.

---

## CARD 7: Refresh the business documents (after every 10 universities added)

1. Run `python3 product/build.py`. It updates the store listing and launch messages with the new numbers by itself.
2. Run `python3 scripts/coverage.py` and write down the four numbers it prints: universities, programs, fields, Not stated %.
3. Open `BUSINESS_PLAN_README.md` and fix **only the numbers** in these places:
   - §1: "It covers about 200 universities…".
   - §2, the Dataset row: "The frozen list has 222 universities…". Use the real number from `data/universities.json`.
   - The first line: "Status as of …". Use today's date.
4. Don't change prices, plans, decisions or anything else.
5. Run `python3 -m pytest -q tests`. All tests must pass.
6. Commit: `Refresh business docs with current counts`.

---

## CARD 8: Weekly source check (once a week)

1. Run `python3 scripts/check_sources.py --out ops/source-check-<YYYY-MM-DD>.md`.
2. Open the report. For each row in the table "quoted claims no longer match their source page", add a line to `handoff/OWNER_REVIEW.md`: `CHANGED? <record> <field> <source>`.
3. Don't change data in this card.
4. Commit: `Weekly source check`.

---

## PROGRESS.md line format

Add one line per card, newest at the bottom:

```
2026-11-02 | CARD 4 | Added umassboston (9 programs) | Not stated 20.7% -> 20.8% | commit abc1234
```

## OWNER_REVIEW.md

This is the list of questions for the owner. Add lines. Never delete lines. The owner answers them.
