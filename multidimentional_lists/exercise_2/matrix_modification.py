rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
columns = len(matrix[0])
while True:
    line = input().split()
    command = line[0]

    if command == "END":
        break

    row_index = int(line[1])
    col_index = int(line[2])
    value = int(line[3])

    if not 0 <= row_index <= rows - 1 or not 0 <= col_index <= columns - 1:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row_index][col_index] += value
    elif command == "Subtract":
        matrix[row_index][col_index] -= value

matrix = [[str(x) for x in row] for row in matrix]
[print(' '.join(row)) for row in matrix]
