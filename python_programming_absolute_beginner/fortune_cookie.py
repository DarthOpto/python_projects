# Fortune Cookie
# The program will tell a player's fortune by picking one of five fortunes

from random import choice

fortunes = ["I hear and I forget. I see and I remember. I do and I understand.",
            "When it is obvious that the goals cannot be reached,"
            "don't adjust the goals, adjust the action steps.",
            "Life is really simple, but we insist on making it complicated.",
            "Everything has beauty, but not everyone sees it.",
            "He who knows all the answers has not been asked all the questions."]

# ask the user if he/she wants a fortune
question = input("Would you like your fortune read? Y/N: ")
if question == "Y":
    print("Your fortune is: {}".format(choice(fortunes)))
    input("\n\nPress the ENTER key to exit.")
else:
    print("Thank you for your time, have a blessed day.")
    input("\n\nPress the ENTER key to exit.")
