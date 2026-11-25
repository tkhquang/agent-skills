# Playtesting

Contents: when and who, preparation, session script, survey template, methods, reading the results, warning signs and fixes.

## When and who

- Start before the game feels ready. "It's not ready yet" is the usual excuse and waiting is the usual mistake.
- More short tests beat fewer long ones. Test after every significant change, whenever the direction is unclear, and at least every couple of weeks. Weekly or more often near the end.
- Not the designer. Not the team, friends or family either: they bend over backward to like it.
- A person can be a naive tester only once. Keep a steady supply of new people, because testers who have learned the game can no longer judge its difficulty or clarity.
- Match the target audience as the game matures, without narrowing so far that you miss people who would love it. Treat opinionated expert players with care: more noise than signal.
- Very rough prototypes can stay with a few trusted outsiders who can see past stand-in art.

## Preparation

1. Write the goal of this test in one sentence. Everything else follows from it.
2. Write a script, word for word, covering greeting, warm-up, consent, the session, questions and goodbye. Run the script once on a teammate before using it.
3. Prepare how you will record: a notes form at minimum. Video of screen and face is useful later in development and costs a lot of analysis time.
4. Any quiet place works. Do not wait for a lab.

## Session script

```text
GREETING
"Thanks for coming. This takes about [15] minutes."
Warm-up: "What games have you been playing lately?"

CONSENT
"We are testing the game, not you. Nothing you do is wrong.
You can stop at any time, and answering questions is optional."
[Get a clear yes.]

SETUP
[Say as little as possible. Choose one, and keep it the same for every tester:
 a) nothing at all, and say that you are deliberately not explaining
 b) only the title or box art
 c) the one-line pitch]

PLAY  (10 to 20 minutes)
[Stay out of their line of sight. Do not hover.]
If they ask for help: "What would you try if I weren't here?"
If they ask if they are doing it right: "You're doing fine, keep going."
Never point at the screen, never explain, never defend.
If they want to stop, stop. That is data.

END OF PLAY
"What were you trying to do just now?"
"What did you expect to happen?"

DEBRIEF
"What are your first thoughts?"   [Write the first sentence down exactly.]
[Hand over the survey.]
"Anything else you want to say about it?"
"Thank you."
```

What to write down during play: what they do first, what they ignore, where they hesitate, where they repeat an action, exact quotes, and every visible feeling (surprise, delight, confusion, frustration, leaning in).

## Survey template

Keep it short and tied to the goal of this test. Balance positive and negative options, and randomize order when the tool allows.

```text
Rate each statement:
(Disagree strongly / Disagree / Neutral / Agree / Agree strongly)

1. It was easy for me to [move around / take my turn / use the menus].
2. I understood what was going on at all times.
3. I had clear goals in mind that I was trying to accomplish.
4. I could play this again without reviewing the rules.
5. [One statement about the specific thing this test is about.]

Circle every word that fits your experience:
Exciting  Fast  Confusing  Boring  Overwhelming  Thoughtful
Strategic  Broken  Engaging  Relaxing  Frustrating  Slow

Short answers:
- Briefly explain the rules as you understand them.
- What surprised you?
- What did you think you were supposed to accomplish?
- What games did this remind you of?
```

Comprehension probes, best asked aloud: show an icon and ask what it means; show a screenshot and ask "what would you do next?"; ask "how would you find out how many soldiers you have?".

"How much would you pay for this?" tells you how they feel. It does not tell you a price.

## Methods

| Method | Use it when | Note |
|---|---|---|
| Observation | Always | Watching beats asking |
| Directed task | Testing one feature or a returning tester | Give a goal, not instructions |
| Free exploration | Finding what draws or repels attention | Note what they avoid |
| Wizard of Oz | Paper or very early tests | You play the computer. Low fidelity, good for expectations |
| Think aloud | Players get lost and you cannot tell why | Prompt "please keep talking". Performance drops, insight rises |

Core gameplay suits short observed sessions. Long-term structure needs tests that run for days.

## Reading the results

- Write impressions immediately after each session.
- Look for what several testers share. One person loving it and one person hating it are both outliers.
- Aim for direction, not statistics. Small samples cannot prove anything, and they can still tell you where to look.
- Track the same questions across builds to see whether changes helped.
- Players are good at symptoms, poor at diagnosis and unreliable at treatment. When someone proposes a fix, ask what problem they were trying to solve.
- Loud minorities mislead. A handful of angry voices can be a tiny fraction of players. Check behavior data before reversing a change.
- Be willing to follow the fun. Testers of a pirate game found exploration to be filler and combat to be the game, so the game became ship battles. Testers of a life simulator cared about relationships and stories, not upkeep, and the design moved toward them.

## Warning signs and fixes

| What you see | Likely cause | Try |
|---|---|---|
| Players are bored | Too much luck, or too few interesting decisions per minute | Turn random events into choices, shorten the game |
| Players are bored except on their own turn | No reason to care about others' actions | Add interaction during other turns, shorten turns |
| Players never engage or do not know what to do | Too complex, too many decisions, too much information | Automate or remove decisions, simplify rules, reveal systems gradually |
| One player wins by a mile | Skill dominates a mixed group, or a runaway leader loop | Add some randomness or a catch-up mechanism |
| Players cannot say why they lost | Cause and effect are unclear | Improve feedback, expose the rule that decided it |
| Players miss "obvious" information | The interface hides it | Move it to where their eyes already are, add a second channel |
| Players stall at one spot | A stuck point with one hidden solution | Add clues, allow another solution, give another goal to pursue |
| Players quit early in the first session | The first minutes do not show the fun | Cut setup, get to the core action faster |
| Players stop making plans | No long-term goals visible | Show the next goal and a farther one |

Questions that reveal strategic depth: Do players care during other players' turns? Are they making long-term plans (ask "how do you think you will win?")? Do different players describe different strategies?
