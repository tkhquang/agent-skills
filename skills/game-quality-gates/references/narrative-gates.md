# Narrative gates

Contents: the script as contract, script sync, route coverage, state rules, saves and rollback, screens in story games, content review.

For visual novels, dialogue-heavy games, quests and any branching text.

## The script as contract

- One approved document holds every line, option, state change and scene order for a release.
- Use a format a parser can read: a heading for each scene, a speaker marker for each line, numbered options, a table for state.
- Game files implement it. An agent does not write new lines into game files. It proposes them in the document first.
- Everything the player reads is a dialogue line, a menu option or screen text. No such text sits in code, where exports and translators miss it.

## Script sync

1. Export dialogue and options from the engine or the data files. Keep speaker, text, file and line.
2. Parse the document into the same shape.
3. Normalize: whitespace, style tags, stage directions, variables shown as placeholders.
4. Compare in order, for each file against its scenes. Print a diff.
5. Fail on an unknown speaker, a file with dialogue that is in no scope, and a scene in scope that is empty.

A matching export proves agreement with the script. Only route coverage proves that the player sees the line.

Text that the export misses, such as in-game documents or a codex, needs its own comparison. Test the parser with a small document and export: match, paraphrase, missing line, unmapped file.

## Route coverage

- List paths as picks at each menu. Together they take every option.
- Play each path from the main menu back to the main menu, on a clean copy with an empty save folder.
- Turn missing images and sounds into errors. Engines often show a placeholder instead.
- After the paths, ask the engine which labels were not reached and which options were never picked. Both lists must be empty. Ignore test scripts and engine screens.
- Assert first that at least one menu was found.
- Repeat for each edition or target with different content.
- For conditional options, add paths that meet and paths that miss the condition.

As choices multiply, full path counts grow too fast. Cover options and labels in play, and enumerate state combinations in the rules without rendering.

## State rules

- Declare all story state in one module, with start values. Scenes change it only through named functions.
- Scan scripts for declarations and writes elsewhere. Cover every form the engine offers: assignment, set methods, interface actions, attribute setters. Test the scan with samples of each.
- Compare the declared variables with the design document's table.
- Check each option against the rule of its kind. Example: an option labelled "Defy" must raise the rebellion counter and may not lower affection.
- Derived values are computed, never stored.
- In play tests, assert the whole state tuple after each choice, not only the variable that should change. That catches unintended changes.

## Saves and rollback

| Test | Expect |
|---|---|
| Save in the middle of a scene, play on, load | The same line, state and screens |
| Roll back across a choice, choose again | State restored exactly, then applied once |
| Open every menu in the middle of a scene and return | The line and state are unchanged |

Save formats, released names and saves across editions: `saves.md` in `game-programming-patterns`.

## Screens in story games

- Assert which screen shows each kind of line.
- Assert drawing order when a panel and a line show together. In one project an end card hid the lines after it, and an open status window hid a notice. The play tests passed both.
- Assert that frames do not overlap, from drawn rectangles.
- A stop or exit control works on every line of a scene that offers one.

## Content review

A command cannot judge content. Use a review gate.

1. Write the content rules as a numbered list in the design document, for each edition and store.
2. Scope: every scene the change touched, plus scenes that show a changed image.
3. Make a table: line or image, rule checked, result. Keep it as evidence.
4. Check declines as well as accepts: refusing costs what the rules say, and play goes on.
5. A dispute goes to the owner.

Where an edition leaves content out, do not rely on a skip. Skipped content still ships. See `game-release-targets`.
