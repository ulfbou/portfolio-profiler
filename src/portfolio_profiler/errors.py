"""Expected Portfolio Profiler failures."""


class PortfolioProfilerError(Exception):
    """Base class for expected product failures."""


class RepositoryInputError(PortfolioProfilerError):
    """The requested repository path is invalid."""


class GitUnavailableError(PortfolioProfilerError):
    """The Git executable is unavailable."""


class GitCollectionError(PortfolioProfilerError):
    """Local Git evidence could not be collected."""
