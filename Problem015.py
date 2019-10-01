# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# 0,0 -> 0,1 -> 0,2 -> 1,2 -> 2,2
# 0,0 -> 0,1 -> 1,1 -> 1,2 -> 2,2
# 0,0 -> 0,1 -> 1,1 -> 2,1 -> 2,2
# 0,0 -> 1,0 -> 1,1 -> 1,2 -> 2,2
# 0,0 -> 1,0 -> 1,1 -> 2,1 -> 2,2
# 0,0 -> 1,0 -> 2,0 -> 2,1 -> 2,2
#
# How many such routes are there through a 20×20 grid?


def count_routes(grid_width: int, grid_height: int):
    if grid_width == 1 and grid_height == 1:
        return 2
    elif grid_width == grid_height:
        return count_routes(grid_width, grid_height - 1) * 2
    else:
        return int((grid_width + grid_height) * count_routes(grid_width - 1, grid_height) / grid_width)


# def test():
#     assert 2 == count_routes(1, 1)
#     assert 3 == count_routes(2, 1)  # (x + y) * prev / x
#     assert 6 == count_routes(2, 2)  # prev * 2
#     assert 10 == count_routes(3, 2)  # (x + y) * prev / x
#     assert 20 == count_routes(3, 3)  # prev * 2
#     assert 35 == count_routes(4, 3)  # (x + y) * prev / x
#     assert 70 == count_routes(4, 4)  # prev * 2
#     assert 126 == count_routes(5, 4)  # (x + y) * prev / x
#     assert 252 == count_routes(5, 5)  # prev * 2
#     assert 462 == count_routes(6, 5)  # (x + y) * prev / x
#     assert 924 == count_routes(6, 6)  # prev * 2


print("answer:", count_routes(20, 20))
