"""The validator must fail on each rule it claims to enforce. Run: python -m unittest discover tests"""
import contextlib
import importlib.util
import io
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_skills", ROOT / "scripts" / "validate_skills.py")
validate_skills = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_skills)

GOOD_SKILL = """---
name: demo-skill
description: Does a thing. Use when the user asks for the thing.
license: MIT
---

# Demo

Short intro.

- Read `references/notes.md` for detail.
"""
GOOD_REFERENCE = "# Notes\n\nContents: one topic.\n\n## One topic\n\n| Case | Do |\n|---|---|\n| A | B |\n"


def problems(skill_text=GOOD_SKILL, reference_text=GOOD_REFERENCE, folder="demo-skill"):
    """Write one skill into a temporary tree and return what the validator reports for it."""
    with tempfile.TemporaryDirectory() as tmp:
        skill = pathlib.Path(tmp) / "skills" / folder
        (skill / "references").mkdir(parents=True)
        (skill / "SKILL.md").write_bytes(skill_text.encode("utf-8"))
        (skill / "references" / "notes.md").write_bytes(reference_text.encode("utf-8"))
        return validate_skills.check(skill)


class Validator(unittest.TestCase):
    def assertFlags(self, found, expected):
        self.assertTrue(any(expected in problem for problem in found), f"Expected '{expected}' in {found}")

    def test_good_skill_passes(self):
        self.assertEqual(problems(), [])

    def test_real_skills_pass(self):
        report = io.StringIO()
        with contextlib.redirect_stdout(report):
            status = validate_skills.main([str(ROOT)])
        self.assertEqual(status, 0, report.getvalue())

    def test_name_must_match_folder(self):
        self.assertFlags(problems(folder="other-name"), "does not match directory")

    def test_description_limit(self):
        long_text = GOOD_SKILL.replace("Does a thing.", "Does a thing. " + "word " * 300)
        self.assertFlags(problems(long_text), "description is")

    def test_license_required(self):
        self.assertFlags(problems(GOOD_SKILL.replace("license: MIT\n", "")), "no license")

    def test_unlinked_reference(self):
        self.assertFlags(problems(GOOD_SKILL.replace("`references/notes.md`", "the notes")), "never mentioned")

    def test_missing_reference(self):
        self.assertFlags(problems(GOOD_SKILL + "- See `references/gone.md`.\n"), "does not exist")

    def test_dash(self):
        self.assertFlags(problems(reference_text=GOOD_REFERENCE + "\nA line — with a dash.\n"), "em or en dash")

    def test_crlf(self):
        self.assertFlags(problems(reference_text=GOOD_REFERENCE.replace("\n", "\r\n")), "CRLF")

    def test_long_paragraph(self):
        self.assertFlags(problems(reference_text=GOOD_REFERENCE + "\n" + "Word " * 61 + "\n"), "Split it")

    def test_long_paragraph_inside_code_is_ignored(self):
        fenced = GOOD_REFERENCE + "\n```text\n" + "word " * 80 + "\n```\n"
        self.assertEqual(problems(reference_text=fenced), [])

    def test_lowercase_starts(self):
        self.assertFlags(problems(reference_text=GOOD_REFERENCE + "\n- lowercase bullet\n"), "starts in lowercase")
        self.assertFlags(problems(reference_text=GOOD_REFERENCE.replace("| A | B |", "| A | b |")), "table cell")

    def test_numbered_and_counted_headings(self):
        self.assertFlags(problems(reference_text=GOOD_REFERENCE + "\n## 1. First\n"), "numbered heading")
        self.assertFlags(problems(reference_text=GOOD_REFERENCE + "\n## The three rules\n"), "count in a heading")
        self.assertFlags(problems(reference_text=GOOD_REFERENCE.replace("| Case |", "| # |")), "numbered table column")

    def test_reference_needs_title_and_contents(self):
        self.assertFlags(problems(reference_text="# Notes\n\nNo list of sections.\n"), "no 'Contents:' line")
        self.assertFlags(problems(reference_text="Contents: none.\n"), "does not start with a title")


if __name__ == "__main__":
    unittest.main()
