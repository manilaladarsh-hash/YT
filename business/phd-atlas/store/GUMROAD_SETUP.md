# Gumroad setup: your one-time steps (about 45 minutes)

Everything else is ready. These steps need **your** identity, bank and approval, so I can't do them for you. Gumroad's menus move occasionally; if a label differs, search Gumroad's help center for it.

## Before you start (10 min, your judgement)
1. **Confirm you can sell.** Check that your study permit allows off-campus work, and plan to count business hours toward your 24 h/week during terms. If unsure, ask McMaster's International Student Services; it's free. Start logging hours in the *Hours* sheet of `ops/Business-Dashboard.xlsx`.
2. **Decide the public name.** The listing copy says "Built by an IISER → McMaster physics PhD student." Keep it, edit it, or delete that line. It's a credibility signal, but it reveals where you study. Using your legal name as the Gumroad display name avoids registering a business name in Ontario.

## Account (15 min)
1. Create an account at gumroad.com with an email you'll check weekly.
2. **Settings → Payments:** add your bank account (or PayPal if bank deposit isn't offered for Canada), and complete the tax form Gumroad asks for. Finish **identity verification**; third-party reports say unverified accounts face a higher minimum payout.
3. **Settings → Purchasing power parity:** turn it **on** and **leave the maximum discount at Gumroad's 60% (no lower cap)**. This is what makes the price affordable in India: Gumroad's discounts run from 20% to 60% and come from World Bank data, and India is expected to get the full 60%. Leave the card-country and IP check on.
4. **Settings → tipping (optional):** turn tipping on so buyers who can afford more can add a tip at checkout. Gumroad's default tip is 0%, so nobody is pushed.

## Product 1: paid kit (10 min)
1. **New product → Digital product.**
2. Name, URL slug, summary and description: copy from `store/LISTING_COPY.md`, Product 1. Set the price to **$5**.
3. **Versions:** add two versions with these exact names and prices: **Personal licence**, $5, and **Batch licence (share with up to 30 students)**, $20. Indian buyers should then see roughly ₹190 and ₹750, in rupees, with UPI offered at checkout. **Before announcing, ask one friend in India to open the link and confirm the rupee price and the UPI option for both versions.** This is the one pricing assumption I couldn't test without an account.
4. Cover: upload `store/images/cover-paid.png`. Thumbnail: `store/images/thumb-paid.png`.
5. Content/file: upload `dist/Physics-PhD-Atlas-2027-v1.1.zip`.
6. Custom receipt: paste the receipt text from `LISTING_COPY.md`.
7. Refund policy: "14-day no-questions refund."
8. Publish, then buy it once yourself with a 100% discount code (Discounts → new code, 100%, 1 use) to see exactly what customers get. Delete the code afterwards.
9. **Student-aid code (2 min):** Discounts → new code `STUDENTAID`, **100% off**, Product 1 Personal licence only, **limited to 20 uses**. Never post it publicly. When a student writes that even ₹190 is a barrier, reply with the "Free copy" template in `store/EMAILS.md`. When it runs out, decide whether to top it up.

## Product 2: free sample (5 min)
1. New digital product with Product 2's text from `LISTING_COPY.md`. Price **$0+**.
2. Cover `store/images/cover-sample.png`, thumbnail `store/images/thumb-sample.png`.
3. File: `dist/Free-Sample-Physics-PhD-Atlas-2027.pdf`.
4. In the description, add a link to Product 1 (paste its URL once it's published).

## Emails (5 min)
**Emails → Workflows:** create the two workflows in `store/EMAILS.md`, "Welcome" (immediately) and "Usefulness check" (10 days after purchase), both triggered by purchase of Product 1.

## Channel tracking (no setup needed)
The launch messages use links ending in `?utm_source=...`. Gumroad creates a UTM link the first time someone uses one, and its UTM-links dashboard shows views, sales and conversion per channel. Discount codes aren't used for tracking: Gumroad's help says PPP and a code don't stack and the bigger discount wins, so a 10% code would change nothing for Indian buyers. Copy each week's per-channel orders into `ops/Business-Dashboard.xlsx`.

## When you're done
Send me the two product URLs (or paste them into `launch/messages/*.md` where it says `{PAID_URL}` and `{SAMPLE_URL}`). I'll fill in the links. The only remaining step is sending the messages from your own WhatsApp, Reddit and LinkedIn accounts, which I can't access.
