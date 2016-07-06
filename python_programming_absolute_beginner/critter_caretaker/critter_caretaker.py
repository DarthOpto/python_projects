# Critter Caretaker
# A virtual pet to care for
# TODO: Add if pet hunger gets less than zero pet dies
# TODO: Add if pet boredom gets less than zero pet's anger is berserker level


class Critter(object):
    """A virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.unhappiness = None

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: {}\n".format(self.name)
        rep += "hunger: {}\n".format(self.hunger)
        rep += "boredom: {}\n".format(self.boredom)
        rep += "mood: {}\n".format(self.mood)
        return rep

    @property
    def mood(self):
        self.unhappiness = self.hunger + self.boredom
        if self.unhappiness < 5:
            mood = "happy"
        elif 5 <= self.unhappiness <= 10:
            mood = "okay"
        elif 11 <= self.unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "mad"
        return mood

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Brrruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Whee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    critter_name = input("What do you want to name your critter?: ")
    critter = Critter(critter_name)

    choice = None
    while choice != 0:
        print \
            ("""
            Critter Caretaker:

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)

        choice = int(input("Choice: "))
        print()

        # exit
        if choice == 0:
            print("Good-bye")

        # listen to your critter
        elif choice == 1:
            critter.talk()

        # feed your critter
        elif choice == 2:
            food = int(input("How much would you like to feed your pet?: "))
            critter.eat(food=food)

        # play with your critter
        elif choice == 3:
            fun = int(
                input("How much would you like to play with your pet?: "))
            critter.play(fun=fun)

        # Backdoor
        elif choice == 1337:
            print(critter)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid option.")


main()
input("\n\nPress the ENTER key to exit.")

