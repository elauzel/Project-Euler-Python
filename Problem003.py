import math


# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(n: int):
    max_prime = -1

    while n % 2 == 0:
        max_prime = 2
        n >>= 1  # equivalent to n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):  # keep dividing n by each prime factor you find to reduce prob space
        while n % i == 0:
            max_prime = i
            n = n / i

    if n > 2:
        max_prime = n

    return max_prime


# def test():
#     assert largest_prime_factor(13195) == 29


print("answer:", largest_prime_factor(600851475143))
