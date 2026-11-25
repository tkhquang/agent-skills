# Difficulty and data

Contents: what difficulty is, tools for tuning it, what to measure, reading a funnel, traps in interpretation.

## What difficulty is

The target is the band between boredom and anxiety where challenge keeps pace with growing skill. Players get used to any level of challenge, so it has to rise, with dips for rest. A flat line bores. A wall ends the session and often the relationship.

Difficulty is also how many new things the player must learn at once. One game lost 59 percent of players before the first checkpoint and about 80 percent of the rest at each of the next two checkpoints. Only 0.2 percent finished.

No single enemy was the cause. Players had to learn a new control scheme, new rules, random terrain, new enemies and risky powers all together, and the bright, friendly art had promised something gentler.

## Tools

| Tool | How it works | Watch out for |
|---|---|---|
| Difficulty levels | Player picks. Scale reaction time required, timing windows, aim forgiveness, number of threats, time limits, enemy health and damage | Label honestly. "Easy" must be easy for a newcomer |
| Dynamic adjustment | The game eases off after failures and tightens after streaks | If players notice, they may feel patronized or learn to exploit it |
| Rising curve | Start easy and ramp until the player is overwhelmed | Suits endless and arcade formats, not story games |
| Catch-up mechanics | Help for whoever is behind, drag on whoever is ahead | Strong versions make skill feel pointless |
| Alternate paths | Let a stuck player grind, upgrade, or go elsewhere and return | Keeps people playing who would otherwise quit at the wall |
| Assist options | Auto-aim, slower speed, skip | Offer without shame |

Ordering of new demands matters as much as size. Introduce one new thing, let the player use it, then combine it with earlier things.

Only new testers can judge difficulty. Anyone who has played the build before, the designer most of all, has lost the ability to feel the first hour.

Luck and skill dials: `chance-and-skill.md` in `game-systems-design`.

## What to measure

For competitive balance:

- Win rate by faction, class, character or opening.
- Pick rate and ban rate.
- Win rate by skill bracket, since something can be weak for beginners and oppressive at the top.
- Match length and how early the eventual winner was ahead.

For progression balance:

- Completion rate at each checkpoint or level.
- Time between checkpoints, median and spread.
- Deaths, retries and quit points per section.
- Resources held and spent at each stage.

For economy balance:

- Currency created and destroyed per day. The difference is net issuance, not inflation.
- Total and median balance by player age.
- Price of a fixed basket of traded goods over time. This is the inflation measure.
- What nobody buys.

For decisions:

- Which options are chosen wherever the player makes a major choice, and how long choosing takes.
- Tutorial completion and where people stop reading.

Tabletop equivalents: game length, turn length, which strategies and pieces get used, final score spread.

## Reading a funnel

List the percentage of starting players who reach each checkpoint, then look at the drop between consecutive checkpoints.

- One drop much larger than its neighbors: a wall at that spot. Inspect what is introduced there.
- The same large proportional drop at every stage: a pervasive problem such as too many simultaneous demands or unclear feedback.
- A big drop before the first checkpoint: the opening does not teach or does not show the fun.

Numbers tell you where. Watching people play tells you why.

## Traps

- Small samples. A friend, a focus group or the boss's relative is not the player base.
- Vocal minorities. A game with 100,000 daily players can have a forum on fire from a few dozen people, a twentieth of one percent, while every measure of play improves. Check behavior before reverting.
- Confounds. If thieves level fastest, check who plays thieves before nerfing them.
- Survivorship. Data from players who stayed says nothing about those who left in the first minutes.
- Local maximum. Optimizing measurable things step by step can lock in a mediocre design. Data does not propose the different game players would love more.
- Asking players what to build. They can tell you what bothers them. They are not designers and often cannot imagine what they would want until they see it.
- Chasing perfect balance. Past a point the effort exceeds the rest of development. Fix what is badly off and what players feel.
