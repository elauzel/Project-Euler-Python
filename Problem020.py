import functools

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def impl(n: int):
    number = factorial(n)
    return sum(int(x) for x in str(number))


def factorial(n: int):
    return functools.reduce((lambda n1, n2: n1 * n2), range(1, n + 1))


# def test_factorial():
#     assert 1 == factorial(1)
#     assert 2 == factorial(2)
#     assert 6 == factorial(3)
#     assert 24 == factorial(4)
#     assert 120 == factorial(5)
#     assert 3628800 == factorial(10)


# def test_impl():
#     assert 1 == impl(1)
#     assert 2 == impl(2)
#     assert 6 == impl(3)
#     assert 6 == impl(4)
#     assert 3 == impl(5)
#     assert 27 == impl(10)


print("answer:", impl(100))
