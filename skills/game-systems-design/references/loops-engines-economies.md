# Engines, economies, ecologies

Contents: core loops, loop structures with failure modes, combining them, common system types, checklist for a new system.

## Core loops

A core loop is the interactive loop the player's attention is mainly on: form an intent, act, the game state changes, feedback arrives (often with a reward or a new ability), which seeds the next intent.

- A game needs at least one. Most have several at different timescales, called inner and outer loops.
- "Core" means most important to the experience at that moment, not necessarily the fastest.
- A proven shape pairs a tense, fast loop with a calm, slow one: battle with build, puzzle with decorate, mission with base management.

Example, a base-building strategy game: collect resources, build and train, battle, collect again.

- Battle is short and tense. Building is slow and restful.
- Every purchase is both reinforcing (more or better units) and balancing (the resources are gone for anything else).
- Goals nest: "upgrade storage so I can upgrade the hall so I can upgrade the barracks".
- An outer social loop (a clan) adds a longer timescale.

Example, a card battler: two reinforcing loops, one against the game and one against players, each limited by its own braking resource (stamina, attack points). An outer loop of fusing and improving cards gives fast, satisfying feedback and long-term tradeoffs, and it is what makes players want to battle again.

A mechanic is a recognizable interactive loop that is independent of any one game: draw a card, control territory, push your luck. Recurring mechanics define a genre and help players build a mental model quickly.

## Engines: same resource

### Boosting engines (reinforcing)

A source produces a resource. The player chooses between spending it to act now and investing it to increase future flow. Examples: buying property that pays rent, buying cards that make later buys cheaper, building production buildings instead of units.

The interesting decision is when to invest and when to act. Invest too little and you fall behind. Invest too much and you lose before the engine pays off.

Failure modes:

| Problem | Cause | Fix |
|---|---|---|
| Runaway leader | Reinforcing loop with no counterweight; a small early lead compounds | Catch-up mechanisms, costs that scale with size, shared threats to the leader |
| Stall or deadlock | Too little seed resource, or the loop's output is required to start the loop | Guaranteed minimum income, an alternate entry path |
| Content exhaustion | Units are cheap and permanent, so everything goes into investment and players burn through the tech tree | Upkeep or attrition, more than one axis of growth. Exponential costs delay the problem and do not remove it |
| Dominant strategy | Balance tuned so tightly that one build order is always best | Several viable paths, situational advantages, counters |

### Braking engines (balancing)

A drain that removes a resource, often in proportion to success. Stamina, upkeep, repair bills, taxes. They appear inside other loops as friction. A penalty that scales with holdings hurts leaders more than trailers and therefore also acts as catch-up.

Failure mode: if the brake overpowers the main growth loop, players cannot act and the game grinds to a halt.

## Economies: reinforcing by exchange

Value grows by exchanging or converting different resources. Trade wood for bread to feed workers who cut more wood. Build a sawmill so wood becomes lumber worth twice as much bread.

What makes economies engaging:

- Conversion decisions have real costs: the build investment, workers taken off other jobs, time, and the payback period.
- Unfolding complexity: introduce new resources, buildings and conversions over time. Production chains (ore to iron to steel to tools) give the player a growing model to master and a sense of discovery.
- Specialization and trade between players.
- Currencies: a resource that is exchanged instead of consumed and can buy many things. It gives a reward that is also a set of choices. Players must perceive it as valuable.

Many core loops are economies in disguise. In a typical role-playing game the player trades time and health for experience and loot on an unpredictable reward schedule, then trades loot for power. Unpredictable rewards hold attention more strongly than regular ones, which is useful and deserves care.

Failure modes:

| Problem | Cause | Fix |
|---|---|---|
| Runaway rich | One player captures the growth loop | Catch-up rules, a blocker other players can aim at leaders, turn order that favors those behind |
| Numbers stop meaning anything | Exponential growth outruns human intuition | A reset loop that converts progress into a permanent multiplier and starts over |

Inflation, stagnation, arbitrage and price setting: `economy.md` in `game-balance`.

## Ecologies: balancing by exchange

Parts trade resources in a way that holds each other in check. The target is dynamic balance, not stillness: every part keeps changing while the whole stays recognizable.

Examples:

- Predator and prey populations.
- Inventory: items compete with free space.
- Combat: sides try to reduce each other, and the winner's reward feeds the larger economy.
- Factions: three mutually hostile sides stay balanced because two will gang up on a leader. Two sides tend to tip, since players flock to the winner.

Failure modes:

- Too static. If nothing can shift, there is nothing to learn or decide.
- Brittle collapse. Past some point the system cannot rebalance. An overpowered unit behaves like an invasive species: everyone uses it and the decision space collapses.
- Oversteer. Countering one overpowered element with another that is also too strong, then countering that.
- Clamping out all variation. A system forced to one fixed value cannot absorb any outside disturbance.

## Combining structures

Most games nest all of them. A role-playing game is, at the top, a reinforcing economy of character power. Inside it sit a skill engine (where to invest points), an item economy (craft, trade, sell), an inventory ecology, a party economy of complementary roles, a combat ecology, and braking engines that pace everything.

- Parallel systems give breadth: more kinds of things to do.
- Nested systems give depth: the player can zoom in and out.
- Reveal systems one at a time. Each reveal gives new knowledge, new decisions and a sense of progress.

## Common system types

| System | Dominant structure | Key design points |
|---|---|---|
| Progression | Economy or engine | Think in reward per unit time. Rates usually have to rise to stay ahead of habituation, which pushes toward exponential curves and inflation. Always keep a visible goal beyond the current one: wanting drives engagement more than having |
| Combat | Ecology | Fast action and tactics. Needs a surrounding growth loop for long-term purpose. Combat with no player decisions weakens engagement even when the outer loop is strong |
| Construction and crafting | Engines and economies | Long-term planning. Often a support system inside progression |
| Skill and tech trees | Limited engines | Points earned then invested. The tree shape creates identity and long-term goals |
| Social and political | Ecologies | Groups balancing each other. Collapses if one side wins beyond challenge |
| Inventory | Ecology | A cap creates decisions and a secondary progression path as capacity grows |

Ways to fight habituation (the tenth reward of the same size feels like nothing):

- Limit sources: rarer drops, steeper requirements.
- Limit stock: carrying caps, which also create a new thing to upgrade.
- Increase sinks: items that wear out keep even ordinary finds valuable.

Designs that lean on content and ever-larger numbers eventually end. Designs with a strong balancing, ecological component can run far longer.

## Checklist for a new system

1. What is this system for, in terms of what the player feels and decides?
2. Which parts does it involve, and what are their attributes and behaviors?
3. Which resources flow, from which sources to which sinks?
4. Which loops form? Label each reinforcing or balancing. Which one dominates?
5. Where is the player's decision in the loop, and what kind of decision is it?
6. What limits growth? What prevents a halt?
7. What does the leader gain that the trailer does not, and what can the trailer do about it?
8. Which other systems does it feed and draw from?
9. What does the player see and hear at each step?
10. What is the cheapest prototype (often paper or a spreadsheet) that would show the loop running?
