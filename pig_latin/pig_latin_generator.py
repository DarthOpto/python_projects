"""Generate strings into Pig Latin"""
import string

VOWELS = {'a', 'e', 'i', 'o', 'u'}
CONSONANTS = set(string.ascii_letters).difference(VOWELS)


def pig_latinizer(word):
    """
    Takes a set of words and performs the pig latin translation
    :param word: a string of ASCII letters
    :return: words translated into Pig Latin
    """
    if word[0] in CONSONANTS:
        return word[1:] + word[0] + 'ay'

    return word + 'ay'


def process(grammatical_unit):
    """
    Processes the strings provided
    :param grammatical_unit: a string of words, usually a sentence
    :return: The translated string
    """
    translator = str.maketrans('', '', string.punctuation)
    without_punct = grammatical_unit.translate(translator)
    print(without_punct)
    translated = [pig_latinizer(word) for word in without_punct.split(' ')]
    return ' '.join(translated)


if __name__ == "__main__":
    SENTENCE = input("Enter the something you would like translated into pig Latin: ").lower()
    print('\n Your sentence: {}'.format(SENTENCE))
    print('Pig Latin Translation: {}'.format(process(SENTENCE)))
