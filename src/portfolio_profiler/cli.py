"""Portfolio Profiler command-line interface."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .collectors.repository_discovery import discover_repositories


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(prog="portfolio-profiler")
    subparsers = parser.add_subparsers(dest="command", required=True)
    discover = subparsers.add_parser(
        "discover",
        help="discover Git repositories in a directory",
    )
    discover.add_argument("root", type=Path)
    return parser


def run(argv: list[str] | None = None) -> int:
    """Run the command-line interface and return its exit code."""
    arguments = build_parser().parse_args(argv)
    try:
        profiles = discover_repositories(arguments.root)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    document = [profile.to_document() for profile in profiles]
    sys.stdout.write(json.dumps(document, indent=2, sort_keys=True) + "\n")
    return 0


def main() -> None:
    """Run Portfolio Profiler as an installed command."""
    raise SystemExit(run())


if __name__ == "__main__":
    main()
