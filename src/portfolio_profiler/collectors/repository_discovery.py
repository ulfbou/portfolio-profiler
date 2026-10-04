"""Deterministic local repository discovery."""

from __future__ import annotations

from pathlib import Path

from portfolio_profiler.errors import RepositoryInputError
from portfolio_profiler.models.repository import RepositoryProfile

from .filesystem import is_git_repository


def discover_repositories(root: str | Path) -> tuple[RepositoryProfile, ...]:
    """Discover Git repositories at the root and among its direct children."""
    resolved = Path(root).expanduser().resolve()
    if not resolved.is_dir():
        raise RepositoryInputError(
            f"repository search root is not a directory: {resolved}"
        )

    candidates = [resolved]
    candidates.extend(path for path in resolved.iterdir() if path.is_dir())
    profiles = (
        RepositoryProfile(name=path.name, path=path.as_posix())
        for path in candidates
        if is_git_repository(path)
    )
    return tuple(sorted(profiles, key=lambda profile: (profile.name, profile.path)))
