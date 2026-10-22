# Emails: what works at launch, and what unlocks later

**Gumroad's email lock.** Gumroad says: "You cannot send emails until you've earned $100 after fees and received a payout." This covers Workflows (automated sequences) and email updates to customers ([Workflows help](https://gumroad.com/help/article/131-using-workflows-to-send-automated-updates), [email updates help](https://gumroad.com/help/article/169-how-to-send-an-update)). At $5 or ₹190 a sale, that's roughly 30–100 sales away. So the kit is set up to need no emails:

- **The receipt is the welcome email.** Gumroad sends it automatically with every order, free or paid. Its text, with start steps, how updates work and the one feedback question, is in `LISTING_COPY.md`.
- **Updates need no email.** Replace the ZIP on the product, and every buyer's receipt link and Gumroad Library serve the new file. START-HERE tells buyers this.
- **Your replies are ordinary email.** Answering a buyer who replied to their receipt isn't affected. Use the templates below.

After your first payout, turn on the two workflows at the end of this file. Product 1 is the trigger.

---

## Template: free copy for a student who can't afford it

Hi {name}, of course. Here's a code for a free copy: open {PAID_URL}, choose *Personal licence*, and enter **STUDENTAID** at checkout. It's limited, so please don't share the code; send friends to the free sample instead. Good luck with your applications!

## Template: free copy for a physics club or batch coordinator (optional, code CLUBCOPY)

Hi {name}, thanks for running {club/batch}. Here's a free copy for you: open {PAID_URL}, choose *Personal licence*, and enter **CLUBCOPY** at checkout. No strings attached. If you think it's useful for your batch, the batch licence ($20, about ₹750 in India) lets you share it with up to 30 people. If not, no worries. Good luck to everyone applying this year.

## Template: refund request reply

Hi {name}, no problem. I've refunded your order in full; it can take a few days to show on your card. Thanks for trying the Atlas. If you have a moment, what was missing? It helps me improve it.

## Template: data error report reply

Thanks, {name}. I'm checking {program}'s page now. If it changed, the fix goes into the next update, which will be at the same download link in your receipt.

## Template: reply to the feedback question

Thanks, {name}, that's really useful. {One sentence responding to what they said.} If anything else would have saved you time, tell me and I'll look at it for the next update.

---

## After your first payout: turn these on (Emails → Workflows → "Purchase" trigger, Product 1)

### Workflow 1: Usefulness check (send 10 days after purchase)

**Subject:** One quick question about the Atlas

Hi,

One question, and a one-line reply is perfect:

**What, if anything, did the Atlas change in your applications?** (For example: a program added or dropped, a fee waiver requested, a test booked or skipped, a supervisor emailed.)

And one yes/no: **did checkout work on your first try?**

Your answers decide what goes into the next update. If it wasn't useful, tell me and I'll refund you; you have 14 days.

Thanks,
{your first name}

### Workflow 2: Free-sample follow-up (send 2 days after a Product 2 download, filtered to "has not yet bought" Product 1)

**Subject:** The rest of the Atlas, if it helps

Hi,

You downloaded the free 10-program sample of the Physics PhD Atlas. If it was useful, the full kit covers {N} programs in the US, UK, Europe, Australia and Canada. It includes an offline explorer that shows fees in rupees, a planner sheet with deadline countdowns, and the playbook. It's about ₹190 in India: {PAID_URL}

If it wasn't useful, reply and tell me why. That's useful too.

{your first name}

### Template: data update (Emails → New email → customers of Product 1)

**Subject:** Atlas update v{X.Y}: {what changed in a few words}

Hi,

A new version of the Atlas is at your usual download link (your receipt or Gumroad Library).

What changed:
- {program}: {field} is now {new value} (source checked {date})
- Added: {programs}

Re-download the ZIP to get it. Your workbook shortlist won't carry over automatically, so copy your column A choices into the new file.
