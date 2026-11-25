# Saves and stable content

Contents: what to store, identifiers, versions, loading, storage failure, several stores, tests, checklist for a release.

Decide the save format before content ships. Released names and identifiers cannot change afterward.

## What to store

| Game | Store |
|---|---|
| Short attempts under deterministic rules | Best result for each level, settings, and the list of moves of the current attempt |
| Long games under deterministic rules | Full state, generator state, and the tuning values the game was started under |
| Branching story | Every story variable and the position. Derive percentages and unlocked lists on load. Do not store them |
| Any | A schema version |

- A list of moves is small and cannot hold an illegal board. Replay it through the rules.
- Storing the tuning values lets a balance change leave running games alone.
- Keep facts that cross playthroughs, such as a gallery, apart from the state of one playthrough.
- Write after every committed move, completed level and settings change.

## Identifiers

- An identifier is stable for the life of the game. Never reuse or renumber one.
- Order is a separate list. Moving a level changes no identifier.
- Removed content leaves the order list. Its data and its save entries stay.
- Keep unknown identifiers through a load and a write, and ignore them in play.
- The same holds for names that an engine stores in saves. Example: in Ren'Py, released label and variable names.
- The save folder or storage key never changes.

## Versions

- Every schema change ships a migration and a fixture of the old shape. Add fixtures. Never edit one.
- Give each field added later a default for older saves.
- If a save names content that no longer exists and cannot be mapped, refuse it whole. A half-loaded game is worse.
- Decide what a save from a newer version does, and test it.
- If saves depend on compiled artifacts of a release, keep those artifacts with each release.

## Loading

1. Parse and check every type and range. Treat the text as untrusted.
2. Migrate to the current version.
3. Replay or restore through the core.
4. If the attempt fails to replay, drop the attempt and keep the rest of the progress.
5. Check that the resume point exists and is open to the player. Otherwise take the first that is.

## Storage failure

| Failure | Behavior |
|---|---|
| Access to storage throws | Guard the access itself, not only the read. A browser can refuse it |
| Read fails | Play in memory and write nothing this session. Storage may hold a save the read did not see |
| Read works and the text is corrupt | Keep the corrupt text under a backup key, then start a clean save |
| Write is interrupted | Write to a temporary file or key, then swap it in |
| Write fails | Keep progress in memory, try again on the next write |
| Access, read or write fails | Show a short notice that progress is not saved. The game stays fully playable |

## Several stores

When a platform store and a local store both hold a save:

- Pick one owner for settings and the current attempt.
- Merge results by keeping the best for each identifier.
- Make the merge safe to repeat. It deletes nothing and writes only when it adds something.

When builds differ in content, such as editions or a demo:

- A save made inside content that the other build lacks must load at the last shared point.
- Clear flags that the other build cannot produce, and block a rollback past the load.
- Test with saves from the larger build, loaded in the packaged smaller build.

## Tests

| Case | Expect |
|---|---|
| A fixture of each released version | Loads exactly, and its attempt replays |
| Corrupt text, wrong types, empty, absent | Clean start, no crash |
| Newer version | The decided behavior |
| Illegal or unknown move in the attempt | Attempt dropped, progress kept |
| Unknown identifier | Survives a later write |
| Reordered or removed levels | Progress stays with its identifiers |
| Storage blocked, and writes failing | Game completes a level, notice shows |
| Save, load, continue for several turns | Equal to a game that was never saved |
| Save in the middle of a scene, menu or animation | Resumes at a valid point |
| Rollback across a state change | Every variable restored |

## Before a release

- Copy a save from the last public build into the fixtures.
- List renamed or removed identifiers since that build. The list should be empty.
- Play from an old save in the packaged build.
