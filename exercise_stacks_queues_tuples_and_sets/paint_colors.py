from collections import deque

line = deque(input().split())

colours_found = []

primary = ["red", "yellow", "blue"]
secondary = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

while line:
    if len(line) > 1:
        left_part = line.popleft()
        right_part = line.pop()
        color = left_part + right_part
        color_two = right_part + left_part

        if color in primary or color in secondary:
            colours_found.append(color)
        elif color_two in primary or color_two in secondary:
            colours_found.append(color_two)

        else:
            if len(left_part) > 1:
                left_part = left_part[:-1]

                line.insert(len(line) // 2, left_part)
            if len(right_part) > 1:
                right_part = right_part[:-1]
                line.insert(len(line) // 2, right_part)
    else:
        color = line.pop()

        if color in primary or color in secondary:
            colours_found.append(color)
        else:
            if len(color) > 1:
                color = color[:-1]
                line.insert(len(line) // 2, color)

for color in colours_found:
    if color in secondary:
        if secondary[color][0] not in colours_found or secondary[color][1] not in colours_found:
            colours_found.remove(color)

print(colours_found)
