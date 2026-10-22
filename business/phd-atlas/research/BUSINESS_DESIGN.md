# Business design: Physics PhD Atlas 2027

## Customer
Self-directed final-year BS-MS, MSc or BSc physics and astronomy students applying to PhD programs for 2027 entry, mainly in the US, UK, Europe and Australia, with Canada secondary (owner's market knowledge, 2026-10-22). Most are in India (IISERs, IITs, IISc, NISER, central and state universities); there are secondary buyers in other countries. They are budget-conscious and often unaware of rules specific to international applicants.

## Problem
Each program publishes its own rules on different pages, and some of them contradict each other. The details that matter most to international applicants are the hardest to find:
- which programs waive fees for internationals;
- whether an English-medium Indian degree waives the English test;
- whether the Physics GRE is required this year;
- whether Canada requires a supervisor before admission, or a European program hires through advertised positions;
- whether a master's is needed first.

Getting these wrong costs $75–155 per application, missed deadlines, or a rejected file.

## Offer (v1.1)
| Component | What it does |
|---|---|
| Atlas.html | Offline explorer covering 100+ programs (US, UK, rest of Europe, Australia, Canada) and 10 fields each. Every value shows the exact official quote and link. Quick picks, fees in ₹ and a days-left countdown. |
| Atlas.xlsx | Planner: auto-filling shortlist, deadline countdown, fee budget by currency, recommender tracker, supervisor-outreach log, full sources sheet. |
| Atlas.csv | Raw data. |
| Playbook.pdf | 11 pages: timeline, English-test rules, GRE strategy, Canadian supervisors, how Europe differs (positions, fees, master's-first rules), email template, SOP framework, letter kit, ethical fee-waiver requests, checklist. |
| Free sample | 10 programs (US, Canada, Europe) plus "6 things international applicants miss". |
| Updates | Free for the Fall 2027 cycle, delivered by Gumroad's update emails. |

**Out of scope:** visa or study-permit advice (official links only), SOP writing or editing, and admission predictions.

## Differentiation
1. **Primary-source verification.** Every value carries the quote it came from, the URL and the date, and a script proves each quote exists on the page. No competitor found offers this.
2. **Fields aimed at international applicants** that free directories omit.
3. **Honest uncertainty.** "Not stated", "year inferred" and "sources conflict" are shown instead of guesses.
4. **Founder credibility.** It is built by an IISER → McMaster physics PhD student (your approval needed to show this publicly).
5. **Works offline**, and costs a fraction of one application fee.

## Pricing (owner decision 2026-10-21: affordable for Indian students first)
- **Personal licence: $5.** Gumroad's purchasing-power parity is on at its full 60% maximum. India's World Bank PPP factor (~22 INR per international dollar) is far below the market exchange rate (about 94.5 INR per USD; Bank of Canada, Oct 21, 2026), so Indian buyers are expected to pay about **$2 (≈₹190)**, shown in rupees, with **UPI** available at checkout (Gumroad help, checked Oct 21, 2026). That's under 3% of one US application fee.
- **Batch licence: $20** (about ₹750 in India), shared with up to 30 people in one batch, society or mentoring group, so about ₹25 per student. This tier keeps the per-student price tiny while letting one purchase cover many students.
- **Why not cheaper:** Gumroad takes 10% + $0.50 per sale, plus 2.9% + $0.30 card processing. A $2 sale nets about $0.94; a ₹99 sale (about $1.05) would net about $0.11.
- **Free tiers:** the 10-program sample is free for everyone, and a free full copy goes to any student who says they can't afford it (single code `STUDENTAID`, 20 uses at a time).
- **Tips:** Gumroad's tipping is on (default 0%) for buyers who can afford more.
- 14-day no-questions refund.

## Delivery process (automated)
1. The buyer pays on Gumroad, which acts as merchant of record and handles sales tax, VAT and GST.
2. Gumroad sends the receipt and ZIP download instantly.
3. Workflow emails go out automatically: welcome with a quick start (day 0), then the usefulness and checkout survey (day 10).
4. Data refreshes are uploaded as new versions, and existing buyers get them through the same receipt link. Gumroad emails ("Send update") unlock only after the first $100 payout, so they are an extra, not the delivery route.
5. A weekly GitHub Action re-checks every cited page and opens an issue if a quote disappears.

## Acquisition
| Channel | Mechanism | Owner time | Cost |
|---|---|---|---|
| A. Your network | ~10 personal messages plus 1–3 group posts (exact drafts) | 20–30 min once | $0 |
| B. Reddit | Value-first posts linking the free sample, within each subreddit's rules | 10 min plus replies | $0 |
| C. Gumroad Discover | Passive marketplace listing | 0 | 30% fee on those sales |
| D. Next season | Free static SEO site (one page per program) on GitHub Pages | Build by me | $0 |

## Financial scenarios
Run with `python3 research/financials.py`. Assumptions are in the script's header. Only Gumroad's 10% + $0.50 and 30% Discover fees are published facts; everything else is an assumption.

| Scenario | This season (orders → net) | Next full season (orders → net) | Key assumptions |
|---|---|---|---|
| Conservative | 10 → **$13** | 50 → **$65** | 80% buy at the India/PPP price, 8% refunds, no Discover sales |
| Base | 40 → **$59** | 200 → **$296** | 75% PPP, 5% refunds, 5% via Discover |
| Optimistic | 120 → **$196** | 600 (three editions) → **$981** | 70% PPP, 4% refunds, 10% via Discover |

Per sale: $5 nets $3.56 and $2 (India) nets $0.94. All scenarios assume:
- card processing of 2.9% + $0.30 on direct sales, as Gumroad's help states, with UPI assumed to cost the same;
- on refunds, Gumroad returns its fee but keeps processing;
- a 2% currency cost on payout to a Canadian bank account;
- $0 fixed costs and $0 customer-acquisition cash (your hours are counted instead).

Batch licences aren't in the model; each one adds about $2.50–15 net, depending on the buyer's country.

**What this means:** at student-friendly prices this is a small, mission-first business, roughly $60–300 a season in the base case. Gumroad pays out once your balance reaches $100, and a new account's first payout review typically needs 3–4 sales and a balance over $100 (Gumroad help). The upside comes from reach (batch licences through student societies and every future edition), not from price.

Income is reported on your T2125. There is no GST/HST registration while you stay under the CAD 30,000 small-supplier threshold; confirm with CRA guidance or an accountant.

## Why this model fits your time limit
There is no inventory, no live service and no meetings. Support is a short FAQ plus email at ≤30 min/week. Data maintenance is automated detection plus a ~30-minute monthly refresh I can do in a session, with you approving the upload. The weekly checklist is in `ops/WEEKLY_CHECKLIST.md`.
