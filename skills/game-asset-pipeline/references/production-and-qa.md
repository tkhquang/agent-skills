# Production and QA

Contents: target, hero and family, sources and exports, checks by type, looking, using critics and generators.

## Target

- Describe the look in properties a person can check: shape, palette roles, light direction, edge treatment, detail at game size. Do not use a living artist or another game as the style.
- Make a few images at game scale over the real background. Write acceptance criteria beside them, such as "Each kind is recognized in grayscale at 48 pixels".
- The owner locks them. Keep them in the repository.
- The target moves only by decision. Never adjust it to match what was produced.

## Hero and family

1. Build one hero asset through the whole path, into the game.
2. Compare with the target. Fix the path, not only the asset.
3. After approval, produce the rest with the same camera, light, palette, outline and export.
4. Review the family together on one sheet, so differences show.

Changing the production path inside a family makes the family inconsistent. Finish or restart it.

## Sources and exports

- The export script is the only way into the shipped folder. A hand step nobody can repeat is a defect.
- Scripts set size, anchor, margin, alpha, name, compression, atlas.
- Constants that both the exporter and the game need live in one place, or a test compares them.
- A rebuild from the same sources gives the same result. Check once for each path.
- Keep large intermediate files and backups out of version control. Keep the sources and the final data.
- Old routes may stay as a record. Say in the document that no new asset comes from them.

## Checks by type

| Type | By script | By eye or ear |
|---|---|---|
| Sprites, atlas | Size, alpha present and used, frame count, margin around frames, power of two where the engine needs it | Silhouette, baseline, drift between frames, light direction |
| Character layers | Same canvas, face position recorded, every expression present | Seams, expression reads at game size |
| Backgrounds | Size, no alpha, safe area for text | Contrast under text and characters |
| Icons, UI | Every size, text is live text | Reads at the smallest size |
| Models | Triangle count, materials, scale, origin, names | Shape from several angles, in plain material and final material |
| Sound effects | Length, channels, peak, loudness, format | Level against others on a phone speaker |
| Music | Loop points, length, loudness | Loop seam, change between tracks |
| Fonts | Glyphs cover every string, weight, file size | Readable at the smallest size |
| Video, trailers | Size, frame rate, length, no sound where required | No cursor, no debug text |

Alpha that is present but fully opaque means a baked background, sometimes a painted checkerboard.

## Looking

- Build a contact sheet for each entry or folder. Open it next to the target.
- View at native size, then in the built game over real backgrounds, in motion.
- For anything with volume, check front, three-quarter, side and an oblique view. A match in one view can break the others.
- For color-coded pieces, check in grayscale.
- Say what was looked at: file, size, build.
- A report script that passes says nothing about quality.

## Using critics and generators

- Generated output is a draft until it passes the checks. Never trust its grid, transparency or size.
- Keep prompts with reference images and settings. Generate in small batches from one approved reference.
- An independent critic, person or model, sees the candidates without knowing which is new.
- A paint-over shows what to change. Do not ship its pixels unless the manifest says so.
- The owner's verdict overrides a measurement or a critic.
- Record each rejected method with its reason, so nobody repeats it under another name.
