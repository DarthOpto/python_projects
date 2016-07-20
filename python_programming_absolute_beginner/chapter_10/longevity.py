# Longevity
# Demonstrates text and entry widgets, and the Grid Layout Manager

from tkinter import *


class Application(Frame):
    """ GUI Application which can reveal the secret of longevity """
    def __init__(self, master):
        """ Initialize the frame """
        super(Application, self).__init__(master)
        self.grid()
        self.inst_lbl = None
        self.pw_lbl = None
        self.pw_ent = None
        self.submit_btn = None
        self.secret_txt = None
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets """
        # Create an instruction label
        self.inst_lbl = Label(self, text="Enter password for the secret of "
                                         "longevity")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        # Create label for password
        self.pw_lbl = Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        # Create entry widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        # Create submit button
        self.submit_btn = Button(self, text="Submit", command=self.reveal)
        root.bind("<Return>", self.reveal_a)
        self.submit_btn.grid(row=2, column=0, sticky=W)

        # create text widget to display message
        self.secret_txt = Text(self, state='disabled', width=35, height=5,
                               wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """ Displays message based on password. """
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Here's the secret to living to 100: live to 99 and " \
                      "then be VERY careful."
        else:
            message = "That's not the correct password, so I cannot share " \
                      "the secret with you."
        self.secret_txt.configure(state='normal')
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
        self.secret_txt.configure(state='disabled')

    def reveal_a(self, event):
        self.reveal()

# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)

root.mainloop()
