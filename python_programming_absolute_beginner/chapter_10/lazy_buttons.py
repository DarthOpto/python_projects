# Lazy Buttons
# Demonstrates creating buttons

from tkinter import *

# Create the root window
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

# Create the frame to hold other widgets
app = Frame(root)
app.grid()

# Create a button in the frame
btn1 = Button(app, text='I do nothing!')
btn1.grid()

# Create a second button in the frame
btn2 = Button(app)
btn2.configure(text="Me too!")
btn2.grid()

# Create a third button
btn3 = Button(app)
btn3.grid()
btn3["text"] = "Same Here!"

# Kick off the window's event loop
root.mainloop()