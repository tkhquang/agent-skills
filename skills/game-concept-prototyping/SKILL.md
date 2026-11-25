---
name: game-concept-prototyping
description: Turns a vague game idea into a tested concept. Generates and stress-tests game ideas, writes the concept statement, hook and concept document, plans throwaway prototypes that each answer one question, plans a vertical slice, and designs playtests with real players that end in a continue, pivot or kill decision. Use when the user is starting a game, brainstorming or choosing between game ideas, asking whether an idea is any good, writing a pitch, one-pager or GDD, scoping a jam or indie project, planning a prototype or vertical slice, wondering whether to pivot, or preparing or interpreting a playtest.
license: MIT
---

# Game concept and prototyping

Most ideas that sound fun are not fun once played, and thinking cannot tell which ones. The job at this stage is to find out cheaply, before art, clean code or a long plan make changing course expensive: small ideas, explicit questions, ugly prototypes, strangers playing, and a scheduled decision.

Act as a design partner. Give opinions, name the weakest part of the idea, and propose the cheapest test for it. Do not write a long design document for an idea nobody has played.

## Find the stage first

| The user has | Do this | Read |
|---|---|---|
| No idea, or wants more | Generate many small ideas from several starting points | `references/idea-generation.md` |
| Several ideas, or one untested idea | Run the evaluation tests | "Evaluate" below |
| A chosen idea | Write the core statement, the One Question and a short concept doc | `references/concept-document.md` |
| A concept and wants to build | Write a prototype plan, one question per prototype | `references/prototyping.md` |
| A core already shown to be fun, and a need to show the whole game working (publisher demo, production estimate) | Plan a vertical slice | `references/prototyping.md`, "Vertical slice" |
| Something playable | Plan and script a playtest | `references/playtesting.md` |
| Playtest or soft launch results | Read the results, then run a pivot decision | `references/playtesting.md`, "Reading the results", then "Decide" below |
| A wish to practice or get unstuck | Run a constrained design exercise | `references/design-exercises.md` |

If the stage is unclear, ask what exists now: nothing, notes, a prototype, or a build with players.

## Generate

Use every source below, produce at least ten candidates, two or three sentences each.

1. An existing game, changed: new perspective, theme or medium, or a neglected formula done better.
2. A genre, bent: fix its known annoyance, combine two so each repairs the other, remove a core mechanic, or keep the mechanics and swap the metaphor.
3. A new mechanic: from a real-world activity, from the input device, or one mechanic from another game expanded into a whole game.
4. An experience: a fantasy ("I want to be this"), a theme or a personal story, with mechanics chosen to fit.

A story alone or a mechanic alone is not yet a game idea. Convert each candidate into a playable frame before judging it:

- Goal: what the player is trying to reach in one level or session.
- Obstacle: what stands in the way.
- Fail state: where the obstacles push the player.
- Actions: what the player does about it.

## Evaluate

Run each serious candidate through these tests and state failures plainly.

1. Can this team make it?
   - Check time, people, money and experience.
   - If scope is the problem, cut the expensive part and let the constraint shape the design: a story told over a radio instead of animated characters.
2. Will it stand out and still be understood?
   - It needs a hook (a reason to try it or talk about it) and an anchor (something familiar that says how it plays).
   - A useful shape: simple, with one unexpected thing.
   - Write the news headline. No catchy headline means no hook.
3. Does it appeal before anyone plays?
   - Name the kind: fantasy, exploration, toy, challenge, comedy, nostalgia.
   - Imagine the trailer, the store image and the name. If no trailer comes to mind, say so.
4. Is it fun? Thinking cannot answer this. The output of this test is a prototype question.

Also ask whether the person will still care about this idea after months of work.

## Write the concept

Keep it short. It grows during development.

- Core statement: one or two sentences beginning "This game is about..." or "This game is the experience of being...". If that takes more than two sentences, there is no game yet.
- The One Question: a single yes or no question that settles feature arguments. "Does it rock?" "Is it stealthy?" A feature that does not strengthen the core is cut.
- Entrance test: give a stranger only the statement. Ask what they think they would do, where it starts, how it ends, and whether it sounds worth their time. If their picture differs from yours, fix the statement.

Full structure and a fill-in template: `references/concept-document.md`.

## Prototype

A prototype answers one question quickly. List the questions by risk, biggest first: Is it fun? Can we build it? Will other people care?

- One question per prototype, and the answer must be able to change the game. A team argument is a prototype waiting to be built.
- If nobody can play it, it is not a game prototype. Close one loop first: intent, action, feedback.
- Keep it ugly: no final art, interface polish or clean architecture. In games where feel is the question, add a little juice and check that it reveals the fun and does not cover its absence.
- Use the fastest medium: paper, cards, dice, a spreadsheet, another tool, or a person playing the computer.
- For a discrete puzzle, compare rule variants with a solver on random boards first. See `solver-checked-levels` in `game-systems-design`.
- Many small prototypes beat one bad version of the whole game.
- Never ship prototype code. Rebuild what you learned.
- Stop when the biggest risks are answered.

For service or progression-heavy games, also prototype the long-term layer by itself, often in a spreadsheet.

A vertical slice follows the opposite rules: one representative segment with every system working at a stated quality, built for people outside the team and for estimating production. If the user asks for a slice before the core is known to be fun, say so and plan the prototype first.

## Playtest

- Test before it feels ready, with people who are not the designer, the team, friends or family.
- Prefer many short tests to a few long ones.
- A playtest checks whether players understand the game, form goals and stay engaged. It is not a bug hunt.
- During the session say almost nothing: no hints, no explaining, no defending. Record what they do and say, where they stall, and every visible reaction.
- Afterward, trust the symptoms players report, doubt their diagnosis, and do not adopt their fix without finding the underlying problem.

Session script, survey and analysis rules: `references/playtesting.md`.

## Decide

- Set the decision date before starting the work: days or weeks for a prototype, never more than a few months.
- Write the questions that meeting must answer. Until then, do only work that answers them.
- The meeting ends in one of: continue, change direction, or kill. Then set the next date and questions.
- A cheap prototype that fails has done its job. Watch for sunk cost keeping alive something everyone agrees is not fun.

## Output formats

- Ideas: a numbered list. Each item has a name, a two-sentence pitch, goal / obstacle / fail state / actions, hook, anchor and biggest risk.
- Evaluation: a short verdict per test, the single weakest point, and the cheapest experiment that would resolve it.
- Prototype plan: a table of question, why it matters, medium, what is in, what is deliberately out, time box, and the result that means stop.
- Vertical slice plan: who it is for and what they decide after seeing it, the segment and why it is representative, quality bar per discipline, what is real and what is faked, time box, what it should establish about the cost of the rest, and what it cannot show.
- Playtest plan: goal of this test, who to recruit, script, what to observe, survey, and how results map to decisions.

## Failure modes to call out

- Committing to the first idea without testing alternatives.
- Planning the whole game on paper before anything is playable.
- Polishing a prototype instead of answering its question.
- Treating a vertical slice as proof that the rest is "just more levels".
- Testing only with people who like you.
- Prototyping without end because the next idea might be better.
- Adding features to fix a core that is not fun.

## Related skills

`game-systems-design` for mechanics, `game-balance` for numbers, `game-feel` for controls and juice, `game-retention-monetization` for long-term structure and business model, `game-programming-patterns` for code structure, `game-quality-gates` for proving a build works.
