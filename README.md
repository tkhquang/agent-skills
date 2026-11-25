# Game development skills

[Agent Skills](https://agentskills.io) that help an AI coding agent design, build, test and release games. Each skill is a short workflow plus reference files that load only when they are needed.

Design:

| Skill | Use it for |
|---|---|
| [game-concept-prototyping](skills/game-concept-prototyping/SKILL.md) | Generating and testing game ideas, concept documents, prototype and vertical slice plans, playtests |
| [game-systems-design](skills/game-systems-design/SKILL.md) | Core loops, feedback loops, economies, decisions, randomness, puzzles, solver-checked levels, multiplayer rules |
| [game-balance](skills/game-balance/SKILL.md) | Stats, costs, counters, XP curves, pacing, drop rates, in-game economies and simulation, with calculator scripts |
| [game-feel](skills/game-feel/SKILL.md) | Tuning movement, jumping, aiming and impact, input forgiveness and polish |
| [game-retention-monetization](skills/game-retention-monetization/SKILL.md) | Long-term structure, sessions, retention, pricing, passes, metrics and ethics |

Engineering and release:

| Skill | Use it for |
|---|---|
| [game-programming-patterns](skills/game-programming-patterns/SKILL.md) | Game loop, components, state machines, events, pooling, data layout, a testable rules core and saves |
| [game-quality-gates](skills/game-quality-gates/SKILL.md) | Named checks, automated playtests, route coverage, budgets and verification of agent work |
| [game-release-targets](skills/game-release-targets/SKILL.md) | Several stores, portals and editions from one codebase, platform adapters, package checks |
| [game-asset-pipeline](skills/game-asset-pipeline/SKILL.md) | Asset manifest, provenance, licenses, approvals and QA, with a manifest check script |

## Install

With the `skills` CLI, for any agent that supports Agent Skills:

```bash
npx skills add tkhquang/agent-skills                        # Every skill
npx skills add tkhquang/agent-skills --skill game-balance   # A single skill
```

With the GitHub CLI:

```bash
gh skill install tkhquang/agent-skills --all
gh skill install tkhquang/agent-skills game-balance
```

As a Claude Code plugin:

```text
/plugin marketplace add tkhquang/agent-skills
/plugin install game-development@tkhquang-agent-skills
```

By hand: copy any folder from `skills/` into your agent's skills directory, for example `~/.claude/skills/`.

## How the skills are built

- `SKILL.md` holds the workflow and the tables an agent needs on most requests.
- `references/` holds the depth, split by topic so an agent reads one small file at a time.
- `scripts/` inside a skill holds calculators and checks. They need Python 3 and nothing else.
- The ideas and perspectives come from *Advanced Game Design* (Sellers), *Challenges for Game Designers* (Romero and Schreiber), *Game Feel* (Swink), *Game Programming Patterns* (Nystrom), *The Pyramid of Game Design* (Lovell) and multiple other sources.

```bash
python skills/game-balance/scripts/balance_tools.py drop --rate 1% --tries 100
```

## Development

[AGENTS.md](AGENTS.md) holds the layout, the gates and the writing rules.

```bash
python scripts/validate_skills.py     # Specification limits, links and writing rules
python -m unittest discover tests     # Script and validator tests
claude plugin validate .              # Plugin and marketplace manifests
```

## License

[MIT](LICENSE)
