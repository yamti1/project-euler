from math import sqrt

TARGET_SUM = 1000


def naturals():
    """
    An infinite generator of the natural numbers.
    """
    n = 0
    while True:
        yield n
        n += 1


def inverse_cantor(z: int) -> (int, int):
    """
    Maps between the natural numbers to all pairs of natural numbers.
    """
    # Source: https://en.wikipedia.org/wiki/Pairing_function#Inverting_the_Cantor_pairing_function

    w = (sqrt(8*z + 1) - 1) // 2
    t = (w*w + w) / 2
    y = z - t
    x = w - y

    return int(x), int(y)


def greatest_common_divisor(a: int, b: int) -> int:
    """
    The largest number that divides both integers `a` and `b`.
    """
    # Source: https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations

    while b != 0:
        a, b = b, a % b
    return a


def euclids_formula(n: int, m: int) -> (int, int, int):
    """
    Euclid's formula for generating Pythagorean triples from pairs of numbers.
    """
    # Source: https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n
    return a, b, c


def primitive_pythagorean_triplets():
    for z in naturals():
        n, m = inverse_cantor(z)
        if not (m > n > 0 and greatest_common_divisor(n, m) == 1):
            continue
        a, b, c = euclids_formula(n, m)
        yield a, b, c


def find_special_triplet(target_sum=TARGET_SUM):
    for a, b, c in primitive_pythagorean_triplets():
        print(f"Checking triplet {a, b, c}")
        div, mod = divmod(target_sum, a + b + c)
        if mod == 0:
            return a * div, b * div, c * div


if __name__ == '__main__':
    print(find_special_triplet())
