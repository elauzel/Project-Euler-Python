# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def sum_even_fib_numers(ceiling: int):
    return sum([x for x in fib_numbers(ceiling) if x % 2 == 0])


def fib_numbers(ceiling: int, previous_numbers=[1, 2]):
    length = previous_numbers.__len__()
    prev1 = previous_numbers[length - 1]
    prev2 = previous_numbers[length - 2]

    next_num = prev1 + prev2
    if next_num > ceiling:
        return previous_numbers
    else:
        previous_numbers.append(next_num)
        return fib_numbers(ceiling, previous_numbers)


# def test():
#     assert 44 == sum_even_fib_numers(100)


print("answer:", sum_even_fib_numers(4000000))
