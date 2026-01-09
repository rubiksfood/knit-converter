# Quality and Limitations

This document records identified risks, known limitations, and intentional quality decisions made during development of knit-converter.  
The goal is not to eliminate all defects, but to understand, mitigate, and document them.  

---

## Known Limitations

## 1. PDF-Derived Formatting Fragmentation

### Risk

PDFs lack semantic structure. During PDF → DOCX conversion:  
- text may be split across multiple runs
- headings may use mixed formatting
- layout metadata may be lost

### Impact

Uncontrolled text replacement can:
- apply styles partially
- shift alignment
- corrupt headings

### Mitigation

- Headings and mixed-format paragraphs are skipped
- Replacement is limited to paragraphs with stable formatting
- Images are never modified

This reduces replacement coverage but significantly improves output stability.  

---

## 2. Line Spacing and Layout Reflow

### Risk

Word may recalculate spacing after edits, causing:
- increased line spacing
- blank pages
- content overflow

### Mitigation
- Paragraph and style-level spacing is normalised where possible
- High-risk content is excluded from modification

Residual layout issues are treated as acceptable given third-party constraints.  

---

### 3. Tables & Text Boxes

### Risk

Some PDF conversions store text inside tables or floating containers, which are only partially accessible via python-docx.  

### Mitigation
- Table cell paragraphs are processed explicitly
- Floating text boxes are treated conservatively or skipped

---

### 4. Ambiguous Terminology

### Risk

Short abbreviations and yarn weight terms can be context-dependent.  

### Mitigation
- Longer, explicit terms are prioritised
- Ambiguous terms are included selectively and documented
- Terminology is configurable and test-backed

---

## Intentional Quality Decisions

- Safety over completeness
- Image preservation over formatting changes
- Tested logic over brittle end-to-end assertions
- Documentation over silent failure

These are deliberate QA-driven choices.

---

## Future Improvements (Not Current Goals)

The following ideas are intentionally out of scope for the current implementation but could be explored in future iterations:

- Visual regression testing (PDF image comparison)
- User-configurable “safe mode” vs “aggressive mode”
- Expanded test coverage
- External terminology configuration
- Optional GUI for selecting input/output directories

---

## Summary

Knit Converter is a best-effort automation tool developed with a quality-engineering mindset.

Limitations are:
- identified
- mitigated where practical
- documented transparently

This reflects real-world testing and automation work, not idealised tooling.