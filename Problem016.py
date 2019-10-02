# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


def sum_of_digits_2_pow(exponent: int):
    return sum([int(x) for x in str(2 ** exponent)])


# def test():
#     assert 1 == sum_of_digits_2_pow(0)  # 1
#     assert 2 == sum_of_digits_2_pow(1)  # 2
#     assert 4 == sum_of_digits_2_pow(2)  # 4
#     assert 8 == sum_of_digits_2_pow(3)  # 8
#     assert 7 == sum_of_digits_2_pow(4)  # 16
#     assert 5 == sum_of_digits_2_pow(5)  # 32
#     assert 10 == sum_of_digits_2_pow(6)  # 64
#     assert 11 == sum_of_digits_2_pow(7)  # 128
#     assert 13 == sum_of_digits_2_pow(8)  # 256
#     assert 8 == sum_of_digits_2_pow(9)  # 512
#     assert 7 == sum_of_digits_2_pow(10)  # 1024
#     assert 14 == sum_of_digits_2_pow(11)  # 2048
#     assert 19 == sum_of_digits_2_pow(12)  # 4096
#     assert 20 == sum_of_digits_2_pow(13)  # 8192
#     assert 22 == sum_of_digits_2_pow(14)  # 16384
#     assert 26 == sum_of_digits_2_pow(15)  # 32768


print("answer:", sum_of_digits_2_pow(1000))
