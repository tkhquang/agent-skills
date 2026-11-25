# Rights

Contents: before a file enters, license questions, attribution, generated content, content that may not ship, libraries and fonts, disclosure, package checks.

This is process guidance and not legal advice. Unclear terms go to the owner.

## Before a file enters

1. Open the license itself. A store badge or a search result is not the license.
2. Write down page, author, license with version, date read. Save the license file beside the asset.
3. Check it against how the game is sold and where, including restricted content and advertising.
4. Add the manifest entry and the notice in the same change.

An item without a license that allows the planned release does not enter the repository.

## License questions

| Question | If yes |
|---|---|
| Must the author be credited? | Add the notice, and show it where the terms ask |
| Are commercial use, ads or adult content excluded? | Do not use |
| Must changes be shared under the same license? | Ask the owner |
| May the source be redistributed? | If not, ship only allowed forms, such as rendered images, and check the package |
| Is use as input to generators excluded? | Keep the files and images of them away from such services |
| Is it limited by seats, projects, revenue or time? | Record the limit and the renewal date |
| Does the license cover trailers and store images? | Record it |

## Attribution

Creative Commons recommends title, author, source and license for each work, with links where possible. Add what you changed.

```text
"Title" by Author, https://example.com/work, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/
Changed: Resized and recolored. Used for: The hero's hair.
```

- Keep one attribution file. Ship it, and show credits in the game where required.
- Name the files each entry covers and the notice file it needs.
- A credit in the repository does not cover a build that ships the work without it.

## Generated content

Record for each asset: tool, model and version, date, prompt, reference images and who owns them, settings, edits made by people, plan or license terms, who confirmed commercial use.

- Use only references the project may use for that purpose.
- Say which parts ship: a generated mesh under hand-made materials is different from a shipped image.
- Decide once, with the owner, what may be generated: characters, backgrounds, text, voice, key art. Write it in the art direction.
- Check the result for near copies of known works, logos and signatures.

## Content that may not ship

Some licenses let you render from an asset and forbid shipping its mesh, texture or source.

- Keep such files outside the repository, or in an ignored folder.
- Exclude that folder in the export settings.
- Search every package for its path and file names. Delete the package on a hit.
- Plan for builds without it. The game must run with a substitute.

## Libraries and fonts

- Pin exact versions. Install from the lock file.
- Compare notices with the lock file in a test: name, version, license.
- A library can embed other libraries. Search its source for copyright lines and name those holders. Minifiers remove unmarked copyright comments.
- For fonts, keep the license, note subsetting and conversion, and check the license allows it.
- Vendored tools and agent skills need their licenses as well.

## Disclosure

Stores ask about generated content. Example: Steam's content survey asks for content made with AI tools that ships with the game, and separately for content generated while the game runs. It leaves out development efficiency tools.

- Build the answer from the manifest: every entry of kind `generated`, plus code and text if the store asks.
- Keep the wording with the listing text, approved by the owner.
- Read the store's page again before each submission.
- Update it when a new kind of generated content enters.

## Package checks

- Every shipped font, library and credited asset has its notice in the package.
- Notices named in the attribution file exist in the package.
- No restricted source is inside.
- The manifest has no placeholder and no empty license.
