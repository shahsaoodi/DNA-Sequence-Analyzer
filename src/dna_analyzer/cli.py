"""Command-line interface for the DNA Sequence Analyzer."""

import argparse
from pathlib import Path

from .analysis import analyze_sequence, validate_dna


def read_sequence_file(path: str) -> str:
    """Read a plain-text file containing one DNA sequence."""
    file_path = Path(path)

    try:
        return file_path.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError(f"Could not read '{file_path}': {error}") from error


def format_report(results: dict) -> str:
    """Format analysis results as a readable terminal report."""
    counts = results["counts"]

    lines = [
        "",
        "=" * 44,
        "             DNA SEQUENCE ANALYSIS",
        "=" * 44,
        f"Sequence: {results['sequence']}",
        f"Length:   {results['length']} bp",
        "",
        "NUCLEOTIDE COUNTS",
        "-" * 44,
    ]

    for base, count in counts.items():
        percentage = (count / results["length"]) * 100
        lines.append(f"  {base}: {count:>6} ({percentage:6.2f}%)")

    lines.extend(
        [
            "",
            "BASE COMPOSITION",
            "-" * 44,
            f"  GC content: {results['gc_content']:.2f}%",
            f"  AT content: {results['at_content']:.2f}%",
            "",
            "STRAND OPERATIONS",
            "-" * 44,
            f"  Complement:         {results['complement']}",
            f"  Reverse complement: {results['reverse_complement']}",
            "=" * 44,
            "",
            "Note: These are sequence-level calculations, not a prediction",
            "of gene function, disease risk, or clinical significance.",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Perform basic analysis of a standard DNA sequence."
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument(
        "-s", "--sequence",
        help="DNA sequence to analyze (A, T, G, and C only).",
    )
    source.add_argument(
        "-f", "--file",
        help="Text file containing one DNA sequence.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.sequence is not None:
            raw_sequence = args.sequence
        elif args.file is not None:
            raw_sequence = read_sequence_file(args.file)
        else:
            raw_sequence = input("Enter a DNA sequence: ")

        results = analyze_sequence(raw_sequence)
        print(format_report(results))
        return 0

    except (ValueError, TypeError) as error:
        parser.exit(status=2, message=f"Error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
