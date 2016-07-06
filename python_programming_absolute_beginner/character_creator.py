"""
The player should be given a pool of 30 points to spend on four attributes:
Strength, Health, Wisdom, and Dexterity. The player should be able to spend
points from the pool on any attribute and should also be able to take points
from an attribute and put them back into the pool.
"""
choice = None
pool = 30
attributes = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
while choice != 0:
    print(
            """
            Character Creator:
            Attribute Pool = {}
            Which Attribute would you like to change?
            1 - Add a Point
            2 - Delete a Point
            """.format(pool)
    )
    choice = int(input("Choice: "))
    print()

    if choice == 0:
        print("Good-bye")
    elif choice == 1:
        attribute = input("What attribute would you like me to increase? ")
        if attribute in attributes:
            points = int(input("How many points do you want to give {} "
                               .format(attribute)))
            attributes[attribute] += points
            pool -= points
            print("\n{} has been changed and now equals {}? "
                  .format(attribute, attributes.get(attribute)))
            print("\nYour attribute pool is now: {}".format(pool))
        else:
            print("\nThat attribute doesn't exist,"\
                  "maybe after some more training.")
    elif choice == 2:
        attribute = input("What attribute would you like me to decrease? ")
        if attribute in attributes:
            points = int(input(
                "How many points do you want me to remove from {}? "
                .format(attribute)))
            attributes[attribute] -= points
            pool += points
            print("\n{} has been changed and now equals {}"
                  .format(attribute, attributes.get(attribute)))
            print("\nYour attribute pool is now: {}".format(pool))
        else:
            print("\nThat attribute doesn't exist,"
                  "maybe after some more training.")
    else:
        print("\nSorry that is is an invalid choice. Good-bye")
