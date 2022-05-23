n, m = [int(x) for x in input().split()]
set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input())

for _ in range(m):
    set_m.add(input())

[print(el) for el in set_n & set_m]
