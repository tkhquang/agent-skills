# Metrics

Contents: tiers of metrics, definitions, benchmarks, reading the retention curve, first-session fixes, spender buckets, the guessing game, modelling notes.

Benchmark figures here are rough guides for planning, each labeled with its date and origin.

## Tiers of metrics

| Tier | Purpose | Count | Examples |
|---|---|---|---|
| Key indicators | Financial vital signs | Fewer than seven, ideally three | Active users, a retention measure, conversion, average spend |
| Performance indicators | Health checks that do not feed the forecast directly | A handful | Uptime, matchmaking wait, recommendation score, virality |
| Diagnostics | Everything else | Many | Session length, level completion, currency balances |

For diagnostics the direction often does not matter. If session length goes up or down while the key indicators are healthy, leave it. Consult diagnostics when a key number moves, like a doctor ordering tests only when vital signs suggest a problem.

One team tracked 157 "key" indicators, which is none. When everyone in the company knows the one or two numbers that matter, everyone pulls the same way.

Instrumentation is a trade-off. Each day spent on telemetry is a day without real players. A sensible minimum for a first release: the key indicators and progress through the first session.

## Definitions

| Term | Meaning |
|---|---|
| DAU, WAU, MAU | Distinct players active in a day, week, month |
| D1, D7, D30 retention | Share of players from day zero who play again exactly 1, 7, 30 days later |
| Stickiness | DAU divided by MAU |
| Cohort | A group that started in the same period, followed over time |
| Conversion rate | Share of active players who spend in the period. State the period and who is in the denominator |
| Lifetime conversion | Share of all players to date who have ever paid |
| Cohort conversion | Share of one cohort who have paid at least once by day N |
| ARPDAU | Daily revenue divided by daily active users |
| ARPU | Revenue divided by all users in the same period, usually monthly |
| ARPPU | Revenue divided by paying users in the period |
| LTV | Revenue expected from a player over their whole time in the game |
| CPI | Cost of one tracked install from paid marketing |
| Effective CPI (eCPI) | All marketing cost divided by all new players, paid and organic |
| Basket size | Value of one transaction |

Relationships:

- ARPU = ARPPU x conversion, when all of them use the same period and the same players. One million in revenue from 100,000 players at 10 percent conversion is an ARPU of 10 and an ARPPU of 100.
- Average daily spend per payer = transactions per payer x basket size. Both are levers.
- A service game works when the cost of getting a player stays below that player's lifetime value.
- Active users = new players + retained players. Act on those two, not on the total.

Measures that mislead:

- Total downloads only rise and say little. Watch daily new users.
- Lifetime conversion can fall as well as rise, because new arrivals join the denominator before any of them pay: ten payers among 100 players is 10 percent, and after 100 more non-paying arrivals it is 5 percent. In an older game its movements cannot be tied to a cause.
- Use daily or monthly conversion to judge changes. Cohort conversion is the version that can only rise.

## Benchmarks

The sets of figures below do different jobs.

Targets for a strong daily-play mobile game, from one practitioner around 2018:

| Measure | Rough guide | Note |
|---|---|---|
| D1 / D7 / D30 retention | 40 / 20 / 10 percent | A top-tier target, not the norm. Misleading for games played twice a week |
| Later months | Model about 25 percent drop per month after day 30 | For forecasting only |
| Conversion, mobile | 1 to 3 percent | Lower end for daily, higher for monthly |
| Conversion, PC | 5 to 10 percent monthly | Higher figures exist. Do not plan on them |
| Cost per install, mobile | 1 to 5 dollars, far more before major holidays | Driven by competition |
| Paid versus organic | Plan on a quarter paid, three quarters organic | A starting guess |

Where live mobile games stood in October 2026, from the GameAnalytics benchmarks page. Worldwide, games with at least 10,000 monthly active users: about 5,500 games for retention and engagement, about 1,800 for the money rows.

| Measure | Bottom quarter | Median | Top quarter | Top 5 percent |
|---|---|---|---|---|
| D1 retention | 12 percent | 21 percent | 28 percent | 41 percent |
| D7 retention | 2 percent | 4 percent | 7 percent | 16 percent |
| D30 retention | 0.4 percent | 0.9 percent | 2 percent | 7 percent |
| Stickiness | 5 percent | 6 percent | 8 percent | 21 percent |
| Sessions per daily player | 3.1 | 4.5 | 6.3 | 10.4 |
| Session length, minutes | 2 | 3 | 5 | 10 |
| ARPDAU, dollars | 0.001 | 0.011 | 0.073 | 0.69 |
| ARPPU, dollars | 5 | 11 | 25 | 213 |
| Transactions per payer | 1.3 | 2.0 | 3.8 | 17.5 |

How to use them:

- The 40 / 20 / 10 shape describes roughly the best one game in twenty on day 1, and better than that by day 30. The table covers only games that already have an audience, so most released games sit lower still.
- The top 5 percent column is far above the top quarter on every money row. Spend is concentrated across games as well as across players.
- Compare a new game with the market table to see where it stands, and with the target shape to see how its curve decays.
- Observed conversion in games that satisfied their makers runs from 0.1 to 10 percent. A benchmark tells you what kind of game you have. It is not a goal.
- Markets, platforms and prices move. Check current figures for your genre and platform before committing money.

## Reading the retention curve

Compare D7 / D1 and D30 / D7 with the market table: about 0.2 and 0.2 at the median, 0.25 and 0.3 for the top quarter, 0.4 and 0.45 for the top 5 percent. Halving at each step is the top-tier target.

| Pattern | Example | Meaning | Response |
|---|---|---|---|
| Low start, typical decay | 15, 4, 1 | The first session loses people. Those who get through behave normally | Fix the first-time experience. Later numbers should rise with it |
| Good start, steep fall | 25, 3, 0.3 | Death by a thousand cuts. Players leave steadily for many small reasons | Review the first weeks for confusion, overload and difficulty mismatch |
| Good early, cliff at a point | Sharp drop at one level or day | A specific wall | Inspect what happens there |
| Flat and low | Low at every point | The core is not compelling to this audience | Reconsider the core or the audience |

Death by a thousand cuts usually means players are not kept at the right edge of their competence: able enough to feel capable, stretched enough to feel challenged.

Typical causes: a tutorial that holds hands so tightly that players pass it without understanding and then drown; complexity delivered in one lump instead of in layers; feedback that does not ring true.

## First-session fixes

- The purpose of the first session is to show the fun. Teaching is in service of that.
- Metrics show where people drop out of the first-session funnel. Watching players shows why.
- Common culprits: forced account creation, unskippable scenes, a long wait before control, one action that is too hard.
- The first thirty seconds earn the next thirty. The first minute earns the next minute.
- Keep it easy and intuitive, and representative. An opening that misrepresents the game only postpones the loss.
- Every extra thing to think about adds friction. Friction beyond a threshold ends the visit.
- A paid game can afford a brutal opening because the sale already happened. A service game cannot.

## Spender buckets

Group players to build a mental model and to see which lever is missing.

| Group | Definition by share of payers | Or by monthly spend |
|---|---|---|
| Players | Do not pay | 0 |
| Tippers | Bottom 50 percent of payers | Under about 5 |
| Fans | Next 40 percent | Between |
| Superfans | Top 10 percent | Over about 20 |

- Many payers and no superfans: nothing worth spending heavily on.
- Superfans and no tippers: the value of spending is invisible until someone is deeply invested.

## The guessing game

Before building a feature, have each person write down which measures it will move, in which direction and by how much, and then explain why. Record the guesses and the average. Check them when results arrive.

- Call it guessing, not forecasting, or people decline to take part.
- The value is in forcing everyone to form a model of the game and in exposing disagreements about what a feature is for.
- One team brainstormed a "retention update", played the guessing game, and found that every person expected every idea to raise spending and none to raise retention. They kept the ideas for later and started again.

## Modelling notes

- Model retention by cohort: each day's or month's arrivals as a group that decays over time. A simple version uses D1, D7 and D30 for the first month and a steady monthly decay after.
- Marketing has a halo: paid installs raise visibility and bring organic ones.
- Forecast revenue as active users times conversion times spend per payer, and check that lifetime value exceeds the blended cost of acquiring a player.
- The same total revenue can come from a mass audience with low spend or a small audience with high spend. Know which game you are making.
- Do not tune one measure in isolation. A shorter promised session may leave session length flat while sessions per day rise.
