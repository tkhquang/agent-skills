#!/usr/bin/env python3
"""Small balance calculators for game design. Standard library only.

Subcommands:
  curve      Print a progression or power curve with step size and step ratio.
  pacing     Estimate minutes per level from a cost curve and reward rates.
  cost       Score items from a CSV by weighted attributes and compare with price.
  dominance  Find items that are beaten on every attribute by a cheaper or equal item.
  cycle      Check a who-beats-whom matrix for rock-paper-scissors style balance.
  drop       Show how long players stay empty-handed at a given drop chance.
  dice       Print the probability distribution of a dice expression such as 2d6+1.

Run any subcommand with -h for its options.
"""
import argparse
import csv
import itertools
import math
import sys
from collections import Counter


def fmt(x):
    if abs(x) >= 1000:
        return f"{x:,.0f}"
    if float(x).is_integer():
        return f"{x:.0f}"
    return f"{x:.2f}"


def table(headers, rows):
    cells = [[str(h) for h in headers]] + [[str(c) for c in r] for r in rows]
    widths = [max(len(r[i]) for r in cells) for i in range(len(headers))]
    for n, r in enumerate(cells):
        print("  ".join(c.ljust(widths[i]) if not headers[i] else c.rjust(widths[i])
                        for i, c in enumerate(r)).rstrip())
        if n == 0:
            print("  ".join("-" * w for w in widths))


def parse_range(text):
    """'50-200' -> (50.0, 200.0); '120' -> (120.0, 120.0)"""
    if "-" in text[1:]:
        lo, hi = text.split("-", 1) if not text.startswith("-") else text.rsplit("-", 1)
        return float(lo), float(hi)
    return float(text), float(text)


def curve_values(args, rounded=True):
    levels = range(args.start, args.start + args.levels)
    kind = args.type
    if kind == "linear":
        vals = [args.a * x + args.b for x in levels]
    elif kind == "poly":
        vals = [args.a * (x ** args.power) + args.b for x in levels]
    elif kind == "exp":
        vals = [args.base * (args.rate ** x) + args.b for x in levels]
    elif kind == "logistic":
        vals = [args.max / (1 + math.exp(-args.k * (x - args.mid))) for x in levels]
    elif kind == "piecewise":
        pts = sorted((float(p.split(":")[0]), float(p.split(":")[1])) for p in args.points.split(","))
        vals = []
        for x in levels:
            if x <= pts[0][0]:
                vals.append(pts[0][1])
            elif x >= pts[-1][0]:
                vals.append(pts[-1][1])
            else:
                for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
                    if x0 <= x <= x1:
                        vals.append(y0 + (y1 - y0) * (x - x0) / (x1 - x0))
                        break
    else:
        raise SystemExit(f"Unknown curve type: {kind}")
    if rounded and args.round:
        vals = [round(v / args.round) * args.round for v in vals]
    return list(levels), vals


def cmd_curve(args):
    levels, vals = curve_values(args)
    rows, total = [], 0.0
    for i, (lv, v) in enumerate(zip(levels, vals)):
        total += v
        if i == 0:
            rows.append([lv, fmt(v), "", "", fmt(total)])
        else:
            prev = vals[i - 1]
            ratio = f"{v / prev:.3f}" if prev else "n/a"
            rows.append([lv, fmt(v), fmt(v - prev), ratio, fmt(total)])
    table(["Level", "Value", "Step", "Ratio", "Cumulative"], rows)
    # Judge the shape on the unrounded curve. Rounding to round numbers makes the ratios jitter.
    _, raw = curve_values(args, rounded=False)
    ratios = [raw[i] / raw[i - 1] for i in range(1, len(raw)) if raw[i - 1]]
    if ratios:
        print(f"\nStep ratio: first {ratios[0]:.3f}, last {ratios[-1]:.3f}.", end=" ")
        if ratios[-1] < 1.02 and ratios[0] > 1.05:
            print("The curve flattens: late steps add almost nothing relative to the total, "
                  "so late rewards will feel small.")
        elif min(ratios) > 1.0 and max(ratios) - min(ratios) < 0.02:
            print("Constant ratio: every step feels about equally large relative to what the "
                  "player has. Check that top values stay readable.")
        else:
            print()


def span(lo, hi):
    return fmt(lo) if fmt(lo) == fmt(hi) else f"{fmt(lo)}-{fmt(hi)}"


# Above this many successes the exact sum below gets slow, and the normal
# approximation to the negative binomial is accurate to well under one percent.
EXACT_SUCCESS_LIMIT = 2000
# Standard normal quantiles for the player shares the tool reports.
Z_SCORE = {0.5: 0.0, 0.9: 1.2816, 0.99: 2.3263}


def attempts_for(successes, p, share):
    """Smallest number of attempts by which `share` of players have `successes` successes."""
    if successes <= 0:
        return 0
    if p >= 1:
        return successes
    if successes > EXACT_SUCCESS_LIMIT:
        return math.ceil(successes / p + Z_SCORE[share] * math.sqrt(successes * (1 - p)) / p)
    n, done = successes, 0.0
    log_p, log_q = math.log(p), math.log(1 - p)
    while True:
        done += math.exp(math.lgamma(n) - math.lgamma(successes) - math.lgamma(n - successes + 1)
                         + successes * log_p + (n - successes) * log_q)
        if done >= share:
            return n
        n += 1


def cmd_pacing(args):
    levels, costs = curve_values(args)
    r_lo, r_hi = parse_range(args.reward)
    m_lo, m_hi = parse_range(args.minutes)
    p = args.success
    if not 0 < p <= 1:
        raise SystemExit("--success must be above 0 and at most 1. At 0 the level is never reached.")
    if r_lo <= 0 or r_hi < r_lo:
        raise SystemExit("--reward must be positive, low end first. At 0 the level is never reached.")
    if m_lo <= 0 or m_hi < m_lo:
        raise SystemExit("--minutes must be positive, low end first.")
    if args.reward_rate <= 0:
        raise SystemExit("--reward-rate must be positive.")
    rows, total_lo, total_hi, total_late = [], 0.0, 0.0, 0.0
    for i, (lv, cost) in enumerate(zip(levels, costs)):
        growth = args.reward_rate ** i
        # Successes needed: fewest if every reward is at the top of the range, most at the bottom.
        wins_lo = max(0, math.ceil(cost / (r_hi * growth)))
        wins_hi = max(0, math.ceil(cost / (r_lo * growth)))
        # Each success takes 1/p attempts on average.
        tries_lo, tries_hi = wins_lo / p, wins_hi / p
        t_lo, t_hi = tries_lo * m_lo, tries_hi * m_hi
        t_late = attempts_for(wins_hi, p, 0.9) * m_hi
        total_lo += t_lo
        total_hi += t_hi
        total_late += t_late
        spread = f"{t_hi / t_lo:.1f}x" if t_lo else "n/a"
        rows.append([lv, fmt(cost), span(wins_lo, wins_hi), span(tries_lo, tries_hi),
                     span(t_lo, t_hi), fmt(t_late), spread])
    table(["Level", "Cost", "Successes", "Avg attempts", "Avg minutes", "9 in 10 by", "Spread"], rows)
    print(f"\nTotal: {total_lo / 60:.1f} to {total_hi / 60:.1f} hours on average for {len(levels)} "
          f"{'level' if len(levels) == 1 else 'levels'}. The '9 in 10 by' column sums to {total_late / 60:.1f} hours, an upper guide: "
          "few players are that unlucky on every level.")
    print("Avg attempts is successes needed divided by success chance. The low end assumes every "
          "reward at the top of the range and the fastest attempts, the high end the reverse.")
    if p < 1:
        print("With a success chance below 1 there is no worst case. '9 in 10 by' is the minute by "
              "which 90% of players finish at the low rewards and slow attempts.")
    print("A spread above about 3x means two players have very different experiences of the "
          "same level. Narrow the reward range or tie reward to time spent.")


def read_items(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    except OSError as error:
        raise SystemExit(f"Error: cannot read {path}: {error.strerror}")
    if not rows:
        raise SystemExit(f"Error: {path} has no rows below its header.")
    return rows


def number(row, column, path):
    """Read one numeric cell, with an error that names the file and the column."""
    if column not in row:
        raise SystemExit(f"Error: {path} has no column '{column}'. Its columns: {', '.join(row)}")
    try:
        return float(row[column])
    except (TypeError, ValueError):
        raise SystemExit(f"Error: {path}: '{row[column]}' in column '{column}' is not a number.")


def cmd_cost(args):
    rows = read_items(args.csv)
    weights = {}
    for pair in args.weights.split(","):
        k, sep, v = pair.partition("=")
        try:
            weights[k.strip()] = float(v)
        except ValueError:
            raise SystemExit(f"Error: '{pair}' is not column=weight. Example: damage=1,accuracy=1.5")
    name_col = args.name or list(rows[0].keys())[0]
    scored = []
    for r in rows:
        score = sum(number(r, k, args.csv) * w for k, w in weights.items())
        price = number(r, args.price, args.csv) if args.price and r.get(args.price) not in (None, "") else None
        scored.append((r[name_col], score, price))
    priced = [(s, p) for _, s, p in scored if p is not None and s]
    per_point = (sum(p for _, p in priced) / sum(s for s, _ in priced)) if priced else None
    out = []
    for name, score, price in sorted(scored, key=lambda t: t[1]):
        if price is None or per_point is None:
            out.append([name, fmt(score), "", "", ""])
            continue
        fair = score * per_point
        diff = (price - fair) / fair * 100 if fair else 0
        flag = "Underpriced" if diff < -args.tolerance else "Overpriced" if diff > args.tolerance else "OK"
        out.append([name, fmt(score), fmt(price), fmt(fair), f"{diff:+.0f}% {flag}"])
    table(["Item", "Benefit score", "Price", "Fair price", "Difference"], out)
    scores = [s for _, s, _ in scored]
    if min(scores) > 0:
        print(f"\nBenefit range: strongest is {max(scores) / min(scores):.2f}x the weakest.")
    print("Weights are a hypothesis about how much each attribute helps the core resource. "
          "Change them until the ordering matches what playtests show, then fix outliers.")


def cmd_dominance(args):
    rows = read_items(args.csv)
    name_col = args.name or list(rows[0].keys())[0]
    benefits = [b.strip() for b in args.benefits.split(",")]
    costs = [c.strip() for c in args.costs.split(",")] if args.costs else []
    found = False

    def value(row, column):
        return number(row, column, args.csv)

    for a, b in itertools.permutations(rows, 2):
        ge = all(value(a, k) >= value(b, k) for k in benefits) and all(value(a, k) <= value(b, k) for k in costs)
        gt = any(value(a, k) > value(b, k) for k in benefits) or any(value(a, k) < value(b, k) for k in costs)
        if ge and gt:
            found = True
            print(f"{a[name_col]} dominates {b[name_col]}: at least as good on every benefit, "
                  f"no more expensive, and strictly better somewhere.")
    if not found:
        print("No item is strictly dominated on the listed attributes.")
    else:
        print("\nA dominated item is never the right choice. Give it a niche, lower its cost, "
              "or remove it.")


CELL_CODES = {"W": "W", "WIN": "W", "1": "W", "+": "W",
              "L": "L", "LOSS": "L", "LOSE": "L", "-1": "L",
              "D": "D", "DRAW": "D", "0": "D", "=": "D",
              "": None, "-": None, "?": None}
MIRROR = {"W": "L", "L": "W", "D": "D"}


def cmd_cycle(args):
    with open(args.csv, newline="", encoding="utf-8-sig") as f:
        grid = [row for row in csv.reader(f) if any(c.strip() for c in row)]
    if len(grid) < 2:
        raise SystemExit("Matrix needs a header row and at least one option row.")
    names = [c.strip() for c in grid[0][1:]]
    if len(set(names)) != len(names) or "" in names:
        raise SystemExit("Option names in the first row must be unique and not empty.")
    cells = {}
    for row in grid[1:]:
        a = row[0].strip()
        if a not in names:
            raise SystemExit(f"Row '{a}' is not one of the options in the first row.")
        for b, cell in zip(names, row[1:]):
            code = cell.strip().upper()
            if code not in CELL_CODES:
                raise SystemExit(f"Unknown cell '{cell}' at {a} against {b}. "
                                 "Use W, L, D, or leave it blank for not yet known.")
            if a != b:
                cells[(a, b)] = CELL_CODES[code]
    wins = {n: 0 for n in names}
    losses = {n: 0 for n in names}
    draws = {n: 0 for n in names}
    unknown, conflicts = [], []
    for a, b in itertools.combinations(names, 2):
        ab, ba = cells.get((a, b)), cells.get((b, a))
        if ab is None and ba is None:
            unknown.append(f"{a} against {b}")
            continue
        if ab is not None and ba is not None and ba != MIRROR[ab]:
            conflicts.append(f"{a} against {b} is {ab}, but {b} against {a} is {ba}")
            continue
        result = ab if ab is not None else MIRROR[ba]
        if result == "D":
            draws[a] += 1
            draws[b] += 1
        else:
            winner, loser = (a, b) if result == "W" else (b, a)
            wins[winner] += 1
            losses[loser] += 1
    rows = [[n, wins[n], losses[n], draws[n], wins[n] - losses[n]] for n in names]
    table(["Option", "Beats", "Loses to", "Draws", "Net"], rows)
    print()
    if conflicts:
        print("Contradictory entries, not counted: " + "; ".join(conflicts) + ".")
    if unknown:
        shown = "; ".join(unknown[:6]) + ("; ..." if len(unknown) > 6 else "")
        print(f"{len(unknown)} matchup(s) with no result: {shown}.")
    if conflicts or unknown:
        print("No balance verdict until every pair has one consistent result. "
              "A blank cell means not yet known. Mark an even matchup with D.")
        return
    n = len(names)
    decided = sum(wins.values())
    if decided == 0:
        print("Every matchup is a draw. Nothing counters anything, so there is no cycle to check.")
        return
    never_lose = [x for x in names if losses[x] == 0 and wins[x] > 0]
    never_win = [x for x in names if wins[x] == 0 and losses[x] > 0]
    if never_lose:
        print("Dominant (never loses): " + ", ".join(never_lose))
    if never_win:
        print("Dominated (never wins): " + ", ".join(never_win))
    if all(wins[x] == losses[x] for x in names):
        if any(draws.values()):
            print("Balanced: every option beats as many as it loses to, with draws making up "
                  "the remaining matchups. Check that the drawn matchups are fun to play.")
        else:
            print("Balanced cycle: every option beats as many as it loses to.")
    else:
        if n % 2 == 0 and not any(draws.values()):
            print(f"{n} options with a winner in every matchup: each plays {n - 1} matchups, an odd "
                  "number, so equal wins and losses is impossible. Make one matchup per option "
                  "even, or use an odd number of options.")
        if not never_lose and not never_win:
            print("No dominant option, but wins and losses are uneven. Options with positive net "
                  "will be picked more often.")
    print("Counts treat every matchup as equally common and equally decisive. "
          "Check pick rates and win margins before calling it done.")


def parse_chance(text):
    """'1%' -> 0.01; '0.01' -> 0.01; '1/100' -> 0.01"""
    text = text.strip()
    if text.endswith("%"):
        value = float(text[:-1]) / 100
    elif "/" in text:
        top, bottom = text.split("/", 1)
        value = float(top) / float(bottom)
    else:
        value = float(text)
    if not 0 < value <= 1:
        raise SystemExit("--rate must be above 0 and at most 1 (or 100%).")
    return value


def cmd_drop(args):
    p = parse_chance(args.rate)
    pity = args.pity
    if pity is not None and pity < 1:
        raise SystemExit("--pity must be 1 or more.")

    def still_dry(n):
        """Share of players with no drop after n tries."""
        if pity is not None and n >= pity:
            return 0.0
        return (1 - p) ** n

    def tries_until(share):
        """Smallest number of tries by which `share` of players have the drop."""
        n = 1 if p >= 1 else max(1, math.ceil(math.log(1 - share) / math.log(1 - p) - 1e-9))
        return min(n, pity) if pity is not None else n

    if pity is None:
        mean = 1 / p
    else:
        mean = (1 - (1 - p) ** pity) / p
    per_try = args.minutes
    rows = []
    for label, share in (("Half of players", 0.5), ("9 in 10", 0.9), ("99 in 100", 0.99)):
        n = tries_until(share)
        rows.append([label, n, fmt(n * per_try) if per_try else ""])
    headers = ["Have it by", "Tries"] + (["Minutes"] if per_try else [])
    table(headers, [r[:len(headers)] for r in rows])
    print(f"\nChance per try {p * 100:.4g}%. Average tries to the first drop: {fmt(mean)}"
          + (f" ({fmt(mean * per_try)} minutes)." if per_try else "."))
    if pity is None:
        print(f"After {fmt(mean)} tries, the 'expected' number, "
              f"{still_dry(round(mean)) * 100:.1f}% of players still have nothing. "
              "There is no worst case without a guarantee.")
    else:
        print(f"Guaranteed on try {pity}. {(1 - p) ** (pity - 1) * 100:.1f}% of players get it "
              "from the guarantee and not from luck.")
    if args.tries:
        print(f"After {args.tries} tries: {still_dry(args.tries) * 100:.1f}% of players have nothing, "
              f"{(1 - still_dry(args.tries)) * 100:.1f}% have at least one.")
    print("Assumes every try is independent with the same chance. A rising chance after each miss, "
          "or draws from a fixed pool without replacement, shorten the dry streaks further.")



def cmd_dice(args):
    expr = args.expr.lower().replace(" ", "")
    mod = 0
    for sign in ("+", "-"):
        if sign in expr[1:]:
            expr, m = expr.rsplit(sign, 1)
            mod = int(m) if sign == "+" else -int(m)
            break
    count, faces = expr.split("d")
    count, faces = int(count or 1), int(faces)
    dist = Counter({0: 1})
    for _ in range(count):
        nxt = Counter()
        for total, ways in dist.items():
            for face in range(1, faces + 1):
                nxt[total + face] += ways
        dist = nxt
    total_ways = faces ** count
    mean = sum((t + mod) * w for t, w in dist.items()) / total_ways
    rows, cum = [], 0.0
    for t in sorted(dist):
        p = dist[t] / total_ways * 100
        cum += p
        rows.append([t + mod, f"{p:.2f}%", f"{100 - cum + p:.2f}%", "#" * max(1, round(p))])
    table(["Result", "Chance", "This or higher", ""], rows)
    print(f"\nMean {mean:.2f}. One die is flat. More dice pull results toward the middle, "
          "which makes outcomes more predictable.")


def add_curve_args(p):
    p.add_argument("--type", choices=["linear", "poly", "exp", "logistic", "piecewise"], default="exp")
    p.add_argument("--levels", type=int, default=20, help="How many levels to print")
    p.add_argument("--start", type=int, default=1, help="First level number")
    p.add_argument("--a", type=float, default=1.0, help="Multiplier for linear and poly")
    p.add_argument("--b", type=float, default=0.0, help="Constant added to linear, poly and exp")
    p.add_argument("--power", type=float, default=2.0, help="Exponent for poly")
    p.add_argument("--base", type=float, default=100.0, help="Starting scale for exp")
    p.add_argument("--rate", type=float, default=1.4, help="Growth per level for exp")
    p.add_argument("--max", type=float, default=100.0, help="Ceiling for logistic")
    p.add_argument("--k", type=float, default=0.5, help="Steepness for logistic")
    p.add_argument("--mid", type=float, default=10.0, help="Midpoint level for logistic")
    p.add_argument("--points", default="1:2,10:20,20:100", help="Piecewise points as level:value,...")
    p.add_argument("--round", type=float, default=0, help="Round values to a multiple of this")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("curve", help="Print a curve")
    add_curve_args(p)
    p.set_defaults(fn=cmd_curve)

    p = sub.add_parser("pacing", help="Minutes per level from a cost curve")
    add_curve_args(p)
    p.add_argument("--reward", required=True, help="Points per successful action. Example: 50-200")
    p.add_argument("--reward-rate", type=float, default=1.0, help="Reward growth per level. Example: 1.3")
    p.add_argument("--success", type=float, default=1.0, help="Chance an action succeeds, 0 to 1")
    p.add_argument("--minutes", required=True, help="Minutes per action. Example: 1-3")
    p.set_defaults(fn=cmd_pacing)

    p = sub.add_parser("cost", help="Weighted benefit score versus price")
    p.add_argument("--csv", required=True)
    p.add_argument("--weights", required=True, help="Example: damage=1,accuracy=1.5,speed=2")
    p.add_argument("--price", help="Name of the price column, if any")
    p.add_argument("--name", help="Name column (default: first column)")
    p.add_argument("--tolerance", type=float, default=15.0, help="Percent off fair price before flagging")
    p.set_defaults(fn=cmd_cost)

    p = sub.add_parser("dominance", help="Find strictly dominated items")
    p.add_argument("--csv", required=True)
    p.add_argument("--benefits", required=True, help="Columns where higher is better")
    p.add_argument("--costs", help="Columns where lower is better")
    p.add_argument("--name", help="Name column (default: first column)")
    p.set_defaults(fn=cmd_dominance)

    p = sub.add_parser("cycle", help="Check a who-beats-whom matrix")
    p.add_argument("--csv", required=True,
                   help="First row and column are option names. Cell W: row beats column. L: row loses. "
                        "D: even matchup. Blank: not yet known. Filling one side of a pair is enough")
    p.set_defaults(fn=cmd_cycle)

    p = sub.add_parser("drop", help="Dry streaks for a random drop")
    p.add_argument("--rate", required=True, help="Chance per try: 0.01, 1%% or 1/100")
    p.add_argument("--tries", type=int, help="Also report the share of players with nothing after this many tries")
    p.add_argument("--pity", type=int, help="Guarantee the drop on this try if it has not dropped yet")
    p.add_argument("--minutes", type=float, default=0, help="Minutes per try, to convert tries into time")
    p.set_defaults(fn=cmd_drop)

    p = sub.add_parser("dice", help="Distribution of NdF+M")
    p.add_argument("expr", help="Example: 2d6, 3d8+2, d20")
    p.set_defaults(fn=cmd_dice)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
