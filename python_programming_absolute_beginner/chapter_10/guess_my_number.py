# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets the player know
# if the guess is too high, too low or right on the money

from tkinter import *
from random import randint


class Application(Frame):
    """ A GUI Application for a number guessing game """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.the_number = randint(1, 100)
        self.guess_ent = Entry(self)
        self.results = None
        self.tries = 1
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text="Welcome to 'Guess My Number'"
              ).grid(row=0, column=0, columnspan=2, sticky=W+E+N+S)
        Label(self,
              text="I'm thinking of a number between 1 and 100"
              ).grid(row=1, column=0, columnspan=2, sticky=W+E+N+S)
        Label(self,
              text="Try to guess it in as few attempts as possible"
              ).grid(row=2, column=0, columnspan=2, sticky=W+E+N+S)
        Label(self,
              text="What is your guess: "
              ).grid(row=4, column=0, sticky=W)
        self.guess_ent.grid(row=4, column=1, sticky=W)
        Button(self,
               text="Submit Guess",
               command=self.guessing
               ).grid(row=5, column=0, sticky=W)
        root.bind("<Return>", self.guessing)

        self.results = Label(self, text="")
        self.results.grid(row=6, column=0, sticky=W+E+N+S)

    def guessing(self, event=None):
        if self.guess_ent.get() != '':
            guess = int(self.guess_ent.get())
            if guess > self.the_number:
                    self.results.config(text="Lower")
                    self.guess_ent.delete(0, END)
            elif guess < self.the_number:
                    self.results.config(text="Higher")
                    self.guess_ent.delete(0, END)
            else:
                self.results.config(
                    text="You guessed it!. "
                         "The number I was thinking of was:{}, "
                         "and it only took you {}, tries"
                         .format(self.the_number, self.tries))

            self.tries += 1
            if self.tries >= 10:
                self.results.config(text="I'm sorry you couldn't guess the "
                                         "number in the appropriate amount "
                                         "of tries. The number I was "
                                         "thinking of was: {}"
                                         .format(self.the_number))


# main
root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()