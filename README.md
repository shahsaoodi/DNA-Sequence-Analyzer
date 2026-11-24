# DNA Sequence Analyzer

A small Python project for exploring the basics of DNA sequence analysis.

I built this project to connect the Python programming concepts I have been
learning with practical bioinformatics. The first version focuses on a few
fundamental operations: checking a DNA sequence, counting its bases, measuring
GC and AT content, and generating complementary sequences.

The aim is to keep the code readable and testable. I want to understand the
algorithms rather than hide the biology behind a library.

## What it can do

- Validate a DNA sequence containing the standard bases `A`, `T`, `G`, and `C`.
- Accept lowercase input and remove whitespace, including spaces and newlines.
- Count each nucleotide.
- Calculate GC and AT percentages.
- Generate the complementary DNA strand.
- Generate the reverse complement.
- Read a single DNA sequence from a plain-text file.
- Print a readable report in the terminal.

**Current scope:** this is an educational Stage 1 project. It does not yet
translate DNA into protein, identify genes, detect variants, or make medical
predictions. Those would require additional algorithms, biological context,
careful validation, and appropriate datasets.

## Example

Input:

```text
ATGCGATCGTAGCTAG
```

Example output (abbreviated):

```text
DNA SEQUENCE ANALYSIS
Sequence length: 16 bp

Nucleotide counts:
  A: 4
  T: 4
  G: 5
  C: 3

GC content: 50.00%
AT content: 50.00%

Complement:         TACGCTAGCATCGATC
Reverse complement: CTAGCTACGATCGCAT
```

The output is calculated from the input sequence. It is not a biological
interpretation of what the sequence does.

## Requirements

- Python 3.10 or newer
- No third-party package is needed to run the application.
- `pytest` is used for development tests.

Check your Python installation:

```bash
python --version
```

On some systems, use `python3` instead of `python`.

## Set up the project

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/dna-sequence-analyzer.git
cd dna-sequence-analyzer
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

**Linux, macOS, or WSL:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and its test dependency:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the analyzer

Analyze a sequence directly:

```bash
dna-analyzer --sequence ATGCGATCGTAGCTAG
```

Or use Python without installing the command:

```bash
python -m dna_analyzer --sequence ATGCGATCGTAGCTAG
```

Analyze a sequence stored in a text file:

```bash
dna-analyzer --file examples/sample_dna.txt
```

Start interactive mode:

```bash
dna-analyzer
```

The file option expects one sequence made of the standard DNA letters. FASTA
headers are not supported yet; FASTA parsing is planned for a later version.

## Run the tests

```bash
python -m pytest
```

The tests cover valid and invalid input, whitespace handling, nucleotide
counts, composition percentages, and complementary-strand operations.

## Project layout

```text
dna-sequence-analyzer/
├── examples/
│   └── sample_dna.txt
├── src/
│   └── dna_analyzer/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analysis.py
│       └── cli.py
├── tests/
│   └── test_analysis.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## A note about the biology

DNA strands are complementary: A pairs with T, and G pairs with C. The
complement function returns the matching bases in the same left-to-right
position order. The reverse-complement function reverses that result to
represent the opposite strand in the usual 5' to 3' orientation.

GC content is the percentage of bases that are either G or C:

`GC percentage = (count(G) + count(C)) / sequence length * 100`

For standard DNA containing only A, T, G, and C, AT percentage is the
percentage of A and T bases. GC and AT percentages should add up to 100%.

GC content alone does not tell us whether a sequence is a gene, what protein
it encodes, or whether it is associated with a disease.

## Development roadmap

Possible next steps, to be added and tested one at a time:

1. Support IUPAC ambiguity codes such as `N`, `R`, and `Y`.
2. Read multi-record FASTA files.
3. Transcribe DNA to RNA.
4. Translate RNA codons into amino acids.
5. Find open reading frames (ORFs).
6. Add visual summaries and downloadable reports.
7. Compare selected results with established bioinformatics tools such as
   Biopython.

## Contributing

This is a learning project. Suggestions, bug reports, and clear explanations
of biological edge cases are welcome. Please include a reproducible example
when reporting an issue.

## License

MIT. See [LICENSE](LICENSE).
