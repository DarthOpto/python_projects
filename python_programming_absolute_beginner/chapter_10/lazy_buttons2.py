# Lazy Buttons 2.0
# Demonstrates using a class with tkinter

from tkinter import *


class Application(Frame):
    """ A GUI application with three buttons """
    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create three buttons which do nothing """
        # Create the first button
        btn1 = Button(self, text="I do nothing.")
        btn1.grid()

        # Create a second button
        btn2 = Button(self)
        btn2.grid()
        btn2.configure(text="Me too.")

        # Create a third button
        btn3 = Button(self)
        btn3.grid()
        btn3["text"] = "Same Here!"

# main
root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()

