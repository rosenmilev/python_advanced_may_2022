def possible_move_generator(row, col, rows, columns):
    possible_moves = []
    if row - 1 >= 0 and col - 2 >= 0:
        possible_moves.append([row - 1, col - 2])
    if row - 2 >= 0 and col - 1 >= 0:
        possible_moves.append([row - 2, col - 1])
    if row - 2 >= 0 and col + 1 <= columns - 1:
        possible_moves.append([row - 2, col + 1])
    if row - 1 >= 0 and col + 2 <= columns - 1:
        possible_moves.append([row - 1, col + 2])
    if row + 1 <= rows - 1 and col + 2 <= columns - 1:
        possible_moves.append([row + 1, col + 2])
    if row + 2 <= rows - 1 and col + 1 <= columns - 1:
        possible_moves.append([row + 2, col + 1])
    if row + 2 <= rows - 1 and col - 1 >= 0:
        possible_moves.append([row + 2, col - 1])
    if row + 1 <= rows - 1 and col - 2 >= 0:
        possible_moves.append([row + 1, col - 2])

    return possible_moves


def attacked_knights(current_possible_moves, current_play_field):
    successful_attacks = 0
    for move in current_possible_moves:
        r = move[0]
        c = move[1]
        if current_play_field[r][c] == "K":
            successful_attacks += 1

    return successful_attacks


rows = int(input())
play_field = []
knights_positions = []


for row in range(rows):
    line = input()
    current_row = []
    for i in range(len(line)):
        if line[i] == "K":
            knights_positions.append([row, i])
        current_row.append(line[i])
    play_field.append(current_row)

columns = len(play_field[0])
removed_knights = 0

while True:
    max_attacks, knight_to_remove = 0, [0, 0]

    for knight in knights_positions:
        i = knight[0]
        j = knight[1]
        possible_move = possible_move_generator(i, j, rows, columns)
        current_attacks = attacked_knights(possible_move, play_field)
        if current_attacks > max_attacks:
            max_attacks, knight_to_remove = current_attacks, [i, j]

    if max_attacks == 0:
        break
    knights_positions.remove(knight_to_remove)
    play_field[knight_to_remove[0]][knight_to_remove[1]] = "0"
    removed_knights += 1

print(removed_knights)