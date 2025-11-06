"""Core utilities for generating and analysing Collatz sequences."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Iterator, List


@dataclass(frozen=True)
class CollatzResult:
    """Summary information about a Collatz trajectory."""

    start: int
    sequence: List[int]

    @property
    def stopping_time(self) -> int:
        """Return the number of steps required to reach ``1``.

        The classical "stopping time" counts the number of steps the sequence
        takes to hit ``1`` for the first time. If the starting number is
        already ``1`` the stopping time is ``0``.
        """

        return len(self.sequence) - 1

    @property
    def total_stopping_time(self) -> int:
        """Return the number of steps required to reach ``1`` for good.

        This is identical to :meth:`stopping_time` for traditional Collatz
        sequences because they stop once ``1`` is reached. The property is
        exposed separately to match common terminology in Collatz literature
        and to make the API explicit.
        """

        return self.stopping_time


def collatz_step(value: int) -> int:
    """Return the next value in the Collatz sequence.

    Parameters
    ----------
    value:
        Positive integer to advance.
    """

    if value < 1:
        raise ValueError("collatz_step is only defined for positive integers")
    if value % 2 == 0:
        return value // 2
    return value * 3 + 1


def generate_sequence(start: int) -> List[int]:
    """Generate the Collatz sequence starting from ``start``.

    The full trajectory, including the starting number and the terminal ``1``,
    is returned as a list for easy inspection and testing.
    """

    if start < 1:
        raise ValueError("The Collatz sequence is only defined for positive integers")

    sequence = [start]
    while sequence[-1] != 1:
        sequence.append(collatz_step(sequence[-1]))
    return sequence


def stopping_time(start: int) -> int:
    """Return the stopping time for ``start``.

    The stopping time counts how many iterations are required to reach ``1``.
    """

    return len(generate_sequence(start)) - 1


def total_stopping_time(start: int) -> int:
    """Return the total stopping time for ``start``.

    The "total" stopping time is usually defined as the steps required to
    reach ``1`` for the first time when always continuing to ``4``. Because
    the Collatz sequence terminates immediately at ``1`` in our implementation,
    this coincides with :func:`stopping_time`. The function exists mostly for
    API completeness and to make it easy to adapt should different behaviour
    be desired.
    """

    return stopping_time(start)


def iter_sequence(start: int) -> Iterator[int]:
    """Yield the values in the Collatz sequence lazily."""

    if start < 1:
        raise ValueError("The Collatz sequence is only defined for positive integers")

    value = start
    yield value
    while value != 1:
        value = collatz_step(value)
        yield value


def summarise(start: int) -> CollatzResult:
    """Return a :class:`CollatzResult` describing the trajectory from ``start``."""

    return CollatzResult(start=start, sequence=list(iter_sequence(start)))
