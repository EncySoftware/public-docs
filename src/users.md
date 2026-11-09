# What your users see

This page follows a user from the catalog to your extension running in the CAM system, so that you
know what your customers experience and what to tell them.

## In the catalog

Users browse the store website or the **Extensions** tab of the CAM system and filter by **Free**
and **Paid**. The button on a card says what awaits them:

- **Install** — a free extension;
- the lowest price, for example **$10/month** — an extension on sale;
- **Price not set** — an extension with a licence check whose author has not priced it yet:
  nobody can take a trial or buy it until then;
- **View** — a licensed extension given away free.

The card itself shows every plan, the licence of the CAM system a gated extension requires, and
the minimum version of the CAM system. A version newer than the user's CAM system is a warning,
not a block.

## Trial

A signed-in user takes a trial with **Get N-day trial · then $X**: the length is the one you set,
from 14 to 30 days, and the button names the price that follows. No card is needed, and nothing
is charged when the trial ends. A trial is issued once per account and extension, and only while
the extension is in the catalog and has a price. The card then shows when the trial ends and
offers **Install in ENCY**; the **Buy** button stays. When the trial is over, the card says so
and the user buys.

## Free for ENCY resellers and the ENCY team

If you ticked these groups in the price window, their members see **Get it free as an ENCY
reseller** or **Get it free as ENCY team** instead of the trial. They get a licence for a year,
renewed when they sign in while they stay in the group.

## Purchase

1. The user picks a plan — **One-time**, **Monthly** or **Yearly** — and clicks **Buy** or
   **Subscribe**, before the trial or after it.
2. Payment goes through Stripe Checkout, by card, in US dollars; the store never sees the card.
3. Back in the store, the card says **You own this extension** and offers **Install in ENCY**.

Each purchase is one licence for the buyer's own account.

A yearly plan is sold only to users whose licence of the CAM system covers the whole year ahead;
others choose monthly or one-time. Nobody can buy the same extension twice or hold two
subscriptions to it.

If the payment went through but the licence has not arrived yet, the card says **the licence is on
its way** and updates by itself.

## Installation and updates

**Install in ENCY** opens the CAM system on the user's machine, starting it if needed, and installs
the extension. **Download .nupkg** gives the package file, to install from the **Extensions** tab
or to take to a machine without internet.

The licence belongs to the user's account: the CAM system must be signed in to the same account.
Once the licence is on the machine, the extension works without a connection to the store;
renewals arrive online.

A purchase covers every later version: updates appear on the **Extensions** tab and install
without paying again.

## Subscriptions

A subscription renews every month or year from the day of purchase.

- **A failed payment.** The subscription shows **Payment failed**, and the extension keeps working
  while Stripe retries, for up to 22 days. A successful retry restores everything; if all retries
  fail, the subscription ends and the licence with it.
- **Cancellation.** **Manage billing** in **My subscriptions** opens the Stripe portal, where the
  user changes the card, downloads invoices or cancels. A cancelled subscription works until the
  end of the paid period.

## Refunds

Users ask the store team for a refund; there is no refund button. A full refund ends the
purchase: the licence is revoked, and a subscription stops at once. A partial refund leaves the
licence in place. Either way, your share of the refunded amount comes off your balance (see
[Selling and payouts](paid-extensions.md#your-share)).

## The user's account

| Section | What it shows |
|---|---|
| **My licenses** | Every licence, trial or full, with its state and end date |
| **My payments** | Purchases and every charge: first payment, renewals, refunds |
| **My subscriptions** | Plan, amount paid so far, next payment, **Manage billing** |

## When you change something

| You… | Users |
|---|---|
| Change the price | New buyers pay the new price; running subscriptions keep theirs |
| Change the trial | New trials get the new length |
| Untick a plan | It disappears for new buyers; subscriptions bought on it keep renewing |
| Make it **Free** | Anyone can take a free perpetual licence |
| Remove it from the catalog | Installed copies and licences keep working; nobody new can buy it or take a trial |
| Publish a new version | Owners of a licence update it free of charge |
