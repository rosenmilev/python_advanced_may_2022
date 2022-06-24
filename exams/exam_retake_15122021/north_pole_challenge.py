def moving_func(santa_i, santa_j,direction, rows, cols):
    if direction == "down":
        if santa_i + 1 > rows - 1:
            santa_i = 0
        else:
            santa_i += 1
    elif direction == "up":
        if santa_i - 1 < 0:
            santa_i = rows - 1
        else:
            santa_i -= 1
    elif direction == "left":
        if santa_j - 1 < 0:
            santa_j = cols - 1
        else:
            santa_j -= 1
    elif direction == "right":
        if santa_j + 1 > cols - 1:
            santa_j = 0
        else:
            santa_j += 1

    return santa_i, santa_j


def checking_coordinates(i, j, matrix, collected_items, presents_collected):
    if matrix[i][j] == "D":
        collected_items["Christmas decorations"] += 1
        presents_collected += 1
    elif matrix[i][j] == "G":
        collected_items["Gifts"] += 1
        presents_collected += 1
    elif matrix[i][j] == "C":
        collected_items["Cookies"] += 1
        presents_collected += 1

    return collected_items, presents_collected


rows, columns = [int(x) for x in input().split(", ")]
matrix = []
santa_i = 0
santa_j = 0
items_count = 0
collected_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}

for i in range(rows):
    line = input().split()
    for j in range(columns):
        if line[j] == "Y":
            santa_i = i
            santa_j = j
        elif line[j] != ".":
            items_count += 1
    matrix.append(line)

presents_collected = 0
matrix[santa_i][santa_j] = "x"

while True:
    line = input().split("-")
    direction = line[0]
    if direction == "End":
        matrix[santa_i][santa_j] = "Y"
        break
    if presents_collected == items_count:
        print("Merry Christmas!")
        break
    steps = int(line[1])

    for i in range(steps):
        santa_i, santa_j = moving_func(santa_i, santa_j, direction, rows, columns)
        collected_items, presents_collected = checking_coordinates(santa_i, santa_j, matrix, collected_items, presents_collected)
        if presents_collected == items_count:
            break
        matrix[santa_i][santa_j] = "x"
    if presents_collected == items_count:
        print("Merry Christmas!")
        matrix[santa_i][santa_j] = "Y"
        break


print("You've collected:")
for toy, value in collected_items.items():
    print(f"- {value} {toy}")
for i in range(rows):
    print(" ".join(matrix[i]))

