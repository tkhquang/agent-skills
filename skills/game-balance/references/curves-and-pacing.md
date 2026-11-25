# Curves and pacing

Contents: why curves, core and subsidiary resources, curve types in detail, choosing rates, time and attention, drop rates and dry streaks, secondary progression, worked weapon example.

## Why curves

Two ideas sit under every progression or power curve.

1. Every benefit has a cost and they rise together. The delay before the player can afford the next benefit is what sets the pace of the game while still letting them feel they are improving.
2. After paying, the player must feel meaningfully better off. If leveling up feels like nothing, or worse, the resource that paid for it loses its value and engagement drops.

People judge rewards relative to what they already have. The tenth identical reward barely registers. This habituation is why reward sizes and rates usually have to grow, and why curve shape matters more than any individual number.

## Core and subsidiary resources

- Core resource: what the player is trying to maximize or not lose. Find it by asking which attribute the player cannot continue without. There may be one per major loop.
- Subsidiary resources: things that maintain, improve or repair the core one. In a strategy game territory is core, and armies, forts and technology are subsidiary. In a relationship game the relationship is core, and friends, money and information are subsidiary.
- Several candidates? Look for one overarching quantity that contains them, even one the player never sees. If the game moves through phases with different core resources, give each its own curve and take care with the hand-off between them.
- Special cases such as a boost that is useless until the moment it is vital cannot be reduced to one number. Price them by judgment and test. Forcing everything into one formula can also make tradeoffs too obvious to the player.

## Curve types

### Linear: `y = a*x + b`

Constant step. Easy to understand and weak on its own, because the relative gain shrinks: going from 16 to 20 is a 25 percent improvement, going from 196 to 200 is 2 percent. Use for short ranges.

### Polynomial: `y = a*x^n`

Steps grow, and the ratio between consecutive steps falls toward one. For x squared the values are 1, 4, 9, 16, 25 and the steps are 3, 5, 7, 9. The next target is never astronomically far, and late steps feel similar to each other.

A quadratic appears naturally when two linear things multiply. If monsters per level grow 1, 2, 3, 4 and gold per monster grows 10, 20, 30, 40, then gold per level grows 10, 40, 90, 160. Expect this whenever two systems interact.

### Exponential: `y = base*rate^x`

Constant ratio. Each step is the same multiple of the one before, so the next goal always looks reachable relative to what the player has, while distant goals look enormous and aspirational. This is the most common choice.

Example with experience needed = 1,000 × 1.4 to the power of the level, rounded:

| Level | Needed | Level | Needed |
|---|---|---|---|
| 2 | 2,000 | 15 | 155,600 |
| 3 | 2,700 | 20 | 836,700 |
| 4 | 3,800 | 25 | 4,499,900 |
| 5 | 5,400 | 30 | 24,201,400 |
| 10 | 28,900 | | |

Weakness: top-end numbers stop meaning anything. People cannot feel the difference between a quadrillion and a quintillion.

### Logistic (S-curve): `y = L / (1 + e^(-k(x - x0)))`

L is the ceiling, k the steepness, x0 the midpoint. Slow start, rapid middle, diminishing returns. Good for anything that should cap.

Stacking several S-curves for different resources creates a strategic choice: when one investment hits diminishing returns the player has to decide when to switch to the next. A stack of S-curves approximates an exponential overall and is easier to balance piece by piece.

### Piecewise linear

Straight segments between chosen points. Ways to build one:

- By rates: 2 hit points per level for levels 1 to 10, then 5 per level to 20, then 10 per level to 30. Starting from 12 that gives 30 at level 10, 80 at level 20, 180 at level 30.
- By endpoints: 2 at level 1, 20 at level 10, 100 at level 20. Slope of each segment is (y1 - y0) / (x1 - x0), so 2 per level then 8 per level.

Breakpoints become interim goals: players learn that things speed up at level 11 and aim for it.

### Hand-crafted

Round numbers and deliberate bumps. A smooth predictable curve can itself become dull because the player knows exactly what the next upgrade is worth. Uneven curves let different resources be the best buy at different times, which gives the player something to explore. Typical practice: start from an exponential and bend it by hand.

## Choosing rates

- The growth rate tells you the feel directly. At 1.4 each level costs 40 percent more than the last and the requirement doubles about every two levels. At 1.2 it doubles in about four. At 1.1 it doubles in about seven.
- Decide the pace you want first: how many minutes, fights or missions per level at the start, middle and end. Then fit the curve to that, not the other way round.
- Match the rates of challenge and reward. Enemy strength, player power and rewards should grow at compatible rates, or the game quickly becomes impossible or trivial.
- A modest spread keeps players in the same game. Item power growing 20 percent per tier makes a tier-eight item about twice as strong as tier four: progress is felt and the gap is not hopeless.

## Time and attention

Whatever the in-game currency, the player is spending time and attention. Convert costs into minutes.

Simple case: an activity gives 10 points, a level needs 100, each activity takes 2 minutes. That is 20 minutes of full attention per level.

Realistic case: a level needs 1,000 points, each success gives 50 to 200, success rate is 80 percent, each attempt takes 1 to 3 minutes.

1. Successes needed: 1,000 / 200 = 5 at best, 1,000 / 50 = 20 at worst. Round up, because a level needs whole successes: 101 points at 100 per success is two successes, not 1.01.
2. Attempts: each success takes 1 / 0.8 = 1.25 attempts on average, so about 6 to 25 attempts.
3. Time: 6 attempts at 1 minute to 25 attempts at 3 minutes, so about 6 to 75 minutes on average.

Those are averages. When success is uncertain there is no worst case, only a tail: here one player in ten at the slow end is still going after 84 minutes. Quote an average and a tail figure, never a single number. `scripts/balance_tools.py pacing` prints both.

A range that wide means two players have very different experiences of the same level. Narrow it: make slower attempts more likely to succeed, give bonuses for doing well, or reduce the reward range.

Attention and clock time are different levers.

- Requiring attention keeps players engaged and caps how long they can keep going.
- Gating by clock time (start a timer, come back later) gives exact control over pace and gives the player nothing to do meanwhile.

Respect the player's time. It is the one resource they cannot earn back.

## Drop rates and dry streaks

A drop rate describes the average player. Design for the unlucky one, because that is who complains and quits.

For a fixed chance p per try, with every try independent:

- Chance of still having nothing after n tries: (1 - p) to the power n.
- Average tries to the first drop: 1 / p.
- Tries by which a given share of players have it: log(1 - share) / log(1 - p), rounded up.

Worked example, a 1 percent drop:

| Question | Answer |
|---|---|
| Average tries | 100 |
| Players with nothing after 100 tries | 36.6 percent |
| Half of players have it by | 69 tries |
| 9 in 10 have it by | 230 tries |
| 99 in 100 have it by | 459 tries |

"One in a hundred" therefore does not mean "within a hundred". For any rare drop, a bit over a third of players are still empty-handed at the expected number of tries. Convert tries into minutes before judging: at 4 minutes a run, one player in ten spends more than 15 hours on this item.

Ways to cut the tail, and how each changes the math:

| Method | Effect |
|---|---|
| Guarantee on try N | Worst case becomes N. The share who need the guarantee is (1 - p) to the power N - 1. Average tries fall to (1 - (1 - p)^N) / p |
| Chance rises after each miss | Shorter streaks. Lower the starting chance if the average should stay the same. Compute by multiplying the miss chances of each try in turn |
| Draw from a fixed pool without replacement | A bag of N with k winners guarantees one within N - k + 1 draws. Each miss raises the odds of the next draw |
| Token price | Every run gives a token and the item costs N tokens. No luck at all: use when the item gates progress |

With the same 1 percent drop and a guarantee on try 150: nobody waits longer than 150 tries, 22.4 percent of players get the item from the guarantee, and the average falls from 100 tries to about 78.

A long dry streak reads as broken or rigged. Showing progress toward a guarantee turns the streak into a countdown. If the drop can be bought, state the odds: see the ethics reference in `game-retention-monetization`.

Run these with `scripts/balance_tools.py drop --rate 1% --tries 100 --pity 150 --minutes 4`.

## Secondary progression

When primary milestones are far apart, add shorter paths alongside them: inventory capacity that grows with wealth, crafting skill, reputation, collections. Keep them loosely coupled to the main track so they self-balance. Players attend to them when they start to pinch.

## Worked example: pricing a weapon set

Setup: seven melee weapons with accuracy, damage and speed. Core resource: enemy health.

1. Gate order: speed (how often you get to attack), then accuracy (whether it lands), then damage (how much).
2. First weights: damage 1.0, accuracy 1.5, speed 2.0.
3. Score each weapon as the weighted sum and compare with intended price.
4. Read the outliers. A heavy slow blade may score below a short sword because speed is weighted heavily. Decide whether that is a pricing problem or whether the blade needs a different stat line to have a purpose.
5. Check dominance. If one weapon is at least as good as another on every stat and costs no more, the second is dead weight.
6. Check spread. If the best weapon costs only twice the worst, the range may be too narrow to feel like progress.
7. Adjust values so each weapon is the right answer somewhere: fastest, hardest hitting, most reliable, cheapest.
8. Play it. The weights were a hypothesis about how the combat system turns stats into results. Revise them until the scores match what happens in fights.

Run steps 3, 5 and 6 with `scripts/balance_tools.py cost` and `dominance`.
