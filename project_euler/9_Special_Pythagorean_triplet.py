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
from datetime import datetime

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


def will_triplet_be_primitive(n: int, m: int) -> bool:
    """
    Will the Pythagorean triple generated from n and m be primitive.
    """
    are_ordered = m > n > 0
    are_coprime = coprime(n, m)
    is_exactly_one_even = (m + n) % 2 == 1

    return are_ordered and are_coprime and is_exactly_one_even


def primitive_pythagorean_triplets():
    for z in naturals():
        n, m = inverse_cantor(z)
        if not will_triplet_be_primitive(n, m):
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


def main():
    try:
        start = datetime.now()
        a, b, c = find_special_triplet()
        end = datetime.now()
        print((a, b, c))
        print(f"Product: {a * b * c}")
        print(f"Runtime: {(end - start).microseconds}ms")
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
