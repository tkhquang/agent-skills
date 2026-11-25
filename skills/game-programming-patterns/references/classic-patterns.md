# Classic patterns in games

Contents: Command, Flyweight, Observer, Prototype, Singleton, State.

## Command

Intent: a method call wrapped in an object, so it can be stored, passed around, queued and undone.

Use when: input must be rebindable, AI and players should drive actors the same way, or you need undo, redo, replay or networked play from a recorded stream.

Watch for:
- Undo needs the earlier state saved inside the command, and every change to the data must go through a command.
- Without garbage collection, something must free command objects.

Decisions: one reusable command per action, or a one-off command bound to a unit and a turn. Classes, or closures where the language has them. Undo by stored old values, by snapshot, or by replaying the command list.

How:
- The input handler returns a command and the caller runs `execute(actor)` later. Choosing and doing are now separate.
- A do-nothing command for unbound buttons removes null checks.
- Undo: `execute` records the old value, `undo` restores it. Multi-level undo is a list plus a current index. A new command discards the redo tail.
- Replay: record each entity's commands per frame and rerun the normal simulation.

## Flyweight

Intent: share the data that is the same for every instance and keep only the per-instance data separate. Purely an efficiency pattern.

Use when: there are too many similar objects. Thousands of trees share one mesh and texture set and store only position, height and tint. Map tiles point at a few shared terrain objects that hold movement cost and texture.

Watch for:
- Shared objects must be immutable, since a change shows up everywhere.
- Each use adds a pointer hop. Measure before assuming it is free.

Decisions: create every shared object up front, or on demand through a factory that returns an existing match.

How: instanced rendering is this pattern on the GPU, with one model drawn many times from a per-instance data stream. An enum with many switches over it is a hint that shared type objects would be cleaner.

## Observer

Intent: an object announces that something happened without knowing who listens.

Use when: linking mostly unrelated parts, such as physics reporting a fall that achievements and audio both react to. Inside one cohesive feature, explicit calls are easier to follow.

Watch for:
- A destroyed listener that stays registered keeps receiving events. Garbage collection does not prevent this, because the subject still references it. Unregister on destruction.
- A destroyed subject leaves listeners pointing at nothing. Send a final notification.
- Notification is synchronous: a slow observer blocks the subject. Push slow work to a queue or thread.
- The coupling exists only at runtime, so it is hard to trace by reading code.

Decisions: an observer interface, or registered functions (simpler in most modern languages). Whether the subject passes itself. Observing a subject, or observing a named event.

How: an intrusive linked list of observers avoids allocation on add and remove. A pool of list nodes lets one observer join several subjects.

## Prototype

Intent: an object creates new objects by cloning itself.

Use when: rarely as a class design. Its useful form in games is data: a content entry names another entry as its prototype and overrides a few fields.

Watch for: deep versus shallow copy (does a cloned demon share its weapon?), and every subclass needing its own `clone`.

How: in JSON content, `"prototype": "goblin grunt"` on a goblin wizard means "inherit every field I do not set". This removes most duplication in content files. For spawners, a function or generic type parameter is usually simpler than cloning.

## Singleton

Intent: one instance with global access. In practice the question is how to avoid it.

Problems: it is global state with hidden dependencies and coupling to everything that includes it. It is hostile to threads. Lazy creation takes initialization timing out of your hands, which can cause a hitch mid-game. It bundles two separate wishes, a single instance and global access.

Alternatives, in order:
1. Remove the class. Many "managers" only babysit another class that could look after itself.
2. Pass the object in as a parameter.
3. Expose it from a base class that the users already share.
4. Hang it off one existing global object, such as the game or world.
5. Service Locator.

If only one instance may exist and global access is not wanted, assert on a static flag in the constructor.

## State

Intent: an object changes behavior when its internal state changes.

Use when: behavior depends on a small set of distinct modes and responds to a sequence of inputs over time. Characters, menus, AI, parsers, network protocols. Boolean flags are the usual symptom: `isJumping` and `isDucking` allow combinations that should not exist.

Watch for:
- State machines are too limited for complex AI. Move to behavior trees or planning.
- One machine for two independent concerns multiplies states (n times m).

Decisions, in order of escalation:
1. An enum and a switch.
2. State objects, when states carry their own data or enter and exit actions.
3. Two machines side by side for independent concerns (n plus m states).
4. A hierarchy of states for shared behavior.
5. A stack of states to return to whatever came before, such as resuming after firing.

How: the input handler returns the next state or nothing. Run the old state's exit action and the new state's enter action at the switch. Stateless states can be single shared instances.
