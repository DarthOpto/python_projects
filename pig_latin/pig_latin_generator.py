"""
A pig latin generator.
Take input of a word or phrase from a user then -
If a word begins with a consonant, then move that consonant to the end and add
"ay".
If the word begins with a vowel, add "way" to the end.
"""
import string

VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
              'y', 'z']

PIG_LATIN = []
PHRASE = input('What word would you like to turn into Pig Latin: ').lower()
WORD_LIST = list(PHRASE.translate(str.maketrans('', '', string.punctuation))
                 .split())

for item in WORD_LIST:
    if item[0] in VOWELS:
        PIG_LATIN.append(item + 'way')
    else:
        new_word = item.replace(item[0], "")
        PIG_LATIN.append(new_word + item[0] + "ay")

print(' '.join(PIG_LATIN))
