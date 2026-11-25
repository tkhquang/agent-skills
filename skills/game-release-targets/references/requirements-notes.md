# Requirements notes

Contents: one file, what to record, sources and dates, from notes to budgets, conflicts, owner actions, note template.

## One file

Keep all platform rules in one note. Code, budgets and design documents point to it. Nothing else repeats a limit, apart from the constants that enforce it, and a test compares those.

## What to record

For each target:

| Group | Examples |
|---|---|
| Technical | Sizes, file counts, path rules, engines or browsers, weakest device, refresh rates, orientation, safe areas |
| Service | Script address, start order, events and when they fire, environments, what throws |
| Ads and money | Break points, frequency, mute and input rules, error codes, what each code means, purchases allowed or not |
| Input | Keys the host takes, scroll prevention, text selection, touch, pause |
| Content | Rating, restricted themes, names, originality, generated content, disclosure |
| Privacy | Consent, children, permissions, policy page |
| Listing | Fields, limits, image and video rules, tags |
| Process | Account, test period, review, update rules, agreement terms that bind other targets |

Record absences too: "No page names a limit for text". It stops the next reader from searching again.

## Sources and dates

- Give each section its page addresses and the date read.
- Mark facts that come from a third party, a form field seen in a dashboard, or an agreement.
- Prefer the platform's own page. Dashboards can enforce limits that no page names. Add what an upload form refused.
- Read the pages again before service code, before each submission, and when the date is older than 90 days.
- If a page cannot be fetched, write that down and ask a person to open it.

Numbers from memory may be out of date. Example: an app store that raises its required system version every year.

## From notes to budgets

1. Put each measure in a row and each target in a column.
2. Take the strictest limit as the project budget, with its source. A budget for each target is the alternative.
3. Say what the measure counts. Example: "Initial download" may mean everything until the first gameplay event, or the whole build when no service is integrated.
4. Take reference screen sizes from the hosts' frame sizes, and add one portrait phone.
5. Put the numbers in the size gate and the screen gate.

## Conflicts

| Conflict | Do |
|---|---|
| Two targets disagree on a key or control | Choose one that both allow |
| A target forbids something the design requires | Ask the owner: change the design, use an edition, or drop the target |
| A target demands exclusivity or update parity | Record the term and which targets it binds before signing |
| A rule is a guideline | Mark it, and decide once |
| A page is silent | Write the assumption, and test the safer reading |

## Owner actions

Some steps need a person: accounts, identity checks, test groups, contracts, ratings, prices, disclosures, keys. List each with the batch it blocks and its lead time. Example: a store that makes new personal accounts run a closed test with a minimum number of testers for two weeks before production.

## Note template

```markdown
# Platform requirements

Pages change. Read the live page before service code and before a submission.

## [Target]

Read: [date]. Sources: [addresses]

| Constraint | Requirement | Applies to us |
|---|---|---|

### Ads
### Listing
### Silent or unclear
- [Question]. Assumed: [reading].

## Strictest limits
| Measure | Limit | Target | Source |
|---|---|---|---|

## Owner actions
| Action | Needed by | Lead time | Done |
|---|---|---|---|
```
