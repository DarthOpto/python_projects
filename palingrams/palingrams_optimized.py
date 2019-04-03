"""
Find all word-pair palingrams in a dictionary file
"""
import time
import load_dictionary

start_time = time.time()
word_list = load_dictionary.load('words.txt')


def find_palingrams():
    """
    Find dictionary palingrams
    :return: a list of word-pairs which are palindromes
    """

    palingram_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = ''.join(reversed(word))
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    palingram_list.append((word, rev_word[end-i:]))
                if word[i:] == rev_word[end-i:] and rev_word[:end-i] in words:
                    palingram_list.append((rev_word[:end-i], word))
    return palingram_list


palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

print("\nNumber of palingrams = {}".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print('{} {}'.format(first, second))

end_time = time.time()
print('Run time for this program was {} seconds'.format(end_time - start_time))