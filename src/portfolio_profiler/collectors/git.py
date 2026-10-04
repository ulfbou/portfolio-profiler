"""Deterministic local Git metadata collection."""
from __future__ import annotations

import subprocess
from pathlib import Path

from portfolio_profiler.errors import (
    GitCollectionError,
    GitUnavailableError,
    RepositoryInputError,
)
from portfolio_profiler.models.git import GitEvidence

_NOT_REPOSITORY_MARKER = "not a git repository"


def run_git(repository: Path, *arguments: str) -> bytes:
    """Execute one read-only local Git observation without a shell."""
    try:
        result = subprocess.run(
            ["git", *arguments],
            cwd=repository,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    except FileNotFoundError as exc:
        raise GitUnavailableError("Git executable is unavailable") from exc
    except OSError as exc:
        raise GitCollectionError("Git could not be executed") from exc

    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        message = detail or f"Git command failed with exit code {result.returncode}"
        raise GitCollectionError(message)
    return result.stdout


def _decode_text(value: bytes, field: str, *, allow_empty: bool = False) -> str:
    """Decode one textual Git result using the public error contract."""
    try:
        result = value.decode("utf-8").strip()
    except UnicodeDecodeError as exc:
        raise GitCollectionError(f"Git returned undecodable {field}") from exc
    if not allow_empty and not result:
        raise GitCollectionError(f"Git returned empty {field}")
    return result


def repository_root(repository: str | Path) -> Path:
    """Resolve and validate the containing Git repository root."""
    requested = Path(repository).expanduser()
    if not requested.exists():
        raise RepositoryInputError(f"repository path does not exist: {requested}")
    if not requested.is_dir():
        raise RepositoryInputError(
            f"repository path is not a directory: {requested}"
        )

    resolved = requested.resolve()
    try:
        output = run_git(resolved, "rev-parse", "--show-toplevel")
    except GitCollectionError as exc:
        if _NOT_REPOSITORY_MARKER in str(exc).casefold():
            raise RepositoryInputError(
                f"path is not inside a Git repository: {resolved}"
            ) from exc
        raise
    return Path(_decode_text(output, "repository root")).resolve()


def collect_git_evidence(repository: str | Path) -> GitEvidence:
    """Collect stable facts from the repository containing the supplied path."""
    root = repository_root(repository)
    current_commit = _decode_text(
        run_git(root, "rev-parse", "--verify", "HEAD"),
        "HEAD",
    )
    branch = _decode_text(
        run_git(root, "branch", "--show-current"),
        "branch",
        allow_empty=True,
    ) or None
    root_commits = tuple(
        sorted(
            _decode_text(
                run_git(root, "rev-list", "--max-parents=0", "HEAD"),
                "root commits",
            ).splitlines()
        )
    )
    count_text = _decode_text(
        run_git(root, "rev-list", "--count", "HEAD"),
        "commit count",
    )
    try:
        commit_count = int(count_text)
    except ValueError as exc:
        raise GitCollectionError("Git returned malformed commit count") from exc

    tracked_files = run_git(root, "ls-files", "-z")
    tracked_file_count = sum(
        1 for item in tracked_files.split(b"\0") if item
    )
    dirty = bool(
        run_git(
            root,
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
        )
    )
    return GitEvidence(
        current_commit=current_commit,
        root_commits=root_commits,
        branch=branch,
        detached_head=branch is None,
        dirty=dirty,
        tracked_file_count=tracked_file_count,
        commit_count=commit_count,
    )
