from math import factorial
from itertools import permutations


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
    print(f"Brute Force: {brute_force()}")
    print(f"Smart: {smart()}")
