# rows = int(input())
# matrix = [[num for num in input().split(", ")] for _ in range(rows)]
# flattened_matrix = [num for sublist in matrix for num in sublist]
# print(flattened_matrix)

rows = int(input())
flattened_matrix = []
for _ in range(rows):
    flattened_matrix.extend(int(x) for x in input().split(", "))
print(flattened_matrix)
