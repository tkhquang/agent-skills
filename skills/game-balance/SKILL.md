---
name: game-balance
description: Balances the numbers in a game. Handles item and unit stats, cost versus benefit, rock-paper-scissors counters, dominant strategies, XP and power curves, pacing and time-to-level, drop rates and rarity tiers, currency sources and sinks, inflation, difficulty tuning, win-rate or funnel data, and automated simulation of matchups and whole games. Includes calculator and simulation-statistics scripts. Use when the user asks whether something is overpowered or underpowered, wants an XP table or price list, is tuning weapons, enemies, classes, loot, an in-game economy or difficulty, wants bots or simulations to test balance, or says a game is too easy, too hard, too slow, grindy, inflated.
compatibility: The scripts need Python 3 and use only the standard library.
license: MIT
---

# Game balance

A balanced game has no dominant strategy, no lead that cannot be overturned, several approaches worth trying, and losers who believe they could have won. Arithmetic finds the large imbalances fast. Playtesting finds the rest. No formula makes the aesthetic choices, so say that when a user expects a spreadsheet to settle everything.

## Workflow

1. Define "balanced" for this game and audience: a fair match between equals, a smooth solo ramp, or an economy that holds its value. Each needs different tools.
2. Find the core resource, the thing the player is trying to maximize or not lose: health and experience in a role-playing game, money in a tycoon game, territory in strategy. Other resources get their value from how they help it.
3. Choose the balance type for each set of things being compared.
   - Cyclic: options counter each other like rock, paper, scissors. For unit types, classes, factions.
   - Cost and benefit: better things cost proportionally more. For gear tiers, upgrades, levels.
4. Put every part in a spreadsheet: rows are things, columns are attributes.
5. Model it with `scripts/balance_tools.py`: weight attributes by their effect on the core resource, score items against cost, find dominated options, pick a curve for anything that grows.
6. Convert costs into minutes of play. Time is what every player spends.
7. Audit the economy: every source, every sink, every buy and sell price pair.
8. If the rules run without rendering, simulate: mirror matches, equal budgets, random armies, whole games. See `references/simulation.md`.
9. Playtest, change one thing, and test the whole game again. Changes ripple.
10. With live players, add behavior data: win rates, pick rates, time to progress, quit points.

## Inputs and when each misleads

| Input | Good for | Misleads when |
|---|---|---|
| Intuition | First values | An argument replaces a quick prototype |
| Playtesting | What players experience | Players' fixes are adopted. They report problems well and solutions poorly |
| Analytics | Win rates, pick rates, funnels, time to level | Samples are small, a vocal few stand in for everyone, or a confound hides the cause (the fastest-leveling class may attract experts) |
| Math models | Curves, costs and economy before launch | They are treated as proof |
| Simulation | First-move advantage, dead options, stalls, whole-game shape | The bots ignore a mechanic, or one fixed matchup stands in for all |

## Cyclic balance

- Each option beats as many others as it loses to. If every matchup has a winner, that needs an odd count: three or five. An even count works only when some matchups are even, such as four types that each beat one, lose to one and draw with one.
- Two sides cannot self-correct. Three can, because two gang up on a leader.
- Fill in the whole who-beats-whom table before judging it. An empty cell is an untested matchup, not a draw.
- Keep top-level types few and add variety with subtypes.
- Build counters from equal budgets spent differently:

| Type | Attack | Defense | Range | Speed | Beats | Because |
|---|---|---|---|---|---|---|
| Infantry | 3 | 2 | 1 | 1 | Cavalry | Attack 3 against defense 1 |
| Cavalry | 2 | 1 | 1 | 3 | Archers | Faster, so archers cannot escape |
| Archers | 1 | 1 | 3 | 2 | Infantry | Outranges and outruns |

- Test with outside conditions such as terrain. One exploit (archers nobody can reach) collapses the cycle into a single strategy.

## Cost and benefit balance

1. Order attributes by how they gate the core resource. For a weapon: speed decides how often you act, accuracy whether you hit, damage how much.
2. Assign weights and compute a benefit score per item. A first guess for that weapon: damage 1.0, accuracy 1.5, speed 2.0. Put attributes on one scale first, such as 1 to 10, or the largest unit decides the score. If the damage formula is known, score its result (damage per second, hits to kill) instead of guessing weights.
3. Compare score with cost. Look for items far off the line and items beaten on everything by something no more expensive.
4. Change attribute values until each item has a niche where a sensible player would choose it.
5. If a value cannot change, add a situational cost: harder to obtain, upkeep, a handling penalty.

Special abilities such as cooldown powers resist formulas. Price them by judgment, then test.

## Curves

| Curve | Formula | Feels like | Use for |
|---|---|---|---|
| Linear | `y = a*x + b` | Each step identical, so later steps feel smaller | Short ranges |
| Polynomial | `y = a*x^n` | Steps grow, then flatten in relative terms | Costs from two linear things multiplied |
| Exponential | `y = base*rate^x` | Next step looks reachable, distant ones look huge | Most experience and power curves. Rate 1.1 is slow, 1.2 doubles in about four steps, 1.4 in about two |
| Logistic | `y = L / (1 + e^(-k(x - x0)))` | Slow start, fast middle, diminishing returns | Stats that should cap. Stack several so players switch investments |
| Piecewise linear | Segments between chosen points | Visible breakpoints that become goals | Hand-tuned progression |

Challenge and reward must grow at matching rates. If enemy strength triples each level while player power grows by a quarter, the game is unplayable within a few levels.

## Economy

- List every faucet (kills, quests, vendor sales, daily gifts) and every drain (purchases, repairs, fees, upgrades).
- Faucets outgrowing drains: balances pile up, prices rise where players set them, and where prices are fixed the currency stops working as a reward.
- Drains choking faucets: hoarding, no trading, players leaving.
- Keep these measurements apart: net issuance (created minus destroyed per hour), balances held, and the price of a fixed basket of goods. Only the basket price is an inflation rate. Do not prescribe a sink from net issuance alone.
- Rewards usually grow to stay exciting, so sinks must grow with them.
- Any buy price below any sell price, anywhere, is a money machine. Audit every pair.
- For player markets, the game always buys at a low price and always sells at a high one. Players set prices in between.
- Keep power and rarity on separate curves: power up 20 percent per tier, rarity tripling per tier.

## The calculator

Run `scripts/balance_tools.py` for table arithmetic.

```bash
# Experience per level: 1000 x 1.4^level, rounded to hundreds
python scripts/balance_tools.py curve --type exp --base 1000 --rate 1.4 --levels 30 --round 100


# Minutes per level: 50 to 200 points per success at 80% success, 1 to 3 minutes per try.
# Rewards grow 30% per level
python scripts/balance_tools.py pacing --type exp --base 1000 --rate 1.4 --levels 10 \
    --reward 50-200 --reward-rate 1.3 --success 0.8 --minutes 1-3

# Weighted benefit score against a price column
python scripts/balance_tools.py cost --csv items.csv --weights "damage=1,accuracy=1.5,speed=2" --price cost

# Items that are never the right choice
python scripts/balance_tools.py dominance --csv items.csv --benefits accuracy,damage,speed --costs cost

# Who-beats-whom matrix. W: row beats column, L: row loses, D: even, blank: not yet known
python scripts/balance_tools.py cycle --csv counters.csv

# Dry streaks: 1% drop, 4 minutes per run, guaranteed on run 150
python scripts/balance_tools.py drop --rate 1% --tries 100 --minutes 4 --pity 150

# Dice odds
python scripts/balance_tools.py dice 2d6+1
```

- Item CSV: a header row, name column first.
- Matrix CSV: option names in the first row and first column. One side of each pair is enough. No verdict is given while a pair is blank or its two sides disagree.
- Pacing prints averages and a "9 in 10 by" column. With a success chance below 1 there is no worst case, so quote that column when asked how long a level can take.

## Quick diagnosis

| Symptom | Look at | Typical fix |
|---|---|---|
| Everyone picks the same thing | Dominance check, win and pick rates | Give alternatives a niche, raise its cost, add a counter. Do not answer one overpowered thing with another |
| Early lead decides the game | An unchecked reinforcing loop | Costs that scale with the lead, catch-up tools, comeback windows |
| Game drags with no winner | Balancing loops too strong, cycle too rigid | Add escalation, loosen the brakes |
| Mid-game slump | Step ratio of the curve, gaps between rewards | Shorten the gap, add a second progression path or a breakpoint goal |
| Late rewards feel like nothing | Linear or flattening curve | Constant-ratio curve, or a new kind of reward |
| Players quit at a wall | Funnel by checkpoint, how many new things arrive at once | Smooth the ramp, one new demand at a time, a way to grind past |
| Time per level varies wildly | Pacing spread | Narrow the reward range, tie reward to time spent |
| Currency is worthless | Net issuance, balances by player age, basket price over time | Scaling sinks, wear, caps, more to buy. Confirm with balances or prices first |
| "I never get the drop" | Share of players empty-handed at the expected number of tries | A guarantee after N tries, a rising chance, a token price, or a fixed pool |
| Nobody spends | Prices against income, fear of future need | Raise income, lower upkeep, make spending reversible or clearly valuable |

## References

- `references/curves-and-pacing.md`: curve math, choosing rates, converting cost to time, drop rates and dry streaks, secondary progression, a worked weapon example.
- `references/economy.md`: sources and sinks, measuring issuance, balances and prices, inflation, stagnation, arbitrage, tiers, price channels, crafting.
- `references/difficulty-and-data.md`: difficulty tools, what to measure, reading funnels, traps in interpretation.
- `references/simulation.md`: harness, opponent, fair comparisons, yardsticks, sample sizes with `scripts/sim_stats.py`, whole-game measures.

## Related skills

`game-systems-design` for loops that numbers cannot fix and solver-checked levels, `game-programming-patterns` for a core that runs headless, `game-retention-monetization` for live-service metrics, `game-concept-prototyping` for playtest method.
