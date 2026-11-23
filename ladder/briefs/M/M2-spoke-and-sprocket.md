# M2 — Spoke & Sprocket Workshop

I'm Liat, and I run Spoke & Sprocket in Haifa. We have two mechanics, one service writer, a bookkeeper, and about 35 open repairs in April. The paper tag on a bike tells me who dropped it off. It doesn't tell me whether Dana approved the extra ₪80, whether the last brake rotor was promised to someone else, or whether we already took a deposit. I want us to run a full week from this system, including Friday's handover to Sunday's crew.

## From drop-off to pickup

Noa at the counter finds or creates a customer and bike, records the reported fault, and prints a claim ticket with the order number and promised pickup. A bike can have more than one order over its life. At intake we can leave the price open. Once Eyal diagnoses it, Noa sends a numbered estimate to the customer's portal inbox. Dana can approve or decline it and see exactly what she agreed to. Noa can record a phone decision with who called and when. If the work changes after approval, issue a new revision. Keep the first decision visible, and require approval of the new revision before work on it starts. Show awaiting approval, in progress, waiting for parts, ready, collected, and cancelled on the counter board. A mechanic must record inspection results before marking a bike ready.

## Parts and the work calendar

I receive stock by SKU and supplier reference. Mechanics reserve whole units against approved work, then consume them when fitted. Keep on-hand, reserved, and available counts visible. If two staff try to reserve the last rotor, one reservation succeeds and the other gets the updated availability. Cancelling releases unused reservations. If a mechanic recorded a part as fitted but never used it, returning it to stock needs a reason and a reversing movement. If the inventory count is corrected, keep the original movement and the adjustment.

Our calendar shows shifts and repair slots in Asia/Jerusalem. Noa assigns approved work using its estimated minutes. A mechanic may have several jobs in a day but can't be in two repair slots at once or booked outside a shift. Let us extend or reassign a slot, update the work board, and notify the affected mechanics. Next season we'll have two stands but still only one hydraulic bleed kit. Add kit booking after the basic calendar works. A bleed job then needs both the mechanic and kit free, and earlier jobs keep their existing bookings.

## Invoices and pickup

The bookkeeper issues an invoice from approved work, with labor and parts shown separately. Use the quantity, unit price, discount and tax rate recorded for each line. For our demo use 18% tax and a 10% discount where specified. Round the discounted net line to agorot, then round the tax on that net line, both half up. Three cables at ₪19.95 each with that discount give ₪53.87 net, ₪9.70 tax, and ₪63.57 due. Sum stored line amounts. Record cash, card-terminal and bank-transfer receipts with dates and references. A ₪20 deposit on that invoice leaves ₪43.57. Block excess receipts, allow a refund up to the unreversed receipt amount, and reopen the balance on a refund. Corrections to an issued invoice go through a linked credit and replacement, with the original still printable. The counter can hand over a paid bike or record my named approval for an unpaid pickup.

## Bring over our parts list

Preview UTF-8 CSV with header `sku,name,unit_price_ils,opening_qty`. Prices use a decimal point and exactly two decimal places. Quantities are whole units. Keep downloadable valid and invalid sample files and export rejected rows with the original values, source line number, and reason. In this sample, line 3 fails for negative stock and line 4 duplicates line 2. Apply selected valid rows together, report any existing SKU as a conflict, and make resubmission of the same accepted batch harmless.

~~~csv
sku,name,unit_price_ils,opening_qty
CAB-01,Brake cable,19.95,12
PAD-04,Resin pads,44.50,-2
CAB-01,Shift cable,21.00,5
~~~

I want three reports with printable views and CSVs matching the selected filters. Show turnaround by mechanic and pickup week, stock movements by SKU and date, and invoice balances and receipts by date and payment method. Include the totals and detail rows so I can reconcile a quiet day as well as a busy one. Give customers an in-app notice when an estimate is ready, when the bike is ready, and once at 09:00 the day after a missed pickup. After downtime, deliver the missed reminder once if the bike still qualifies. Let me see the actor, time, reason and before/after values for sensitive changes. I need to undo a mistaken assignment or unused reservation if nothing since then depends on it, with the undo itself visible.

## Who can do what

| Account | Access |
| --- | --- |
| Owner | Manage accounts, rates, shifts, equipment, stock receipts, count corrections and CSV imports. Approve pickup exceptions, undo eligible changes, and access all shop reports and records. |
| Service writer | Manage customers, bikes, intake, estimates, phone decisions, assignments and pickup. Read stock availability and order balances. |
| Mechanic | Read assigned repair details and own calendar. Update diagnosis, work, checks, reservations and consumption on assigned orders. |
| Bookkeeper | Read billable order details. Issue, credit and replace invoices, record receipts and refunds, and export financial reports. |
| Customer | Read own bikes, order status, estimates, invoices and receipts. Respond to own estimates and read own notices. |

## Hard constraints

1. Run on Windows using Python, Node, or both. Serve only localhost or the shop's private LAN.
2. Use local files and locally served assets, with zero paid services or runtime internet dependencies.
3. Persist business records in a local SQL database with versioned migrations that preserve existing data.
4. Use individual logins with salted password hashes, expiring sessions, logout, and session revocation when an account is disabled.
5. Enforce the matrix on the server for pages, writes, reports, and exports. Check customer ownership and mechanic assignment on every relevant request.
6. Keep money exact to the agora and use the stated rounding sequence for both invoices and credits.
7. Commit stock and financial changes atomically with their audit records. Prevent negative stock and duplicate receipts from resubmission.
8. Record payments locally. Leave payment processing, email and SMS outside this release.
9. Run persisted notification jobs with catch-up and duplicate prevention after restart.
10. Support keyboard operation, visible focus, labelled fields, and errors announced on forms and CSV previews.
11. Deliver readable production-quality code and at least one automated end-to-end or integration test per workflow. Cover the last-rotor race, stale estimate, refund and restart cases at the relevant boundary.
12. Supply realistic seed data for each role and a non-developer Windows guide for first launch, backup, restore, and reopening after a restart.
