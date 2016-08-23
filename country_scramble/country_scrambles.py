# Country Scramble
# Picks a country from the countries database, scrambles it, and asks the user
# to unscramble it

from tkinter import *
from tkinter import messagebox
from country_scramble.country_getter import get_country


class Application(Frame):
    """A GUI Application for unscrambling a country"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.country = get_country()
        self.the_country = self.country[0]
        self.scrambled = self.country[1]
        self.grid()
        self.guess_ent = Entry(self)
        self.tries = 1
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Welcome to Country Scramble"
              ).grid(row=0, column=0, columnspan=2, sticky=W + E + N + S)
        Label(self,
              text="Try to guess the country in as few tries as possible."
              ).grid(row=1, column=0, columnspan=2, sticky=W + E + N + S)
        Label(self,
              text=self.scrambled
              ).grid(row=2, column=0, sticky=W + E + N + S)
        Label(self,
              text="What is your guess?: "
              ).grid(row=4, column=0, sticky=W)
        self.guess_ent.grid(row=5, column=0, sticky=W)
        Button(self,
               text="Submit Guess",
               command=self.guessing
               ).grid(row=6, column=0, sticky=W)
        root.bind("<Return>", self.guessing)

    def guessing(self, event=None):
        if self.guess_ent.get() != '':
            guess = str(self.guess_ent.get()).upper()
            if guess != self.the_country.upper():
                messagebox.showwarning(
                    "Continue?",
                    "Sorry that answer is not correct")
                self.guess_ent.delete(0, END)
            else:
                if messagebox.askyesno("Congratulations",
                                       "Would you like to try another?"):
                    self.new_game()
                else:
                    root.destroy()

    def new_game(self):
        country = get_country()
        self.the_country = country[0]
        self.scrambled = country[1]
        Label(self,
              text=self.scrambled
              ).grid(row=2, column=0, sticky=W + E + N + S)
        self.guess_ent.delete(0, END)





# main
root = Tk()
root.title("Country Scramble")
app = Application(root)
root.mainloop()
