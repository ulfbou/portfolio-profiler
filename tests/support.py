"""Reusable test support for local Git repositories."""
from __future__ import annotations

import subprocess
from pathlib import Path


def git(repository: Path, *arguments: str) -> str:
    """Execute Git for controlled test setup."""
    result = subprocess.run(
        ["git", *arguments],
        cwd=repository,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def create_repository(root: Path, commits: int = 2) -> Path:
    """Create a repository with deterministic test commits."""
    repository = root / "repository"
    repository.mkdir()
    git(repository, "init", "-b", "master")
    git(repository, "config", "user.name", "Test User")
    git(repository, "config", "user.email", "test@example.invalid")
    for index in range(commits):
        path = repository / f"file-{index}.txt"
        path.write_text(f"content {index}\n", encoding="utf-8")
        git(repository, "add", ".")
        git(repository, "commit", "-m", f"commit {index}")
    return repository
