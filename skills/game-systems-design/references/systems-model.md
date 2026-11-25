# The systems model of a game

Contents: parts, loops, wholes; structure of a game; emergence; interactive loops; the attention budget; goals.

## Parts, loops, wholes

A system is a set of parts that form loops of interaction, creating a persistent whole with properties no single part has.

### Parts

Each part has:

- State: attributes with values at a moment in time. A monster has 10 hit points and a name.
- Boundary: what is inside the part. Test: if it can change the part's overall behavior it is inside.
- Behaviors: what it does to other parts, usually by creating, changing, moving or destroying a resource.

Rules for good parts:

- Encapsulate. One part perturbs another. The receiver decides its own response. A cannon delivers 20 damage. The target ship decides whether that means lost crew, lost sails or sinking.
- Bring every part down to attribute and value pairs before building. This level of specificity is the floor of a design, not its ceiling.
- Group simple parts into subsystems where you can. A forest's health can be the aggregate of its trees.

### Resource plumbing

- Source: creates a resource at some rate. In games it is usually treated as inexhaustible.
- Stock: holds an amount. May have a cap.
- Sink: removes a resource. An empty stock cannot be drained.
- Converter: turns one resource into another.
- Decider: measures something and branches, which is how feedback enters.

A "faucet and drain" economy is this picture at game scale. If faucets outrun drains, the resource loses value.

### Collections, complicated processes, complex systems

- Collection: parts that do not affect each other. Not a system.
- Complicated process: parts connected in a line. Predictable, repeatable, traceable to a root cause. A sequence of levels where level ten never affects level two. Needs a lot of content because each piece is used once.
- Complex system: parts connected in loops, so each part affects its own future. Unpredictable in detail, stable in pattern. Cannot be understood by taking it apart.

### Loops

- Reinforcing loops amplify. Interest on a balance. Cash buys property that earns cash. In play they reward the leader, magnify early success and destabilize.
- Balancing loops dampen. A thermostat. Experience needed per level rising each level. A catch-up item that targets first place. In play they forgive, stabilize and prolong.
- A system needs at least one main reinforcing loop or it fades out. Healthy systems combine both kinds.
- Loops produce nonlinear results. Predator and prey populations oscillate because each kill also removes future offspring: the effect multiplies instead of adding.

Classic loop traps, useful as a checklist when a design misbehaves:

| Trap | Shape | Game example |
|---|---|---|
| Fixes that fail | A quick balancing fix plus a delayed reinforcing loop that brings the problem back worse | Massing cheap units now and falling behind an opponent who invested in better units |
| Limits to growth | A reinforcing loop meets a balancing loop on a resource it depletes. S-curve, sometimes a crash | Expansion that outgrows its food or upkeep |
| Tragedy of the commons | Each actor's private gain drains a shared resource | Every player overhunting the same herd |
| Vicious cycle | A reinforcing loop running downward | Losing units reduces income which loses more units |
| Cascade | One change propagates through several linked loops | Removing a top predator changes the whole map |

### Wholes and emergence

When loops reach a dynamic balance, a stable pattern appears that is not found in any part and is not a simple sum: a flock, a school of fish, a market, a metagame. Causation runs upward (parts produce the whole) and downward (the whole changes how parts behave, as when a falling market makes individuals sell).

Emergence in games comes from behaviors that are local, modular and generic.

- A few rules per bird produce flocking: match neighbors' heading, avoid collisions, move toward the local center.
- Creatures that like to stack plus creatures that seek food produce escapes from pens that nobody scripted.
- A creature that moves food it cannot eat toward other food is read by players as stealing or as gift giving.
- Spilled drink, self-grooming animals and body weight, each modeled separately, produced an epidemic of tavern cats dying of alcohol in a famously systemic simulation.

A scripted behavior such as "walk this character from their quarters to the command room" does one job once. "Open door", "unlock door" and "go to" as separate small behaviors recombine forever.

## Structure of a game as a system

- Structure: tokens (the nouns: anything with state and behavior, including abstract things like a turn or a hand size) and rules (the verbs). A mechanic is a meaningful combination of the two.
- Function: the loops that tokens and rules create when running. This is what people usually mean by "the game systems". Think of each as "a machine that does X", built from smaller machines.
- Whole: architecture (the developer-facing side: balance of content and systems, narrative structure, interface organization, platform) and theme (the player-facing side: what the game is about and how it feels).

Use as few rules as possible to define the space. Too few and the game is ambiguous. Too many and the player has no agency. Avoid exceptions: the same token and rule should not mean different things in different cases, and similar inputs should have similar results.

Content-driven designs are authored, linear and consumed. Systemic designs are replayable because the space is large. Every game mixes both. A reskin with the same parts and rules holds players only until they notice there is nothing new to learn.

Theme has to connect to the systems. A technically deep world with no goals to form falls flat. A beautiful abstract engine with a pasted-on theme loses anyone who does not love the mechanics for their own sake.

## Interactive loops

Every loop between player and game runs intent, action, state change, feedback. They differ in speed and in the mental resources they use, and they run at the same time, nested.

| Loop | Timescale | Attention used | What it feels like | Design notes |
|---|---|---|---|---|
| Action and feedback | Under a second to a few seconds | Reflexive | Running, jumping, shooting, tapping | Feels instant under 100 ms. The link breaks past about 250 ms. This is the carrier wave for everything else |
| Short-term cognitive | Seconds to a minute or two | Deliberate | Puzzles, tactics | Needs readable state and quick resolution |
| Long-term cognitive | Minutes to hours | Deliberate, planning | Strategy, builds, goals | Needs predictable rules and layered depth to plan around |
| Social | Hours to weeks | Deliberate and reflective | Belonging, status, cooperation, rivalry | Needs players to need each other: shared objects to play with, competition, formal groups, complementary roles, reciprocity |
| Emotional | Minutes to hours and longer | Reflective | Dread, guilt, loss, pride, awe | Emotions follow motivations. Give the player something to gain, keep or protect, then put it at risk |
| Cultural | Long after play | Reflective | Seeing values or history differently | Rare. Arises when rules make the player complicit in something worth questioning |

Useful consequences:

- Ask "what is the player doing in every moment?" and insist on an answer in present-tense verbs.
- Games built on fast loops feel light: easy to pick up, easy to drop. Loyalty that lasts years comes from the slow loops.
- Stack loops of different lengths so tension and release alternate. One well-known shooter was built as a three-second loop inside a thirty-second loop inside a three-minute loop, each varying.
- Formal groups such as guilds hold players far longer than casual proximity grouping.
- Asynchronous "visiting" with no real interaction does not satisfy social motives.
- For emotion, prefer situations that arise from systems over cutscenes. Cutscenes are more reliable. System-born moments are more personal.
- Narrative that bookends missions without being changed by them teaches the player that their choices do not matter.

## The attention budget

A player has a limited amount of attention, and the fast drives out the slow. Reflexive demands are served first, then deliberate thought, then reflection.

- No successful game is both extremely frantic and extremely strategic at the same moment.
- A high-action game can have long-term planning or social play if it happens at a different time: between fights, in a lobby, on a map screen.
- A long-term strategy game should keep fast demands low. It can look calm on purpose.
- A game aiming for emotional weight should keep its mechanics and presentation spare.
- Feedback volume should match: action games can flood the senses, planning games should not.
- A game that makes the player learn new controls, new rules, new terrain, new enemies and new powers all at once will lose most players at the first checkpoint.

## Goals

- Explicit goals are given by the game. Implicit goals are made by the player. Games with only explicit goals have shorter lives.
- Goals nest by timescale: instant, short term, long term, plus social and emotional goals.
- An activity done only for an outside reward stops being play. A chain of such tasks is what players call the grind.
- Adding explicit goals and a progression system is the standard way to turn a toy into a game.
