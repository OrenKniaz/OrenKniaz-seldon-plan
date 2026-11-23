# DoorCount

I'm Mara, and I manage the Lantern Room, a 120-person music venue. On a busy Friday I put Jo at the front door and Ben by the patio. We each have a clicker, and when the line backs up I have to yell across the room to find out whether we can let anyone else in. Staff and performers count toward our limit, so I've already got 14 people inside before the first ticket holder arrives.

I'd start with one door and my old Windows laptop. I want to open a new night, enter those 14 people, and tap people in or out on my phone. Give me a big number I can read with one hand full of wristbands, plus how many places are left. When there's no night open, tell me that plainly so I don't accidentally add people to last Friday. If I tap Out when the room is empty, tell me what happened and keep the count at zero.

Once that works, let Jo and Ben join the same night from their phones. At 119, if both try to admit someone, one should get the last place and the other should see that we're full. If a phone drops off Wi-Fi while someone is tapping, they need to know whether that tap went through before they try again. Sometimes somebody hits In twice for one guest. I want to correct the count with a reason and be able to see who made the correction later.

At closing I want to see when we first filled up and what our peak was. On Monday I want to pull up the last four Fridays and export the numbers for the owner. If the laptop reboots in the middle of a set, I need to reopen the same night with the count we already recorded.

## Hard constraints

- I run it on Windows. Python, Node, or both are fine.
- Staff phones use our local Wi-Fi. The app works with the internet disconnected, uses no network-hosted assets at runtime, and needs no paid services.
- Every door sees the same occupancy. Entries stop at the stated capacity, and exits never take occupancy below zero.
- Every correction keeps the original activity and records who changed the count and why.
- A restart preserves the open night and confirmed activity. Retrying an uncertain tap must never count the same action twice.
- Closed nights stay available for date-range reports and CSV export.
