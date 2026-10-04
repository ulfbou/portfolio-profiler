"""Composed repository evidence profiles."""
from __future__ import annotations

from dataclasses import dataclass

from .git import GitEvidence
from .repository import RepositoryProfile


@dataclass(frozen=True)
class RepositoryEvidenceProfile:
    """Versioned factual evidence for one repository."""

    schema_version: str
    repository: RepositoryProfile
    git: GitEvidence

    def to_document(self) -> dict[str, object]:
        """Return the stable public JSON representation."""
        return {
            "git": self.git.to_document(),
            "repository": self.repository.to_document(),
            "schemaVersion": self.schema_version,
        }
