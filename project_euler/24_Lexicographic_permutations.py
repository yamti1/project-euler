"""
https://projecteuler.net/problem=24

Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from math import factorial
from itertools import permutations

from .com.timing import timed


TARGET_INDEX = int(1e6)
N = 10


def brute_force(n: int = N, target_index: int = TARGET_INDEX):
    numbers = list(range(n))
    for i, permutation in enumerate(permutations(numbers)):
        if i == target_index:
            return permutation
    raise IndexError(f"Not enough permutations of {n} numbers to reach index {target_index}")


def smart(n: int = N, target_index: int = TARGET_INDEX):
    numbers = list(range(n))
    result = []
    for i in range(n, 0, -1):
        total_permutations = factorial(i)
        permutations_per_number = total_permutations // i
        j, target_index = divmod(target_index, permutations_per_number)

        result.append(numbers.pop(j))
    return result


if __name__ == '__main__':
    print(f"Brute Force: {timed(brute_force)()}")
    print(f"Smart: {timed(smart)()}")
