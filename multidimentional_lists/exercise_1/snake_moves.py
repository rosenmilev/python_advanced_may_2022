from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque([x for x in input()])
snake_path = [[" " for x in range(columns)] for _ in range(rows)]


for i in range(rows):
    if i % 2 == 0:
        for j in range(columns):
            current_element = snake.popleft()
            snake.append(current_element)
            snake_path[i][j] = current_element
    else:
        for j in range(columns - 1, -1, -1):
            current_element = snake.popleft()
            snake.append(current_element)
            snake_path[i][j] = current_element

[print("".join(row)) for row in snake_path]
