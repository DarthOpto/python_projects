"""
Poor Man's Bar Chart:

Take any text and display the number of instances of each letter.
"""
import pprint
from collections import defaultdict
from string import ascii_lowercase

SENTENCE = input("Enter the text you would like to analyze: ").lower()

d = defaultdict(list)
pp = pprint.PrettyPrinter()

for letter in SENTENCE:
    if letter in ascii_lowercase:
        d[letter].append(letter)

x = sorted(d.items())
pp.pprint(x)

