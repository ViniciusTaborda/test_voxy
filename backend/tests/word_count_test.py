import pytest
from app.internal.word_count import (
    word_count_regex,
    word_count_split,
    word_count_stack,
    word_count_loop,
)


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


@pytest.mark.parametrize(
    "input_text, expected_count",
    [
        ("Hello world!", 2),
        ("", 0),
        ("One two three four five", 5),
        ("No special characters here", 4),
        ("Multiple     spaces", 2),
        ("Special! Characters? Here.", 3),
    ],
)
def test_word_count_split(input_text, expected_count):
    assert word_count_split(input_text) == expected_count


@pytest.mark.parametrize(
    "input_text, expected_count",
    [
        ("Hello World", 2),
        ("Hello    World", 2),
        ("", 0),
        ("OneWord", 1),
        ("Two  Words", 2),
        ("With\nNewlines", 2),
        ("With\tTabs", 2),
    ],
)
def test_word_count_stack(input_text, expected_count):
    assert word_count_stack(input_text) == expected_count


@pytest.mark.parametrize(
    "input_text, expected_count",
    [
        ("Hello World", 2),
        ("", 0),
        ("One two three four", 4),
        ("With special characters !@#$%^&*()", 3),
        ("SingleWord", 1),
        ("123 456 789", 3),
    ],
)
def test_word_count_loop(input_text, expected_count):
    assert word_count_loop(input_text) == expected_count
