# Country Scramble
# Picks a country from the countries database, scrambles it, and asks the user
# to unscramble it

from tkinter import *
from country_scramble.country_getter import CountryGetter
from country_scramble.country_scrambler import CountryScrambler


class Application(Frame):
    """A GUI Application for unscrambling a country"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.the_country = CountryGetter.get_country()
        self.scrambled = CountryScrambler.scrambled_country()
        self.guess_ent = Entry(self)
        self.results = None
        self.tries = 1
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Welcome to Country Scramble"
              ).grid(row=0, column=0, columnspan=2, sticky=W+E+N+S)
        Label(self,
              text="Try to guess the country in as few tries as possible."
              ).grid(row=1, column=0, columnspan=2, sticky=W+E+N+S)
        Label(self,
              text=scrambled_country()
              ).grid(row=2, column=2, columnspan=1, sticky=W+E+N+S)
        Label(self,
              text="What is your guess?: "
              ).grid(row=3, column=0, sticky=W)
        self.guess_ent.grid(row=3, column=1, sticky=W)
        Button(self,
               text="Submit Guess",
               command=self.guessing
               ).grid(row=4, column=0, sticky=W)
        root.bind("<Return>", self.guessing)
        self.results = Label(self, text="")
        self.results.grid(row=5, column=0, sticky=W+E+N+S)

    def guessing(self, event=None):
        if self.guess_ent.get() != '':
            guess = str(self.guess_ent.get())
            if guess != self.the_country:
                self.results.config(text="Sorry try again")
                self.guess_ent.delete(0, END)
            else:
                self.results.config(
                    text="Congratulations, you guessed the country. It was: "
                         "{}, and it only took you {}, tries!"
                         .format(self.the_country, self.tries)
                )
            self.tries += 1
            if self.tries >= 10:
                self.results.config(text="I'm sorry you were not able to "
                                         "guess the country in the "
                                         "appropriate amount of tries. The "
                                         "country was: {}"
                                         .format(self.the_country))


# main
root = Tk()
root.title("Country Scramble")
app = Application(root)
root.mainloop()
