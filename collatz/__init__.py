"""Utilities for working with the Collatz conjecture."""
from .sequence import collatz_step, generate_sequence, stopping_time, total_stopping_time

__all__ = [
    "collatz_step",
    "generate_sequence",
    "stopping_time",
    "total_stopping_time",
]
