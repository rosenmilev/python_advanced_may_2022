# Primary diagonal

n = int(input())
matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

result = 0

for i in range(n):
    result += matrix[i][i]

print(result)
#
# Secondary diagonal
#
# n = int(input())
# matrix = []
# result = 0
# for _ in range(n):
#     nums = [int(el) for el in input().split()]
#     matrix.append(nums)
#
# for i in range(n):
#     result += matrix[i][n - i - 1]
# print(result)
