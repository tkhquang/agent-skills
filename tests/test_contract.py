"""AGENTS.md, README.md and the manifests must agree. Run: python -m unittest discover tests"""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
AGENTS = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
SKILLS = sorted(path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md"))


def table_rows(text, heading):
    """Rows of the first table under a heading, without the header and divider rows."""
    section = text.split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]
    rows = [line for line in section.split("\n") if line.startswith("|")][2:]
    return [[cell.strip() for cell in row.strip("|").split("|")] for row in rows]


class Contract(unittest.TestCase):
    def test_gate_commands_are_in_the_readme(self):
        commands = [row[1].strip("`") for row in table_rows(AGENTS, "Gates")]
        self.assertGreater(len(commands), 0)
        for command in commands:
            self.assertIn(command, README)

    def test_layout_paths_exist(self):
        paths = [row[0].strip("`") for row in table_rows(AGENTS, "Layout")]
        self.assertGreater(len(paths), 0)
        for path in paths:
            real = path.replace("<name>", SKILLS[0])
            # Scratch space is ignored and may be absent. Not every skill has scripts.
            if real.startswith(".drafts") or real.endswith("/scripts/"):
                continue
            self.assertTrue((ROOT / real).exists(), f"AGENTS.md lists {path}, which does not exist")

    def test_readme_lists_every_skill_once(self):
        listed = re.findall(r"\(skills/([a-z0-9-]+)/SKILL\.md\)", README)
        self.assertEqual(sorted(listed), SKILLS)

    def test_plugin_names_agree(self):
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual([entry["name"] for entry in market["plugins"]], [plugin["name"]])
        self.assertIn(f"/plugin install {plugin['name']}@{market['name']}", README)

    def test_every_script_has_a_test(self):
        tests = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "tests").glob("test_*.py"))
        for script in list((ROOT / "skills").glob("*/scripts/*.py")) + list((ROOT / "scripts").glob("*.py")):
            self.assertIn(script.name, tests, f"No test names {script.name}")


if __name__ == "__main__":
    unittest.main()
