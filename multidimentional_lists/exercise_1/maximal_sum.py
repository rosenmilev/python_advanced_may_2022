import sys

rows, cols = [int(x) for x in input().split()]

matrix = [[int(el) for el in input().split()] for i in range(rows)]
maximum_sum = -sys.maxsize
maximum_cube_matrix = []

for i in range(rows - 2):
    current_result = 0
    for j in range(cols - 2):
        current_matrix = [
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
            ]

        current_sum = sum(current_matrix)
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            maximum_cube_matrix = current_matrix.copy()

print(f"Sum = {maximum_sum}")
print(f"{maximum_cube_matrix[0]} {maximum_cube_matrix[1]} {maximum_cube_matrix[2]}")
print(f"{maximum_cube_matrix[3]} {maximum_cube_matrix[4]} {maximum_cube_matrix[5]}")
print(f"{maximum_cube_matrix[6]} {maximum_cube_matrix[7]} {maximum_cube_matrix[8]}")
