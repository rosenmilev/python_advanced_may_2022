r, c = [int(x) for x in input().split()]
matrix = []

for i in range(r):
    first_letter = chr(i + 97)
    last_letter = chr(i + 97)
    current_row = []
    for j in range(c):
        middle_letter = chr(97 + j + i)
        current_element = first_letter + middle_letter + last_letter
        current_row.append(current_element)
    matrix.append(current_row)

[print(" ".join(el)) for el in matrix]