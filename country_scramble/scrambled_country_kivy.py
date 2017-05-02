import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from country_scramble.country_getter import get_country


class CountryScramble(GridLayout):
    def __init__(self, **kwargs):
        super(CountryScramble, self).__init__(**kwargs)
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=40
        self.the_country = None
        self.scrambled = None
        self.languages = None
        self.guess_ent = None
        self.scrambled_label = None
        self.tries = None
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        scrambled = self.add_widget(Label())
        welcome = self.add_widget(Label(
            text='[b][size=30]Welcome to Country Scramble[/size][/b]',
            markup=True))
        try_to = self.add_widget(Label(
            text='[b][size=25]Try to guess the country in as few tries as '
                 'possible.[/size][/b]',
            markup=True))
        your_guess = self.add_widget(Label(text='What is your guess?: '))
        guess_ent = TextInput(focus=True)
        submit = Button(text='Submit')
        self.guess_ent = guess_ent
        self.scrambled_label = scrambled

    # def reset_input(self):
    #     self.guess_ent.reset()

    def guessing(self):
        guess = self.guess_ent.get().upper()
        country = self.the_country.upper()
        if not guess:
            return

        if guess != country:
            # title, \
            # message = "Continue?", "Sorry that answer is not correct"
            # # messagebox.showwarning(title, message)
            # self.reset_input()
            self.tries += 1

            # Ask if user wants a hint at 5 tries
            # if self.tries == 5:
            #     title, message = "Hint?", "Would you like a hint?"
            #     if messagebox.askyesno(title, message):
            #         title, message = "Languages", \
            #                          "The language(s) of this country is: {}" \
            #                              .format(self.languages)
            #         messagebox.askokcancel(title, message)
            #         self.reset_input()
            #     else:
            #         self.reset_input()
            #
            # # Ask if user wants another hint at 10 tries
            # if self.tries == 10:
            #     title, message = "Hint?", "Would you like another hint?"
            #     if messagebox.askyesno(title, message):
            #         title, message = "Currency", \
            #                          "The currency of this country is: {}" \
            #                              .format(self.currency)
            #         messagebox.askokcancel(title, message)
            #         self.reset_input()
            #     else:
            #         self.reset_input()
            #
            # # Ask if user wants another hint at 15 tries
            # if self.tries == 15:
            #     title, message = "Hint?", "Would you like your final hint?"
            #     if messagebox.askyesno(title, message):
            #         title, message = "Capital", \
            #                          "The capital of this country is: {}" \
            #                              .format(self.country_capital)
            #         messagebox.askokcancel(title, message)
            #         self.reset_input()
            #     else:
            #         self.reset_input()

            # User isn't going to get it at this point give them the answer
            # and ask if they want to try again.
            # if self.tries == 20:
            #     title, message = "Sorry", "You went over the max number of " \
            #                               "tries, the country was: {}, " \
            #                               "would you like to try another" \
            #         .format(self.the_country)
            #     if messagebox.askyesno(title, message):
            #         self.new_game()
            #     else:
            #         root.destroy()
            return
        #
        # title, message = "Congratulations", "Would you like to try another?"
        # if messagebox.askyesno(title, message):
        #     self.new_game()
        # else:
        #     root.destroy()

    def new_game(self):
        self.the_country, self.scrambled, self.country_capital, \
        self.currency, self.languages = get_country()
        self.scrambled_label = self.add_widget(Label(text=self.scrambled))
        self.tries = 1
        # self.reset_input()


class MyApp(App):
    def build(self):
        return CountryScramble()

if __name__ == '__main__':
    MyApp().run()