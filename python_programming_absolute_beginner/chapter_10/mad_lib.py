# Mad Lib
# Create a story based on user input

from tkinter import *


class Application(Frame):
    """ GUI Application that creates a story based on user input """
    def __init__(self, master):
        """ Initialize the Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.person_ent = Entry(self)
        self.noun_ent = Entry(self)
        self.verb_ent = Entry(self)
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get story information and to display story """
        # Create instruction label
        Label(self,
              text="Enter information for a new story",
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        # Create a label and text entry for the name of a person
        Label(self,
              text="Person: "
              ).grid(row=1, column=0, sticky=W)
        self.person_ent.grid(row=1, column=1, sticky=W)

        # Create a label and text entry for a plural noun
        Label(self,
              text="Plural Noun: "
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        # Create a label and text entry for a verb
        Label(self,
              text="Verb: "
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent.grid(row=3, column=1, sticky=W)