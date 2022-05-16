message = input()

stack = []

for char in message:
    stack.append(char)

reversed_message = ""

while stack:
    reversed_message += stack.pop(-1)

print(reversed_message)
