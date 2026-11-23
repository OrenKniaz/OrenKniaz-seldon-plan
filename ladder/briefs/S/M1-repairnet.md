# RepairNet

I'm Ana, and I coordinate three neighbourhood repair cafés. Maple Library takes lamps and small appliances, Cedar Hall has the sewing crew, and Riverside draws people with bikes. We share 28 volunteers. Last month I carried intake sheets home to count repairs and found the same toaster on two sheets. Nobody remembered which volunteer had it or whether the replacement knob was still on order.

I'd begin with one Saturday at Maple Library. At the front desk, Sam should be able to log Ruth's desk lamp, attach two photos, and hand her a queue number. Noor should see the waiting items and pick up the lamp because she does electrical repairs. If Noor and Eli both reach for it, one of them gets the assignment and the other can see who has it. I'd like to finish the day knowing which items were fixed, which couldn't be repaired, and which are waiting on a part. When a new café opens with zero items, show an empty queue for that event.

Once that Saturday works, I want all three cafés on the same system. Volunteers should be able to list their skills and sign up for shifts. Our coordinators need to schedule events, and desk volunteers need to move the queue along. When the last 3-amp fuse is used at Maple, the next person should see we're out. If I enter a negative parts quantity or attach a file the app can't read as a photo, leave the record as it was and tell me what to fix.

Then I'd like an inbox inside the app for shift reminders and notes when a part arrives. On the first of the month I want a report with items taken in, repair outcomes, and parts used by café, including a café that ran no events. If the Windows host is off overnight, I want reminders that still matter and missing reports to appear when it starts again, without getting the same notice twice.

## Hard constraints

- The app runs on a Windows host using Python, Node, or both. The network's cafés use the host on a private local network.
- No paid services, external email, or network-hosted assets at runtime. Photos, notifications, and reports stay local.
- Individual accounts distinguish coordinators, intake staff, and repair volunteers. Only authorized staff can access item photos or change event settings.
- Event queues, assignments, outcomes, and parts records survive restart in a local SQL database. Parts stock cannot go below zero.
- A background job handles reminders and monthly reports, catches up after downtime, and avoids duplicate notices and reports.
- Record only what we need for intake. Keep customer details and photos out of monthly reports.
