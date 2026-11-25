#!/usr/bin/env python3
"""Check every skill against the Agent Skills specification and this repository's writing rules.

Run from the repository root: python scripts/validate_skills.py [root]
Exits with status 1 if any check fails. Standard library only.
"""
import pathlib
import re
import sys

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME = 64             # Specification limit.
MAX_DESCRIPTION = 1024    # Specification limit.
MAX_BODY_LINES = 500      # Specification recommendation for SKILL.md.
MAX_PARAGRAPH_WORDS = 60  # Repository rule: no walls of text.
COUNT_WORD = r"(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|eighteen|twenty)"
# A count in a heading or contents line goes stale when an item is added or removed.
COUNTED_TITLE = re.compile(rf"\b{COUNT_WORD}\b", re.I)


def frontmatter(text):
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return None, text
    end = text.index("\n---\n", 4)
    fields = {}
    for line in text[4:end].splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, text[end + 5:]


def prose_lines(text):
    """Yield (line number, line) for lines outside code fences."""
    fenced = False
    for number, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            yield number, line


def style_problems(label, text):
    """Return the writing-rule problems of one markdown file."""
    problems = []
    if "\r" in text:
        problems.append(f"{label} has CRLF line endings")
    if "—" in text or "–" in text:
        problems.append(f"{label} contains an em or en dash")
    if re.search(r"(references|scripts|assets)\\", text):
        problems.append(f"{label} uses a backslash path")
    for number, line in prose_lines(text):
        where = f"{label}:{number}"
        stripped = line.strip()
        if stripped.startswith("|"):
            if re.match(r"^\|\s*#\s*\|", stripped):
                problems.append(f"{where} has a numbered table column")
            for cell in stripped.strip("|").split("|"):
                if re.match(r"\s*[a-z]", cell):
                    problems.append(f"{where} has a table cell that starts in lowercase: '{cell.strip()[:30]}'")
            continue
        heading = re.match(r"^#+\s+(.*)", stripped)
        if heading:
            if re.match(r"\d+[.)]\s", heading.group(1)):
                problems.append(f"{where} is a numbered heading")
            if COUNTED_TITLE.search(heading.group(1)):
                problems.append(f"{where} has a count in a heading")
            if re.match(r"[a-z]", heading.group(1)):
                problems.append(f"{where} is a heading that starts in lowercase")
            continue
        if stripped.startswith("Contents:") and COUNTED_TITLE.search(stripped):
            problems.append(f"{where} has a count in the contents line")
        item = re.match(r"^(?:[-*]|\d+\.)\s+(.*)", stripped)
        body = item.group(1) if item else stripped
        if re.match(r"[a-z]", body):
            problems.append(f"{where} starts in lowercase: '{body[:30]}'")
        words = len(body.split())
        if words > MAX_PARAGRAPH_WORDS:
            problems.append(f"{where} runs to {words} words. Split it, the limit is {MAX_PARAGRAPH_WORDS}")
    return problems


def check(skill):
    errors = []
    text = (skill / "SKILL.md").read_bytes().decode("utf-8")
    fields, body = frontmatter(text.replace("\r\n", "\n"))
    if fields is None:
        return ["SKILL.md has no frontmatter"]

    name = fields.get("name", "")
    if not NAME.match(name) or len(name) > MAX_NAME:
        errors.append(f"name '{name}' must be lowercase letters, digits and single hyphens, at most {MAX_NAME} characters")
    if name != skill.name:
        errors.append(f"name '{name}' does not match directory '{skill.name}'")

    description = fields.get("description", "")
    if not 1 <= len(description) <= MAX_DESCRIPTION:
        errors.append(f"description is {len(description)} characters, allowed 1 to {MAX_DESCRIPTION}")
    if "<" in description or ">" in description:
        errors.append("description contains angle brackets")
    if not fields.get("license"):
        errors.append("frontmatter has no license")

    lines = body.count("\n")
    if lines > MAX_BODY_LINES:
        errors.append(f"SKILL.md body is {lines} lines, keep it under {MAX_BODY_LINES}")

    bundled = [p for sub in ("references", "scripts", "assets") for p in sorted((skill / sub).glob("*")) if p.is_file()]
    for path in bundled:
        if path.name not in body:
            errors.append(f"{path.relative_to(skill).as_posix()} is never mentioned in SKILL.md")
    for mention in re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", body):
        if not (skill / mention).exists():
            errors.append(f"SKILL.md mentions {mention}, which does not exist")
    for mention in re.findall(r"`([a-z0-9-]+\.md)`", body):
        if not (skill / "references" / mention).exists():
            errors.append(f"SKILL.md mentions {mention}, which is not in references/")

    # Blank the frontmatter instead of cutting it, so reported line numbers match the file.
    head_lines = text.replace("\r\n", "\n").count("\n") - body.count("\n")
    errors += style_problems("SKILL.md", "\n" * head_lines + body if "\r" not in text else text)
    for path in bundled:
        if path.suffix != ".md":
            continue
        label = path.relative_to(skill).as_posix()
        content = path.read_bytes().decode("utf-8")
        errors += style_problems(label, content)
        if path.parent.name == "references":
            head = content.split("\n")[:6]
            if not head[0].startswith("# "):
                errors.append(f"{label} does not start with a title")
            if not any(line.startswith("Contents:") for line in head):
                errors.append(f"{label} has no 'Contents:' line near the top")
    return errors


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    root = pathlib.Path(args[0]) if args else pathlib.Path(__file__).resolve().parents[1]
    skills = sorted(p.parent for p in (root / "skills").glob("*/SKILL.md"))
    if not skills:
        print(f"No skills found in {root / 'skills'}")
        return 1
    failed = 0
    for skill in skills:
        errors = check(skill)
        print(f"{'FAIL' if errors else 'ok  '} {skill.name}")
        for error in errors:
            print(f"     {error}")
        failed += bool(errors)
    print(f"\n{len(skills) - failed} of {len(skills)} skills pass.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
