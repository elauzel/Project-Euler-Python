import math


# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?


def triangle_number_with_divisor_count_exceeding(count: int):
    n = 0
    divisors = 0
    next_triangle_number = 0
    while divisors <= count:
        n += 1
        next_triangle_number = int((n * (n + 1)) / 2)  # The nth triangular number is given by T(n) = n * (n+1) / 2
        # Now, n and n + 1 are coprime
        # Since a and b are coprime, the number of divisors of (a * b) is just divisors_a * divisors_b
        if n % 2 == 0:
            divisors = count_divisors(int(n / 2)) * count_divisors(n + 1)
        else:
            divisors = count_divisors(n) * count_divisors(int((n + 1) / 2))
    return next_triangle_number


def count_divisors(n, start: int = 2):
    if n < 2:
        return 1
    for i in range(start, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            cnt = 1
            while n % i == 0:  # there is one divisor for each multiple of i
                n /= i
                cnt += 1
            return count_divisors(n, i + 1) * cnt  # continue finding more divisors
    return 2  # n was prime


# def test():
#     assert 1 == triangle_number_with_divisor_count_exceeding(0)
#     assert 3 == triangle_number_with_divisor_count_exceeding(1)
#     assert 6 == triangle_number_with_divisor_count_exceeding(2)
#     assert 6 == triangle_number_with_divisor_count_exceeding(3)
#     assert 28 == triangle_number_with_divisor_count_exceeding(4)
#     assert 28 == triangle_number_with_divisor_count_exceeding(5)


print("answer:", triangle_number_with_divisor_count_exceeding(500))