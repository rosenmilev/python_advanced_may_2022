from collections import deque

n = int(input())
petrol_pumps = deque()
tank = 0

for _ in range(n):
    petrol_pumps.append([int(x) for x in input().split()])

for i in range(len(petrol_pumps)):
    tank = 0
    failed_to_reach = False

    for pump in petrol_pumps:
        petrol = pump[0]
        distance = pump[1]
        if tank + petrol >= distance:
            tank = petrol + tank - distance
        else:
            failed_to_reach = True
            break
    if failed_to_reach:
        petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(i)
        break
