# Gate integrity

Contents: prove that a gate can fail, empty passes, package searches, agreement tests, budgets, evidence, when a gate fails.

## Prove that a gate can fail

| Gate type | Proof |
|---|---|
| Lint ban | Feed each banned form as text. It fails in the restricted folder and passes elsewhere |
| Pattern scan | Known bad and known good samples, asserted as exact lists |
| Build check | Write a minimal fake package that passes, break one thing, expect one named failure |
| Content check | A complete entry passes. Each missing field fails with its own message |
| Regression test | Fails on the old code. Say how that was confirmed |
| Test that guards a rule | Remove or invert the guarded line. The named test fails. Restore the line |
| Level check | Unsolvable, over-length and off-band levels are rejected |
| Document comparison | A paraphrase, a missing line and an unmapped file each fail |

Keep these proofs as permanent tests beside the gate.

## Empty passes

A check that ran on nothing passes. Guard each one:

- Assert that the list being checked is not empty.
- Assert that the expected file exists exactly once.
- Treat an unknown report format as a failure. Do not read it as "No findings".
- Require the runner's success text and a zero exit code.
- If the engine can exit with 0 after a script error, count the checks and compare with a stored number, or print an end marker.
- Fail when a marker file, such as a traceback, exists after the run. Delete it before.
- Compare a search with a build that must contain the text.
- Rebuild when any source is newer than the package.

## Package searches

Check the file that players download, not the source tree. Every search needs a build that must contain the text. Rules: `packaging-checks.md` in `game-release-targets`.

## Agreement tests

When a document and code both state a fact, a test compares them. Give each fact one owner, and point to it from everywhere else.

| Fact | Compare |
|---|---|
| Gate table | The document's rows equal the runner's commands |
| Reference sizes | The document equals the test configuration and the game's design size |
| Budgets | The document's numbers equal the constants that the gate enforces |
| Tool and engine versions | The document equals what is installed |
| Story variables, items, units | The design document's table equals the declarations |
| Script | The approved text equals an export from the game |
| Attribution | Notices equal the shipped fonts and the lock file |
| Listing text | Lengths, tags and images equal each store's limits |
| Generated data | Frame sizes and positions equal the tool that made them |

Parse tables by heading. Fail when the heading or table is missing.

## Budgets

1. List each target's limits with source and date. See `game-release-targets`.
2. Take the strictest for each measure, or keep a budget for each target.
3. Measure the production build. State what the number counts.
4. Print measured and allowed values on every run.
5. A budget may be tightened in design. Loosening one is a decision with a reason.

Common measures: initial download, total size, file count, largest file, archive size, unpacked size, frame percentiles, longest animation, search positions.

## Evidence

- A result belongs to a tree. Record the hash of the tree it ran on.
- A result stays valid while only documents changed since that tree. Any change to code, data, assets or build files ends it.
- Reports, commit text and roadmap status are claims. Run the gate again.
- An attestation names the person, the goal and the tree, and ends the same way.

## When a gate fails

| Question | Then |
|---|---|
| Does it fail on the base version? | Not caused by this change. Report it and keep it open |
| Is the machine busy or different? | Fix the conditions first, then run again |
| Is the test wrong? | Fix the test and show that it still catches the defect |
| Is the limit wrong? | Ask the owner. Record old value, new value, reason |
| Is the test flaky? | Find the race. Retrying hides it. Wait on state instead of time |

Never edit a limit, a fixture or an expected output in the same step that makes a gate pass without saying so.
