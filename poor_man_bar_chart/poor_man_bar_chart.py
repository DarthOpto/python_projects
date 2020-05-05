import pprint
from collections import defaultdict
import string

SENTENCE = input("Enter the text you would like to analyze: ").lower()
TRANSLATOR1 = str.maketrans('', '', string.punctuation)
TRANSLATOR2 = str.maketrans('', '', string.whitespace)
WITHOUT_PUNCT = SENTENCE.translate(TRANSLATOR1)
WITHOUT_WHITESPACE = WITHOUT_PUNCT.translate(TRANSLATOR2)

s = list(WITHOUT_WHITESPACE)
d = defaultdict(list)
pp = pprint.PrettyPrinter()

for k in s:
    d[k].append(k)


x = sorted(d.items())
pp.pprint(x)