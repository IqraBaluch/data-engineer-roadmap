"""
Given numRows, return the first numRows rows of Pascal’s triangle. 
Each number is the sum of the two numbers directly above it, and the edges are always 1.

numRows = 5 → [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

"""

numRows = 5

triangle = []

for i in range(numRows):

    if i == 0:
        row = [1]

    else:
        previous_row = triangle[-1]
        row = [1]

        for j in range(len(previous_row) - 1):
            row.append(previous_row[j] + previous_row[j + 1])

        row.append(1)

    triangle.append(row)

print(triangle)