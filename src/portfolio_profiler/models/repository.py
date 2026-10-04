"""Repository evidence models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RepositoryProfile:
    """Minimal factual identity for one discovered repository."""

    name: str
    path: str

    def to_document(self) -> dict[str, str]:
        """Return a stable JSON-compatible representation."""
        return {"name": self.name, "path": self.path}
