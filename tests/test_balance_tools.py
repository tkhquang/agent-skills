"""Tests for the game-balance calculator. Run from the repo root: python -m unittest discover tests"""
import importlib.util
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "skills" / "game-balance" / "scripts" / "balance_tools.py"

spec = importlib.util.spec_from_file_location("balance_tools", SCRIPT)
balance_tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(balance_tools)


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)


def matrix(text):
    handle = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
    handle.write(text)
    handle.close()
    return handle.name


class Pacing(unittest.TestCase):
    def test_whole_successes_and_expected_attempts(self):
        # 101 points at 100 per success needs 2 successes. At 50% that is 4 attempts on average.
        out = run("pacing", "--type", "linear", "--a", "0", "--b", "101", "--levels", "1",
                  "--reward", "100", "--success", "0.5", "--minutes", "1").stdout
        row = out.splitlines()[2].split()
        self.assertEqual(row[2:6], ["2", "4", "4", "7"])

    def test_certain_success_has_no_tail(self):
        out = run("pacing", "--type", "linear", "--a", "0", "--b", "100", "--levels", "1",
                  "--reward", "10", "--minutes", "2").stdout
        self.assertEqual(out.splitlines()[2].split()[2:6], ["10", "10", "20", "20"])

    def test_impossible_inputs_are_rejected(self):
        for flag, value in (("--success", "0"), ("--reward", "0")):
            args = {"--reward": "100", "--success": "0.5", "--minutes": "1"}
            args[flag] = value
            result = run("pacing", "--levels", "1", *[x for pair in args.items() for x in pair])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("never reached", result.stderr)

    def test_attempts_for_matches_negative_binomial(self):
        self.assertEqual(balance_tools.attempts_for(2, 0.5, 0.9), 7)
        self.assertEqual(balance_tools.attempts_for(5, 1.0, 0.9), 5)


class Cycle(unittest.TestCase):
    def test_blank_matrix_gets_no_verdict(self):
        out = run("cycle", "--csv", matrix(",A,B,C\nA,,,\nB,,,\nC,,,\n")).stdout
        self.assertIn("No balance verdict", out)
        self.assertNotIn("Balanced", out)

    def test_one_side_of_each_pair_is_enough(self):
        out = run("cycle", "--csv", matrix(",Rock,Paper,Scissors\nRock,,L,W\nPaper,,,L\nScissors,,,\n")).stdout
        self.assertIn("Balanced cycle", out)

    def test_even_count_balanced_by_draws(self):
        out = run("cycle", "--csv", matrix(",A,B,C,D\nA,,W,D,L\nB,L,,W,D\nC,D,L,,W\nD,W,D,L,\n")).stdout
        self.assertIn("Balanced:", out)
        self.assertNotIn("impossible", out)

    def test_even_count_without_draws_is_flagged(self):
        out = run("cycle", "--csv", matrix(",A,B,C,D\nA,,W,W,L\nB,,,W,L\nC,,,,W\nD,,,,\n")).stdout
        self.assertIn("impossible", out)

    def test_contradiction_is_reported(self):
        out = run("cycle", "--csv", matrix(",A,B,C\nA,,W,W\nB,W,,L\nC,,,\n")).stdout
        self.assertIn("Contradictory", out)

    def test_dominant_option_is_named(self):
        out = run("cycle", "--csv", matrix(",A,B,C\nA,,W,W\nB,,,W\nC,,,\n")).stdout
        self.assertIn("Dominant (never loses): A", out)


class Drop(unittest.TestCase):
    def test_one_percent(self):
        out = run("drop", "--rate", "1%", "--tries", "100").stdout
        for expected in (" 69", "230", "459", "36.6%"):
            self.assertIn(expected, out)

    def test_guarantee_caps_the_tail(self):
        out = run("drop", "--rate", "1/100", "--pity", "150").stdout
        self.assertIn("22.4%", out)
        self.assertNotIn("230", out)


class Items(unittest.TestCase):
    CSV = "name,accuracy,damage,speed,cost\nSword,3,4,2,100\nAxe,2,6,1,120\nDagger,3,4,2,150\n"

    def test_documented_columns_work(self):
        path = matrix(self.CSV)
        cost = run("cost", "--csv", path, "--weights", "damage=1,accuracy=1.5,speed=2", "--price", "cost")
        self.assertEqual(cost.returncode, 0, cost.stderr)
        dominance = run("dominance", "--csv", path, "--benefits", "accuracy,damage,speed", "--costs", "cost")
        self.assertIn("Sword dominates Dagger", dominance.stdout)

    def test_bad_input_gives_a_message_and_no_traceback(self):
        path = matrix(self.CSV)
        cases = (
            (("cost", "--csv", path, "--weights", "attack=1"), "has no column 'attack'"),
            (("cost", "--csv", path, "--weights", "name=1"), "is not a number"),
            (("cost", "--csv", path, "--weights", "damage"), "is not column=weight"),
            (("dominance", "--csv", path + ".missing", "--benefits", "damage"), "cannot read"),
        )
        for args, message in cases:
            result = run(*args)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(message, result.stderr)
            self.assertNotIn("Traceback", result.stderr)


class Other(unittest.TestCase):
    def test_dice_mean(self):
        self.assertIn("Mean 7.00", run("dice", "2d6").stdout)

    def test_curve_rounding(self):
        out = run("curve", "--type", "exp", "--base", "1000", "--rate", "1.4", "--levels", "2", "--round", "100").stdout
        self.assertIn("1,400", out)
        self.assertIn("2,000", out)

    def test_rounding_does_not_hide_the_curve_verdict(self):
        out = run("curve", "--type", "exp", "--base", "1000", "--rate", "1.4", "--levels", "30", "--round", "100").stdout
        self.assertIn("Constant ratio", out)

    def test_one_level_is_singular(self):
        out = run("pacing", "--levels", "1", "--reward", "100", "--minutes", "1").stdout
        self.assertIn("for 1 level.", out)


if __name__ == "__main__":
    unittest.main()
