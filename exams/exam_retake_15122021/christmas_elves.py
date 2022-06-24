from collections import deque

elfs = deque([int(x) for x in input().split(" ")])
materials = [int(x) for x in input().split(" ")]
total_energy_spent = 0
toys_made = 0
counter = 0

while elfs and materials:
    if elfs[0] < 5:
        elfs.popleft()
        continue

    current_elf = elfs.popleft()
    current_material = materials.pop()

    counter += 1
    toys_to_be_made = 1
    energy_to_spent = current_material
    energy_increase = 1

    if counter % 3 == 0:
        toys_to_be_made = 2
        energy_to_spent *= 2

    if counter % 5 == 0:
        toys_to_be_made = 0
        energy_increase = 0

    if current_elf >= energy_to_spent:
        toys_made += toys_to_be_made
        total_energy_spent += energy_to_spent
        elfs.append(current_elf - energy_to_spent + energy_increase)
    else:
        materials.append(current_material)
        elfs.append(current_elf * 2)

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy_spent}")

if elfs:
    print(f"Elves left: {', '.join([str(x) for x in elfs])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")
