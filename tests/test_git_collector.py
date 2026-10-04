"""Tests for deterministic local Git collection."""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from portfolio_profiler.collectors.git import (
    collect_git_evidence,
    repository_root,
    run_git,
)
from portfolio_profiler.errors import (
    GitCollectionError,
    GitUnavailableError,
    RepositoryInputError,
)
from tests.support import create_repository, git


def test_collects_deterministic_git_evidence(tmp_path: Path) -> None:
    repository = create_repository(tmp_path)
    evidence = collect_git_evidence(repository)
    assert evidence.current_commit == git(repository, "rev-parse", "HEAD")
    assert evidence.root_commits == (
        git(repository, "rev-list", "--max-parents=0", "HEAD"),
    )
    assert evidence.branch == "master"
    assert evidence.detached_head is False
    assert evidence.dirty is False
    assert evidence.tracked_file_count == 2
    assert evidence.commit_count == 2
    assert evidence.to_document() == collect_git_evidence(repository).to_document()


def test_accepts_string_and_relative_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = create_repository(tmp_path)
    monkeypatch.chdir(tmp_path)
    assert collect_git_evidence("repository") == collect_git_evidence(repository)


def test_dirty_and_detached_states(tmp_path: Path) -> None:
    repository = create_repository(tmp_path)
    (repository / "new.txt").write_text("new", encoding="utf-8")
    assert collect_git_evidence(repository).dirty is True
    git(repository, "checkout", "--detach", "HEAD")
    evidence = collect_git_evidence(repository)
    assert evidence.branch is None
    assert evidence.detached_head is True


def test_multiple_root_commits_are_sorted(tmp_path: Path) -> None:
    repository = create_repository(tmp_path)
    first_root = git(repository, "rev-list", "--max-parents=0", "HEAD")
    git(repository, "checkout", "--orphan", "unrelated")
    for path in repository.glob("file-*.txt"):
        path.unlink()
    git(repository, "rm", "-r", "--cached", ".")
    (repository / "other.txt").write_text("other\n", encoding="utf-8")
    git(repository, "add", ".")
    git(repository, "commit", "-m", "unrelated root")
    second_root = git(repository, "rev-parse", "HEAD")
    git(repository, "checkout", "master")
    git(repository, "merge", "--allow-unrelated-histories", "unrelated", "-m", "merge")
    assert collect_git_evidence(repository).root_commits == tuple(
        sorted((first_root, second_root))
    )


@pytest.mark.parametrize("kind", ["missing", "file", "directory"])
def test_rejects_invalid_inputs(tmp_path: Path, kind: str) -> None:
    path = tmp_path / kind
    if kind == "file":
        path.write_text("x", encoding="utf-8")
    elif kind == "directory":
        path.mkdir()
    with pytest.raises(RepositoryInputError):
        collect_git_evidence(path)


def test_empty_repository_fails(tmp_path: Path) -> None:
    repository = create_repository(tmp_path, commits=0)
    with pytest.raises(GitCollectionError):
        collect_git_evidence(repository)


def test_git_unavailable(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repository = create_repository(tmp_path)

    def missing(*args: object, **kwargs: object) -> None:
        raise FileNotFoundError

    monkeypatch.setattr("portfolio_profiler.collectors.git.subprocess.run", missing)
    with pytest.raises(GitUnavailableError):
        collect_git_evidence(repository)


def test_nonzero_git_exit_preserves_stderr(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def failed(*args: object, **kwargs: object) -> subprocess.CompletedProcess[bytes]:
        return subprocess.CompletedProcess([], 128, b"", b"stable failure\n")

    monkeypatch.setattr("portfolio_profiler.collectors.git.subprocess.run", failed)
    with pytest.raises(GitCollectionError, match="stable failure"):
        run_git(tmp_path, "status")


def test_corrupt_repository_failure_is_not_invalid_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository = create_repository(tmp_path)

    def failed(*args: object, **kwargs: object) -> bytes:
        raise GitCollectionError("corrupt repository")

    monkeypatch.setattr("portfolio_profiler.collectors.git.run_git", failed)
    with pytest.raises(GitCollectionError, match="corrupt repository"):
        repository_root(repository)
