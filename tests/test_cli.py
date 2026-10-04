"""Tests for profile CLI behavior."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from portfolio_profiler.cli import run
from portfolio_profiler.errors import GitCollectionError
from tests.support import create_repository


def test_profile_cli_is_byte_stable(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repository = create_repository(tmp_path)
    assert run(["profile", str(repository)]) == 0
    first = capsys.readouterr()
    assert run(["profile", str(repository)]) == 0
    second = capsys.readouterr()
    assert first.out == second.out
    assert first.err == second.err == ""
    document = json.loads(first.out)
    assert document["schemaVersion"] == "1.0"
    assert document["repository"]["name"] == "repository"


def test_profile_cli_invalid_input(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert run(["profile", str(tmp_path / "missing")]) == 2
    assert "ERROR:" in capsys.readouterr().err


def test_profile_cli_reports_collection_failure(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    def failure(repository: Path) -> None:
        raise GitCollectionError("stable failure")

    monkeypatch.setattr("portfolio_profiler.cli.profile_repository", failure)
    assert run(["profile", "."]) == 3
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "ERROR: stable failure\n"
