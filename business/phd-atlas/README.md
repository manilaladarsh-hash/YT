# Physics PhD Atlas 2027

A low-input online business: a verified, source-cited guide to 40 physics PhD programs in the US, Canada and Europe for international applicants (mostly from India). It is sold as an instant download on Gumroad, with a free sample as the lead magnet.

**Status (2026-10-21):** product built and tested. **Not launched.** There are no customers, sales or revenue yet. Launch needs the owner actions below.

## What's here

| Folder | Contents |
|---|---|
| `research/` | Opportunity comparison with sources, validation plan and gates, business design, financial model (`financials.py`) |
| `data/` | 40 program records (21 US, 10 Canada, 9 Europe) (`programs/*.json`): each value has an exact official quote, URL and date. Also the schema and source manifest |
| `scripts/` | `research.py` (fetch and extract), `validate_data.py` (schema check, plus proof that every quote appears on its page), `check_sources.py` (weekly change detection), `rec.py` |
| `product/` | `build.py` builds everything into `dist/`; templates and content (playbook, start-here, licence) |
| `dist/` | **The deliverables.** `Physics-PhD-Atlas-2027-v1.1.zip` (upload to Gumroad) and `Free-Sample-Physics-PhD-Atlas-2027.pdf` |
| `store/` | Gumroad setup steps, listing copy, policies, emails, cover and thumbnail images |
| `launch/` | Launch plan with experiments, budgets and success criteria, exact message drafts, experiment log |
| `ops/` | Weekly checklist, maintenance schedule, expenses, support playbook, `Business-Dashboard.xlsx` (actuals, gates, forecast, hours) |
| `tests/` | End-to-end tests: data, ZIP, PDFs, offline explorer in Chromium, workbook formulas recalculated in LibreOffice |

## Your remaining actions (about 3 hours in total, once)

1. **Confirm eligibility (10 min):** check that your study permit allows off-campus work, and log business hours in `ops/Business-Dashboard.xlsx` → *Hours* (self-employment counts toward the 24 h/week limit).
2. **Review the kit (60–90 min):** open `dist/Physics-PhD-Atlas-2027/Atlas.html` and `Playbook.pdf`. Spot-check 5 values against the official pages. Edit or remove the "Built by an IISER → McMaster physics PhD student" line if you prefer (`store/LISTING_COPY.md`, `store/render_images.py`).
3. **Gumroad (45 min):** follow `store/GUMROAD_SETUP.md` (account, payout, tax form, PPP on at 60%, two products, $5 personal / $20 batch versions, two email workflows, one `STUDENTAID` code). Then ask a friend in India to confirm they see about ₹190 and a UPI option.
4. **Approve and send messages (30 min):** paste your two Gumroad URLs into `launch/messages/*.md`, then send E1 and E2 (see `launch/LAUNCH_PLAN.md`).
5. **Activate the weekly source watch:** merge this branch into the repo's default branch. Scheduled GitHub Actions only run from there. Ask me to open a pull request if you want.

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
