# Multiplayer systems

Contents: classify the game, what player count changes, joining and leaving, low population, players who spoil the session, old and new players, community, design sheet, low-population playtest.

Other players are the best source of uncertainty a game can have and the least reliable part of it. They arrive late, leave early, differ in skill and sometimes play to ruin the session. A multiplayer design is finished when it says what happens in each of those cases.

## Classify the game

| Axis | Options | What it decides |
|---|---|---|
| Count | Two, a small group, large teams, thousands in one world | Which social dynamics exist at all |
| Relationship | Competitive, cooperative, teams, free-for-all, or modes the player picks | Where goals are shared and where they collide |
| Time | Real time or turns. Everyone present, or play when you can | How much one player's absence costs the others |
| Session | Fixed roster, or players coming and going | Whether join and leave rules are needed |

## What player count changes

- Two: a pure contest or a pure partnership. No trading, negotiation or alliances, and no third party to check a leader, so the rules must check any lead.
- Three to about eight: negotiation, alliances and ganging up appear. So does kingmaking, where a player who cannot win decides who does. Check what a losing player can still do, and to whom.
- More than about eight: free-for-all becomes rare and players form teams. Design roles, a way to coordinate, and what a team does when a member is weak or absent.
- Thousands: give each player a scope they can affect, such as a group, a territory or a market niche.

## Joining and leaving

| Question | Options | Watch for |
|---|---|---|
| A player drops mid-session | A bot takes over, play continues short-handed, the slot reopens, or the match ends | Short-handed play that cannot be won. A bot much better or worse than the person |
| A player joins in progress | At once, at the next round, or at the next match | Late joiners far behind in power, or unable to tell what is going on |
| Minimum and maximum players | Hard limits, or content that scales | A minimum that is rarely met. A maximum that splits groups of friends |
| The count changes during play | Scale threats, rewards and resources to players present | Scaling that makes leaving the best move, or punishes a group for an idle member |
| A co-op partner leaves | Rebalance for one, pause, add a bot, or let the remaining player finish and keep the reward | Progress lost through someone else's disconnect |
| Reconnection | Hold the slot for a grace period, or not | Disconnecting on purpose to dodge a loss |

Rules: nobody loses progress to another person's connection, and leaving is never the best strategy.

## Low population

Every online game is nearly empty at some point: at launch, at off-peak hours, in a small region, late in its life.

- Scale spawns, rewards and objectives to the players present.
- Find the smallest count at which each mode is still fun, and decide what the game offers below it: bots, a solo variant, play against stored opponents, or wider matchmaking.
- Wider matchmaking trades fairness for speed. Decide how long a wait is acceptable before the skill range widens, and tell the player when it does.
- Do not split a small population across many modes, regions and queues. Each split multiplies the wait.

## Players who spoil the session

Some players enjoy ruining the experience for others. For every rule that lets one player affect another, ask what the worst-intentioned person would do with it.

Common routes: repeatedly killing or blocking weaker players, sabotaging a team from inside, idling while collecting rewards, abusive chat, quitting to deny a result.

| Tool | How |
|---|---|
| Consent | Conflict between players happens in places or modes they chose to enter |
| Limits in the rules | Remove the route: no friendly fire where it adds nothing, no collision that lets one player block a doorway, protection for new or just-defeated players |
| Player controls | Block, mute and avoid, per player and effective at once |
| Reporting | Records, and consequences that are seen to happen |
| Reputation | Players choose who they play with |
| Incentives | Reward what the group needs (healing, reviving, finishing the match) more visibly than what hurts it |

Change the rules before relying on moderation. A reporting system only handles what the rules still allow.

## Old and new players

An online game holds several populations: people new to the genre, people new to this game who often arrive in groups, and veterans.

- Power caps keep newcomers within reach and give veterans less to chase.
- Open competition rewards experience and is hard on newcomers.
- Skill-based matchmaking, brackets, separate starting areas and mentoring rewards let them share a game without sharing every match.

Test the first hour of a player who joins a year after launch, alone, among experts.

## Community

- Player-made groups (guilds, clans) with tools to run them.
- Friend lists, and a way to see who is online and join them.
- Recognition in the game for players who organize and lead.
- Something a group can do that individuals cannot.

Group obligation is also the strongest retention force. See the superfan layer in `game-retention-monetization`.

On a shared board or screen, everyone must be able to see what they need and tell whose turn it is. In tabletop designs, check how much waiting each added player causes and whether a player can be eliminated long before the end.

## Multiplayer design sheet

```markdown
# Multiplayer design: [game or mode]

Count: [minimum, ideal, maximum]
Relationship: [competitive, cooperative, teams, free-for-all, mixed]
Time: [real time or turns; everyone present or play when you can]
Session: [fixed roster or drop-in]

Shared goals:
Opposing goals:
Every way one player can affect another:
Worst-intentioned use of each, and what stops it:

Drop-out rule:
Join-in-progress rule:
Reconnect rule:
Scaling with player count:
Smallest count that is still fun, and the fallback below it:

A new player joining late in the game's life:
What groups can do that individuals cannot:
```

## Low-population playtest

Run this before any large test.

1. Play with the minimum count the mode allows. Then try one fewer and note what breaks.
2. Start a full session and have one player leave at the start, the middle and near the end. Record what the others experience and whether anyone loses progress.
3. Have a player join late. Record how long until they are useful and whether they can catch up.
4. Pair an expert with a first-time player, on the same side and then on opposing sides. Ask both whether they would play again.
5. Ask one tester to spoil the session within the rules. List every method that worked.
6. With two people online, try to find a match in each mode. Time the wait.

Each failure maps to a row in the joining and leaving table or a tool in the spoiling table.
