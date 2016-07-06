# If there are an even number of digits,
# double every other digit starting with the first,
#  and if there are an odd number of digits,
#  double every other digit starting with the second.
# Another way to think about it is, from the right to left,
#  double every other digit starting with the second to last digit.

# If a resulting doubled number is greater than 9,
# replace it with either the sum of it's own digits, or 9 subtracted from it.

# Sum all of the final digits

# Finally, take that sum and divide it by 10. If the remainder equals zero,
# the original credit card number is valid.


def validate(a):
    result = (10 - sum([int(y) * [7, 3, 1][x % 3] for x, y in
              enumerate(str(a)[::-1])]) % 10) % 10
    if result == 0:
        print(True)
    else:
        print(False)

validate(5438058091002682)