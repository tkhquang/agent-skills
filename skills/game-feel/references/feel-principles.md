# Feel principles and supporting elements

Contents: principles in depth, input, sensitivity, context, metaphor, rules, measuring, response targets.

## The principles

### Predictable results

The player gets the response they expected. This does not mean easy or simple. It means nothing comes between intent and outcome. If controls feel random, practice is pointless and people stop.

The difficulty is that computers are exact and people are not. The game sees one button fourteen milliseconds before another. The player believes they pressed both together. Shape expectations through mapping, representation and art, and resolve close calls according to what the player perceived.

Pitfalls:

- Control ambiguity. Two inputs pressed almost together produce different moves depending on which registered first, so the same action seems to give random results. Decide what simultaneous presses mean and make that rule robust to small timing differences.
- State overwhelm. Many states, each remapping every button, with transitions the player cannot see. A newcomer has no idea why the same button did something else, and falls back on mashing. Keep the number of states learnable and make each visibly distinct.
- Staging. If the result of an input happens too fast or is lost among other motion, the player cannot tell what they did. Show one idea at a time and exaggerate it.

Predictability includes inference. The first minutes should let the player correctly guess how the rest of the game behaves.

### Instantaneous response

Some obvious result within about 70 to 100 ms. This is different from a short attack: a vehicle can take seconds to settle into a turn and still feel responsive if the largest, clearest change comes right after the input. Ease in too slowly and it feels sluggish.

### Easy but deep

Low floor, high ceiling.

- Easy: natural mappings where the on-screen motion matches the physical motion of the control, established conventions, tutorials, assists.
- Deep is the hard part and cannot be guaranteed. Ways to add it: increase input or response sensitivity so there is more nuance to master, then support that nuance with goals and level layout.
- Cheap depth: time an action and show the result. Beating your own time unlocks layers of optimization from a simple move set.
- Competition between players, direct or through leaderboards, removes the ceiling entirely.

### Novelty

Predictable results, never exactly the same twice. The enemy is the canned response: an identical animation on the ten-thousandth press. Remedies: more varied contexts, new moves and states introduced over time, and simulation rich enough that tiny input differences produce different motion. Reality never repeats exactly, and motion that does looks wrong.

### Appealing response

Control should be engaging with all context removed, in an empty space. Layer animation and effects on the motion. Make every outcome watchable, especially failure, since that is where players spend much of their time. A crash that is fun to watch teaches without frustrating and pulls in bystanders.

### Organic motion

Good-feeling games draw curves. Setting position directly produces straight lines and instant stops, which read as rigid. Forces acting on a velocity produce arcs. Animation layered on top should follow arcs as well.

### Harmony

Every element supports one coherent physical reality. Players notice a wrong bounce or a limb clipping through a wall at once, and each lapse erodes belief.

The most common break is motion, such as a character running in place against a wall. One shooter turned pressing against walls into its central cover mechanic, which removed the awkward case.

### Ownership

After mastery, enough sensitivity and enough ways to use the environment let players improvise and express themselves. They start performing for style, sharing recordings and identifying with the game. With other players present, expression becomes communication.

## Input

- Each input has a number of states and axes. A button has two states. A trigger has many along one axis. A stick has two axes and effectively unlimited states. Sensitivity runs stick, then trigger, then button.
- Note which inputs can be combined. A directional pad cannot press left and right together. A keyboard can, so decide what that means.
- Physical quality matters. The same prototype usually feels better on a well-made controller than on keys.
- You rarely choose the device. You always choose which inputs to use and how.

## Input and response sensitivity

Overall expressiveness is the product of how sensitive the input is and how sensitive the response is.

| Input | Response | Result | Suits |
|---|---|---|---|
| Low | Low | Stiff, on or off, grid-like | Deliberate, contemplative games |
| Low | High | Fluid and expressive from simple buttons | Classic platformers |
| High | Low | Natural and immediate, nothing to master, no weight | Cursors, menus |
| High | High | Rich and demanding | Skill-centered action and simulation |

A sensitive device wasted on an on-or-off response feels flat. Simple buttons feeding a responsive simulation can feel wonderful.

## Context

Context is the simulated space: collision behavior plus the layout of the world. Constraints define sensation.

- Objects packed tightly relative to the avatar's speed and turning feel clumsy and oppressive.
- Objects far apart make the tuning irrelevant. Top speed and turning radius mean nothing on an empty plain.
- Spacing means nothing without collision. A dense forest the car passes through is not dense.
- Collision character changes everything: sliding off, sticking, bouncing, or exploding on contact. Instant death on touch makes the avatar feel fragile and steering paramount.
- Change the playfield and you change the game. A falling-block game three columns wide is a different game.
- Space gives the impression of speed and size through objects passing nearby.
- Build test spaces that exercise the mechanic: a place to reach top speed, tight turns, gaps at the edge of jump range, things to bump into.

## Metaphor

What the avatar looks like sets expectations before any input.

- People will say a horse does not feel like a horse without ever having ridden one. Their idea of a horse comes from everywhere.
- A realistic car is expected to handle, sound and crash like a car. A cartoon car can do almost anything.
- Swap the model without touching the tuning and the same motion feels different.

Choose a look whose expectations the game can meet or beat.

## Rules

Rules give motion a reason. Collectibles, health, timers and scores are arbitrary variables that make certain movements worth learning.

- High-level goals focus the player on a subset of motions.
- Mid-level rules change how movement feels in the moment: carrying the objective makes every step tense.
- Low-level rules read as physical properties: an enemy that dies in one hit feels fragile, one that takes twenty feels solid.

## Measuring

- Hard measures: frames or milliseconds from input to response, speeds, heights, distances, envelope timings.
- Soft measures: impressions, smiles, requests to keep playing.
- For a stubborn "it doesn't feel right", log input and output per frame and graph them. Problems such as a jump pressed just after leaving a ledge become visible immediately.
- Compare with a reference by measuring it the same way: film it, count frames, estimate distances in avatar heights.

## Response targets

Measure on the target hardware: film the controller and the screen together at a high frame rate and count frames.

| Task | Target |
|---|---|
| Fast, precise aiming | Keeps improving as end-to-end latency drops below 20 ms. A competitive shooter on mouse should not settle for 50 ms |
| Character action, platforming, driving | Comfortable at 50 to 100 ms if the delay is steady. Uneven delay feels worse than slightly higher steady delay |
| Slow or turn-based interaction | Tolerates more, and still needs an immediate acknowledgment of the press |

The controller, the display and any streaming link add delay the code cannot remove. On a television or a phone, the game's own share is smaller.
