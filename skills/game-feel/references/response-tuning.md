# Response tuning

Contents: what an input can modulate, describing motion, the envelope and what each phase feels like, where envelopes come from, states, filtering, input alternatives, platformer recipe, steering notes.

## What an input can modulate

- Position, set each frame.
- Orientation, set each frame.
- A force or torque applied to a simulated body.
- A simulation variable: gravity, friction, drag. A drift button that lowers tire grip is this kind.
- A one-shot animation played from start to finish, as with a fighting-game move.
- The playback speed of a looping animation.
- Creation of a new object such as a projectile.

The same button can therefore move something a fixed distance, move it while held, push it with a force, or change the world it moves in. Each feels different.

Building all control out of fixed animations gives a stiff, puppet-like result, because the player only chooses which clip plays.

## Describing motion

For each thing the player controls, note:

- Linear or rotational.
- Which dimensions.
- Frame of reference: relative to the avatar (rotate and thrust), to the camera (push the stick up to go away from the camera), or to the world.
- Position or rate: a mouse usually sets a position, a stick usually sets a rate.
- Direct or indirect: does the input move the avatar, or move something the avatar then follows?
- Integrated or separate: one stick doing both turn and thrust, or separate inputs for each.

Indirect control can be a pleasure in itself. A vehicle that swings toward an aim point with some overshoot is harder to master and more satisfying than one that snaps to the heading.

## The envelope

Borrowed from sound synthesis. For any input, graph the controlled parameter (usually speed) over time.

| Phase | Meaning | Long | Short |
|---|---|---|---|
| Attack | Time from input to full effect | Loose, floaty | Tight, responsive |
| Decay | Drop from an initial peak to the held level | Usually accidental | None is normal |
| Sustain | Level held while input is held | The cap, such as top speed | |
| Release | Time back to rest after input ends | Soft, sliding | Abrupt stop |

Reading envelopes:

- A long attack is not a problem by itself. A thruster that builds speed over more than a second can feel great. The problem is when nothing perceptible happens in the first 100 ms. Best of both: a steep start, then a long curved ramp. Responsive and loose at once.
- A short attack that is also perfectly linear feels twitchy. Very short and linear feels stiff. Keep a slight curve even in tight controls.
- Attack and release are often mirrored. A soft release preserves a loose feel. Zero release feels abrupt.
- Decay means the avatar is briefly faster just after an input change than at steady state. That rewards rapid tapping, tires hands, and creates exploits (alternating two movement keys to travel faster than intended).
- Floaty, loose, tight, twitchy, stiff and unresponsive are all points on one continuum of envelope shapes.

## Where envelopes come from

The structure decides which tunings are possible at all. Common ones:

1. Direct position. Each frame the input is held, add a fixed amount to position. No attack, no release. Stiff and crisp. Good for precise positioning challenges and grid-like games.
2. Velocity with forces. Keep a velocity. Input adds acceleration, drag removes it, a maximum clamps it. Smooth curved motion. Tune acceleration for attack, drag for release, the clamp for sustain. With zero drag the object slides forever.

```text
velocity += input_direction * acceleration * dt
velocity -= velocity * drag * dt
velocity  = clamp(velocity, -max_speed, max_speed)
position += velocity * dt
```

3. Filtered input. Ramp the input itself over a short time before applying it. A turn rate that grows over the first fraction of a second lets taps make fine adjustments and holds give full rate.

A jump driven by a small simulation feels fluid. A jump read from a fixed table of positions feels crisper and more exact. Choose on purpose.

## States

A state changes what an input means. On the ground, left and right apply full acceleration. In the air, the same inputs apply much less. That is two responses from one input and it adds expressive range at no cost in buttons.

- More states mean more expressivity: a skating game can have six states in which every button does something different.
- States must be obvious to the player. If they cannot tell which state they are in, inputs feel random.
- List states explicitly with what each input does in each, and what triggers each transition.

## Filtering and interpretation

- Scaling: the ratio between physical movement and on-screen movement. Even "raw" pointer control has one.
- Non-linear response: make the effect grow faster toward the edge of a stick's range. Half tilt gives a gentle turn, full tilt a sharp one. This prevents oversteer while keeping hard turns available.
- Gestures: sequences of inputs within a short time window, recognized as a new signal. Quarter-circle motions, double taps.
- Chords: simultaneous inputs with a meaning of their own. A run button that changes what left and right do is a chord.
- Context sensitivity: the same button does different things depending on where the avatar is. This can be discrete (near a ladder) or continuous (strength varies with distance to something).

## Input alternatives

Chords, holds, rapid presses and timed sequences add expressive range, and each shuts out players who cannot perform it: one-handed play, limited grip or reach, tremor, an adaptive controller with few buttons. Platform accessibility guidelines ask for the alternatives below.

| The mapping requires | Offer |
|---|---|
| Two inputs at once (a chord) | A single-input route to the same action: a toggle for the modifier, or a separate binding. Menus must be fully usable with single, non-simultaneous presses |
| Holding a button, especially for two seconds or more | Press to toggle. Converting every hold into a press is a common single option |
| Rapid repeated presses or a quick-time sequence | Hold instead of mash, a single press, or a slower timing window |
| A tight gesture window (double tap, quarter circle) | An adjustable window, or a one-button shortcut |
| Fixed bindings | Remapping in the game itself, by action and not by button, even when the platform also remaps |
| One analog sensitivity | Sensitivity adjustable for each analog control separately, by at least half of the default in each direction |

Design the alternative with the mechanic.

- A toggle must show its state. A held button tells the player which mode they are in and a toggle does not.
- Check whether the alternative changes the challenge. Hold to charge and press to charge test the same timing. Replacing a mash with one press removes an endurance test that was rarely the point.

## Platformer recipe

This is the classic side-scrolling run and jump, described as parameters and the tricks that matter.

### Horizontal

Parameters: acceleration, deceleration, maximum speed, run acceleration, run maximum speed, air acceleration.

- Holding a direction accelerates toward the maximum. Releasing decelerates to rest. Deceleration is its own value, independent of how fast the character sped up.
- Reversing direction uses its own handling so a skid can feel distinct.
- A run button swaps in a higher acceleration and a higher maximum.
- In the air, acceleration is a different, lower number. It limits acceleration, not speed, so running momentum carries into a jump. The run button has no effect in the air.

### Vertical

Values: gravity, initial jump velocity, minimum hold time, maximum hold time, reduced jump velocity, falling gravity, terminal velocity.

Derive the first values from the design: `gravity = 2 * height / time_to_apex^2` and `jump_velocity = 2 * height / time_to_apex`.

1. On press, set vertical velocity instantly to a high value. The big response on the first frame is what makes the jump feel immediate.
2. While the button is held, let the jump continue up to a maximum hold time. A full hold of about half a second reaches roughly five tiles. A one-frame tap reaches about one and a half.
3. Cut the jump on early release. If the button is released while upward velocity is above the reduced value, set it to that value instead of letting it decay: 100, 90, 80, then straight to 20. Every jump then ends with the same arc and only the height differs.
4. During any fall, including walking off a ledge or bumping a ceiling, multiply gravity by about three. Equal gravity up and down feels floaty, keeps the player out of control too long, and makes the character seem too light.
5. Clamp fall speed. Without a cap long falls feel wrong. With a cap that is too low the clamp is visible, like a cartoon umbrella opening.
6. Optional coupling: jumping while above walking speed adds a small fixed boost to jump velocity, enough to clear one extra tile.

```text
# Timers count down: coyote_timer from leaving the ground, buffer_timer from the jump press
when buffer_timer > 0 and (grounded or coyote_timer > 0):
    vy = jump_velocity
    hold_timer = 0
    buffer_timer = coyote_timer = 0

each frame while airborne:
    released_early = not jump_held and min_hold <= hold_timer < max_hold
    if released_early and vy > reduced_jump_velocity:
        vy = reduced_jump_velocity          # Early out: same arc at the end
    g = gravity * (fall_multiplier if vy <= 0 else 1)
    vy -= g * dt
    vy = max(vy, -terminal_velocity)
    hold_timer += dt
```

### Collision

- Predict the next position, and if it is inside something solid, snap flush against it.
- No friction against walls, so the character never snags. That slipperiness is part of the loose feel.
- Zero vertical velocity every frame while standing on ground. Otherwise gravity accumulates and the character plummets when stepping off an edge.
- Zero vertical velocity on hitting a ceiling. Otherwise the character sticks to it for a moment.

### Forgiveness

The computer knows the player pressed jump nine milliseconds after leaving the ledge. The player believes they pressed in time. Resolve such cases the way the player meant. Precise platformers rely on these techniques, and players do not notice them when they work.

| Technique | What it does | Starting value |
|---|---|---|
| Coyote time | A jump still works shortly after walking off a ledge | About 0.1 s |
| Jump buffering | A jump pressed shortly before landing fires on the landing frame | About 0.1 s |
| Lighter apex | While the button is held and vertical speed is near zero, gravity is halved. Falling gravity applies once the character is clearly descending | Half gravity |
| Corner correction | Clipping a ceiling corner nudges the character around it. Clipping a ledge sideways pops them on top | A few pixels |
| Generous wall range | A wall jump works from slightly away from the wall | A quarter of a tile |

Tune the windows by feel. Too long and jumps appear to come from thin air.

## Steering notes

- A fixed steering ratio is twitchy at speed. Let the ratio vary with stick deflection.
- Sideways friction is what makes a vehicle feel planted. A drift state is a temporary reduction of it.
- An aim point that the vehicle chases gives an immediate visible response (the aim point moves at once) with a looser follow-through.
- A widening field of view, motion blur and nearby passing objects raise the impression of speed without changing speed.
