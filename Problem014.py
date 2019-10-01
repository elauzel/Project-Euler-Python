# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proven yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def find_longest_collatz_chain(ceiling: int):
    longest_chain = 0
    longest_number = 0
    for x in range(1, ceiling):
        chain_length = _collatz_chain_length(x)
        if chain_length > longest_chain:
            longest_chain = chain_length
            longest_number = x
    return longest_number


def _collatz_chain_length(n: int, chain_length: int = 1):
    if n == 1:
        return chain_length
    elif n % 2 == 0:
        return _collatz_chain_length(int(n / 2), chain_length + 1)
    else:
        return _collatz_chain_length(int(3 * n) + 1, chain_length + 1)


# def test():
#     assert 0 == find_longest_collatz_chain(1)
#     assert 1 == find_longest_collatz_chain(2)
#     assert 2 == find_longest_collatz_chain(3)
#     assert 3 == find_longest_collatz_chain(4)
#     assert 3 == find_longest_collatz_chain(5)
#     assert 3 == find_longest_collatz_chain(6)
#     assert 6 == find_longest_collatz_chain(7)
#     assert 7 == find_longest_collatz_chain(8)
#     assert 10 == _collatz_chain_length(13)


print("answer:", find_longest_collatz_chain(1000000))
