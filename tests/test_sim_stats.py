"""Tests for the simulation statistics. Run from the repo root: python -m unittest discover tests"""
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "skills" / "game-balance" / "scripts" / "sim_stats.py"


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)


class Rate(unittest.TestCase):
    def test_interval_matches_the_wilson_formula(self):
        # The Wilson interval of 5 in 10 at 95% is 23.7% to 76.3%.
        self.assertIn("23.7% to 76.3%", run("rate", "--wins", "5", "--games", "10").stdout)

    def test_verdicts(self):
        self.assertIn("Inside", run("rate", "--wins", "300", "--games", "600").stdout)
        self.assertIn("Outside", run("rate", "--wins", "540", "--games", "600").stdout)
        self.assertIn("Undecided", run("rate", "--wins", "35", "--games", "60").stdout)

    def test_bad_input_is_explained(self):
        out = run("rate", "--wins", "11", "--games", "10")
        self.assertEqual(out.returncode, 2)
        self.assertIn("--wins must be", out.stderr)


class Games(unittest.TestCase):
    def test_margin(self):
        # 1.96^2 * 0.25 / 0.04^2 = 600.2
        self.assertIn("601 independent games", run("games", "--margin", "4%").stdout)

    def test_difference_needs_more_games_than_a_margin(self):
        out = run("games", "--diff", "5%").stdout
        self.assertGreater(int(out.split()[0]), 1500)

    def test_exactly_one_question(self):
        self.assertEqual(run("games").returncode, 2)
        self.assertEqual(run("games", "--margin", "4%", "--diff", "5%").returncode, 2)


class Paired(unittest.TestCase):
    def csv(self, rows):
        handle = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
        handle.write("seed,base,variant\n" + "\n".join(rows) + "\n")
        handle.close()
        self.addCleanup(pathlib.Path(handle.name).unlink)
        return handle.name

    def test_clear_change(self):
        rows = [f"{seed},0,{1 if seed % 2 else 0}" for seed in range(60)]
        out = run("paired", "--csv", self.csv(rows)).stdout
        self.assertIn("Change +0.500", out)
        self.assertIn("clear at this level", out)

    def test_no_change(self):
        rows = [f"{seed},{seed % 2},{(seed + 1) % 2}" for seed in range(60)]
        self.assertIn("No clear change", run("paired", "--csv", self.csv(rows)).stdout)

    def test_rows_of_one_seed_count_as_one_group(self):
        rows = [f"{seed},0,1" if seed % 3 else f"{seed},1,0" for seed in range(40) for _ in range(4)]
        self.assertIn("160 rows in 40 groups", run("paired", "--csv", self.csv(rows)).stdout)

    def test_missing_column_is_named(self):
        out = run("paired", "--csv", self.csv(["1,0,1", "2,0,1"]), "--base", "old")
        self.assertEqual(out.returncode, 2)
        self.assertIn("no column 'old'", out.stderr)


if __name__ == "__main__":
    unittest.main()
