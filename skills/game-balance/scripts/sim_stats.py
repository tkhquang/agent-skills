#!/usr/bin/env python3
"""Statistics for balance simulations. Standard library only.

  rate    Interval for a win rate, and whether it is inside a target band
  games   Games needed for a margin, or to detect a difference
  paired  Difference between a baseline and a variant that share seeds

Run a command with --help for its options.
"""
import argparse
import csv
import math
import statistics
import sys


def fail(message):
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(2)


def share(text):
    """Read 0.55 or 55% as a fraction from 0 to 1."""
    try:
        value = float(text[:-1]) / 100 if text.endswith("%") else float(text)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{text}' is not a number or a percentage")
    if not 0 <= value <= 1:
        raise argparse.ArgumentTypeError(f"'{text}' is outside 0 to 1. Write 55 percent as 55% or 0.55")
    return value


def z_for(level):
    return statistics.NormalDist().inv_cdf(0.5 + level / 2)


def wilson(wins, games, level):
    """Wilson score interval."""
    z = z_for(level)
    rate = wins / games
    scale = 1 + z * z / games
    center = (rate + z * z / (2 * games)) / scale
    half = z * math.sqrt(rate * (1 - rate) / games + z * z / (4 * games * games)) / scale
    return max(0.0, center - half), min(1.0, center + half)


def cmd_rate(args):
    if args.games < 1:
        fail("--games must be at least 1")
    if not 0 <= args.wins <= args.games:
        fail("--wins must be from 0 to --games")
    if args.low > args.high:
        fail("--low must not be above --high")
    low, high = wilson(args.wins, args.games, args.level)
    print(f"Rate {args.wins / args.games:.1%} over {args.games} games. {args.level:.0%} interval {low:.1%} to {high:.1%}.")
    if low >= args.low and high <= args.high:
        verdict = "Inside the target"
    elif high < args.low or low > args.high:
        verdict = "Outside the target"
    else:
        verdict = "Undecided. Play more games"
    print(f"Target {args.low:.1%} to {args.high:.1%}: {verdict}.")


def cmd_games(args):
    if (args.margin is None) == (args.diff is None):
        fail("Give exactly one of --margin and --diff")
    z = z_for(args.level)
    if args.margin is not None:
        if args.margin == 0:
            fail("--margin must be above 0")
        games = math.ceil(z * z * args.rate * (1 - args.rate) / args.margin ** 2)
        print(f"{games} independent games give a margin of {args.margin:.1%} at a rate of {args.rate:.0%}.")
        return
    other = args.rate + args.diff
    if args.diff == 0 or other > 1:
        fail("--diff must be above 0, and --rate plus --diff at most 1")
    power = statistics.NormalDist().inv_cdf(args.power)
    spread = args.rate * (1 - args.rate) + other * (1 - other)
    games = math.ceil((z + power) ** 2 * spread / args.diff ** 2)
    print(f"{games} independent games for each version detect {args.rate:.0%} against {other:.0%} in {args.power:.0%} of runs.")
    print("Shared seeds can need fewer. Measure with the paired command.")


def read_pairs(path, key, base, variant):
    """Return the row count and the mean difference of each group of rows with the same key."""
    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as error:
        fail(f"Cannot read {path}: {error.strerror}")
    if not rows:
        fail(f"{path} has no rows below its header")
    for column in (key, base, variant):
        if column not in rows[0]:
            fail(f"{path} has no column '{column}'. Its columns: {', '.join(rows[0])}")
    groups = {}
    for number, row in enumerate(rows, start=2):
        try:
            difference = float(row[variant]) - float(row[base])
        except (TypeError, ValueError):
            fail(f"{path} line {number}: '{base}' and '{variant}' must be numbers")
        groups.setdefault(row[key], []).append(difference)
    return len(rows), [statistics.fmean(values) for values in groups.values()]


def cmd_paired(args):
    rows, means = read_pairs(args.csv, args.key, args.base, args.variant)
    if len(means) < 2:
        fail(f"The column '{args.key}' needs at least two different values")
    change = statistics.fmean(means)
    error = statistics.stdev(means) / math.sqrt(len(means))
    z = z_for(args.level)
    low, high = change - z * error, change + z * error
    print(f"{rows} rows in {len(means)} groups of '{args.key}'.")
    print(f"Change {change:+.3f}. {args.level:.0%} interval {low:+.3f} to {high:+.3f}.")
    if len(means) < 30:
        print("Fewer than 30 groups, so the interval is too narrow.")
    print("No clear change." if low <= 0 <= high else "The change is clear at this level.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    level = argparse.ArgumentParser(add_help=False)
    level.add_argument("--level", type=share, default=0.95, help="Confidence level, default 95%%")

    rate = commands.add_parser("rate", parents=[level], help="Interval for a win rate")
    rate.add_argument("--wins", type=float, required=True, help="Count a game with no result as 0.5, or leave it out of both numbers")
    rate.add_argument("--games", type=int, required=True)
    rate.add_argument("--low", type=share, default=0.4, help="Lowest acceptable rate, default 40%%")
    rate.add_argument("--high", type=share, default=0.6, help="Highest acceptable rate, default 60%%")
    rate.set_defaults(run=cmd_rate)

    games = commands.add_parser("games", parents=[level], help="Games needed")
    games.add_argument("--margin", type=share, help="Half the width of the interval, for example 4%%")
    games.add_argument("--diff", type=share, help="Difference to detect, for example 5%%")
    games.add_argument("--rate", type=share, default=0.5, help="Expected rate, default 50%%")
    games.add_argument("--power", type=share, default=0.8, help="Chance to detect the difference, default 80%%")
    games.set_defaults(run=cmd_games)

    paired = commands.add_parser("paired", parents=[level], help="Compare versions that share seeds")
    paired.add_argument("--csv", required=True, help="One row for each game, with the result under each version")
    paired.add_argument("--key", default="seed", help="Column that groups games that depend on each other, default seed")
    paired.add_argument("--base", default="base", help="Column with the baseline result")
    paired.add_argument("--variant", default="variant", help="Column with the variant result")
    paired.set_defaults(run=cmd_paired)

    args = parser.parse_args(argv)
    if not 0 < args.level < 1:
        fail("--level must be between 0 and 1")
    if args.command == "games" and not 0 < args.power < 1:
        fail("--power must be between 0 and 1")
    args.run(args)


if __name__ == "__main__":
    main()
