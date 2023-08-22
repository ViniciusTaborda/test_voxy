import re


def word_count_regex(text: str) -> int:
    return len(re.findall(r"\w+", text))


def word_count_split(text: str) -> int:
    words_list = re.split(r"\W+", text)
    return len([word for word in words_list if word != ""])


def word_count_stack(text: str) -> int:
    stack = []
    word_count = 0

    text = text.strip()

    if text.isalnum():
        return 1

    for i, char in enumerate(text):
        if stack:
            if not stack[-1].isalnum() and char.isalnum():
                word_count += 1
            elif i + 1 < len(text):
                if char.isalnum() and not text[i + 1].isalnum():
                    word_count += 1

        stack.append(char)

    return word_count


def word_count_loop(text: str) -> int:
    count = 0
    in_word = False

    for char in text:
        if char.isalnum():
            in_word = True
        elif in_word:
            count += 1
            in_word = False

    if in_word:
        count += 1

    return count
