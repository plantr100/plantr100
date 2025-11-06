import pytest

from collatz.sequence import (
    CollatzResult,
    collatz_step,
    generate_sequence,
    iter_sequence,
    stopping_time,
    summarise,
    total_stopping_time,
)


def test_collatz_step_even_and_odd():
    assert collatz_step(6) == 3
    assert collatz_step(3) == 10


def test_collatz_step_requires_positive():
    with pytest.raises(ValueError):
        collatz_step(0)


def test_generate_sequence_until_one():
    assert generate_sequence(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]


def test_iter_sequence_matches_generate_sequence():
    assert list(iter_sequence(7)) == generate_sequence(7)


def test_stopping_time_counts_edges():
    assert stopping_time(1) == 0
    assert stopping_time(6) == 8


def test_total_stopping_time_alias():
    assert total_stopping_time(6) == stopping_time(6)


def test_summarise_returns_dataclass():
    result = summarise(6)
    assert isinstance(result, CollatzResult)
    assert result.sequence[0] == 6
    assert result.sequence[-1] == 1
    assert result.stopping_time == stopping_time(6)
