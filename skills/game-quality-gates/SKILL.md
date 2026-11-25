---
name: game-quality-gates
description: Sets up named quality gates and automated playtests for a game repository. Covers checks by risk, a change-to-gate map, a test bridge that plays the built game, route coverage for branching stories, screenshot review, frame and size budgets, gates that prove they can fail, contract and code agreement, and verification rounds. Use when the user asks how to test a game, writes AGENTS.md or contributor rules, wants CI, smoke or screenshot tests, a performance budget or a definition of done for an agent, asks whether a change is safe to ship, or reports passing tests on a broken game, flaky tests, or docs that disagree with code.
license: MIT
---

# Game quality gates

A gate is a named command that passes or fails for a stated reason. A change is done when its gates passed on that exact tree. Gates prove that a game works as specified. They do not prove that it is fun.

## Workflow

1. List what can hurt a player: lost progress, a dead end, a crash, a wrong rule, an unreadable screen, a stall, content in the wrong build.
2. Pick the cheapest check that can see each one. Use the table below and `references/gate-catalog.md`.
3. Write a contract table in the repository's contributor or agent document: gate, command, proves, kind, state. See `references/engineering-contract.md`.
4. Map change types to gates. A change runs the union of its rows.
5. Wire a gate when its subject first exists: a save gate with the first save, a performance gate with the first real scene. List the others as "Not wired". Never report them as passed.
6. Build a test bridge with the first screen. See `references/test-bridge.md`.
7. Break the game on purpose and watch each gate fail. See `references/gate-integrity.md`.
8. Run the gates on the final tree. Record command, result and tree hash. Example: `git write-tree` after staging, or the commit hash of a clean tree.
9. Look at every captured image. Ask a person about feel, difficulty and taste.

## Choose a check

| Risk | Check | Reference |
|---|---|---|
| A rule is wrong | Unit tests on the rules core | `game-programming-patterns` |
| A level cannot be finished | Solver or recorded solution for every level | `game-systems-design` |
| A route is unreachable or ends nowhere | Route coverage | `narrative-gates.md` |
| Shipped dialogue differs from the approved script | Script sync | `narrative-gates.md` |
| The built game does not start, or a flow breaks | End-to-end run on the built game | `test-bridge.md` |
| Touch, resize or rotation breaks play | The same run at phone sizes, rotated in the middle | `test-bridge.md` |
| Text clips, overlaps or is too small | Captures at every reference size, inspected | `test-bridge.md` |
| Frames drop | Percentile frame budget on a worst-case sample | `test-bridge.md` |
| The download is too large | Size budget on the production build | `gate-catalog.md` |
| An old save fails | Fixture for each released save version | `game-programming-patterns` |
| A platform service fails | Mock service that fails, hangs or refuses | `test-bridge.md` |
| Debug tools or unlicensed files ship | Search of the built package | `gate-integrity.md` |
| An agent reports work that is not done | Fresh verification bound to the tree | `verification-rounds.md` |

## Kinds of gate

State the kind in the contract. The last column is the limit of what it proves.

| Kind | Example | Limit |
|---|---|---|
| Pass or fail command | Unit tests, build, size budget | Only what it observes |
| Capture, then inspection | Screenshots, contact sheets | A zero exit code proves only that files exist |
| Review against a list | Content rules, checked line by line | Keep the line table as evidence |
| Manual on a device | Install, touch, rotate, background, resume | Names the device and build |
| Attestation by a person | Feel, difficulty, onboarding | Names the build. Ends when behavior changes |

An agent cannot attest for a person. It gives the exact build, command and checklist, then waits.

## Map changes to gates

Adapt this table. Keep it in one place.

| Change | Required |
|---|---|
| Rules, random numbers, opponent | Types or compile, lint, unit, levels |
| Level or encounter data | Levels, unit, end to end |
| Script, dialogue, menus | Compile, script sync, route coverage, content review |
| Scenes, input, layout | Build, end to end, phone run, captures |
| Motion, effects, audio | Build, end to end, captures |
| Save format, released names | Unit, save fixtures, end to end |
| Platform service, ads, purchases | Build, mock service, end to end |
| Assets | Asset check, build, size, captures |
| Build config, dependencies | Everything automatic |
| Comments and documents | Agreement tests only |

## Trust rules

- Compile or build before tests, on the same tree. Stale output gives false passes.
- Test a clean copy: no saves, no caches, no compiled leftovers, an empty user folder.
- Prefer the packaged build over the source tree for the last run.
- Zero retries, and no focused or skipped tests in the gate run.
- An unavailable gate is "Not run" with the reason. Never substitute another one.
- A fix ships with a test that failed before it.
- Keep captures and reports in an ignored folder. Stop every server the run started.

## Quick diagnosis

| Symptom | Likely cause | Fix |
|---|---|---|
| Tests pass, the game is broken | Tests read the model, or their own input, and not the built game | Play the built game through the bridge |
| A gate passes after you break the thing | Empty list, wrong path, or a search that finds nothing | Positive control, non-empty assertions |
| The runner exits with 0 after a script error | The engine swallowed the error | Count the checks, or require an end marker |
| A test passes alone and fails in a run | Shared state, or a wait on time | Fresh state for each test, wait on bridge state |
| The performance gate flips | Busy machine or software renderer | Idle machine, hardware check, percentiles |
| Screens clip on one device | Captures cover too few sizes | Take reference sizes from each platform's page |
| The document says one thing and the code another | A number has more than one owner | One owner, plus an agreement test |
| The full run takes too long | Every gate on every change | Change map, samples of worst cases, release-only gates |
| Review rounds never end | Style findings reopen finished work | Lint style, and use the stop rule in `verification-rounds.md` |

## Output formats

Gate row: gate, command, proves, kind, state (Wired, Manual, Not wired).

Run report: tree hash, then a table of gate, command, exit code, key numbers, images inspected. Then "Not run" with reasons, and open questions for a person.

## References

- `references/gate-catalog.md`: gates by area, with what each proves and how it fails to.
- `references/engineering-contract.md`: sections of the contract file, who owns which fact, dependency policy, a template.
- `references/test-bridge.md`: bridge shape, driving the game, mock services, captures, performance runs, soak runs.
- `references/gate-integrity.md`: gates that prove they can fail, agreement tests, budgets, package searches.
- `references/narrative-gates.md`: script sync, route coverage, state rules, saves and content review for branching stories.
- `references/verification-rounds.md`: blind audits, evidence bound to a tree, stop rules, choosing the size of the process.

## Related skills

`game-programming-patterns` for the testable core and saves, `game-balance` for simulation, `game-systems-design` for solver-checked levels, `game-asset-pipeline` for asset checks, `game-release-targets` for platform builds, `game-concept-prototyping` for playtests with people.
