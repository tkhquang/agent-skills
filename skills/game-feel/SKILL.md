---
name: game-feel
description: Diagnoses and tunes how real-time controls feel. Works on the sensation of controlling a character, vehicle, cursor or camera using response envelopes (attack, sustain, release), input mapping, input forgiveness, collision and level spacing, and polish such as animation, particles, sound, screen shake and hit pause. Use when the user is building or tuning movement, jumping, aiming, driving, combat impact or camera, asks for "juice", or describes controls as floaty, stiff, sluggish, slippery, twitchy, unresponsive, weightless or "just not right", including when they only paste a character controller and ask why it feels off.
license: MIT
---

# Game feel

Game feel is real-time control of a virtual object in a simulated space, with interactions emphasized by polish.

Its parts are control (a continuous correction loop, like steering), space (things to move around and collide with), and polish (effects that change how an interaction is perceived without changing the simulation). Players cannot tell them apart, which is why a squash animation alone can make a stone ball read as a rubber one.

Feel is judged in the first minutes of play, and it is measurable. This skill turns words like "floaty" into specific numbers to change.

## What you can change

| Element | What it is | Question to ask |
|---|---|---|
| Input | The device and which of its inputs you use | How expressive is each input, and which combine? |
| Response | How each input changes a game parameter over time | What does it modulate, how fast, through what simulation? |
| Context | Collision and the spacing of the world | Does the space give the motion meaning without crowding it? |
| Polish | Animation, particles, sound, camera, rumble | What do the effects say about weight, material and force? |
| Metaphor | What the thing looks like | What does the player expect before touching it? |
| Rules | Goals that give motion a purpose | Which motions do the goals make worth learning? |

Most feel problems are response problems. Start there.

## Thresholds from human perception

A person's perceive, think, act cycle takes roughly 240 ms. The figures below mark where real-time control breaks down. They are outer bounds on a gradual curve, not targets.

| Threshold | Bound | Notes |
|---|---|---|
| Motion | Above 10 frames per second, 30 for smooth | Lower reads as a slideshow |
| Response | Input to visible result under about 100 ms | About 50 ms feels instant in most games. Above 100 ms lag is noticeable. Around 200 ms is sluggish. Past 240 ms control is broken |
| Continuity | Accept input and respond every 100 ms or less, consistently | Frame drops and long uninterruptible animations break the flow |

Response targets by task and device, and how to measure: `references/feel-principles.md`.

## Tuning workflow

1. Name the target feel in plain words ("tight and precise", "loose and flowing", "heavy and deliberate") and a reference game if there is one.
2. Inventory the motion: which inputs, which dimensions, linear or rotational, relative to what (avatar, camera, world), and whether input sets a position or a rate.
3. For each input, sketch the response envelope of the parameter it controls, usually speed.
   - Attack: time from input to full effect.
   - Sustain: the level held while the input is held.
   - Release: time back to rest after the input ends.
   - Decay: overshoot above the sustain level. Almost always a bug.
4. Compare the envelope with the target using the table below and change the specific phase.
5. Check ratios between parameters: ground speed to air speed, jump force to gravity, turning to grip. These carry more of the feel than any single value.
6. Check context. Space obstacles relative to how far and fast the avatar moves. Too tight feels clumsy. Too sparse makes the tuning irrelevant.
7. Add polish last, aimed at one overall impression. Do not start it before the motion feels right with plain shapes.
8. Test in an empty room. Good control is enjoyable with nothing to do.
9. Expose every tuning value for live editing and iterate while playing.

## From complaint to change

| It feels | Usual cause | Change |
|---|---|---|
| Unresponsive, laggy | No visible result within about 100 ms | Make the first frame show something obvious. A long attack is fine if it starts at once |
| Floaty | Long attack and release. Same gravity rising and falling | Shorten release, raise gravity on the way down, cap fall speed |
| Stiff, robotic | Position set directly. No attack or release. Straight-line motion | Drive a velocity with acceleration and drag |
| Twitchy | Very short linear attack. Stick mapped linearly | Curve the attack slightly. Use a non-linear stick response |
| Sluggish | Long attack with a slow start. Animation locks out input | Front-load the response. Let input interrupt wind-ups |
| Slippery | Long release, little friction | Raise drag. Use a stronger value for reversing direction |
| Weightless | Nothing conveys mass | Faster fall, landing squash and dust, low-end impact sound, small camera response |
| Random, unfair | Same input gives different results. State changes the player cannot see. No forgiveness at edges | Resolve close calls in the player's favor (coyote time, input buffering). Make states visually distinct |
| Shallow | Low input and response sensitivity | Let hold time, speed or state change what an input does |
| Samey after an hour | Identical response every time | Let the simulation add small variation. Add states and moves over time |
| Fake, off | Sound, look and motion disagree | Bring all cues to the same level of abstraction |

## Principles to check against

Predictable results, instantaneous response, easy but deep, novelty, appealing response, organic motion, harmony. Each is explained in `references/feel-principles.md`.

## Working with code

When the user shares a controller, read it for these before suggesting effects:

- Is position set directly, or is there a velocity with acceleration and drag? Which suits the target feel?
- Are acceleration, deceleration, turn-around and air control separate values?
- Is gravity the same rising and falling? Is fall speed capped?
- Does jump height depend on hold time, and does an early release cut the rise cleanly?
- Can the player jump just after leaving a ledge, and is a jump pressed just before landing remembered?
- Is vertical speed zeroed on landing and on hitting a ceiling?
- Is any input ignored during an animation, and for how long?
- Is input read and applied in the same frame it arrives?
- Does any required action need two buttons at once, a long hold, rapid repeated presses or a tight sequence? If so, is there a remap, toggle or single-press alternative?
- Are the tuning values exposed for live editing?

Propose changes as named parameters with starting values, and say which way to move each. Feel is found by iteration, so give dials and a hypothesis.

## Output format

- Diagnosis: restate the target feel, describe what the code currently does in envelope terms, name the two or three changes most likely to help in priority order with concrete values, then list polish to add once the motion is right.
- New mechanic: the mapping, parameters with starting values, the states and what each input means in each, the alternative for any input that needs a chord, hold or rapid presses, spacing guidance for levels, and a polish audit table.

## References

- `references/response-tuning.md`: envelopes in depth, mapping types, simulation structures, states, input filtering, input alternatives, and a platformer run and jump recipe with forgiveness techniques.
- `references/polish-audit.md`: the kinds of polish, what each communicates, an audit table per action, when to stop.
- `references/feel-principles.md`: the principles in depth, why controls feel random, input and response sensitivity, context, metaphor, measuring.

## Related skills

`game-systems-design` for what the player decides, `game-balance` for difficulty numbers, `game-programming-patterns` for state machines, game loops and update order.
