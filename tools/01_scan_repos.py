"""Scan bare git repositories without cloning them.

Reads every ``*.git`` directory in the export folder using only git
plumbing commands (``ls-tree``, ``show``, ``log``) and writes one JSON
record per repository.

Usage:
    uv run python tools/01_scan_repos.py
    uv run python tools/01_scan_repos.py --repos /path/to/export --out tools/repo_scan.json
"""

from __future__ import annotations

import argparse
import collections
import json
import subprocess
from pathlib import Path

# Bare repos are read-only inputs; results go here by default.
DEFAULT_REPOS = Path("/workspace/src/github/repositories/plops")
DEFAULT_OUT = Path("tools/repo_scan.json")

# Filenames that strongly hint at a language/ecosystem. Basename match.
MARKER_FILES = {
    "Cargo.toml",
    "Cargo.lock",
    "package.json",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "requirements.txt",
    "CMakeLists.txt",
    "Makefile",
    "go.mod",
    "Gemfile",
    "build.gradle",
    "pom.xml",
    "Dockerfile",
    "environment.yml",
    ".ino",
    ".pde",
}

# Suffix markers are matched against the file extension instead.
MARKER_SUFFIXES = {".asd", ".ino", ".pde"}

# README candidates in priority order (top-level first, then nested).
README_NAMES = {
    "readme.md",
    "readme.org",
    "readme.txt",
    "readme.rst",
    "readme",
    "read.me",
}

MAX_README_LINES = 40


def git(git_dir: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Run a git command against a bare repository."""
    return subprocess.run(
        ["git", f"--git-dir={git_dir}", *args],
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


def has_head(git_dir: Path) -> bool:
    proc = git(git_dir, "rev-parse", "--verify", "HEAD")
    return proc.returncode == 0


def list_files(git_dir: Path) -> list[str]:
    proc = git(git_dir, "ls-tree", "-r", "HEAD", "--name-only", "-z")
    if proc.returncode != 0:
        return []
    return [p for p in proc.stdout.split("\0") if p]


def show_file(git_dir: Path, path: str, max_bytes: int = 8000) -> str:
    proc = git(git_dir, "show", f"HEAD:{path}")
    if proc.returncode != 0:
        return ""
    text = proc.stdout[:max_bytes]
    lines = [
        line
        for line in text.splitlines()
        if "![" not in line
        and "<img" not in line.lower()
        and "badge" not in line.lower()
    ]
    return "\n".join(lines[:MAX_README_LINES])


def last_commit(git_dir: Path) -> tuple[str, str]:
    proc = git(git_dir, "log", "-1", "--format=%ci%x00%s")
    if proc.returncode != 0:
        return "", ""
    date, _, subject = proc.stdout.strip().partition("\x00")
    return date.strip(), subject.strip()


def find_readme(files: list[str]) -> str:
    """Return the README path to read (top-level preferred), else ''."""
    nested = ""
    for path in files:
        name = path.lower()
        base = name.rsplit("/", 1)[-1]
        if base in README_NAMES:
            if "/" not in path:
                return path
            nested = nested or path
    return nested


def top_extensions(files: list[str], limit: int = 12) -> list[list]:
    """Count file extensions, e.g. [['.lisp', 42], ['.md', 3]]."""
    counts: collections.Counter[str] = collections.Counter()
    for path in files:
        base = path.rsplit("/", 1)[-1]
        if (
            "." in base
            and not base.startswith(".")
            or base.startswith(".")
            and base.count(".") > 1
        ):
            counts["." + base.rsplit(".", 1)[-1].lower()] += 1
    return [[ext, n] for ext, n in counts.most_common(limit)]


def find_markers(files: list[str]) -> list[str]:
    """Return sorted marker filenames/extensions found in the repo."""
    found: set[str] = set()
    for path in files:
        base = path.rsplit("/", 1)[-1]
        if base in MARKER_FILES:
            found.add(base)
        if "." in base:
            suffix = "." + base.rsplit(".", 1)[-1].lower()
            if suffix in MARKER_SUFFIXES:
                found.add("*" + suffix)
        low = base.lower()
        if low.startswith("requirements") and low.endswith(".txt"):
            found.add("requirements*.txt")
    return sorted(found)


def scan_repo(git_dir: Path) -> dict:
    """Scan one bare repository, return its JSON record."""
    name = git_dir.name.removesuffix(".git")
    if name.endswith(".wiki"):
        date, subject = last_commit(git_dir) if has_head(git_dir) else ("", "")
        return {
            "name": name,
            "status": "wiki",
            "last_commit_date": date,
            "last_commit_subject": subject,
        }
    if not has_head(git_dir):
        return {"name": name, "status": "empty"}
    files = list_files(git_dir)
    readme_path = find_readme(files)
    date, subject = last_commit(git_dir)
    return {
        "name": name,
        "status": "ok",
        "file_count": len(files),
        "top_extensions": top_extensions(files),
        "markers": find_markers(files),
        "readme_path": readme_path,
        "readme_head": show_file(git_dir, readme_path) if readme_path else "",
        "last_commit_date": date,
        "last_commit_subject": subject,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repos", type=Path, default=DEFAULT_REPOS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    git_dirs = sorted(p for p in args.repos.iterdir() if p.suffix == ".git")
    records = [scan_repo(d) for d in git_dirs]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(records, indent=1, ensure_ascii=False) + "\n")

    counts: collections.Counter[str] = collections.Counter(r["status"] for r in records)
    print(f"scanned {len(records)} repos from {args.repos}")
    for status, num in sorted(counts.items()):
        print(f"  {status}: {num}")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
