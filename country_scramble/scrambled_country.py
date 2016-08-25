# Country Scramble
# Picks a country from the countries database, scrambles it, and asks the user
# to unscramble it
# A special thank you to /r/Vaphell for his/her help in making this run a lot
# smoother.

from tkinter import *
from tkinter import messagebox
from country_scramble.country_getter import get_country


class Application(Frame):
    """A GUI Application for unscrambling a country"""

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=BOTH, expand=1, padx=10, pady=10)

        self.columnconfigure(0, weight=1)
        for i in range(7):
            self.rowconfigure(i, weight=1)

        self.the_country = None
        self.scrambled = None
        self.guess_ent = None
        self.scrambled_label = None
        self.tries = 1

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        welcome = Label(self, text="Welcome to Country Scramble", font="bold")
        try_to = Label(
            self, text="Try to guess the country in as few tries as possible.")
        scrambled = Label(self, font="sans-serif 12 bold", fg="blue")
        your_guess = Label(self, text="What is your guess?: ")
        guess_ent = Entry(self, font="sans-serif 12")
        submit = Button(self, text="Submit Guess", command=self.guessing)

        welcome.grid(row=0, column=0, sticky=N + E + W + S)
        try_to.grid(row=1, column=0, sticky=N + E + W + S)
        scrambled.grid(row=2, column=0, sticky=N + E + W + S)
        your_guess.grid(row=4, column=0, sticky=W)
        guess_ent.grid(row=5, column=0, sticky=N + E + W + S)
        submit.grid(row=6, column=0, sticky=N + S, pady=5)

        self.guess_ent = guess_ent
        self.scrambled_label = scrambled
        root.bind("<Return>", self.guessing)

    def reset_input(self):
        self.guess_ent.delete(0, END)

    def guessing(self, event=None):
        guess = self.guess_ent.get().upper()
        country = self.the_country.upper()
        if not guess:
            return

        self.tries += 1
        if guess != country:
            title, \
                message = "Continue?", "Sorry that answer is not correct"
            messagebox.showwarning(title, message)
            self.reset_input()
            return

        title, message = "Congratulations", "Would you like to try another?"
        if messagebox.askyesno(title, message):
            self.new_game()
        else:
            root.destroy()

    def new_game(self):
        self.the_country, self.scrambled = get_country()
        self.scrambled_label.configure(text=self.scrambled)
        self.tries = 1
        self.reset_input()
# TODO - Add Hints after a certain number of tries

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x200")
    root.resizable(width=False, height=False)
    root.title("Country Scramble")
    app = Application(root)
    root.mainloop()
