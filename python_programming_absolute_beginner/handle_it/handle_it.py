# Handle It
# Demonstrates handling exceptions

# try/except
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("That was not a number!")

# Handle multiple exceptions
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert ", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong.")

# Handle multiple exceptions better
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number")
    except ValueError:
        print("I can only convert a string of digits.")

# getting an exceptions argument
try:
    num = float(input("Enter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)
