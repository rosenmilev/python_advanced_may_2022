from collections import deque


chocolate = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while True:
    if not chocolate or not cups_of_milk or milkshakes == 5:
        break

    current_chocolate = chocolate.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 or current_cup_of_milk <= 0:
        if current_chocolate > 0:
            chocolate.append(current_chocolate)
        elif current_cup_of_milk > 0:
            cups_of_milk.appendleft(current_cup_of_milk)
        continue

    if current_chocolate == current_cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(current_cup_of_milk)
        current_chocolate -= 5
        chocolate.append(current_chocolate)



if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")


print("Chocolate: ", end="")

if chocolate:
    print(*chocolate, sep=", ")
else:
    print("empty")

print("Milk: ", end="")
if cups_of_milk:
    print(*cups_of_milk, sep=", ")
else:
    print("empty")
    