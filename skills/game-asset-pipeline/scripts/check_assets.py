#!/usr/bin/env python3
"""Check an asset manifest against the files that the game ships. Standard library only.

  python check_assets.py assets/manifest.json --shipped public/assets
  python check_assets.py assets/manifest.json --shipped game/images --release

Paths in the manifest are relative to --root (default: the current folder).
Exits with 1 when a check fails, and with 2 when the input cannot be read.
"""
import argparse
import json
import pathlib
import struct
import sys

SOURCE_FIELDS = ("kind", "origin", "license", "rebuild")
GENERATED_FIELDS = ("tool", "model", "date", "prompt")
APPROVAL_FIELDS = ("by", "date")
STATUSES = ("placeholder", "final")
KINDS = ("original", "generated", "bought", "free-license", "commissioned", "engine")


def stop(message):
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(2)


def filled(value):
    return isinstance(value, str) and value.strip() != ""


def png_size(path):
    with path.open("rb") as handle:
        head = handle.read(24)
    if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return "{}x{}".format(*struct.unpack(">II", head[16:24]))


def missing(entry, group, fields):
    values = entry.get(group)
    values = values if isinstance(values, dict) else {}
    return [f"{group}.{field} is empty" for field in fields if not filled(values.get(field))]


def tidy(name):
    """Spell a path one way: forward slashes and no leading dot folder."""
    return pathlib.PurePosixPath(name.replace("\\", "/")).as_posix()


def names_of(entry):
    """Return the files of an entry, or an empty list when the value has the wrong form."""
    files = entry.get("files")
    return [tidy(name) for name in files] if isinstance(files, list) and all(filled(name) for name in files) else []


def check_entry(entry, root, release):
    """Return the problems of one manifest entry."""
    problems = []
    status = entry.get("status")
    if status not in STATUSES:
        problems.append(f"status must be one of: {', '.join(STATUSES)}")
    if release and status == "placeholder":
        problems.append("is a placeholder, and --release accepts none")
    problems += missing(entry, "source", SOURCE_FIELDS)
    source = entry.get("source")
    if isinstance(source, dict) and filled(source.get("kind")) and source["kind"] not in KINDS:
        problems.append("source.kind must be one of: " + ", ".join(KINDS))
    if isinstance(source, dict) and source.get("kind") == "generated":
        problems += missing(entry, "generated", GENERATED_FIELDS)
    if status != "placeholder":
        problems += missing(entry, "approval", APPROVAL_FIELDS)
    files = names_of(entry)
    if not files:
        return problems + ["files must be a list with at least one path"]
    sizes = entry.get("sizes") if isinstance(entry.get("sizes"), dict) else {}
    sizes = {tidy(name): expected for name, expected in sizes.items() if filled(name)}
    for name in files:
        if not (root / name).is_file():
            problems.append(f"{name} does not exist")
    for name, expected in sizes.items():
        if name not in files:
            problems.append(f"sizes names {name}, which is not in files")
        elif (root / name).is_file():
            found = png_size(root / name)
            if found is None:
                problems.append(f"{name} is not a PNG, so its size cannot be checked")
            elif found != expected:
                problems.append(f"{name} is {found}, not {expected}")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("manifest")
    parser.add_argument("--shipped", action="append", required=True, help="Folder that the game loads. Every file in it needs an entry. May repeat")
    parser.add_argument("--root", default=".", help="Folder that manifest paths start from")
    parser.add_argument("--ignore", action="append", default=[], help="File name pattern to skip in shipped folders, for example *.import. May repeat")
    parser.add_argument("--release", action="store_true", help="Fail on placeholders")
    args = parser.parse_args(argv)

    root = pathlib.Path(args.root).resolve()
    try:
        data = json.loads(pathlib.Path(args.manifest).read_text(encoding="utf-8-sig"))
    except OSError as error:
        stop(f"Cannot read {args.manifest}: {error.strerror}")
    except ValueError as error:
        stop(f"{args.manifest} is not valid JSON in UTF-8: {error}")
    entries = data.get("assets") if isinstance(data, dict) else None
    if not isinstance(entries, list) or not all(isinstance(entry, dict) for entry in entries):
        stop(f"{args.manifest} needs a list of objects under the key assets")
    if not entries:
        stop(f"{args.manifest} lists no asset, so the check proves nothing")

    failures, owners, ids = [], {}, set()
    for entry in entries:
        label = entry["id"] if filled(entry.get("id")) else None
        if label is None:
            label = "An entry without an id"
            failures.append(f"{label}: id is empty")
        elif label in ids:
            failures.append(f"{label}: the id is used more than once")
        ids.add(label)
        failures += [f"{label}: {problem}" for problem in check_entry(entry, root, args.release)]
        for name in names_of(entry):
            if name in owners:
                failures.append(f"{label}: {name} is also in {owners[name]}")
            owners.setdefault(name, label)

    shipped = set()
    for folder in args.shipped:
        base = (root / folder).resolve()
        if not base.is_dir():
            stop(f"The shipped folder {folder} does not exist")
        if base != root and root not in base.parents:
            stop(f"The shipped folder {folder} is outside --root")
        for path in base.rglob("*"):
            if path.is_file() and not any(path.match(pattern) for pattern in args.ignore):
                shipped.add(path.relative_to(root).as_posix())
    if not shipped:
        stop("The shipped folders hold no file, so the check proves nothing")
    failures += [f"{name}: has no manifest entry" for name in sorted(shipped - set(owners))]

    for failure in failures:
        print(f"FAIL {failure}")
    if failures:
        print(f"Problems: {len(failures)}")
        return 1
    print(f"Passed. Entries: {len(entries)}. Shipped files: {len(shipped)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
