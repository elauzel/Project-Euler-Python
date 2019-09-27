# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square_sum_difference(ceiling: int):
    nums = range(1, ceiling + 1)
    sum_of_squares = sum([x ** 2 for x in nums])
    square_of_sums = sum([x for x in nums]) ** 2
    return abs(square_of_sums - sum_of_squares)


# def test():
#     assert 2640 == square_sum_difference(10)


print("answer:", square_sum_difference(100))
