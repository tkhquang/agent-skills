---
name: game-systems-design
description: Designs and critiques game mechanics as interacting systems. Covers core loops, feedback loops, engines, economies and ecologies, meaningful decisions, randomness versus skill, puzzle design, solver-checked and generated levels, multiplayer and co-op structure. Use when the user is designing or reviewing mechanics, a core loop, resources, crafting, combat, progression, a skill tree, NPC or AI behavior, puzzles, level generation, proving that levels can be solved, dice or card randomness, co-op, PvP or drop-in multiplayer rules, or says a game feels shallow, solved, confusing, overwhelming, snowbally, or like "the choices don't matter".
license: MIT
---

# Game systems design

A game is what happens when parts with their own state and behaviors affect each other in loops, and a player joins the loop. The designer builds a space of possible play, not one path through it.

Reason about loops, because a feature list cannot show whether a game snowballs, stalls, collapses into one strategy or stays interesting on the hundredth play.

Be concrete: name the parts, the resources and the arrows.

## Workflow for designing a system

1. State the experience. Finish "In this game the player is a..." and "This game is about...". Say what the system is for in terms of that experience before writing rules.
2. List the parts. For each, write attributes and behaviors: what resource it creates, changes, moves or destroys. A part delivers an effect and the receiver decides its own response.
3. Draw the loops. Mark sources, stocks and sinks for each resource. Label each loop reinforcing or balancing. Every part should both affect something and be affected. A one-way arrow is a missed loop.
4. Classify the structure. Engines invest a resource for more of the same later. Economies gain by converting or exchanging different resources. Ecologies hold resources in dynamic balance. Most games nest all of them. See `references/loops-engines-economies.md`.
5. Audit the decisions the player makes in a typical minute and a typical hour. See `references/decisions.md`.
6. Stack the timescales: every second, every minute, every session, across weeks. Do not demand fast reactions and deep planning in the same moment.
7. Check feedback. Every behavior the player triggers or needs to know about gets clear, immediate feedback. If a state change is not worth feedback, question whether it belongs.
8. Remove exceptions and special cases. Prefer a few rules that combine. Make low-level systems resemble high-level ones so learning transfers.
9. If more than one person plays, settle player count, shared or opposing goals, joining and leaving, play with too few people, and bad-faith behavior. See `references/multiplayer.md`.
10. Hand numbers to `game-balance`, then prototype and watch people play.

## Loop types and how they fail

| Structure | What it is | Fails as | Usual fix |
|---|---|---|---|
| Boosting engine | Invest now for more of the same later. Builders, deck building, production | Runaway leader. Deadlock when the output is needed to start. One dominant build order | A balancing loop, seed resources, several viable paths |
| Braking engine | A drain that scales with success. Stamina, upkeep, repairs | Too strong, and the game halts | Loosen until the growth loop clearly wins |
| Economy | Gain by exchange or conversion. Loot for gear, crafting, trading | Inflation, stagnation, runaway rich | Sinks, more to buy, catch-up rules, new conversions over time |
| Ecology | Parts keep each other in check. Counters, factions, inventory space | Static and dull, or collapse after one element dominates | Three or more mutually checking sides. Do not patch one overpowered thing with another |

## Decision quality

Label each decision obvious, meaningless, blind, tradeoff, dilemma or risk versus reward. Signs and repairs: `references/decisions.md`.

A strong decision involves a tradeoff, depends on the situation, allows a personal style, and has lasting effects the player had the information to foresee. Acknowledge every decision with feedback.

## Diagnosing a design

| Complaint | Look for | Direction |
|---|---|---|
| "The choices don't matter" | Obvious, meaningless or blind decisions. Outcomes that reset whatever the player did | Rebuild as tradeoffs with lasting, visible effects |
| "There's one best strategy" | A dominant option | Give each option a niche, add counters, vary the situation. Check with `dominance` in `game-balance` |
| "Whoever gets ahead wins" | Unchecked reinforcing loop | Costs that scale with the lead, catch-up tools, shared threats |
| "It drags and nobody can finish" | Balancing loops dominate | Strengthen growth, add an escalation clock |
| "It's a grind" | Chains of explicit goals with rewards and no decisions | Add decisions to the repeated activity, let players set goals, add a loop at another timescale |
| "It's shallow" | Few loops, nothing to learn after the first hour | Turn parts into subsystems and reveal them gradually |
| "It's overwhelming" | Too many new things at once. Fast and slow demands collide | One system at a time. Separate action from planning in time |
| "It's confusing" | Rules with exceptions. Missing or inconsistent feedback | Remove special cases, make every state change visible |
| "It's solved" | Deterministic, small possibility space | Hidden information, measured randomness, other players |
| "It's all luck" | Few, large random events with no way to plan around them | Many small random events, visible odds, choices after the roll |
| "Some levels are trivial and some are walls" | Length used as difficulty. No measured curve | Solver measures and bands. See `references/solver-checked-levels.md` |
| "Money is worthless late game" | Sources outgrow sinks | Scaling sinks, item wear, storage limits, new things to buy |
| "Our content runs out" | Authored, play-once design | Shift weight from content to interacting systems |
| "The match is ruined when someone leaves" | No rule for drop-outs, late joiners or reconnection | Choose bot, short-handed scaling or an open slot on purpose |
| "It's dead unless the server is full" | Content tuned for one player count | Scale to players present. Define the smallest fun count and a fallback below it |
| "One player wrecks it for everyone" | A rule that lets players affect each other without limit or consent | Remove the mechanical route first, then add block, report and opt-in conflict |
| "The game got worse after we fixed X" | A delayed outer loop undoing the quick fix | Trace the second-order loop before patching |

## Principles

- If only one route through the game is viable, the player has nothing to decide.
- More realism or complexity does not make a better game. The player must be able to build a mental model.
- Decisions need uncertainty: randomness, hidden information or other people.
- Prefer a general rule to a scripted moment. "Downed enemies drop pickups" creates a thousand situations. A scripted ambush creates one.
- Explicit goals get players started. Games last when players set their own.
- Narrative delivers information in arcs, not loops. Use it for context and reward, and make what the player does between story beats matter.
- Urgent, flashy demands take attention before thoughtful ones can.

## References

- `references/systems-model.md`: parts, loops, emergence, vocabulary, interactive loops, the attention budget, goals.
- `references/loops-engines-economies.md`: engines, economies, ecologies, progression, combat, common system types.
- `references/decisions.md`: decision types, mechanics that create tradeoffs, presenting and pacing decisions, an audit procedure.
- `references/chance-and-skill.md`: jobs of randomness, kinds of randomness, strategy versus dexterity, tuning the mix for an audience.
- `references/puzzles.md`: puzzle traits, types, difficulty levers, stuck points.
- `references/solver-checked-levels.md`: solver measures, difficulty bands, level generation, checks for every level, hints.
- `references/multiplayer.md`: player counts, co-op and competitive structure, joining and leaving, low population, players who spoil sessions.

## Output formats

- New system: purpose in player terms, parts table (attributes, behaviors), resource flows, loops labeled reinforcing or balancing, the decisions it creates and their type, feedback list, risks with the loop behind each, and the first thing to prototype.
- Critique: the loop map as you understand it, the most serious systemic problems with the mechanism behind each, and the smallest rule change that would test each fix.

## Related skills

`game-balance` for numbers and curves, `game-feel` for second-to-second control, `game-concept-prototyping` for testing the idea, `game-retention-monetization` for long-term structure in service games.
