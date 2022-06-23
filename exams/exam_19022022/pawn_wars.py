def player_to_move(current_move):
    if current_move == "White":
        return "Black"
    elif current_move == "Black":
        return "White"


def check_diagonals(w_i, w_j, b_i, b_j, current_move):
    if current_move == "White":
        if (w_i - 1, w_j - 1) == (b_i, b_j) or (w_i - 1, w_j + 1) == (b_i, b_j):
            return f"{columns[b_j]}{8 - b_i}"
    elif current_move == "Black":
        if (b_i + 1, b_j - 1) == (w_i, w_j) or (b_i + 1, b_j + 1) == (w_i, w_j):
            return f"{columns[w_j]}{8 - w_i}"


def move(w_i, w_j, b_i, b_j, current_move):
    promoted = ""
    if current_move == "White":
        w_i -= 1
        if w_i == 0:
            promoted = f"{columns[w_j]}{8 - w_i}"
    elif current_move == "Black":
        b_i += 1
        if b_i == 7:
            promoted = f"{columns[b_j]}{8 - b_i}"
    return w_i, b_i, promoted


columns = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

matrix = []
w_i = 0
w_j = 0
b_i = 0
b_j = 0
is_promoted = False

for i in range(8):
    line = input().split(" ")
    for j in range(8):
        if line[j] == "w":
            w_i = i
            w_j = j
        elif line[j] == "b":
            b_i = i
            b_j = j
    matrix.append(line)

current_move = "White"

while True:
    capture = check_diagonals(w_i, w_j, b_i, b_j, current_move)
    if capture:
        print(f"Game over! {current_move} win, capture on {capture}.")
        break
    w_i, b_i, is_promoted = move(w_i, w_j, b_i, b_j, current_move)
    if is_promoted:
        print(f"Game over! {current_move} pawn is promoted to a queen at {is_promoted}.")
        break

    current_move = player_to_move(current_move)
