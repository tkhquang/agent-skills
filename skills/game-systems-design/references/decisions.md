# Decisions

Contents: what makes a decision interesting, decision types and repairs, mechanics that create tradeoffs, presenting decisions, pacing, opposition, player types to weigh feedback from, audit procedure.

## What makes a decision interesting

A useful lens for most games: a game is a series of interesting decisions. It is easier to spot the uninteresting ones first. If players always pick the same option, or pick at random, the decision is not doing its job. The lens fits less well for rhythm and pure-reflex games, where execution is the point.

Traits of an interesting decision:

1. Tradeoff. Each option costs something. The big sword costs 500 gold. The fastest car handles worst.
2. Situational. The best answer depends on the current state of the game.
3. Personal style. A cautious player and an aggressive player can both choose well and differently.
4. Persistent. The effects last a while, on the condition that the player had enough information to choose. Early choices that can quietly ruin a game later must be presented with that weight.

Recurring flavors:

- Risk versus reward: potential penalty against possible gain.
- Short term versus long term: a quick unit now or a slow wonder with lasting impact.
- Multiple time horizons at once: juggling near, middle and far goals, and advancing the near ones to make the far ones reachable.
- Customization: even naming a city or picking a color connects the player to the game.

A decision is meaningful when the player believes it moves them toward or away from something they want, and when it changes the game state in a way they can perceive, opening some options and closing others.

## Decision types and repairs

| Type | Description | Example | Repair |
|---|---|---|---|
| Obvious | One option is clearly best | Move toward the helpful space; take the free piece | Automate it (auto-reload, passive regeneration) or add time pressure so it becomes a test of execution |
| Meaningless | No effect on the outcome | "Do you want to see the king?" where "no" loops back | Remove it. A perceived effect can carry a first playthrough and does not survive a second |
| Blind | It matters and there is nothing to base it on | Choosing a greeting for a stranger with no clues | Give partial information. Decisions that sharpen as information arrives are good |
| Tradeoff | Not enough resources for every goal | Weapon, armor or spell with one purse | Keep. Guard against one option quietly becoming dominant |
| Dilemma | Every option hurts | Pay money or lose maximum health | Keep, in moderation |
| Risk versus reward | Safe and small or risky and large | Leave a piece exposed for position | Keep. It produces natural drama: trailers gamble, leaders consolidate |
| Illusion of choice | Options differ in appearance only | Two doors to the same room | Remove or make the difference real |

The prisoner's dilemma family (cooperate or defect, with variants for repetition, many players, retaliation and hidden defectors) is a reliable source of tension in multiplayer design.

No choice at all turns the player into a spectator. Late in some classic board games the only instruction left is "roll and pay", which is when people start waiting for the game to end.

## Mechanics that create tradeoffs

- Auctions. Open (rising calls), sequential (one bid each in turn), sealed (simultaneous secret bids), fixed price (first to accept), descending price (first to accept as it falls), reverse (bid to avoid a penalty). Variations: lots, several auctions at once, everyone pays their bid, second place gets a consolation or a penalty, the winner pays the losers.
- Purchases with a limited budget and limited stock. What to buy and when, knowing it may not be there later.
- Limited-use abilities. Use it now for a known benefit or hold it for an unknown better moment.
- Abilities that grow while held. The longer you wait the stronger it gets, and waiting has a price.
- Explicit choices. "Gain 10 gold or heal 5."
- Limited actions. Several units, few orders per turn.
- Trading and negotiation. Promises that are binding, non-binding or breakable at a cost. Alliances.
- Position and timing. Where to stand, when to commit.

## Presenting decisions

- Players must understand the scope of what they are choosing. Having to pick and then wonder what it did is not fun. Err toward too much information.
- Lean on conventions. Familiar genre interfaces reassure. A familiar button that does something unfamiliar is disorienting.
- Lean on what players already know. Historical figures, pirates, railroads and zombies all arrive with built-in expectations. Reinforce them.
- Acknowledge every decision. Even a sound confirms the game noticed. Feedback makes the player feel responsible for what happens.
- Reinforce the fantasy in the feedback: you are the leader of a great nation, you are a great driver.
- Hidden information plus randomness together (an unknown weapon doing unknown random damage) frustrates. Players need to be able to reason about consequences.

Tuning levers for a decision that is not working: how much it affects the game, how much information the player gets, how long they have to decide, how many options there are.

## Pacing decisions

- Frequency matters. One decision every twenty minutes makes a different and usually weaker game than decisions every few seconds, even if the rare ones are big.
- Keep the player's mind busy with possibilities. The strongest position is several good options at once: "which of these good things do I do next?".
- Anticipation counts. A known decision ahead (the elevator ride, the corridor before a boss) holds attention through a quiet stretch.
- Complicated decisions arriving back to back make players feel out of control. Simple decisions at a slow pace bore them.
- Expect to cut. Experienced teams remove a third or more of what they try because it is not interesting enough.

## Opposition

Decisions need something to push against.

- The rules themselves: limits on movement, actions and resources. They should feel like part of the world, not arbitrary barriers.
- Active opponents controlled by the game.
- Other players.
- The player's own scarcity: not enough to do everything.

## Strategy and tactics

- Strategy is long-term planning. Tactics is short-term execution.
- Fast, reflex decisions can only be tactical. Strategy games should be built on tradeoffs.
- Pure-skill thinking games risk being solved. Pure-skill action games do not, because execution can always improve.

## Player types to weigh feedback from

Each is useful and each misleads if followed alone.

| Type | Cares about | Useful for | Risk |
|---|---|---|---|
| Winner | Winning | Tuning high difficulty | Over-hardening the game |
| Genre fan | Familiar conventions | Learning the conventions | Blocking anything new |
| System analyst | Understanding and calculating optimal play | Balance | Optimizing the fun away |
| Paranoid | Suspecting the game cheats | Spotting where randomness feels unfair | Chasing fairness that is already there |
| Accuracy buff | Fidelity to the source or history | Catching false notes | Realism over play |
| One bad experience | A single painful loss | Showing where setbacks are poorly explained | Overcorrecting for one incident |
| Armchair designer | The game they would have made | Occasional insight | Designing someone else's game |

Setbacks deserve special care. The player should understand why it happened and what they could do next time, because one bad incident can color the whole experience.

Designers also tend to assume everyone plays the way they do. Support as many styles as the design can carry.

## Audit procedure

1. Play or simulate ten minutes. Write every decision the player makes, however small.
2. For each: what are the options, what does the player know, what does it cost, how long does the effect last?
3. Label each with a type from the table.
4. Count decisions per minute and note any long gaps with neither a decision nor anticipation of one.
5. Fix in this order: remove meaningless ones, automate obvious ones, add information to blind ones, then check whether the remaining tradeoffs each have at least two options that a reasonable player would defend.
6. Check the feedback after each remaining decision.
