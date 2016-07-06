# Craps Roller
# Demonstrates random number generation

from random import randint, randrange

# generate random numbers 1-6
die1 = randint(1, 6)
die2 = randrange(6) + 1

total = die1 + die2

print("You rolled a: {0:d}, and a: {1:d}, for a total of: {2:d}"
      .format(die1, die2, total))

raw_input("\n\nPress the ENTER key to exit")
