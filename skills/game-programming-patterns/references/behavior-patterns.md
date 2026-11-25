# Behavior patterns

Contents: Bytecode, Subclass Sandbox, Type Object.

## Bytecode

Intent: define behavior as data, as instructions for a small virtual machine.

Use when: there is a lot of behavior to define and the implementation language is too slow to iterate in, too low-level for the authors, or too trusted for mods and patches. Check first whether an existing scripting language such as Lua already solves it.

Watch for:
- Scripting systems grow into full languages unless scope is held deliberately.
- A debugger no longer shows what the author wrote. Budget for tools.
- Nobody should write raw bytecode. It needs a text language or a visual editor in front of it.
- It is slower than native code. Keep it out of hot paths.

Decisions:
- Stack-based machine (simpler, easier to generate code for, recommended) or register-based (fewer, larger instructions).
- Value types: one type, a tagged union (safe, larger) or an untagged union (compact, unsafe).
- Authoring: text (needs a parser and error messages, excludes non-programmers) or visual (more interface work, fewer ways to make errors).

How:
- One-byte opcodes. A literal instruction reads the next byte as a value. Operations pop arguments from the stack and push results.
- Sandbox with a bounded stack and an instruction limit per run, so content cannot hang or crash the game.

## Subclass Sandbox

Intent: define behavior in subclasses using only operations the base class provides.

Use when: one base class has many subclasses with overlapping behavior, and the subclasses should stay decoupled from the rest of the engine. Hundreds of abilities that each need to play sounds, spawn particles and move things.

Watch for: the base class collects every operation any subclass needs and becomes coupled to every system. When it grows too large, move groups of operations into helper objects.

Decisions:
- Which operations to provide. Provide what many subclasses use, and skip what one subclass uses once.
- Methods on the base, or a getter returning a helper such as a sound player.
- How the base gets its dependencies: constructor argument, a separate init step behind a factory function, shared static state, or a Service Locator.

How: one abstract method for the subclass to implement, plus protected helpers such as `move`, `playSound` and `spawnParticles`.

## Type Object

Intent: one class whose instances each represent a kind of thing, so new kinds are data instead of code.

Use when: there are many kinds that differ mostly in data, kinds are not known up front (downloadable content, mods), or designers must tune without recompiling. Monster breeds, items, units.

Watch for:
- Sharing data is easy and sharing behavior is hard. Options: choose from a fixed set of behavior functions, or define behavior in Bytecode.
- You manage types yourself: they must stay loaded, and every instance needs a valid one.

Decisions:
- Hide the type behind the instance (instance forwards calls and can override) or expose it.
- Construct an instance and hand it a type, or ask the type to create instances (the type then controls allocation, for example from a pool).
- Whether an instance can change type at runtime.
- Inheritance between types: none, or a single parent. Single is usually enough.

How:
- A `Breed` holds health and attack text. A `Monster` holds a reference to its breed and reads values through it.
- For inheritance, copy the parent's fields down at load time where the child leaves them unset. Lookups stay fast.
- In data, a zero or missing field means "inherit from the parent".
