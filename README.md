# knit-converter
## Overview

**knit-converter** is a Python utility that converts US knitting terminology to its UK equivalent in PDF knitting patterns.

The project was built to solve a real-world problem and is intentionally designed as a small, maintainable automation tool rather than a full application. It focuses on clean separation of concerns, testable text-processing logic, and pragmatic handling of imperfect PDF formats.

---

## Problem Statement

Knitting patterns written for a US audience often use terminology that differs from UK standards (e.g. “bind off” vs “cast off”).  
For knitters following complex patterns, these differences can cause confusion, mistakes and frustration.  

Manually converting patterns is time-consuming and error-prone — especially across multiple files.  


---

## Solution

This script:
1. Converts PDF knitting patterns into editable Word documents
2. Replaces US knitting terms with their UK equivalents using a configurable dictionary
3. Converts the edited documents back into PDFs
4. Processes multiple files in batch via a simple command-line interface

The core terminology replacement logic is implemented as a pure, unit-tested function, making the behaviour easy to verify independently of file conversion.

---

## Project Structure
```
knit_converter/
├── knit_converter.py        # CLI entry point (argparse)
├── file_conversion.py       # PDF <-> DOCX conversion logic
├── heading_safe.py          # Avoids modifying headers & paragraphs with mixed formatting
├── term_conversion.py       # Applies text processing to Word documents
├── text_processing.py       # Pure, testable text replacement logic
├── terminology.py           # US → UK knitting terminology dictionary
├── test_text_processing.py  # Unit tests for text processing
├── README.md
└── issues-features.md
```

## Key Design Choices
- **Separation of concerns**  
  File conversion, text processing, and domain terminology are isolated from each other.  

- **Testable core logic**  
  Terminology replacement is implemented as a pure function operating on plain strings, allowing unit tests without relying on PDF or Word libraries.  

- **Minimal CLI interface**  
  The script uses argparse for usability without introducing unnecessary complexity.  

- **Explicit trade-offs**  
  Image preservation was prioritised over perfect text formatting due to PDF conversion constraints.  

---

## Technologies Used
- **Python**
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

## Testing

Unit tests cover the core text replacement logic, including:
- correct term replacement
- word-boundary safety
- case handling (uppercase, sentence case, lowercase)
- edge cases

Run tests with:
```
pytest
```

## Known Limitations

- PDF formatting quality varies depending on the source document
- Some PDFs may gain additional blank pages during conversion
- Very short abbreviations (e.g. two-letter terms) can be ambiguous
- PDF -> DOCX conversion can fragment formatting across runs
- Headings and mixed-format paragraphs are intentionally skipped to preserve layout. This means some terminology (e.g. subheadings like ‘Gauge’) may remain unchanged if modifying them risks layout corruption.

These limitations are documented transparently in issues-features.md.

---

## Future Improvements

- Improved preservation of formatted text
- Optional GUI or richer CLI options
- Expanded automated test coverage
- Configurable terminology via external data files

---

## Why This Project Matters

This project demonstrates:
- Practical Python scripting
- Clean modular design in a small codebase
- Test-driven handling of text transformation logic
- Realistic engagement with third-party library constraints
- Clear documentation and honest trade-off analysis

It was created for a real user (my mother) and reflects a **problem-driven development approach** rather than a tutorial exercise.