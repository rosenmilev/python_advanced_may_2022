from collections import deque

materials = [int(x) for x in input().split(" ")]
magic = deque([int(x) for x in input().split(" ")])
presents_prices = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
presents_crafted = {}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()

    if current_material == 0 or current_magic == 0:
        if current_material != 0:
            materials.append(current_material)
        if current_magic != 0:
            magic.appendleft(current_magic)
        continue

    total_magic_level = current_magic * current_material

    if total_magic_level in presents_prices:
        if presents_prices[total_magic_level] not in presents_crafted:
            presents_crafted[presents_prices[total_magic_level]] = 0
        presents_crafted[presents_prices[total_magic_level]] += 1
        continue

    if total_magic_level < 0:
        material_to_add = current_material + current_magic
        materials.append(material_to_add)
    elif total_magic_level > 0:
        material_to_add = current_material + 15
        materials.append(material_to_add)

if ("Doll" in presents_crafted and "Train" in presents_crafted) or ("Teddy bear" in presents_crafted and "Bicycle" in presents_crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: ", end="")
    print(*reversed(materials), sep=", ")
if magic:
    print("Magic left: ", end="")
    print(*magic, sep=", ")

presents_crafted = sorted(presents_crafted.items(), key=lambda x: x[0])
for toy, number in presents_crafted:
    print(f"{toy}: {number}")
