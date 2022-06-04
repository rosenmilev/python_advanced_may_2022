n = int(input())
matrix = []

for _ in range(n):
    line = input()
    matrix.append(line)

searched_symbol = input()
symbol_found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == searched_symbol:
            print((i, j))
            symbol_found = True
            break
    if symbol_found:
        break

if not symbol_found:
    print(f"{searched_symbol} does not occur in the matrix")
