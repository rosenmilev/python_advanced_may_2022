import sys

rows, columns = [int(x) for x in input().split(", ")]
matrix = []
max_sum = -sys.maxsize
max_sub_matrix = []


for _ in range(rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)

for i in range(rows - 1):
    current_matrix_sum = 0

    for j in range(columns - 1):
        current_sub_matrix = [matrix[i][j], matrix[i][j + 1],
                              matrix[i + 1][j], matrix[i + 1][j + 1]]

        current_matrix_sum = sum(current_sub_matrix)
        if current_matrix_sum > max_sum:
            max_sum = current_matrix_sum
            max_sub_matrix = current_sub_matrix.copy()

print(f"{max_sub_matrix[0]} {max_sub_matrix[1]}\n{max_sub_matrix[2]} {max_sub_matrix[3]}\n{max_sum}")
