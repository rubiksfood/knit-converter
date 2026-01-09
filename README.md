# knit-converter

![tests](../../actions/workflows/tests.yml/badge.svg)

## Overview

**knit-converter** is a Python utility that converts US knitting terminology to its UK equivalent in PDF knitting patterns.

The project was designed with a quality-first mindset: the core text-processing logic is isolated, unit tested, and validated independently of file conversion. Particular attention is paid to risk management, edge cases, and known limitations introduced by PDF → DOCX → PDF workflows.

While the tool is fully functional, the project’s primary focus is **correctness, testability, and transparent handling of imperfect inputs**, rather than achieving perfect formatting fidelity.

---

## Problem Context

PDF knitting patterns are often:
- inconsistently formatted
- visually complex
- difficult to edit safely

Knitting patterns written for a US audience often use terminology that differs from UK standards (e.g. “bind off” vs “cast off”).  
These differences can introduce cognitive overhead and increase the risk of user error.  

Manually converting patterns is time-consuming and error-prone - especially across multiple files.  

---

## Solution

This script takes a defensive approach:
1. Converts PDF knitting patterns into Word documents
2. Replaces US knitting terms with their UK equivalents using a configurable dictionary
3. Skips formatting-sensitive content where modification risks corruption
4. Converts the edited documents back into PDFs
5. Processes multiple files in batch via a CLI, reporting successes, skips, and failures

The core terminology replacement logic is implemented as a pure, unit-tested function, making the behaviour easy to verify independently of file conversion.

---

## Project Structure
```
knit_converter/
├── knit_converter.py        # CLI entry point (argparse)
├── file_conversion.py       # PDF <-> DOCX conversion logic
├── heading_safe.py          # Skips headers & mixed-format paragraphs
├── term_conversion.py       # Applies text processing to Word documents
├── text_processing.py       # Pure, unit-tested text replacement logic
├── terminology.py           # US → UK knitting terminology dictionary
├── test_text_processing.py  # Unit tests for text processing
├── README.md
└── issues-features.md
```

## Quality & Testing Focus

### Unit Testing  

Unit tests validate:
- correct term replacement
- word boundary handling
- overlapping terms
- case handling (lowercase, sentence case, acronyms)
- regression scenarios discovered during development

Tests target pure logic, avoiding brittle file-based tests.

Run tests with:  
```
pytest
```

### Risk-based Decisions

To prevent visual corruption:
- headings and mixed-format paragraphs are intentionally skipped
- images are never modified
- ambiguous abbreviations are treated cautiously

These decisions prioritise output stability over aggressive automation.

---

## Technologies Used
- Python
- pdf2docx
- docx2pdf
- python-docx
- pytest (unit testing)
- Standard library: argparse, pathlib, re

---

## Installation

### 1. Clone the repository
### 2. Create & activate a virtual environment
```
python -m venv .venv
```
**Windows**  
```
.venv\Scripts\activate
```
**macOS / Linux**  
```
source .venv/bin/activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

Basic usage:
```
python knit_converter.py --input ./US_patterns --output ./GB_patterns
```

Options:
```
python knit_converter.py --help
```

Common flags:
- --skip-existing – skip PDFs that have already been converted
- --keep-docx – keep intermediate .docx files for debugging
- --prefix – customise the output filename prefix (default: gb_)

---

## Known Limitations

PDF conversion introduces unavoidable constraints:

- formatting may vary by source document
- headings may remain unchanged
- some layout reflow can occur

Limitations, mitigations, and trade-offs are documented in [`QUALITY_AND_LIMITATIONS.md`](./QUALITY_AND_LIMITATIONS.md)

---

## Future Improvements

- Improved preservation of formatted text
- Optional GUI or richer CLI options
- Expanded automated test coverage
- Configurable terminology via external data files

---

## Why This Project Matters (QA Perspective)

This project demonstrates:
- risk-based decision making
- separation of testable logic from I/O
- clear defect boundaries and documented limitations
- realistic handling of third-party tool behaviour
- automation built with verification in mind

It reflects how real systems are **tested and stabilised**, not how ideal systems are imagined.