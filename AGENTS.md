# Engineering contract

This file owns the layout, the gates and the writing rules of this repository. `README.md` owns installation.

## Layout

| Path | Holds |
|---|---|
| `skills/<name>/SKILL.md` | The entry point of a skill: frontmatter, workflow, tables, pointers |
| `skills/<name>/references/` | Depth, one topic for each file, loaded only when read |
| `skills/<name>/scripts/` | Python 3, standard library only |
| `scripts/validate_skills.py` | The `VALIDATE` gate |
| `tests/` | Tests for every script and for the validator |
| `.claude-plugin/` | Plugin and marketplace manifests |
| `.drafts/` | Ignored scratch space |

## Gates

| Gate | Command | Proves |
|---|---|---|
| `VALIDATE` | `python scripts/validate_skills.py` | Specification limits, links, and the writing rules marked below |
| `TEST` | `python -m unittest discover tests` | Scripts give correct results, and the validator fails on each rule it enforces |
| `PLUGIN` | `claude plugin validate .` | The manifests load and list every skill |

Run every gate before a commit. A change is done when they pass on that tree.

## Writing rules

Skill text loads into an agent's context, so every word costs tokens.

| Rule | Enforced by |
|---|---|
| The name equals the folder. The description is third person, says what and when, at most 1024 characters | `VALIDATE` |
| The SKILL.md body stays under 500 lines | `VALIDATE` |
| Every bundled file is named in SKILL.md, and every named file exists | `VALIDATE` |
| A reference starts with a title and a `Contents:` line | `VALIDATE` |
| No paragraph or list item over 60 words | `VALIDATE` |
| No em or en dashes, LF line endings, forward slashes in paths | `VALIDATE` |
| Sentences, bullets, headings and table cells start in uppercase | `VALIDATE` |
| No numbered headings, no numbered table columns, no counts in headings | `VALIDATE` |
| No count of items in running text, such as "the five gates" | Review |
| Plain words, no clichés or filler, tables and bullets before paragraphs | Review |
| Written for any engine. A product name appears only as a labelled example | Review |
| Only verified facts. Anything that can go stale is dated or left out | Review |
| Nothing a capable agent already knows | Review |

## Adding or changing a skill

1. Put the workflow and the tables used on most requests in SKILL.md. Move depth to a reference.
2. Split references by topic, so an agent loads one small file.
3. Use a script for arithmetic or checks that must be exact, and test it in `tests/`.
4. Add the skill to the table in `README.md`.
5. Run the gates.
