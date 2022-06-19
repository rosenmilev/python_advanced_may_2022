def moving_func(i, j, direction, dir_map, size):
    new_position = dir_map[direction](i, j)
    if new_position[0] < 0 or new_position[0] > size - 1 or new_position[1] < 0 or new_position[1] > size - 1:
        return i, j
    return new_position[0], new_position[1]


def cookie_func(i, j, neighbor, dir_map, presents, good_kids):
    upper_cell = dir_map["up"](i, j)
    bottom_cell = dir_map["down"](i, j)
    left_cell = dir_map["left"](i, j)
    right_cell = dir_map["right"](i, j)

    if neighbor[left_cell[0]][left_cell[1]] == "V":
        presents -= 1
        good_kids -= 1
    elif neighbor[left_cell[0]][left_cell[1]] == "X":
        presents -= 1

    neighbor[left_cell[0]][left_cell[1]] = "-"
    if presents == 0:
        return neighbor, presents, good_kids

    if neighbor[right_cell[0]][right_cell[1]] == "V":
        presents -= 1
        good_kids -= 1
    elif neighbor[right_cell[0]][right_cell[1]] == "X":
        presents -= 1
    neighbor[right_cell[0]][right_cell[1]] = "-"
    if presents == 0:
        return neighbor, presents, good_kids

    if neighbor[upper_cell[0]][upper_cell[1]] == "V":
        presents -= 1
        good_kids -= 1
    elif neighbor[upper_cell[0]][upper_cell[1]] == "X":
        presents -= 1
    neighbor[upper_cell[0]][upper_cell[1]] = "-"

    if presents == 0:
        return neighbor, presents, good_kids

    if neighbor[bottom_cell[0]][bottom_cell[1]] == "V":
        presents -= 1
        good_kids -= 1
    elif neighbor[bottom_cell[0]][bottom_cell[1]] == "X":
        presents -= 1
    neighbor[bottom_cell[0]][bottom_cell[1]] = "-"

    return neighbor, presents, good_kids


directions_map = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}

presents_left = int(input())
size = int(input())
santa_pos_i = 0
santa_pos_j = 0
neighborhood = []
nice_kids = 0

for i in range(size):
    line = input().split(" ")
    for j in range(size):
        if line[j] == "S":
            santa_pos_i = i
            santa_pos_j = j
        elif line[j] == "V":
            nice_kids += 1
    neighborhood.append(line)

nice_kids_total = nice_kids

while True:
    command = input()

    if command == "Christmas morning":
        neighborhood[santa_pos_i][santa_pos_j] = "S"
        break

    neighborhood[santa_pos_i][santa_pos_j] = "-"

    santa_pos_i, santa_pos_j = moving_func(santa_pos_i, santa_pos_j, command, directions_map, size)

    if neighborhood[santa_pos_i][santa_pos_j] == "V":
        nice_kids -= 1
        presents_left -= 1
    elif neighborhood[santa_pos_i][santa_pos_j] == "C":
        neighborhood, presents_left, nice_kids = cookie_func(santa_pos_i, santa_pos_j, neighborhood, directions_map, presents_left, nice_kids)
    elif neighborhood[santa_pos_i][santa_pos_j] == "X":
        neighborhood[santa_pos_i][santa_pos_j] = "-"

    if presents_left == 0:
        print("Santa ran out of presents!")
        neighborhood[santa_pos_i][santa_pos_j] = "S"
        break

for i in range(size):
    for el in neighborhood[i]:
        print(el, end=" ")
    print()

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_total} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
