n = int(input())
set_of_names = set()

for _ in range(n):
    set_of_names.add(input())

print(*set_of_names, sep="\n")
