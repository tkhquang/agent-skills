# Test bridge and automated playtests

Contents: what a bridge is, its interface, driving the game, what each run checks, mock services, captures, performance runs, soak runs, keeping it out of releases.

## What a bridge is

A small interface, present only in development and test builds, that reads the state of the game and applies moves the way a player does. Tests decide by state. They never read pixels to decide whether something happened.

Use the engine's own facility when it has one. Examples: a global object in a web build, a test framework that clicks and advances dialogue, a scripted main loop that opens scenes and sends key events.

## Interface

| Part | Holds |
|---|---|
| Version | Goes up when the shape changes, so old tests fail clearly |
| Ready | True when a screen, or the load error screen, is showing |
| Active screen | Name, and the open panel |
| State for each screen | Plain data: counters, board, selected item, buttons with their on-screen rectangles, what is enabled |
| Busy | True while a move resolves or animates |
| Feedback log | The sounds and effects that played for each event |
| Load progress and error | Values shown to the player |
| Move | Applies a player action through the same path as input |
| Start | Opens a given level, or a test setup that the game does not ship |
| Service log | Events that reached the platform service |

Return plain data, not live objects.

## Driving the game

- Use real input for pointer mapping, drag, keyboard and focus. Take positions from the rectangles the bridge reports.
- Use bridge moves for long sequences.
- Wait on state ("Ready", "Not busy"), never on a fixed delay.
- Complete levels with the solver's path or a recorded solution.
- For menus and panels: open, act, close, interrupt. Every disabled input needs a way back.
- Interrupt on purpose: hide and show the window, resize, rotate, reload, save and load, leave and return.
- Start each test from a fresh profile. Seed an old or broken save before the first load.

## What each run checks

Fail the test on any of these, in every run:

- A console or log error.
- An uncaught exception.
- A request to a host that is not allowed.
- A missing asset. Turn engine placeholders into errors.
- A state that should be unreachable, such as input accepted during a break.

List exceptions one by one, with the cause.

## Mock services

Replace the platform service in test builds with a mock that records events. Let a test choose:

| Part | Modes |
|---|---|
| Start | Works, fails, hangs |
| Ad or purchase | Fills and waits for the test, fails once, unavailable for the session |
| Reward | Granted, refused, granted after the time limit |
| Storage | Works, blocked, full |
| Device and mute | Each value that the platform can report |

Assert the order of events, no repeated event, no event during a break, and that play goes on after every failure.

## Captures

- Take the reference sizes from the platforms' requirement pages, plus the smallest supported size.
- Reach each screen through the bridge, then capture. Include the longest text, the largest board, every panel and error state.
- Check that each file exists once and has exact dimensions.
- Open every image. Look for clipping, overlap, unreadable text, small targets, wrong order.
- Pixel comparison against stored images works only when the same machine and browser or engine version produced both. Rendering varies with operating system, hardware and settings.
- An open panel can hide another one. Assert drawing order and non-overlap from rectangles where it matters.

## Performance runs

| Choice | Do |
|---|---|
| Scene | A worst-case sample: the largest, the busiest, one of each kind. Not every level |
| Load | A stated slowdown that stands for the weakest device |
| Renderer | Fail on a software renderer. It measures drawing and not the game |
| Measure | Frame intervals while something moves, over several runs |
| Pass rule | A high percentile, a higher one for rare frames, and a separate limit for a stall |
| Machine | Nothing else running. Stray frames come from other programs. Name each long frame with its scene and action |
| When | Before a release, and after a change to a hot path |

A single-frame maximum is not a usable pass rule on a shared machine. In one project it failed while other programs ran, and was replaced by a 99.9th percentile of 34 ms with a stall limit of 100 ms.

Record the numbers before and after. Make no claim about speed without both.

## Soak runs

Let a bot or attract mode play for hours. Watch memory, entity counts, frame time and log size. Leaks and fragmentation are the usual failures.

## Keeping it out of releases

- Compile the bridge out with a build flag. The release flag is false by default.
- Search every release package for a text that only bridge code contains.
- The same search must find it in the test build. Otherwise it proves nothing.
- Do the same for mocks, cheat commands, test scenes and generators.
