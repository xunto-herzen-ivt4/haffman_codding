from collections import Counter
import math


def encode(text: str):
    # Generate codes for letters in sentence
    codes = {}

    letters = Counter(text).most_common()
    stack = []
    for letter, frequency in letters:
        codes[letter] = []
        stack.append((letter, frequency/len(text)))

    while len(stack) > 1:
        first, first_probability = stack.pop()
        second, second_probability = stack.pop()

        for letter in first:
            codes[letter].insert(0, 0)

        for letter in second:
            codes[letter].insert(0, 1)

        stack.append((first + second, first_probability + second_probability))
        stack.sort(key=lambda item: item[1], reverse=True)

    # Encode phrase
    result = []
    for letter in text:
        result += codes[letter]

    return codes, result


def decode(codes: dict, encoded_text: list):
    result = ""
    i = 0
    while len(encoded_text) >= i:
        for letter, code in codes.items():
            if encoded_text[:i] == code:
                encoded_text = encoded_text[i:]
                result += letter
                i = 0
        i += 1
    return result
