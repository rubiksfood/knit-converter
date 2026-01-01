import re
from typing import Dict


def apply_case_from_match(original: str, replacement: str) -> str:
    if not original:
        return replacement
    
    # Handle acronyms in the replaced term
    if replacement.isupper():
        return replacement

    # Handle acronyms in the original term (that are not acronyms in the replaced term)
    if original.isupper():
        return replacement.lower()

    # Handle phrase/sentence case (covers "Yarn over" at start of a sentence, etc.)
    if original[0].isupper():
        return replacement[:1].upper() + replacement[1:]

    return replacement


def replace_terms_in_text(text: str, terms: Dict[str, str]) -> str:
    if not text or not terms:
        return text

    # Sort longest-first to reduce overlaps (e.g., "light worsted" vs "worsted")
    items = sorted(terms.items(), key=lambda kv: len(kv[0]), reverse=True)

    result = text
    for src, dst in items:
        # Word boundary on both sides to prevent partial matches.
        # Note: This may not match terms with punctuation directly next to them.
        pattern = re.compile(r"\b" + re.escape(src) + r"\b", re.IGNORECASE)

        def _repl(m: re.Match) -> str:
            original = m.group(0)
            return apply_case_from_match(original, dst)

        result = pattern.sub(_repl, result)

    return result