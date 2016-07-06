"""
Useless Trivia

Gets personal information from the user and then prints true but useless
information about him or her
"""

name = raw_input("Hello there, please tell me your name so we can begin. ")
age = int(raw_input("And how old are you? "))
weight = int(raw_input("Okay, final question. How many pounds do you weigh? "))

# Display to the user what he/she would be called be poet EE Cummings in an email
# or if EE were angry
print("\nIf poet EE Cummings were to email you, he'd address you as {}"
     .format(name.lower()))
print("However, if EE were angry, he'd call you {}".format(name.upper()))

# Display to the User what he/she would be called by a child
called = name * 5
print("\nIf a small child were trying to get your attention , your name would " \
      "become: {}".format(called))

# Display the User's age in Seconds
seconds = age * 365 * 24 * 60 * 60
print("\nYou're over {}, seconds old! Wow, what were the dinosaurs like?"
     .format(seconds))

# Display to the User what their weight would be on the sun and moon
moon_weight = weight / 6
sun_weight = weight * 27.1

print("\nDid you know that on the moon you would weigh only {}, pounds"
     .format(moon_weight))

print("\nOn the Sun you would weigh: {} pounds, but not for long."
     .format(sun_weight))

raw_input("\n\nPress the ENTER key to exit the program")
