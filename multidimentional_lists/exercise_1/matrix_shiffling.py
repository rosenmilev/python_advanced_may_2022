def index_validator(indexes):
    is_valid = True
    if not len(indexes) == 4:
        is_valid = False

    for i in range(len(indexes)):
        if not indexes[i].isdigit():
            is_valid = False
        elif int(indexes[i]) < 0:
            is_valid = False
        elif i == 0 or i == 2:
            if int(indexes[i]) > rows - 1:
                is_valid = False
        elif i == 1 or i == 3:
            if int(indexes[i]) > cols - 1:
                is_valid = False

    return is_valid


rows, cols = [int(x) for x in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    current_command = command[0]

    if current_command == "END":
        break

    if not current_command == "swap":
        print("Invalid input!")
        continue

    current_indexes = command[1:]
    if not index_validator(current_indexes):
        print("Invalid input!")
        continue

    current_indexes = [int(x) for x in command[1:] if int(x) >= 0 and x.isdigit()]

    i1 = current_indexes[0]
    j1 = current_indexes[1]
    i2 = current_indexes[2]
    j2 = current_indexes[3]

    matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
    [print(" ".join(row)) for row in matrix]
