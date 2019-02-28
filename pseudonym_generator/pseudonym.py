"""Generate side kick names"""

import sys
import random

print("Welcome to the Psych 'Sidekick Name Picker'. \n")
print("A name just like Sean would pick for Gus: \n\n")

FIRST = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'")

LAST = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom')

while True:
    FIRST_NAME = random.choice(FIRST)

    LAST_NAME = random.choice(LAST)

    print('\n\n')
    print('{} {}'.format(FIRST_NAME, LAST_NAME), file=sys.stderr)
    print('\n\n')

    TRY_AGAIN = input('\n\nTry again? (Press ENTER else n to quit)\n')
    if TRY_AGAIN.lower() == 'n':
        break

input("\nPress ENTER to exit")
