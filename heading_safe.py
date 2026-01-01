from typing import Dict, Callable, Optional, Tuple
from docx.text.paragraph import Paragraph
from docx.text.run import Run


def _run_style_signature(run: Run) -> Tuple[Optional[float], Optional[bool], Optional[str]]:
    # Includes only a few attributes to keep the heuristic simple and stable.

    size = None
    try:
        if run.font.size:
            size = float(run.font.size.pt)
    except Exception:
        size = None

    bold = None
    try:
        bold = run.bold
    except Exception:
        bold = None

    color = None
    try:
        if run.font.color and run.font.color.rgb:
            color = str(run.font.color.rgb)
    except Exception:
        color = None

    return (size, bold, color)


def paragraph_has_mixed_formatting(paragraph: Paragraph) -> bool:
    # Returns True if a paragraph contains multiple distinct run style signatures.
    # PDF->DOCX conversions often fragment headings/subheadings into many runs.

    sigs = set()
    for run in paragraph.runs:
        if not run.text:
            continue
        sigs.add(_run_style_signature(run))
        if len(sigs) > 1:
            return True
    return False


def is_heading_paragraph(paragraph: Paragraph) -> bool:
    # Heuristic: style-based headings (works for normal DOCX).

    try:
        style_name = (paragraph.style.name or "").lower()
    except Exception:
        style_name = ""
    return "heading" in style_name or style_name.startswith("title")


def replace_terms_heading_safe(
    paragraph: Paragraph,
    terms: Dict[str, str],
    replace_cross_run_fn: Callable[[Paragraph, Dict[str, str]], bool],
) -> bool:
    
    # Heading-safe replacement:
    # - Skip paragraphs styled as headings/titles
    # - Skip paragraphs with mixed run formatting (common for PDF-derived headings/subheadings)
    #   because cross-run replacement is likely to break formatting or split styling.
    # - Otherwise, perform a normal cross-run replacement.

    if is_heading_paragraph(paragraph):
        return False

    # Prevents subheading replacements that cause styling splits.
    if paragraph_has_mixed_formatting(paragraph):
        return False

    return replace_cross_run_fn(paragraph, terms)