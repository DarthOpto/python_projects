"""
Load a text file as a list

Arguments:
    - words.txt

Exceptions:
    - IOError if filename not found

Returns:
    - A list of words in a text file in lower case

Requires:
- import sys
"""

import sys


def load(file):
    """
    Open a text file and return a list of lowercase strings
    :param file: words.txt
    :return: a list of words in lower case
    """

    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print('{}\n Error opening {}. Terminating program.'.format(e, file), file=sys.stderr)
        sys.exit(1)


