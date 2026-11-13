# Validation plan: Physics PhD Atlas 2027

Desk research is not customer validation. Everything below the "Customer tests" heading needs real people, real money, and your approval before anything is sent or published.

## Assumptions most likely to kill the business

| # | Assumption | Why it might fail | Cheapest test | Signal |
|---|---|---|---|---|
| A1 | Applicants will pay about ₹190 (India, via Gumroad PPP) to $5 when free sources exist | Reddit, GradCafe and department pages are free | Live paid listing next to a free sample | Paid orders; sample-to-paid conversion |
| A2 | We can reach applicants late in the season with no audience | Many lists are already final by November | One network message plus one Reddit post, each with its own UTM-tagged link | Views, downloads and orders per channel |
| A3 | Indian buyers can complete checkout and see the rupee price | Cards issued since 2020 have international online use off by default (RBI); PPP or UPI might not show as expected | Before launch, a friend in India opens the link and confirms the rupee price and the UPI option. Then the day-10 survey question | Friend's check; survey answers; "payment failed" emails; share of orders from India |
| A4 | The data stays accurate cheaply | Programs edit pages mid-cycle | Weekly `check_sources.py` via GitHub Actions; error-report channel | Missing-quote count; reported errors |
| A5 | The kit changes real decisions | Buyers may already know it all | One-question survey ("What did the Atlas change?") | ≥2 concrete benefits reported |
| A6 | You can lawfully sell under your study permit | Off-campus work conditions and hours | You confirm your permit conditions; log hours in the *Hours* sheet of `ops/Business-Dashboard.xlsx` | Done before the first sale |

## Desk research completed (not validation)

- Competitor scan, price anchors and market size (see `OPPORTUNITY_RESEARCH.md`).
- 100+ programs (US, UK, rest of Europe, Australia, Canada) verified against official pages, with exact quotes, all passing `validate_data.py`.
- The product works end to end in tests (`tests/`, 18 automated checks).

## Customer tests (need your approval to run)

| Test | What | Cost | Your time | Window |
|---|---|---|---|---|
| T1a | Gumroad live: paid kit ($5 / about ₹190 in India; $20 batch licence) plus free 10-program sample | $0 | 45 min setup | From launch |
| T1b | Personal messages to ~10 people you know who are applying or mentoring applicants (exact drafts in `launch/messages/`) | $0 | 20 min | Week 1 |
| T1c | Reddit post leading with free value, within each subreddit's rules (drafts provided) | $0 | 10 min plus replies | Week 1–2 |
| T2 | Feedback question in the purchase receipt and START-HERE ("What did the Atlas change for you?"); a day-10 Gumroad workflow is added once emails unlock after the first payout | $0 | 5 min/week to read | Ongoing |
| T3 | Same email asks whether checkout worked | $0 | n/a | Ongoing |

## Limits before meaningful evidence is required

- **Cash:** $0 needed. A hard cap of **$30** applies this cycle for anything unforeseen, and only with your approval. No ads in v1.
- **Your time:** ≤3 h before launch; ≤1 h/week after. Everything is logged in the *Hours* sheet of `ops/Business-Dashboard.xlsx`.
- **Calendar:** launch when the release gate passes. Gate review **6 weeks after launch**, no later than **Jan 15, 2027**. Season closes **Jan 15, 2027**.

## Decision rules (gate review, 6 weeks after launch)

- **Proceed** (plan a 2028 edition, chemistry/maths editions, an SEO site) only if **all** of these hold:
  - ≥10 paid orders
  - ≥2 **unrelated** retained purchases (buyers with no prior connection to you, kept past the 14-day refund window)
  - refund rate ≤10%
  - ≥2 buyers report a concrete benefit
  - 0 critical data errors
- **Change** the offer, price or channel and run one more 3-week cycle if there are ≥50 sample downloads or ≥500 product views but fewer than 5 paid orders, or if sales come only from people you know. The price is already near Gumroad's practical floor (about $2 in India; below that its $0.80 fixed fees take nearly everything), so the options are channel and offer changes: push the batch licence through student societies, or move to pay-what-you-want with a $2 floor.
- **Stop** if, after both channels have actually run, there are under 20 sample downloads and 0 unrelated paid orders. Leave the listing up passively, build nothing more, and record the lessons in Notion.

## What will not count as validation

Page views, likes, compliments, friends buying to support you, passing tests, or the number of programs in the dataset.
