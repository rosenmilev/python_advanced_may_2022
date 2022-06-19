import sys

size = int(input())

matrix = []
bunny_position_i = 0
bunny_position_j = 0

max_eggs = -sys.maxsize
max_direction = ""
max_path = []

current_eggs = -1
current_path = []

for i in range(size):
    line = input().split()
    for j in range(size):
        if line[j] == "B":
            bunny_position_i, bunny_position_j = i, j
    matrix.append(line)


if bunny_position_i != 0:
    current_path = []
    current_eggs = 0
    for i in range(bunny_position_i - 1, -1, -1):
        if matrix[i][bunny_position_j] == "X":
            break

        current_eggs += int(matrix[i][bunny_position_j])
        current_path.append([i, bunny_position_j])
if current_eggs > max_eggs and current_path:
    max_eggs = current_eggs
    max_direction = "up"
    max_path = current_path


if bunny_position_i != size - 1:
    current_path = []
    current_eggs = 0
    for i in range(bunny_position_i + 1, size):
        if matrix[i][bunny_position_j] == "X":
            break
        current_path.append([i, bunny_position_j])
        current_eggs += int(matrix[i][bunny_position_j])

if current_eggs > max_eggs and current_path:
    max_eggs = current_eggs
    max_direction = "down"
    max_path = current_path

if bunny_position_j != 0:
    current_path = []
    current_eggs = 0
    for i in range(bunny_position_j - 1, -1, -1):
        if matrix[bunny_position_i][i] == "X":
            break
        current_eggs += int(matrix[bunny_position_i][i])
        current_path.append([bunny_position_i, i])
if current_eggs > max_eggs and current_path:
    max_eggs = current_eggs
    max_direction = "left"
    max_path = current_path

if bunny_position_j != size - 1:
    current_path = []
    current_eggs = 0
    for i in range(bunny_position_j + 1, size):
        if matrix[bunny_position_i][i] == "X":
            break
        current_path.append([bunny_position_i, i])
        current_eggs += int(matrix[bunny_position_i][i])

if current_eggs > max_eggs and current_path:
    max_eggs = current_eggs
    max_direction = "right"
    max_path = current_path


print(max_direction)
print(*max_path, sep="\n")
print(max_eggs)
