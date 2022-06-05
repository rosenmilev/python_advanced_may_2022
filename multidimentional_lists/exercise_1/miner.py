def commands_interpreter(command, cur_position, r_c):
    r = cur_position[0]
    c = cur_position[1]

    if command == "up":
        if r - 1 >= 0:
            cur_position = [r - 1, c]
        else:
            cur_position = "won"

    elif command == "left":
        if c - 1 >= 0:
            cur_position = [r, c - 1]
        else:
            cur_position = "won"

    elif command == "down":
        if r + 1 <= r_c - 1:
            cur_position = [r + 1, c]
        else:
            cur_position = "won"

    elif command == "right":
        if c + 1 <= r_c - 1:
            cur_position = [r, c + 1]
        else:
            cur_position = "won"

    return cur_position


rows = columns = int(input())
commands = input().split()
playground = []
coal_positions = []
coal_collected = 0
current_position = []
end_of_route = []
game_over = False

for i in range(rows):
    line = input().split()
    playground.append(line)
    for j in range(len(line)):
        if line[j] == "e":
            end_of_route = [i, j]
        elif line[j] == "c":
            coal_positions.append([i, j])
        elif line[j] == "s":
            current_position = [i, j]

coal_number = len(coal_positions)

for curr_command in commands:
    current_position = commands_interpreter(curr_command, current_position, rows)
    i = int(current_position[0])
    j = int(current_position[1])

    if current_position == end_of_route:
        game_over = True
        print(f"Game over! ({i}, {j})")
        break

    elif current_position in coal_positions:
        coal_collected += 1
        coal_positions.remove(current_position)
        if coal_collected == coal_number:
            game_over = True
            print(f"You collected all coal! ({i}, {j})")
            break

if not game_over:
    print(f"{len(coal_positions)} pieces of coal left. ({i}, {j})")
