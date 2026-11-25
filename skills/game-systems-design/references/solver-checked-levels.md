# Solver-checked levels

Contents: when it fits, what to measure, how the search works, a difficulty curve in bands, generating levels, checks for every level, use inside the game, testing a rule set early, traps.

## When it fits

Use it for a puzzle with discrete states, fixed rules and a state space small enough to search. The solver and the game must call the same rules code. For physics, hidden information or an opponent, use simulation instead (`game-balance`).

## What to measure

| Measure | Meaning | Use |
|---|---|---|
| Par | Fewest moves to the goal | Length, rating thresholds |
| Shortest solutions | Number of move sequences of par length that reach the goal | Few is tight. Many feels obvious |
| Dead first moves | Share of opening moves after which no solution exists | Cost of guessing |
| Key idea needed | No solution of par length exists without the idea | Proves the level teaches it |
| Reachable positions | Size of the search | Keeps checks fast in the game |
| Still solvable | Share of reachable positions with a solution | How often players get stuck |
| Blind solve | Share of random move sequences that reach the goal | High means no planning is needed |

## How the search works

1. Search breadth first from the start. Record every edge.
2. Treat identical pieces as interchangeable, so equal positions are stored once.
3. Search back from the goal positions over the recorded edges. A position not reached is dead.
4. Count shortest solutions from the goal outward: a goal counts 1, and any other position counts the sum of its next positions that are one step closer to the goal.
5. To test a key idea, search again without the moves that use it and compare lengths.
6. Stop at a position limit and report "Unknown". Never report "No solution" at the limit.

## Difficulty in bands

Write the curve as data and check levels against it.

| Field | Rule |
|---|---|
| Elements | The pieces and rules a level of this band may use |
| New element | At most one, introduced in the first level of the band, with few other pieces |
| Par range | Lowest and highest par |
| Rest level | The first level of a band has a lower par |
| Gentle limits | Early bands: a ceiling on dead first moves and at least two shortest solutions |
| Tight limits | Late bands: a ceiling on shortest solutions and a floor on dead first moves |

- Length is not difficulty. In one game, long levels with many shortest solutions felt obvious in play, so late bands got a ceiling of 4 and a floor of half the openings dead.
- Watch the step between bands. In the same game, tutorial levels needed 1 move and the next level needed 3, with half its openings dead. On the first public day most players stopped after about 2 minutes, so a gentle band was added between them.
- A rest level can be short and still tight.

## Generating levels

1. Input: piece set, board size, obstacle rate, seed range. The same input and seed always give the same candidate.
2. Build the board from the seed, then solve it. Drop candidates with no solution or over the position limit.
3. Keep by the band rules.
4. Rank: key idea needed, then fewer shortest solutions, then more dead first moves, then lower seed.
5. A person plays each candidate to the end, then keeps, edits or rejects it. Record the date and the seed in the level data.

Log how many candidates each input keeps. In one game, small boards with a strong piece gave tight levels, and larger boards mostly gave pieces that could go home in any order. Keep the generator out of the shipped build and check that it stays out.

## Checks for every level

Run on every change to levels or rules:

- A solution exists, and the stored par equals the solver's par.
- The solver's path, played through the real game state, completes the level with the top rating.
- A second, plain search without the solver's shortcuts finds no shorter path.
- The level fits its band, and the first level of a band shows its new element.
- The level stays inside the position limit.
- No two levels share a layout.
- The level has a recorded human play.
- The identifier is valid and in the order list at most once.

## Use inside the game

| Feature | Rule |
|---|---|
| Stuck warning | Search from the current position, off the main thread. On "Unknown", say nothing |
| Hint | Show the first move of a shortest solution from the current position. The player still makes the move |
| Tutorial | Check that the shown move belongs to a shortest solution |
| Player-made levels | Same proof, and the author must complete the level before it goes live |
| Leaderboards | Replay the submitted moves with the same rules before accepting a result |

## Testing a rule set early

Before building a prototype, run the measures on random boards for each rule variant. Useful comparisons: share of boards with a solution, median par, still solvable, blind solve, key idea needed, next positions for each move.

- In one concept test, adding one piece type raised the positions that were still solvable from 2 to 4 percent to 9 to 21 percent, so the piece became part of the core.
- Doubling the directions of a move barely raised depth and made the search 1.5 to 2.1 times larger, so it was dropped.
- Write kill criteria as numbers the probe can return, next to those only a player can.
- A random board is not a designed level. The numbers compare rule sets. They do not predict what players do.

## Traps

- A solver measures rules. It cannot see whether a player can read or predict a move.
- A solver test on trivial levels passes anything. Include levels known to be unsolvable, too long and off band.
- A regenerated par file hides a rule change. Fail when a stored par differs, and review each change.
