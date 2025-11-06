# Collatz Project

A small Python package for exploring the Collatz conjecture. It exposes
re-usable utilities as well as a simple command-line interface.

## Usage

```bash
python -m collatz.cli 27
```

Add `--summary` to show additional statistics instead of only the
trajectory.

## Development

Install the project in editable mode and run the tests:

```bash
python -m pip install -e .[dev]
pytest
```

Large log files generated during experimentation should be stored under a
`logs/` directory which is ignored by Git.
