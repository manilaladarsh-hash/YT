# Physics PhD Atlas 2027

A low-input online business: a verified, source-cited guide to 100+ physics PhD programs in the US, UK, Europe, Australia and Canada for international applicants (mostly from India). It is sold as an instant download on Gumroad, with a free sample as the lead magnet.

**Status (2026-10-22):** v1.2 (106 programs) is built, tested and **ready to launch**. There are no customers, sales or revenue yet. Launch needs only the owner actions below. UK/Australia additions follow as a free v1.3 (target Nov 5). A Gemini deep-research audit was checked claim by claim (`research/AUDIT_RESPONSE.md`).

## What's here

| Folder | Contents |
|---|---|
| `research/` | Opportunity comparison with sources, validation plan and gates, business design, financial model (`financials.py`) |
| `data/` | One record per program (`programs/*.json`), each value with an exact official quote, URL and date. Also the schema, exchange rates (`fx.json`), source manifest, and incomplete records in `pending/` |
| `scripts/` | `research.py` (fetch and extract), `validate_data.py` (schema check, plus proof that every quote appears on its page), `check_sources.py` (weekly change detection), `rec.py`, `import_saved_page.py` (for pages that block automated reads: save in your browser, upload, import) |
| `product/` | `build.py` builds everything into `dist/`; templates and content (playbook, start-here, licence) |
| `dist/` | **The deliverables.** `Physics-PhD-Atlas-2027-v1.2.zip` (upload to Gumroad; built locally and sent to you in chat, not stored in git so the public repo doesn't give it away) and `Free-Sample-Physics-PhD-Atlas-2027.pdf` |
| `store/` | Gumroad setup steps, listing copy, policies, emails, cover and thumbnail images |
| `launch/` | Launch plan with experiments, budgets and success criteria, exact message drafts, experiment log |
| `ops/` | Weekly checklist, maintenance schedule, expenses, support playbook, `Business-Dashboard.xlsx` (actuals, gates, forecast, hours) |
| `tests/` | End-to-end tests: data, ZIP, PDFs, offline explorer in Chromium, workbook formulas recalculated in LibreOffice |

## Your remaining actions (about 3 hours in total, once)

0. **Make this repo private (1 min):** GitHub → Settings → General → Danger Zone → Change visibility → Private. The old v1.1 ZIP is still in the git history.
1. **Confirm eligibility (10 min):** check that your study permit allows off-campus work, and log business hours in `ops/Business-Dashboard.xlsx` → *Hours*. Self-employment counts toward the 24 h/week limit; treat it as applying all year.
2. **Review the kit (60–90 min):** open `dist/Physics-PhD-Atlas-2027/Atlas.html` and `Playbook.pdf`. Spot-check 5 values against the official pages. Edit or remove the "Built by an IISER → McMaster physics PhD student" line if you prefer (`store/LISTING_COPY.md`, `store/render_images.py`).
3. **Gumroad (45 min):** follow `store/GUMROAD_SETUP.md`. It covers:
   - the account, under **your full legal name**;
   - payout and the tax form;
   - PPP on at 60%;
   - two products, with $5 personal / $20 batch versions;
   - the custom receipt text;
   - the `STUDENTAID` code.

   There are no email workflows yet, because Gumroad locks emails until your first payout. Then ask a friend in India to confirm they see about ₹190 and a UPI option.
4. **Approve and send messages (30 min):** send me your two Gumroad URLs (or paste them into `launch/messages/*.md`), then send E1, E2 and E5 (see `launch/LAUNCH_PLAN.md`).
5. **Optional (10 min):** save the Oxford DPhil Physics, UCL Physics PhD and Michigan Physics admissions pages in your browser (Ctrl+S → "Webpage, HTML only") and upload them in chat. I'll add those programs in v1.3.

The weekly source watch is already active: this folder is merged into `main`.

After that, the weekly routine takes ~20–30 min (`ops/WEEKLY_CHECKLIST.md`).

## Rebuild and test

```bash
cd business/phd-atlas
python3 scripts/validate_data.py           # 0 errors required
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
