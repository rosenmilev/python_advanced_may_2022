rows = int(input())
matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - i - 1])

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
