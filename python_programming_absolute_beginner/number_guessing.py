# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets the player know
# if the guess is too high, too low or right on the money

from random import randint

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Set the initial values
the_number = randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# Guessing the loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1

    if tries >= 10:
        print("I'm sorry you couldn't guess the number in an appropriate "
              "number of tries.")
        exit()

# Congratulate the player
print("You guessed it! The Number I was think of was: {}.".format(the_number))
print("And it only took you {}, tries!".format(tries))
input("\n\nPress the ENTER key to exit.")
