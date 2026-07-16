#!/usr/bin/env python3
"""Mirror skill directories from AI-Human-Research-OS into this repository."""

from __future__ import annotations

import argparse
import fnmatch
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE_REPOSITORY = "https://github.com/pengqianhan/AI-Human-Research-OS"
MAPPINGS = (
    ("research-skills-hub/open-paper-skills", "skills"),
    ("research-skills-hub/collected-skills", "collected-skills"),
)
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CATALOG_START = "<!-- BEGIN GENERATED SKILLS CATALOG -->"
CATALOG_END = "<!-- END GENERATED SKILLS CATALOG -->"


class SyncError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to a checkout of AI-Human-Research-OS.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Path to this repository (defaults to the script's repository).",
    )
    parser.add_argument(
        "--source-revision",
        help="Upstream commit SHA; derived from the source checkout when omitted.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report drift without changing files; exits 1 when drift exists.",
    )
    return parser.parse_args()


def load_ignore_patterns(target: Path) -> list[str]:
    ignore_file = target / ".syncignore"
    if not ignore_file.exists():
        return []
    return [
        line.strip()
        for line in ignore_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def is_ignored(relative_path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(relative_path, pattern) for pattern in patterns)


def skill_name(skill_file: Path) -> str:
    text = skill_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SyncError(f"missing YAML frontmatter: {skill_file}")

    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise SyncError(f"unclosed YAML frontmatter: {skill_file}") from exc

    for line in lines[1:end]:
        match = re.match(r"^name:\s*([^#]+?)\s*$", line)
        if match:
            return match.group(1).strip().strip("'\"")
    raise SyncError(f"frontmatter has no name: {skill_file}")


def discover_skills(
    source_root: Path, source_relative: str, patterns: list[str]
) -> dict[str, Path]:
    source_directory = source_root / source_relative
    if not source_directory.is_dir():
        raise SyncError(f"source directory does not exist: {source_directory}")

    skills: dict[str, Path] = {}
    for child in sorted(source_directory.iterdir()):
        relative_path = f"{source_relative}/{child.name}"
        if not child.is_dir() or is_ignored(relative_path, patterns):
            continue
        skill_file = child / "SKILL.md"
        if not skill_file.is_file():
            continue
        declared_name = skill_name(skill_file)
        if declared_name != child.name:
            raise SyncError(
                f"skill name {declared_name!r} does not match directory {child.name!r}"
            )
        if not NAME_PATTERN.fullmatch(declared_name):
            raise SyncError(f"invalid skill name: {declared_name!r}")
        skills[child.name] = child
    return skills


def path_signature(root: Path) -> list[tuple[str, str, int | str]]:
    if not root.exists() and not root.is_symlink():
        return []

    signature: list[tuple[str, str, int | str]] = []
    for current_root, directory_names, file_names in os.walk(root, followlinks=False):
        directory_names.sort()
        file_names.sort()
        current = Path(current_root)
        for name in directory_names + file_names:
            path = current / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink():
                signature.append((relative, "link", os.readlink(path)))
            elif path.is_file():
                signature.append((relative, "file", path.stat().st_mode & 0o777))
                signature.append((relative, "bytes", path.read_bytes()))
    return signature


def destination_skills(target_directory: Path) -> dict[str, Path]:
    if not target_directory.is_dir():
        raise SyncError(f"target directory does not exist: {target_directory}")
    return {
        child.name: child
        for child in sorted(target_directory.iterdir())
        if child.is_dir() and (child / "SKILL.md").is_file()
    }


def managed_lines(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = lines.index(CATALOG_START)
        end = lines.index(CATALOG_END, start + 1)
    except ValueError as exc:
        raise SyncError(f"missing generated catalog markers: {path}") from exc
    return lines[start + 1 : end]


def markdown_link_name(text: str) -> str | None:
    match = re.search(r"\[(?:`)?([^]`]+)(?:`)?\]\(", text)
    return match.group(1) if match else None


def table_entries(lines: list[str]) -> dict[str, list[str]]:
    entries: dict[str, list[str]] = {}
    for line in lines:
        if not line.startswith("|"):
            continue
        columns = [column.strip() for column in line.strip().strip("|").split(" | ")]
        name = markdown_link_name(columns[0]) if columns else None
        if name:
            entries[name] = columns
    return entries


def index_entries(lines: list[str]) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in lines:
        match = re.match(r"^\* \[([^]]+)\]\([^)]+\) - (.+)$", line)
        if match:
            entries[match.group(1)] = match.group(2)
    return entries


def source_table_entries(path: Path) -> dict[str, list[str]]:
    return table_entries(path.read_text(encoding="utf-8").splitlines())


def source_index_entries(path: Path) -> dict[str, str]:
    return index_entries(path.read_text(encoding="utf-8").splitlines())


def fallback_description(skill_file: Path) -> str:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^description:\s*(.+)$", line)
        if match and match.group(1) not in {">", ">-", "|", "|-"}:
            description = match.group(1).strip().strip("'\"")
            first_sentence = re.split(r"(?<=[.!?])\s+", description, maxsplit=1)[0]
            return first_sentence
    return "See the skill documentation for details."


def replace_managed_lines(path: Path, replacement: list[str], check: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    try:
        start = lines.index(CATALOG_START)
        end = lines.index(CATALOG_END, start + 1)
    except ValueError as exc:
        raise SyncError(f"missing generated catalog markers: {path}") from exc
    updated_lines = lines[: start + 1] + replacement + lines[end:]
    updated = "\n".join(updated_lines) + ("\n" if text.endswith("\n") else "")
    if updated == text:
        return False
    if not check:
        path.write_text(updated, encoding="utf-8")
    return True


def update_catalogs(
    source_root: Path,
    target_root: Path,
    source_skill_sets: dict[str, dict[str, Path]],
    check: bool,
) -> list[str]:
    open_source = "research-skills-hub/open-paper-skills"
    collected_source = "research-skills-hub/collected-skills"
    open_skills = source_skill_sets[open_source]
    collected_skills = source_skill_sets[collected_source]

    open_source_table = source_table_entries(source_root / open_source / "README.md")
    collected_source_table = source_table_entries(
        source_root / collected_source / "README.md"
    )
    open_source_index = source_index_entries(source_root / open_source / "index.md")
    collected_source_index = source_index_entries(
        source_root / collected_source / "index.md"
    )

    root_readme = target_root / "README.md"
    skills_readme = target_root / "skills/README.md"
    collected_readme = target_root / "collected-skills/README.md"
    skills_index = target_root / "skills/index.md"
    collected_index = target_root / "collected-skills/index.md"

    root_existing = table_entries(managed_lines(root_readme))
    skills_existing = table_entries(managed_lines(skills_readme))
    collected_existing = table_entries(managed_lines(collected_readme))
    skills_index_existing = index_entries(managed_lines(skills_index))
    collected_index_existing = index_entries(managed_lines(collected_index))

    def description(
        name: str,
        existing: dict[str, list[str]],
        source_table: dict[str, list[str]],
        source_index: dict[str, str],
        skill_file: Path,
    ) -> str:
        if name in existing and len(existing[name]) >= 2:
            return existing[name][1]
        if name in source_table and len(source_table[name]) >= 2:
            return source_table[name][1]
        if name in source_index:
            return source_index[name]
        return fallback_description(skill_file)

    root_rows = []
    skills_rows = []
    skills_index_rows = []
    for name, skill_directory in sorted(open_skills.items()):
        root_description = description(
            name, root_existing, open_source_table, open_source_index, skill_directory / "SKILL.md"
        )
        skills_description = description(
            name, skills_existing, open_source_table, open_source_index, skill_directory / "SKILL.md"
        )
        index_description = (
            skills_index_existing.get(name)
            or open_source_index.get(name)
            or skills_description
        )
        root_rows.append(
            f"| [`{name}`](skills/{name}/) | {root_description} |"
        )
        skills_rows.append(f"| [{name}]({name}/) | {skills_description} |")
        skills_index_rows.append(
            f"* [{name}]({name}/SKILL.md) - {index_description}"
        )

    collected_rows = []
    collected_index_rows = []
    for name, skill_directory in sorted(collected_skills.items()):
        collected_description = description(
            name,
            collected_existing,
            collected_source_table,
            collected_source_index,
            skill_directory / "SKILL.md",
        )
        existing_columns = collected_existing.get(name, [])
        source_columns = collected_source_table.get(name, [])
        provenance = (
            existing_columns[2]
            if len(existing_columns) >= 3
            else source_columns[2]
            if len(source_columns) >= 3
            else "Verify upstream provenance and license before redistribution."
        )
        index_description = (
            collected_index_existing.get(name)
            or collected_source_index.get(name)
            or collected_description
        )
        collected_rows.append(
            f"| [{name}]({name}/) | {collected_description} | {provenance} |"
        )
        collected_index_rows.append(
            f"* [{name}]({name}/SKILL.md) - {index_description}"
        )

    replacements = (
        (root_readme, root_rows),
        (skills_readme, skills_rows),
        (skills_index, skills_index_rows),
        (collected_readme, collected_rows),
        (collected_index, collected_index_rows),
    )
    actions: list[str] = []
    for path, rows in replacements:
        if replace_managed_lines(path, rows, check):
            actions.append(f"update {path.relative_to(target_root).as_posix()} catalog")
    return actions


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def replace_directory(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".skill-sync-", dir=destination.parent) as temp:
        staged = Path(temp) / destination.name
        shutil.copytree(source, staged, symlinks=True)
        remove_path(destination)
        shutil.move(str(staged), str(destination))


def derive_revision(source: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(source), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def write_revision(target: Path, revision: str) -> None:
    content = f"source_repository={SOURCE_REPOSITORY}\nsource_commit={revision}\n"
    (target / ".upstream-revision").write_text(content, encoding="utf-8")


def sync_mapping(
    source_skills: dict[str, Path],
    target_root: Path,
    source_relative: str,
    target_relative: str,
    patterns: list[str],
    check: bool,
) -> list[str]:
    target_directory = target_root / target_relative
    target_skills = destination_skills(target_directory)
    actions: list[str] = []

    for name, source_path in source_skills.items():
        destination = target_directory / name
        if name not in target_skills:
            actions.append(f"add {target_relative}/{name}")
            if not check:
                replace_directory(source_path, destination)
        elif path_signature(source_path) != path_signature(destination):
            actions.append(f"update {target_relative}/{name}")
            if not check:
                replace_directory(source_path, destination)

    for name, destination in target_skills.items():
        upstream_path = f"{source_relative}/{name}"
        if name not in source_skills and not is_ignored(upstream_path, patterns):
            actions.append(f"remove {target_relative}/{name}")
            if not check:
                remove_path(destination)

    return actions


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    patterns = load_ignore_patterns(target)

    actions: list[str] = []
    try:
        source_skill_sets = {
            source_relative: discover_skills(source, source_relative, patterns)
            for source_relative, _ in MAPPINGS
        }
        for source_relative, target_relative in MAPPINGS:
            actions.extend(
                sync_mapping(
                    source_skill_sets[source_relative],
                    target,
                    source_relative,
                    target_relative,
                    patterns,
                    args.check,
                )
            )
        actions.extend(update_catalogs(source, target, source_skill_sets, args.check))
    except (OSError, SyncError, subprocess.CalledProcessError) as exc:
        print(f"sync error: {exc}", file=sys.stderr)
        return 2

    if args.check:
        if actions:
            print("skill mirror is out of date:")
            for action in actions:
                print(f"- {action}")
            return 1
        print("skill mirror is up to date")
        return 0

    if actions:
        for action in actions:
            print(action)
        try:
            revision = args.source_revision or derive_revision(source)
            write_revision(target, revision)
        except (OSError, subprocess.CalledProcessError) as exc:
            print(f"sync error: unable to record source revision: {exc}", file=sys.stderr)
            return 2
    else:
        print("no skill changes detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
