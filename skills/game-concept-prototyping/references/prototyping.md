# Prototyping

Contents: what counts as a prototype, the big questions, rules for speed, minimum products, prototyping the long-term layer, plan template, vertical slice, pivot meeting.

## What counts

A game prototype is any working portion of a game that allows at least one interactive loop: the player forms an intent, acts, the game state changes, and feedback comes back. A mockup, an animation or a gameplay video is not a game prototype, though each can be a valid test of something else (look, tone, stakeholder interest).

The first milestone of any project is closing that loop. Not the level editor, not the icon set, not the backstory. Until the loop is closed and found engaging there is no game.

Expect first ideas to be bad. Experienced designers report that half or more of their prototypes are not fun. That is the system working.

## The big questions

1. Is it fun? Only playing answers this. Small, simple ideas can still feel wrong in the hands (a shooter where recoil is your only movement sounded great and felt passive).
2. Is it viable? Building the prototype previews production. If puzzles for a puzzle game are easy to invent, the ground is fertile. If the prototype alone takes weeks, the project is larger than it looked.
3. Will other people care? A playable thing shared with strangers gives a far better signal than a pitch. Silence is also an answer, and a cheap one.

Prototypes can also test art style, camera, narrative (as a rough storyboard with stand-in voices) or technology. Name which question each one serves.

## Rules for speed

The rules in SKILL.md apply. Also:

- Keep gameplay, art, technical and audio prototypes in separate projects.
- A different engine or language helps guarantee the code is thrown away.

Prototyping does not end at production. A new feature, boss or level deserves the same treatment, and two quick variants in front of testers beat an argument.

## Minimum products

Separate lenses, then their combination.

| Name | Question | Who asks it |
|---|---|---|
| Minimum feasible product | Can we make this? | Engineering |
| Minimum viable product | Will enough people pay for or want this? | Business |
| Minimum desirable product | Will people say "I want to play that"? | Marketing |
| Minimum awesome product | What is the smallest thing that delivers the vision, makes players say "that's awesome", and can sustain us? | The game maker |

Common mistake: asking "can we build it?" before "should we build it?". Be explicit about which lens a prototype serves, because a team can argue for weeks while one person means desirability and another means feasibility.

Ways to test viability and desirability: announce and measure (trailer, store page, crowdfunding, wishlists) or build and control access (closed beta, early access, soft launch). Both can end in a cheap, useful "no".

Spending to reduce the risk of an imperfect product (more polish, more features, famous voices) raises the money at risk and the bar for success. Test whether you can find and keep an audience before paying for polish.

## Prototyping the long-term layer

Games that rely on progression, collection or daily return need a second prototype for the layer that keeps people playing for weeks. It can be a spreadsheet with a few macros.

1. Know what the moment-to-moment game is, or that there is none, so testers can imagine it.
2. Start with a Play button. Make time pass for about ten seconds while the tester imagines playing. Do not shorten the wait to zero.
3. Show a results screen with simulated rewards (currency, experience, items, losses) and a clear "well done".
4. Show the home screen with the persistent record: level bar, currency, inventory, upgrade tree, map, stars.
5. Go round again and again. Notice what you want to spend on and what you look forward to. Add one candidate system at a time (tasks, map, upgrades, leaderboard) and state what each iteration is meant to teach.

The test: do players want to go back into the imagined gameplay repeatedly to earn things that matter on the home screen?

Guidance:

- Keep artists away from this prototype. Good art creates emotional attachment exactly when you need to throw ideas out, and it wins arguments because it is easy to understand. If it is fun when crude it will be more fun with art.
- No art does not mean no usability. Buttons look like buttons, things have labels, icons are recognizable.
- Only systems-minded testers can evaluate it, and it needs longer tests than a gameplay prototype.
- Decide when to merge it with the gameplay prototype. Too late and you have two games that do not fit. Too early and iteration slows from hourly to weekly and feedback drifts to camera and controls.

## Prototype plan template

```markdown
# Prototype plan: [game]

| Question | Why it matters (what changes if the answer is no) | Lens | Medium | In | Deliberately out | Time box | Kill or pivot signal |
|---|---|---|---|---|---|---|---|
| Is the core action fun for five minutes? | Everything else builds on it | Desirable | Paper / engine grey box | One action, one obstacle, one goal | Art, menus, audio, save | 2 days | Testers stop early or cannot say what was fun |
| | | | | | | | |

## Assumptions about the player
- What they know going in:
- Their goal in this prototype:

## What happens to the prototype afterwards
[Deleted / kept only as reference. Code is not reused.]
```

## Vertical slice

A vertical slice is one segment of the game with every system working together at near-final quality: interface, controls, art, audio, saving. A prototype samples one feature for the team. A slice shows the whole stack to someone else.

| | Prototype | Vertical slice |
|---|---|---|
| Question | One design question | "Is this the game, at this quality, and what will the rest cost?" |
| Audience | The team | Publishers, investors, management, players at a show |
| Quality | As rough as possible | Close to shippable for one segment |
| Risk reduced | Building the wrong game | Failing to deliver the game that was promised |
| Afterwards | Thrown away | Often production's starting point, so build it properly |

Build one only after prototypes have shown the core is fun. A slice is far too expensive a way to find that out.

Plan:

1. Audience and decision. Who will see it, what they decide afterwards (fund, sign, schedule), and how long they will spend with it. Twenty minutes with a senior audience is common, which favors features understood quickly.
2. Segment. Ten to twenty representative minutes, not the easiest part to build: the core loop, one example of each major system, one arc from start to a satisfying stop.
3. Quality bar. Write the target for design, code, art, animation, audio, interface and performance, and the platform it must run on.
4. Real versus faked. List what is built and what is staged. Declared fakes are fine. Undeclared fakes become promises.
5. Cost record. Log hours per discipline, per asset and per feature. This measured cost of one unit of content is the main thing a slice gives the team.
6. Time box, and what gets cut first if it slips.

What a slice cannot show:

- That the rest is "just more levels". Systems interact, and new content keeps exposing new interactions. Multiply the measured cost, then add for what the slice left out.
- Long-term play. Progression and economies that unfold over weeks are nearly invisible in twenty minutes. For service or progression-heavy games, show the long-term layer prototype beside the slice.
- Whether an audience exists. That needs real players: see "Minimum products".

If outsiders only need to see the direction and cannot look past grey boxes, a non-interactive video of the intended game is often cheaper. It still costs time, so make it on purpose.

```markdown
# Vertical slice plan: [game]

Audience and decision:
Time they will spend with it:
Segment and why it is representative:
Systems included:

| Discipline | Quality bar | Real | Faked or placeholder |
|---|---|---|---|
| Design | | | |
| Code | | | |
| Art and animation | | | |
| Audio | | | |
| Interface | | | |

Platform and performance target:
Time box, and what gets cut first:
Costs to measure (hours per level, character, feature):
What this slice will not show, and how that gets tested:
```

## The pivot meeting

1. Fix a date. A week or a month for rapid prototyping, three to six months at most for larger cycles.
2. Write the questions the meeting must answer. Examples: Is the core gameplay working? Is the long-term layer working? Do they work together? If not, which one changes? What will people pay for? Will players keep playing? How will we reach players affordably?
3. Until the date, do only work that helps answer those questions. Do not polish.
4. At the meeting choose one: continue, change direction, or stop. Changes are usually small (swap one progression structure for another) and occasionally large (the long-term layer turned out better than the core, so rebuild the core to suit it).
5. Set the next date and questions.

It only counts as a pivot if you set out to learn that thing. Otherwise it is a mistake being renamed. The meeting also parks circular debates: "we decide that at the pivot meeting". It must not feel like an approval gate to be gamed.
