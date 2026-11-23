# LoadIn

I'm Jules, tour manager for a five-piece band called Northbound Static. There are six of us working the van and trailer on a good day. At the Harbor Mill we can park at the dock, but at the Fox Annex it's a 40-metre push through a side alley. Last Saturday we packed the cable trunks first and buried them behind the drum riser. We lost twenty minutes before we could run a single line.

I'd start by setting up one show at the Fox Annex. I want the crew to see where the driver stops, who has the key, and what needs to happen between our 15:00 arrival and 17:30 soundcheck. I'd make a gear list with quantities, then put the cases in the order we load them into the trailer. On arrival I want the unload view to start with the cases nearest the door. A new show with no gear assigned should say so before we mistake an empty list for a finished pack.

Next I'd reuse the gear and venue details when we go back to Harbor Mill. This time we're leaving the spare guitar amp at home, so that change belongs to this show. Show me if I've assigned three radio packs when we only carry two, or put line check before the stage is ready. Give me a printed copy of the day's plan for the driver.

Show day is where I'd really use it. Lina might tick off the cable trunk from the dock while Dev checks off stands from the stage. We need to see what's left, including anything that was marked missing. Sometimes both will scan the same list and tick the same case. I want one completion that says who did it. If the laptop restarts while we're unloading, the person at the door should get back to the same list without walking the trailer again.

## Hard constraints

- I run it on Windows with Python, Node, or both. Crew phones connect over our local network.
- The app needs no internet connection, paid services, or network-hosted assets at runtime.
- The shared gear and venue details can be reused. Show-specific edits leave the shared records and earlier shows intact.
- Pack order is explicit. The unload view shows door-first order based on how we packed.
- Each show has its own timings and checklist. Impossible quantities are rejected and schedule conflicts are visible before the plan goes out.
- Confirmed checklist changes survive restart. Simultaneous taps never create duplicate completions, and a missing case stays visible until we resolve it.
