def next_position(i, j, direction, size):
    if direction == "up" and i - 1 >= 0:
        return i - 1, j
    elif direction == "down" and i + 1 < size:
        return i + 1, j
    elif direction == "left" and j - 1 >= 0:
        return i, j - 1
    elif direction == "right" and j + 1 < size:
        return i, j + 1
    else:
        return i, j


def cookie_func(i, j, neighbour):
    res = []
    if neighbour[i][j - 1] == "V" or neighbour[i][j - 1] == "X":
        res.append([i, j - 1])
    if neighbour[i][j + 1] == "V" or neighbour[i][j + 1] == "X":
        res.append([i, j + 1])
    if neighbour[i - 1][j] == "V" or neighbour[i - 1][j] == "X":
        res.append([i - 1, j])
    if neighbour[i + 1][j] == "V" or neighbour[i + 1][j] == "X":
        res.append([i + 1, j])

    return res


presents_left = int(input())
size = int(input())
santa_pos_i = 0
santa_pos_j = 0
neighborhood = []
nice_kids = 0
nice_kids_gifted = 0

for i in range(size):
    line = input().split(" ")
    for j in range(size):
        if line[j] == "S":
            santa_pos_i = i
            santa_pos_j = j
        elif line[j] == "V":
            nice_kids += 1
    neighborhood.append(line)

while presents_left > 0:
    command = input()
    if command == "Christmas morning":
        break
    neighborhood[santa_pos_i][santa_pos_j] = "-"
    santa_pos_i, santa_pos_j = next_position(santa_pos_i, santa_pos_j, command, size)

    if neighborhood[santa_pos_i][santa_pos_j] == "V":
        presents_left -= 1
        nice_kids_gifted += 1

    elif neighborhood[santa_pos_i][santa_pos_j] == "C":
        gifted_kids_around = cookie_func(santa_pos_i, santa_pos_j, neighborhood)
        for kid_i, kid_j in gifted_kids_around:
            if neighborhood[kid_i][kid_j] == "V":
                nice_kids_gifted += 1
            presents_left -= 1
            neighborhood[kid_i][kid_j] = "-"
            if presents_left == 0:
                break

    neighborhood[santa_pos_i][santa_pos_j] = "S"
if nice_kids_gifted != nice_kids and presents_left == 0:
    print("Santa ran out of presents!")

for i in range(size):
    for el in neighborhood[i]:
        print(el, end=" ")
    print()

if nice_kids_gifted == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
    