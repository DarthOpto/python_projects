"""
You are given a text, which contains different english letters and punctuation
symbols. You should find the most frequent letter in the text.
The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the
purpose of your search, "A" == "a". Make sure you do not count punctuation
symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the
letter which comes first in the latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each,
thus we choose "e".
Input: A text for analysis as a string (unicode for py2.7).
Output: The most frequent letter in lower case as a string.
Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
"""

import re
from collections import Counter


def checkio(text):
    lowered = text.lower()
    alpha_char = re.sub(r'[^a-z0-9]', '', lowered)
    counts = Counter(alpha_char)
    results = {k: v for (k, v) in counts.items() if v > 1}
    rev_multidict = {}
    for key, value in results.items():
        rev_multidict.setdefault(value, set()).add(key)

    if not results or \
            [key for key, values in rev_multidict.items() if len(values) > 1]:
        list_alpha = list(alpha_char)
        sorted_list = sorted(list_alpha)
        print(sorted_list)
        return sorted_list[0]
    else:
        return max(results.keys(), key=(lambda k: results[k]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio("Lorem ipsum dolor sit amet") == "m"
    # assert checkio("Hello World!") == "l", "Hello test"
    # assert checkio("How do you do?") == "o", "O is most wanted"
    # assert checkio("One") == "e", "All letter only once."
    # assert checkio("Oops!") == "o", "Don't forget about lower case."
    # assert checkio("AAaooo!!!!") == "a", "Only letters."
    # assert checkio("abe") == "a", "The First."
    # print("Start the long test")
    # assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    # print("The local tests are done.")
