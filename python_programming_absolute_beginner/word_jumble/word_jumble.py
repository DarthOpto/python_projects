# Word Jumble
#
# The computer picks a random word and then jumbles it.
# The player must guess the original word

from random import choice, randrange

# Create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

HINTS = {"python": "a snake",
         "jumble": "a mess",
         "easy": "something simple is...",
         "difficult": "something hard is...",
         "answer": "question...",
         "xylophone": "a musical instrument that starts with an 'x'"
         }

# Choose a random word from the WORDS tuple
word = choice(WORDS)
# Get the hint for the jumbled word
hint = HINTS.get(word)
# Count the guesses
guess_count = 1


# Create a variable to use later to see if the guess is correct
correct = word

# Create a jumbled version of the word
jumbled = ""

while word:
    position = randrange(len(word))
    jumbled += word[position]
    word = word[:position] + word[(position + 1):]

# Start the game
print("""
                  Welcome to Word Jumble!
          Unscramble the letters to make a word.
       (Press the ENTER key at the prompt to quit.)
      """)

print("The jumbled word is: {}".format(jumbled))

# Getting the player's guess
wrong_guess_msg = "Sorry that was not correct. Try again."
while True:
    guess = input("\nYour guess: ")
    guess_count += 1
    if guess == correct:
        print("That's It! You guessed it!\n")
        break
    else:
        print(wrong_guess_msg)

print("Thanks for playing")
input("\n\nPress the ENTER key to exit.")
