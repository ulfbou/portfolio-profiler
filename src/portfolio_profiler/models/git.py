"""Immutable local Git evidence."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GitEvidence:
    """Factual evidence collected from a local Git repository."""

    current_commit: str
    root_commits: tuple[str, ...]
    branch: str | None
    detached_head: bool
    dirty: bool
    tracked_file_count: int
    commit_count: int

    def to_document(self) -> dict[str, object]:
        """Return the stable public JSON representation."""
        return {
            "branch": self.branch,
            "commitCount": self.commit_count,
            "currentCommit": self.current_commit,
            "detachedHead": self.detached_head,
            "dirty": self.dirty,
            "rootCommits": list(self.root_commits),
            "trackedFileCount": self.tracked_file_count,
        }
