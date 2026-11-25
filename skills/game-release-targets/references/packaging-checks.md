# Packaging checks

Contents: target table, build guards, the package, play the package, web archives, mobile wrappers, desktop builds, listings.

## Target table

One list in code drives everything. Example:

```js
export const TARGETS = {
  plain:  { service: null,      scripts: [],                          ships: 'zip' },
  portal: { service: 'PortalX', scripts: ['https://example.com/x.js'], ships: 'zip' },
  store:  { service: 'Wrapper', scripts: [],                          ships: 'app' },
};
```

- The build mode must name a target. An unknown or missing name is an error.
- Development and test builds use the mock.
- Tests loop over the table, so a new target is checked from its first build.

## Build guards

| Guard | Fails when |
|---|---|
| Paths | A page or file refers to an absolute path or a host outside the target's list |
| Service present | The target's own service code is missing |
| Service split | Another target's service code is found |
| Test tools | Bridge, mock, cheats, test scenes or debug flags are found |
| Tooling | Generators or editors are in the bundle |
| Identity | Title, icon, version or identifiers are missing or wrong |
| Notices | License and attribution files are missing |
| Settings agree | Permissions, audience switch and service flags disagree |
| Licensed sources | Files that may not be distributed are found |

Search code files for service names, because notice files name them too. Each search needs a positive control: the test build must contain the marker.

## The package

Check the archive after writing it, by reading it back.

- An allow list of paths. An unknown file fails.
- A list of required files. A missing file fails.
- Size, file count, largest file and path length against the target's limits.
- Forward slashes, relative paths, exact letter case. Hosts can be case sensitive when your machine is not.
- The same input gives the same archive: sorted entries and fixed dates. A changed hash then means changed content.
- One package for each target. Fail on none or several.
- A package older than any source is rebuilt.

## Play the package

Extract it to a clean folder, start it, draw the first screen, and complete the smallest full loop. Then check the log. Where bots exist, let them play a whole game. Run editions and targets separately.

## Web archives

| Check | Why |
|---|---|
| Start page at the root | Hosts require it |
| Relative paths only | Games are served from a sub-folder |
| No external requests beyond the target's list | Portals block them |
| Storage optional | Private windows restrict it |
| Text selection and scroll disabled in the game area | A long press or arrow key otherwise acts on the host page |
| Refresh rates above 60 Hz | Speed must not change |

## Mobile wrappers

- One command builds the game, copies it into the native project, and builds debug and release.
- List every hand change to generated native files. Do not edit files that the tool regenerates.
- The version code only goes up and stays under the store's maximum. Example: one store refuses values above 2,100,000,000, so seconds since 1970 fit and a date stamp does not.
- Debug uses test ad identifiers. Release refuses to build without real ones, all from one account.
- Read the key and passwords from the environment. A partial set is an error. Resolve the key path once, because tools may start in different folders.
- Check permissions in the merged manifest. A removal line can be ignored in the merge.
- Handle back button, background, resume, safe areas, rotation.
- Smoke test on a device or emulator and say which.

## Desktop builds

- Verify the export templates or toolchain version before building.
- Exclude source and licensed folders in the export settings, and search the pack for their names.
- The program may stay locked for a moment after it closes. Retry the archive step, then read the archive back.

## Listings

Keep text and upload steps as data for each target. Check:

- Every target has an entry with the required fields.
- Text limits, tag counts, capital letters, banned words.
- Image and video files exist with exact sizes and formats. No cursor, borders or text where the platform forbids them.
- Numbers in the text match the game, such as the level count.
- Screenshots come from the built game, and one command makes them again after a visual change.
- Disclosures, such as generated content, match the asset manifest.
