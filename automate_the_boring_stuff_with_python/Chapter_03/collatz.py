# Collatz Sequence


def collatz():
    try:
        number = int(input("Please enter a number: "))
        if number % 2 == 0:
            value = number // 2
            print(value)
        else:
            value = 3 * number + 1
            print(value)
    except ValueError:
        print("Invalid input, please enter a number")

# main
collatz()
