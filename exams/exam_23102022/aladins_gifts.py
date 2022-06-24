from collections import deque


def check_for_gifts(material, magic_level):
    def check_if_in_range(mat, mag):
        if 100 > mat + mag or mat + mag > 499:
            return False
        else:
            return True

    gift = False
    current_magic_level = material + magic_level

    if current_magic_level < 100:
        if current_magic_level % 2 == 0:
            material *= 2
            magic_level *= 3
        else:
            material *= 2
            magic_level *= 2
        if check_if_in_range(material, magic_level):
            gift = check_for_gifts(material, magic_level)
        else:
            return False

    elif 100 <= current_magic_level <= 199:
        gift = "Gemstone"
    elif 200 <= current_magic_level <= 299:
        gift = "Porcelain Sculpture"
    elif 300 <= current_magic_level <= 399:
        gift = "Gold"
    elif 400 <= current_magic_level <= 499:
        gift = "Diamond Jewellery"
    elif current_magic_level > 499:
        material /= 2
        magic_level /= 2
        if check_if_in_range(material, magic_level):
            gift = check_for_gifts(material, magic_level)
        else:
            return False

    return gift


materials = [int(x) for x in input().split(" ")]
magic_levels = deque([int(x) for x in input().split(" ")])
all_gifts_crafted = False
recursion_counter = 1
crafted_gifts = {
    "Diamond Jewellery": 0,
    "Gemstone": 0,
    "Gold": 0,
    "Porcelain Sculpture": 0,
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    crafted_gift = check_for_gifts(current_material, current_magic_level)
    if crafted_gift:
        crafted_gifts[crafted_gift] += 1
    if crafted_gifts["Gemstone"] and crafted_gifts["Porcelain Sculpture"] or crafted_gifts["Gold"] and crafted_gifts["Diamond Jewellery"]:
        all_gifts_crafted = True


if all_gifts_crafted:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
if crafted_gifts:
    for key, value in crafted_gifts.items():
        if value:
            print(f"{key}: {value}")
