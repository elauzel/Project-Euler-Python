import math


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def sum_of_primes_below_n(n: int):
    not_primes = []
    for x in range(2, int(math.sqrt(n)) + 1):
        i = x
        while i < n:
            i += x
            not_primes.append(i)
    sieve = set(not_primes)
    return sum([x for x in range(2, n) if x not in sieve])


# def test():
#     assert 17 == sum_of_primes_below_n(10)


print("answer:", sum_of_primes_below_n(2000000))
