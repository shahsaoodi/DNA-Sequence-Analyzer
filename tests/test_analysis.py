import pytest

from dna_analyzer.analysis import (
    analyze_sequence,
    calculate_at_content,
    calculate_gc_content,
    complementary_sequence,
    count_nucleotides,
    reverse_complement,
    validate_dna,
)


def test_validation_converts_lowercase_to_uppercase():
    assert validate_dna("atgc") == "ATGC"


def test_validation_removes_whitespace():
    assert validate_dna(" ATG\nC G ") == "ATGCG"


def test_validation_rejects_empty_sequence():
    with pytest.raises(ValueError, match="empty"):
        validate_dna("  \n ")


def test_validation_rejects_invalid_symbols():
    with pytest.raises(ValueError, match="X"):
        validate_dna("ATGX")


def test_validation_requires_string():
    with pytest.raises(TypeError):
        validate_dna(123)


def test_nucleotide_counts_include_zeroes():
    assert count_nucleotides("AAGT") == {
        "A": 2, "T": 1, "G": 1, "C": 0
    }


def test_gc_content():
    assert calculate_gc_content("GGCCAT") == pytest.approx(66.6666667)


def test_at_content():
    assert calculate_at_content("AATTGC") == pytest.approx(66.6666667)


def test_gc_and_at_content_sum_to_one_hundred():
    sequence = "ATGCGATC"
    total = calculate_gc_content(sequence) + calculate_at_content(sequence)
    assert total == pytest.approx(100.0)


def test_complement_preserves_display_order():
    assert complementary_sequence("ATGC") == "TACG"


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_reverse_complement_is_its_own_inverse():
    sequence = "ATGCCGTA"
    assert reverse_complement(reverse_complement(sequence)) == sequence


def test_analyze_sequence_returns_all_stage_one_results():
    result = analyze_sequence("ATGC")
    assert result == {
        "sequence": "ATGC",
        "length": 4,
        "counts": {"A": 1, "T": 1, "G": 1, "C": 1},
        "gc_content": 50.0,
        "at_content": 50.0,
        "complement": "TACG",
        "reverse_complement": "GCAT",
    }
