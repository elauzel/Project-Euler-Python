import math


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def sum_of_primes_below_n(n: int):
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for x in range(2, int(math.sqrt(n)) + 1):
        i = x * 2
        while i < n:
            sieve[i] = False
            i += x
    return sum([x for x in range(2, n) if sieve[x]])


# def test():
#     assert 17 == sum_of_primes_below_n(10)


print("answer:", sum_of_primes_below_n(2000000))
