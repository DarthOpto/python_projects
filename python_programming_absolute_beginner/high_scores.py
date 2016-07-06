# High Scores
# Demonstrates list methods

scores = []
choice = None

while choice != 0:
    print("""
            High Scores

            0 - Exit
            1 - Show Scores
            2 - Add a Score
            3 - Delete a Score
            4 - Sort Scores
    """)
    choice = int(input("Please enter a choice: "))
    print()

# Exit the program
if choice == 0:
    print("Good-bye.")
    exit()

# list the high score table
elif choice == 1:
    print("High Scores")
    for score in scores:
        print(score)

# adding a score
elif choice == 2:
    score = int(input("What score did you get?: "))
    scores.append(score)

# remove a score
elif choice == 3:
    score = int(input("Which score would you like to remove?: "))
    if score in scores:
        scores.remove(score)
    else:
        print(score, "isn't in the high scores list.")

# sort the scores
elif choice == 4:
    scores.sort(reverse=True)

# Handle an invalid choice
# some unknown choice
else:
    print("Sorry, but", choice, "isn't a valid choice.")
