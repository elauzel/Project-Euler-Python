# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def smallest_number(range_ceiling: int):
    max_num = range_ceiling * (range_ceiling - 1)
    one_to_twenty = range(1, range_ceiling + 1)
    for x in range(range_ceiling + 1, max_num, 2):
        if all(x % y == 0 for y in one_to_twenty):
            return x


# def test():
#     assert 2520 == smallest_number(10)

print("answer:", smallest_number(20))
