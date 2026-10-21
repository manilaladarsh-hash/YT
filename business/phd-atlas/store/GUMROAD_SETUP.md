# Gumroad setup: your one-time steps (about 45 minutes)

Everything else is ready. These steps need **your** identity, bank and approval, so I can't do them for you. Gumroad's menus move occasionally; if a label differs, search Gumroad's help center for it.

## Before you start (10 min, your judgement)
1. **Confirm you can sell.** Check that your study permit allows off-campus work, and plan to count business hours toward your 24 h/week during terms. If unsure, ask McMaster's International Student Services; it's free. Start logging hours in the *Hours* sheet of `ops/Business-Dashboard.xlsx`.
2. **Decide the public name.** The listing copy says "Built by an IISER → McMaster physics PhD student." Keep it, edit it, or delete that line. It's a credibility signal, but it reveals where you study. Using your legal name as the Gumroad display name avoids registering a business name in Ontario.

## Account (15 min)
1. Create an account at gumroad.com with an email you'll check weekly.
2. **Settings → Payments:** add your bank account (or PayPal if bank deposit isn't offered for Canada), and complete the tax form Gumroad asks for. Finish **identity verification**; third-party reports say unverified accounts face a higher minimum payout.
3. **Settings → Purchasing power parity:** turn it **on** and set the maximum discount to **50%**.

## Product 1: paid kit (10 min)
1. **New product → Digital product.**
2. Name, URL slug, price ($15), summary and description: copy from `store/LISTING_COPY.md`, Product 1.
3. Cover: upload `store/images/cover-paid.png`. Thumbnail: `store/images/thumb-paid.png`.
4. Content/file: upload `dist/Physics-PhD-Atlas-2027-v1.1.zip`.
5. Custom receipt: paste the receipt text from `LISTING_COPY.md`.
6. Refund policy: "14-day no-questions refund."
7. Publish, then buy it once yourself with a 100% discount code (Discounts → new code, 100%, 1 use) to see exactly what customers get. Delete the code afterwards.

## Product 2: free sample (5 min)
1. New digital product with Product 2's text from `LISTING_COPY.md`. Price **$0+**.
2. Cover `store/images/cover-sample.png`, thumbnail `store/images/thumb-sample.png`.
3. File: `dist/Free-Sample-Physics-PhD-Atlas-2027.pdf`.
4. In the description, add a link to Product 1 (paste its URL once it's published).

## Emails (5 min)
**Emails → Workflows:** create the two workflows in `store/EMAILS.md`, "Welcome" (immediately) and "Usefulness check" (10 days after purchase), both triggered by purchase of Product 1.

## Attribution codes (2 min)
**Discounts:** create two codes for Product 1, each **10% off** with no expiry: `NETWORK` and `REDDIT`. The launch messages use them, so you can tell which channel sold. Record each week's code counts in `ops/Business-Dashboard.xlsx`.

## When you're done
Send me the two product URLs (or paste them into `launch/messages/*.md` where it says `{PAID_URL}` and `{SAMPLE_URL}`). Then nothing in launch is blocked except your approval to send the messages.
