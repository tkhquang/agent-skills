# Decoupling patterns

Contents: Component, Event Queue, Service Locator.

## Component

Intent: let one entity span several domains without coupling those domains to each other.

Use when: a class handles input, physics, rendering and audio and keeps growing, or objects need to mix capabilities in ways inheritance cannot express without a diamond.

Watch for:
- More classes to create and wire together.
- Communication between components is the hard part.
- Extra indirection in inner loops. Laying components out in arrays can win that back.
- Do not split a class that is not causing a problem.

Decisions:
- How fine to slice. It depends on the genre and the size of the engine.
- Who builds the entity: the entity creates its own components (never incomplete, less flexible) or outside code supplies them (flexible, mix and match).
- How components talk. Use each where it fits:

| Method | Good for | Cost |
|---|---|---|
| Shared state on the entity | Basics such as position and velocity | Order of update matters |
| Direct references | Tightly related pairs such as animation and rendering | Couples the pair |
| Messages through the entity | Everything loosely related | Harder to trace, risk of loops |

How: swap the player's input component for a recorded or AI one to get demo mode or bots with no other change.

Entity component system: when entities become plain IDs, components become plain data in contiguous arrays, and behavior lives in systems that iterate those arrays, you have an ECS. It is Component plus Data Locality. If the engine provides one (examples: Unity Entities, Unreal Mass, Bevy, Flecs), use it instead of building these patterns by hand.

## Event Queue

Intent: decouple when a message is sent from when it is handled.

Use when: the sender must not wait for the receiver, requests should be merged or dropped, or work must cross a thread. Audio is the standard case: two identical sounds requested in one frame should play once, and loading must not block the caller. If you only need to decouple who from whom, Observer is simpler.

Watch for:
- A central queue is a global and shapes the whole architecture.
- The world has moved on by the time a message is handled. Put what the handler needs inside the message.
- Handlers that send messages can form loops that are hard to see. Log the traffic in debug builds.
- A poor fit when the sender needs an answer.

Decisions:
- Events (something happened, many listeners) or requests (do this, usually one handler).
- Readers: one, broadcast to all, or a work queue where each item goes to one worker.
- Writers: one or many. With many, include the sender.
- Who owns queued objects.

How: a fixed-size ring buffer with head and tail indices needs no allocation. Merge duplicates when enqueueing. With threads, make both enqueue and dequeue thread-safe, and keep the locked work small.

## Service Locator

Intent: global access to a service without coupling callers to its concrete class.

Use when: sparingly, after passing the object in has been ruled out. It fits services used almost everywhere, such as logging or audio.

Watch for:
- Dependencies become invisible to anyone reading the code.
- The service may not be registered yet, and registration must happen before first use.
- Any code can reach it, so it must work in any context.

Decisions:
- When the service is missing: return null (every caller checks), assert, or return a null service that does nothing. The null service is the usual choice.
- Who registers it: outside code at startup (swappable at runtime), compile-time selection (fastest), or configuration.
- Scope: global, or limited to one base class and its descendants.

How: wrap the registered service in a logging decorator to trace calls during development. Registering the null service is an easy way to turn audio off.
