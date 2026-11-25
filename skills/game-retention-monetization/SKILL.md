---
name: game-retention-monetization
description: Designs the long-term structure and business model of a game. Covers the retention layer and core loop, session design, return hooks, what players pay for, seasonal and battle passes, soft launch scope, live-service metrics and benchmarks, and the ethics of persuasion. Use when the user works on a free-to-play, mobile, live-service or long-running game, asks about retention, D1/D7/D30, churn, daily rewards, energy, battle passes, loot boxes, in-app purchases, ads, ARPU, LTV, soft launch, or why players do not come back or do not spend, and for premium games that need a reason to return.
license: MIT
---

# Retention and monetization

A product game succeeds at the sale. A service game succeeds when people choose to come back for months. Fun in the moment is necessary and not enough, and content cannot carry retention because players consume it faster than anyone can make it. Long-term play has to come from systems.

Give recommendations as trade-offs. This field has few right answers and many consequences to choose between.

## The Pyramid

One game in layers. Do not design a separate game per layer.

| Layer | What it is | Examples | Test |
|---|---|---|---|
| Base | Moment-to-moment play: one level, match or run | A match, a puzzle level, a race | The genre word you would use to describe the game |
| Retention | What gives long-term purpose | Levels, unlocks, upgrades, collections, quests, seasons, story | Would someone still be here in a month, and why? |
| Core loop | The link between the two | Play to earn, earn to progress, progress to want to play | Can the player see why the next round matters? |
| Superfan | Where the game becomes a hobby for a few | Guilds, group competition, deep collection, status | Is there something worth years and serious money to the most devoted? |

Shapes vary. An arcade game is mostly base. A farm or idle game is nearly all retention layer. A social strategy game lives in its superfan layer. Choose the shape on purpose.

A good base layer for a service game is fun, replayable or cheap to produce, unpredictable (other players, randomness, skill, interacting systems), and able to hand rewards to the retention layer.

## The core loop and its screens

Play for fun and rewards, use rewards to progress, progress makes the next play more attractive. The player has to see that link, and the screens before and after play carry it.

- Before play: what you are about to do, why it matters, what you can win, what you can bring (loadout, boosts), and any extra goal for this round.
- After play: what you earned and how it moved you forward, shown visually. Frame the end of a run as an achievement ("you delivered 33 cargo units"), not as "game over".

Checks for any feature here: will the player see it, understand it, and value it? A "no" means more design work.

## The session

Design every visit as these parts.

1. On-ramp: make choosing this game right now easy. The player asks "do I have time?" and "is it worth the effort of starting?". Promise a short, meaningful visit: fast load, a reward for returning, a clear next step.
2. Playtime: fun and progress.
3. Off-ramp: signal that the main things are done, let the player stay if they want, never trap them. People start more readily when they trust they can stop.
4. Return hook: a specific reason to come back.

Shorten the promise and real sessions often get longer while return rate rises. A sixty-second round replayed for forty minutes beats a forty-minute commitment nobody starts.

Details: `references/session-design.md`.

## Retention techniques

Build purpose into the retention layer first. Add return hooks second. Hooks do not fix a weak loop.

| Family | Techniques | Note |
|---|---|---|
| Score | High score, personal best on screen, leaderboards, seasons that reset | Seasons fix the unreachable top score |
| Journey | Levels, an ending, leveling up, a visible map | Show progress |
| Loops | Nested short, medium and long goals | People finish what they have started |
| Time | Real-time timers, appointments the player sets | Player choice separates an appointment from a nag |
| Meaning | Narrative, collection, building something of one's own | Narrative is powerful and expensive. Use it to amplify |
| Tasks | Repeatable challenges, one-time achievements, stars per level | Only about a quarter of players are driven by achievements |
| People | Turns owed to friends, guild commitments, gifts | Strongest and most costly to build |

The full list with cautions: `references/retention-techniques.md`. Return hooks (daily rewards, streaks, appointments, events, notifications) and energy: `references/session-design.md`.

## Money

Players of free games expect the content for free. They pay for how the game makes them feel, amplified by other people seeing it.

Revenue is concentrated in a small share of players, so the design must let people who love the game spend a lot, repeatedly, on things they value, without regret. A trick earns one purchase and loses the player.

- What sells: self-expression, status, progress speed, convenience, gifts and group contributions, content.
- Selling advantage in the long-term layer (faster progress) is accepted. Selling it in moment-to-moment play (more damage) is not.
- Virtual goods need display, agency and permanence.

Details, plus a worked seasonal or battle pass design: `references/monetization.md`.

## Numbers

Track few key indicators: active users, a retention measure, conversion and average spend. Everything else is diagnostic and consulted when a key number moves.

Read the shape of the retention curve. A low start with normal decay points at the first session. A normal start with steep decay points at many small frustrations afterward.

Definitions, current market benchmarks and diagnosis: `references/metrics.md`.

## Order of work

1. Prototype the base layer and confirm it is fun.
2. Prototype the retention layer separately, even in a spreadsheet, and confirm people want to go round again.
3. Join them through the before and after screens.
4. Soft launch the smallest version that is fun, shareable and able to earn.
5. Read retention first, then monetization.
6. Once the loop holds players unaided, add the amplifiers that can wait: daily rewards, events, social extras, notifications.

Amplifiers added early hide whether the core works.

### What goes into the soft launch

The choice for each feature is now or later, and the default is later, when soft launch data can inform it. Ask these questions.

| Question | Ask | Build it now if |
|---|---|---|
| Publicity | Will it help or hurt how players and press see the game? | Adding it after launch would cause a backlash |
| Retrofit | How hard is it to add afterwards? | It is woven into the economy, interface or progression |
| Impact | Which key measures will it move, and how much? | The soft launch cannot answer its question without it |
| Cost | What does it cost in money, delay and attention? | The cost is low. High cost with weak answers above means later |

- Later: daily login bonus, friend connections, seasonal events. Each bolts on.
- Now: an unproven feature central to the vision, boosts that change moment-to-moment play (resented if added later), matchmaking in a player-versus-player game.
- Depends: a challenge system goes in now only if it is the main way rewards reach players.
- A feature whose only justification is "best practice" or "every other game has it" goes later.

## Ethics, built in

A game can adapt its persuasion to each player over months. Treat these as design constraints.

- Never deceive or trick someone into a purchase.
- State odds for random paid rewards, and make the real odds match.
- Do not make the game harder for people who have paid.
- Give a clear stopping point and do not stretch sessions.
- Reward returning more than you punish absence.
- Take particular care with children and with anyone spending or playing beyond their means.
- Judge each mechanic by intent, method and outcome.

Details and a review checklist: `references/ethics.md`. If the user asks for something that crosses these lines, say so plainly and offer the version that does not.

## Diagnosis

| Symptom | Likely cause | First move |
|---|---|---|
| Good downloads, poor day-one retention | The first session fails to show the fun, or early friction | Watch new players. Remove forced sign-up, long intros, the one step that is too hard |
| Good day one, steep fall after | Overwhelmed or under-challenged after the tutorial | Introduce systems in layers. Keep players at the edge of their competence |
| Long sessions, no return | No stopping point and no reason to come back | Add an off-ramp and a return hook |
| People return and never spend | Nothing worth buying, or its value is unclear | Rework what is sold. Check display, agency, permanence |
| A few spend, nobody spends big | No depth for devoted players | Build the superfan layer |
| Big spenders, no small spenders | Value visible only after heavy investment | Add an obvious, generous first purchase |
| Players burn through content | Retention built on assets | Move retention to systems, replay and other players |
| Returning feels like a chore | The first seconds back list problems and tasks | Open with rewards and progress |
| "Pay to win" complaints | Advantage sold in moment-to-moment play, or deceptive offers | Sell speed and expression, not victory |

## Related skills

`game-systems-design` for loops and economies, `game-balance` for progression curves and sinks, `game-concept-prototyping` for testing and pivot decisions, `game-feel` for the base layer's moment-to-moment quality, `game-release-targets` for ad services, consent and store rules.
