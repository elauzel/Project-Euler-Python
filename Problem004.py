# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome(digits: int):
    biggest_num = (10 ** digits) - 1
    largest_palindrome = 1
    for x in range(biggest_num, 1, -1):
        factors_of_x_for_exceeding_largest_palindrome = range(biggest_num, int(largest_palindrome / x), -1)
        pal_factors_of_x = [y for y in factors_of_x_for_exceeding_largest_palindrome if is_palindrome(str(x * y))]
        if pal_factors_of_x.__len__() > 0:
            largest_palindrome = x * pal_factors_of_x[0]
    return largest_palindrome


def is_palindrome(s: str):
    length = s.__len__()
    even = length % 2 == 0
    left_half = s[0: int(length / 2)] if even else s[0:int((length - 1) / 2)]
    right_half = s[int(length / 2):] if even else s[int((length + 1) / 2):]
    return left_half == right_half[::-1]


# def test():
#     assert 9009 == largest_palindrome(2)


print("answer:", largest_palindrome(3))
