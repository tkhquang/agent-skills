# Testable core

Contents: levels of separation, what the core may touch, randomness and numbers, the boundary with the view, keeping it enforced, tests worth writing, traps.

The rules of the game run without rendering, input or real time. That makes tests fast, bugs repeatable, and simulation, undo, replay, saves and bots cheap.

## Levels of separation

Choose the strictest level the engine allows and the team can enforce.

| Level | The core may use | Fits |
|---|---|---|
| Engine-free | The language only | Discrete games in a general language |
| Scene-free | Engine math, file and random classes. No nodes, scenes, rendering, input or frame time | Engines whose scripts run headless. Example: a Godot class that extends RefCounted |
| State module | One module declares all story state and holds the only functions that change it | Engines where the script is the program. Example: Ren'Py |

In a physics-driven game, start with the discrete parts: damage, inventory, quests, economy, win conditions.

## What the core may touch

| Allowed | Not allowed |
|---|---|
| Its own state and data files | Scenes, rendering, audio, input |
| One seeded generator | Global random functions |
| Turn or step counters | Wall clock, frame time, timers |
| Commands passed in | Storage, network, platform services |
| Returned results and event lists | Text the player reads |

- A command resolves until the state is stable before the next command is accepted.
- Keep tuning values in one table that a test or a simulation can override for one run.
- The opponent, tools and tutorials use the same commands as the player.
- A command reports whether it was illegal, legal at no cost, or a counted move, when the design treats those differently.

## Randomness and numbers

- Give each purpose its own generator: rules, opponent choices, map generation, cosmetic effects. A choice by the opponent must not shift a later roll.
- Store the generator state in saves and undo steps.
- Prefer integers in rules. Floating point results can differ across compilers, instruction sets and build types, which breaks replays and lockstep between machines.
- Some text formats and engines read every number back as floating point. Restore whole numbers on load.
- Break ties and iterate in a defined order.

## The boundary with the view

- The view sends commands and draws state. It decides no rule.
- A command returns a result: what happened, in order. The view animates that list. Skipping or interrupting an animation changes nothing.
- A preview ("what will this do?") calls the same function as the command, on a copy.
- Values the player reads come from core state. Derived values, such as a percentage, are computed and not stored.
- The view finds out which moves are legal by asking the core.

Record commands and replay them through the core to get undo, demos, bug reports and saves. See Command in `classic-patterns.md`.

## Keeping it enforced

Use the first of these that the project can run, then add the rest:

1. A linter ban on the core folder: engine imports, platform modules, dynamic imports, clocks, timers, global random, global objects.
2. A test that feeds each banned form to the linter. It must fail inside the folder and pass outside it.
3. With no linter, a text scan in the test suite, with known bad and known good samples for its patterns.
4. A build check that tooling-only modules, such as a level generator, are not in the shipped build.
5. Running the core tests in a process that cannot load the engine.

## Tests worth writing

| Test | Proves |
|---|---|
| Same seed and commands, run twice, give equal serialized state | Determinism |
| Save, load, play on. Compare with a game that was never saved, after the same number of turns | Complete saves |
| Undo restores board, score, counters and generator state | Exact undo |
| A mirrored setup gives a mirrored game | No side advantage in rules or opponent |
| Both sides of a symmetric map have the same terrain, sites and travel costs | Fair maps |
| Every content row obeys its rule, such as an option's effect matching its declared kind | Data errors |
| Bots play many seeds to the end with a turn limit | Stalls and crashes |
| Replaying illegal or outdated commands is rejected | Safe loading |
| Random rolls stay in range, and many seeds give many values | Broken dice |

Test a rule on the smallest board that shows it. A test that needs the full game to set up belongs in an end-to-end gate.

## Traps

| Trap | Sign | Fix |
|---|---|---|
| State changed in an animation callback | Results differ when animations are skipped | Change state first, then animate |
| Second copy of a rule | Preview or tutorial disagrees with play | Call the core |
| Hidden clock | A test passes alone and fails in a slow run | Pass time in as data, or count steps |
| Opponent rolls the rules' dice | Changing the opponent changes unrelated hits | Separate generators |
| Cosmetic choice from the core generator | Turning effects off changes results | A generator for the view |
| Test edits fields directly | Passes on states the game can never reach | Reach states through commands |
