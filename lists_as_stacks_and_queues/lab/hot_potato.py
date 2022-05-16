from collections import deque

"""
Adding children names to queue
Reading toss number

Creating counter

Adding children names until counter == toss number and repeating until 1 child is left.

"""
queue = deque(input().split(" "))
toss_number = int(input())
counter = 0

while len(queue) > 1:
    counter += 1
    current_child = queue.popleft()
    if counter < toss_number:
        queue.append(current_child)
    else:
        print(f"Removed {current_child}")
        counter = 0

print(f"Last is {queue.popleft()}")
