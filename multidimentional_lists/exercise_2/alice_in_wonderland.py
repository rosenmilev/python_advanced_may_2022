def moving_func(i, j, direction, dir_map, size):
    new_position = dir_map[direction](i, j)
    if new_position[0] < 0 or new_position[0] > size - 1 or new_position[1] < 0 or new_position[1] > size - 1:
        return (i, j), True
    else:
        return new_position, False


def printing_func(matrix, size):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print()


matrix = []
n = int(input())
alice_i = 0
alice_j = 0
tea_bags = 0

directions_map = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}

for i in range(n):
    row = input().split(" ")
    for j in range(n):
        if row[j] == "A":
            alice_i = i
            alice_j = j

    matrix.append(row)

matrix[alice_i][alice_j] = "*"

while True:
    command = input()

    new_position, out_of_range = moving_func(alice_i, alice_j, command, directions_map, n)
    alice_i = new_position[0]
    alice_j = new_position[1]


    if out_of_range or matrix[new_position[0]][new_position[1]] == "R":
        matrix[alice_i][alice_j] = "*"
        print("Alice didn't make it to the tea party.")
        printing_func(matrix, n)
        break

    if matrix[alice_i][alice_j].isdigit():
        tea_bags += int(matrix[alice_i][alice_j])
    matrix[alice_i][alice_j] = "*"

    if tea_bags >= 10:
        print("She did it! She went to the party.")
        printing_func(matrix, n)
        break
    matrix[alice_i][alice_j] = "*"
