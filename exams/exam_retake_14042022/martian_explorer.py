def next_position(cur_i, cur_j, cur_command):
    if cur_command == "down":
        if cur_i + 1 > 5:
            cur_i = 0
        else:
            cur_i += 1
    elif cur_command == "up":
        if cur_i - 1 < 0:
            cur_i = 5
        else:
            cur_i -= 1
    elif cur_command == "left":
        if cur_j - 1 < 0:
            cur_j = 5
        else:
            cur_j -= 1
    elif cur_command == "right":
        if cur_j + 1 > 5:
            cur_j = 0
        else:
            cur_j += 1

    return cur_i, cur_j


matrix = []
rover_i = 0
rover_j = 0

for i in range(6):
    line = input().split(" ")
    for j in range(6):
        if line[j] == "E":
            rover_i = i
            rover_j = j
    matrix.append(line)

commands = input().split(", ")
water, metal, concrete = False, False, False

for command in commands:
    matrix[rover_i][rover_j] = "-"
    rover_i, rover_j = next_position(rover_i, rover_j, command)
    if matrix[rover_i][rover_j] == "R":
        print(f"Rover got broken at {rover_i, rover_j}")
        break
    elif matrix[rover_i][rover_j] == "W":
        print(f"Water deposit found at {rover_i, rover_j}")
        water = True
    elif matrix[rover_i][rover_j] == "M":
        print(f"Metal deposit found at {rover_i, rover_j}")
        metal = True
    elif matrix[rover_i][rover_j] == "C":
        print(f"Concrete deposit found at {rover_i, rover_j}")
        concrete = True

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
