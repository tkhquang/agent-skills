---
name: game-release-targets
description: Ships one game codebase to several stores, portals, platforms and editions. Covers dated requirement notes, strictest-limit budgets, a target table that drives builds, a platform adapter that never blocks play (ads, consent, cloud saves), checks on each packaged build, content editions such as adult and all-ages or demo and full, listings and signing. Use when the user prepares a release, submission or store page, ports a game to another portal, store or device, integrates a platform SDK, ads or rewarded video, splits editions or a demo, wraps a web game as a mobile app, or asks why a build was rejected, is too large, leaks debug code or content, or breaks when the SDK fails.
license: MIT
---

# Game release targets

Each target is a platform, store, portal or edition with its own rules. Keep one game and one list of targets. Let the list drive the build, the checks and the packages. The game runs without any platform service.

## Workflow

1. List the targets. For each, read the live requirement pages and write a dated note. See `references/requirements-notes.md`.
2. Settle conflicts between targets and the design before building. A hard platform requirement that conflicts with a design rule goes to the owner.
3. Derive budgets and reference screen sizes from the notes.
4. Write the target table in code: name, service, allowed external addresses, how it ships, content included.
5. Put every platform call behind one adapter. Write the mock first. See `references/platform-adapter.md`.
6. Build each target by name. A build with no target name fails.
7. Check the packaged result of each target. See `references/packaging-checks.md`.
8. If builds differ in content, split by folder and allow list. See `references/editions.md`.
9. Keep listing text, image sizes and upload steps as data beside the code, and check them.
10. Before submitting, read the live pages again and update the dates.

## What differs between targets

| Area | Ask |
|---|---|
| Service | Script or library, start order, events, environments where calls throw |
| Ads and purchases | Allowed kinds, break points, frequency, who reports failure, states when disabled |
| Saves | Platform storage, guest play, merge with local saves |
| Network | Any external request allowed? Fonts, analytics, links |
| Input and layout | Touch, keyboard keys the host uses, orientation, safe areas, host overlays |
| Audio | Start only after a user action, mute requests, interruptions |
| Size | Download before play, total, file count, largest file, archive |
| Content | Rating, restricted content, originality, generated-content rules and disclosure |
| Privacy | Consent, age group, permissions, policy page |
| Identity | Application identifier, version rules, signing key, store account |
| Listing | Title, text limits, tags, image and video sizes, what images may contain |
| Process | Review steps, test periods, updates, exclusivity terms |

## Flag, adapter or separate app

| Difference | Use |
|---|---|
| A number or a text | Target config |
| Platform calls | A driver behind the adapter, picked at build time |
| An optional capability, such as native back button | A service module that only that target's build contains |
| Content that must not ship elsewhere | An edition: separate folder, allow list, search of the package |
| Different session shape or server, such as a daily game inside a social site | A separate app that imports the rules core |

A separate app that imports the core needs its own lock file, tests and build. It also needs its gates listed, because a change in the shared core can break it and the main gates will not see it.

## Rules

- The release that a person plays is the packaged build and not the development server.
- A failed, slow or missing service never blocks play.
- A build contains only its own service code and content. Remove the rest at build time.
- A button with no effect is a defect. Hide or disable what a target cannot do.
- Test identifiers, such as ad test units, never reach a release. Release identifiers never reach a debug build.
- Signing keys and passwords stay outside the repository and the logs.
- Design for the strictest target, then relax with a reason.

## Quick diagnosis

| Symptom | Check |
|---|---|
| Works locally, blank on the host | Absolute paths, letter case of file names, missing start file at the archive root |
| Rejected for external requests | Fonts, analytics or libraries loaded at run time |
| Stuck on loading with an ad blocker or offline | Start waits for the service with no time limit |
| Sound missing after an ad, or stuck muted | Late ad start after the break timed out, or audio resumed outside a user action |
| Reward not granted, or granted twice | Time limit, late result, repeated event |
| Progress lost on the platform only | Platform storage not ready, no merge, write after a failed read |
| Debug tools in the release | Wrong build mode, no package search |
| Restricted content found in the clean edition | Compiled files, caches, names in strings. Search unpacked files |
| Upload refused | Version number not higher, signing, archive format, text or image limits |
| Old save breaks in one edition | Save made in content the edition lacks |

## Submission folder

Produce one folder for each target with a single command:

- The package, named by target and version.
- Listing images and videos at the required sizes.
- Listing text, one field for each form field.
- Upload steps, including owner-only steps such as ratings, prices and disclosures.
- The check results.

The owner uploads. An agent does not submit, publish or accept terms without an explicit instruction.

## Output formats

- Target plan: a table of target, service, budgets, content, missing owner actions, risks.
- Release report: target, package name, size against budgets, checks passed, played on, not run, page dates.

## References

- `references/requirements-notes.md`: dated notes, strictest limits, conflicts, owner actions.
- `references/platform-adapter.md`: adapter interface, failure rules, ads, consent, saves, mute, the mock.
- `references/packaging-checks.md`: build guards, package searches, archives, mobile wrappers, listings.
- `references/editions.md`: splitting content between builds, guarded entry, leak checks, saves across editions.

## Related skills

`game-quality-gates` for gates and test bridges, `game-programming-patterns` for saves, `game-retention-monetization` for what to sell and ad ethics, `game-asset-pipeline` for rights.
