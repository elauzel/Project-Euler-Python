# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def sum_of_primes_below_n(n: int):
    primes = [2]
    i = 1
    while i < n - 1:
        i += 2
        if all(i % y != 0 for y in primes):
            primes.append(i)
    return sum(primes)


# def test():
#     assert 17 == sum_of_primes_below_n(10)


print("answer:", sum_of_primes_below_n(2000000))
