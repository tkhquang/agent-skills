# Balance by simulation

Contents: what it answers, the harness, the opponent, fair comparisons, yardsticks, how many games, whole-game measures, reading results, limits.

## What it answers

Simulation plays the real rules many times with no rendering. Run it on the game's own rules code, never on a copy.

| Question | Run |
|---|---|
| Is moving first, or one seat, favored? | Mirror match: the same army on each side, each side first |
| Is a price right? | Equal budgets, with only one side holding the thing |
| Is one faction stronger? | Faction series at equal budgets, on each kind of map |
| Is one upgrade plainly better? | Each option against every rival at its price, and against its sibling |
| What is a new ability worth? | Random armies with and without it, against a yardstick |
| Does the whole game have the intended shape? | Full games with the opponent on every side |
| Can a player come back? | Full games, split by who lost the first big fight |

## The harness

- Runs headless from one command, with no window.
- One seed for each game. The same seed plays the same game. Every report line can be replayed.
- Any rule number can be changed for one run from the command line. The report header prints the changes.
- A new rule has a switch that brings the old rule back, so one build plays before and after.
- A turn limit. A game past it counts as "No result", apart from wins and losses.
- Setups are data files: map, pieces, positions, first side, seed.
- Filters rerun only the rows that a change touches, so a check takes seconds.
- The log of any one game can be written to a file.
- The target is printed beside each measure.

## The opponent

| Rule | Why |
|---|---|
| A short, documented list of priorities, the same for every side | A result should come from the armies |
| The same information as a player, fog included | Otherwise it measures a game nobody plays |
| No draws from the rules' dice. Give it none, or its own generator seeded from the game seed | Its choices must not shift later rolls |
| Ties broken as seen from its own side of the map | A mirrored setup must give a mirrored game. Test this |
| Uses counted for each mechanic | A mechanic the opponent never uses measures as worthless |

Fix the opponent before the numbers. In one strategy game, changes to the opponent alone (leave lost fights, avoid stronger squads) raised the games won by the side that lost the first clash from 36 to 54 of 160. Fail the run when the opponent repeats an impossible order.

## Fair comparisons

- Play every seed with sides swapped and with each side first.
- Reuse the same seeds for the baseline and the variant. This cuts variance when both versions spend the same roll on the same event. It can raise variance when a change pushes the rolls out of step, so check the paired interval.
- Do not trust a fixed matchup. With one fixed formation, 1 extra point of initiative turned 86 wins in 100 into 16. Shuffle formations by seed and use many random armies of equal budget.
- Report each map type on its own row before adding rows together.
- Change one thing for each run.
- Tune on one block of seeds and confirm on seeds and maps that no run has used.

## Yardsticks

A win rate is hard to act on. Measure a cheap, familiar unit under the same draws, then express everything in it.

1. Baseline: random armies, nothing changed. The first side should win about half.
2. Yardstick: the first side gets one more basic unit.
3. Variant: the first side gets the thing under test.
4. Worth = (variant minus baseline) / (yardstick minus baseline).

A result such as "0.6 of a basic unit" maps directly to a price.

## How many games

| Independent games | 95 percent margin near an even win rate |
|---|---|
| 100 | 10 points |
| 400 | 5 points |
| 600 | 4 points |
| 1,000 | 3 points |
| 2,500 | 2 points |

Games from one draw of armies depend on each other. Group them by draw.

```bash
# Interval for 345 wins in 600, and whether it is inside 40% to 60%
python scripts/sim_stats.py rate --wins 345 --games 600

# Games needed for a margin of 4 points, or to detect a change of 5 points
python scripts/sim_stats.py games --margin 4%
python scripts/sim_stats.py games --diff 5%

# Same seeds under both versions. Columns: seed, base, variant
python scripts/sim_stats.py paired --csv results.csv
```

"Undecided" means more games, not a pass.

## Whole-game measures (example: turn-based strategy)

| Measure | Shows |
|---|---|
| Share of games with no result, and when the rest end | Stalls and pace |
| Wins by first mover, faction, leader, map size | Hidden advantages |
| Day of first contact, fights for each week | Dead time |
| Days on which a side did nothing | Waiting |
| Games won by whoever took the first objective | A decisive opening |
| Games won by the loser of the first clash | Room for a comeback |
| Share of fights where the winner brought 1.5 times the force or more | Fights decided before they start |
| Currency held, in weeks of income | Sinks and sources |
| Options taken into service, and the share of the commonest loadout | Dead and dominant options |
| Turns on which nobody lost health | Healing or defense that stalls |
| Thinking time for each side and turn | Cost on the player's machine |

Print the median with the earliest and latest, or with the lower and upper quarter. A mean hides the games that went wrong.

## Reading results

| Result | Check first |
|---|---|
| One option beats one other 80 to 20 | Counters do that. It is a fault only when the option wins most of its matchups at its price |
| Even overall | Split by leader, map and first mover. In one roster, the same soldiers won from 13 to 72 fights in 100 depending on the leader |
| A mechanic has no effect | Use count, then price, then whether the opponent times it well |
| A row moved and nothing related changed | The margin, then the seeds, then a fixed setup |
| A strong side loses oddly | Read one full log before changing a number |
| Everyone brings the same loadout | Score options by the situation, or restrict who knows them |

Report: question, command, seeds, games, rule changes, result with its interval, target, verdict, what one read log showed, next change.

## Limits

- The opponent is not a person. It shows large faults and the direction of a change.
- Nothing here measures fun, clarity, bluffing or learning. Playtest after the numbers settle.
- Simulated percentages are not predictions of live win rates.
- A search with one right answer, such as a puzzle, needs a solver instead. See `game-systems-design`.
