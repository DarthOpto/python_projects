# Simple Game
# Demonstrates importing modules

import random
from python_programming_absolute_beginner.chapter_9 import games

print("Welcome to the world's simplest game!\n")


again = None
while again != "n":
    num = games.ask_number(question="How many players? (2 - 5): ", low=2,
                           high=5)

    players = []

    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100) + 1
        player = games.Player(name=name, score=score)
        players.append(player)

    print("\nHere are the game results: ")
    for player in players:
        print(player)

    again = games.ask_yes_no(question="\nDo you want to play again? (y/n): ")

input("\n\nPress the ENTER key to exit")
