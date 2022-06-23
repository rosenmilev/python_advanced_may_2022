from collections import deque

ramen_bowls = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while ramen_bowls and customers:
    current_bowl = ramen_bowls[-1]
    current_customer = customers[0]

    if current_bowl == current_customer:
        ramen_bowls.pop()
        customers.popleft()

    elif current_bowl > current_customer:
        ramen_bowls[-1] -= customers.popleft()

    elif current_bowl < current_customer:
        customers[0] -= ramen_bowls.pop()

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print("Bowls of ramen left: ", end="")
        print(*ramen_bowls, sep=", ")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left: ", end="")
    print(*customers, sep=", ")
