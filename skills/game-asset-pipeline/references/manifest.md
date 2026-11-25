# Asset manifest

Contents: example, fields, rules, approvals, agreement with code, adopting it late.

## Example

```json
{
  "assets": [
    {
      "id": "Hero sprites",
      "status": "final",
      "files": ["public/assets/hero.png", "public/assets/hero.json"],
      "sizes": { "public/assets/hero.png": "2048x1024" },
      "use": "Every state of the hero in play",
      "targets": ["All"],
      "source": {
        "kind": "generated",
        "origin": "assets-src/hero/hero.blend, from a generated base mesh",
        "license": "Project-owned. Plan terms allow commercial use, confirmed by the owner on 2026-01-10",
        "rebuild": "python assets-src/build.py hero"
      },
      "generated": {
        "tool": "Example Mesh",
        "model": "example-3",
        "date": "2026-01-09",
        "prompt": "Full prompt, with the reference images and settings"
      },
      "approval": { "by": "The art lead", "date": "2026-01-11" }
    }
  ]
}
```

## Fields

| Field | Required | Holds |
|---|---|---|
| `id` | Always | A stable name |
| `status` | Always | Either `placeholder` or `final` |
| `files` | Always | Every file of the asset, by path |
| `sizes` | Optional | Pixel size for each PNG. The script compares them |
| `source.kind` | Always | One of `original`, `generated`, `bought`, `free-license`, `commissioned`, `engine` |
| `source.origin` | Always | Source file in the repository, or page address with author |
| `source.license` | Always | License name, where the text is, who confirmed it and when |
| `source.notice` | Optional | The notice file that must ship with the asset |
| `source.rebuild` | Always | The command. For an untouched file, "None. The file is the author's release" |
| `generated.*` | Kind is `generated` | Tool, model, date, prompt. Add one record for each step when several tools were used |
| `approval.*` | Status is `final` | Who and when |
| `use`, `targets`, `technical` | Optional | Purpose, editions, anchor, frame count, loudness, color space |

Extra fields are fine. The script ignores them.

## Rules

- One entry for each thing that is approved together, such as an atlas or a sound set.
- Every file the game loads is in exactly one entry. Store images, icons and launcher icons count.
- Record a source that carries a license, such as a bought sound pack, in `source.origin`. List under `files` only files in the repository.
- Change the entry in the same commit as the file. A new file with old approval is wrong, so clear the approval.
- State what a tool did in each step. "Generated" is not enough when a person modeled, traced or painted over it.
- Do not put names of private persons, receipts or keys in the manifest. Say where they are kept.

## Approvals

- Only the owner or a named lead fills `approval`. An agent leaves it empty and lists what waits.
- The approval is for the file as it looks in the built game, not for a preview.
- Any visible change ends the approval.
- A failing gate because of missing approvals is a correct state. Report it and do not work around it.

## Agreement with code

Compare with tests where the same fact lives in code:

| Fact | Compare |
|---|---|
| List of runtime assets | The game's load list equals the shipped folder |
| Frame size, anchor, counts | Atlas data equals the constants the view uses |
| Layer positions | The exporter's record equals the values in scripts |
| Every state | Each state the design lists has frames |
| Fonts and libraries | Notices equal what ships |
| Listing numbers | Store image sizes equal the platform note |

## Adopting it late

1. List all shipped files. Make one entry for each group with what is known.
2. Mark unknown origin as `placeholder`, with "Unknown" in the license. They fail the release check until solved.
3. Find sources in history, tool accounts, stores. Record the date read.
4. Replace what stays unknown.
5. Wire the gate after the list is complete, so that new files cannot slip in.
