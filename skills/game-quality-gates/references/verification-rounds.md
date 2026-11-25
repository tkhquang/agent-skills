# Verification rounds

Contents: when to use, choosing the size, evidence bound to a tree, the blind audit, corrections, the stop rule, people in the loop, what it cost, a short form.

A way to check work that an agent wrote, by a session that did not write it.

## When to use

Use rounds for changes to rules, saves, content boundaries, platform services, or anything that is hard to undo after release. Skip them for prototypes and document changes.

## Choosing the size

| Change | Process |
|---|---|
| Documents, comments | Agreement tests |
| A few files, and none of: game rules, saves, identifiers, random numbers, dependencies, build config, platform code, intentional choices, a new asset family | Build, one fresh verification |
| A feature or a system | Build, one review by a fresh session, decide on each finding, then verification until stable |
| A whole-game check before a release | Isolated audit of the game against its own contract |

A change that outgrows its size moves up, and says so. The owner may shorten the process. Record that as a decision, not as a pass.

## Evidence bound to a tree

- Hand over a fixed state, such as a staged index or a commit. The next session starts by checking that the hash matches.
- Write the scope once, from the plan and before reading the diff: what must change, what must not, required gates. Report gaps both ways: required work that is missing, and delivered work nobody asked for.
- Bind each gate result to a tree hash. Reuse one only while later changes touch documents alone.
- Treat earlier reports as claims. Run the gates.

## The blind audit

1. Start a fresh session. It reads the contract, the scope, the code and the running game. It does not read earlier findings, the development log or the author's report.
2. Audit the whole change, not the last correction.
3. Write the findings to a file and freeze it, for example by hash.
4. Only then read the open items from the previous round. Decide each one: resolved, not reproduced, still open, outside this session.
5. Fix, run gates, write the verdict with evidence.

Each finding needs the code, the rule it breaks, and a failing test or a recorded run. Without those it is a question. A taste concern, or a listed intentional choice, is a question for the owner.

Ranks: player progress, correctness, missing test, convention.

## Corrections

- Set a budget for each round, such as 3 production fixes. Progress defects are always in budget.
- Every fix ships with a test that failed before it.
- Do not revert earlier work without stating the defect in the present code. Reverting on preference is how rounds fail to end.
- Review proposals apart from the work, such as unstaged changes over a staged base. The author accepts or rejects each one with a reason from the contract.

## The stop rule

Stable when all hold:

- No open finding.
- No required gate missing.
- This round changed no behavior. Document changes do not count.

A round that fixed behavior needs one more fresh round on the corrected tree. If the base moves, start over.

The owner may stop earlier. The open items stay listed.

## People in the loop

- Feel, difficulty, taste, spending, publishing and intentional design choices belong to the owner.
- Ask with options and a recommendation. Stop when the answer changes what the player sees.
- Record each decision once, with a date, where that fact lives.
- Keep a table of intentional choices: the choice, why it exists, what the opposite breaks. Reviewers may not reverse one.

## What it cost

Rounds are an expensive style checker. In two game projects that ran the full process, 85 of 144 blind findings were conventions and 17 were correctness or lost progress.

- Put conventions in lint and tests first.
- Offer the short form first. One review by a fresh session found most of the real defects.

## A short form

For most projects:

1. The author finishes, runs the gates, and commits to a branch.
2. A fresh session gets the contract, the diff and the build. It writes findings before seeing any report.
3. The author answers each finding: fix with a test, or reject with the rule that overrides it.
4. Rerun the gates that match the changed paths.
5. If step 3 changed behavior in rules, saves or platform code, repeat step 2 once.
