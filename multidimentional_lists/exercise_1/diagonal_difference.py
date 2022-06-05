rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(len(matrix)):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][rows - i - 1]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))
