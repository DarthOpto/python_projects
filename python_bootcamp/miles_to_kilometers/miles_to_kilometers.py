from tkinter import *


def miles_to_km():
    calculated = round(float(input.get()) * 1.609344)
    kilometers.config(text=calculated)


window = Tk()
window.title("Convert Miles to Kilometers")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Labels
miles = Label(text="Miles", font=("Arial", 15, "bold"))
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to:", font=("Arial", 15, "bold"))
is_equal.grid(column=0, row=1)

kilometers = Label(text="0", font=("Arial", 15, "bold"))
kilometers.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 15, "bold"))
km.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)









window.mainloop()

