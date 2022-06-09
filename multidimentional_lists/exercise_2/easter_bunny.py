size = int(input())

matrix = []
bunny_position_i = 0
bunny_position_j = 0
max_eggs = 0
max_directions = {
    "up": [],
    "down": [],
    "left": [],
    "right": []
}
max_direction = ""
up = 0
down = 0
right = 0
left = 0

for i in range(size):
    line = input().split()
    for j in range(size):
        if line[j] == "B":
            bunny_position_i, bunny_position_j = i, j
    matrix.append(line)

if bunny_position_i == 0:
    up = 0
else:
    for i in range(bunny_position_i - 1, -1, -1):
        if matrix[i][bunny_position_j] == "X":
            break

        up += int(matrix[i][bunny_position_j])
        max_directions["up"].append([i, bunny_position_j])
if 1 <= up > max_eggs:
    max_eggs = up
    max_direction = "up"

if bunny_position_i == size - 1:
    down = 0
else:
    for i in range(bunny_position_i + 1, size):
        if matrix[i][bunny_position_j] == "X":
            break
        max_directions["down"].append([i, bunny_position_j])
        down += int(matrix[i][bunny_position_j])

if 1 <= down > max_eggs:
    max_eggs = down
    max_direction = "down"

if bunny_position_j == 0:
    left = 0
else:
    for i in range(bunny_position_j - 1, -1, -1):
        if matrix[bunny_position_i][i] == "X":
            break
        left += int(matrix[bunny_position_i][i])
        max_directions["left"].append([bunny_position_i, i])
if 1 <= left > max_eggs:
    max_eggs = left
    max_direction = "left"

if bunny_position_j == size - 1:
    right = 0
else:
    for i in range(bunny_position_j + 1, size):
        if matrix[bunny_position_i][i] == "X":
            break
        max_directions["right"].append([bunny_position_i, i])
        right += int(matrix[bunny_position_i][i])

if 1 <= right > max_eggs:
    max_eggs = right
    max_direction = "right"


print(max_direction)
print(*max_directions[max_direction], sep="\n")
print(max_eggs)
