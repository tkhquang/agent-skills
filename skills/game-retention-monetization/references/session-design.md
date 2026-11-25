# Session design

Contents: on-ramp, playtime and intensity, off-ramp and energy, pottering, return hooks, session review template.

## On-ramp

The competition is everything that wants the player's attention, social media above all, and not only other games.

The on-ramp is not onboarding. Onboarding happens once. The on-ramp happens every visit.

The test: can the player do something meaningful in the time it takes to wait for a coffee? It splits into questions the player asks without noticing.

- Have I got time for this right now?
- Is the fun or progress worth the effort of starting?

A player with a whole evening free can still think "I don't have time for that game" and then spend two hours in another one that let them start small. Commitment cost, not available time, decides.

Expectations depend on device. A phone is always in reach, so seconds matter. A tablet is more forgiving. A console needs the screen, the controller and usually an hour, so the bar to start is higher. Mobile play mostly happens at home in the evening, competing with television, not in queues.

### What helps and what hurts

| Helps | Hurts |
|---|---|
| Short load time | Long load, splash screens, logo parades |
| An instant reward or progress report on arrival | A list of chores or problems on arrival |
| A clear next step | No reminder of what you were doing |
| Short rounds that invite one more | Long mandatory commitments |
| Play that survives being put down and resumed | State lost on suspend, forced logouts |
| Works without a connection | Mandatory online, matchmaking waits |
| Lightweight presentation | Heavy graphics that slow everything |
| Straight into the game | Interrupting menus and confirmations with one option |

None of the right-hand items is forbidden. Many hit games fail several of them. Each is a cost that something else in the design must pay for.

Sample load times measured on one tablet show the spread: five seconds for simple pixel-art games, about half a minute for a major puzzle game, forty-five seconds for an online card game, two minutes for a graphically rich resource manager whose own fans drifted away partly for that reason.

### First seconds back

Make the returning player feel like a ruler coming home, not a cleaner arriving at a mess. Open with what they earned while away, a bonus, a level-up. A restaurant game that made players pick up litter before anything else taught them to dread opening it. Chores can exist. They should not be first.

### Sleight of hand

If loading cannot be shortened, disguise it. An animated zoom into the world while systems finish initializing feels faster than a progress bar. Complaints about slow lifts in an office tower stopped after mirrors were installed.

### The session-length paradox

Shorten the promised session and the real one often gets longer. Sixty-second rounds led to average sessions of over forty minutes.

A home screen where opening a reward and starting the next timer takes thirty seconds invites "I'm here, one quick match". When the on-ramp is fixed, expect session length to hold or rise and, more importantly, sessions per day to rise.

### Questions

- What rhythm do we expect: several short visits a day, or a few long ones a week? The more frequent, the more the on-ramp matters.
- Can a slow start be mitigated by loading order, by dropping a requirement, or by theater?
- How do we reward the return in a way that fits the genre?
- How do we put the player back in the loop knowing what they were doing and why?

## Playtime and intensity

Plan intensity. Lean-back play is the norm on phones, and long stretches at full intensity cost both the current session and the next visit. Give respite: breaks between matches, waves with gaps, calm moments in an endless run. A three-minute match can save its intensity for the final minute by doubling resource flow.

High skill combined with high intensity narrows the audience. That is a legitimate choice if made knowingly. The appeal of competition also declines with age.

## Off-ramp

Recipe: signal that the main tasks are done, let people stay if they wish, plant a hook.

Natural stopping points: a level completed, all crops planted and all machines running, daily tasks finished, out of lives.

Players start more easily when they trust they can stop. One player said she would never play a certain puzzle game without its limited lives, because she lacks the willpower to stop on her own.

The chocolate cake problem: one slice is lovely, a second is nice, and the whole cake makes even the first slice a bad memory. Parcel play out.

### Energy

Energy (also fuel, stamina, lives, or simply a limited number of slots to fill) is first a retention tool. It sets session length, signals completion, prevents rage-quitting at a hard level, and makes choices matter: with one unit left, do you grind a safe race or risk the boss?

| For | Against |
|---|---|
| Paces sessions and marks a stopping point | Clunky and artificial |
| Stops players burning out on a repetitive activity | Seen as a paywall and a sign of manipulative design |
| Scarcity pushes players toward challenges at the edge of their ability | Removes control from the player |
| Can be sold | Caps the play of devoted players who would not burn out |
| | Does not feel generous |

It has evolved from a hard stop ("pay or leave") to a gentle signal ("everything is running, come back later, or stay and tinker"). Look first for other ways to get the same benefits.

## Pottering

Pottering is unhurried, self-directed activity with no pressure: the answer for players who have finished the main tasks and want to stay.

- Enjoyable tidying: arranging an inventory, reorganizing a production line.
- Learning and theory-crafting: reading lore, studying a tech tree, building a deck.
- Self-expression: decorating, dressing a character.

It also provides the low points that make high intensity bearable. The aim is that the player chooses session length: short if they need it, long if they want it.

## Return hooks

Tactics that bring the player back for the next session. Most can be added after launch and are better left out until the core loop has shown it retains on its own.

| Hook | How it works | Caution |
|---|---|---|
| Welcome back | Show what was earned while away | None. Do it |
| Timed rewards | A free reward every few hours and a better one daily | Builds cadence without commitment |
| Streak accumulator | Rewards grow over three to seven consecutive days, then reset | A broken streak can hurt enough that the player never returns, or sours the icon. A monthly calendar that counts total days with milestones and no reset is kinder |
| Appointment | The player starts something that finishes later. A set of slots with multi-hour timers gives several short visits and one longer refill session | Works best when part of the main loop |
| Decay | Something worsens while away | Feels like punishment in gentle games. Fits where being raided is part of the fiction. Give the player control over the window, and reward returning at all |
| Live events | Limited-time activities and content | Powerful, expensive to run, and a bandage if the core loop is weak |
| Social | A friend is waiting, the group needs you | Include from the start only when intrinsic. Nagging forms can wait |
| Notifications | A nudge | Not a hook in themselves. They amplify a real reason to return. Ask permission in context when the player starts a timer, and explain the benefit |

## Session review template

```markdown
## Session review: [game]

Expected rhythm: [visits per day or week, typical length]

On-ramp
- Time from icon to first meaningful action:
- What the player sees first:
- What blocks a quick visit:

Playtime
- Shortest satisfying unit of play:
- Intensity pattern and where the rests are:

Off-ramp
- Natural stopping points:
- What signals "done for now":
- What a player can do if they want to stay:

Return hook
- The reason to come back, in the player's words:
- When, and who chose that time:
- What happens if they are late:

Changes, in priority order:
1.
2.
3.
```
