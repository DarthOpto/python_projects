from itertools import groupby


def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')


