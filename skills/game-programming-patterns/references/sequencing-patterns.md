# Sequencing patterns

Contents: Double Buffer, Game Loop, Update Method.

## Double Buffer

Intent: make a series of changes appear to happen all at once.

Use when all of these hold: state is changed step by step, it can be read in the middle of those changes, readers must not see half-finished work, and readers must not wait for the writer. Cases: a renderer writing a frame while the display reads it, and actors whose results depend on the order they update in.

Watch for:
- The swap must be atomic and cheap. If swapping costs more than the work, there is no gain.
- Memory doubles.

Decisions:
- Swap pointers (fast, but outside code cannot hold a pointer across swaps) or copy next into current (simpler, slow for large data).
- One buffer for everything, or a current and next value on each object.

How: for update order, every actor reads `current` and writes `next`, then all swap after the pass. A single shared index that flips between 0 and 1 swaps every object in one step.

## Game Loop

Intent: decouple game time from processor speed and from user input.

Use when: nearly always. An engine usually owns the loop and calls your code. Turn-based games still need one for animation and audio.

Decisions:

| Option | Trade-off |
|---|---|
| Fixed step, no sync | Simplest. Game speed follows machine speed |
| Fixed step, sleep to a target rate | Saves power. Slows down if a frame runs long |
| Variable step | Adapts to any machine. Breaks determinism and physics stability. Avoid |
| Fixed update, variable render | Most adaptable. More complex. The usual choice |

Watch for:
- Running flat out drains batteries. Cap the frame rate or sleep.
- Work with the platform's own loop where there is one, such as `requestAnimationFrame` in a browser.
- If `update` takes longer than one step, the loop never catches up. Cap updates per frame and discard the leftover lag. The same cap absorbs a long pause such as a breakpoint.

How:

```text
previous = now()
lag = 0
loop:
    current = now()
    lag += current - previous
    previous = current
    process_input()
    steps = 0
    while lag >= STEP and steps < MAX_STEPS:   # Cap, for example 5 updates per frame
        update()
        lag -= STEP
        steps += 1
    if lag >= STEP:             # Still behind after the cap
        lag = lag mod STEP      # Drop the backlog: the game slows, it does not lock up
    render(lag / STEP)          # From 0 up to just under 1
```

The renderer receives how far the frame sits between two updates. Blend the last two states (always correct, one step late) or project forward from velocity (no delay, occasionally wrong).

See also: Glenn Fiedler, "Fix Your Timestep".

## Update Method

Intent: simulate many independent objects by giving each one frame of behavior at a time.

Use when: many objects act at once, mostly independently, and change over time. A poor fit for abstract turn-based games such as chess.

Watch for:
- Behavior that was a straight loop must be cut into frame-sized steps with explicit state. Coroutines or generators can hide this.
- Order matters: later objects see what earlier ones just did. Double Buffer removes that.
- Objects added during the pass: record the count first so new ones wait a frame.
- Objects removed during the pass: iterate backward, or mark dead and sweep afterward.

Decisions:
- Where `update` lives: on the entity (simple, brittle), on components (decoupled), or on a delegate such as a state or type object.
- Dormant objects: one collection with an active flag (wasted iteration) or a separate active list (must be kept in sync).
