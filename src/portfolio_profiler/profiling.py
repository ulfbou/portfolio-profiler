"""Repository evidence profile composition."""
from __future__ import annotations

from pathlib import Path

from .collectors.git import collect_git_evidence, repository_root
from .models.profile import RepositoryEvidenceProfile
from .models.repository import RepositoryProfile


def profile_repository(repository: str | Path) -> RepositoryEvidenceProfile:
    """Compose identity and local Git evidence for one repository."""
    root = repository_root(repository)
    identity = RepositoryProfile(name=root.name, path=root.as_posix())
    return RepositoryEvidenceProfile(
        schema_version="1.0",
        repository=identity,
        git=collect_git_evidence(root),
    )
