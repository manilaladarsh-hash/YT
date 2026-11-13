# STEM PhD Atlas 2027

A low-input online business: a verified, source-cited guide to PhD programs in every STEM field (about 200 universities in the US, UK, Europe, Canada and Australia) for international applicants, mostly from India. It is sold as an instant download on Gumroad, with a free sample as the lead magnet.

**Status (2026-10-24):** the physics-only v1.2 is being overhauled into the STEM edition (v2.0): two-level data (university-wide rules plus department rules), one research agent per university, a rebuilt explorer that checks every program against the buyer's situation, and a plan with calendar export. **Launch is paused until the release gate passes** (≥180 universities, ≥12 fields, Not stated under 15% overall and 25% per field; `python3 scripts/coverage.py --gate`). There are no customers, sales or revenue yet.

## What's here

| Folder | Contents |
|---|---|
| `research/` | Opportunity comparison with sources, validation plan and gates, business design, financial model (`financials.py`) |
| `data/` | Schema 2.0: `universities/<uid>.json` (graduate-school rules shared by every department) and `programs/<uid>--<field>.json` (department rules and overrides). Every value has an exact official quote, URL and date. Also `fields.json` (taxonomy), `universities.json` (frozen list), exchange rates and `staging/` (research drafts and the agent brief) |
| `scripts/` | `research.py` (fetch and extract), `validate_data.py` (schema check, plus proof that every quote appears on its page), `check_sources.py` (weekly change detection), `coverage.py` (progress and release gate), `promote.py` (staging → data), `rec.py`, `import_saved_page.py` (for pages that block automated reads: save in your browser, upload, import) |
| `product/` | `build.py` builds everything into `dist/`; templates and content (playbook, start-here, licence) |
| `dist/` | **The deliverables.** `STEM-PhD-Atlas-2027-v2.0.zip` (upload to Gumroad; built locally, not stored in git so the repo doesn't give it away) and `Free-Sample-STEM-PhD-Atlas-2027.pdf` |
| `store/` | Gumroad setup steps, listing copy (`LISTING_COPY.md`, generated from `LISTING_COPY.src.md` by the build so every figure matches the data), policies, emails, cover and thumbnail images |
| `launch/` | Launch plan with experiments, budgets and success criteria, message drafts (generated from `messages/*.src.md`), experiment log |
| `ops/` | Weekly checklist, maintenance schedule, expenses, support playbook, `Business-Dashboard.xlsx` (actuals, gates, forecast, hours) |
| `tests/` | End-to-end tests: data, ZIP, PDFs, the offline explorer in Chromium (fit engine against the rules, My plan, .ics, phone layout, load time on a slow CPU, 5 MB budget), workbook formulas recalculated in LibreOffice |

## Your remaining actions (once the release gate passes; about 3 hours in total)

0. **Make this repo private (1 min):** GitHub → Settings → General → Danger Zone → Change visibility → Private. The old v1.1 ZIP is still in the git history.
1. **Confirm eligibility (10 min):** check that your study permit allows off-campus work, and log business hours in `ops/Business-Dashboard.xlsx` → *Hours*. Self-employment counts toward the 24 h/week limit; treat it as applying all year.
2. **Review the kit (60–90 min):** open `dist/STEM-PhD-Atlas-2027/Atlas.html` and `Playbook.pdf`. Spot-check 5 values against the official pages. Edit or remove the "Built by an IISER → McMaster physics PhD student" line if you prefer (`store/LISTING_COPY.src.md`, `store/render_images.py`).
3. **Gumroad (45 min):** follow `store/GUMROAD_SETUP.md`. It covers:
   - the account, under **your full legal name**;
   - payout and the tax form;
   - PPP on at 60%;
   - two products, with $5 personal / $20 batch versions;
   - the custom receipt text;
   - the `STUDENTAID` code.

   There are no email workflows yet, because Gumroad locks emails until your first payout. Then ask a friend in India to confirm they see about ₹190 and a UPI option.
4. **Approve and send messages (30 min):** send me your two Gumroad URLs (or paste them into `launch/messages/*.md`), then send E1, E2 and E5 (see `launch/LAUNCH_PLAN.md`).
5. **Optional (10 min):** some universities block automated reads (for example Oxford, UCL, Michigan). When I list them, save their admissions pages in your browser (Ctrl+S → "Webpage, HTML only") and upload them in chat, and I'll import them.

The weekly source watch is already active: this folder is merged into `main`.

After that, the weekly routine takes ~20–30 min (`ops/WEEKLY_CHECKLIST.md`).

## Rebuild and test

```bash
cd business/phd-atlas
python3 scripts/validate_data.py --require-cache   # 0 errors required
python3 scripts/coverage.py --gate         # release gate
python3 product/build.py                   # builds dist/
python3 store/render_images.py             # cover and thumbnail PNGs
python3 ops/build_ops_workbook.py          # owner dashboard
python3 -m pytest -q tests                 # end-to-end checks
python3 scripts/check_sources.py           # live check of every cited page
```

Requirements: Python 3 with `openpyxl requests beautifulsoup4 lxml pytest`; Node with Playwright and Chromium (for PDFs and the browser test); `pandoc`, `pdftotext`; LibreOffice (optional, for the formula test).

## Honesty rules this business runs on
- Every published program value is tied to an official quote. Unknowns are labelled, never guessed.
- Forecasts live in `research/financials.py` and the *Forecast* sheet. Actuals go only in *Weekly actuals*.
- No invented customers, testimonials or sales. No messages sent or money spent without the owner's approval.
