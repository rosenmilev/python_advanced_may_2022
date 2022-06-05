def coordinate_validator(i, j, r_c):
    valid_coordinates = []
    i_minus = False
    i_plus = False
    j_minus = False
    j_plus = False

    if i - 1 >= 0:
        i_minus = True
    if i + 1 <= r_c - 1:
        i_plus = True
    if j - 1 >= 0:
        j_minus = True
    if j + 1 <= r_c - 1:
        j_plus = True

    if i_minus and j_minus:
        valid_coordinates.append([i - 1, j - 1])
    if i_minus:
        valid_coordinates.append([i - 1, j])
    if i_minus and j_plus:
        valid_coordinates.append([i - 1, j + 1])
    if j_minus:
        valid_coordinates.append([i, j - 1])
    if j_plus:
        valid_coordinates.append([i, j + 1])
    if i_plus and j_minus:
        valid_coordinates.append([i + 1, j - 1])
    if i_plus:
        valid_coordinates.append([i + 1, j])
    if i_plus and j_plus:
        valid_coordinates.append([i + 1, j + 1])

    return valid_coordinates


rows = columns = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
neighboring_cells_coordinates = []
alive_cells = []
bombs_to_detonate_coordinates = input().split(" ")

for bomb in bombs_to_detonate_coordinates:
    curr_i, curr_j = [int(x) for x in bomb.split(",")]
    if matrix[curr_i][curr_j] > 0:
        explosion = matrix[curr_i][curr_j]
        matrix[curr_i][curr_j] = 0
        neighboring_cells_coordinates = coordinate_validator(curr_i, curr_j, rows)

        for coordinates in neighboring_cells_coordinates:
            i = coordinates[0]
            j = coordinates[1]
            if matrix[i][j] > 0:
                matrix[i][j] -= explosion

for r in range(rows):
    for c in range(columns):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])
        matrix[r][c] = str(matrix[r][c])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(' '.join(row)) for row in matrix]
