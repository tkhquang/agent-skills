# Engineering contract

Contents: what it is, who owns which fact, sections, writing rules that hold, dependency policy, template.

## What it is

One file at the repository root that states the engineering rules of the project. Examples: `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`. An agent reads it at the start of every task, so it is the cheapest place to stop a repeated mistake. Keep it to rules and tables. Reasons and history belong in design documents.

## Who owns which fact

Each fact has one owning document. The others point to it.

| Document | Owns |
|---|---|
| Engineering contract | Layout, gate commands, invariants, bans, pinned versions, reference sizes, budgets |
| Design document | Game rules, content rules, art direction, intentional choices |
| Roadmap | Scope, order of work, status |
| Requirements note | Platform limits, each with its source and the date read |

A number stated in more than one place needs an agreement test. See `gate-integrity.md`.

## Sections

| Section | Holds |
|---|---|
| Stack | Each tool and library with its pinned version |
| Layout | Path and what it holds, plus what is ignored |
| Gates | Name, command, what it proves, kind and state for each gate |
| Change map | Which gates each kind of change must pass |
| Architecture invariants | Short rules, each with the gate or test that enforces it |
| Bans | What the linter or tooling tests reject |
| Reference sizes | Screen sizes the game must work at, each with its source and the gates that use it |
| Budgets | Size, file count and frame limits, each with its source and the key that holds it in code |
| Dependency policy | How a dependency is added |
| Assets | Where sources live, what the game loads, how exports are built |
| Release | Targets, signing, submission steps |

## Writing rules that hold

- Write each rule so that a command can check it. "Rules import no engine code" can be checked. "Keep the rules clean" cannot.
- Name the gate or test that enforces a rule next to the rule. A rule with none is a wish.
- State exact units, such as "1 MB is 1,000,000 bytes".
- List a gate that does not exist yet as "Not wired", with the change that will wire it.
- When a rule changes, change the contract and the check in the same commit.

## Dependency policy

- Pin every dependency to an exact version and commit the lock file.
- A new dependency states its purpose, license and size cost before it is added.
- A runtime dependency needs a license that permits the game's distribution, and its notice ships with every build.
- Load nothing from another host at run time, unless a platform requires its own script.

## Template

```markdown
# Engineering contract

This file owns: layout, gate commands, invariants, pinned stack, reference sizes, budgets.
[Design document] owns game rules. [Roadmap] owns scope and status.

## Stack
| Item | Version | Note |
|---|---|---|

## Layout
| Path | Holds |
|---|---|

## Gates
| Gate | Command | Proves | Kind | State |
|---|---|---|---|---|

## Change map
| Change | Required gates |
|---|---|

## Architecture invariants
- [Rule]. Enforced by [gate or test].

## Bans
- [Ban]. Enforced by [gate or test].

## Reference sizes
| Size | Source | Gates |
|---|---|---|

## Budgets
| Budget | Key in code | Limit | Source |
|---|---|---|---|

## Dependency policy
- [Rules]

## Assets
- [Source folder, shipped folder, export command]

## Release
- [Targets, signing, submission steps]
```
