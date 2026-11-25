# Editions

Contents: when to split, structure, the guarded entry, build rules, leak checks, saves across editions, playing each edition, checklist.

For builds from one tree that hold different content, such as adult and all-ages. The same method fits any content that one build must not hold, such as a demo without later chapters.

## When to split

| Situation | Use |
|---|---|
| Content a store or rating forbids | Edition. The files must be absent |
| Players who prefer not to see something | An in-game setting. The files still ship |
| Optional content that both builds may hold | Data or a setting |

A skip option is not an edition. Skipped content still ships.

## Structure

- Put all restricted content in one folder: scenes, images, audio, text, data.
- The shared game never names a restricted label, file or image. Only the folder's own files register themselves.
- The smaller edition is complete from start to end. Optional content changes no shared story or progress state, apart from its own flag.
- Where the larger edition plays the content, the smaller one plays a bridge written for that point.

## The guarded entry

One function or label enters the restricted folder.

1. The caller passes an identifier.
2. The entry looks it up in a registry that only restricted files fill.
3. If it is missing, the entry returns at once, and the shared game continues.

The registry is constant after start. A save must not hold it.

## Build rules

- Use an allow list. A file that no pattern allows stays out of every build.
- Give the restricted folder its own pattern that only the larger edition uses.
- Exclude caches and combined bytecode. They can hold code from every source file.
- Exclude tests, sources and tools.
- Compare the built file list with the sources, so an allow list that is too narrow also fails.

## Leak checks

Run on the packaged smaller edition:

1. Collect every restricted name: labels, images, file stems. Fail if the list is empty.
2. Search every file name and every file's content, with compiled and compressed files unpacked.
3. Scan shared sources for those names.
4. Check that only the folder registers scenes, and that only the entry reads the registry.

Test the name collector on samples of every form the engine offers, such as layered images and file-based images. A form it misses is a leak it cannot see.

## Saves across editions

A save from the larger edition loads in the smaller one at the last shared point, then plays the bridge. Rules and tests: `saves.md` in `game-programming-patterns`.

## Playing each edition

- Run the story and route suites on both packages.
- Coverage differs. Labels and options must be reached in every edition that holds them.
- Refusing or skipping optional content costs nothing and leads on.

## Checklist

- Both builds come from one command and one tree.
- Every store page names the right edition, and its rating and disclosures match.
- License notices are in both.
- Sizes are checked for both.
- Live policy pages were read on the release date.
- A person approved the content table. See `game-quality-gates`.
