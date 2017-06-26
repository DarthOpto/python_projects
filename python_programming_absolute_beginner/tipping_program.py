"""
Gets the restaurant total from the user and the calculates a 15 percent and a 20
percent tip for the nice waitress.
"""

restaurant_total = float(input("\nGreetings User, please enter the total "\
                                   "bill: "))

# Calculate the 15% tip
ten_percent = restaurant_total * .10
half_ten_percent = ten_percent * .50
fifteen_percent = ten_percent + half_ten_percent

print("\nYour fifteen percent tip would be: {0:.2f}"
      .format(float(fifteen_percent)))

# Calculate the 20% tip
twenty_percent = ten_percent * 2

print("\nYour twenty percent tip if you were generous Dave would be: {0:.2f}"
      .format(float(twenty_percent)))

raw_input("\n\nPress the ENTER key to exit the program")
