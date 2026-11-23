# RehearsalKeys

I'm Priya, stage manager for Junction Players. We're rehearsing The Clockmaker for six weeks with 12 cast members, a hall we borrow on Tuesdays, and a smaller room on Thursdays. Last week I called Callum in for Act I, Scene 3 and only found out at the door that we'd switched him from Theo to the Inspector. The director had changed the cast list, and my printed schedule was already out of date.

First I need somewhere to put the cast, their roles, and which roles appear in each scene. For our first Tuesday I'd like to book Scene 3 at 7 p.m. and see the names I actually need. Then I can print a one-page call sheet with arrival times, room, and scenes for the hall noticeboard. An empty week should say there are no calls yet so I can tell at a glance if I've forgotten to schedule it.

Once we've got a week on paper, I want cast members to enter when they're free from their phones. Mae can only arrive after 7:30, Luis is unavailable this Thursday, and I haven't heard back from Callum. Those are three different things when I'm deciding whom to call. If someone types an end time before the start time, show them where to fix it. I also need to catch overlapping calls for the same actor when the director wants to split the cast between rooms.

By week four we'll be moving calls around after publishing them. If the director moves Scene 3 while I'm changing its room, I need to see what's changed before either of us wipes out the other's edit. After a restart I want the current call sheet and the previous published version so I can answer someone who brings in last week's printout.

## Hard constraints

- I run it on Windows with Python, Node, or both. On-site phones connect over the local network.
- It works offline from the internet with no paid services or network-hosted assets at runtime.
- Each scene call uses the current role assignments. Switching actors flags any affected published calls for review.
- Unavailable, available, and no reply stay distinct. Availability and overlap warnings identify the affected actor and time.
- Published call sheets carry a date and revision, print legibly on A4, and stay retrievable after later changes or restarts.
- Cast members can edit their own availability. Only the scheduling team can publish or revise calls.
