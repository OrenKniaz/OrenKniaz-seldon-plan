# M3 — Bridge Music Schools

I'm Yael, and I manage the office at Bridge Music in Jerusalem. We're sharing a Windows host with North Strings in Haifa and Valley Music in Afula. Each school runs its own office, teachers, family accounts, and books. Together that's about 430 students and 29 teachers. A parent with children at two schools should be able to sign in once and switch schools. I should be able to export Jerusalem's overdue balances without ever seeing those other schools' families.

## Open one school and move in the roster

Give the host operator a way to create a school and its first administrator. The administrator sets the school calendar, rooms, fees, and staff memberships. A household may have two guardians, and a student can have one guardian allowed to see billing and another who sees lessons only. Keep family and teacher records school-specific even when they share a login email.

Our legacy roster uses UTF-8 CSV with header `family_ref,guardian_email,student_ref,student_name,instrument,start_date`. References are required and unique within the school for their record type. A family reference can repeat across students if its guardian matches. Dates are ISO calendar dates. Bring in family and student records together and link guardians by email after the administrator reviews the preview. New guardians get an activation code the office can hand over. Existing users keep their credentials. The second data row below conflicts on family email and the third uses an impossible date. The error CSV keeps the source row number, original fields, and all reasons. Confirm only selected valid rows in a single commit. If a record changed since preview, ask for a new preview. Replaying a confirmed batch must leave the roster and memberships as they were. Undo an unused batch with one audited reversal. If any record has since acquired lessons, payments or changed membership, show the blocking references and leave the batch alone.

~~~csv
family_ref,guardian_email,student_ref,student_name,instrument,start_date
F018,rin@example.test,S091,Rin Levi,Cello,2027-01-05
F018,other@example.test,S092,Ori Levi,Violin,2027-01-05
F020,ari@example.test,S095,Ari Bar,Piano,2027-02-30
~~~

## Run a school week

Schedule a weekly series through a term end date. A room and a teacher can't be booked twice at the same school. Keep a 16:30 lesson at 16:30 local time across daylight-saving changes, skip school closure dates, and tell the scheduler which dates conflict before saving. Let the scheduler move one occurrence, cancel one, or change this and future occurrences. Preserve earlier attendance and billing. Show whether future exceptions are kept or superseded before saving a series change. The teacher sees today's roster and marks present, school cancellation, or student absence. A correction needs a reason. A school-cancelled lesson earns a make-up credit good through term end. Booking a make-up uses the credit once, and cancelling that booking releases it while it's still valid.

Next term we'll share Tamar between Haifa and Afula. After each school's basic calendar works, give those two administrators a way to link her existing staff memberships, with Tamar's acceptance, and agree to a 45-minute travel buffer between sites. Both schedulers see blocked times, with no other school's names or details. If they book at the same time, the first confirmed booking holds the shared slot.

## Close a month

Our families pay per scheduled lesson, including student absences. School cancellations and make-ups cost zero. On the first local day of the next month, prepare draft statements per family for the closed month. Flag unmarked lessons and hold the affected statement until attendance is resolved. Price from the lesson's booked rate. Households with two or more students with billable regular lessons get 10% off the smallest positive student subtotal for the month, using student reference to break ties. For two eligible subtotals of ₪301.05 and ₪218.75, round a 10% discount on the cheaper subtotal half up to ₪21.88, for ₪497.92 due. Apply the discount once per household. The bursar reviews and posts, records partial receipts and allocations, and issues linked credits for corrections after posting. Keep effective dates, reversals, and the issued statement's original figures visible.

Give the administrator room utilization by site, room and week, using booked minutes against configured room opening minutes, and attendance and make-up credit balances by teacher, term and instrument. Give the bursar an aging view as of a selected date and a receipts and credits reconciliation by month. Guardians get a printable statement and their own history. Every office report needs a detail view and matching CSV, with site, date, and status filters where applicable. Show zero activity for an empty room week. Keep the attendance correction, credit use, and posted ledger traceable back to the relevant lesson or statement.

Send in-app notices for the next day's lessons at 18:00, schedule changes, and newly posted statements. If the host was off at month close, prepare each missing draft once. Skip expired reminders and still notify guardians of changes to future lessons. A recipient with two memberships sees each notice in its own school.

## Who can do what

| Account | Access |
| --- | --- |
| Host operator | Create schools and bootstrap administrators. No student, lesson, or billing access through that role. |
| School administrator | Manage own school settings, accounts, roster import and audit. Read operations reports, approve eligible roster undo and authorize shared-teacher links for own school. |
| Scheduler | Manage own school rooms, closures, series, exceptions and make-up bookings. Read own school's scheduling contacts and availability. |
| Teacher | Read own rosters and schedule, mark and correct own attendance, and accept a shared membership link. |
| Bursar | Read own school's billing inputs, post statements, record receipts and credits, and export billing reports. |
| Guardian | Read permitted student schedules and notices, plus family statements and receipts where granted. |

## Hard constraints

1. Run on Windows using Python, Node, or both. Keep access on localhost or a private LAN.
2. Use no paid services, hosted assets, or runtime internet dependencies. Store data, print views, exports and notices locally.
3. Use a local SQL database with versioned, data-preserving migrations and transactional business changes.
4. Use real login, salted password hashes, expiring sessions, logout, and revocation on account disable. Removing a school membership blocks access immediately.
5. Check the active school, role, and record-level rights on the server for every relevant read, write, export, and notification. Shared-teacher availability exposes only blocked times.
6. Scope uniqueness and record relationships to the school. Scope import, jobs and audit records to the same ownership rules as interactive operations.
7. Use Asia/Jerusalem for scheduling and billing cutoffs. Explicitly reject nonexistent local times and require a choice when a local time occurs twice.
8. Keep exact agorot amounts and link posted corrections to the original records. Block receipt allocations beyond either the available receipt or outstanding statement balance.
9. Make schedule saves, attendance-generated credit changes, and receipt allocations atomic, including under competing requests. Audit sensitive changes with actor, time, reason, and before/after values.
10. Persist background job progress so restart catches up once per eligible school, month, or notice.
11. Make calendars, dialogs and report filters keyboard operable, with visible focus, labelled controls and accessible conflict and error feedback.
12. Deliver readable production-quality code and at least one automated integration or end-to-end test per workflow. Exercise the live write-to-report path, cross-school denial, schedule races, month-close restart and the roster undo guard.
13. Seed all three schools and every role, including the shared guardian and teacher. Include a non-developer Windows guide for setup, demo accounts, backup, restore, and restart.
