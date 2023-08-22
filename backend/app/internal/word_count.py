import re


def word_count_regex(text: str) -> int:
    return len(re.findall(r"\w+", text))
