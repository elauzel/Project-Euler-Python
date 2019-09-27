# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?


def prime_number(n: int):
    primes = [2]
    i = 2
    while primes.__len__() < n:
        i += 1
        if all(i % y != 0 for y in primes):
            if primes.__len__() == n - 1:
                return i
            else:
                primes.append(i)


# def test():
#     assert 13 == prime_number(6)


print("answer:", prime_number(10001))
