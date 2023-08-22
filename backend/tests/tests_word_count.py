import pytest
from app.internal.word_count import word_count_regex


@pytest.mark.parametrize(
    "input_text, expected_count",
    [
        ("Hello World", 2),
        ("", 0),
        ("One two three four five", 5),
        ("Special characters !@#$%^&*() do not count", 5),
        ("Hyphenated-words and apostrophes' count as one", 7),
    ],
)
def test_word_count_regex(input_text, expected_count):
    assert word_count_regex(input_text) == expected_count
