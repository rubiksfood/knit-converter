from text_processing import replace_terms_in_text

TERMS = {
    "bind": "cast",
    "gauge": "tension",
    "C4R": "C4B",
    "seed stitch": "moss stitch",
    "YO": "yarn over needle",
    "light worsted": "DK",
    "worsted": "aran",
}

def test_replaces_basic_term():
    assert replace_terms_in_text("Ensure you bind off at end.", TERMS) == "Ensure you cast off at end."

def test_word_boundaries_prevent_partial_matches():
    # "engauge" should not match "gauge"
    assert replace_terms_in_text("engauge is not a word", TERMS) == "engauge is not a word"

def test_case_all_caps():
    assert replace_terms_in_text("C4R", TERMS) == "C4B"

def test_case_title():
    assert replace_terms_in_text("Gauge matters.", TERMS) == "Tension matters."

def test_multi_word_phrase_capitalisation():
    assert replace_terms_in_text("Seed stitch the next row.", TERMS) == "Moss stitch the next row."

def test_acronym_replacement_forces_uppercase():
    assert replace_terms_in_text("light worsted yarn", TERMS) == "DK yarn"

def test_uppercase_acronym_to_lowercase_phrase():
    assert replace_terms_in_text("YO x2", TERMS) == "yarn over needle x2"

def test_longer_terms_win_over_shorter_terms():
    # "light worsted" is longer than "worsted", so it should be replaced first
    assert replace_terms_in_text("Use worsted yarn, not light worsted yarn.", TERMS) == "Use aran yarn, not DK yarn."

def test_no_terms_or_empty_text():
    assert replace_terms_in_text("", TERMS) == ""
    assert replace_terms_in_text("Hello", {}) == "Hello"