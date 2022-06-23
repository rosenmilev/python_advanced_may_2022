from collections import deque


def honey_making_process(current_symbol, current_bee, current_nectar):
    result = 0
    if current_symbol == "+":
        result = abs(current_bee + current_nectar)
    elif current_symbol == "-":
        result = abs(current_bee - current_nectar)
    elif current_symbol == "*":
        result = abs(current_bee * current_nectar)
    elif current_symbol == "/":
        if current_bee == 0 and current_nectar == 0:
            result = 0
        else:
            result = abs(current_bee / current_nectar)
    return result


bees = deque([int(x) for x in input().split(" ")])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey_made = 0
bee_collected = True

while bees and nectar:
    cur_bee = bees[0]
    cur_nectar = nectar.pop()

    if cur_nectar >= cur_bee:
        honey_made += honey_making_process(symbols.popleft(), bees.popleft(), cur_nectar)

print(f"Total honey made: {honey_made}")
if bees:
    print("Bees left: ", end="")
    print(*bees, sep=", ")
if nectar:
    print("Nectar left: ", end="")
    print(*nectar, sep=", ")
