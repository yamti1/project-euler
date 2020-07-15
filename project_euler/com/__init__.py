def naturals():
    """
    An infinite generator of the natural numbers.
    """
    n = 0
    while True:
        yield n
        n += 1


def greatest_common_divisor(a: int, b: int) -> int:
    """
    The largest number that divides both integers `a` and `b`.
    """
    # Source: https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations

    while b != 0:
        a, b = b, a % b
    return a


gcd = greatest_common_divisor
