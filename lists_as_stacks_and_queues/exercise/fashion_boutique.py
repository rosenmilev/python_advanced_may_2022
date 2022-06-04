clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack_capacity = rack_capacity
rack_number = 1

while clothes:
    current_cloth = clothes.pop()
    if current_rack_capacity < current_cloth:
        rack_number += 1
        current_rack_capacity = rack_capacity
    current_rack_capacity -= current_cloth

print(rack_number)
