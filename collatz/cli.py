"""Command-line interface for exploring Collatz sequences."""
from __future__ import annotations

import argparse
from typing import Iterable

from .sequence import generate_sequence, summarise


def _format_sequence(values: Iterable[int]) -> str:
    return " → ".join(str(value) for value in values)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect Collatz trajectories")
    parser.add_argument(
        "start",
        type=int,
        help="Positive integer to start the Collatz sequence from",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print summary statistics instead of the full sequence",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.start < 1:
        parser.error("start must be a positive integer")

    if args.summary:
        result = summarise(args.start)
        print(f"Sequence for {result.start}: {_format_sequence(result.sequence)}")
        print(f"Stopping time: {result.stopping_time}")
        print(f"Total stopping time: {result.total_stopping_time}")
    else:
        print(_format_sequence(generate_sequence(args.start)))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
