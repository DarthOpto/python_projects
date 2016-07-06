"""
Create a program that prints a list of words in random order.
The program should print all the words and not repeat any.
"""
from random import shuffle

WORDS = ["consider", "minute", "accord", "evident", "practice", "intend",
         "concern"]

shuffle(WORDS)
print(*WORDS)
