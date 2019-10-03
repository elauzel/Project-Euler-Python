# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#               75                                 -> 75
#              95 64                               -> 95
#             17 47 82                             -> 82
#            18 35 87 10                           -> 87
#           20 04 82 47 65                         -> 82
#          19 01 23 75 03 34                       -> 75
#         88 02 77 73 07 63 67                     -> 88
#        99 65 04 28 06 16 70 92                   -> 99
#       41 41 26 56 83 40 80 70 33                 -> 83
#      41 48 72 33 47 32 37 16 94 29               -> 94
#     53 71 44 65 25 43 91 52 97 51 14             -> 97
#    70 11 33 28 77 73 17 78 39 68 17 57           -> 78
#   91 71 52 38 17 14 91 43 58 50 27 29 48         -> 91
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31       -> 89
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23     -> 98
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)


_triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]


def find_path_with_greatest_sum(triangle):
    return _fold_up_from_bottom(triangle, triangle[-1], len(triangle) - 2)


def _fold_up_from_bottom(triangle, row_of_sums, row_index_to_fold: int):
    if row_index_to_fold == 0:
        return max(row_of_sums[0] + triangle[0][0], row_of_sums[1] + triangle[0][0])
    else:
        row_to_fold = triangle[row_index_to_fold]

        new_sums = [max(row_to_fold[n] + row_of_sums[n], row_to_fold[n] + row_of_sums[n + 1]) for n in
                    range(0, row_to_fold.__len__())]
        return _fold_up_from_bottom(triangle, new_sums, row_index_to_fold - 1)


_test_triangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]


# def test():
#     assert 23 == find_path_with_greatest_sum(_test_triangle)


print("answer:", find_path_with_greatest_sum(_triangle))
