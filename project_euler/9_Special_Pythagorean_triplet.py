"""
https://projecteuler.net/problem=9

Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

from .com import naturals, coprime


TARGET_SUM = 1000


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
        if not (m > n > 0 and coprime(n, m)):
            continue
        a, b, c = euclids_formula(n, m)
        yield a, b, c


def find_special_triplet(target_sum=TARGET_SUM):
    for a, b, c in primitive_pythagorean_triplets():
        print(f"Checking triplet {a, b, c}")
        div, mod = divmod(target_sum, a + b + c)
        if mod == 0:
            return a * div, b * div, c * div
        if div < 1:
            raise ValueError("Could not find Special Triplet")


if __name__ == '__main__':
    try:
        a, b, c = find_special_triplet()
        print((a, b, c))
        print(f"Product: {a * b * c}")
    except ValueError as e:
        print(e)
