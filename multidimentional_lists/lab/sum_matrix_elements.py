rows, columns = [int(x) for x in input().split(", ")]
matrix = []
result = 0

for row in range(rows):
    current_numbers = [int(x) for x in input().split(", ")]
    result += sum(current_numbers)
    matrix.append(current_numbers)

print(result)
print(matrix)
