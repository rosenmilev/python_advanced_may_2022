def is_vip(guest):
    return guest[0].isdigit()


vip = set()
regular = set()

n = int(input())
for _ in range(n):
    guest = input()
    if is_vip(guest):
        vip.add(guest)
    else:
        regular.add(guest)

while True:
    guests_came_to_party = input()

    if guests_came_to_party == "END":
        break

    if guests_came_to_party in vip:
        vip.remove(guests_came_to_party)
    elif guests_came_to_party in regular:
        regular.remove(guests_came_to_party)

print(len(vip) + len(regular))

if vip:
    [print(cur_guest) for cur_guest in sorted(vip)]

if regular:
    [print(cur_guest) for cur_guest in sorted(regular)]
