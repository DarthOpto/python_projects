# Click Counter
# Demonstrates binding an event with an event handler
from tkinter import *


class Application(Frame):
    """A GUI application which counts button clicks"""
    def __init__(self, master):
        """ Initialize the Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.btn_clicks = 0
        self.create_widget()

    def create_widget(self):
        """ Create a button which displays number of clicks """
        self.btn = Button(self)
        self.btn["text"] = "Total Clicks: 0"
        self.btn["command"] = self.update_count
        self.btn.grid()

    def update_count(self):
        """ Increase the click count and display new total """
        self.btn_clicks += 1
        self.btn["text"] = "Total Clicks: {}".format(str(self.btn_clicks))


# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")

app = Application(root)
root.mainloop()
