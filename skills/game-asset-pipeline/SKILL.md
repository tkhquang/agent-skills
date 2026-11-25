---
name: game-asset-pipeline
description: Keeps game art, audio, fonts and generated assets traceable, licensed, reproducible and approved. Covers a manifest with source, license, prompt and approval for every shipped file, scripted exports, a locked art target, contact sheets, placeholders, attribution, generated-content disclosure, licensed sources that may not ship, and consent for paid generation tools. Includes a manifest check script. Use when the user adds, buys, generates or replaces sprites, models, textures, music, sound effects or fonts, asks whether an asset may ship or needs credit, sets up an asset manifest, or reports inconsistent art, lost sources, unlicensed files or placeholder art in a release.
compatibility: The manifest script needs Python 3 and uses only the standard library.
license: MIT
---

# Game asset pipeline

Every shipped file answers these questions: where did it come from, who allows its use, how is it made again, who approved it. Answer them in a manifest that a gate checks. This skill covers records and process. It does not teach drawing or modeling.

## Workflow

1. Create the manifest with the first asset, placeholders included. See `references/manifest.md`.
2. Split folders: sources in one, exports that the game loads in another. The game never loads a source.
3. Write the look down as properties: shape language, palette roles, light, edges, detail. Lock target images at game scale with acceptance criteria. The owner picks them. See `references/production-and-qa.md`.
4. Choose a production path for each family: drawn in code, rendered, generated and cleaned, bought, commissioned. Take the cheapest that meets the target at game scale.
5. Approve one hero asset, then make the family with one camera, light, palette and edge treatment.
6. Export by script. Fix size, anchor, alpha, name, atlas, loudness there.
7. Check files, then look: contact sheet beside the target, then the built game at native size.
8. Record the license and notice before the file enters the repository. See `references/rights.md`.
9. Ask the owner for approval. Only a person fills that field.
10. Run the manifest check in the gate, and with `--release` before shipping.

## The check

```bash
# Every file under the shipped folder needs a complete entry
python scripts/check_assets.py assets-src/manifest.json --shipped public/assets

# Before a release: no placeholders
python scripts/check_assets.py assets-src/manifest.json --shipped game/images --shipped game/audio --release

# Engine side files that need no entry
python scripts/check_assets.py assets-src/manifest.json --shipped assets --ignore "*.import"
```

It fails on a shipped file with no entry, a listed file that does not exist, empty source, license, rebuild, generation or approval fields, a repeated identifier or path, and a PNG of the wrong size.

## Source kinds

| Kind | Record | Watch |
|---|---|---|
| Original | Author, source file, export command | Reference images that were traced |
| Generated | Tool, model, date, prompt, inputs, edits, plan terms | Terms change. Keep the date and who confirmed commercial use |
| Bought | Store, item, license, receipt location | Forbidden uses: redistribution of source, use as input to generators |
| Free license | Page, author, exact license, date read, copy of the license file | Attribution, share-alike, non-commercial, edits to note |
| Commissioned | Artist, contract, scope | Rights in trailers, stores, merchandise |
| Engine or template | Version, license | Template art left in a release |

## Placeholders

- Mark status "placeholder" from the first day. It needs a source and license, not an approval.
- Use shapes or color cards that nobody mistakes for final art.
- A placeholder in a public build is the owner's decision. The release check fails on it.
- "Better than the last version" is not done. Compare with the locked target.

## Paid and metered tools

- Before each paid call: tool, model, price, number of calls. Wait for the owner.
- Set a call budget. Do not exceed it.
- A tool that sends money by default needs a dry run mode. Example: print the request, and send only with an explicit flag.
- If a call fails with no answer, look for the finished job before sending it again.
- Keys live in the environment or an ignored file. Never in the game, logs or commits.
- The shipped game does not call generation services unless the design says so.

## Quick diagnosis

| Symptom | Fix |
|---|---|
| Nobody knows where a file came from | Stop shipping it, or replace it. Add the gate |
| Art looks mixed | Target images, hero first, one rig for the family |
| Looks right in the tool, wrong in the game | Judge at game scale over real backgrounds |
| Cannot make a small change | Rebuild command missing. Recover the source first |
| Same asset differs after a rebuild | Pin tool versions. Compare bytes or pixels after a rebuild |
| Frames jitter or drift | Fixed frame size and anchor in the export, checked by data |
| Missing letters | Compare every string with the font subset |
| A credit is missing at release | Build the notice list from the manifest and the lock file |
| Licensed source found in a package | Exclude the folder and search the package |
| The store asks about generated content | List every entry of kind "generated" |

## Output formats

- Asset plan: family, count, production path, hero, sizes, budget, owner approvals needed.
- Entry: the manifest object, plus the notice text if one is needed.
- Review: per asset, pass or fail for target, scale, technical, rights, with the image looked at.

## References

- `references/manifest.md`: fields, example, rules, approvals, how to adopt it in an old project.
- `references/production-and-qa.md`: target, hero and family, sources and exports, checks for images, audio, fonts and models.
- `references/rights.md`: licenses, attribution, generated content, content that may not ship, disclosure.

## Related skills

`game-quality-gates` for wiring the gate, `game-release-targets` for listings and package searches, `game-feel` for what effects and sound should do.
