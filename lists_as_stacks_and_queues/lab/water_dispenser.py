from collections import deque

"""
First we read the amount of water and the names of the people who want water and add them to the queue until we receive
"Start"

On the following lines we receive some commands:

(int) - check the current amount of water and, if enough, print the person's name and remove him from the queue
else print "{Person name} must wait"

"refill {liters}" - adding {liters} to the amount of water

"End" - printing the remaining amount of water
"""

water_quantity = int(input())
queue = deque()

while True:
    name = input()

    if name == "Start":
        break

    queue.append(name)

while True:

    command = input()

    if command == "End":
        print(f"{water_quantity} liters left")
        break

    elif command.startswith("refill "):
        command = command.split(" ")
        water_quantity += int(command[1])

    else:
        if int(command) <= water_quantity:
            print(f"{queue.popleft()} got water")
            water_quantity -= int(command)
        else:
            print(f"{queue.popleft()} must wait")
