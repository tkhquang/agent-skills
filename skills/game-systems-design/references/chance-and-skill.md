# Chance and skill

Contents: what randomness is for, sources of randomness, measured randomness, kinds of skill, mixing them for an audience, exchange rules, checks.

## What randomness is for

Randomness earns its place by doing one or more of these jobs.

1. Delaying or preventing solvability. A small deterministic game gets solved and dies. With randomness the same decisions lead to different outcomes.
2. Keeping mismatched players in the same game. The weaker player has a chance, and the loser can blame luck.
3. Increasing variety. Random setups and draws mean no memorized openings.
4. Creating dramatic moments. A plan that hangs on one roll is tense in proportion to what is riding on it.
5. Enriching decisions. With uncertainty there is no always-correct move, only risks to weigh.

It also stands in for detail you chose not to simulate: a damage range replaces a thousand small factors.

## Sources of randomness

| Source | Behavior | Notes |
|---|---|---|
| One die | Flat: every face equally likely | As random as it gets |
| Several dice summed | Bell-shaped: middle values common, extremes rare | More dice means less swing. More faces means wider range |
| Cards or tiles from a finite pool | Each draw changes the odds of the rest until a reshuffle | Players can count. Reshuffling after every draw equals a die |
| Software random numbers | Any distribution you want | Verify shuffles and distributions are actually fair. Real games have shipped biased shuffles |
| Hidden information | Not random to its owner, random to everyone else | Hands, fog of war, simultaneous secret choices |
| Other players | Unpredictable intentions | Enough on its own for many games |
| Sensitive simulation | Tiny input differences give different results | Physics games |

Dice have no memory. Ten fives in a row do not change the next roll. Do not design around hot or cold streaks, and do expect players to believe in them.

## Measured randomness

A random element is measured when its nature is known and players can plan around it. Over many trials luck evens out and skill decides: a card game played for one hand is a gamble, and the same game played for a hundred hands is a skill contest.

Practical rules:

- Many small random events favor skill. A few large ones favor luck.
- Put the randomness before the decision when you want strategy (deal, then choose). Put it after when you want tension (choose, then roll).
- Let skill govern how randomness is used. Random card draws become skill when the player chooses when to cash them in.
- Show the odds or make them learnable. Hidden plus random together reads as arbitrary.
- Too much pure randomness makes players feel their actions do not matter.

Pure-chance games exist in two places. Children's games use building tension resolved by chance, sudden reversals and the constant possibility of coming from behind. Gambling games need real stakes and offer choices that give a feeling of control without changing the odds.

## Kinds of skill

### Strategic skill

Thinking decisions with time to consider. See `decisions.md`. Difficulty here is a question of depth.

### Twitch skill

Execution under time pressure. The correct action is usually obvious and the challenge is doing it fast and accurately. Types:

- Pure speed: do it as fast as possible, or as many times as possible.
- Timing: hit the right moment.
- Precision: hit the right place.
- Avoidance: stay away from threats. Harder when the view is limited and locating threats is part of the task.
- Time pressure: a limit applied to any task, explicit or implied. The same rules with a clock are a different game.

Time pressure can rescue an obvious decision: trivially easy questions become hard to answer correctly at speed.

Tuning twitch challenge:

- Every type scales: required reaction time, width of the timing window, aim forgiveness or assistance, number of threats, length of the limit.
- Offer difficulty levels, or adjust difficulty during play based on how the player is doing, or ramp steadily until the player is overwhelmed.

## Mixing for an audience

Every game is dominated by one of chance, twitch skill or strategic skill, even when it contains all of them.

| Audience | What they want | Mix |
|---|---|---|
| Young children | To win, including against adults | Mostly luck, few or no decisions, each turn self-contained |
| Families | Everyone can play and anyone can win | Short playtime, simple rules, some luck, a few real decisions for adults |
| Social players | The time together | Tolerate a lot of luck, still need decisions that affect each other |
| Competitive players | To prove skill | Mostly skill, a little luck for variety and face-saving |
| Professional play | Consistent results for the best | Skill clearly outweighs luck |

A family game is not a children's game. Designing for the lowest common denominator pleases the youngest at everyone else's expense.

Compatibility:

- Adding luck to a twitch game feels like robbery. A perfect shot spoiled by a random jam is not fun.
- Adding heavy strategy to a twitch game breaks the rush.
- Adding small twitch moments to a strategy game makes a welcome break.
- Adding luck to a strategy game widens the audience. Too much removes the pride of winning.
- A twitch challenge beyond a player's ability behaves as luck for that player. Very hard execution elements widen the gap between beginners and experts.

The more luck, the more level the field, and the wider the skill gap that can still produce a good match.

## Exchange rules

All tuning comes down to adding or removing random elements and adding or removing decisions.

| To get | Change | Example |
|---|---|---|
| Less luck, same simplicity | Random element to automatic rule | "Move 1d6" becomes "move one space" |
| Less luck, more skill | Random element to decision | "Move 1d6" becomes "move one to three spaces, your choice" |
| More skill | Automatic rule to decision | "Roll and move" becomes "pay to roll three dice and keep two" |
| More luck | Decision to random element | "Choose a target" becomes "draw a target card" |
| More variety without more luck | Random setup, deterministic play | Shuffle the map, then no dice |
| More tension | Decision first, random resolution after | Commit, then roll |

## Checks

- Can a stronger player still lose to a weaker one sometimes, and does that suit the audience?
- After a loss can the player tell what was luck and what was their own choice?
- Is any single random event able to decide the whole game?
- Does the player get to respond to bad luck, or only watch it?
- For three-player games: can two gang up on one, or can one run away? Consider a neutral randomly driven fourth force, or a catch-up rule.
