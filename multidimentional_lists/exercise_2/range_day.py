def moving_func(pos_i, pos_j, field, steps, dir_map, moving_direction):

    new_position = dir_map[moving_direction](pos_i, pos_j, steps)
    if new_position[0] > 4 or new_position[0] < 0 or new_position[1] > 4 or new_position[1] < 0:
        return pos_i, pos_j, field
    elif field[new_position[0]][new_position[1]] != ".":
        return pos_i, pos_j, field

    field[pos_i][pos_j] = "."
    field[new_position[0]][new_position[1]] = "A"
    return new_position[0], new_position[1], field


def shooting_func(pos_i, pos_j, field, dir_map, moving_direction, targets_hit):
    while True:

        target_position = dir_map[moving_direction](pos_i, pos_j, 1)

        if target_position[0] < 0 or target_position[0] > 4 or target_position[1] < 0 or target_position[1] > 4:
            return field, targets_hit

        pos_i = target_position[0]
        pos_j = target_position[1]

        if field[pos_i][pos_j] == "x":
            field[pos_i][pos_j] = "."
            targets_hit.append([pos_i, pos_j])
            return field, targets_hit


targets_hit = []
targets = 0
matrix = []
position_i = 0
position_j = 0
directions_map = {
    "up": lambda r, c, x: (r - x, c),
    "down": lambda r, c, x: (r + x, c),
    "left": lambda r, c, x: (r, c - x),
    "right": lambda r, c, x: (r, c + x)
}

for i in range(5):
    row = input().split(" ")
    for j in range(5):
        if row[j] == "A":
            position_i = i
            position_j = j
        if row[j] == "x":
            targets += 1

    matrix.append(row)

n = int(input())


for _ in range(n):
    line = input().split(" ")
    command = line[0]
    direction = line[1]

    if command == "move":
        curr_steps = int(line[2])
        position_i, position_j, matrix = moving_func(position_i, position_j, matrix, curr_steps, directions_map, direction)
    elif command == "shoot":
        matrix, targets_hit = shooting_func(position_i, position_j, matrix, directions_map, direction, targets_hit)

    if targets == len(targets_hit):
        print(f"Training completed! All {targets} targets hit.")
        print(*targets_hit, sep="\n")
        break

if targets > len(targets_hit):
    print(f"Training not completed! {targets - len(targets_hit)} targets left.")
    print(*targets_hit, sep="\n")
