# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a² + b² = c²
#
# For example, 3² + 4² = 9 + 16 = 25 = 5².
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def find_triplet_product_for_sum(sum: int):
    for a in range(1, sum - 2):
        for b in range(a + 1, sum - 1):
            for c in range(b + 1, sum):
                if (a + b + c == sum) and (a ** 2 + b ** 2 == c ** 2):
                    return a * b * c


# def test():
#     assert 60 == find_triplet_product_for_sum(12)


print("answer:", find_triplet_product_for_sum(1000))
