# Optimization patterns

Contents: Data Locality, Dirty Flag, Object Pool, Spatial Partition.

Each of these trades flexibility for speed. Apply one only to a measured problem.

## Data Locality

Intent: arrange data so the processor's cache already holds what the code touches next.

Use when: a profiler shows cache misses in code that runs every frame. Memory access is far slower than computation, and following a pointer per object misses the cache every time. Layout alone can change loop speed many times over.

Watch for:
- Interfaces, virtual calls and pointers to separately allocated objects all work against it. Hot code gets less abstract.
- Across threads, keep each thread's writes on separate cache lines.

Techniques:
- Contiguous arrays. Keep each component type in its own flat array and process the array, instead of visiting entities and following their pointers.
- Packed data. Keep active items at the front of the array and swap on activate and deactivate, so the loop touches only live items with no per-item flag check.
- Hot and cold splitting. Keep fields used every frame inline and move rarely used fields behind a pointer.

Decisions:
- Polymorphism in hot code: avoid it, use a type object, or keep a separate array per concrete type.
- How entities refer to components: pointers (components cannot move), indices or IDs (components can move, lookup costs a little), or the entity is only an ID.

See also: the entity component system note under Component in `decoupling-patterns.md`.

## Dirty Flag

Intent: defer expensive derived work until the result is needed, and skip it when nothing changed.

Use when: source data changes more often than the derived data is read, deriving is expensive, and updating incrementally is hard. World transforms in a scene graph, cached pathfinding, unsaved documents. If a running total is easy to maintain, do that instead.

Watch for:
- The deferred work can land as a visible pause when it finally runs.
- Every path that changes the source must set the flag. Route changes through one function.
- If the deferred work is saving, a crash loses it.

Decisions:
- When to clean: on demand, at a quiet checkpoint such as a loading screen, or on a timer in the background.
- Granularity: fine flags do only the needed work and cost more bookkeeping. Coarse flags redo some work and cost less.

How: in a scene graph, setting a transform marks only that node. During traversal, pass a "parent was dirty" bit down so descendants recompute without being marked individually.

## Object Pool

Intent: reuse objects from a fixed set instead of allocating and freeing them.

Use when: objects are created and destroyed often, are similar in size, and allocation is slow or fragments memory. Particles, projectiles, sounds.

Watch for:
- Size needs tuning. Too small and requests fail. Too large and memory is wasted.
- Decide what happens when the pool is full: skip the request (fine for particles), replace the least important live object (the quietest sound), or grow.
- Reused objects keep their old contents. Initialize every field on reuse.
- With garbage collection, clear references held by dead pooled objects or they keep other objects alive.

Decisions:
- The object tracks its own in-use state, or a generic pool tracks it separately.
- The pool initializes the object, or hands it back for the caller to initialize.

How: a free list threaded through the unused objects themselves gives constant-time acquire and release with no extra memory.

## Spatial Partition

Intent: find objects by location quickly by storing them in a structure organized by position.

Use when: there are many objects with positions and frequent "what is near here" queries. Testing every pair grows with the square of the count.

Watch for:
- Only worth it for large counts.
- Moving objects must be re-filed, which costs time and is easy to get wrong.

Decisions:

| Choice | Options |
|---|---|
| Shape | Flat grid: simple, fixed memory, cheap updates. Hierarchy (quadtree, octree, BVH, k-d tree): handles uneven density, costs more to update |
| Boundaries | Fixed regardless of objects: easy to add and move. Adapted to objects: balanced, costly to rebuild |
| Storage | The partition is the only collection, or a second flat list exists for visiting everything |

How:
- Grid: each cell holds a list of its objects. Moving relinks only when the cell changes.
- To test each pair once, compare within a cell and against half of the neighboring cells.
- Cell size should be at least the largest query radius, so a query touches only adjacent cells.
