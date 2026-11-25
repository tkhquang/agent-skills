"""Tests for the asset manifest check. Run from the repo root: python -m unittest discover tests"""
import copy
import json
import pathlib
import struct
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "skills" / "game-asset-pipeline" / "scripts" / "check_assets.py"

ENTRY = {
    "id": "Hero",
    "status": "final",
    "files": ["shipped/hero.png"],
    "sizes": {"shipped/hero.png": "4x2"},
    "source": {"kind": "generated", "origin": "sources/hero.blend", "license": "Project-owned", "rebuild": "python build.py hero"},
    "generated": {"tool": "Example", "model": "Example 1", "date": "2026-01-01", "prompt": "A hero"},
    "approval": {"by": "The art lead", "date": "2026-01-02"},
}


class Manifest(unittest.TestCase):
    def check(self, entries, *flags, extra=(), raw=None):
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            (root / "shipped").mkdir()
            (root / "shipped" / "hero.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + struct.pack(">II", 4, 2))
            for name in extra:
                (root / name).write_bytes(b"x")
            (root / "manifest.json").write_text(raw if raw is not None else json.dumps({"assets": entries}), encoding="utf-8")
            command = [sys.executable, str(SCRIPT), str(root / "manifest.json"), "--root", folder, "--shipped", "shipped", *flags]
            return subprocess.run(command, capture_output=True, text=True)

    def changed(self, **values):
        entry = copy.deepcopy(ENTRY)
        entry.update(values)
        return entry

    def test_a_complete_manifest_passes(self):
        out = self.check([ENTRY], "--release")
        self.assertEqual((out.returncode, out.stdout), (0, "Passed. Entries: 1. Shipped files: 1.\n"))

    def test_an_unknown_kind_fails(self):
        source = dict(ENTRY["source"], kind="Generated")
        self.assertIn("source.kind must be one of", self.check([self.changed(source=source)]).stdout)

    def test_path_spellings_and_a_byte_order_mark_are_accepted(self):
        entry = self.changed(files=["./shipped\\hero.png"], sizes={"shipped/hero.png": "4x2"})
        raw = "\ufeff" + json.dumps({"assets": [entry]})
        self.assertEqual(self.check([], raw=raw).returncode, 0)

    def test_a_shipped_folder_outside_the_root_is_refused(self):
        out = self.check([ENTRY], "--shipped", "..")
        self.assertEqual(out.returncode, 2)
        self.assertIn("outside --root", out.stderr)

    def test_a_shipped_file_without_an_entry_fails(self):
        out = self.check([ENTRY], extra=["shipped/new.png"])
        self.assertEqual(out.returncode, 1)
        self.assertIn("shipped/new.png: has no manifest entry", out.stdout)

    def test_an_ignored_file_needs_no_entry(self):
        self.assertEqual(self.check([ENTRY], "--ignore", "*.import", extra=["shipped/hero.png.import"]).returncode, 0)

    def test_each_empty_field_is_named(self):
        for group, field in [("source", "license"), ("source", "rebuild"), ("generated", "prompt"), ("approval", "by")]:
            entry = copy.deepcopy(ENTRY)
            entry[group][field] = " "
            with self.subTest(field=field):
                self.assertIn(f"Hero: {group}.{field} is empty", self.check([entry]).stdout)

    def test_a_placeholder_needs_no_approval_until_release(self):
        entry = self.changed(status="placeholder", approval={})
        self.assertEqual(self.check([entry]).returncode, 0)
        self.assertIn("is a placeholder", self.check([entry], "--release").stdout)

    def test_a_wrong_size_fails(self):
        self.assertIn("is 4x2, not 8x8", self.check([self.changed(sizes={"shipped/hero.png": "8x8"})]).stdout)

    def test_a_listed_file_that_does_not_exist_fails(self):
        out = self.check([self.changed(files=["shipped/hero.png", "shipped/gone.png"])])
        self.assertIn("shipped/gone.png does not exist", out.stdout)

    def test_duplicates_and_a_wrong_form_fail(self):
        self.assertIn("the id is used more than once", self.check([ENTRY, ENTRY]).stdout)
        self.assertIn("files must be a list", self.check([self.changed(files="shipped/hero.png")]).stdout)
        self.assertIn("id is empty", self.check([self.changed(id="")]).stdout)

    def test_unreadable_or_empty_input_exits_with_2(self):
        for raw in ("{", "{}", '{"assets": []}'):
            with self.subTest(raw=raw):
                self.assertEqual(self.check([], raw=raw).returncode, 2)


if __name__ == "__main__":
    unittest.main()
