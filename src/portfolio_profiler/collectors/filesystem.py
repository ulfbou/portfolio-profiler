"""Filesystem evidence helpers."""

from __future__ import annotations

from pathlib import Path


def is_git_repository(path: Path) -> bool:
    """Return whether a path contains a Git administrative entry."""
    marker = path / ".git"
    return marker.is_dir() or marker.is_file()
