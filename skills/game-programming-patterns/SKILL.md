---
name: game-programming-patterns
description: Chooses and applies code architecture patterns for games. Covers the game loop and fixed timestep, components and entity component systems, state machines, commands with undo and replay, observers and event queues, object pools, spatial partitions, cache-friendly data layout, dirty flags, type objects, bytecode, alternatives to singletons, a rules core that runs without the engine, determinism, and saves that survive updates. Use when the user is structuring or refactoring game code, fighting a god class, global managers, tangled update order, frame hitches, allocation spikes or slow collision checks, wants rules that can be unit tested or replayed, designs a save format, breaks old saves, or asks which pattern fits a gameplay feature.
license: MIT
---

# Game programming patterns

Good structure is measured by how little you must understand before making a change. Game code is pulled between being easy to change, fast at runtime, and quick to write today. Every pattern here trades among those.

- Keep code flexible while the design is still moving. Harden the hot paths once it settles.
- Apply a pattern when you have the problem it solves. Unused flexibility is extra code to read.
- Prototype code may be rough only if it is thrown away.

## Start from the problem

| Problem | Pattern | Reference |
|---|---|---|
| Game speed varies by machine, or physics is unstable | Game Loop with a fixed update step | `sequencing-patterns.md` |
| Many independent things act each frame | Update Method | `sequencing-patterns.md` |
| Results depend on update order, or readers see half-finished state | Double Buffer | `sequencing-patterns.md` |
| One class handles input, physics, rendering and audio | Component | `decoupling-patterns.md` |
| Deep inheritance, or objects must mix capabilities | Component, or a shallow hierarchy with Subclass Sandbox | `decoupling-patterns.md`, `behavior-patterns.md` |
| Hundreds of subclasses that differ mostly in data | Type Object | `behavior-patterns.md` |
| Designers change behavior without recompiling, or mods need a sandbox | Bytecode, or an existing scripting language | `behavior-patterns.md` |
| Booleans and nested ifs decide what a character can do | State | `classic-patterns.md` |
| Rebinding, undo, replay, or AI and player sharing controls | Command | `classic-patterns.md` |
| A system reacts to events without the source knowing | Observer | `classic-patterns.md` |
| Sender must not wait, or requests should be merged or deferred | Event Queue | `decoupling-patterns.md` |
| Everything reaches for a global manager | Pass it in first, then Service Locator | `classic-patterns.md`, `decoupling-patterns.md` |
| Spawning and destroying causes hitches or fragmentation | Object Pool | `optimization-patterns.md` |
| Too many identical heavy objects | Flyweight | `classic-patterns.md` |
| Checking every pair of objects is too slow | Spatial Partition | `optimization-patterns.md` |
| Profiler shows cache misses in a hot loop | Data Locality | `optimization-patterns.md` |
| Expensive derived data recomputed when nothing changed | Dirty Flag | `optimization-patterns.md` |
| Variants of objects spawned from templates | Type Object, or prototypes in data | `behavior-patterns.md`, `classic-patterns.md` |
| Rules cannot be tested, simulated or replayed without running the game | Testable core | `testable-core.md` |
| The same seed gives different results | Testable core: randomness and numbers | `testable-core.md` |
| Updates break saves, or content is renamed, reordered or removed | Stable identifiers and versioned saves | `saves.md` |

The files are in `references/`. Each pattern entry gives intent, when to use, pitfalls, design decisions and implementation notes. Read the entry before recommending a pattern. The files `testable-core.md` and `saves.md` are practices that cut across patterns.

## The game loop

Most engines own the loop. Work with the engine's update model and do not rebuild it. A fixed-step loop with its required catch-up cap is under Game Loop in `sequencing-patterns.md`.

## Choosing between neighbors

- Observer or Event Queue: Observer decouples who from whom and runs immediately. A queue also decouples when, at the cost of stale data and harder debugging. Use a queue only for the delay, the merging or a thread hop.
- Singleton or anything else: pass the object in first. The full order is under Singleton in `classic-patterns.md`.
- Inheritance or Component: inheritance is fine in moderation. Split by component when a class spans domains or variants need a diamond.
- Component or ECS: an entity component system is Component plus Data Locality. If the engine ships one, use it.
- Subclass or Type Object: when kinds differ in data, make the kind a data object loaded from a file. Shared behavior is harder: pick from fixed functions or step up to scripting.
- State enum or state objects: start with an enum and a switch. The escalation path is under State in `classic-patterns.md`.
- Flyweight, Object Pool, Type Object: sharing at one moment to save memory, reuse over time to avoid allocation, and organizing kinds.
- Dirty Flag or running total: update incrementally when that is cheap. Use a flag when it is not.

## Performance patterns need evidence

Data Locality, Object Pool, Spatial Partition, Dirty Flag and Flyweight each make code less flexible.

- Profile before and after. Cache behavior cannot be guessed.
- They rely on assumptions such as "never more than this many". Add those late, when the design has settled.
- Several trade memory for speed. Check which one the target platform lacks.

## Workflow

1. Restate the problem as a symptom: what change is hard, what is slow, what breaks.
2. Pick one or two candidates from the table and read their entries.
3. Check "use when" and "watch for" against the user's situation. Say so if no pattern is needed.
4. Show the smallest version in the user's language and engine. Many patterns shrink to a few lines with closures, generics or engine features.
5. Name the design decisions and recommend a default for each.
6. State the cost: what gets harder to read, debug or change.

## Review prompts

When reviewing game code, look for:

- One class that knows about rendering, physics, input and audio.
- Managers and globals reached from everywhere.
- Flags that encode states which cannot combine.
- Allocation every frame in hot paths.
- Collections modified while the update pass iterates them.
- Logic that assumes a frame rate.
- Rules decided in rendering, animation or interface code.
- Clocks or global random functions inside rules.
- Saves that store list positions instead of identifiers.
- Listeners that are never unregistered.
- Every-pair loops over large sets.
- Derived values recomputed every frame from unchanged inputs.
- Indirection that no current feature needs.

## Related skills

`game-feel` for what a character controller should do, `game-systems-design` for the rules being implemented, `game-balance` for the data that type objects carry and for simulation, `game-quality-gates` for enforcing the boundaries.
