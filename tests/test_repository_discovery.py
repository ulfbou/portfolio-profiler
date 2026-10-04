"""Tests for deterministic local repository discovery."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from portfolio_profiler.cli import run
from portfolio_profiler.collectors.repository_discovery import discover_repositories
from portfolio_profiler.errors import RepositoryInputError


def make_repository(path: Path) -> Path:
    """Create a minimal repository marker for discovery tests."""
    path.mkdir()
    (path / ".git").mkdir()
    return path


def test_discovery_finds_direct_children_in_stable_order(tmp_path: Path) -> None:
    make_repository(tmp_path / "zeta")
    make_repository(tmp_path / "alpha")
    (tmp_path / "ordinary").mkdir()

    profiles = discover_repositories(tmp_path)

    assert [profile.name for profile in profiles] == ["alpha", "zeta"]
    assert all(Path(profile.path).is_absolute() for profile in profiles)


def test_discovery_includes_root_repository(tmp_path: Path) -> None:
    (tmp_path / ".git").write_text("gitdir: elsewhere\n", encoding="utf-8")

    profiles = discover_repositories(tmp_path)

    assert [profile.name for profile in profiles] == [tmp_path.name]


def test_discovery_accepts_expanded_string_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    home = tmp_path / "home"
    repositories = home / "github"
    repositories.mkdir(parents=True)
    make_repository(repositories / "portfolio-profiler")
    monkeypatch.setenv("HOME", str(home))

    profiles = discover_repositories("~/github")

    assert [profile.name for profile in profiles] == ["portfolio-profiler"]


def test_discovery_rejects_missing_root(tmp_path: Path) -> None:
    with pytest.raises(RepositoryInputError, match="not a directory"):
        discover_repositories(tmp_path / "missing")


def test_cli_emits_stable_json(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repository = make_repository(tmp_path / "sample")

    assert run(["discover", str(tmp_path)]) == 0
    captured = capsys.readouterr()

    assert json.loads(captured.out) == [
        {"name": "sample", "path": repository.as_posix()}
    ]
    assert captured.err == ""


def test_cli_reports_invalid_root(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert run(["discover", str(tmp_path / "missing")]) == 2

    captured = capsys.readouterr()
    assert captured.out == ""
    assert "not a directory" in captured.err
