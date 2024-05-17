import math


def paint_calc(height, width, cover):
    area = (height * width) / coverage
    number_of_cans = math.ceil(area)
    print(f"You will need this many {number_of_cans} cans of paint.")

test_height = int(input("What is the height of the wall you are painting? \n"))
test_width = int(input("What is the width of the wall you are painting? \n"))
coverage = 5

paint_calc(height=test_height, width=test_width, cover=coverage)