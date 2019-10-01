# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


def impl(exponent: int):
    return sum([int(x) for x in str(2 ** exponent)])


# def test():
#     assert 1 == impl(0)  # 1
#     assert 2 == impl(1)  # 2
#     assert 4 == impl(2)  # 4
#     assert 8 == impl(3)  # 8
#     assert 7 == impl(4)  # 16
#     assert 5 == impl(5)  # 32
#     assert 10 == impl(6)  # 64
#     assert 11 == impl(7)  # 128
#     assert 13 == impl(8)  # 256
#     assert 8 == impl(9)  # 512
#     assert 7 == impl(10)  # 1024
#     assert 14 == impl(11)  # 2048
#     assert 19 == impl(12)  # 4096
#     assert 20 == impl(13)  # 8192
#     assert 22 == impl(14)  # 16384
#     assert 26 == impl(15)  # 32768


print("answer:", impl(1000))
