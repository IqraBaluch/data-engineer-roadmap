# LeetCode 1572: Matrix Diagonal Sum
# Idea: one loop; row i uses column i (main diagonal) and column len - 1 - i (other diagonal).
# For an odd size the middle cell is on both diagonals, so subtract it once after the loop.
# Time: O(n), n = number of rows; only 2n cells are visited
# Space: O(1), only a few single variables are stored

# total = 0
# for i in range(len(grid)):
#     val = grid[i][i]
#     total = total + val
#     print(val)
#     val2 = len(grid)-1-i
#     val2 = grid[i][val2]
#     print(val2)
#     total = total + val2

# mid = len(grid) // 2
# mid = grid[mid][mid]
# print(total-mid)


# grid1 = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]


def diagonalSum(grid1):
    mid = 0
    total = 0
    for i in range(len(grid1)):

        val1 = grid1[i][i]
        # print(val1)
        total = total+val1

        val2 = len(grid1)-1-i
        val2 = grid1[i][val2]
        # print(val2)
        total = total + val2

    if len(grid1) % 2 !=0:
        mid = len(grid1) //2
        total = total - grid1[mid][mid]


    return total

print(diagonalSum(grid1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]))