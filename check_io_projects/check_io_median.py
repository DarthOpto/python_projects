# import statistics

# The right way to do this
# def checkio(data):
#
#     median = statistics.median(data=data)
#     return median


def checkio(data):
    sorted_list = sorted(data)
    middle = len(data) // 2
    if len(data) % 2:
        median = sorted_list[middle]
        return median
    else:
        median = (sorted_list[middle] + sorted_list[middle - 1]) / 2
        return median

# These "asserts" using only for self-checking and not necessary for
#  auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")