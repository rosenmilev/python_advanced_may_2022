# rows, columns = [int(x) for x in input().split(", ")]
# sum_of_columns = {}
#
# for row in range(rows):
#     current_row = [int(x) for x in input().split(" ")]
#     for i in range(len(current_row)):
#         if i not in sum_of_columns:
#             sum_of_columns[i] = 0
#         sum_of_columns[i] += current_row[i]
#
# [print(value, end="\n") for value in sum_of_columns.values()]

rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

for j in range(columns):
    result = 0
    for i in range(rows):
        result += matrix[i][j]
    print(result)
