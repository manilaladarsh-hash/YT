# Gumroad setup: your one-time steps (about 45 minutes)

Everything else is ready. These steps need **your** identity, bank and approval, so I can't do them for you. Gumroad's menus move occasionally; if a label differs, search Gumroad's help center for it.

## Before you start (10 min, your judgement)
1. **Confirm you can sell.** Check that your study permit allows off-campus work. Count every business hour (building, posting, emails) toward your 24 h/week off-campus limit. Thesis-based graduate students usually have no scheduled summer break, so treat the limit as applying **all year**. If unsure, ask McMaster's International Student Services; it's free. Log hours in the *Hours* sheet of `ops/Business-Dashboard.xlsx`.
2. **Sell under your full legal name.** Set the Gumroad name (Settings → Profile) to your full legal name exactly, and use "STEM PhD Atlas 2027" only as the product title.
   - Under Ontario's Business Names Act, a sole proprietor trading under their own full name doesn't register anything.
   - Trading under any other name (for example "STEM PhD Atlas" as the shop name) needs a business-name registration, and not registering can bring a fine of up to $2,000.
3. **Decide the credibility line.** The listing copy says "Built by an IISER → McMaster physics PhD student." Keep it, edit it, or delete it. It's a credibility signal, but it reveals where you study.

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
5. Content/file: upload `dist/STEM-PhD-Atlas-2027-v2.0.zip` (I've also sent it to you in chat).
6. Custom receipt: paste the receipt text from `LISTING_COPY.md`.
7. Refund policy: "14-day no-questions refund."
8. Publish, then buy it once yourself with a 100% discount code (Discounts → new code, 100%, 1 use) to see exactly what customers get, including the receipt. Delete the code afterwards, but **keep that test purchase**. When an update ships, replace the ZIP and open your own receipt link to confirm it serves the new version. That's how buyers get updates while Gumroad emails are locked (see below).
9. **Student-aid code (2 min):** Discounts → new code `STUDENTAID`, **100% off**, Product 1 Personal licence only, **limited to 20 uses**. Never post it publicly. When a student writes that even ₹190 is a barrier, reply with the "Free copy" template in `store/EMAILS.md`. When it runs out, decide whether to top it up.
10. **Club-coordinator code (optional, 1 min):** `CLUBCOPY`, 100% off, Personal licence only, **10 uses**. It's for student-society or batch coordinators you message under experiment E6 in `launch/LAUNCH_PLAN.md`. It's a free copy with no obligation, and you never ask for a review in return.

## Product 2: free sample (5 min)
1. New digital product with Product 2's text from `LISTING_COPY.md`. Price **$0+**.
2. Cover `store/images/cover-sample.png`, thumbnail `store/images/thumb-sample.png`.
3. File: `dist/Free-Sample-STEM-PhD-Atlas-2027.pdf`.
4. In the description, add a link to Product 1 (paste its URL once it's published).

## Emails (nothing to set up at launch)
Gumroad says: "You cannot send emails until you've earned $100 after fees and received a payout." So Workflows and update emails are locked at first. The kit doesn't depend on them:
- The **custom receipt** (step 6) carries the start steps, the update note and the one feedback question.
- **Updates** reach buyers through their existing download link.

After your first payout, create the two workflows at the end of `store/EMAILS.md`.

## If the India check fails (no rupee price or no UPI)
Do these in order, and stop at the first that works:
1. **Check the settings.** Confirm PPP is on with no lower cap (Account step 3), and ask your friend to retry without a VPN, with an Indian card or Indian IP.
2. **Tell buyers the other ways to pay.** Add one line to the listing: "If UPI doesn't show, pay by card with international transactions switched on in your banking app, or by PayPal." RBI rules switch international transactions off by default on cards issued since 2020.
3. **Use the free-copy route** for anyone who still can't pay: the STUDENTAID template.
4. **A second, India-only store (last resort).** Topmate's own pages say creators outside India can withdraw by PayPal or to a US bank. But before using it, get Topmate support to confirm **in writing** that Topmate charges and remits India's GST on your sales.
   - A seller outside India who sells digital products straight to Indian consumers generally has to register for Indian GST, with no threshold, unless the platform counts as the supplier.
   - Topmate wouldn't carry your Gumroad updates or licence versions, so you'd send updates by hand.
5. **Never** sell through Instamojo, Razorpay or another Indian gateway into an Indian bank account. As a non-resident Indian, keep this income out of resident Indian accounts and ask a CA before changing that.

## Channel tracking (no setup needed)
The launch messages use links ending in `?utm_source=...`. Gumroad creates a UTM link the first time someone uses one, and its UTM-links dashboard shows views, sales and conversion per channel. Discount codes aren't used for tracking: Gumroad's help says PPP and a code don't stack and the bigger discount wins, so a 10% code would change nothing for Indian buyers. Copy each week's per-channel orders into `ops/Business-Dashboard.xlsx`.

## When you're done
Send me the two product URLs (or paste them into `launch/messages/*.md` where it says `{PAID_URL}` and `{SAMPLE_URL}`). I'll fill in the links. The only remaining step is sending the messages from your own WhatsApp, Reddit and LinkedIn accounts, which I can't access.
