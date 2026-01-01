# Known Issues, Limitations & Future Improvements

This document tracks known limitations, design trade-offs, and potential future enhancements for the Knit Converter project.  
All items below reflect real-world constraints encountered when working with PDF → DOCX → PDF conversions.  

---

## Known Limitations

### 1. Formatting Fidelity in PDF-Derived Documents

PDF files do not contain semantic structure (e.g. “this is a heading”), only positioned text and graphics.
As a result, converting PDFs to Word documents can fragment text into multiple runs with differing styles.

**Impact**:
- Some headings or subheadings may have mixed formatting internally
- Replacing text across these runs can cause partial styling (e.g. only part of a word retaining heading colour/size)

**Mitigation (current approach)**:
- The script intentionally skips headings and mixed-format paragraphs
- This preserves layout and images at the cost of occasionally missing replacements in layout-critical text

This trade-off prioritises visual stability over aggressive text replacement.

---

### 2. Line Spacing and Layout Reflow

After modifying text in a Word document, Microsoft Word may recompute layout, resulting in:
- Increased line spacing
- Additional blank space
- Extra pages when converting back to PDF

**Mitigation (current approach)**:
- Paragraph and style-level spacing is normalised where possible
- Formatting-sensitive content (headings, mixed-format paragraphs) is excluded from modification

Despite this, some layout changes are unavoidable due to third-party conversion behaviour.

---

### 3. Tables and Text Boxes

Some PDF conversions represent content as:
- Tables
- Floating text boxes
- Positioned frames

These structures are only partially accessible via python-docx, and spacing or overflow issues may still occur in these cases.

**Mitigation**:

- Table cell paragraphs are processed explicitly
- Text boxes are treated conservatively (often skipped) to avoid layout corruption

---

### 4. Ambiguous Terminology

Very short knitting abbreviations (e.g. two-letter terms) can be ambiguous depending on context.
Plus, certain terms used to describe yarn weight i.e. "sock" or "sport" may be interpreted incorrectly.

Current handling:
- Longer, unambiguous terms are prioritised
- Some shorter, more ambiguous terms are included cautiously and documented as potentially problematic

Users may choose to adjust the terminology dictionary based on their specific patterns.

---

## Intentional Design Decisions

- **Images are prioritised over perfect text formatting**  
  Images are critical for understanding knitting patterns and are never modified or removed.

- **Pure text replacement logic is isolated and unit tested**  
  Core term replacement is implemented as a pure function and covered by unit tests.

- **Safety over completeness**  
  When formatting stability is at risk, the script prefers skipping replacements rather than producing visually corrupted output.

These decisions are deliberate and documented.

---

## Future Improvements (Non-Goals for Current Version)

The following ideas are intentionally out of scope for the current implementation but could be explored in future iterations:

- Optional GUI for selecting input/output directories
- Visual regression testing (PDF image comparison)
- More granular replacement rules for headings
- User-configurable “safe mode” vs “aggressive mode”
- External configuration files for terminology sets

None of these are required for the current project goals.

---

## Summary

Knit Converter is designed as a best-effort automation tool operating within the constraints of PDF conversion technologies.

Known limitations are:
- Understood
- Mitigated where practical
- Documented transparently

This reflects a realistic, production-minded approach rather than an attempt to achieve impossible formatting fidelity.