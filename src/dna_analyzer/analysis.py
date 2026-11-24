"""Core functions for basic DNA sequence analysis."""

from collections import Counter
from typing import TypedDict


VALID_BASES = frozenset("ATGC")
BASE_ORDER = ("A", "T", "G", "C")
COMPLEMENT = str.maketrans("ATGC", "TACG")


class SequenceAnalysis(TypedDict):
    """The results returned by :func:`analyze_sequence`."""

    sequence: str
    length: int
    counts: dict[str, int]
    gc_content: float
    at_content: float
    complement: str
    reverse_complement: str


def validate_dna(sequence: str) -> str:
    """Normalize and validate a DNA sequence.

    Lowercase letters are converted to uppercase and whitespace is removed.
    Only the four standard DNA bases (A, T, G, and C) are accepted.

    Raises:
        TypeError: If ``sequence`` is not a string.
        ValueError: If the sequence is empty or contains another symbol.
    """
    if not isinstance(sequence, str):
        raise TypeError("DNA sequence must be a string.")

    normalized = "".join(sequence.split()).upper()

    if not normalized:
        raise ValueError("DNA sequence cannot be empty.")

    invalid_symbols = sorted(set(normalized) - VALID_BASES)
    if invalid_symbols:
        symbols = ", ".join(invalid_symbols)
        raise ValueError(f"Invalid DNA symbol(s): {symbols}")

    return normalized


def count_nucleotides(sequence: str) -> dict[str, int]:
    """Return counts for A, T, G, and C in a DNA sequence."""
    normalized = validate_dna(sequence)
    observed = Counter(normalized)
    return {base: observed.get(base, 0) for base in BASE_ORDER}


def calculate_gc_content(sequence: str) -> float:
    """Return the percentage of bases that are G or C."""
    normalized = validate_dna(sequence)
    gc_count = normalized.count("G") + normalized.count("C")
    return (gc_count / len(normalized)) * 100.0


def calculate_at_content(sequence: str) -> float:
    """Return the percentage of bases that are A or T."""
    normalized = validate_dna(sequence)
    at_count = normalized.count("A") + normalized.count("T")
    return (at_count / len(normalized)) * 100.0


def complementary_sequence(sequence: str) -> str:
    """Return the complementary strand in the same displayed order.

    This function does not reverse the sequence.
    """
    normalized = validate_dna(sequence)
    return normalized.translate(COMPLEMENT)


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement, conventionally written 5' to 3'."""
    return complementary_sequence(sequence)[::-1]


def analyze_sequence(sequence: str) -> SequenceAnalysis:
    """Run all Stage 1 analyses and return the results in one dictionary."""
    normalized = validate_dna(sequence)
    counts = count_nucleotides(normalized)

    return {
        "sequence": normalized,
        "length": len(normalized),
        "counts": counts,
        "gc_content": calculate_gc_content(normalized),
        "at_content": calculate_at_content(normalized),
        "complement": complementary_sequence(normalized),
        "reverse_complement": reverse_complement(normalized),
    }
