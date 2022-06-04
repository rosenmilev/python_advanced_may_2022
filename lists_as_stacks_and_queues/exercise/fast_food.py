from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

while orders:
    if food_quantity < orders[0]:
        break
    food_quantity -= orders.popleft()

if orders:
    print("Orders left: ", end="")
    print(*orders, sep=" ")
else:
    print("Orders complete")
