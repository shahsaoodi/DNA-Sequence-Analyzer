"""Allow the package to be run with ``python -m dna_analyzer``."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
