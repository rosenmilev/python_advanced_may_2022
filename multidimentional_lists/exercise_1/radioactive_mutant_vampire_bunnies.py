def commands_interpreter(command, cur_position, i, j):
    r = cur_position[0]
    c = cur_position[1]
    won = False

    if command == "U":
        if r - 1 >= 0:
            cur_position = [r - 1, c]
        else:
            won = True

    elif command == "L":
        if c - 1 >= 0:
            cur_position = [r, c - 1]
        else:
            won = True

    elif command == "D":
        if r + 1 <= i - 1:
            cur_position = [r + 1, c]
        else:
            won = True

    elif command == "R":
        if c + 1 <= j - 1:
            cur_position = [r, c + 1]
        else:
            won = True

    return cur_position, won


def lair_final_state(lair, bunnies_positions, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if [i, j] in bunnies_positions:
                lair[i][j] = "B"

    return lair


rows, columns = [int(x) for x in input().split()]
lair = []
current_position = ""
bunnies_positions = []
dead = False
won = False
for i in range(rows):
    line = input()
    row = []
    for j in range(len(line)):
        row.append(line[j])
        if line[j] == "P":
            current_position = [i, j]
        elif line[j] == "B":
            bunnies_positions.append([i, j])
    lair.append(row)

commands = input()

for curr_command in commands:
    last_position = current_position
    current_position, won = commands_interpreter(curr_command, current_position, rows, columns)

    cur_i = current_position[0]
    cur_j = current_position[1]

    if lair[cur_i][cur_j] == "B":
        dead = True

    else:
        lair[last_position[0]][last_position[1]] = "."
        lair[cur_i][cur_j] = "P"

    curr_bunnies_positions = bunnies_positions.copy()

    for bunnie_pos in curr_bunnies_positions:

        i = bunnie_pos[0]
        j = bunnie_pos[1]

        if i - 1 >= 0:
            if lair[i - 1][j] == "P":
                dead = True
            if [i - 1, j] not in bunnies_positions:
                bunnies_positions.append([i - 1, j])
        if j - 1 >= 0:
            if lair[i][j - 1] == "P":
                dead = True
            if[i, j - 1] not in bunnies_positions:
                bunnies_positions.append([i, j - 1])
        if i + 1 <= rows - 1:
            if lair[i + 1][j] == "P":
                dead = True
            if [i + 1, j] not in bunnies_positions:
                bunnies_positions.append([i + 1, j])
        if j + 1 <= columns - 1:
            if lair[i][j + 1] == "P":
                dead = True
            if [i, j + 1] not in bunnies_positions:
                bunnies_positions.append([i, j + 1])

    if dead or current_position in bunnies_positions:
        dead = True

    if won:
        lair[cur_i][cur_j] = "."
        break
    if dead:
        lair[last_position[0]][last_position[1]] = "."
        break

lair = lair_final_state(lair, bunnies_positions, rows, columns)
for row in lair:
    print(''.join(row))

if won:
    print(f"won: {' '.join([str(x) for x in last_position])}")
elif dead:
    print(f"dead: {' '.join([str(x) for x in current_position])}")
